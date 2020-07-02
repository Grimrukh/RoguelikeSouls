using System.Collections.Generic;
using System.IO;
using SoulsFormats;

namespace SoulsFormatsMod.PARAMS
{
    public class GameParamHandler
    {
        public ParamDict<NPCThought> AI;
        public ParamDict<Armor> Armor;
        public ParamDict<ArmorUpgrade> ArmorUpgrades;
        public ParamDict<Attack> AttacksPC;
        public ParamDict<Attack> AttacksNPC;
        public ParamDict<Behavior> BehaviorsPC;
        public ParamDict<Behavior> BehaviorsNPC;
        public ParamDict<Bullet> Bullets;
        public ParamDict<CalcCorrect> CalcCorrects;
        public ParamDict<ChrInit> ChrInits;
        public ParamDict<CoolTime> CoolTimes;
        public ParamDict<EquipMtrlSet> UpgradeMaterials;
        public ParamDict<FaceGen> FaceGens;
        public ParamDict<GameArea> GameAreas;
        public ParamDict<Good> Goods;
        public ParamDict<HitMtrl> HitMtrls;
        public ParamDict<ItemLot> ItemLots;
        public ParamDict<Knockback> Knockbacks;
        public ParamDict<LockCam> LockCams;
        public ParamDict<Magic> Magic;
        public ParamDict<Move> Movement;
        public ParamDict<MenuColorTable> MenuColorTables;
        public ParamDict<NPC> NPCs;
        public ParamDict<ObjAct> ObjActs;
        public ParamDict<GameObject> Objects;
        public ParamDict<Accessory> Rings;
        public ParamDict<ShopLineup> ShopLineups;
        public ParamDict<Skeleton> Skeletons;
        public ParamDict<SpEffect> SpEffects;
        public ParamDict<SpEffectVFX> SpEffectVFXs;
        public ParamDict<Talk> Talks;
        public ParamDict<Throw> Throws;
        public ParamDict<Weapon> Weapons;
        public ParamDict<WeaponUpgrade> WeaponUpgrades;
        public ParamDict<WhiteCoolTime> WhiteCoolTimes;

