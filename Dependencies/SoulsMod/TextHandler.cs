using SoulsFormats;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SoulsFormatsMod
{
    public class TextHandler
    {
        string GameDir { get; }

        internal BND3 Item { get; set; }
        internal BND3 Menu { get; set; }

        public FMGHandler NPCNames;
        public FMGHandler EventText;

        public FMGHandler WeaponNames;
        public FMGHandler WeaponSummaries;
        public FMGHandler WeaponDescriptions;

        public FMGHandler ArmorNames;
        public FMGHandler ArmorDescriptions;
        public FMGHandler ArmorLongDescriptions;

        public FMGHandler GoodsNames;
        public FMGHandler GoodsDescriptions;
        public FMGHandler GoodsLongDescriptions;

        public FMGHandler AccessoryNames;
        public FMGHandler AccessoryDescriptions;
        public FMGHandler AccessoryLongDescriptions;

        public FMGHandler MagicNames;
        public FMGHandler MagicDescriptions;
        public FMGHandler MagicLongDescriptions;

        public FMGHandler MenuOther;
        public FMGHandler Conversations;

        public TextHandler(byte[] itemMSGBNDData, byte[] menuMSGBNDData)
        {
            Item = BND3.Read(itemMSGBNDData);
            Menu = BND3.Read(menuMSGBNDData);

            NPCNames = new FMGHandler(this, Item, "NPC_name_");
            EventText = new FMGHandler(this, Menu, "Event_text_");

            WeaponNames = new FMGHandler(this, Item, "Weapon_name_");
            WeaponSummaries = new FMGHandler(this, Item, "Weapon_description_");
            WeaponDescriptions = new FMGHandler(this, Item, "Weapon_long_desc_");

            ArmorNames = new FMGHandler(this, Item, "Armor_name_");
            ArmorDescriptions = new FMGHandler(this, Item, "Armor_description_");
            ArmorLongDescriptions = new FMGHandler(this, Item, "Armor_long_desc_");

            GoodsNames = new FMGHandler(this, Item, "Item_name_");
            GoodsDescriptions = new FMGHandler(this, Item, "Item_description_");
            GoodsLongDescriptions = new FMGHandler(this, Item, "Item_long_desc_");

            AccessoryNames = new FMGHandler(this, Item, "Accessory_name_");
            AccessoryDescriptions = new FMGHandler(this, Item, "Accessory_description_");
            AccessoryLongDescriptions = new FMGHandler(this, Item, "Accessory_long_desc_");

            MagicNames = new FMGHandler(this, Item, "Magic_name_");
            MagicDescriptions = new FMGHandler(this, Item, "Magic_description_");
            MagicLongDescriptions = new FMGHandler(this, Item, "Magic_long_desc_");

            MenuOther = new FMGHandler(this, Menu, "Menu_others_");
            Conversations = new FMGHandler(this, Menu, "Conversation_");
        }

        public void Export(string gameDir)
        {
            //foreach (int id in WeaponNames.GetIDs())
            //{
            //    int diff = id % 100;
            //    if (diff == 0 || id < 100000) continue;
            //    WeaponNames[id] = $"{WeaponNames[id - diff]}+{diff}";
            //}

            NPCNames.Save();
            EventText.Save();

            WeaponNames.Save(true);
            WeaponSummaries.Save(true);
            WeaponDescriptions.Save(true);

            ArmorNames.Save(true);
            ArmorDescriptions.Save(true);
            ArmorLongDescriptions.Save(true);

            GoodsNames.Save();
            GoodsDescriptions.Save();
            GoodsLongDescriptions.Save();

            AccessoryNames.Save();
            AccessoryDescriptions.Save();
            AccessoryLongDescriptions.Save();

            MagicNames.Save();
            MagicDescriptions.Save();
            MagicLongDescriptions.Save();

            MenuOther.Save();
            Conversations.Save();

            Item.Write(gameDir + @"msg\ENGLISH\item.msgbnd.dcx");
            Menu.Write(gameDir + @"msg\ENGLISH\menu.msgbnd.dcx");
        }

        public class FMGHandler
        {
            private FMG Proper;
            private FMG Patch;
            private BinderFile FileProper;
            private BinderFile FilePatch;

            public FMGHandler(TextHandler th, BND3 bnd, string name)
            {
                IEnumerable<BinderFile> list = bnd.Files.Where(f => Path.GetFileNameWithoutExtension(f.Name) == name);
                FileProper = list.ElementAt(0);
                Proper = FMG.Read(FileProper.Bytes);
                if (list.Count() > 1)
                {
                    FilePatch = list.ElementAtOrDefault(1);
                    Patch = FMG.Read(FilePatch.Bytes);
                }
            }

            public void Save(bool needsUpgrade = false)
            {
                if (needsUpgrade) SetUpgradeTexts();
                Proper.Entries.Sort((x, y) => x.ID.CompareTo(y.ID));
                FileProper.Bytes = Proper.Write();
                if (FilePatch != null)
                {
                    Patch.Entries.Sort((x, y) => x.ID.CompareTo(y.ID));
                    FilePatch.Bytes = Patch.Write();
                }
            }

            internal IEnumerable<int> GetIDs()
            {
                var ienum = Proper.Entries.Select(e => e.ID);
                if (Patch != null) ienum = ienum.Concat(Patch.Entries.Select(e => e.ID));
                return ienum.Distinct();
            }

            private string GetFromFile(FMG fmg, long id)
            {
                if (fmg == null) return null;
                FMG.Entry entry = fmg.Entries.FirstOrDefault(f => f.ID == id);
                if (entry != null && !string.IsNullOrWhiteSpace(entry.Text)) return entry.Text;
                return null;
            }

            private void SetInFile(FMG fmg, long id, string s)
            {
                if (fmg == null) return;
                FMG.Entry entry = fmg.Entries.FirstOrDefault(f => f.ID == id);
                if (entry != null) entry.Text = s;
                else
                {
                    FMG.Entry newEntry = new FMG.Entry((int)id, s);
                    fmg.Entries.Add(newEntry);
                }
            }

            public string this[long i]
            {
                get => GetFromFile(Proper, i) ?? GetFromFile(Patch, i);
                set
                {
                    SetInFile(Proper, i, value);
                    SetInFile(Patch, i, value);
                }
            }

            private void SetUpgradeTexts()
            {
                foreach (int id in GetIDs())
                {
                    int diff = id % 100;
                    if (diff == 0 || id < 100000) continue;
                    this[id] = $"{this[id - diff]}+{diff}";
                }
            }

        }
    }

   
}
