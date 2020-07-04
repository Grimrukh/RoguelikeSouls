using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using RoguelikeSouls.Extensions;
using FFXDict = System.Collections.Generic.Dictionary<int, string>;

namespace RoguelikeSouls.Installation
{
    class EnemyGenerator
    {
        SoulsMod Mod { get; }
        Random Rand { get; }
        WeaponGenerator WeaponGen { get; }
        ArmorGenerator ArmorGen { get; }
        ItemLot ItemLotTemplate { get => Mod.VanillaGPARAM.ItemLots[1000]; }

        BossNameGenerator NameGenerator { get; }

        public static List<Enemy> EnemyList { get; } = new List<Enemy>()
        {
            new Enemy("Large Rat",                              EnemyRarity.Common,   1200, 120000, 120000, aiParamID: 120000, 100,  ChrSize.Normal,  Label.Animal, Label.Infested),
            new Enemy("Small Rat",                              EnemyRarity.Common,   1201, 120100, 120100, aiParamID: 120100, 60,   ChrSize.Small,   Label.Animal, Label.Infested),
            new Enemy("Giant Rat",                              EnemyRarity.Rare,     1202, 120200, 120200, aiParamID: 120200, 500,  ChrSize.Giant,   Label.Animal, Label.Infested),
            new Enemy("Snow Rat",                               EnemyRarity.Common,   1203, 120300, 120300, aiParamID: 120300, 100,  ChrSize.Normal,  Label.Animal, Label.Infested, Label.Snow),
            new Enemy("Infested Ghoul (Sword)",                 EnemyRarity.Common,   2060, 206000, 206000, aiParamID: 206000, 100,  ChrSize.Normal,  Label.Sapient, Label.Infested),
            new Enemy("Infested Ghoul (Spear)",                 EnemyRarity.Common,   2060, 206001, 206010, aiParamID: 206001, 100,  ChrSize.Normal,  Label.Sapient, Label.Infested),
            new Enemy("Infested Ghoul (Corpse)",                EnemyRarity.Uncommon, 2060, 206002, 206020, aiParamID: 206002, 150,  ChrSize.Normal,  Label.Sapient, Label.Infested),
            new Enemy("Stray Demon",                            EnemyRarity.Boss,     2230, 223000, 223000, aiParamID: 223000, 3000, ChrSize.Giant,   Label.Demon, Label.Winged),
            new Enemy("Stray Demon (Mob)",                      EnemyRarity.VeryRare, 2230, 223000, 223010, aiParamID: 223010, 2000, ChrSize.Giant,   Label.Demon, Label.Winged),
            new Enemy("Demon Firesage",                         EnemyRarity.Boss,     2231, 223100, 223100, aiParamID: 223100, 3000, ChrSize.Giant,   Label.Demon, Label.Fire, Label.Winged),
            new Enemy("Demon Firesage (Mob)",                   EnemyRarity.VeryRare, 2231, 223100, 223110, aiParamID: 223110, 2000, ChrSize.Giant,   Label.Demon, Label.Fire, Label.Winged),
            // new Enemy("Asylum Demon",                           EnemyRarity.Boss,     2232, 223200, 223200, aiParamID: 223200, 3000, ChrSize.Giant,   Label.Demon, Label.Winged),  // TODO: AI is region-dependent.
            // new Enemy("Asylum Demon (Mob)",                     EnemyRarity.VeryRare, 2232, 223200, 223210, aiParamID: 223210, 2000, ChrSize.Giant,   Label.Demon, Label.Winged),
            new Enemy("Capra Demon",                            EnemyRarity.Boss,     2240, 224000, 224000, aiParamID: 224000, 3000, ChrSize.Normal,  Label.Demon),
            new Enemy("Capra Demon (Mob)",                      EnemyRarity.Rare,     2240, 224000, 224010, aiParamID: 224000, 2000, ChrSize.Normal,  Label.Demon),  // only rare
            new Enemy("Taurus Demon",                           EnemyRarity.Boss,     2250, 225000, 225000, aiParamID: 225000, 3000, ChrSize.Normal,  Label.Demon),
            new Enemy("Taurus Demon (Mob)",                     EnemyRarity.VeryRare, 2250, 225000, 225010, aiParamID: 225010, 2000, ChrSize.Normal,  Label.Demon),
            new Enemy("Batwing Demon",                          EnemyRarity.Uncommon, 2260, 226000, 226000, aiParamID: 226000, 200,  ChrSize.Normal,  Label.Demon, Label.Winged),
            new Enemy("Mushroom Parent",                        EnemyRarity.Uncommon, 2270, 227000, 227000, aiParamID: 227000, 300,  ChrSize.Normal,  Label.Plant),
            new Enemy("Mushroom Child",                         EnemyRarity.Common,   2280, 228000, 228000, aiParamID: 228000, 50,   ChrSize.Small,   Label.Plant),
            // new Enemy("Titanite Demon",                         EnemyRarity.Rare,     2300, 230000, 230000, aiParamID: 230000, ChrSize.Normal,  Label.Stone, Label.Lightning),  // TODO: Need a general AI script...
            new Enemy("Crow Demon",                             EnemyRarity.Uncommon, 2310, 231000, 231000, aiParamID: 231000, 400,  ChrSize.Normal,  Label.Sapient, Label.Winged),
            new Enemy("Iron Golem",                             EnemyRarity.Boss,     2320, 232000, 232000, aiParamID: 232000, 3000, ChrSize.Giant,   Label.Stone, Label.Metal),
            new Enemy("Iron Golem (Mob)",                       EnemyRarity.VeryRare, 2320, 232000, 232010, aiParamID: 232010, 2000, ChrSize.Giant,   Label.Stone, Label.Metal),
            new Enemy("Demonic Foliage",                        EnemyRarity.Common,   2330, 233000, 233000, aiParamID: 233000, 80,   ChrSize.Normal,  Label.Plant),
            new Enemy("Executioner Smough",                     EnemyRarity.Boss,     2360, 236000, 236000, aiParamID: 236000, 3000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Executioner Smough (Mob)",               EnemyRarity.VeryRare, 2360, 236000, 236010, aiParamID: 236010, 2000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Executioner Smough (Lightning)",         EnemyRarity.Boss,     2360, 236001, 236020, aiParamID: 236001, 4000, ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Lightning),
            new Enemy("Executioner Smough (Lightning) (Mob)",   EnemyRarity.VeryRare, 2360, 236001, 236030, aiParamID: 236011, 2500, ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Lightning),
            new Enemy("Channeler",                              EnemyRarity.Rare,     2370, 237000, 237000, aiParamID: 237000, 1000, ChrSize.Normal,  Label.Sapient, Label.Magic),
            new Enemy("Stone Knight",                           EnemyRarity.Uncommon, 2380, 238000, 238000, aiParamID: 238000, 500,  ChrSize.Normal,  Label.Stone, Label.Divine),
            new Enemy("Darkwraith",                             EnemyRarity.Common,   2390, 239000, 239000, aiParamID: 239000, 500,  ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Abyssal),
            new Enemy("Painting Guardian",                      EnemyRarity.Common,   2400, 240000, 240000, aiParamID: 240000, 500,  ChrSize.Normal,  Label.Sapient, Label.Stealth),
            new Enemy("Silver Knight (Sword)",                  EnemyRarity.Common,   2410, 241000, 241000, aiParamID: 241000, 500,  ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Silver Knight (Spear)",                  EnemyRarity.Common,   2410, 241003, 241010, aiParamID: 241003, 500,  ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Silver Knight (Bow)",                    EnemyRarity.Uncommon, 2410, 241004, 241020, aiParamID: 241004, 500,  ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Archer),
            new Enemy("Demonic Statue",                         EnemyRarity.Common,   2430, 243000, 243000, aiParamID: 243000, 100,  ChrSize.Normal,  Label.Stone, Label.Fire),
            new Enemy("Hollow (Sword)",                         EnemyRarity.Common,   2500, 250050, 250000, aiParamID: 250000, 50,   ChrSize.Normal,  Label.Sapient, Label.Hollow),
            new Enemy("Hollow (Torch)",                         EnemyRarity.Common,   2500, 250051, 250010, aiParamID: 250010, 50,   ChrSize.Normal,  Label.Sapient, Label.Hollow),
            new Enemy("Hollow (Bow)",                           EnemyRarity.Uncommon, 2500, 250052, 250020, aiParamID: 250020, 50,   ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Archer),
            new Enemy("Hollow (Unarmed)",                       EnemyRarity.Common,   2500, 250040, 250030, aiParamID: 250006, 30,   ChrSize.Normal,  Label.Sapient, Label.Hollow),  // doesn't attack
            new Enemy("Hollow Assassin",                        EnemyRarity.Common,   2520, 252000, 252000, aiParamID: 252000, 80,   ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Stealth),
            new Enemy("Blowdart Sniper",                        EnemyRarity.Rare,     2530, 253002, 253000, aiParamID: 253002, 150,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Stealth),
            new Enemy("Hollow Warrior (Sword)",                 EnemyRarity.Common,   2540, 254000, 254000, aiParamID: 254000, 100,  ChrSize.Normal,  Label.Sapient, Label.Hollow),
            new Enemy("Hollow Warrior (Axe)",                   EnemyRarity.Common,   2540, 254001, 254010, aiParamID: 254001, 100,  ChrSize.Normal,  Label.Sapient, Label.Hollow),
            new Enemy("Hollow Warrior (Firebombs)",             EnemyRarity.Uncommon, 2540, 254002, 254020, aiParamID: 254002, 120,  ChrSize.Normal,  Label.Sapient, Label.Hollow),
            new Enemy("Hollow Soldier (Spear)",                 EnemyRarity.Common,   2550, 255000, 255000, aiParamID: 255000, 150,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Hollow Soldier (Sword)",                 EnemyRarity.Common,   2550, 255001, 255010, aiParamID: 255001, 150,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Hollow Soldier (Crossbow)",              EnemyRarity.Uncommon, 2550, 255002, 255020, aiParamID: 255002, 150,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal, Label.Archer),
            new Enemy("Balder Knight (Longsword)",              EnemyRarity.Common,   2560, 256000, 256000, aiParamID: 256000, 200,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Balder Knight (Crossbow)",               EnemyRarity.Common,   2560, 256001, 256010, aiParamID: 256001, 200,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal, Label.Archer),
            new Enemy("Balder Knight (Rapier)",                 EnemyRarity.Uncommon, 2560, 256002, 256020, aiParamID: 256002, 200,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Berenike Knight (Sword)",                EnemyRarity.Uncommon, 2570, 257000, 257000, aiParamID: 257000, 300,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Berenike Knight (Mace)",                 EnemyRarity.Uncommon, 2570, 257001, 257010, aiParamID: 257001, 300,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Metal),
            new Enemy("Necromancer",                            EnemyRarity.Uncommon, 2650, 265000, 265000, aiParamID: 265000, 300,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Fire),
            new Enemy("Butcher",                                EnemyRarity.Uncommon, 2660, 266000, 266000, aiParamID: 266000, 300,  ChrSize.Normal,  Label.Sapient, Label.Hollow),
            // new Enemy("Ghost (Male)",                           EnemyRarity.Common,   2670, 267000, 267000, aiParamID: 267000, ChrSize.Normal,  Label.Ghost),  // AI broken
            // new Enemy("Ghost (Female)",                         EnemyRarity.Uncommon, 2680, 268000, 268000, aiParamID: 268000, ChrSize.Normal,  Label.Ghost, Label.Magic),  // AI broken
            new Enemy("Serpent Soldier",                        EnemyRarity.Common,   2690, 269000, 269000, aiParamID: 269000, 200,  ChrSize.Normal,  Label.Serpent, Label.Metal),
            new Enemy("Serpent Mage",                           EnemyRarity.Uncommon, 2700, 270000, 270000, aiParamID: 270000, 200,  ChrSize.Normal,  Label.Serpent, Label.Lightning),
            new Enemy("Crystal Golem",                          EnemyRarity.Common,   2710, 271000, 271000, aiParamID: 271000, 200,  ChrSize.Normal,  Label.Stone, Label.Crystal),
            new Enemy("Golden Crystal Golem",                   EnemyRarity.VeryRare, 2711, 271100, 271100, aiParamID: 271100, 5000, ChrSize.Normal,  Label.Stone, Label.Crystal),
            new Enemy("Crossbreed Priscilla",                   EnemyRarity.Boss,     2730, 273000, 273000, aiParamID: 273000, 3000, ChrSize.Giant,   Label.Sapient, Label.Snow, Label.Stealth),
            new Enemy("Crossbreed Priscilla (Mob)",             EnemyRarity.VeryRare, 2730, 273000, 273010, aiParamID: 273000, 2000, ChrSize.Giant,   Label.Sapient, Label.Snow, Label.Stealth),
            // new Enemy("Crossbreed Priscilla (Tail)",            EnemyRarity.Boss,     2731, 273100, 273100, aiParamID: 273100, ChrSize.Giant,   Label.Part),
            new Enemy("Mimic",                                  EnemyRarity.Rare,     2780, 278000, 278000, aiParamID: 278000, 1000, ChrSize.Normal,  Label.Mimic),
            new Enemy("Black Knight (Sword)",                   EnemyRarity.Rare,     2790, 279050, 279000, aiParamID: 279000, 1000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Black Knight (Greatsword)",              EnemyRarity.Rare,     2790, 279051, 279010, aiParamID: 279001, 1000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Black Knight (Axe)",                     EnemyRarity.Rare,     2790, 279052, 279020, aiParamID: 279002, 1000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Black Knight (Halberd)",                 EnemyRarity.Rare,     2790, 279053, 279030, aiParamID: 279003, 1000, ChrSize.Normal,  Label.Sapient, Label.Metal),
            new Enemy("Hollow Crystal Soldier (Sword)",         EnemyRarity.Common,   2800, 280000, 280000, aiParamID: 280000, 200,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Crystal),
            new Enemy("Hollow Crystal Soldier (Bow)",           EnemyRarity.Uncommon, 2800, 280001, 280010, aiParamID: 280001, 200,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Crystal, Label.Archer),
            new Enemy("Infested Barbarian (Club)",              EnemyRarity.Uncommon, 2810, 281000, 281000, aiParamID: 281000, 300,  ChrSize.Normal,  Label.Sapient, Label.Infested),
            new Enemy("Infested Barbarian (Boulder)",           EnemyRarity.Uncommon, 2811, 281100, 281100, aiParamID: 281100, 350,  ChrSize.Normal,  Label.Sapient, Label.Infested),
            // new Enemy("Spider Hollow",                          EnemyRarity.Common,   2820, 282000, 282000, aiParamID: 282000, ChrSize.Normal,  Label.Hollow, Label.Demon),
            new Enemy("Phalanx",                                EnemyRarity.Uncommon, 2830, 283010, 283000, aiParamID: 283010, 150,  ChrSize.Normal,  Label.Hollow, Label.Slime),
            new Enemy("Engorged Hollow (Torch)",                EnemyRarity.Common,   2840, 284000, 284000, aiParamID: 284000, 100,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Infested),
            new Enemy("Engorged Hollow (Pyromancy)",            EnemyRarity.Uncommon, 2840, 284001, 284010, aiParamID: 284001, 120,  ChrSize.Normal,  Label.Sapient, Label.Hollow, Label.Infested, Label.Fire),
            // new Enemy("Giant",                                  EnemyRarity.Rare,     2860, 286000, 286000, aiParamID: 286000, ChrSize.Giant,   Label.Giant, Label.Metal),  // TODO: needs general AI
            new Enemy("Sentinel",                               EnemyRarity.Uncommon, 2870, 287010, 287010, aiParamID: 287010, 300,  ChrSize.Giant,   Label.Giant, Label.Metal),
            new Enemy("Sentinel (Royal)",                       EnemyRarity.Rare,     2870, 287000, 287000, aiParamID: 287000, 800,  ChrSize.Giant,   Label.Giant, Label.Metal, Label.Divine),
            new Enemy("Skeleton (Scimitar)",                    EnemyRarity.Common,   2900, 290000, 290000, aiParamID: 290000, 100,  ChrSize.Normal,  Label.Skeleton),
            new Enemy("Skeleton (Bow)",                         EnemyRarity.Uncommon, 2900, 290001, 290010, aiParamID: 290001, 100,  ChrSize.Normal,  Label.Skeleton, Label.Archer),
            new Enemy("Skeleton (Sword)",                       EnemyRarity.Common,   2900, 290002, 290020, aiParamID: 290002, 100,  ChrSize.Normal,  Label.Skeleton),
            new Enemy("Giant Skeleton (Sword)",                 EnemyRarity.Uncommon, 2910, 291000, 291000, aiParamID: 291000, 300,  ChrSize.Giant,   Label.Giant, Label.Skeleton),
            new Enemy("Giant Skeleton (Bow)",                   EnemyRarity.Uncommon, 2910, 291001, 291010, aiParamID: 291001, 300,  ChrSize.Giant,   Label.Giant, Label.Skeleton, Label.Archer),
            new Enemy("Bonewheel Skeleton",                     EnemyRarity.Uncommon, 2930, 293000, 293000, aiParamID: 293000, 200,  ChrSize.Normal,  Label.Skeleton),
            new Enemy("Skeleton Baby",                          EnemyRarity.Uncommon, 2940, 294000, 294000, aiParamID: 294000, 30,   ChrSize.Small,   Label.Skeleton),
            new Enemy("Skeleton Beast",                         EnemyRarity.Uncommon, 2950, 295000, 295000, aiParamID: 295000, 400,  ChrSize.Normal,  Label.Skeleton, Label.Animal),
            new Enemy("Bone Tower",                             EnemyRarity.Uncommon, 2960, 296000, 296000, aiParamID: 296000, 200,  ChrSize.Normal,  Label.Skeleton),
            new Enemy("Giant Mosquito",                         EnemyRarity.Common,   3090, 309000, 309000, aiParamID: 309000, 20,   ChrSize.Small,   Label.Bug),
            new Enemy("Slime",                                  EnemyRarity.Common,   3200, 320000, 320000, aiParamID: 320000, 80,   ChrSize.Small,   Label.Slime),
            new Enemy("Egg Carrier",                            EnemyRarity.Uncommon, 3210, 321000, 321000, aiParamID: 321000, 50,   ChrSize.Normal,  Label.Hollow, Label.Bug),
            new Enemy("Vile Maggot",                            EnemyRarity.Uncommon, 3220, 322000, 322000, aiParamID: 322000, 20,   ChrSize.Small,   Label.Bug),
            new Enemy("Chaos Eater",                            EnemyRarity.Uncommon, 3240, 324000, 324000, aiParamID: 324000, 400,  ChrSize.Giant,   Label.Bug),
            new Enemy("Man-Eater Shell",                        EnemyRarity.Uncommon, 3250, 325000, 325000, aiParamID: 325000, 400,  ChrSize.Normal,  Label.Bug, Label.Crystal),
            new Enemy("Basilisk",                               EnemyRarity.Common,   3270, 327000, 327000, aiParamID: 327000, 100,  ChrSize.Normal,  Label.Bug),
            new Enemy("Crystal Lizard",                         EnemyRarity.Rare,     3300, 330000, 330000, aiParamID: 330000, 1000, ChrSize.Small,   Label.Bug, Label.Crystal),
            new Enemy("Pinwheel",                               EnemyRarity.Rare,     3320, 332002, 332020, aiParamID: 332002, 800,  ChrSize.Normal,  Label.Fire, Label.Magic),
            // new Enemy("Pisaca",                                 EnemyRarity.Common,   3330, 333000, 333000, aiParamID: 333000, ChrSize.Normal,  Label.Bug, Label.Crystal),  // TODO: needs general AI
            new Enemy("Attack Dog",                             EnemyRarity.Common,   3340, 334000, 334000, aiParamID: 334000, 100,  ChrSize.Small,   Label.Animal),
            new Enemy("Flaming Attack Dog",                     EnemyRarity.Uncommon, 3341, 334100, 334100, aiParamID: 334100, 150,  ChrSize.Small,   Label.Animal, Label.Fire),
            new Enemy("Possessed Tree",                         EnemyRarity.VeryRare, 3350, 335000, 335000, aiParamID: 335000, 1000, ChrSize.Giant,   Label.Plant),
            new Enemy("Tree Lizard",                            EnemyRarity.Uncommon, 3370, 337000, 337000, aiParamID: 337000, 250,  ChrSize.Normal,  Label.Bug, Label.Plant),
            new Enemy("Giant Leech",                            EnemyRarity.Common,   3380, 338000, 338000, aiParamID: 338000, 100,  ChrSize.Small,   Label.Bug, Label.Slime),
            new Enemy("Burrowing Rockworm (Ground)",            EnemyRarity.Rare,     3390, 339001, 339010, aiParamID: 339001, 800,  ChrSize.Giant,   Label.Bug),
            new Enemy("Cragspider",                             EnemyRarity.Common,   3400, 340000, 340000, aiParamID: 340000, 100,  ChrSize.Normal,  Label.Bug, Label.Fire),  // TODO: Enable "path move"
            new Enemy("Frog-Ray",                               EnemyRarity.Common,   3410, 341000, 341000, aiParamID: 341000, 100,  ChrSize.Small,   Label.Bug, Label.Aquatic),
            new Enemy("Bounding Demon",                         EnemyRarity.VeryRare, 3421, 342100, 342100, aiParamID: 342100, 2000, ChrSize.Giant,   Label.Dragon, Label.Demon),
            new Enemy("Armored Tusk",                           EnemyRarity.Rare,     3460, 346000, 346000, aiParamID: 346100, 800,  ChrSize.Normal,  Label.Animal, Label.Metal),  // both use my modified DoA AI
            // new Enemy("Armored Tusk (No Backstab)",             EnemyRarity.Rare,     3461, 346100, 346100, aiParamID: 346100, 1500, ChrSize.Normal,  Label.Animal, Label.Metal),  // too annoying
            new Enemy("Sanctuary Guardian",                     EnemyRarity.Boss,     3471, 347100, 347100, aiParamID: 347100, 4000, ChrSize.Giant,   Label.Animal, Label.Aquatic, Label.Lightning),
            new Enemy("Sanctuary Guardian (Mob)",               EnemyRarity.VeryRare, 3471, 347100, 347110, aiParamID: 347101, 2500, ChrSize.Giant,   Label.Animal, Label.Aquatic, Label.Lightning),
            new Enemy("Chaos Bug",                              EnemyRarity.Uncommon, 3480, 348000, 348000, aiParamID: 348000, 200,  ChrSize.Small,   Label.Bug, Label.Demon),
            new Enemy("Chaos Bug (Red Eyes)",                   EnemyRarity.Rare,     3480, 348000, 348010, aiParamID: 348000, 2000, ChrSize.Small,   Label.Bug, Label.Demon),
            new Enemy("Good Vagrant",                           EnemyRarity.Rare,     3490, 349000, 349000, aiParamID: 349000, 500,  ChrSize.Small,   Label.Vagrant),
            new Enemy("Evil Vagrant",                           EnemyRarity.Rare,     3491, 349100, 349100, aiParamID: 349100, 500,  ChrSize.Small,   Label.Vagrant),
            new Enemy("Mass of Souls",                          EnemyRarity.Rare,     3500, 350000, 350000, aiParamID: 350000, 1000, ChrSize.Giant,   Label.Slime),
            // new Enemy("Wisp",                                   EnemyRarity.Uncommon, 3501, 350100, 350100, aiParamID: 350100, ChrSize.Small,   Label.Slime, Label.Magic),  // explodes forever without EMEVD
            new Enemy("Drake (Ground)",                         EnemyRarity.Uncommon, 3520, 352002, 352020, aiParamID: 352002, 500,  ChrSize.Normal,  Label.Dragon, Label.Winged, Label.Lightning),
            new Enemy("Artorias",                               EnemyRarity.Boss,     4100, 410000, 410000, aiParamID: 410000, 5000, ChrSize.Normal,  Label.Sapient, Label.Abyssal),
            new Enemy("Artorias (Mob)",                         EnemyRarity.VeryRare, 4100, 410000, 410010, aiParamID: 410010, 3000, ChrSize.Normal,  Label.Sapient, Label.Abyssal),
            // new Enemy("Hawkeye Gough",                          EnemyRarity.Rare,     4110, 411000, 411000, aiParamID: 411000, ChrSize.Giant,   Label.Giant, Label.Metal),
            new Enemy("Stone Guardian",                         EnemyRarity.Uncommon, 4120, 412000, 412000, aiParamID: 412000, 400,  ChrSize.Normal,  Label.Giant, Label.Stone),
            new Enemy("Scarecrow",                              EnemyRarity.Common,   4130, 413000, 413000, aiParamID: 413000, 100,  ChrSize.Normal,  Label.Plant),
            new Enemy("Bloathead",                              EnemyRarity.Common,   4150, 415000, 415000, aiParamID: 415000, 150,  ChrSize.Normal,  Label.Sapient, Label.Abyssal),
            new Enemy("Bloathead Sorcerer",                     EnemyRarity.Uncommon, 4160, 416000, 416000, aiParamID: 416000, 300,  ChrSize.Normal,  Label.Sapient, Label.Abyssal, Label.Magic),
            new Enemy("Humanity Phantom (Small)",               EnemyRarity.Common,   4170, 417000, 417000, aiParamID: 417000, 50,   ChrSize.Small,   Label.Ghost, Label.Abyssal),
            new Enemy("Humanity Phantom (Medium)",              EnemyRarity.Common,   4171, 417100, 417100, aiParamID: 417100, 100,  ChrSize.Normal,  Label.Ghost, Label.Abyssal),
            new Enemy("Humanity Phantom (Large)",               EnemyRarity.Uncommon, 4172, 417200, 417200, aiParamID: 417200, 300,  ChrSize.Normal,  Label.Ghost, Label.Abyssal),
            new Enemy("Chained Prisoner",                       EnemyRarity.Rare,     4180, 418000, 418000, aiParamID: 418000, 1000, ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Abyssal),
            new Enemy("Abyss Attack Dog",                       EnemyRarity.Uncommon, 4190, 419000, 419000, aiParamID: 419000, 200,  ChrSize.Small,   Label.Animal, Label.Abyssal),
            new Enemy("Manus",                                  EnemyRarity.Boss,     4500, 450000, 450000, aiParamID: 450000, 5000, ChrSize.Giant,   Label.Abyssal),
            new Enemy("Manus (Mob)",                            EnemyRarity.VeryRare, 4500, 450000, 450010, aiParamID: 450000, 3000, ChrSize.Giant,   Label.Abyssal),
            new Enemy("Black Dragon Kalameet",                  EnemyRarity.Boss,     4510, 451000, 451000, aiParamID: 451000, 6000, ChrSize.Titanic, Label.Dragon, Label.Fire),
            new Enemy("Black Dragon Kalameet (Mob)",            EnemyRarity.VeryRare, 4510, 451000, 451010, aiParamID: 451010, 5000, ChrSize.Titanic, Label.Dragon, Label.Fire),
            // new Enemy("Black Dragon Kalameet (Tail)",           EnemyRarity.Boss,     4511, 451100, 451100, aiParamID: 451100, ChrSize.Titanic, Label.Part),
            new Enemy("Centipede Demon",                        EnemyRarity.Boss,     5200, 520000, 520000, aiParamID: 520000, 4000, ChrSize.Titanic, Label.Bug, Label.Demon, Label.Fire),
            new Enemy("Centipede Demon (Mob)",                  EnemyRarity.VeryRare, 5200, 520000, 520010, aiParamID: 520010, 2500, ChrSize.Titanic, Label.Bug, Label.Demon, Label.Fire),
            // new Enemy("Centipede Demon (Arm)",                  EnemyRarity.Boss,     5201, 520100, 520100, aiParamID: 520100, ChrSize.Titanic, Label.Part),
            // new Enemy("Centipede Demon (Tail)",                 EnemyRarity.Boss,     5202, 520200, 520200, aiParamID: 520200, ChrSize.Titanic, Label.Part),
            new Enemy("Sif",                                    EnemyRarity.Boss,     5210, 521000, 521000, aiParamID: 521000, 4000, ChrSize.Titanic, Label.Animal, Label.Abyssal),  // abyssal here; and no mob version
            new Enemy("Gravelord Nito",                         EnemyRarity.Boss,     5220, 522000, 522000, aiParamID: 522000, 5000, ChrSize.Giant,   Label.Skeleton, Label.Magic),
            new Enemy("Gravelord Nito (Mob)",                   EnemyRarity.VeryRare, 5220, 522000, 522010, aiParamID: 522010, 3000, ChrSize.Giant,   Label.Skeleton, Label.Magic),
            new Enemy("Gaping Dragon",                          EnemyRarity.Boss,     5260, 526000, 526000, aiParamID: 526000, 5000, ChrSize.Titanic, Label.Dragon, Label.Infested),
            new Enemy("Gaping Dragon (Mob)",                    EnemyRarity.VeryRare, 5260, 526000, 526010, aiParamID: 526010, 3000, ChrSize.Titanic, Label.Dragon, Label.Infested),
            // new Enemy("Gaping Dragon (Tail)",                   EnemyRarity.Boss,     5261, 526100, 526100, aiParamID: 526100, ChrSize.Titanic, Label.Part),
            new Enemy("Ornstein",                               EnemyRarity.Boss,     5270, 527000, 527000, aiParamID: 527000, 4000, ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Lightning),
            new Enemy("Ornstein (Mob)",                         EnemyRarity.VeryRare, 5270, 527000, 527010, aiParamID: 527010, 2500, ChrSize.Normal,  Label.Sapient, Label.Metal, Label.Lightning),
            new Enemy("Giant Ornstein",                         EnemyRarity.Boss,     5271, 527100, 527100, aiParamID: 527100, 4000, ChrSize.Giant,   Label.Giant, Label.Metal, Label.Lightning),
            new Enemy("Giant Ornstein (Mob)",                   EnemyRarity.VeryRare, 5271, 527100, 527110, aiParamID: 527110, 2500, ChrSize.Giant,   Label.Giant, Label.Metal, Label.Lightning),
            new Enemy("Quelaag",                                EnemyRarity.Boss,     5280, 528000, 528000, aiParamID: 528000, 4000, ChrSize.Giant,   Label.Bug, Label.Demon),
            new Enemy("Quelaag (Mob)",                          EnemyRarity.VeryRare, 5280, 528000, 528010, aiParamID: 528010, 2500, ChrSize.Giant,   Label.Bug, Label.Demon),
            new Enemy("Seath the Scaleless",                    EnemyRarity.Boss,     5290, 529000, 529000, aiParamID: 529000, 5000, ChrSize.Giant,   Label.Dragon, Label.Crystal),
            new Enemy("Seath the Scaleless (Mob)",              EnemyRarity.VeryRare, 5290, 529000, 529010, aiParamID: 529010, 3000, ChrSize.Giant,   Label.Dragon, Label.Crystal),
            new Enemy("Bell Gargoyle",                          EnemyRarity.Boss,     5350, 535000, 535000, aiParamID: 535000, 3000, ChrSize.Giant,   Label.Stone, Label.Winged, Label.Fire),
            new Enemy("Bell Gargoyle (Mob)",                    EnemyRarity.Rare,     5350, 535000, 535010, aiParamID: 535010, 2000, ChrSize.Giant,   Label.Stone, Label.Winged, Label.Fire),  // only rare, not very rare
            new Enemy("Lightning Gargoyle",                     EnemyRarity.Boss,     5351, 535100, 535100, aiParamID: 535100, 3000, ChrSize.Giant,   Label.Stone, Label.Winged, Label.Lightning),
            new Enemy("Lightning Gargoyle (Mob)",               EnemyRarity.VeryRare, 5351, 535100, 535110, aiParamID: 535110, 2000, ChrSize.Giant,   Label.Stone, Label.Winged, Label.Lightning),  // only rare, not very rare
            // new Enemy("Bell Gargoyle (Tail)",                   EnemyRarity.Boss,     5352, 535200, 535200, aiParamID: 535200, ChrSize.Giant,   Label.Part),
            // new Enemy("Lightning Gargoyle (Tail)",              EnemyRarity.Boss,     5353, 535300, 535300, aiParamID: 535300, ChrSize.Giant,   Label.Part),
            new Enemy("Great Feline",                           EnemyRarity.Rare,     5360, 536000, 536000, aiParamID: 536000, 1000, ChrSize.Normal,  Label.Animal),
            new Enemy("Gwyn",                                   EnemyRarity.Boss,     5370, 537000, 537000, aiParamID: 537000, 5000, ChrSize.Normal,  Label.Sapient, Label.Fire),
            new Enemy("Gwyn (Mob)",                             EnemyRarity.VeryRare, 5370, 537000, 537010, aiParamID: 537010, 4000, ChrSize.Normal,  Label.Sapient),
            new Enemy("Four Kings",                             EnemyRarity.Boss,     5390, 539001, 539000, aiParamID: 539000, 4000, ChrSize.Giant,   Label.Abyssal, Label.Magic),
            new Enemy("Four Kings (Mob)",                       EnemyRarity.VeryRare, 5390, 539001, 539010, aiParamID: 539010, 2500, ChrSize.Giant,   Label.Abyssal, Label.Magic),
        };

        public static Dictionary<int, FFXDict> EnemyFFXSources = new Dictionary<int, FFXDict>()
        {
        { 1000, new FFXDict() { } },
        { 1200, new FFXDict() { } },
        { 1201, new FFXDict() { } },
        { 1202, new FFXDict() {
            { 1212000, "FRPG_SfxBnd_m10_00" },
        } },
        { 1203, new FFXDict() {
            { 1120400, "FRPG_SfxBnd_m11" },
            { 1120300, "FRPG_SfxBnd_m11" },
            { 1120500, "FRPG_SfxBnd_m11" },
            { 1120401, "FRPG_SfxBnd_m11" },
        } },
        { 2060, new FFXDict() {
            { 12061, "FRPG_SfxBnd_m14" },
        } },
        { 2210, new FFXDict() { } },
        { 2230, new FFXDict() {
            { 12239, "FRPG_SfxBnd_m18_01" },
            { 12232, "FRPG_SfxBnd_m18_01" },
            { 12234, "FRPG_SfxBnd_m18_01" },
            { 12237, "FRPG_SfxBnd_m18_01" },
            { 12235, "FRPG_SfxBnd_m18_01" },
            { 12238, "FRPG_SfxBnd_m18_01" },
            { 12230, "FRPG_SfxBnd_m18_01" },
            { 12231, "FRPG_SfxBnd_m18_01" },
        } },
        { 2231, new FFXDict() {
            { 11035, "FRPG_SfxBnd_m14_01" },
            { 11030, "FRPG_SfxBnd_m14_01" },
            { 11031, "FRPG_SfxBnd_m14_01" },
            { 11032, "FRPG_SfxBnd_m14_01" },
            { 12239, "FRPG_SfxBnd_m18_01" },
            { 12232, "FRPG_SfxBnd_m18_01" },
            { 12237, "FRPG_SfxBnd_m18_01" },
            { 11036, "FRPG_SfxBnd_m14_01" },
            { 12235, "FRPG_SfxBnd_m18_01" },
            { 12230, "FRPG_SfxBnd_m18_01" },
            { 12238, "FRPG_SfxBnd_m18_01" },
            { 12231, "FRPG_SfxBnd_m18_01" },
        } },
        { 2232, new FFXDict() {
            { 12239, "FRPG_SfxBnd_m18_01" },
            { 12232, "FRPG_SfxBnd_m18_01" },
            { 12237, "FRPG_SfxBnd_m18_01" },
            { 12238, "FRPG_SfxBnd_m18_01" },
        } },
        { 2240, new FFXDict() {
            { 12242, "FRPG_SfxBnd_m14_01" },
            { 12241, "FRPG_SfxBnd_m14_01" },
            { 12240, "FRPG_SfxBnd_m14_01" },
        } },
        { 2250, new FFXDict() {
            { 12258, "FRPG_SfxBnd_m18_00" },
            { 1225000, "FRPG_SfxBnd_m18_00" },
            { 12250, "FRPG_SfxBnd_m18_00" },
        } },
        { 2260, new FFXDict() {
            { 12262, "FRPG_SfxBnd_m15" },
            { 12261, "FRPG_SfxBnd_m15" },
            { 12260, "FRPG_SfxBnd_m15" },
        } },
        { 2270, new FFXDict() { } },
        { 2280, new FFXDict() { } },
        { 2290, new FFXDict() { } },
        { 2300, new FFXDict() {
            { 1223500, "FRPG_SfxBnd_m15" },
            { 1223000, "FRPG_SfxBnd_m15" },
            { 1223600, "FRPG_SfxBnd_m15" },
            { 1223100, "FRPG_SfxBnd_m15" },
            { 12304, "FRPG_SfxBnd_m15" },
            { 12303, "FRPG_SfxBnd_m15" },
            { 12305, "FRPG_SfxBnd_m15" },
            { 12306, "FRPG_SfxBnd_m15" },
        } },
        { 2310, new FFXDict() {
            { 1223200, "FRPG_SfxBnd_m11" },
            { 1223300, "FRPG_SfxBnd_m11" },
        } },
        { 2320, new FFXDict() {
            { 1222000, "FRPG_SfxBnd_m15_00" },
            { 12320, "FRPG_SfxBnd_m15_00" },
            { 12322, "FRPG_SfxBnd_m15_00" },
            { 12325, "FRPG_SfxBnd_m15_00" },
            { 12324, "FRPG_SfxBnd_m15_00" },
            { 12321, "FRPG_SfxBnd_m15_00" },
        } },
        { 2330, new FFXDict() {
            { 12330, "FRPG_SfxBnd_m12" },
        } },
        { 2360, new FFXDict() {
            { 12364, "FRPG_SfxBnd_m15_01" },
            { 12365, "FRPG_SfxBnd_m15_01" },
            { 12360, "FRPG_SfxBnd_m15_01" },
            { 12362, "FRPG_SfxBnd_m15_01" },
            { 12363, "FRPG_SfxBnd_m15_01" },
        } },
        { 2370, new FFXDict() {
            { 12373, "FRPG_SfxBnd_m17" },
            { 12371, "FRPG_SfxBnd_m17" },
            { 12370, "FRPG_SfxBnd_m17" },
            { 12374, "FRPG_SfxBnd_m17" },
            { 12372, "FRPG_SfxBnd_m17" },
            { 12375, "FRPG_SfxBnd_m17" },
            { 12376, "FRPG_SfxBnd_m17" },
        } },
        { 2380, new FFXDict() {
            { 12383, "FRPG_SfxBnd_m12" },
            { 12382, "FRPG_SfxBnd_m12" },
            { 12380, "FRPG_SfxBnd_m12" },
        } },
        { 2390, new FFXDict() {
            { 12390, "FRPG_SfxBnd_m18" },
            { 12391, "FRPG_SfxBnd_m18" },
            { 12392, "FRPG_SfxBnd_m18" },
        } },
        { 2400, new FFXDict() {
            { 12522, "FRPG_SfxBnd_m15_01" },
            { 12521, "FRPG_SfxBnd_m15_01" },
            { 12520, "FRPG_SfxBnd_m15_01" },
        } },
        { 2410, new FFXDict() {
            { 12411, "FRPG_SfxBnd_m15_01" },
            { 12410, "FRPG_SfxBnd_m15_01" },
        } },
        { 2430, new FFXDict() {
            { 12430, "FRPG_SfxBnd_m14_01" },
        } },
        { 2500, new FFXDict() {
            { 12500, "FRPG_SfxBnd_m18_01" },
        } },
        { 2510, new FFXDict() { } },
        { 2520, new FFXDict() {
            { 12522, "FRPG_SfxBnd_m15_01" },
            { 12521, "FRPG_SfxBnd_m15_01" },
            { 12520, "FRPG_SfxBnd_m15_01" },
            { 12523, "FRPG_SfxBnd_m10_01" },
        } },
        { 2530, new FFXDict() {
            { 12532, "FRPG_SfxBnd_m14" },
            { 12531, "FRPG_SfxBnd_m14" },
            { 12530, "FRPG_SfxBnd_m14" },
        } },
        { 2540, new FFXDict() {
            { 12540, "FRPG_SfxBnd_m11" },
        } },
        { 2550, new FFXDict() { } },
        { 2560, new FFXDict() { } },
        { 2570, new FFXDict() { } },
        { 2590, new FFXDict() { } },
        { 2591, new FFXDict() { } },
        { 2600, new FFXDict() { } },
        { 2640, new FFXDict() {
            { 12865, "FRPG_SfxBnd_m15_01" },
        } },
        { 2650, new FFXDict() {
            { 12653, "FRPG_SfxBnd_m13" },
            { 12651, "FRPG_SfxBnd_m13" },
            { 12650, "FRPG_SfxBnd_m13" },
            { 12654, "FRPG_SfxBnd_m13" },
            { 12652, "FRPG_SfxBnd_m13" },
        } },
        { 2660, new FFXDict() {
            { 12660, "FRPG_SfxBnd_m10_00" },
            { 12661, "FRPG_SfxBnd_m10_00" },
        } },
        { 2670, new FFXDict() {
            { 12672, "FRPG_SfxBnd_m16" },
            { 12673, "FRPG_SfxBnd_m16" },
            { 12671, "FRPG_SfxBnd_m16" },
            { 12670, "FRPG_SfxBnd_m16" },
            { 12674, "FRPG_SfxBnd_m16" },
        } },
        { 2680, new FFXDict() {
            { 12672, "FRPG_SfxBnd_m16" },
            { 12673, "FRPG_SfxBnd_m16" },
            { 12681, "FRPG_SfxBnd_m16" },
            { 12680, "FRPG_SfxBnd_m16" },
            { 12682, "FRPG_SfxBnd_m16" },
        } },
        { 2690, new FFXDict() { } },
        { 2700, new FFXDict() {
            { 12701, "FRPG_SfxBnd_m17" },
            { 12700, "FRPG_SfxBnd_m17" },
            { 12703, "FRPG_SfxBnd_m17" },
            { 12702, "FRPG_SfxBnd_m17" },
            { 12704, "FRPG_SfxBnd_m17" },
        } },
        { 2710, new FFXDict() {
            { 12714, "FRPG_SfxBnd_m17" },
            { 12713, "FRPG_SfxBnd_m17" },
        } },
        { 2711, new FFXDict() {
            { 12711, "FRPG_SfxBnd_m17" },
            { 12710, "FRPG_SfxBnd_m17" },
            { 12712, "FRPG_SfxBnd_m17" },
        } },
        { 2730, new FFXDict() {
            { 1273000, "FRPG_SfxBnd_m11" },
            { 1273100, "FRPG_SfxBnd_m11" },
            { 12730, "FRPG_SfxBnd_m11" },
            { 12733, "FRPG_SfxBnd_m11" },
            { 12732, "FRPG_SfxBnd_m11" },
        } },
        { 2731, new FFXDict() { } },
        { 2750, new FFXDict() {
            { 12750, "FRPG_SfxBnd_m10_02" },
        } },
        { 2780, new FFXDict() {
            { 12780, "FRPG_SfxBnd_m17" },
        } },
        { 2790, new FFXDict() { } },
        { 2791, new FFXDict() {
            { 12790, "FRPG_SfxBnd_m18_00" },
        } },
        { 2792, new FFXDict() { } },
        { 2793, new FFXDict() { } },
        { 2794, new FFXDict() { } },
        { 2795, new FFXDict() { } },
        { 2800, new FFXDict() { } },
        { 2810, new FFXDict() { } },
        { 2811, new FFXDict() {
            { 12812, "FRPG_SfxBnd_m14" },
            { 12811, "FRPG_SfxBnd_m14" },
            { 12810, "FRPG_SfxBnd_m14" },
        } },
        { 2820, new FFXDict() {
        } },
        { 2830, new FFXDict() {
            { 12832, "FRPG_SfxBnd_m11" },
            { 12831, "FRPG_SfxBnd_m11" },
            { 12830, "FRPG_SfxBnd_m11" },
        } },
        { 2840, new FFXDict() {
            { 12500, "FRPG_SfxBnd_m18_01" },
            { 12849, "FRPG_SfxBnd_m11" },
            { 12846, "FRPG_SfxBnd_m11" },
            { 12841, "FRPG_SfxBnd_m11" },
            { 12840, "FRPG_SfxBnd_m11" },
            { 12843, "FRPG_SfxBnd_m11" },
            { 12842, "FRPG_SfxBnd_m11" },
            { 12844, "FRPG_SfxBnd_m11" },
            { 12847, "FRPG_SfxBnd_m11" },
        } },
        { 2860, new FFXDict() {
            { 12859, "FRPG_SfxBnd_m15_00" },
            { 12865, "FRPG_SfxBnd_m15_01" },
            { 12864, "FRPG_SfxBnd_m15_01" },
        } },
        { 2870, new FFXDict() {
            { 12870, "FRPG_SfxBnd_m15_01" },
            { 12872, "FRPG_SfxBnd_m15_01" },
            { 12876, "FRPG_SfxBnd_m15_01" },
            { 12873, "FRPG_SfxBnd_m15_01" },
            { 12874, "FRPG_SfxBnd_m15_01" },
            { 12875, "FRPG_SfxBnd_m15_01" },
        } },
        { 2900, new FFXDict() {
            { 12900, "FRPG_SfxBnd_m13" },
            { 4600, "FRPG_SfxBnd_m13" },
            { 12901, "FRPG_SfxBnd_m13" },
        } },
        { 2910, new FFXDict() {
            { 12914, "FRPG_SfxBnd_m13" },
            { 12901, "FRPG_SfxBnd_m13" },
            { 12911, "FRPG_SfxBnd_m13" },
            { 12910, "FRPG_SfxBnd_m13" },
        } },
        { 2920, new FFXDict() {
            { 12865, "FRPG_SfxBnd_m15_01" },
        } },
        { 2930, new FFXDict() { } },
        { 2940, new FFXDict() { } },
        { 2950, new FFXDict() { } },
        { 2960, new FFXDict() {
            { 12960, "FRPG_SfxBnd_m13" },
        } },
        { 3090, new FFXDict() {
            { 13090, "FRPG_SfxBnd_m14" },
        } },
        { 3110, new FFXDict() {
            { 13110, "FRPG_SfxBnd_m17" },
        } },
        { 3200, new FFXDict() {
            { 13200, "FRPG_SfxBnd_m10_00" },
            { 13202, "FRPG_SfxBnd_m10_00" },
            { 13201, "FRPG_SfxBnd_m10_00" },
        } },
        { 3210, new FFXDict() {
            { 13211, "FRPG_SfxBnd_m14" },
        } },
        { 3220, new FFXDict() {
            { 13090, "FRPG_SfxBnd_m14" },
        } },
        { 3230, new FFXDict() {
            { 13232, "FRPG_SfxBnd_m17" },
            { 13237, "FRPG_SfxBnd_m17" },
            { 13235, "FRPG_SfxBnd_m17" },
            { 13233, "FRPG_SfxBnd_m17" },
            { 13234, "FRPG_SfxBnd_m17" },
            { 13236, "FRPG_SfxBnd_m17" },
            { 13238, "FRPG_SfxBnd_m17" },
            { 13239, "FRPG_SfxBnd_m17" },
            { 13228, "FRPG_SfxBnd_m17" },
            { 13226, "FRPG_SfxBnd_m17" },
            { 13227, "FRPG_SfxBnd_m17" },
            { 13229, "FRPG_SfxBnd_m17" },
        } },
        { 3240, new FFXDict() {
            { 13240, "FRPG_SfxBnd_m14_01" },
            { 13242, "FRPG_SfxBnd_m14_01" },
            { 13243, "FRPG_SfxBnd_m14_01" },
        } },
        { 3250, new FFXDict() {
            { 13250, "FRPG_SfxBnd_m17" },
        } },
        { 3270, new FFXDict() {
            { 13270, "FRPG_SfxBnd_m13_02" },
            { 13271, "FRPG_SfxBnd_m13_02" },
            { 13272, "FRPG_SfxBnd_m13_02" },
        } },
        { 3290, new FFXDict() {
            { 1329000, "FRPG_SfxBnd_m14_00" },
            { 13290, "FRPG_SfxBnd_m14_00" },
            { 13292, "FRPG_SfxBnd_m14_00" },
            { 13291, "FRPG_SfxBnd_m14_00" },
        } },
        { 3300, new FFXDict() {
            { 13110, "FRPG_SfxBnd_m17" },
        } },
        { 3320, new FFXDict() {
            { 13320, "FRPG_SfxBnd_m13_01" },
            { 13325, "FRPG_SfxBnd_m13_01" },
            { 13322, "FRPG_SfxBnd_m13_01" },
            { 13321, "FRPG_SfxBnd_m13_01" },
            { 13318, "FRPG_SfxBnd_m13_01" },
            { 13326, "FRPG_SfxBnd_m13_01" },
            { 13323, "FRPG_SfxBnd_m13_01" },
            { 13319, "FRPG_SfxBnd_m13_01" },
            { 13327, "FRPG_SfxBnd_m13_01" },
            { 13314, "FRPG_SfxBnd_m13_01" },
            { 13315, "FRPG_SfxBnd_m13_01" },
            { 13328, "FRPG_SfxBnd_m13_01" },
            { 13317, "FRPG_SfxBnd_m13_01" },
            { 13316, "FRPG_SfxBnd_m13_01" },
            { 13329, "FRPG_SfxBnd_m13_01" },
        } },
        { 3330, new FFXDict() {
            { 13331, "FRPG_SfxBnd_m17" },
            { 13330, "FRPG_SfxBnd_m17" },
            { 13332, "FRPG_SfxBnd_m17" },
        } },
        { 3340, new FFXDict() { } },
        { 3341, new FFXDict() {
            { 13341, "FRPG_SfxBnd_m14" },
            { 13340, "FRPG_SfxBnd_m14" },
        } },
        { 3350, new FFXDict() { } },
        { 3370, new FFXDict() { } },
        { 3380, new FFXDict() {
            { 13380, "FRPG_SfxBnd_m14" },
        } },
        { 3390, new FFXDict() {
            { 13391, "FRPG_SfxBnd_m14" },
            { 13390, "FRPG_SfxBnd_m14" },
            { 13397, "FRPG_SfxBnd_m14" },
            { 13396, "FRPG_SfxBnd_m14" },
            { 13392, "FRPG_SfxBnd_m14" },
            { 13395, "FRPG_SfxBnd_m14" },
            { 13398, "FRPG_SfxBnd_m14" },
            { 13399, "FRPG_SfxBnd_m14" },
        } },
        { 3400, new FFXDict() {
            { 13400, "FRPG_SfxBnd_m14" },
            { 13401, "FRPG_SfxBnd_m14" },
            { 13402, "FRPG_SfxBnd_m14" },
        } },
        { 3410, new FFXDict() {
            { 13411, "FRPG_SfxBnd_m12" },
            { 1341100, "FRPG_SfxBnd_m12" },
            { 1341200, "FRPG_SfxBnd_m12" },
            { 13410, "FRPG_SfxBnd_m12" },
        } },
        { 3420, new FFXDict() {
            { 13422, "FRPG_SfxBnd_m11" },
            { 13423, "FRPG_SfxBnd_m11" },
            { 16005, "FRPG_SfxBnd_m11" },
            { 13421, "FRPG_SfxBnd_m16" },
            { 13426, "FRPG_SfxBnd_m11" },
            { 13427, "FRPG_SfxBnd_m11" },
            { 13420, "FRPG_SfxBnd_m16" },
            { 13428, "FRPG_SfxBnd_m11" },
            { 13429, "FRPG_SfxBnd_m16" },
            { 16006, "FRPG_SfxBnd_m16" },
            { 16007, "FRPG_SfxBnd_m16" },
            { 13424, "FRPG_SfxBnd_m11" },
            { 16009, "FRPG_SfxBnd_m16" },
            { 16013, "FRPG_SfxBnd_m16" },
            { 16010, "FRPG_SfxBnd_m16" },
            { 16011, "FRPG_SfxBnd_m16" },
            { 16012, "FRPG_SfxBnd_m16" },
        } },
        { 3421, new FFXDict() {
            { 1342000, "FRPG_SfxBnd_m14" },
        } },
        { 3422, new FFXDict() { } },
        { 3430, new FFXDict() {
            { 15130, "FRPG_SfxBnd_m10_01" },
            { 15131, "FRPG_SfxBnd_m10_01" },
            { 15136, "FRPG_SfxBnd_m10_01" },
            { 15135, "FRPG_SfxBnd_m10_01" },
            { 15138, "FRPG_SfxBnd_m10_01" },
            { 15143, "FRPG_SfxBnd_m10_01" },
            { 15140, "FRPG_SfxBnd_m10_01" },
            { 15141, "FRPG_SfxBnd_m10_01" },
            { 15142, "FRPG_SfxBnd_m10_01" },
            { 15151, "FRPG_SfxBnd_m10_01" },
            { 15155, "FRPG_SfxBnd_m10_01" },
            { 15163, "FRPG_SfxBnd_m10_01" },
            { 15164, "FRPG_SfxBnd_m10_01" },
            { 15167, "FRPG_SfxBnd_m10_01" },
            { 15166, "FRPG_SfxBnd_m10_01" },
            { 15170, "FRPG_SfxBnd_m10_01" },
            { 15171, "FRPG_SfxBnd_m10_01" },
            { 15174, "FRPG_SfxBnd_m10_01" },
            { 15175, "FRPG_SfxBnd_m10_01" },
            { 15148, "FRPG_SfxBnd_m10_01" },
            { 15149, "FRPG_SfxBnd_m10_01" },
            { 15147, "FRPG_SfxBnd_m10_01" },
            { 15177, "FRPG_SfxBnd_m10_01" },
            { 15176, "FRPG_SfxBnd_m13_02" },
        } },
        { 3431, new FFXDict() {
            { 15176, "FRPG_SfxBnd_m13_02" },
        } },
        { 3440, new FFXDict() { } },
        { 3450, new FFXDict() {
            { 13452, "FRPG_SfxBnd_m13_02" },
            { 13453, "FRPG_SfxBnd_m13_02" },
            { 13450, "FRPG_SfxBnd_m13_02" },
            { 13451, "FRPG_SfxBnd_m13_02" },
            { 15176, "FRPG_SfxBnd_m13_02" },
        } },
        { 3451, new FFXDict() { } },
        { 3460, new FFXDict() {
            { 13461, "FRPG_SfxBnd_m17" },
            { 13466, "FRPG_SfxBnd_m17" },
            { 13462, "FRPG_SfxBnd_m17" },
            { 13463, "FRPG_SfxBnd_m17" },
            { 13460, "FRPG_SfxBnd_m17" },
            { 13467, "FRPG_SfxBnd_m17" },
            { 13464, "FRPG_SfxBnd_m17" },
            { 13465, "FRPG_SfxBnd_m17" },
            { 13468, "FRPG_SfxBnd_m17" },
        } },
        { 3461, new FFXDict() {
            { 13461, "FRPG_SfxBnd_m17" },
            { 13466, "FRPG_SfxBnd_m17" },
            { 13462, "FRPG_SfxBnd_m17" },
            { 13463, "FRPG_SfxBnd_m17" },
            { 13460, "FRPG_SfxBnd_m17" },
            { 13467, "FRPG_SfxBnd_m17" },
            { 13464, "FRPG_SfxBnd_m17" },
            { 13465, "FRPG_SfxBnd_m17" },
            { 13468, "FRPG_SfxBnd_m17" },
        } },
        //{ 3470, new FFXDict() {
        //    { 12304, "FRPG_SfxBnd_m15" },
        //    { 12303, "FRPG_SfxBnd_m15" },
        //} },
        { 3471, new FFXDict() { } },
        { 3472, new FFXDict() { } },
        { 3480, new FFXDict() {
            { 13480, "FRPG_SfxBnd_m14_01" },
            { 13481, "FRPG_SfxBnd_m14_01" },
        } },
        { 3490, new FFXDict() { } },
        { 3491, new FFXDict() { } },
        { 3500, new FFXDict() {
            { 13501, "FRPG_SfxBnd_m16" },
            { 13503, "FRPG_SfxBnd_m16" },
            { 13500, "FRPG_SfxBnd_m16" },
        } },
        { 3501, new FFXDict() {
            { 13507, "FRPG_SfxBnd_m16" },
            { 13506, "FRPG_SfxBnd_m16" },
            { 13509, "FRPG_SfxBnd_m16" },
        } },
        { 3510, new FFXDict() { } },
        { 3520, new FFXDict() {
            { 13522, "FRPG_SfxBnd_m16" },
            { 13520, "FRPG_SfxBnd_m16" },
            { 13521, "FRPG_SfxBnd_m16" },
            { 13523, "FRPG_SfxBnd_m16" },
        } },
        { 3530, new FFXDict() {
            { 13540, "FRPG_SfxBnd_m13_02" },
            { 13537, "FRPG_SfxBnd_m13_02" },
            { 13530, "FRPG_SfxBnd_m13_02" },
            { 13533, "FRPG_SfxBnd_m13_02" },
            { 13539, "FRPG_SfxBnd_m13_02" },
            { 13536, "FRPG_SfxBnd_m13_02" },
        } },
        { 3531, new FFXDict() {
            { 13541, "FRPG_SfxBnd_m13_02" },
            { 13534, "FRPG_SfxBnd_m13_02" },
        } },
        { 4090, new FFXDict() {
            { 14292, "FRPG_SfxBnd_m12_01" },
            { 14291, "FRPG_SfxBnd_m12_01" },
            { 14290, "FRPG_SfxBnd_m12_01" },
        } },
        { 4100, new FFXDict() { } },
        { 4110, new FFXDict() {
            { 14110, "FRPG_SfxBnd_m12_01" },
            { 14111, "FRPG_SfxBnd_m12_01" },
            { 14112, "FRPG_SfxBnd_m12_01" },
            { 14113, "FRPG_SfxBnd_m12_01" },
            { 14114, "FRPG_SfxBnd_m12_01" },
            { 14115, "FRPG_SfxBnd_m12_01" },
        } },
        { 4120, new FFXDict() {
            { 1412100, "FRPG_SfxBnd_m12_01" },
            { 1412000, "FRPG_SfxBnd_m12_01" },
            { 12385, "FRPG_SfxBnd_m12_01" },
            { 12384, "FRPG_SfxBnd_m12_01" },
        } },
        { 4130, new FFXDict() {
            { 14230, "FRPG_SfxBnd_m12_01" },
            { 14231, "FRPG_SfxBnd_m12_01" },
            { 14232, "FRPG_SfxBnd_m12_01" },
        } },
        { 4140, new FFXDict() { } },
        { 4150, new FFXDict() {
            { 14150, "FRPG_SfxBnd_m12_01" },
        } },
        { 4160, new FFXDict() {
            { 14255, "FRPG_SfxBnd_m12_01" },
            { 14251, "FRPG_SfxBnd_m12_01" },
            { 14250, "FRPG_SfxBnd_m12_01" },
            { 14256, "FRPG_SfxBnd_m12_01" },
            { 14254, "FRPG_SfxBnd_m12_01" },
            { 14252, "FRPG_SfxBnd_m12_01" },
            { 14150, "FRPG_SfxBnd_m12_01" },
        } },
        { 4170, new FFXDict() {
            { 14260, "FRPG_SfxBnd_m12_01" },
            { 14261, "FRPG_SfxBnd_m12_01" },
            { 14267, "FRPG_SfxBnd_m12_01" },
            { 14278, "FRPG_SfxBnd_m12_01" },
        } },
        { 4171, new FFXDict() {
            { 14270, "FRPG_SfxBnd_m12_01" },
            { 14271, "FRPG_SfxBnd_m12_01" },
            { 14268, "FRPG_SfxBnd_m12_01" },
            { 14277, "FRPG_SfxBnd_m12_01" },
        } },
        { 4172, new FFXDict() {
            { 14280, "FRPG_SfxBnd_m12_01" },
            { 14281, "FRPG_SfxBnd_m12_01" },
            { 14269, "FRPG_SfxBnd_m12_01" },
            { 14277, "FRPG_SfxBnd_m12_01" },
        } },
        { 4180, new FFXDict() {
            { 1412000, "FRPG_SfxBnd_m12_01" },
            { 14181, "FRPG_SfxBnd_m12_01" },
        } },
        { 4190, new FFXDict() {
            { 14190, "FRPG_SfxBnd_m12_01" },
        } },
        { 4500, new FFXDict() { } },
        { 4510, new FFXDict() {
            { 14430, "FRPG_SfxBnd_m12_01" },
            { 14412, "FRPG_SfxBnd_m12_01" },
            { 14411, "FRPG_SfxBnd_m12_01" },
            { 14410, "FRPG_SfxBnd_m12_01" },
        } },
        { 4511, new FFXDict() { } },
        { 4520, new FFXDict() {
            { 14521, "FRPG_SfxBnd_m12_01" },
            { 14522, "FRPG_SfxBnd_m12_01" },
            { 14520, "FRPG_SfxBnd_m12_01" },
        } },
        { 4531, new FFXDict() {
            { 15365, "FRPG_SfxBnd_m12_01" },
            { 15364, "FRPG_SfxBnd_m12_01" },
            { 15363, "FRPG_SfxBnd_m12" },
        } },
        { 5200, new FFXDict() {
            { 15204, "FRPG_SfxBnd_m14_01" },
            { 15208, "FRPG_SfxBnd_m14" },
            { 15207, "FRPG_SfxBnd_m14" },
            { 1520000, "FRPG_SfxBnd_m14" },
            { 1520100, "FRPG_SfxBnd_m14" },
            { 15205, "FRPG_SfxBnd_m14" },
            { 15209, "FRPG_SfxBnd_m14" },
            { 15203, "FRPG_SfxBnd_m14" },
            { 15300, "FRPG_SfxBnd_m14" },
            { 15202, "FRPG_SfxBnd_m14" },
            { 15201, "FRPG_SfxBnd_m14" },
            { 15200, "FRPG_SfxBnd_m14" },
            { 15303, "FRPG_SfxBnd_m14" },
            { 15302, "FRPG_SfxBnd_m14" },
            { 15301, "FRPG_SfxBnd_m14" },
            { 15304, "FRPG_SfxBnd_m14" },
            { 15306, "FRPG_SfxBnd_m14" },
            { 15307, "FRPG_SfxBnd_m14" },
        } },
        { 5201, new FFXDict() {
            { 1520000, "FRPG_SfxBnd_m14" },
            { 1520100, "FRPG_SfxBnd_m14" },
            { 15306, "FRPG_SfxBnd_m14" },
            { 15300, "FRPG_SfxBnd_m14" },
        } },
        { 5202, new FFXDict() {
            { 1520000, "FRPG_SfxBnd_m14" },
            { 1520100, "FRPG_SfxBnd_m14" },
            { 15306, "FRPG_SfxBnd_m14" },
        } },
        { 5210, new FFXDict() {
            { 15211, "FRPG_SfxBnd_m12" },
            { 1521100, "FRPG_SfxBnd_m12" },
            { 1521000, "FRPG_SfxBnd_m12" },
            { 1521200, "FRPG_SfxBnd_m12" },
            { 15210, "FRPG_SfxBnd_m12" },
        } },
        { 5220, new FFXDict() {
            { 15220, "FRPG_SfxBnd_m13" },
            { 15221, "FRPG_SfxBnd_m13" },
            { 15225, "FRPG_SfxBnd_m13" },
            { 15223, "FRPG_SfxBnd_m13" },
            { 15228, "FRPG_SfxBnd_m13" },
            { 15229, "FRPG_SfxBnd_m13" },
            { 15227, "FRPG_SfxBnd_m13" },
            { 17222, "FRPG_SfxBnd_m13" },
            { 17220, "FRPG_SfxBnd_m13" },
            { 17225, "FRPG_SfxBnd_m13" },
            { 17221, "FRPG_SfxBnd_m13" },
            { 17223, "FRPG_SfxBnd_m13" },
            { 17224, "FRPG_SfxBnd_m13" },
            { 17226, "FRPG_SfxBnd_m13" },
            { 15226, "FRPG_SfxBnd_m13" },
        } },
        { 5230, new FFXDict() {
            { 15233, "FRPG_SfxBnd_m14" },
            { 15236, "FRPG_SfxBnd_m14_01" },
            { 15234, "FRPG_SfxBnd_m14_01" },
            { 15232, "FRPG_SfxBnd_m14_01" },
        } },
        { 5231, new FFXDict() {
            { 15233, "FRPG_SfxBnd_m14" },
            { 15234, "FRPG_SfxBnd_m14_01" },
        } },
        { 5240, new FFXDict() { } },
        { 5250, new FFXDict() {
            { 15252, "FRPG_SfxBnd_m14_01" },
            { 15248, "FRPG_SfxBnd_m14_01" },
            { 1525000, "FRPG_SfxBnd_m14_01" },
            { 15258, "FRPG_SfxBnd_m14_01" },
            { 15257, "FRPG_SfxBnd_m14_01" },
            { 15250, "FRPG_SfxBnd_m14_01" },
            { 15254, "FRPG_SfxBnd_m14_01" },
            { 15249, "FRPG_SfxBnd_m14_01" },
            { 15242, "FRPG_SfxBnd_m14_01" },
            { 15247, "FRPG_SfxBnd_m14_01" },
            { 15246, "FRPG_SfxBnd_m14_01" },
            { 15256, "FRPG_SfxBnd_m14_01" },
            { 15259, "FRPG_SfxBnd_m14_01" },
        } },
        { 5260, new FFXDict() {
            { 1526000, "FRPG_SfxBnd_m10_00" },
            { 1526100, "FRPG_SfxBnd_m10_00" },
            { 15262, "FRPG_SfxBnd_m10_00" },
            { 15263, "FRPG_SfxBnd_m10_00" },
            { 15264, "FRPG_SfxBnd_m10_00" },
            { 15260, "FRPG_SfxBnd_m10_00" },
            { 15261, "FRPG_SfxBnd_m10_00" },
            { 15510, "FRPG_SfxBnd_m10_00" },
        } },
        { 5261, new FFXDict() {
            { 15510, "FRPG_SfxBnd_m10_00" },
        } },
        { 5270, new FFXDict() {
            { 15276, "FRPG_SfxBnd_m15_01" },
            { 15273, "FRPG_SfxBnd_m15_01" },
            { 15244, "FRPG_SfxBnd_m15_01" },
            { 15243, "FRPG_SfxBnd_m15_01" },
            { 15270, "FRPG_SfxBnd_m15_01" },
        } },
        { 5271, new FFXDict() {
            { 15274, "FRPG_SfxBnd_m15_01" },
            { 15275, "FRPG_SfxBnd_m15_01" },
            { 15276, "FRPG_SfxBnd_m15_01" },
            { 15279, "FRPG_SfxBnd_m15_01" },
            { 15278, "FRPG_SfxBnd_m15_01" },
            { 15272, "FRPG_SfxBnd_m15_01" },
            { 15271, "FRPG_SfxBnd_m15_01" },
            { 15277, "FRPG_SfxBnd_m15_01" },
            { 15269, "FRPG_SfxBnd_m15_01" },
            { 15267, "FRPG_SfxBnd_m15_01" },
            { 15268, "FRPG_SfxBnd_m15_01" },
            { 15245, "FRPG_SfxBnd_m15_01" },
        } },
        { 5280, new FFXDict() {
            { 15286, "FRPG_SfxBnd_m14_00" },
            { 15287, "FRPG_SfxBnd_m14_00" },
            { 16001, "FRPG_SfxBnd_m14_00" },
            { 15280, "FRPG_SfxBnd_m14_00" },
            { 16000, "FRPG_SfxBnd_m14_00" },
            { 15281, "FRPG_SfxBnd_m14_00" },
            { 15282, "FRPG_SfxBnd_m14_00" },
            { 15289, "FRPG_SfxBnd_m14_00" },
            { 15283, "FRPG_SfxBnd_m14_00" },
            { 16003, "FRPG_SfxBnd_m14_00" },
            { 15288, "FRPG_SfxBnd_m14_00" },
            { 15285, "FRPG_SfxBnd_m14_00" },
            { 15284, "FRPG_SfxBnd_m14_00" },
        } },
        { 5290, new FFXDict() {
            { 15299, "FRPG_SfxBnd_m17" },
            { 15290, "FRPG_SfxBnd_m17" },
            { 15294, "FRPG_SfxBnd_m17" },
            { 15297, "FRPG_SfxBnd_m17" },
            { 15904, "FRPG_SfxBnd_m17" },
            { 15293, "FRPG_SfxBnd_m17" },
            { 15298, "FRPG_SfxBnd_m17" },
            { 15903, "FRPG_SfxBnd_m17" },
            { 15905, "FRPG_SfxBnd_m17" },
        } },
        { 5291, new FFXDict() {
            { 15903, "FRPG_SfxBnd_m17" },
        } },
        { 5300, new FFXDict() {
            { 15308, "FRPG_SfxBnd_m18" },
            { 15309, "FRPG_SfxBnd_m18" },
        } },
        { 5310, new FFXDict() {
            { 15310, "FRPG_SfxBnd_m15_01" },
            { 15311, "FRPG_SfxBnd_m15_01" },
        } },
        { 5320, new FFXDict() {
            { 15321, "FRPG_SfxBnd_m15_01" },
            { 15320, "FRPG_SfxBnd_m15_01" },
            { 15322, "FRPG_SfxBnd_m15_01" },
            { 15326, "FRPG_SfxBnd_m15_01" },
            { 15325, "FRPG_SfxBnd_m15_01" },
            { 15324, "FRPG_SfxBnd_m15_01" },
            { 15327, "FRPG_SfxBnd_m15_01" },
            { 15329, "FRPG_SfxBnd_m15_01" },
            { 15328, "FRPG_SfxBnd_m15_01" },
        } },
        { 5330, new FFXDict() { } },
        { 5340, new FFXDict() { } },
        { 5350, new FFXDict() {
            { 15369, "FRPG_SfxBnd_m15_01" },
            { 15351, "FRPG_SfxBnd_m15_01" },
            { 15350, "FRPG_SfxBnd_m15_01" },
            { 15358, "FRPG_SfxBnd_m15_01" },
            { 15354, "FRPG_SfxBnd_m15_01" },
            { 15359, "FRPG_SfxBnd_m15_01" },
            { 15355, "FRPG_SfxBnd_m15_01" },
            { 15353, "FRPG_SfxBnd_m15_01" },
            { 41100, "FRPG_SfxBnd_m10_01" },
            { 15368, "FRPG_SfxBnd_m15_01" },
        } },
        { 5351, new FFXDict() {
            { 15369, "FRPG_SfxBnd_m15_01" },
            { 15351, "FRPG_SfxBnd_m15_01" },
            { 15348, "FRPG_SfxBnd_m15_01" },
            { 15347, "FRPG_SfxBnd_m15_01" },
            { 15355, "FRPG_SfxBnd_m15_01" },
            { 15368, "FRPG_SfxBnd_m15_01" },
        } },
        { 5352, new FFXDict() {
            { 15368, "FRPG_SfxBnd_m15_01" },
        } },
        { 5353, new FFXDict() {
            { 15368, "FRPG_SfxBnd_m15_01" },
        } },
        { 5360, new FFXDict() {
            { 15360, "FRPG_SfxBnd_m12" },
            { 15361, "FRPG_SfxBnd_m12" },
        } },
        { 5361, new FFXDict() {
            { 15363, "FRPG_SfxBnd_m12" },
        } },
        { 5370, new FFXDict() {
            { 15371, "FRPG_SfxBnd_m18_00" },
            { 15373, "FRPG_SfxBnd_m18_00" },
            { 15375, "FRPG_SfxBnd_m18_00" },
            { 15374, "FRPG_SfxBnd_m18_00" },
        } },
        { 5390, new FFXDict() {
            { 15403, "FRPG_SfxBnd_m16" },
            { 15388, "FRPG_SfxBnd_m16" },
            { 15389, "FRPG_SfxBnd_m16" },
            { 15398, "FRPG_SfxBnd_m16" },
            { 15395, "FRPG_SfxBnd_m16" },
            { 15391, "FRPG_SfxBnd_m16" },
            { 15390, "FRPG_SfxBnd_m16" },
            { 15401, "FRPG_SfxBnd_m16" },
            { 15400, "FRPG_SfxBnd_m16" },
            { 15402, "FRPG_SfxBnd_m16" },
            { 15404, "FRPG_SfxBnd_m16" },
        } },
        { 5400, new FFXDict() {
            { 15410, "FRPG_SfxBnd_m14_01" },
            { 15419, "FRPG_SfxBnd_m14_01" },
            { 15417, "FRPG_SfxBnd_m14_01" },
            { 15418, "FRPG_SfxBnd_m14_01" },
            { 15421, "FRPG_SfxBnd_m14_01" },
            { 15422, "FRPG_SfxBnd_m14_01" },
            { 15412, "FRPG_SfxBnd_m14_01" },
            { 15411, "FRPG_SfxBnd_m14_01" },
            { 15414, "FRPG_SfxBnd_m14_01" },
            { 15423, "FRPG_SfxBnd_m14_01" },
            { 15416, "FRPG_SfxBnd_m14_01" },
            { 15415, "FRPG_SfxBnd_m14_01" },
        } },
        { 5401, new FFXDict() {
            { 15425, "FRPG_SfxBnd_m14_01" },
            { 15424, "FRPG_SfxBnd_m14_01" },
        } },
        };

        public static List<Boss> BossList { get; } = new List<Boss>()
        {
            // Only one boss in a given category can appear per run.
            // Also note that Pinwheel has been demoted.
            new Boss("Stray Demon",                     0,  2,  2231, ArenaSize.Medium, false),  // note name ID is swapped with Firesage
            new Boss("Demon Firesage",                  0,  2,  2230, ArenaSize.Medium, false),
            // new Boss("Asylum Demon",                    0,  1,  2232, ArenaSize.Medium, false),
            new Boss("Capra Demon",                     1,  3,  2240, ArenaSize.Small,  false),
            new Boss("Taurus Demon",                    2,  3,  2250, ArenaSize.Small, false),
            new Boss("Iron Golem",                      3,  2,  2320, ArenaSize.Medium, false),
            new Boss("Executioner Smough",              4,  3,  2360, ArenaSize.Large,  false),
            new Boss("Executioner Smough (Lightning)",  4,  3,  2361, ArenaSize.Large,  false),
            new Boss("Crossbreed Priscilla",            5,  1,  2730, ArenaSize.Medium, false),
            new Boss("Sanctuary Guardian",              6,  4,  3471, ArenaSize.Large,  false),
            new Boss("Artorias",                        7,  4,  4100, ArenaSize.Small, false),
            new Boss("Manus",                           8,  5,  4500, ArenaSize.Large,  false),
            new Boss("Black Dragon Kalameet",           9,  5,  4510, ArenaSize.Giant,  false),
            new Boss("Centipede Demon",                 10, 5,  5200, ArenaSize.Large,  false),
            new Boss("Sif",                             11, 5,  5210, ArenaSize.Giant,  true),  // NOTE: Sif will always be harder!
            new Boss("Gravelord Nito",                  12, 1,  5220, ArenaSize.Medium, false),
            new Boss("Gaping Dragon",                   13, 2,  5260, ArenaSize.Giant,  false),
            new Boss("Ornstein",                        14, 4,  5270, ArenaSize.Medium, false),
            new Boss("Giant Ornstein",                  14, 4,  5270, ArenaSize.Medium, false),
            new Boss("Quelaag",                         15, 3,  5280, ArenaSize.Large,  false),
            new Boss("Seath the Scaleless",             16, 2,  5290, ArenaSize.Large,  false),
            new Boss("Bell Gargoyle",                   17, 2,  5350, ArenaSize.Large,  false),
            new Boss("Lightning Gargoyle",              18, 2,  5350, ArenaSize.Large,  false),
            new Boss("Gwyn",                            19, 5,  5370, ArenaSize.Small,  false),
            new Boss("Four Kings",                      20, 3,  5390, ArenaSize.Medium, false),
        };

        public EnemyGenerator(SoulsMod mod, Random random, WeaponGenerator weapons, ArmorGenerator armor)
        {
            Mod = mod;
            Rand = random;
            WeaponGen = weapons;
            ArmorGen = armor;
            NameGenerator = new BossNameGenerator(Rand);
        }

        public void Install()
        {
            // Mostly deterministic. 
            // - NPC params that currently differ by only 1 are made to differ by 10 instead (to allow use of the last digit for levels).
            // - Creates ten different levels of each enemy's NPC entry and points them to the best AI, so MSB doesn't need to specify AI.
            // Also randomizes boss names.

            ModifyMiscellaneousParams();
            AdjustNewGamePlusBuffs();

            foreach (Enemy enemy in EnemyList)
                CreateEnemy(enemy);
        }

        void CreateEnemy(Enemy enemy)
        {
            // Clear range of NPC entries, then copy from vanilla to new IDs with some tweaks.
            Mod.GPARAM.NPCs.DeleteRowRange(enemy.NPCParamID, enemy.NPCParamID + 10);  // normal
            Mod.GPARAM.NPCs.DeleteRowRange(enemy.RedPhantomNPCParamID, enemy.RedPhantomNPCParamID + 10);  // red phantom
            NPC enemyNPC = Mod.GPARAM.NPCs.CopyRow(Mod.VanillaGPARAM.NPCs[enemy.OldNPCParamID], enemy.NPCParamID);
            if (enemy.OldNPCParamID != -1)  // Change name (non-Mob only).
                enemyNPC.Name = enemy.Name;
            enemyNPC.Row.Name = $"{enemy.Name} (1)";

            // Bosses (normal and Abyssal) award their item lots directly via
            // common EMEVD, rather than dropping them.
            enemyNPC.ItemLotID1 = enemy.Rarity == EnemyRarity.Boss ? -1 : enemy.ItemLotParamID;
            enemyNPC.ItemLotID2 = -1;
            enemyNPC.ItemLotID3 = -1;
            enemyNPC.ItemLotID4 = -1;
            enemyNPC.ItemLotID5 = -1;
            enemyNPC.ItemLotID6 = -1;

            enemyNPC.IsWeakToDivine = enemy.HasLabel(Label.Skeleton);
            enemyNPC.IsWeakToOccult = enemy.HasLabel(Label.Dragon);
            enemyNPC.IsDemon = enemy.HasLabel(Label.Demon);
            enemyNPC.IsAbyssal = enemy.HasLabel(Label.Abyssal);

            enemyNPC.SoulReward = enemy.SoulReward;  // will be multiplied by level scale SpEffect

            Mod.GPARAM.AI[enemy.AIParamID].Name = enemy.Name;  // Set AI param name.

            CreateLevelVariants(enemy.NPCParamID);  // Create 10 level variants.
            CreateRedPhantomVariants(enemy.NPCParamID, enemy.Rarity == EnemyRarity.Boss);  // Create Red Phantom variants (+50).

            RandomizeItemLots(enemy);

            if (enemy.Rarity == EnemyRarity.Boss)
            {
                // Randomize boss name (except Sif).
                Boss boss = GetBoss(enemy.Name);
                if (enemy.Name == "Sif")
                    Mod.Text.NPCNames[boss.NameTextID] = "Dark Lobos";
                else
                    Mod.Text.NPCNames[boss.NameTextID] = NameGenerator.GetRandomName(false);
            }
        }

        void ModifyMiscellaneousParams()
        {
            // Creates extra "mob"-style AI params for bosses.

            CreateMobAIVariant(223000, 223010);
            CreateMobAIVariant(223100, 223110);
            CreateMobAIVariant(223200, 223210);
            CreateMobAIVariant(224000, 224010);  // ignoring existing variant of Capra
            CreateMobAIVariant(225000, 225010);  // ignoring existing variant of Taurus
            CreateMobAIVariant(232000, 232010);
            CreateMobAIVariant(236000, 236010);
            CreateMobAIVariant(236001, 236011);
            CreateMobAIVariant(273000, 273010);
            CreateMobAIVariant(347100, 347110);
            CreateMobAIVariant(410000, 410010);
            CreateMobAIVariant(450000, 450010);
            CreateMobAIVariant(451000, 451010);
            CreateMobAIVariant(520000, 520010);  // Centipede cut tail/arm still have no retreat distance
            CreateMobAIVariant(521000, 521010);
            CreateMobAIVariant(522000, 522010);
            CreateMobAIVariant(526000, 526010);
            CreateMobAIVariant(527000, 527010);
            CreateMobAIVariant(527100, 527110);
            CreateMobAIVariant(528000, 528010);
            CreateMobAIVariant(529000, 529010);
            CreateMobAIVariant(535000, 535010);
            CreateMobAIVariant(535100, 535110);
            CreateMobAIVariant(537000, 537010);
            CreateMobAIVariant(539000, 539010);

            // Set bomb-throwing Giant in Sen's Fortress to "Boss" team, which will let his bombs hurt other enemies (for fun).
            Mod.GPARAM.NPCs[286000].TeamType = 1;  // Boss
            // Also reduce his level to 4.
            Mod.GPARAM.NPCs[286000].SpecialEffectID4 = 7004;
            Mod.GPARAM.NPCs[286000].NewGamePlusSpecialEffect = 7404;

            // TODO: Consider de-levelling Undead Dragon in Valley of Drakes (and eventually Painted World).

            // De-level Bed of Chaos from 7014 to 7007.
            Mod.GPARAM.NPCs[523000].SpecialEffectID4 = 7007;
            Mod.GPARAM.NPCs[523000].NewGamePlusSpecialEffect = 7407;
            Mod.GPARAM.NPCs[540000].SpecialEffectID4 = 7007;
            Mod.GPARAM.NPCs[540000].NewGamePlusSpecialEffect = 7407;
        }

        void AdjustNewGamePlusBuffs()
        {
            // Currently, all NG+ buffs are identical (blanket mild increase).
            for (int i = 1; i <= 15; i++)
            {
                SpEffect buff = Mod.GPARAM.SpEffects[7400 + i];
                buff.MaxHPMultiplier = 1.2f;
                buff.MaxMPMultiplier = 1.2f;
                buff.MaxStaminaMultiplier = 1.2f;
                buff.PhysicalAttackPowerMultiplier = 1.2f;
                buff.MagicAttackPowerMultiplier = 1.2f;
                buff.FireAttackPowerMultiplier = 1.2f;
                buff.LightningAttackPowerMultiplier = 1.2f;
                buff.PhysicalDefenseMultiplier = 1.2f;
                buff.MagicDefenseMultiplier = 1.2f;
                buff.FireDefenseMultiplier = 1.2f;
                buff.LightningDefenseMultiplier = 1.2f;
                buff.OutgoingStaminaDamageMultiplier = 1.2f;
                buff.SoulRewardMultiplier = 1.2f;
            }
        }

        void CreateMobAIVariant(int sourceRowID, int newRowID)
        {
            // Creates a new variant of the given AI param row with standard mob retreat and smell distances.
            // (The boss versions typically have 9999 retreat distance and 100 smell.)
            
            Mod.GPARAM.AI.DeleteRow(newRowID);
            NPCThought sourceAI = Mod.GPARAM.AI[sourceRowID];
            NPCThought newAI = Mod.GPARAM.AI.CopyRow(sourceAI, newRowID);  // copying live GPARAM
            newAI.BattleRetreatDistance = 50;
            newAI.MaxRetreatDistance = 75;
            newAI.RetreatBattleStartDistance = 6;
            newAI.SmellDistance = 0;
        }

        void CreateLevelVariants(int baseNPCParamID)
        {
            // Level variants all have the same drop table.
            NPC baseParam = Mod.GPARAM.NPCs[baseNPCParamID];
            baseParam.SpecialEffectID4 = 7001;
            baseParam.NewGamePlusSpecialEffect = 7401;
            for (int level = 1; level < 10; level++)
            {
                NPC levelParam = Mod.GPARAM.NPCs.CopyRow(baseParam, baseNPCParamID + level);
                levelParam.Name = baseParam.Name + $" ({level + 1})";
                levelParam.SpecialEffectID4 = 7000 + level + 1;
                levelParam.NewGamePlusSpecialEffect = 7400 + level + 1;
            }
        }

        void CreateRedPhantomVariants(int baseNPCParamID, bool isBoss)
        {
            // Red phantom variants are (obviously) red phantoms, and are also two levels higher
            // and have a different (better) drop table. Abyssal boss red phantoms are three
            // levels higher instead.
            int redPhantomItemLotID = 100 * (baseNPCParamID + 50);
            for (int offset = 0; offset < 10; offset++)
            {
                NPC baseParam = Mod.GPARAM.NPCs[baseNPCParamID + offset];
                baseParam.DrawType = 0;
                NPC redPhantomParam = Mod.GPARAM.NPCs.CopyRow(baseParam, baseNPCParamID + offset + 50);
                redPhantomParam.Name = baseParam.Name + $" (RED)";
                redPhantomParam.DrawType = 2;
                redPhantomParam.SpecialEffectID4 += isBoss ? 3 : 2;
                if (redPhantomParam.SpecialEffectID4 > 7015)
                    redPhantomParam.SpecialEffectID4 = 7015;
                redPhantomParam.NewGamePlusSpecialEffect += isBoss ? 3 : 2;
                if (redPhantomParam.NewGamePlusSpecialEffect > 7415)
                    redPhantomParam.NewGamePlusSpecialEffect = 7415;

                // Abyssal Red Phantom bosses give rewards directly in common EMEVD.
                redPhantomParam.ItemLotID1 = isBoss ? -1 : redPhantomItemLotID;
                redPhantomParam.ItemLotID2 = -1;
                redPhantomParam.ItemLotID3 = -1;
                redPhantomParam.ItemLotID4 = -1;
                redPhantomParam.ItemLotID5 = -1;
                redPhantomParam.ItemLotID6 = -1;
            }
        }

        void RandomizeItemLots(Enemy enemy)
        {
            int itemLotID = 100 * enemy.NPCParamID;
            int redPhantomItemLotID = 100 * (enemy.NPCParamID + 50);
            ItemLot bonusLot;

            switch (enemy.Rarity)
            {
                case EnemyRarity.Common:
                    CreateRandomItemLot(
                        enemy,
                        itemLotID,
                        (TreasureType.None, 88),
                        (TreasureType.CommonItem, 3),
                        (TreasureType.CommonItem, 3),
                        (TreasureType.CommonItem, 3),
                        (TreasureType.UncommonItem, 3)
                        );
                    CreateRandomItemLot(  // Identical to normal Uncommon enemy.
                        enemy,
                        redPhantomItemLotID,
                        (TreasureType.None, 75),
                        (TreasureType.CommonItem, 4),
                        (TreasureType.CommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.RareItem, 5)
                        );
                    break;
                case EnemyRarity.Uncommon:
                    CreateRandomItemLot(
                        enemy,
                        itemLotID,
                        (TreasureType.None, 75),
                        (TreasureType.CommonItem, 4),
                        (TreasureType.CommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.UncommonItem, 4),
                        (TreasureType.RareItem, 5)
                        );
                    CreateRandomItemLot(  // Not quite as good as Rare enemy, but at least guaranteed.
                        enemy,
                        redPhantomItemLotID,
                        (TreasureType.RareItem, 13),
                        (TreasureType.RareItem, 12),
                        (TreasureType.RareItem, 13),
                        (TreasureType.RareItem, 12),
                        (TreasureType.BasicWeapon, 13),
                        (TreasureType.BasicWeapon, 12),
                        (TreasureType.BasicArmor, 13),
                        (TreasureType.BasicArmor, 12)
                        );
                    break;
                case EnemyRarity.Rare:
                    CreateRandomItemLot(
                        enemy,
                        itemLotID,
                        (TreasureType.RareItem, 13),
                        (TreasureType.RareItem, 12),
                        (TreasureType.RareItem, 12),
                        (TreasureType.BasicWeapon, 13),
                        (TreasureType.BasicArmor, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.Ember, 13)
                        );
                    CreateRandomItemLot(  // Not quite as good as normal Very Rare enemy.
                        enemy,
                        redPhantomItemLotID,
                        (TreasureType.RareItem, 13),
                        (TreasureType.RareItem, 13),
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.Ember, 12),
                        (TreasureType.Ember, 12)
                        );
                    CreateRandomItemLot(
                        enemy,
                        redPhantomItemLotID + 1,
                        (TreasureType.None, 80),
                        (TreasureType.VeryRareItem, 10),
                        (TreasureType.VeryRareItem, 10),
                        (TreasureType.VeryRareItem, 10)
                        );
                    break;
                case EnemyRarity.VeryRare:
                    CreateRandomItemLot(
                        enemy,
                        itemLotID,
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.Ember, 12),
                        (TreasureType.Ember, 12)
                        );
                    CreateRandomItemLot(
                        enemy,
                        itemLotID + 1,
                        (TreasureType.None, 80),
                        (TreasureType.VeryRareItem, 10),
                        (TreasureType.VeryRareItem, 10),
                        (TreasureType.VeryRareItem, 10)
                        );
                    CreateRandomItemLot(
                        enemy,
                        redPhantomItemLotID,
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.Ember, 12),
                        (TreasureType.Ember, 12)
                        );
                    CreateRandomItemLot(  // Very Rare Red Phantoms always drop two items.
                        enemy,
                        redPhantomItemLotID + 1,
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.VeryRareItem, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.LegendaryArmor, 12)
                        );
                    break;
                case EnemyRarity.Boss:
                    // Awarded directly, not dropped by Boss.
                    CreateRandomItemLot(
                        enemy,
                        itemLotID,
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 13),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryWeapon, 12),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 13),
                        (TreasureType.LegendaryArmor, 12),
                        (TreasureType.LegendaryArmor, 12)
                        );
                    CreateRandomItemLot(  // Each boss can award one of two possible Embers.
                        enemy,
                        itemLotID + 1,
                        (TreasureType.None, 60),
                        (TreasureType.Ember, 20),
                        (TreasureType.Ember, 20)
                        );
                    if (enemy.HasLabel(Label.Sapient))
                    {
                        bonusLot = GetCleanItemLot(itemLotID + 1);
                        bonusLot.SetSimpleItem(  // Guaranteed Humanity reward
                            ItemLotCategory.Good,
                            Roll(0.2) ? 501 : 500,  // 20% chance of Twin Humanities
                            count: 1);
                        bonusLot.Name = $"{enemy.Name}";
                    }
                    CreateRandomItemLot(  // Abyssal challenge bosses.
                        enemy,
                        redPhantomItemLotID,
                        (TreasureType.AbyssalWeapon, 13),
                        (TreasureType.AbyssalWeapon, 13),
                        (TreasureType.AbyssalWeapon, 12),
                        (TreasureType.AbyssalWeapon, 12),
                        (TreasureType.AbyssalArmor, 13),
                        (TreasureType.AbyssalArmor, 13),
                        (TreasureType.AbyssalArmor, 12),
                        (TreasureType.AbyssalArmor, 12)
                        );
                    bonusLot = GetCleanItemLot(redPhantomItemLotID + 1);
                    bonusLot.SetSimpleItem(  // Guaranteed Humanity reward
                        ItemLotCategory.Good,
                        Roll(0.4) ? 501 : 500,  // 40% chance of Twin Humanities
                        count: 1);
                    bonusLot.Name = $"{enemy.Name} RP";
                    CreateRandomItemLot(  // Very rarely, abyssal boss will drop a second equipment.
                        enemy,
                        redPhantomItemLotID + 2,
                        (TreasureType.None, 94),
                        (TreasureType.AbyssalWeapon, 1),
                        (TreasureType.AbyssalWeapon, 1),
                        (TreasureType.AbyssalWeapon, 1),
                        (TreasureType.AbyssalArmor, 1),
                        (TreasureType.AbyssalArmor, 1),
                        (TreasureType.AbyssalArmor, 1)
                        );
                    break;
            }
        }

        void CreateRandomItemLot(Enemy enemy, int itemLotID, params (TreasureType rewardType, uint chance)[] itemLots)
        {
            List<ItemLotCategory> categories = new List<ItemLotCategory>();
            List<int> itemIDs = new List<int>();
            List<uint> counts = new List<uint>();
            List<uint> chancePoints = new List<uint>();
            List<(ItemLotCategory, int)> usedItems = new List<(ItemLotCategory, int)>();
            foreach (var (treasureType, chance) in itemLots)
            {
                ItemLotCategory category;
                int itemID;
                int count;
                if (treasureType == TreasureType.None)  // Empty slot.
                {
                    category = ItemLotCategory.None;
                    itemID = 0;
                    count = 0;
                }
                else if (treasureType.In(TreasureType.BasicWeapon, TreasureType.LegendaryWeapon, TreasureType.AbyssalWeapon))
                {
                    category = ItemLotCategory.Weapon;
                    do
                    {
                        itemID = GetRandomWeaponID(treasureType);
                    } while (usedItems.Contains((category, itemID)));
                    count = 1;
                }
                else if (treasureType.In(TreasureType.BasicArmor, TreasureType.LegendaryArmor, TreasureType.AbyssalArmor))
                {
                    {
                        category = ItemLotCategory.Armor;
                        do
                        {
                            itemID = GetRandomArmorID(treasureType);
                        } while (usedItems.Contains((category, itemID)));
                    }
                    count = 1;
                }
                else if (treasureType == TreasureType.Ember)
                {
                    category = ItemLotCategory.Good;
                    itemID = 1000 + 10 * Rand.Next(9);  // Random ember from 1000 to 1080.
                    count = 1;
                }
                else  // Common / Uncommon / Rare / VeryRare. Get a match to any label.
                {
                    if (treasureType == TreasureType.RareItem && Roll(0.1))
                    {
                        // 10% chance of a Mote for rare lots, regardless of labels.
                        category = ItemLotCategory.Good;
                        itemID = Rand.Next(650, 659);
                        count = 1;
                    }
                    else if (treasureType == TreasureType.VeryRareItem && Roll(0.1))
                    {
                        // 10% chance of a Tome for very rare lots, regardless of labels.
                        category = ItemLotCategory.Good;
                        itemID = Rand.Next(660, 669);
                        count = 1;
                    }
                    else
                    {
                        // 
                        Treasure chosen = Treasures.GetRandomReward(treasureType, enemy.Labels, usedItems, Rand);
                        if (chosen != null)
                        {
                            category = chosen.Category;
                            itemID = chosen.ItemID;
                            count = Rand.Next(0, chosen.MaxCount);
                        }
                        else  // Leave slot empty.
                        {
                            category = ItemLotCategory.None;
                            itemID = 0;
                            count = 0;
                        }
                    }
                }

                categories.Add(category);
                itemIDs.Add(itemID);
                counts.Add((uint)count);
                chancePoints.Add(chance);
                usedItems.Add((category, itemID));
            }
            ItemLot itemLot = GetCleanItemLot(itemLotID);
            itemLot.SetItemSlots(categories.ToArray(), itemIDs.ToArray(), counts.ToArray(), chancePoints.ToArray(), true);
            itemLot.Name = $"{enemy.Name} Drop";
        }

        int GetRandomWeaponID(TreasureType weaponType)
        {
            List<(Upgrade upgrade, double odds)> upgradeOptions = new List<(Upgrade, double)>();
            return WeaponGen.GetRandomWeaponID(weaponType == TreasureType.BasicWeapon, weaponType == TreasureType.LegendaryWeapon,
                weaponType == TreasureType.AbyssalWeapon, upgradeOptions.ToArray());
        }

        int GetRandomArmorID(TreasureType armorType)
        {
            // Fixed odds of getting pre-upgraded armor.
            (int upgrade, double odds)[] upgradeOptions = { (1, 0.1), (2, 0.05), (3, 0.03), (4, 0.01) };
            return ArmorGen.GetRandomArmorID(armorType == TreasureType.BasicArmor, basic: armorType == TreasureType.BasicArmor,
                armorType == TreasureType.LegendaryArmor, armorType == TreasureType.AbyssalArmor, upgradeOptions);
        }

        bool Roll(double odds)
        {
            return Rand.NextDouble() < odds;
        }

        ItemLot GetCleanItemLot(int itemLotID, int itemLotFlag = -1)
        {
            // Return to template (but with no flag).
            Mod.GPARAM.ItemLots.DeleteRowRange(itemLotID, itemLotID + 10);
            ItemLot cleaned = Mod.GPARAM.ItemLots.CopyRow(ItemLotTemplate, itemLotID);
            cleaned.GetItemFlagId = itemLotFlag;
            return cleaned;
        }


        public static Enemy GetEnemy(string name)
        {
            return EnemyList.Where(enemy => enemy.Name == name).First();
        }

        public static Enemy GetRandomEnemyWithAllLabels(Label[] labels, Random random, Func<EnemyRarity, int> rarityWeightMap = null)
        {
            // Returns a random enemy with all the given labels. 
            // Weights chances by rarity enum value, but the mapping from rarities to weights can also be specified manually.
            IEnumerable<Enemy> options = EnemyList.Where(enemy => enemy.Rarity != EnemyRarity.Boss && (!labels.Any() || labels.Except(enemy.Labels).Any()));
            int total = options.Sum(enemy => rarityWeightMap == null ? (byte)enemy.Rarity : rarityWeightMap(enemy.Rarity));
            if (total == 0)
                throw new Exception($"Total probability for all enemies with all labels in ({string.Join(" ", labels)}) is zero. Cannot select one.");
            int roll = random.Next(total);
            int accumulatedPoints = 0;
            foreach (Enemy enemy in options)
            {
                accumulatedPoints += rarityWeightMap == null ? (byte)enemy.Rarity : rarityWeightMap(enemy.Rarity);
                if (roll < accumulatedPoints)
                    return enemy;
            }
            throw new Exception($"Could not select random enemy (roll = {roll}, weight total = {total}).");
        }

        public static Enemy GetRandomEnemyWithAnyLabels(Label[] labels, Random random, Func<EnemyRarity, int> rarityWeightMap = null)
        {
            // Returns a random enemy with any of the given labels. 
            // Weights chances by rarity enum value, but the mapping from rarities to weights can also be specified manually.
            IEnumerable<Enemy> options = EnemyList.Where(enemy => enemy.Rarity != EnemyRarity.Boss && labels.Intersect(enemy.Labels).Any());
            int total = options.Sum(enemy => rarityWeightMap == null ? (byte)enemy.Rarity : rarityWeightMap(enemy.Rarity));
            if (total == 0)
                throw new Exception($"Total probability for all enemies with any labels in ({string.Join(" ", labels)}) is zero. Cannot select one.");
            int roll = random.Next(total);
            int accumulatedPoints = 0;
            foreach (Enemy enemy in options)
            {
                accumulatedPoints += rarityWeightMap == null ? (byte)enemy.Rarity : rarityWeightMap(enemy.Rarity);
                if (roll < accumulatedPoints)
                    return enemy;
            }
            throw new Exception($"Could not select random enemy (roll = {roll}, weight total = {total}).");
        }

        public static Enemy GetRandomEnemyWithLabel(Label label, Random random, Func<EnemyRarity, int> rarityWeightMap = null)
        {
            // Shortcut for specifying a single label.
            return GetRandomEnemyWithAllLabels(new Label[] { label }, random, rarityWeightMap);
        }

        public static Enemy GetRandomEnemy(Random random, Func<EnemyRarity, int> rarityWeightMap = null)
        {
            // Shortcut for getting any enemy, regardless of labels.
            return GetRandomEnemyWithAllLabels(new Label[] { }, random, rarityWeightMap);
        }

        public static Enemy GetRandomEnemyWithRarity(Random random, EnemyRarity rarity, List<Label> labels)
        {
            // Get a random enemy of the given rarity, weighted by the number of labels it shares with those given.
            Dictionary<Enemy, int> weightDict = new Dictionary<Enemy, int>();
            foreach (Enemy enemy in EnemyList)
            {
                IEnumerable<Label> sharedLabels = enemy.Labels.Intersect(labels);
                if (enemy.Rarity == rarity && sharedLabels.Any())
                    weightDict[enemy] = sharedLabels.Count();
            }
            if (!weightDict.Any())
            {
                // Ignore labels, if necessary (except exclude Vagrants).
                return new List<Enemy>(EnemyList.Where(e => e.Rarity == rarity && !e.Labels.Contains(Label.Vagrant))).GetRandomElement(random);
                // string labelString = string.Join(", ", labels);
                // throw new ArgumentException($"Could not find any enemies with rarity {rarity} and labels: [{labelString}].");
            }
            return weightDict.GetWeightedRandomElement(random);
        }

        public static int LastBossCategory
        {
            get => BossList.Max(boss => boss.Category);
        }

        public static Boss GetBoss(string bossName)
        {
            IEnumerable<Boss> matches = BossList.Where(boss => boss.Name == bossName);
            if (!matches.Any())
                throw new ArgumentException($"Invalid boss name: {bossName}");
            return matches.First();
        }

        public static Boss GetRandomBoss(Random random, ArenaSize maxSize, List<int> excludeCategories)
        {
            // Get a boss with required arena size up to the given maximum. Bosses closer to the max size are weighted more.
            // Currently not doing any weighting by label for bosses. Arena size and non-reusability is restrictive enough.
            List<Boss> options = new List<Boss>(BossList.Where(boss => boss.RequiredArenaSize <= maxSize && !excludeCategories.Contains(boss.Category)));
            if (options.Count == 0)
            {
                // It's possible that, e.g., all "Small" bosses have already been used. Try to re-use an existing one in this case (no other choice).
                options = new List<Boss>(BossList.Where(boss => boss.RequiredArenaSize <= maxSize));
                if (options.Count == 0)
                    // Must be a bad label.
                    throw new Exception("Could not find a boss with a non-excluded category and given required size. This shouldn't happen!");
            }
            Dictionary<Boss, int> weightedOptions = options.ToDictionary(boss => boss, boss => 6 - ((int)maxSize - (int)boss.RequiredArenaSize));
            return weightedOptions.GetWeightedRandomElement(random);
        }
    }
}
