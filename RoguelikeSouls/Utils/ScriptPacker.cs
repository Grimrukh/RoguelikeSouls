using SoulsFormats;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Xml;

namespace NightfallMod
{
    public class ScriptPacker
    {
        class ScriptPackerException : Exception
        {
            public ScriptPackerException(string message) : base(message) { }
        }

        static IBinder ReadIBinder(string name)
        {
            if (BND4.Is(name))
                return BND4.Read(name);
            else
                return BND3.Read(name);
        }

        static byte[] compiledLuaStartBytes = new byte[]
        {
            0x1B, 0x4C, 0x75, 0x61,
            0x50, 0x01, 0x04,
        };

        static bool IsCompiledLua(byte[] bytes)
        {
            for (int i = 0; i < compiledLuaStartBytes.Length; i++)
            {
                if (bytes[i] != compiledLuaStartBytes[i])
                    return false;
            }

            return true;
        }

        //const string EXT_TALK_SCRIPT_LIST = @".talks.txt";
        //const string EXT_AI_GOAL_LIST = @"luainfo_";
        //const string EXT_AI_SCRIPT_LIST = @".luascripts.txt";
        //const string EXT_LUA_GLOBALS_LIST = @"luagnl_";
        const string EXT_BINDER_HEADER = @"BinderHeader.xml";
        const string EXT_SCRIPT_INCLUDE_LIST = @"AIScriptIncludeList.xml";
        const string EXT_TALK_INCLUDE_LIST = @"TalkScriptIncludeList.xml";

        //struct LuaScriptInfo
        //{
        //    public List<string> IncludeInMaps = new List<string>();
        //    public List<LUAINFO.Goal> Goals = new List<LUAINFO.Goal>();
        //}


        static Dictionary<string, List<string>> ReadScriptIncludeListXML(string xmlName)
        {
            var result = new Dictionary<string, List<string>>();

            XmlDocument xml = new XmlDocument();
            xml.Load(xmlName);

            foreach (XmlNode scriptNode in xml.SelectNodes("script_include_list/script"))
            {
                var scriptName = scriptNode.Attributes["name"].Value;

                if (!result.ContainsKey(scriptName))
                    result.Add(scriptName, new List<string>());

                foreach (XmlNode luabndNode in scriptNode.SelectNodes("bnd"))
                {
                    var luabndName = luabndNode.Attributes["name"].Value;

                    if (!result[scriptName].Contains(luabndName))
                        result[scriptName].Add(luabndName);
                }
            }

            return result;
        }

        static void WriteScriptIncludeListToXML(Dictionary<string, List<string>> includeList, string xmlName)
        {
            XmlWriterSettings xws = new XmlWriterSettings()
            {
                Indent = true,
            };

            XmlWriter xw = XmlWriter.Create(xmlName, xws);

            xw.WriteStartElement("script_include_list");
            {
                foreach (var kvp in includeList.OrderBy(k => k.Key))
                {
                    xw.WriteStartElement("script");
                    {
                        xw.WriteAttributeString("name", kvp.Key);

                        foreach (var luabndName in kvp.Value.OrderBy(lb => lb))
                        {
                            xw.WriteStartElement("bnd");
                            {
                                xw.WriteAttributeString("name", luabndName);
                            }
                            xw.WriteEndElement();
                        }
                    }
                    xw.WriteEndElement();
                }
            }
            xw.WriteEndElement();
            xw.Close();
        }

