using System.Linq;
using SoulsFormatsMod.PARAMS;

namespace SoulsFormatsMod
{

    public enum ItemLotCategory
    {
        None = -1,
        Weapon = 0,
        Armor = 268435456,
        Ring = 536870912,
        Good = 1073741824,
    }

    public class StartingClass
    {
        ChrHandler Player;
        GameParamHandler GPARAM;
        TextHandler Text;
        
        readonly byte Index;

        public string Name
        {
            get => Text.MenuOther[132020 + Index];
            set => Text.MenuOther[132020 + Index] = value;
        }

        public string Description
        {
            get => Text.MenuOther[132320 + Index];
            set => Text.MenuOther[132320 + Index] = value;
        }

        public int HeadArmor
        {
            get => InMenu.HeadArmor;
            set
            {
                InGame.HeadArmor = value;
                InMenu.HeadArmor = value;
            }
        }

        public int BodyArmor
        {
            get => InMenu.BodyArmor;
            set
            {
                InGame.BodyArmor = value;
                InMenu.BodyArmor = value;
            }
        }

        public int HandArmor
        {
            get => InMenu.ArmsArmor;
            set
            {
                InGame.ArmsArmor = value;
                InMenu.ArmsArmor = value;
            }
        }

        public int LegsArmor
        {
            get => InMenu.LegsArmor;
            set
            {
                InGame.LegsArmor = value;
                InMenu.LegsArmor = value;
            }
        }

        public int RightWeapon
        {
            get => InMenu.RightHandWeapon1;
            set
            {
                InMenu.RightHandWeapon1 = value;
                GPARAM.ItemLots[1810100 + Index * 20].LotItemId01 = value;
            }
        }

        public int LeftWeapon
        {
            get => InMenu.LeftHandWeapon1;
            set
            {
                InMenu.LeftHandWeapon1 = value;
                GPARAM.ItemLots[1810110 + (Index * 20)].LotItemId01 = value;
            }
        }

        private int AddPickup(int firstId, ItemLotCategory category, int itemId)
        {
            // Adds a pickup to an existing "set" of continguous ItemLot entries.
            int newId = firstId;
            while (GPARAM.ItemLots.Values.Any(r => r.ID == newId))
                // TODO: Should throw an exception if newId gets too large (+6 is the limit I believe).
                newId++;

            ItemLot pickup = GPARAM.ItemLots.CopyRow(firstId, newId);
            pickup.LotItemCategory01 = (int)category;
            pickup.LotItemId01 = itemId;
            return itemId;
        }

        public int AddRightPickup(ItemLotCategory category, int itemId)
        {
            int initID = 1810100 + (Index * 20);
            return AddPickup(initID, category, itemId);
        }

        public int AddLeftPickup(ItemLotCategory category, int itemId)
        {
            int initID = 1810110 + (Index * 20);
            return AddPickup(initID, category, itemId);
        }

        public ChrStats Stats;

        public class ChrStats
        {

            StartingClass SC;

            public ChrStats(StartingClass sc) => SC = sc;

            public byte Vitality
            {
                get => SC.InGame.Vitality;
                set
                {
                    SC.InGame.Vitality = value;
                    SC.InMenu.Vitality = value;
                }
            }

            public byte Attunement
            {
                get => SC.InGame.Attunement;
                set
                {
                    SC.InGame.Attunement = value;
                    SC.InMenu.Attunement = value;
                }
            }

            public byte Endurance
            {
                get => SC.InGame.Endurance;
                set
                {
                    SC.InGame.Endurance = value;
                    SC.InMenu.Endurance = value;
                }
            }

            public byte Strength
            {
                get => SC.InGame.Strength;
                set
                {
                    SC.InGame.Strength = value;
                    SC.InMenu.Strength = value;
                }
            }

            public byte Dexterity
            {
                get => SC.InGame.Dexterity;
                set
                {
                    SC.InGame.Dexterity = value;
                    SC.InMenu.Dexterity = value;
                }
            }

            public byte Intelligence
            {
                get => SC.InGame.Intelligence;
                set
                {
                    SC.InGame.Intelligence = value;
                    SC.InMenu.Intelligence = value;
                }
            }

            public byte Faith
            {
                get => SC.InGame.Faith;
                set
                {
                    SC.InGame.Faith = value;
                    SC.InMenu.Faith = value;
                }
            }
        }

        public ChrInit InGame => GPARAM.ChrInits[2000 + Index];
        public ChrInit InMenu => GPARAM.ChrInits[3000 + Index];

        public StartingClass(byte index, ChrHandler player, GameParamHandler gParam, TextHandler text)
        {
            Player = player;
            GPARAM = gParam;
            Text = text;
            Index = index;
            Stats = new ChrStats(this);
        }
    }

     
}
