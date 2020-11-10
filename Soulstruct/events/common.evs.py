"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *


def Constructor():
    """ 0: Event 0 """
    EndIfClient()

    # AwardItemLot(50010)
    # AwardItemLot(50020)
    # AwardItemLot(50030)
    # AwardItemLot(50070)
    # AwardItemLot(50100)

    # Miscellaneous stuff (leave).
    DisableFlag(760)
    DisableFlag(762)
    DisableFlag(765)

    RunEvent(761)  # Flag disables itself after 200 frames.
    RunEvent(763)  # Flags 762 and 764 force player sitting animation at some point.
    RunEvent(290)  # Enables 280-289, then disables flag 288 if the player started as Knight/Cleric and 287 otherwise.
    DisableVagrantSpawning()  # replaces event 701
    RunEvent(702)  # Flag 702 is enabled if you're in the Kiln and the Lordvessel hasn't been filled (11800210).
    # Event 717 always enabled warping in the Abyss.
    # Event 718 displayed the "Taken by the abyss" status.
    RunEvent(706)  # Disables warping in Archives prison and Painted World.
    RunEvent(740)  # Enabled if player is Pyromancer class.
    RunEvent(750)  # Enables flag 751 upon curse.
    RunEvent(752)  # Activates Eingyi dialogue if you have an egg infection.
    RunEvent(757)  # Shows "seek Ingward" message upon curse.
    RunEvent(758)  # Shows "Ring of Sacrifice shattered" message.
    RunEvent(759)  # Shows "Rare Ring of Sacrifice shattered" message.
    RunEvent(754)  # Creates some temporary FX when flag 754 is enabled.
    # Event 770 clears all player "sin", I believe, by resetting hostile character flags.
    # Event 772 is also something to do with sin, and enables flag 744 (probably triggers option in Oswald's menu).
    RunEvent(730)  # Not sure. Causes flag 8000 to enable flag 735, once.
    RunEvent(731)  # Related to above.
    RunEvent(766)  # Enables flag 765 if you're offline.
    # Event 710 enabled bonfire warping upon Lordvessel receipt.

    # Monitor Lord Soul possession (leave).
    RunEvent(711, slot=0, args=(2500, 711))
    RunEvent(711, slot=1, args=(2501, 712))
    RunEvent(711, slot=2, args=(2502, 713))
    RunEvent(711, slot=3, args=(2504, 714))
    RunEvent(715)  # Gwyn's Soul
    RunEvent(716)  # Sunlight Spear

    # Estus upgrade level.
    RunEvent(8131, slot=0, args=(202, 203))
    RunEvent(8131, slot=1, args=(204, 205))
    RunEvent(8131, slot=2, args=(206, 207))
    RunEvent(8131, slot=3, args=(208, 209))
    RunEvent(8131, slot=4, args=(210, 211))
    RunEvent(8131, slot=5, args=(212, 213))
    RunEvent(8131, slot=6, args=(214, 215))

    # Repair box sync.
    RunEvent(819)

    # Event 970 slots (boss rewards) removed.

    # Event 250 slots enabled other bonfire menu flags upon item receipt (e.g. Weapon Smithbox).

    # Event 350 slots marked Ember possession for blacksmith dialogue/giving.

    # Event 780 slots toggled flags based on possession of each Titanite type.

    # Leaving covenant events commented out for future potential stuff.
    # Event 870 slots toggled flags based on covenant membership.
    # Event 840 slots controlled covenant-joining events.

    # RunEvent(870, slot=0, args=(0, 850), arg_types='Bi')
    # RunEvent(870, slot=1, args=(1, 851), arg_types='Bi')
    # RunEvent(870, slot=2, args=(2, 852), arg_types='Bi')
    # RunEvent(870, slot=3, args=(3, 853), arg_types='Bi')
    # RunEvent(870, slot=4, args=(4, 854), arg_types='Bi')
    # RunEvent(870, slot=5, args=(5, 855), arg_types='Bi')
    # RunEvent(870, slot=6, args=(6, 856), arg_types='Bi')
    # RunEvent(870, slot=7, args=(7, 857), arg_types='Bi')
    # RunEvent(870, slot=8, args=(8, 858), arg_types='Bi')
    # RunEvent(870, slot=9, args=(9, 859), arg_types='Bi')
    # RunEvent(840, slot=0, args=(840, 7905, 6370, 4294967295))
    # RunEvent(840, slot=1, args=(841, 7905, 6072, 4294967295))
    # RunEvent(840, slot=2, args=(842, 7905, 6080, 4294967295))
    # RunEvent(840, slot=3, args=(843, 7905, 6001, 4294967295))
    # RunEvent(840, slot=4, args=(844, 7898, 10000, 7896))
    # RunEvent(840, slot=5, args=(845, 7905, 6340, 4294967295))
    # RunEvent(840, slot=6, args=(846, 7905, 6341, 4294967295))
    # RunEvent(840, slot=7, args=(847, 7913, 10000, 7911))
    # RunEvent(840, slot=8, args=(848, 7905, 6380, 4294967295))
    # RunEvent(840, slot=9, args=(849, 7905, 1400700, 4294967295))
    # RunEvent(840, slot=10, args=(860, 7905, 16969, 4294967295))

    # Monitor NG+ level.
    RunEvent(690, slot=0, args=(600, 4, 16, 1175), arg_types='iIIi')

    CleanupRun()
    KillPlayerOnBossQuit()
    CreateBonfire()
    KilnAvailable()

    # Award ally gifts (once per run).
    AwardSiegmeyerGift()
    AwardQuelanaGift()

    for i in range(10):
        StatBoostFlagToggle(0 + i, 8900 + i, CommonFlags.BoostVitalityBase + i)
        StatBoostFlagToggle(10 + i, 8910 + i, CommonFlags.BoostAttunementBase + i)
        StatBoostFlagToggle(20 + i, 8920 + i, CommonFlags.BoostEnduranceBase + i)
        StatBoostFlagToggle(30 + i, 8930 + i, CommonFlags.BoostStrengthBase + i)
        StatBoostFlagToggle(40 + i, 8940 + i, CommonFlags.BoostDexterityBase + i)
        StatBoostFlagToggle(50 + i, 8950 + i, CommonFlags.BoostResistanceBase + i)
        StatBoostFlagToggle(60 + i, 8960 + i, CommonFlags.BoostIntelligenceBase + i)
        StatBoostFlagToggle(70 + i, 8970 + i, CommonFlags.BoostFaithBase + i)

    DireDamageModifier()
    ShieldHitTrigger()
    RollingTrigger()
    InvisibleEffect()
    EnchantedSpellRechargeRequest()
    GoToNewGamePlus()
    QuitRun()
    MarkRunStart()
    LoseLife()
    RunPermadeath()

    for i in range(10):
        LevelIndicatorRequest(i, CommonFlags.RequestLevelBannerBase + i, CommonTexts.LevelMessageBase + i)
    for i in range(10):
        LevelIndicatorRequest(i, CommonFlags.RequestCursedLevelBannerBase + i, CommonTexts.CursedLevelMessageBase + i)
    LevelIndicatorRequest(10, CommonFlags.RequestBonusLevelBanner, CommonTexts.BonusLevel)

    WarpRequest(0,  CommonFlags.RequestWarpToFirelink, 10, 2, -1, 1102960)  # When run ends.

    WarpRequest(1,  11002005, 10, 0, 1000240, 1000230)
    # No start point at Depths arena drop.
    WarpRequest(2,  11002025, 10, 0, 1000242, 1000232)

    WarpRequest(3,  11012005, 10, 1, 1010240, 1010230)
    WarpRequest(4,  11012015, 10, 1, 1010241, 1010231)
    WarpRequest(5,  11012025, 10, 1, 1010242, 1010232)
    WarpRequest(6,  11012035, 10, 1, 1010243, 1010233)
    WarpRequest(7,  11012045, 10, 1, 1010244, 1010234)
    WarpRequest(8,  11012055, 10, 1, 1010245, 1010235)

    WarpRequest(9,  11012305, 10, 1, 1010540, 1010530)
    WarpRequest(10, 11012315, 10, 1, 1010541, 1010531)
    WarpRequest(11, 11012325, 10, 1, 1010542, 1010532)
    WarpRequest(12, 11012335, 10, 1, 1010543, 1010533)
    WarpRequest(13, 11012345, 10, 1, 1010544, 1010534)

    WarpRequest(14, 11102005, 11, 0, 1100240, 0)  # Respawn point not set in Painted World.
    # No start point at Painted World arena drop.

    WarpRequest(15, 11202005, 12, 0, 1200240, 1200230)
    WarpRequest(16, 11202015, 12, 0, 1200241, 1200231)
    WarpRequest(17, 11202025, 12, 0, 1200242, 1200232)
    WarpRequest(18, 11202035, 12, 0, 1200243, 1200233)

    WarpRequest(19, 11212005, 12, 1, 1210240, 1210230)
    WarpRequest(20, 11212015, 12, 1, 1210241, 1210231)
    WarpRequest(21, 11212025, 12, 1, 1210242, 1210232)

    WarpRequest(22, 11212305, 12, 1, 1210540, 1210530)
    WarpRequest(23, 11212315, 12, 1, 1210541, 1210531)

    WarpRequest(24, 11212605, 12, 1, 1210840, 1210830)
    # No start point at Chasm arena.

    WarpRequest(25, 11302005, 13, 0, 1300240, 1300230)
    # No start point at Catacombs coffin.
    WarpRequest(26, 11302025, 13, 0, 1300242, 1300232)

    WarpRequest(27, 11312005, 13, 1, 1310240, 1310230)
    # No start point at Nito arena.

    WarpRequest(28, 11322005, 13, 2, 1320240, 1320230)
    WarpRequest(29, 11322015, 13, 2, 1320241, 1320231)
    WarpRequest(30, 11322305, 13, 2, 1320540, 1320530)
    WarpRequest(31, 11322315, 13, 2, 1320541, 1320531)
    # No start point at Nito arena.

    WarpRequest(32, 11402005, 14, 0, 1400240, 1400230)
    WarpRequest(33, 11402015, 14, 0, 1400241, 1400231)
    WarpRequest(34, 11402025, 14, 0, 1400242, 1400232)
    WarpRequest(35, 11402035, 14, 0, 1400243, 1400233)

    WarpRequest(36, 11412005, 14, 1, 1410240, 1410230)
    WarpRequest(37, 11412015, 14, 1, 1410241, 1410231)
    WarpRequest(38, 11412025, 14, 1, 1410242, 1410232)
    WarpRequest(39, 11412035, 14, 1, 1410243, 1410233)

    WarpRequest(40, 11412305, 14, 1, 1410540, 1410530)
    WarpRequest(41, 11412315, 14, 1, 1410541, 1410531)
    # No start point at Bed of Chaos arena.

    WarpRequest(42, 11502005, 15, 0, 1500240, 1500230)
    WarpRequest(43, 11502015, 15, 0, 1500241, 1500231)

    WarpRequest(44, 11512005, 15, 1, 1510240, 1510230)
    WarpRequest(45, 11512015, 15, 1, 1510241, 1510231)
    # No start point at Gwynevere's room.

    WarpRequest(46, 11602005, 16, 0, 1600240, 1600230)
    WarpRequest(47, 11602015, 16, 0, 1600241, 1600231)
    WarpRequest(48, 11602025, 16, 0, 1600242, 1600232)
    # No start point in Abyss (exluding portal warp handled in each map).

    WarpRequest(49, 11702005, 17, 0, 1700240, 1700230)
    # No start point in Seath arena.

    WarpRequest(50, 11802005, 18, 0, 1800240, 1800230)

    Wait(3.0)  # Wait for hook to catch up on load.
    HookCheck()


