using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormats;
using SoulsFormatsMod.PARAMS;
using System.IO;
using System.Text.RegularExpressions;

namespace SoulsFormatsMod
{
    public class SoulsMod
    {
        internal string BackupExt;
        public string GameDir;
        private int[] InvalidCharacters { get; } = { 2220, 3511, 4091, 9999 };

        public AnimModHandler DefaultAnimMod = new AnimModHandler();

        public Dictionary<int, ChrHandler> Characters = new Dictionary<int, ChrHandler>();
        public ChrHandler this[int id] => Characters[id];
        public ChrHandler Player => Characters[0];
        public TextHandler Text { get; set; }
        public TextHandler VanillaText { get; set; }
        public Dictionary<string, PARAMDEF> ParamDefs { get; } = new Dictionary<string, PARAMDEF>();
        public GameParamHandler GPARAM { get; set; }
        public GameParamHandler VanillaGPARAM { get; }

        public StartingClass[] StartingClasses = new StartingClass[10];

        public SoulsMod(string gameDir, string backupExt = ".smbak", 
            byte[] paramBNDData = null, byte[] paramdefBNDData = null, 
            byte[] itemMSGBNDData = null, byte[] menuMSGBNDData = null)
        {
            if (!gameDir.EndsWith(@"\"))
                gameDir += @"\";
            GameDir = gameDir;
            BackupExt = backupExt;
            // RestoreBackups();  // No need to restore backups automatically, as all files are loaded directly FROM the backups anyway.

            // Text is loaded first so it can be passed to `GameParamHandler`.
#if DEBUG
            Console.Write("Loading Text... ");
#endif
            if (itemMSGBNDData == null)
                itemMSGBNDData = File.ReadAllBytes(GameDir + @"msg/ENGLISH/item.msgbnd.dcx");
            if (menuMSGBNDData == null)
                menuMSGBNDData = File.ReadAllBytes(GameDir + @"msg/ENGLISH/menu.msgbnd.dcx");
            Text = new TextHandler(itemMSGBNDData, menuMSGBNDData);
#if DEBUG
            Console.Write("Done.\n");
            Console.Write("Loading Text (vanilla copy)... ");
#endif
            VanillaText = new TextHandler(itemMSGBNDData, menuMSGBNDData);
#if DEBUG
            Console.Write("Done.\n");
            Console.Write("Loading ParamDefs... ");
#endif
            if (paramdefBNDData == null)
                paramdefBNDData = File.ReadAllBytes(GameDir + @"paramdef\paramdef.paramdefbnd.dcx");
            BND3 paramdefBnd = BND3.Read(paramdefBNDData);
            foreach (BinderFile file in paramdefBnd.Files)
            {
                PARAMDEF paramdef = PARAMDEF.Read(file.Bytes);
                ParamDefs[paramdef.ParamType] = paramdef;
            }
#if DEBUG
            Console.Write("Done.\n");
            Console.Write("Loading GameParams... ");
#endif
            if (paramBNDData == null)
                paramBNDData = File.ReadAllBytes(GameDir + @"param\GameParam\GameParam.parambnd.dcx");
            GPARAM = new GameParamHandler(ParamDefs, Text, paramBNDData);
#if DEBUG
            Console.Write("Done.\n");
            Console.Write("Loading GameParams (vanilla copy)... ");
#endif
            if (paramBNDData != null)
                VanillaGPARAM = new GameParamHandler(ParamDefs, VanillaText, paramBNDData);
            else
                VanillaGPARAM = new GameParamHandler(ParamDefs, VanillaText, GameDir + @"param\GameParam\GameParam.parambnd.dcx");
#if DEBUG
            Console.Write("Done.\n");   
#endif
        }

        public void LoadPlayerCharacter()
        {
            string match = @"^c0000[.]anibnd([.]dcx)?$";
            IEnumerable<string> chrFiles = Directory.GetFiles($"{GameDir}chr");
            chrFiles = chrFiles.Select(f => Path.GetFileName(f)).Where(f => Regex.IsMatch(f, match));
            foreach (string file in chrFiles)
            {
                int id = int.Parse(file.Substring(1, 4));
                Characters[id] = new ChrHandler(id, this);
            }
            for (byte i = 0; i < 10; i++)
                StartingClasses[i] = new StartingClass(i, Player, GPARAM, Text);
        }

        public void LoadNonPlayerCharacters()
        {
            string match = @"^c\d{4}[.]anibnd([.]dcx)?$";
            IEnumerable<string> chrFiles = Directory.GetFiles($"{GameDir}chr");
            chrFiles = chrFiles.Select(f => Path.GetFileName(f)).Where(f => Regex.IsMatch(f, match));
            foreach (string file in chrFiles)
            {
                int id = int.Parse(file.Substring(1, 4));
                if (InvalidCharacters.Contains(id) || id == 0)
                {
                    continue;  // skip invalid/unused characters and player character (c0000)
                }
                Characters[id] = new ChrHandler(id, this);
            }
        }

        public Dictionary<int, string> IndexAllFFX()
        {
            // Maps each FFX ID to the name of the (first) vanilla FFXBND that contains it (e.g. "10_01_00_00").
            Dictionary<int, string> dict = new Dictionary<int, string>();
            foreach (string bndFile in Directory.GetFiles(GameDir + @"\sfx"))
            {
                string bndFileName = Path.GetFileName(bndFile);
                if (bndFile.EndsWith(".ffxbnd.dcx"))
                {
                    var bnd = BND3.Read(bndFile);
                    foreach (var file in bnd.Files.Where(f => f.Name.EndsWith(".ffx")))
                    {
                        string fileNumStr = Path.GetFileNameWithoutExtension(file.Name).Substring(1);
                        int FFXID = int.Parse(fileNumStr);
                        dict[FFXID] = bndFileName;
                    }
                }
            }
            return dict;
        }

        public string Backup(string filePath)
        {
            if (!File.Exists(filePath + BackupExt))
            {
                Console.Write($"Creating backup of {filePath}... ");
                File.Copy(filePath, filePath + BackupExt);
                Console.Write("Done.\n");
            }
            return filePath + BackupExt;
        }

        public void Install()
        {
            Console.WriteLine("Final installation...");
#if DEBUG
            //Console.Write($"Exporting GameParam...");
#endif
            GPARAM.Export(GameDir);
#if DEBUG
            //Console.Write($"Done.\n");
            //Console.Write($"Exporting Text...");
#endif
            Text.Export(GameDir);
#if DEBUG
            //Console.Write($"Done.\n");
#endif

            foreach (KeyValuePair<int, ChrHandler> kv in Characters)
            {
                string chrFile = $"c{kv.Key:0000}";
                //Console.Write($"Exporting {chrFile}...");
                try
                {
                    kv.Value.Export();
                    //Console.Write("Done.\n");
                }
                catch (Exception e)
                {
                    Console.Write("FAILED.\n");
                    Console.WriteLine(Environment.NewLine + e.ToString());
                    Console.WriteLine(Environment.NewLine + $"Modification of {chrFile} failed.");
                    Console.WriteLine("Continue anyway? [Y/N]");
                    ConsoleKey key = Console.ReadKey(true).Key;
                    while (key != ConsoleKey.Y && key != ConsoleKey.N)
                        key = Console.ReadKey(true).Key;

                    if (key == ConsoleKey.N)
                        Environment.Exit(0);
                    else Console.WriteLine(Environment.NewLine);
                }
            }

            Console.WriteLine("\nInstallation successful! Press ENTER to exit.");
            Console.ReadLine();
        }

        public void RestoreBackups()
        {
            Console.Write("Restoring backups...");
            void restoreDir(string dir)
            {
                string[] directories = Directory.GetDirectories(dir, "*", SearchOption.AllDirectories);
                foreach (string directory in directories)
                {
                    if (directory.Contains("_utilities")) continue;

                    IEnumerable<string> files = Directory.GetFiles(directory).Where(f => !f.EndsWith(BackupExt));
                    foreach (string file in files)
                        if (File.Exists(file + BackupExt))
                            File.Copy(file + BackupExt, file, true);

                    IEnumerable<string> dirs = Directory.GetDirectories(directory, "*", SearchOption.AllDirectories);
                    foreach (string dct in dirs)
                        restoreDir(dct);
                }
            }
            restoreDir(GameDir);
            Console.WriteLine("SUCCESS");
        }
    }
}