        static List<string> FixedScriptListOrder = new List<string>()
        {
            "nf_goal_list",
            "nf_logic_list",
            "ai_define",
            "event_list",
            "common_battle_func",
            "common_logic_func",
            "nf_common_func2",
            "common_func",
            "approach_target",
            "attack",
            "attack_tunable_spin",
            "combo_attack",
            "combo_attack_success_angle180",
            "combo_attack_tunable_spin",
            "combo_final",
            "combo_repeat",
            "combo_repeat_success_angle180",
            "come_down",
            "common_attack",
            "goal_list_dlc",
            "continue_attack",
            "default_logic",
            "door_act",
            "fall",
            "gaurd_break_attack",
            "if",
            "ladder_act",
            "landing",
            "non_battle_act",
            "nonspinning_attack",
            "normal",
            "npc_subgoals",
            "obj_act",
            "specialTurn",
            "team_call_help",
            "team_reply_help",
            "template",
            "top_goal",
            "turn",
            "turnaround",
            "use_item",
            "walk_around",
            "keep_dist_yaxis",
            "pursuit",
            "approach_setting_direction",
            "nonspinning_combo_attack",
            "nonspinning_combo_repeat",
            "nonspinning_combo_final",
            "combo_tunable_success_angle180",
            "gaurd_break_tunable",
        };

        static int GetOrderOfScriptName(string scriptName)
        {
            scriptName = Utils.GetShortIngameFileName(scriptName).ToLower();
            if (FixedScriptListOrder.Contains(scriptName))
                return FixedScriptListOrder.IndexOf(scriptName);
            else if (!char.IsDigit(scriptName[0]))
                return 8888888;
            else
                return 9999999;
        }

        public enum PackOperation
        {
            Unpack,
            UnpackPTDE,
            Repack
        }