def Preconstructor():
    """ 50: Event 50 """
    EndIfFlagOn(909)
    EnableFlag(909)
    EnableFlag(814)  # Leaving this because I'm not sure what it does.


def Event290():
    """ 290: Event 290 """
    EndIfThisEventOn()
    EnableFlagRange((280, 290))
    IfPlayerClass(-1, ClassType.Knight)
    IfPlayerClass(-1, ClassType.Cleric)
    IfConditionTrue(1, input_condition=-1)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableFlag(287)
    End()
    DisableFlag(288)


def Event702():
    """ 702: Event 702 """
    DisableFlag(702)
    IfFlagOff(1, 11800210)
    IfInsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(702)
    IfOutsideMap(-1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfFlagOn(-1, 11800210)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(702)
    Restart()


def Event718():
    """ 718: Event 718 """
    EndIfFlagOff(8120)
    DisplayStatus(10010650, pad_enabled=True)
    DisableFlag(8120)


def Event706():
    """ 706: Event 706 """
    IfFlagOn(0, 710)
    EnableFlag(706)
    IfFlagOn(-1, 11705170)
    IfInsideMap(-1, game_map=PAINTED_WORLD)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(706)
    IfFlagOff(1, 11705170)
    IfOutsideMap(1, game_map=PAINTED_WORLD)
    IfConditionTrue(0, input_condition=1)
    Restart()


def Event711(_, arg_0_3: int, arg_4_7: int):
    """ 711: Event 711 """
    EndIfThisEventSlotOn()
    IfPlayerHasGood(0, arg_0_3, including_box=False)
    EnableFlag(arg_4_7)


def Event715():
    """ 715: Event 715 """
    DisableFlag(715)
    IfFlagOn(1, 11010595)
    IfPlayerHasGood(1, 702, including_box=False)
    IfPlayerDoesNotHaveGood(1, 5520, including_box=True)
    IfPlayerCovenant(1, Covenant.WarriorOfSunlight)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(715)
    IfPlayerDoesNotHaveGood(-1, 702, including_box=False)
    IfPlayerHasGood(-1, 5520, including_box=True)
    IfPlayerCovenant(2, Covenant.WarriorOfSunlight)
    IfConditionFalse(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event716():
    """ 716: Event 716 """
    EndIfThisEventOn()
    IfFlagOn(0, 50000082)
    EnableFlag(716)


def Event8131(_, arg_0_3: int, arg_4_7: int):
    """ 8131: Event 8131 """
    EndIfThisEventSlotOn()
    IfPlayerHasGood(-1, arg_0_3, including_box=False)
    IfPlayerHasGood(-1, arg_4_7, including_box=False)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=202)
    EnableFlag(8131)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=204)
    EnableFlagRange((8131, 8132))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=206)
    EnableFlagRange((8131, 8133))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=208)
    EnableFlagRange((8131, 8134))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=210)
    EnableFlagRange((8131, 8135))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=212)
    EnableFlagRange((8131, 8136))
    SkipLinesIfNotEqual(1, left=arg_0_3, right=214)
    EnableFlagRange((8131, 8137))