        // Slightly modified params (ObjAct mainly) packaged with mod. Still "vanilla" for our purposes.
        Dictionary<string, PARAMDEF> ParamDefs { get; }
        Dictionary<string, PARAM> Params { get; } = new Dictionary<string, PARAM>();
        BND3 ParamBnd { get; set; }
        public GameParamHandler(Dictionary<string, PARAMDEF> paramdefs, TextHandler text, byte[] paramBNDData)
        {
            ParamDefs = paramdefs;
            ParamBnd = BND3.Read(paramBNDData);
            foreach (BinderFile file in ParamBnd.Files)
            {
                string name = Path.GetFileNameWithoutExtension(file.Name);
                PARAM param = PARAM.Read(file.Bytes);
                PARAMDEF p = ParamDefs[param.ParamType];
                param.ApplyParamdef(p);
                Params[name] = param;
            }

            AI = new ParamDict<NPCThought>("NpcThinkParam", this, text);
            Armor = new ParamDict<Armor>("EquipParamProtector", this, text);
            ArmorUpgrades = new ParamDict<ArmorUpgrade>("ReinforceParamProtector", this, text);
            AttacksPC = new ParamDict<Attack>("AtkParam_Pc", this, text);
            AttacksNPC = new ParamDict<Attack>("AtkParam_Npc", this, text);
            BehaviorsPC = new ParamDict<Behavior>("BehaviorParam_PC", this, text);
            BehaviorsNPC = new ParamDict<Behavior>("BehaviorParam", this, text);
            Bullets = new ParamDict<Bullet>("Bullet", this, text);
            CalcCorrects = new ParamDict<CalcCorrect>("CalcCorrectGraph", this, text);
            ChrInits = new ParamDict<ChrInit>("CharaInitParam", this, text);
            CoolTimes = new ParamDict<CoolTime>("CoolTimeParam", this, text);
            UpgradeMaterials = new ParamDict<EquipMtrlSet>("EquipMtrlSetParam", this, text);
            FaceGens = new ParamDict<FaceGen>("FaceGenParam", this, text);
            GameAreas = new ParamDict<GameArea>("GameAreaParam", this, text);
            Goods = new ParamDict<Good>("EquipParamGoods", this, text);
            HitMtrls = new ParamDict<HitMtrl>("HitMtrlParam", this, text);
            ItemLots = new ParamDict<ItemLot>("ItemLotParam", this, text);
            Knockbacks = new ParamDict<Knockback>("KnockBackParam", this, text);
            LockCams = new ParamDict<LockCam>("LockCamParam", this, text);
            Magic = new ParamDict<Magic>("Magic", this, text);
            Movement = new ParamDict<Move>("MoveParam", this, text);
            MenuColorTables = new ParamDict<MenuColorTable>("MenuColorTableParam", this, text);
            NPCs = new ParamDict<NPC>("NpcParam", this, text);
            ObjActs = new ParamDict<ObjAct>("ObjActParam", this, text);
            Objects = new ParamDict<GameObject>("ObjectParam", this, text);
            Rings = new ParamDict<Accessory>("EquipParamAccessory", this, text);
            ShopLineups = new ParamDict<ShopLineup>("ShopLineupParam", this, text);
            Skeletons = new ParamDict<Skeleton>("SkeletonParam", this, text);
            SpEffects = new ParamDict<SpEffect>("SpEffectParam", this, text);
            SpEffectVFXs = new ParamDict<SpEffectVFX>("SpEffectVfxParam", this, text);
            Talks = new ParamDict<Talk>("TalkParam", this, text);
            Throws = new ParamDict<Throw>("ThrowParam", this, text);
            Weapons = new ParamDict<Weapon>("EquipParamWeapon", this, text);
            WeaponUpgrades = new ParamDict<WeaponUpgrade>("ReinforceParamWeapon", this, text);
            WhiteCoolTimes = new ParamDict<WhiteCoolTime>("WhiteCoolTimeParam", this, text);
        }

        public GameParamHandler(Dictionary<string, PARAMDEF> paramdefs, TextHandler text, string paramBNDPath) :
            this(paramdefs, text, File.ReadAllBytes(paramBNDPath))
        { }

        public PARAM this[string paramName] => Params[paramName];

        public void Export(string gameDir, bool sort = true)
        {
            if (sort)
                SortAll();

            foreach (BinderFile file in ParamBnd.Files)
            {
                string name = Path.GetFileNameWithoutExtension(file.Name);
                file.Bytes = Params[name].Write();
            }
            string path = gameDir + @"param\GameParam\GameParam.parambnd.dcx";
            ParamBnd.Write(path);
        }

        public void SortAll()
        {
            AI.SortRows();
            Armor.SortRows();
            ArmorUpgrades.SortRows();
            AttacksPC.SortRows();
            AttacksNPC.SortRows();
            BehaviorsPC.SortRows();
            BehaviorsNPC.SortRows();
            Bullets.SortRows();
            CalcCorrects.SortRows();
            ChrInits.SortRows();
            CoolTimes.SortRows();
            UpgradeMaterials.SortRows();
            FaceGens.SortRows();
            GameAreas.SortRows();
            Goods.SortRows();
            HitMtrls.SortRows();
            ItemLots.SortRows();
            Knockbacks.SortRows();
            LockCams.SortRows();
            Magic.SortRows();
            Movement.SortRows();
            MenuColorTables.SortRows();
            NPCs.SortRows();
            ObjActs.SortRows();
            Objects.SortRows();
            Rings.SortRows();
            ShopLineups.SortRows();
            Skeletons.SortRows();
            SpEffects.SortRows();
            SpEffectVFXs.SortRows();
            Talks.SortRows();
            Throws.SortRows();
            Weapons.SortRows();
            WeaponUpgrades.SortRows();
            WhiteCoolTimes.SortRows();
        }
    }
}