        public static void DoPackOperation(string scriptDir, string unpackedScriptDir, PackOperation packOperation)
        {
            var script = scriptDir;
            var script_talk = Utils.Frankenpath(scriptDir, @"\talk\");
            var script_src = unpackedScriptDir;
            var script_src_scripts_lua = Utils.Frankenpath(unpackedScriptDir, @"\AIScriptLua\");
            var script_src_scripts_bin = Utils.Frankenpath(unpackedScriptDir, @"\AIScriptBin\");
            var script_src_talk = Utils.Frankenpath(unpackedScriptDir, @"\TalkScriptEsd\");
            var script_src_header = Utils.Frankenpath(unpackedScriptDir, $@"\{EXT_BINDER_HEADER}");

            void DO_UNPACK(bool isPTDE)
            {
                if (Directory.Exists(script))
                {
                    if (!Directory.Exists(script_src))
                        Directory.CreateDirectory(script_src);

                    if (!Directory.Exists(script_src_scripts_lua))
                        Directory.CreateDirectory(script_src_scripts_lua);

                    if (!Directory.Exists(script_src_scripts_bin))
                        Directory.CreateDirectory(script_src_scripts_bin);

                    if (!Directory.Exists(script_src_talk))
                        Directory.CreateDirectory(script_src_talk);

                    bool hasSavedBinderHeader = false;

                    Dictionary<string, List<string>> mapsThatScriptsAreIn = new Dictionary<string, List<string>>();
                    Dictionary<string, List<string>> mapsThatTalksAreIn = new Dictionary<string, List<string>>();

                    foreach (var luabndName in Directory.GetFiles(script, isPTDE ? "*.luabnd" : "*.luabnd.dcx"))
                    {
                        var mapName = Utils.GetShortIngameFileName(luabndName);

                        //var scriptList = new List<string>();

                        var luabnd = ReadIBinder(luabndName);

                        if (!hasSavedBinderHeader)
                        {
                            YBinder.WriteHeaderToXML(luabnd, script_src_header);
                            hasSavedBinderHeader = true;
                        }

                        foreach (var f in luabnd.Files)
                        {
                            if (f.Name.ToUpper().EndsWith(".LUA"))
                            {
                                var shortLuaName = Utils.GetShortIngameFileName(f.Name);

                                if (IsCompiledLua(f.Bytes))
                                {
                                    File.WriteAllBytes(Utils.Frankenpath(script_src_scripts_bin, $"{shortLuaName}.bin"), f.Bytes);
                                }
                                else
                                {
                                    File.WriteAllBytes(Utils.Frankenpath(script_src_scripts_lua, $"{shortLuaName}.lua"), f.Bytes);
                                }

                                //if (!scriptList.Contains(shortLuaName))
                                //    scriptList.Add(shortLuaName);

                                if (!mapsThatScriptsAreIn.ContainsKey(shortLuaName))
                                {
                                    mapsThatScriptsAreIn.Add(shortLuaName, new List<string>());
                                }

                                if (!mapsThatScriptsAreIn[shortLuaName].Contains(mapName))
                                    mapsThatScriptsAreIn[shortLuaName].Add(mapName);
                            }
                            //else if (mapName.ToLower() == "aicommon" && f.Name.ToUpper().EndsWith(".LUAGNL"))
                            //{
                            //    var gnl = LUAGNL.Read(f.Bytes);
                            //    gnl.ToXML(Utils.Frankenpath(script_src, $"{EXT_LUA_GLOBALS_LIST}{mapName}.xml"));
                            //}
                            //else if (mapName.ToLower() == "aicommon" && f.Name.ToUpper().EndsWith(".LUAINFO"))
                            //{
                            //    var info = LUAINFO.Read(f.Bytes);
                            //    info.ToXML(Utils.Frankenpath(script_src, $"{EXT_AI_GOAL_LIST}{mapName}.xml"));
                            //}
                        }

                        //File.WriteAllLines(Utils.Frankenpath(script_src, $"{mapName}{EXT_AI_SCRIPT_LIST}"), scriptList);
                    }

                    WriteScriptIncludeListToXML(mapsThatScriptsAreIn, Utils.Frankenpath(script_src, EXT_SCRIPT_INCLUDE_LIST));

                    foreach (var talkesdbndName in Directory.GetFiles(script_talk, isPTDE ? "*.talkesdbnd" : "*.talkesdbnd.dcx"))
                    {
                        var mapName = Utils.GetShortIngameFileName(talkesdbndName);
                        var talkesdbnd = ReadIBinder(talkesdbndName);

                        if (!hasSavedBinderHeader)
                        {
                            YBinder.WriteHeaderToXML(talkesdbnd, script_src_header);
                            hasSavedBinderHeader = true;
                        }

                        //var talkList = new List<string>();
                        foreach (var f in talkesdbnd.Files)
                        {
                            var shortTalkName = Utils.GetShortIngameFileName(f.Name);
                            File.WriteAllBytes(Utils.Frankenpath(script_src_talk, $"{shortTalkName}.esd"), f.Bytes);

                            //if (!talkList.Contains(shortTalkName))
                            //    talkList.Add(shortTalkName);

                            if (!mapsThatTalksAreIn.ContainsKey(shortTalkName))
                            {
                                mapsThatTalksAreIn.Add(shortTalkName, new List<string>());
                            }

                            if (!mapsThatTalksAreIn[shortTalkName].Contains(mapName))
                                mapsThatTalksAreIn[shortTalkName].Add(mapName);
                        }

                        //File.WriteAllLines(Utils.Frankenpath(script_src, $"{Utils.GetShortIngameFileName(talkesdbndName)}{EXT_TALK_SCRIPT_LIST}"), talkList);
                    }

                    WriteScriptIncludeListToXML(mapsThatTalksAreIn, Utils.Frankenpath(script_src, EXT_TALK_INCLUDE_LIST));
                }
                else
                {
                    Console.Write("Could not find 'script' folder within game directory to unpack");
                }
            }

            void DO_REPACK(bool isPTDE)
            {
                if (Directory.Exists(script_src))
                {
                    if (!Directory.Exists(script))
                        Directory.CreateDirectory(script);

                    if (!Directory.Exists(script_talk))
                        Directory.CreateDirectory(script_talk);

                    IBinder NewBinder()
                    {
                        return YBinder.CreateFromExampleHeader(script_src_header);
                    }

                    Dictionary<string, byte[]> luaScripts = new Dictionary<string, byte[]>();

                    foreach (var f in Directory.GetFiles(script_src_scripts_lua, "*.lua"))
                    {
                        var fs = Utils.GetShortIngameFileName(f.ToLower());
                        if (!luaScripts.ContainsKey(fs))
                            luaScripts.Add(fs, File.ReadAllBytes(f));
                    }

                    foreach (var f in Directory.GetFiles(script_src_scripts_bin, "*.bin"))
                    {
                        var fs = Utils.GetShortIngameFileName(f.ToLower());
                        if (!luaScripts.ContainsKey(fs))
                            luaScripts.Add(fs, File.ReadAllBytes(f));
                    }

                    Dictionary<string, byte[]> talkEsds = new Dictionary<string, byte[]>();

                    foreach (var f in Directory.GetFiles(script_src_talk, "*.esd"))
                    {
                        var fs = Utils.GetShortIngameFileName(f.ToLower());
                        if (!talkEsds.ContainsKey(fs))
                            talkEsds.Add(fs, File.ReadAllBytes(f));
                    }

                    Dictionary<string, IBinder> map_luabnds = new Dictionary<string, IBinder>();
                    Dictionary<string, IBinder> map_talkesdbnds = new Dictionary<string, IBinder>();
                    Dictionary<string, LUAGNL> map_luagnls = new Dictionary<string, LUAGNL>();
                    Dictionary<string, LUAINFO> map_luainfos = new Dictionary<string, LUAINFO>();
                    //Dictionary<string, List<string>> map_luaScriptLists = new Dictionary<string, List<string>>();
                    //Dictionary<string, List<string>> map_talkEsdLists = new Dictionary<string, List<string>>();

                    //List<string> legacyMasterScriptIndexer = new List<string>();

                    //Dictionary<string, List<string>> luaFilesToIncludeInEachmap = new Dictionary<string, List<string>>();

                    luaScripts = luaScripts.OrderBy(kvp => GetOrderOfScriptName(kvp.Key)).ToDictionary(kvp => kvp.Key, kvp => kvp.Value);

                    var luaScriptNameIndexer = luaScripts.Keys.ToList();

                    void AddLuaScriptToMap(string map, string luaScriptName)
                    {
                        //luaScriptName = luaScriptName.ToLower();

                        if (luaScripts.ContainsKey(luaScriptName.ToLower()))
                        {
                            if (!map_luabnds.ContainsKey(map))
                                map_luabnds.Add(map, NewBinder());

                            int nextScriptID = luaScriptNameIndexer.IndexOf(luaScriptName.ToLower()) + 1000;

                            map_luabnds[map].Files.Add(new BinderFile(Binder.FileFlags.x40, nextScriptID, luaScriptName + ".lua", luaScripts[luaScriptName.ToLower()]));
                        }
                        else
                        {
                            throw new ScriptPackerException($"Tried to add script '{luaScriptName}' to map '{map}' but the script file did not exist.");
                        }
                    }

                    void AddTalkESDToMap(string map, string talkEsdName)
                    {
                        //talkEsdName = talkEsdName.ToLower();

                        if (talkEsds.ContainsKey(talkEsdName.ToLower()))
                        {
                            if (!map_talkesdbnds.ContainsKey(map))
                                map_talkesdbnds.Add(map, NewBinder());

                            map_talkesdbnds[map].Files.Add(new BinderFile(Binder.FileFlags.x40, map_talkesdbnds[map].Files.Count, talkEsdName + ".esd", talkEsds[talkEsdName.ToLower()]));
                        }
                        else
                        {
                            throw new ScriptPackerException($"Tried to add talk script '{talkEsdName}' to map '{map}' but the script file did not exist.");
                        }
                    }

                    //void ProcessLuaGlobals(string fileName)
                    //{
                    //    string map = Utils.GetShortIngameFileName(fileName);
                    //    var luagnl = YLUAGNL.FromXML(fileName);

                    //    if (!map_luagnls.ContainsKey(map))
                    //        map_luagnls.Add(map, luagnl);
                    //    else
                    //        map_luagnls[map] = luagnl;
                    //}

                    //void ProcessGoalList(string fileName)
                    //{
                    //    string map = Utils.GetShortIngameFileName(fileName);

                    //    var luainfo = YLUAINFO.FromXML(fileName);

                    //    if (!map_luainfos.ContainsKey(map))
                    //        map_luainfos.Add(map, luainfo);
                    //    else
                    //        map_luainfos[map] = luainfo;
                    //}


                    var scriptListDict = ReadScriptIncludeListXML(Utils.Frankenpath(script_src, EXT_SCRIPT_INCLUDE_LIST));

                    foreach (var kvp in scriptListDict)
                    {
                        foreach (var map in kvp.Value)
                        {
                            AddLuaScriptToMap(map, kvp.Key);
                        }
                    }

                    var talkListDict = ReadScriptIncludeListXML(Utils.Frankenpath(script_src, EXT_TALK_INCLUDE_LIST));

                    foreach (var kvp in talkListDict)
                    {
                        foreach (var map in kvp.Value)
                        {
                            AddTalkESDToMap(map, kvp.Key);
                        }
                    }

                    //ProcessGoalList(Utils.Frankenpath(script_src, $"{EXT_LUA_GLOBALS_LIST}aiCommon.xml"));
                    //ProcessLuaGlobals(Utils.Frankenpath(script_src, $"{EXT_AI_GOAL_LIST}aiCommon.xml"));

                    foreach (var kvp in map_luabnds)
                    {
                        if (map_luagnls.ContainsKey(kvp.Key))
                        {
                            map_luabnds[kvp.Key].Files.Add(new BinderFile(Binder.FileFlags.x40, 1000000, $"{kvp.Key}.luagnl", map_luagnls[kvp.Key].Write()));
                        }

                        if (map_luainfos.ContainsKey(kvp.Key))
                        {
                            map_luabnds[kvp.Key].Files.Add(new BinderFile(Binder.FileFlags.x40, 1000001, $"{kvp.Key}.luainfo", map_luainfos[kvp.Key].Write()));
                        }

                        kvp.Value.Files = kvp.Value.Files.OrderBy(f => f.ID).ToList();

                        if (kvp.Value is BND3 asBND3)
                        {
                            var luabndName = $@"\{kvp.Key}.luabnd{(asBND3.Compression != DCX.Type.None ? ".dcx" : "")}";

                            luabndName = Utils.Frankenpath(script, luabndName);

                            //if (File.Exists(luabndName) && !File.Exists(luabndName + ".bak"))
                            //    File.Copy(luabndName, luabndName + ".bak");

                            asBND3.Write(luabndName);
                        }
                        else if (kvp.Value is BND4 asBND4)
                        {
                            var luabndName = $@"\{kvp.Key}.luabnd{(asBND4.Compression != DCX.Type.None ? ".dcx" : "")}";

                            luabndName = Utils.Frankenpath(script, luabndName);

                            //if (File.Exists(luabndName) && !File.Exists(luabndName + ".bak"))
                            //    File.Copy(luabndName, luabndName + ".bak");

                            asBND4.Write(luabndName);
                        }
                    }

                    foreach (var kvp in map_talkesdbnds)
                    {
                        if (kvp.Value is BND3 asBND3)
                        {
                            var talkesdbndName = $@"\{kvp.Key}.talkesdbnd{(asBND3.Compression != DCX.Type.None ? ".dcx" : "")}";

                            talkesdbndName = Utils.Frankenpath(script_talk, talkesdbndName);

                            //if (File.Exists(talkesdbndName) && !File.Exists(talkesdbndName + ".bak"))
                            //    File.Copy(talkesdbndName, talkesdbndName + ".bak");

                            asBND3.Write(talkesdbndName);
                        }
                        else if (kvp.Value is BND4 asBND4)
                        {
                            var talkesdbndName = $@"\{kvp.Key}.talkesdbnd{(asBND4.Compression != DCX.Type.None ? ".dcx" : "")}";

                            talkesdbndName = Utils.Frankenpath(script_talk, talkesdbndName);

                            //if (File.Exists(talkesdbndName) && !File.Exists(talkesdbndName + ".bak"))
                            //    File.Copy(talkesdbndName, talkesdbndName + ".bak");

                            asBND4.Write(talkesdbndName);
                        }
                    }
                }
                else
                {
                    throw new ScriptPackerException($"Could not find '{script_src}' folder.");
                }
            }


            if (packOperation == PackOperation.UnpackPTDE)
            {
                DO_UNPACK(isPTDE: true);
            }
            else if (packOperation == PackOperation.Unpack)
            {
                DO_UNPACK(isPTDE: false);
            }
            else if (packOperation == PackOperation.Repack)
            {
                DO_REPACK(isPTDE: false);
            }
            else
            {
                throw new NotImplementedException();
            }
        }

        static class YBinder
        {
            public static void WriteHeaderToXML(IBinder bnd, string xmlName)
            {
                var xws = new XmlWriterSettings();
                xws.Indent = true;
                var xw = XmlWriter.Create(xmlName, xws);

                if (bnd is BND3 asBND3)
                {
                    xw.WriteStartElement("bnd3-header");

                    xw.WriteElementString("compression", asBND3.Compression.ToString());
                    xw.WriteElementString("version", asBND3.Timestamp);
                    xw.WriteElementString("format", asBND3.Format.ToString());
                    xw.WriteElementString("bigendian", asBND3.BigEndian.ToString());
                    xw.WriteElementString("bitbigendian", asBND3.Unk1.ToString());
                    xw.WriteElementString("unk18", $"0x{asBND3.Unk2:X}");
                    //YBinder.WriteBinderFiles(bnd, xw, targetDir);
                }
                else if (bnd is BND4 asBND4)
                {
                    xw.WriteStartElement("bnd4-header");

                    //xw.WriteElementString("filename", sourceName);
                    xw.WriteElementString("compression", asBND4.Compression.ToString());
                    xw.WriteElementString("version", asBND4.Timestamp);
                    xw.WriteElementString("format", asBND4.Format.ToString());
                    xw.WriteElementString("bigendian", asBND4.BigEndian.ToString());
                    //xw.WriteElementString("bitbigendian", asBND4.Flag1.ToString());
                    xw.WriteElementString("unicode", asBND4.Unicode.ToString());
                    xw.WriteElementString("extended", $"0x{asBND4.Extended:X2}");
                    xw.WriteElementString("unk04", asBND4.Flag1.ToString());
                    xw.WriteElementString("unk05", asBND4.Flag2.ToString());
                }
                else
                {
                    throw new NotImplementedException();
                }



                xw.WriteEndElement();
                xw.Close();
            }

            public static IBinder CreateFromExampleHeader(string xmlName)
            {
                var xml = new XmlDocument();
                xml.Load(xmlName);

                if (xml.DocumentElement.Name == "bnd3-header")
                {
                    var bnd = new BND3();

                    Enum.TryParse(xml.SelectSingleNode("bnd3-header/compression")?.InnerText ?? "None", out bnd.Compression);

                    bnd.Timestamp = xml.SelectSingleNode("bnd3-header/version")?.InnerText ?? "07D7R6";
                    string strFormat = xml.SelectSingleNode("bnd3-header/format")?.InnerText ?? "x2E";
                    string strBigEndian = xml.SelectSingleNode("bnd3-header/bigendian")?.InnerText ?? "False";
                    string strBitBigEndian = xml.SelectSingleNode("bnd3-header/bitbigendian")?.InnerText ?? "False";
                    string strUnk18 = xml.SelectSingleNode("bnd3-header/unk18")?.InnerText ?? "0x0";

                    try
                    {
                        bnd.Format = (Binder.Format)Enum.Parse(typeof(Binder.Format), strFormat);
                    }
                    catch
                    {
                        throw new ScriptPackerException($"Could not parse format: {strFormat}\nFormat must be a comma-separated list of flags.");
                    }

                    if (!bool.TryParse(strBigEndian, out bool bigEndian))
                        throw new ScriptPackerException($"Could not parse big-endianness: {strBigEndian}\nBig-endianness must be true or false.");
                    bnd.BigEndian = bigEndian;

                    if (!bool.TryParse(strBitBigEndian, out bool bitBigEndian))
                        throw new ScriptPackerException($"Could not parse bit big-endianness: {strBitBigEndian}\nBit big-endianness must be true or false.");
                    bnd.Unk1 = bitBigEndian;

                    try
                    {
                        bnd.Unk2 = Convert.ToInt32(strUnk18, 16);
                    }
                    catch
                    {
                        throw new ScriptPackerException($"Could not parse unk18: {strUnk18}\nUnk18 must be a hex value.");
                    }

                    return bnd;
                }
                else if (xml.DocumentElement.Name == "bnd4-header")
                {
                    var bnd = new BND4();

                    //string filename = xml.SelectSingleNode("bnd4-header/filename").InnerText;
                    Enum.TryParse(xml.SelectSingleNode("bnd4-header/compression")?.InnerText ?? "None", out bnd.Compression);
                    bnd.Timestamp = xml.SelectSingleNode("bnd4-header/version").InnerText;
                    bnd.Format = (Binder.Format)Enum.Parse(typeof(Binder.Format), xml.SelectSingleNode("bnd4-header/format").InnerText);
                    bnd.BigEndian = bool.Parse(xml.SelectSingleNode("bnd4-header/bigendian").InnerText);
                    //bnd.BitBigEndian = bool.Parse(xml.SelectSingleNode("bnd4-header/bitbigendian").InnerText);
                    bnd.Unicode = bool.Parse(xml.SelectSingleNode("bnd4-header/unicode").InnerText);
                    bnd.Extended = Convert.ToByte(xml.SelectSingleNode("bnd4-header/extended").InnerText, 16);
                    bnd.Flag1 = bool.Parse(xml.SelectSingleNode("bnd4-header/unk04").InnerText);
                    bnd.Flag2 = bool.Parse(xml.SelectSingleNode("bnd4-header/unk05").InnerText);
                    //YBinder.ReadBinderFiles(bnd, xml.SelectSingleNode("bnd4/files"), sourceDir);

                    return bnd;
                }
                throw new ScriptPackerException("Invalid BND header type");
            }
        }

        public static class Utils
        {
            public static string Frankenpath(params string[] pathParts)
            {
                StringBuilder sb = new StringBuilder();

                for (int i = 0; i < pathParts.Length; i++)
                {
                    sb.Append(pathParts[i].Trim('\\'));
                    if (i < pathParts.Length - 1)
                        sb.Append('\\');
                }

                return sb.ToString();
            }

            public static string GetShortIngameFileName(string fileName)
            {
                return GetFileNameWithoutAnyExtensions(GetFileNameWithoutDirectoryOrExtension(fileName));
            }

            private static readonly char[] _dirSep = new char[] { '\\', '/' };
            public static string GetFileNameWithoutDirectoryOrExtension(string fileName)
            {
                if (fileName.EndsWith("\\") || fileName.EndsWith("/"))
                    fileName = fileName.TrimEnd(_dirSep);

                if (fileName.Contains("\\") || fileName.Contains("/"))
                    fileName = fileName.Substring(fileName.LastIndexOfAny(_dirSep) + 1);

                if (fileName.Contains("."))
                    fileName = fileName.Substring(0, fileName.LastIndexOf('.'));

                return fileName;
            }

            public static string GetFileNameWithoutAnyExtensions(string fileName)
            {
                var dirSepIndex = fileName.LastIndexOfAny(_dirSep);
                if (dirSepIndex >= 0)
                {
                    var dotIndex = -1;
                    bool doContinue = true;
                    do
                    {
                        dotIndex = fileName.LastIndexOf('.');
                        doContinue = dotIndex > dirSepIndex;
                        if (doContinue)
                            fileName = fileName.Substring(0, dotIndex);
                    }
                    while (doContinue);
                }
                else
                {
                    var dotIndex = -1;
                    bool doContinue = true;
                    do
                    {
                        dotIndex = fileName.LastIndexOf('.');
                        doContinue = dotIndex >= 0;
                        if (doContinue)
                            fileName = fileName.Substring(0, dotIndex);
                    }
                    while (doContinue);
                }

                return fileName;
            }
        }
    }
}