def Event819():
    """ 819: Event 819 """
    EndIfThisEventOn()
    IfFlagOn(-1, 11017040)
    IfFlagOn(-1, 11017170)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11017040)
    EnableFlag(11017170)


def Event720():
    """ 720: Event 720 """
    EndIfThisEventOn()
    IfPlayerHasGood(-1, 4020, including_box=False)
    IfPlayerHasGood(-1, 4030, including_box=False)
    IfPlayerHasGood(-1, 4040, including_box=False)
    IfPlayerHasGood(-1, 4060, including_box=False)
    IfPlayerHasGood(-1, 4110, including_box=False)
    IfPlayerHasGood(-1, 4500, including_box=False)
    IfPlayerHasGood(-1, 4510, including_box=False)
    IfPlayerHasGood(-1, 4520, including_box=False)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11020102)


def Event730():
    """ 730: Event 730 """
    IfFlagOff(1, 732)
    IfFlagOn(1, 8000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(732)
    EnableFlag(735)
    Restart()


def Event731():
    """ 731: Event 731 """
    IfFlagOff(0, 8000)
    DisableFlag(732)
    DisableFlag(735)
    IfFlagOn(0, 8000)
    Restart()


def Event350(_, arg_0_3: int, arg_4_7: int):
    """ 350: Event 350 """
    SkipLinesIfThisEventSlotOff(2)
    IfPlayerHasGood(1, arg_4_7, including_box=False)
    EndIfConditionFalse(1)
    IfFlagOn(0, arg_0_3)
    RemoveGoodFromPlayer(arg_4_7, quantity=1)


def Event780(_, arg_0_3: int, arg_4_7: int):
    """ 780: Event 780 """
    DisableFlag(arg_4_7)
    IfPlayerHasGood(0, arg_0_3, including_box=False)
    EnableFlag(arg_4_7)
    IfPlayerDoesNotHaveGood(0, arg_0_3, including_box=False)
    Restart()


def Event870(_, arg_0_0: uchar, arg_4_7: int):
    """ 870: Event 870 """
    IfPlayerCovenant(0, arg_0_0)
    EnableFlag(arg_4_7)
    IfPlayerCovenant(1, arg_0_0)
    IfConditionFalse(0, input_condition=1)
    DisableFlag(arg_4_7)
    Restart()


def Event260(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 260: Event 260 """
    EndIfFlagOn(arg_0_3)
    IfFlagOn(0, arg_0_3)
    SkipLinesIfFlagOn(2, 9121)
    Wait(arg_8_11)
    DisplayStatus(arg_4_7, pad_enabled=True)


def Event970(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 970: Event 970 """
    EndIfFlagOn(arg_0_3)
    IfFlagOn(0, arg_0_3)
    SkipLinesIfEqual(1, left=arg_4_7, right=0)
    AwardItemLot(arg_4_7, host_only=True)
    DisableNetworkSync()
    Wait(5.0)
    SkipLinesIfEqual(1, left=arg_8_11, right=0)
    AwardItemLot(arg_8_11, host_only=True)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    AwardItemLot(arg_12_15, host_only=True)


def Event911(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar):
    """ 911: Event 911 """
    EndIfFlagOn(arg_0_3)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    SetFlagState(arg_0_3, state=arg_8_8)
    EndIfFlagOn(arg_0_3)
    Restart()


def Event890(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar):
    """ 890: Event 890 """
    EndIfFlagOn(arg_0_3)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    SetFlagState(arg_0_3, state=arg_8_8)
    EndIfFlagOn(arg_0_3)
    Restart()


def Event960(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 960: Event 960 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, arg_0_3)
    IfCharacterDead(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(arg_8_11, host_only=True)


def Event8200(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 8200: Event 8200 """
    EndIfFlagOn(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_box=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)
    EnableFlag(arg_12_15)


def Event8300(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """ 8300: Event 8300 """
    EndIfFlagOn(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_box=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)


def Event8090(_, arg_0_0: uchar, arg_4_7: int, arg_8_11: int):
    """ 8090: Event 8090 """
    EndIfFlagOn(arg_8_11)
    IfNewGameCycleGreaterThanOrEqual(1, completion_count=1)
    EndIfConditionFalse(1)
    IfPlayerHasItem(2, arg_4_7, item_type=arg_0_0, including_box=True)
    EndIfConditionFalse(2)
    EnableFlag(arg_8_11)


def Event910(_, arg_0_3: int, arg_4_7: int):
    """ 910: Event 910 """
    SkipLinesIfFlagOn(2, arg_0_3)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=True)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event690(_, arg_0_3: int, arg_4_7: uint, arg_8_11: uint, arg_12_15: int):
    """ 690: Event 690 """
    SkipLinesIfThisEventSlotOn(1)
    IfFlagOn(0, arg_12_15)
    SkipLinesIfFlagOn(1, 2)
    IfFlagOn(-1, 2)
    SkipLinesIfFlagOn(1, 3)
    IfFlagOn(-1, 3)
    SkipLinesIfFlagOn(1, 4)
    IfFlagOn(-1, 4)
    SkipLinesIfFlagOn(1, 5)
    IfFlagOn(-1, 5)
    SkipLinesIfFlagOn(1, 6)
    IfFlagOn(-1, 6)
    SkipLinesIfFlagOn(1, 7)
    IfFlagOn(-1, 7)
    SkipLinesIfFlagOn(1, 8)
    IfFlagOn(-1, 8)
    SkipLinesIfFlagOn(1, 9)
    IfFlagOn(-1, 9)
    SkipLinesIfFlagOn(1, 10)
    IfFlagOn(-1, 10)
    SkipLinesIfFlagOn(1, 11)
    IfFlagOn(-1, 11)
    SkipLinesIfFlagOn(1, 12)
    IfFlagOn(-1, 12)
    SkipLinesIfFlagOn(1, 13)
    IfFlagOn(-1, 13)
    SkipLinesIfFlagOn(1, 14)
    IfFlagOn(-1, 14)
    SkipLinesIfFlagOn(1, 15)
    IfFlagOn(-1, 15)
    IfConditionTrue(0, input_condition=-1)
    IncrementEventValue(arg_0_3, bit_count=arg_4_7, max_value=arg_8_11)
    Restart()


def Event721():
    """ 721: Event 721 """
    EndIfFlagOn(728)
    IfFlagOn(1, 11707000)
    IfFlagOn(1, 11707010)
    IfFlagOn(1, 11707020)
    IfFlagOn(1, 11707030)
    IfFlagOn(1, 11707040)
    IfFlagOn(1, 11707050)
    IfFlagOn(1, 11707060)
    IfFlagOn(1, 11707070)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(721)
    IfFlagOn(2, 11707090)
    IfFlagOn(2, 11707100)
    IfFlagOn(2, 11707110)
    IfConditionTrue(0, input_condition=2)
    EnableFlag(728)


def Event722():
    """ 722: Event 722 """
    EndIfThisEventOn()
    IfFlagOn(1, 11407120)
    IfFlagOn(1, 11407130)
    IfFlagOn(1, 11407150)
    IfFlagOn(1, 11407160)
    IfFlagOn(1, 11407170)
    IfFlagOn(1, 11407140)
    IfFlagOn(1, 11407180)
    IfFlagOn(1, 11407190)
    IfFlagOn(1, 10)
    IfPlayerHasWeapon(1, 1332500, including_box=False)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(722)


def Event723():
    """ 723: Event 723 """
    EndIfThisEventOn()
    IfFlagOn(1, 11027130)
    IfFlagOn(1, 11027140)
    IfFlagOn(1, 11027150)
    IfFlagOn(1, 11027160)
    IfFlagOn(1, 11027170)
    IfFlagOn(1, 11027180)
    IfFlagOn(1, 11027190)
    IfFlagOn(1, 11027200)
    IfFlagOn(1, 11027210)
    IfFlagOn(1, 11027220)
    IfFlagOn(1, 11027230)
    IfFlagOn(1, 11027240)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(723)


def Event724():
    """ 724: Event 724 """
    EndIfThisEventOn()
    IfFlagOn(1, 11017050)
    IfFlagOn(1, 11017060)
    IfFlagOn(1, 11017070)
    IfFlagOn(1, 11017080)
    IfFlagOn(1, 11017090)
    IfFlagOn(1, 11017100)
    IfFlagOn(1, 11017110)
    IfFlagOn(1, 11017120)
    IfFlagOn(1, 11017130)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(724)


def Event725():
    """ 725: Event 725 """
    EndIfThisEventOn()
    IfTrueFlagCountGreaterThanOrEqual(0, 2, (11707100, 11707190))
    EnableFlag(725)


def Event726():
    """ 726: Event 726 """
    EndIfThisEventOn()
    IfTrueFlagCountGreaterThanOrEqual(0, 2, (11607000, 11607090))
    EnableFlag(726)


def Event727():
    """ 727: Event 727 """
    EndIfThisEventOn()
    IfFlagOn(1, 11327000)
    IfFlagOn(1, 11327010)
    IfFlagOn(1, 11327020)
    IfFlagOn(1, 11327030)
    IfFlagOn(1, 11327040)
    IfFlagOn(1, 11327050)
    IfFlagOn(1, 11327060)
    IfFlagOn(1, 11327070)
    IfFlagOn(1, 11327080)
    IfFlagOn(1, 11327090)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(727)


def Event740():
    """ 740: Event 740 """
    IfPlayerClass(0, ClassType.Pyromancer)
    EnableFlag(740)


def Event745():
    """ 745: Event 745 """
    IfFlagOn(7, 1604)
    IfFlagOn(7, 1764)
    SkipLinesIfConditionFalse(1, 7)
    IfFlagOn(0, 703)
    SkipLinesIfFlagOn(1, 1604)
    IfFlagOn(-1, 1604)
    SkipLinesIfFlagOn(1, 1764)
    IfFlagOn(-1, 1764)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    End()


def Event754():
    """ 754: Event 754 """
    DisableFlag(754)
    IfFlagOn(0, 754)
    DisableFlag(754)
    AddSpecialEffect(PLAYER, 4600)
    AddSpecialEffect(PLAYER, 4601)
    CreateTemporaryFX(22715, anchor_entity=10000, anchor_type=CoordEntityType.Character, model_point=7)
    Restart()


def Event770():
    """ 770: Event 770 """
    IfFlagOn(0, 755)
    DisableFlag(755)
    DisableFlag(742)
    DisableFlag(743)
    DisableFlag(744)
    DisableFlag(745)
    DisableFlag(746)
    DisableFlagRange((11000501, 11000519))
    DisableFlagRange((11010501, 11010519))
    DisableFlagRange((11020501, 11020529))
    DisableFlagRange((11100501, 11100519))
    DisableFlagRange((11200501, 11200519))
    DisableFlagRange((11300501, 11300519))
    DisableFlagRange((11310501, 11310519))
    DisableFlagRange((11320501, 11320519))
    DisableFlagRange((11400501, 11400519))
    DisableFlagRange((11410501, 11410519))
    DisableFlagRange((11500501, 11500519))
    DisableFlagRange((11510501, 11510519))
    DisableFlagRange((11600501, 11600519))
    DisableFlagRange((11700501, 11700519))
    DisableFlagRange((11800501, 11800519))
    DisableFlagRange((11810501, 11810519))
    DisableFlagRange((11210501, 11210519))
    DisableFlag(1004)
    DisableFlag(1033)
    DisableFlag(1096)
    DisableFlag(1114)
    DisableFlag(1176)
    DisableFlag(1179)
    DisableFlag(1195)
    DisableFlag(1197)
    DisableFlag(1213)
    DisableFlag(1223)
    DisableFlag(1241)
    DisableFlag(1253)
    DisableFlag(1282)
    DisableFlag(1283)
    DisableFlag(1287)
    DisableFlag(1294)
    DisableFlag(1314)
    DisableFlag(1321)
    DisableFlag(1341)
    DisableFlag(1361)
    DisableFlag(1381)
    DisableFlag(1401)
    DisableFlag(1411)
    DisableFlag(1421)
    DisableFlag(1434)
    DisableFlag(1461)
    DisableFlag(1512)
    DisableFlag(1547)
    DisableFlag(1574)
    DisableFlag(1603)
    DisableFlag(1627)
    DisableFlag(1646)
    DisableFlag(1675)
    DisableFlag(1691)
    EnableFlag(1710)
    DisableFlag(1711)
    DisableFlag(1712)
    DisableFlag(11200596)
    DisableFlag(71200035)
    DisableFlag(71200042)
    DisableFlag(1763)
    DisableFlag(1822)
    DisableFlag(1841)
    DisableFlag(1863)
    DisableFlag(1871)
    SetTeamType(6001, TeamType.Ally)
    SetTeamType(6040, TeamType.Ally)
    SetTeamType(6072, TeamType.Ally)
    SetTeamType(6190, TeamType.Ally)
    SetTeamType(6230, TeamType.Ally)
    SetTeamType(6300, TeamType.Ally)
    Restart()


def Event772():
    """ 772: Event 772 """
    IfFlagOff(0, 744)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1033)
    IfFlagOn(-1, 1096)
    IfFlagOn(-1, 1114)
    IfFlagOn(-1, 1176)
    IfFlagOn(-1, 1179)
    IfFlagOn(-1, 1195)
    IfFlagOn(-1, 1197)
    IfFlagOn(-1, 1213)
    IfFlagOn(-1, 1223)
    IfFlagOn(-1, 1241)
    IfFlagOn(-1, 1253)
    IfFlagOn(-1, 1282)
    IfFlagOn(-1, 1283)
    IfFlagOn(-1, 1287)
    IfFlagOn(-1, 1294)
    IfFlagOn(-1, 1314)
    IfFlagOn(-1, 1321)
    IfFlagOn(-1, 1341)
    IfFlagOn(-1, 1361)
    IfFlagOn(-1, 1381)
    IfFlagOn(-1, 1401)
    IfFlagOn(-1, 1411)
    IfFlagOn(-1, 1421)
    IfFlagOn(-1, 1434)
    IfFlagOn(-1, 1461)
    IfFlagOn(-1, 1512)
    IfFlagOn(-1, 1547)
    IfFlagOn(-1, 1574)
    IfFlagOn(-1, 1603)
    IfFlagOn(-1, 1627)
    IfFlagOn(-1, 1646)
    IfFlagOn(-1, 1675)
    IfFlagOn(-1, 1691)
    IfFlagOn(-1, 1711)
    IfFlagOn(-1, 1712)
    IfFlagOn(-1, 71200035)
    IfFlagOn(-1, 71200042)
    IfFlagOn(-1, 1763)
    IfFlagOn(-1, 1822)
    IfFlagOn(-1, 1841)
    IfFlagOn(-1, 1863)
    IfFlagOn(-1, 1871)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(744)
    IfFlagOff(0, 744)
    Restart()


def Event761():
    """ 761: Event 761 """
    DisableNetworkSync()
    IfFlagOn(0, 760)
    WaitFrames(200)
    DisableFlag(760)
    Restart()


def Event763():
    """ 763: Event 763 """
    DisableNetworkSync()
    IfFlagOn(0, 762)
    ForceAnimation(PLAYER, 7697)
    Wait(3.5)
    DisableFlag(762)
    Wait(2.799999952316284)
    DisableFlag(764)
    ForceAnimation(PLAYER, 7701, loop=True)
    Restart()


def Event750():
    """ 750: Event 750 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 71)
    IfCharacterHasSpecialEffect(-1, PLAYER, 72)
    IfCharacterHasSpecialEffect(-1, PLAYER, 73)
    IfCharacterHasSpecialEffect(-1, PLAYER, 74)
    IfFlagOn(-1, 751)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(751)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 71)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 72)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 73)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 74)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(751)
    Restart()


def Event752():
    """ 752: Event 752 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(-1, PLAYER, 5213)
    IfCharacterHasSpecialEffect(-1, PLAYER, 5214)
    IfFlagOn(-1, 753)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(753)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5213)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5214)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(753)
    DisableFlag(11400591)
    Restart()


def Event757():
    """ 757: Event 757 """
    SkipLinesIfFlagOff(1, 757)
    DisplayStatus(10010660, pad_enabled=True)
    DisableFlag(757)
    IfHost(1)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 71)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 72)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 73)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 74)
    IfCharacterHasSpecialEffect(-1, PLAYER, 33)
    IfCharacterHasSpecialEffect(-1, PLAYER, 34)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    End()


def Event758():
    """ 758: Event 758 """
    SkipLinesIfThisEventOff(1)
    DisplayStatus(10010670, pad_enabled=True)
    DisableFlag(758)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, 0.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 2130)
    IfConditionTrue(0, input_condition=1)
    IfHost(2)
    IfCharacterDead(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2130)
    IfConditionTrue(0, input_condition=2)
    End()


def Event759():
    """ 759: Event 759 """
    SkipLinesIfThisEventOff(1)
    DisplayStatus(10010680, pad_enabled=True)
    DisableFlag(759)
    IfHost(1)
    IfHealthLessThanOrEqual(1, PLAYER, 0.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 2131)
    IfConditionTrue(0, input_condition=1)
    IfHost(2)
    IfCharacterDead(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 2131)
    IfConditionTrue(0, input_condition=2)
    End()


def Event818():
    """ 818: Event 818 """
    SkipLinesIfFlagOn(2, 11510150)
    IfFlagOn(0, 11510150)
    DisplayStatus(10010690, pad_enabled=True)
    IfFlagOn(1, 11510150)
    IfOutsideMap(1, game_map=ANOR_LONDO)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11510150)
    Restart()


def Event810():
    """ 810: Event 810 """
    EndIfThisEventOn()
    IfFlagOn(0, 50001031)
    EnableFlag(810)


def Event812(_, arg_0_3: int):
    """ 812: Event 812 """
    EndIfThisEventSlotOn()
    IfFlagOn(0, arg_0_3)
    End()


def Event822():
    """ 822: Event 822 """
    IfFlagOn(0, 830)
    IfTimeElapsed(1, 0.5)
    IfOutsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(830)
    Restart()


def Event823():
    """ 823: Event 823 """
    IfFlagOn(0, 831)
    IfTimeElapsed(1, 0.5)
    IfOutsideMap(1, game_map=KILN_OF_THE_FIRST_FLAME)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(831)
    Restart()


def Event840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 840: Event 840 """
    DisableFlag(arg_0_3)
    IfFlagOn(0, arg_0_3)
    SkipLinesIfFlagOn(3, 844)
    SkipLinesIfFlagOn(2, 847)
    RotateToFaceEntity(PLAYER, arg_8_11)
    ForceAnimation(PLAYER, arg_4_7)
    SkipLinesIfFlagOn(9, 840)
    SkipLinesIfFlagOn(8, 841)
    SkipLinesIfFlagOn(7, 842)
    SkipLinesIfFlagOn(6, 843)
    SkipLinesIfFlagOn(5, 845)
    SkipLinesIfFlagOn(4, 846)
    SkipLinesIfFlagOn(3, 848)
    SkipLinesIfFlagOn(2, 849)
    SkipLinesIfFlagOn(1, 860)
    ForceAnimation(PLAYER, arg_4_7, skip_transition=True)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=123456789)
    Wait(4.0)
    SkipLinesIfEqual(1, left=arg_12_15, right=-1)
    ForceAnimation(PLAYER, arg_12_15, loop=True)
    Restart()


def Event766():
    """ 766: Event 766 """
    IfOnline(1)
    EndIfConditionTrue(1)
    EnableFlag(765)


def HookCheck():
    """ 2510: Keeps enabling a flag and expects mod hook to disable it within two seconds. If not, shows an error
    message. """
    EnableFlag(CommonFlags.HookCheckFlag)
    Wait(10.0)  # MSB generator shouldn't take longer than this.
    if CommonFlags.HookCheckFlag:
        # Display error message and disable all pending request flags.
        DisplayBattlefieldMessage(CommonTexts.HookConnectionError, 0)
        DisableFlag(CommonFlags.RequestWarpToFirelink)
        DisableFlag(CommonFlags.RequestFirelinkSpawnReset)
        DisableFlag(CommonFlags.AbyssBattleRequest)
        DisableFlag(CommonFlags.StatBoostRequest)
        DisableFlag(CommonFlags.StatResetRequest)
        DisableFlag(CommonFlags.AttunementClearRequest)
        DisableFlag(CommonFlags.SpellRechargeRequest)
        DisableFlag(CommonFlags.BonfireCreationRequest)
        DisableFlag(CommonFlags.DoRunSetupFlag)
        DisableFlag(CommonFlags.DoRunCleanupFlag)
        DisableFlag(11002005)
        DisableFlag(11002015)
        DisableFlag(11012005)
        DisableFlag(11012015)
        DisableFlag(11012025)
        DisableFlag(11012035)
        DisableFlag(11012045)
        DisableFlag(11012055)
        DisableFlag(11012305)
        DisableFlag(11012315)
        DisableFlag(11012325)
        DisableFlag(11012335)
        DisableFlag(11012345)
        DisableFlag(11202005)
        DisableFlag(11202015)
        DisableFlag(11202025)
        DisableFlag(11202035)
        DisableFlag(11212005)
        DisableFlag(11212015)
        DisableFlag(11212025)
        DisableFlag(11212305)
        DisableFlag(11212315)
        DisableFlag(11212605)
        DisableFlag(11302005)
        DisableFlag(11302025)
        DisableFlag(11312005)
        DisableFlag(11322005)
        DisableFlag(11322015)
        DisableFlag(11322305)
        DisableFlag(11322315)
        DisableFlag(11402005)
        DisableFlag(11402015)
        DisableFlag(11402025)
        DisableFlag(11402035)
        DisableFlag(11412005)
        DisableFlag(11412015)
        DisableFlag(11412025)
        DisableFlag(11412035)
        DisableFlag(11412305)
        DisableFlag(11412315)
        DisableFlag(11502005)
        DisableFlag(11502015)
        DisableFlag(11512005)
        DisableFlag(11512015)
        DisableFlag(11602005)
        DisableFlag(11602015)
        DisableFlag(11602025)
        DisableFlag(11702005)
        DisableFlag(11802005)
    Wait(5.0)
    return RESTART


def CleanupRun():
    """ 2511: Script runs when a run ends (because the player finished it, ran out of lives, or completed it). """
    Await(CommonFlags.DoRunCleanupFlag)
    DisableFlag(CommonFlags.DoRunCleanupFlag)
    DisableFlag(CommonFlags.RunCleanupCompleteFlag)
    DisableFlag(CommonFlags.RunHasStarted)
    DisableFlag(CommonFlags.Permadeath)
    DisableFlag(CommonFlags.OneBonfireCreated)
    DisableFlag(CommonFlags.TwoBonfiresCreated)

    DisableFlagRange((1600, 1699))  # Merchant hostile/dead flags.

    if FlagEnabled(1951) and FlagDisabled(1952):
        # Didn't make it past first level.
        EnableFlag(CommonFlags.AllyGiftUnavailable)
    else:
        DisableFlag(CommonFlags.AllyGiftUnavailable)
    # Disable map level flags and go back to level 1.
    DisableFlagRange((1950, 1959))
    EnableFlag(1951)

    EnableFlag(CommonFlags.StatResetRequest)
    EnableFlag(CommonFlags.AttunementClearRequest)

    # Disable life counter (and permadeath flag 1909).
    # New life counter will be determined at run startup.
    DisableFlagRange((1900, 1909))

    # Disable starting equipment/option flags.
    DisableFlagRange((11022400, 11022410))
    DisableFlag(CommonFlags.StartingEquipmentReceived)

    DisableFlag(CommonFlags.OneAllyGiftReceived)
    DisableFlag(CommonFlags.TwoAllyGiftsReceived)
    DisableFlagRange((1960, 1969))  # No gift effects.
    # Disable all gift item lots.
    DisableFlag(50051000)
    DisableFlag(50051010)
    DisableFlag(50051020)
    DisableFlag(50051030)
    DisableFlag(50051040)
    DisableFlag(50051050)
    DisableFlag(50051060)
    DisableFlag(50051070)

    # Disable miscellaneous flags.
    DisableFlag(51020002)  # Homeward Bones in Firelink well are available again.
    DisableFlag(CommonFlags.SiegmeyerCarePackageReceived)
    DisableFlag(CommonFlags.QuelanaCarePackageReceived)
    DisableFlag(CommonFlags.DisableAbyssPortal)
    DisableFlag(CommonFlags.InBossBattle)

    # Disable ALL map flags. Includes enemy despawn flags (3000 to 3999) and chest item lot flags (4000 to 4999).
    DisableFlagRange((11000000, 11004999))
    DisableFlagRange((11010000, 11014999))
    DisableFlagRange((11100000, 11104999))
    DisableFlagRange((11200000, 11204999))
    DisableFlagRange((11210000, 11214999))
    DisableFlagRange((11300000, 11304999))
    DisableFlagRange((11310000, 11314999))
    DisableFlagRange((11320000, 11324999))
    DisableFlagRange((11400000, 11404999))
    DisableFlagRange((11410000, 11414999))
    DisableFlagRange((11500000, 11504999))
    DisableFlagRange((11510000, 11514999))
    DisableFlagRange((11600000, 11604999))
    DisableFlagRange((11700000, 11704999))
    DisableFlagRange((11800000, 11804999))

    # Disable corpse item lot flags.
    DisableFlagRange((51000000, 51009999))
    DisableFlagRange((51010000, 51019999))
    DisableFlagRange((51100000, 51103999))
    DisableFlagRange((51200000, 51209999))
    DisableFlagRange((51210000, 51219999))
    DisableFlagRange((51300000, 51309999))
    DisableFlagRange((51310000, 51319999))
    DisableFlagRange((51320000, 51329999))
    DisableFlagRange((51400000, 51409999))
    DisableFlagRange((51410000, 51419999))
    DisableFlagRange((51500000, 51509999))
    DisableFlagRange((51510000, 51519999))
    DisableFlagRange((51600000, 51609999))
    DisableFlagRange((51700000, 51709999))
    DisableFlagRange((51800000, 51809999))

    # Disable ObjAct state flags.
    DisableFlagRange((61000000, 61009999))
    DisableFlagRange((61010000, 61019999))
    DisableFlagRange((61100000, 61103999))
    DisableFlagRange((61200000, 61209999))
    DisableFlagRange((61210000, 61219999))
    DisableFlagRange((61300000, 61309999))
    DisableFlagRange((61310000, 61319999))
    DisableFlagRange((61320000, 61329999))
    DisableFlagRange((61400000, 61409999))
    DisableFlagRange((61410000, 61419999))
    DisableFlagRange((61500000, 61509999))
    DisableFlagRange((61510000, 61519999))
    DisableFlagRange((61600000, 61609999))
    DisableFlagRange((61700000, 61709999))
    DisableFlagRange((61800000, 61809999))

    # Disable merchant item bought flags.
    DisableFlagRange((11817000, 11817999))

    # Remove all Marks of Death.
    RemoveGoodFromPlayer(CommonGoods.MarkOfDeath, 0)

    # Last weapon base ID is 323000.
    for weapon in range(100000, 324000, 100):
        RemoveWeaponFromPlayer(weapon, 0)

    # Remove starting equipment.
    for starting_weapon in range(1000, 22000, 100):
        RemoveWeaponFromPlayer(starting_weapon, 0)

    # Arrows
    for weapon in range(2000000, 2009000, 1000):
        RemoveWeaponFromPlayer(weapon, 0)

    # Bolts
    for weapon in range(2100000, 2105000, 1000):
        RemoveWeaponFromPlayer(weapon, 0)

    # Last armor set is 740000.
    for armor_set in range(100000, 750000, 10000):
        for piece_offset in (0, 1000, 2000, 3000):
            RemoveArmorFromPlayer(armor_set + piece_offset, 0)
            RemoveArmorFromPlayer(armor_set + piece_offset + 1, 0)  # Titanite upgrades
            RemoveArmorFromPlayer(armor_set + piece_offset + 2, 0)
            RemoveArmorFromPlayer(armor_set + piece_offset + 3, 0)
            RemoveArmorFromPlayer(armor_set + piece_offset + 4, 0)

    # Consumables
    RemoveGoodFromPlayer(230)
    RemoveGoodFromPlayer(240)
    RemoveGoodFromPlayer(260)
    RemoveGoodFromPlayer(270)
    RemoveGoodFromPlayer(271)
    RemoveGoodFromPlayer(272)
    RemoveGoodFromPlayer(274)
    RemoveGoodFromPlayer(275)
    RemoveGoodFromPlayer(280)
    RemoveGoodFromPlayer(290)
    RemoveGoodFromPlayer(291)
    RemoveGoodFromPlayer(292)
    RemoveGoodFromPlayer(293)
    RemoveGoodFromPlayer(294)
    RemoveGoodFromPlayer(296)
    RemoveGoodFromPlayer(297)
    RemoveGoodFromPlayer(310)
    RemoveGoodFromPlayer(311)
    RemoveGoodFromPlayer(312)
    RemoveGoodFromPlayer(313)
    RemoveGoodFromPlayer(330)
    RemoveGoodFromPlayer(370)
    for soul in range(400, 410):
        RemoveGoodFromPlayer(soul)
    RemoveGoodFromPlayer(500)
    RemoveGoodFromPlayer(501)

    for mote in range(8):
        RemoveGoodFromPlayer(650 + mote)
        RemoveGoodFromPlayer(660 + mote)

    # Embers and Titanite
    for material in range(1000, 1140, 10):
        RemoveGoodFromPlayer(material)

    # Key Items
    for key_item in range(2000, 2011):
        RemoveGoodFromPlayer(key_item)
    RemoveGoodFromPlayer(2100)  # Skeleton Keys

    # Spells
    for spell_item in range(3000, 6000, 10):
        RemoveGoodFromPlayer(spell_item)

    # TODO: Remove Black Eye Orb, when implemented.

    RemoveRingFromPlayer(Rings.AlvinaRing)
    RemoveRingFromPlayer(Rings.SolaireRing)
    RemoveRingFromPlayer(Rings.SiegmeyerRing)
    RemoveRingFromPlayer(Rings.LoganRing)
    RemoveRingFromPlayer(Rings.QuelanaRing)
    RemoveRingFromPlayer(Rings.HavelRing)
    RemoveRingFromPlayer(Rings.MornsteinRing)
    RemoveRingFromPlayer(Rings.LobosJrRing)

    AddSpecialEffect(PLAYER, 3000)  # Divine Blessing effect to restore HP.
    AddSpecialEffect(PLAYER, 3051)  # Divine Blessing effect to heal bleed.
    AddSpecialEffect(PLAYER, 3061)  # Divine Blessing effect to heal poison.
    AddSpecialEffect(PLAYER, 3071)  # Divine Blessing effect to heal toxic.
    AddSpecialEffect(PLAYER, 3090)  # Purging Stone effect to heal curse.
    AddSpecialEffect(PLAYER, 3091)  # Egg Vermifuge effect to heal parasite.

    DisableFlag(CommonFlags.RunHasStarted)
    EnableFlag(CommonFlags.RunCleanupCompleteFlag)
    EnableFlag(CommonFlags.RequestFirelinkSpawnReset)
    EnableFlag(CommonFlags.ShowUncurlMessage)
    EnableFlag(CommonFlags.RequestWarpToFirelink)


def KillPlayerOnBossQuit():
    """ 2512: Kills player if `InBossBattle` flag is enabled on load. """
    if not CommonFlags.InBossBattle or InsideMap(NEW_LONDO_RUINS):
        return
    DisableFlag(CommonFlags.InBossBattle)
    if CommonFlags.AbyssBattleActive:
        DisableFlag(CommonFlags.AbyssBattleActive)
        Kill(PLAYER)  # Kill player if they quit in an Abyss battle.
    return


def CreateBonfire():
    """ 2513: Player uses the bonfire creation item. """
    Await(HasSpecialEffect(PLAYER, CommonEffects.CreateBonfire))

    if InsideMap(PAINTED_WORLD) or InsideMap(FIRELINK_SHRINE):
        # Can't create bonfires in the Painted World.
        DisplayBattlefieldMessage(CommonTexts.BonfireCreationFailed, 0)
        Await(not HasSpecialEffect(PLAYER, CommonEffects.CreateBonfire))
        return RESTART

    if CommonFlags.TwoBonfiresCreated or (CommonFlags.OneBonfireCreated and not CommonFlags.SolaireRingFlag):
        DisplayBattlefieldMessage(CommonTexts.MaxBonfiresCreated, 0)
        Await(not HasSpecialEffect(PLAYER, CommonEffects.CreateBonfire))
        return RESTART

    EnableFlag(CommonFlags.BonfireCreationRequest)
    success = Condition(CommonFlags.BonfireRequestSuccessful)
    failure = Condition(CommonFlags.BonfireRequestUnsuccessful)
    Await(success or failure)
    if failure:
        DisableFlag(CommonFlags.BonfireRequestUnsuccessful)
        DisplayBattlefieldMessage(CommonTexts.BonfireCreationFailed, 0)
        Await(not HasSpecialEffect(PLAYER, CommonEffects.CreateBonfire))
        return RESTART
    DisableFlag(CommonFlags.BonfireRequestSuccessful)
    if CommonFlags.OneBonfireCreated:
        DisableFlag(CommonFlags.OneBonfireCreated)
        EnableFlag(CommonFlags.TwoBonfiresCreated)
    else:
        EnableFlag(CommonFlags.OneBonfireCreated)
    DisplayBattlefieldMessage(CommonTexts.BonfireCreationSuccess, 0)
    Wait(2.0)
    # Mod program also waits two seconds, then warps player to last bonfire.
    return RESTART


@RestartOnRest
def DireDamageModifier():
    """ 2520: Apply dire weapon damage modifier. """
    Await(HasSpecialEffect(PLAYER, CommonEffects.DireEquipped))
    if any((CommonFlags.LifeCount9, CommonFlags.LifeCount5)):
        AddSpecialEffect(PLAYER, CommonEffects.DireDamageWayDown)
    elif CommonFlags.LifeCount4:
        AddSpecialEffect(PLAYER, CommonEffects.DireDamageDown)
    elif CommonFlags.LifeCount3:
        AddSpecialEffect(PLAYER, CommonEffects.DireDamageNoChange)
    elif CommonFlags.LifeCount2:
        AddSpecialEffect(PLAYER, CommonEffects.DireDamageUp)
    else:
        AddSpecialEffect(PLAYER, CommonEffects.DireDamageWayUp)

    Await(not HasSpecialEffect(PLAYER, CommonEffects.DireEquipped))
    CancelSpecialEffect(PLAYER, CommonEffects.DireDamageWayDown)
    CancelSpecialEffect(PLAYER, CommonEffects.DireDamageDown)
    CancelSpecialEffect(PLAYER, CommonEffects.DireDamageNoChange)
    CancelSpecialEffect(PLAYER, CommonEffects.DireDamageUp)
    CancelSpecialEffect(PLAYER, CommonEffects.DireDamageWayUp)

    return RESTART


@RestartOnRest
def ShieldHitTrigger():
    """ 2521: Give the player a SpEffect under certain conditions when shield is hit (TAE SpEffect). """
    Await(HasSpecialEffect(PLAYER, CommonEffects.ShieldHitTrigger))
    if HasSpecialEffect(PLAYER, 8085):
        AddSpecialEffect(PLAYER, 8086)  # weaken physical attack
    if HasSpecialEffect(PLAYER, 8087):
        AddSpecialEffect(PLAYER, 8088)  # curse
    if HasSpecialEffect(PLAYER, 8089):
        AddSpecialEffect(PLAYER, 8090)  # lose souls
    Await(not HasSpecialEffect(PLAYER, CommonEffects.ShieldHitTrigger))
    return RESTART


@RestartOnRest
def RollingTrigger():
    """ 2522: Give the player a SpEffect under certain conditions when shield is hit (TAE SpEffect). """
    Await(HasSpecialEffect(PLAYER, CommonEffects.RollingDamageTrigger))
    if HasSpecialEffect(PLAYER, CommonEffects.RollingDamageActive):
        AddSpecialEffect(PLAYER, CommonEffects.RollingDamageEffect)
    Await(not HasSpecialEffect(PLAYER, CommonEffects.RollingDamageTrigger))
    return RESTART


def InvisibleEffect():
    """ 2523: Player becomes invisible (mod hook effect) when effect is present. """
    Await(HasSpecialEffect(PLAYER, CommonEffects.InvisibleEffect))
    EnableFlag(CommonFlags.InvisibleEffect)
    Await(not HasSpecialEffect(PLAYER, CommonEffects.InvisibleEffect))
    DisableFlag(CommonFlags.InvisibleEffect)
    return RESTART


def EnchantedSpellRechargeRequest():
    """ 2524: Requests mod hook to recharge all spells (as a proportion of max usages). """
    Await(HasSpecialEffect(PLAYER, CommonEffects.EnchantedHitTrigger))
    EnableFlag(CommonFlags.SpellRechargeRequest)
    Wait(2.0)  # Let hook work, and provide "cooldown" for effect.
    Await(not HasSpecialEffect(PLAYER, CommonEffects.EnchantedHitTrigger))
    DisableFlag(CommonFlags.SpellRechargeRequest)  # Mod hook has hopefully disabled it already.
    return RESTART


def GoToNewGamePlus():
    """ 2525: Player uses Heart of St. Jude item to go to NG+. """
    Await(HasSpecialEffect(PLAYER, CommonEffects.NewGamePlus))
    IncrementNewGameCycle(1)
    Await(not HasSpecialEffect(PLAYER, CommonEffects.NewGamePlus))
    return RESTART


def QuitRun():
    """ 2528: Player uses Hand of Cessation item to quit run. """
    Await(HasSpecialEffect(PLAYER, CommonEffects.QuitRun))
    EnableFlag(CommonFlags.DoRunCleanupFlag)
    Await(not HasSpecialEffect(PLAYER, CommonEffects.QuitRun))
    return RESTART


def MarkRunStart():
    """ 2529: Enables flag for run start when they load the map and are NOT in Firelink (or Asylum, briefly). """
    if not InsideMap(FIRELINK_SHRINE) and not InsideMap(UNDEAD_ASYLUM):
        EnableFlag(CommonFlags.RunHasStarted)  # Also marked in hook.
    return


def LoseLife():
    """ 2530: Player loses a life when they die. """
    Await(not InsideMap(FIRELINK_SHRINE) and HealthRatio(PLAYER) <= 0)
    DisableFlag(CommonFlags.InBossBattle)   # Don't kill player again when they respawn!
    AwardItemLot(CommonItemLots.MarkOfDeathLot)
    if FlagEnabled(CommonFlags.LifeCount9):
        DisableFlag(CommonFlags.LifeCount9)
        EnableFlag(CommonFlags.LifeCount8)
    elif FlagEnabled(CommonFlags.LifeCount8):
        DisableFlag(CommonFlags.LifeCount8)
        EnableFlag(CommonFlags.LifeCount7)
    elif FlagEnabled(CommonFlags.LifeCount7):
        DisableFlag(CommonFlags.LifeCount7)
        EnableFlag(CommonFlags.LifeCount6)
    elif FlagEnabled(CommonFlags.LifeCount6):
        DisableFlag(CommonFlags.LifeCount6)
        EnableFlag(CommonFlags.LifeCount5)
    elif FlagEnabled(CommonFlags.LifeCount5):
        DisableFlag(CommonFlags.LifeCount5)
        EnableFlag(CommonFlags.LifeCount4)
    elif FlagEnabled(CommonFlags.LifeCount4):
        DisableFlag(CommonFlags.LifeCount4)
        EnableFlag(CommonFlags.LifeCount3)
    elif FlagEnabled(CommonFlags.LifeCount3):
        DisableFlag(CommonFlags.LifeCount3)
        EnableFlag(CommonFlags.LifeCount2)
    elif FlagEnabled(CommonFlags.LifeCount2):
        DisableFlag(CommonFlags.LifeCount2)
        EnableFlag(CommonFlags.LifeCount1)
    elif FlagEnabled(CommonFlags.LifeCount1):
        DisableFlag(CommonFlags.LifeCount1)
        EnableFlag(CommonFlags.Permadeath)
    return


def RunPermadeath():
    """ 2531: Sends player back to Firelink when they respawn or reload with no lives left. """
    if not InsideMap(FIRELINK_SHRINE) and not InsideMap(UNDEAD_ASYLUM) and CommonFlags.Permadeath:
        EnableFlag(CommonFlags.DoRunCleanupFlag)
    return


def WarpRequest(_, warp_flag: int, map_area: int, map_block: int, start: int, spawn_point: int):
    """ 2600: Warp to given map and start point when flag is enabled. """
    Await(FlagEnabled(warp_flag))
    DisableFlag(warp_flag)
    if spawn_point != 0:
        SetRespawnPoint(spawn_point)
    WaitFrames(1)  # Allow flag to be disabled.
    WarpToMap((map_area, map_block), start)


def KilnAvailable():
    """ 1860: All four Lord Soul bosses defeated. Only enabled in Firelink. """
    if THIS_FLAG:
        return
    Await(InsideMap(FIRELINK_SHRINE) and CommonFlags.ArchivesBossDefeated and CommonFlags.IzalithBossDefeated
          and CommonFlags.TombBossDefeated and CommonFlags.NewLondoBossDefeated)
    EnableFlag(CommonFlags.KilnAvailable)


def StatBoostFlagToggle(_, speffect: int, flag: int):
    """ 2800: Flag is enabled exactly whenever player has given SpEffect. """
    DisableFlag(flag)
    Await(HasSpecialEffect(PLAYER, speffect))
    EnableFlag(flag)
    EnableFlag(CommonFlags.StatBoostRequest)  # disabled in mod hook
    Await(not HasSpecialEffect(PLAYER, speffect))
    return RESTART


def LevelIndicatorRequest(_, flag: Flag, text: Text):
    """ 2700: Request a status message showing level number upon map load. """
    if FlagDisabled(flag):
        return
    DisableFlag(flag)
    DisplayBattlefieldMessage(text, 0)


def AwardSiegmeyerGift():
    """ 2540: Get Siegmeyer gift. Delayed by a few seconds, so the player can clear Quelana's gift, potentially."""
    Await(OutsideMap(FIRELINK_SHRINE)
          and CommonFlags.SiegmeyerRingFlag
          and not CommonFlags.SiegmeyerCarePackageReceived)
    Wait(3.0)
    EnableFlag(CommonFlags.SiegmeyerCarePackageReceived)
    AwardItemLot(CommonItemLots.SiegmeyerGiftLot)


def AwardQuelanaGift():
    """ 2541: Get Quelana gift."""
    Await(OutsideMap(FIRELINK_SHRINE)
          and CommonFlags.QuelanaRingFlag
          and not CommonFlags.QuelanaCarePackageReceived)
    EnableFlag(CommonFlags.QuelanaCarePackageReceived)
    AwardItemLot(CommonItemLots.QuelanaGiftLot)
