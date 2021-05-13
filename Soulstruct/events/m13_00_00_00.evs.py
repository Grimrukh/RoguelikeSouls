"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from common_constants import *
from catacombs_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1303800,
        ItemLots.Boss1Reward,
        1301990, 1301991, 0, 0,
        1000, 1000,
    )

    # TODO: Boss battle up top.
    EnableFlag(Flags.Boss2Dead)
    # BossBattle(
    #     1,
    #     Chrs.Boss2, Chrs.Boss2Twin, Flags.Boss2IsTwin,
    #     Regions.Boss2Trigger, Flags.Boss2Dead, 1303801,
    #     ItemLots.Boss2Reward,
    #     1301890, 1301891, 0, 0,  # No exit fog (ladder instead).
    #     1000, 1000,
    # )

    RegisterBonfire(11300992, obj=1301960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)

    RegisterLadder(start_climbing_flag=11300010, stop_climbing_flag=11300011, obj=1301140)
    RegisterLadder(start_climbing_flag=11300012, stop_climbing_flag=11300013, obj=1301141)
    RegisterLadder(start_climbing_flag=11300014, stop_climbing_flag=11300015, obj=1301142)
    # Former ladder 1301143 (out of Pinwheel's) is disabled.
    RegisterLadder(start_climbing_flag=11300018, stop_climbing_flag=11300019, obj=1301144)
    RegisterLadder(start_climbing_flag=11300020, stop_climbing_flag=11300021, obj=1301145)
    RegisterLadder(start_climbing_flag=11300022, stop_climbing_flag=11300023, obj=1301146)
    RegisterLadder(start_climbing_flag=11300024, stop_climbing_flag=11300025, obj=1301147)
    RegisterBoss2Ladder()  # Ladder 1301148 only registered when boss 2 is dead.
    RegisterLadder(start_climbing_flag=11300028, stop_climbing_flag=11300029, obj=1301149)

    SkipLinesIfClient(3)
    DisableFlag(11300000)
    DisableObject(1301994)
    DeleteVFX(1301995, erase_root_only=False)
    DisableObject(1301700)
    DeleteVFX(1301701, erase_root_only=False)

    # Spike bridges.
    RunEvent(11300300)
    RunEvent(11300350)
    # Doors.
    RunEvent(11300900, slot=0, args=(11300900, 1301000, 1301100, 1304000))
    RunEvent(11300900, slot=1, args=(11300901, 1301001, 1301101, 1304001))
    RunEvent(11305032, slot=0, args=(11300902, 11300903, 11305035, 11305036))
    RunEvent(11305030, slot=0, args=(11300402, 11305035, 11305036, 1301002, 1301102, 1304002))
    RunEvent(11305032, slot=1, args=(11300904, 11300905, 11305037, 11305038))
    RunEvent(11305030, slot=1, args=(11300403, 11305037, 11305038, 1301003, 1301103, 1304003))

    # Coffin events (just leaving).
    CoffinExit()  # Activates Exit 2.
    RunEvent(11305001)
    RunEvent(11305002)
    RunEvent(11305003)
    RunEvent(11305004)
    RunEvent(11305009)
    RunEvent(11300420, slot=0, args=(10000,))
    RunEvent(11300420, slot=1, args=(10001,))
    RunEvent(11300420, slot=2, args=(10002,))
    RunEvent(11300420, slot=3, args=(10003,))
    RunEvent(11300420, slot=4, args=(10004,))
    RunEvent(11300420, slot=5, args=(10005,))
    RunEvent(11300420, slot=6, args=(10006,))
    RunEvent(11300420, slot=7, args=(10007,))
    RunEvent(11300420, slot=8, args=(10008,))
    RunEvent(11300420, slot=9, args=(10009,))
    RunEvent(11300420, slot=10, args=(10010,))
    RunEvent(11300420, slot=11, args=(10011,))
    RunEvent(11300420, slot=12, args=(10012,))
    RunEvent(11300420, slot=13, args=(10013,))
    RunEvent(11300420, slot=14, args=(10014,))
    RunEvent(11300420, slot=15, args=(10015,))
    RunEvent(11300420, slot=16, args=(10016,))
    RunEvent(11300420, slot=17, args=(10017,))

    # Vamos wall always disabled.
    DisableObject(1301030)
    DisableObject(1301031)

    RevealLadderAfterBoss()

    # Collapsing floors.
    RunEvent(11300100, slot=0, args=(11300100, 1302100, 1301010, 303000000))
    RunEvent(11300100, slot=1, args=(11300101, 1302101, 1301011, 303100000))
    RunEvent(11300100, slot=2, args=(11300102, 1302102, 1301012, 303200000))
    RunEvent(11300100, slot=3, args=(11300103, 1302103, 1301013, 303300000))
    RunEvent(11300100, slot=4, args=(11300104, 1302104, 1301014, 303400000))
    RunEvent(11300100, slot=5, args=(11300105, 1302105, 1301015, 303500000))

    # Ceiling break.
    RunEvent(11300150)
    # Illusory wall.
    RunEvent(11300160)
    IllusoryWallInvincible()

    # Statue spike traps. Now disabled if you have the Skeleton Keys.
    StatueSpikeTrap(0, 1301200, 11300750)
    StatueSpikeTrap(1, 1301201, 11300751)
    StatueSpikeTrap(2, 1301202, 11300752)
    StatueSpikeTrap(3, 1301203, 11300753)
    StatueSpikeTrap(4, 1301204, 11300754)
    StatueSpikeTrap(5, 1301205, 11300755)
    StatueSpikeTrap(6, 1301206, 11300756)
    StatueSpikeTrap(7, 1301207, 11300757)
    StatueSpikeTrap(8, 1301208, 11300758)
    StatueSpikeTrap(9, 1301209, 11300759)
    StatueSpikeTrap(10, 1301210, 11300760)
    StatueSpikeTrap(12, 1301212, 11300762)
    StatueSpikeTrap(13, 1301213, 11300763)
    StatueSpikeTrap(14, 1301214, 11300764)
    StatueSpikeTrap(15, 1301215, 11300765)
    StatueSpikeTrap(16, 1301216, 11300766)
    StatueSpikeTrap(17, 1301217, 11300767)
    StatueSpikeTrap(18, 1301218, 11300768)
    StatueSpikeTrap(19, 1301219, 11300769)

    # Chests.
    OpenChest(0, 1301650, 11300600)
    OpenChest(1, 1301651, 11300601)
    OpenChest(2, 1301652, 11300602)
    OpenChest(3, 1301653, 11300603)
    OpenChest(4, 1301654, 11300604)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # Despawn rare/red phantom enemies.
    for enemy in range(100):
        DespawnEnemy(enemy, 1300100 + enemy)

    GetReward(0, 1300130, CommonItemLots.SkeletonKeysLot, CommonFlags.SkeletonKeyObtained)

    DepartLevelUnconditional(
        0, Objects.Exit1Prompt, CommonTexts.DepartLevel, Flags.Exit1Disabled, Flags.Exit1Activated)
    # Coffin exit handled in 11305000.
    DepartLevelIfFlag(
        0, Objects.Exit3Prompt, CommonTexts.DepartLevel, Flags.Exit3Disabled, Flags.Boss1Dead,
        Flags.Exit3Activated)

    ActivateAbyssPortal(0, 1300997, 1300998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, 6990, 6991, Chrs.Invader, Regions.InvaderTrigger, Flags.InvaderDead)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


def Event11305390():
    """ 11305390: Event 11305390 """
    IfFlagOff(1, 6)
    IfCharacterAlive(1, 1300800)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1302998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1301990,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11305391():
    """ 11305391: Event 11305391 """
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305393)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1302998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1301990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1302997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11305393():
    """ 11305393: Event 11305393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305390)
    IfCharacterInsideRegion(1, PLAYER, region=1302996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1300800)


@RestartOnRest
def Event11305392():
    """ 11305392: Event 11305392 """
    SkipLinesIfFlagOff(3, 6)
    DisableCharacter(1300800)
    Kill(1300800, award_souls=False)
    End()
    SkipLinesIfFlagOn(1, 11300000)
    DisableCharacter(1300800)
    DisableAI(1300800)
    IfFlagOff(1, 6)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1302999)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(8, 11300000)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(130000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(130000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableCharacter(1300800)
    EnableFlag(11300000)
    EnableFlag(11300005)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1300800, UpdateAuthority.Forced)
    EnableAI(1300800)
    EnableBossHealthBar(1300800, name=3320, slot=0)


def Event11300001():
    """ 11300001: Event 11300001 """
    IfHealthLessThanOrEqual(0, 1300800, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1300800, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1300800)
    EnableFlag(6)
    KillBoss(1300800)
    DisableObject(1301990)
    DeleteVFX(1301991, erase_root_only=True)
    RegisterLadder(start_climbing_flag=11300016, stop_climbing_flag=11300017, obj=1301143)
    RunEvent(11300880)


def Event11305394():
    """ 11305394: Event 11305394 """
    DisableNetworkSync()
    IfFlagOff(1, 6)
    IfFlagOn(1, 11305392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11305391)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1303800)


def Event11305395():
    """ 11305395: Event 11305395 """
    DisableNetworkSync()
    IfFlagOn(1, 6)
    IfFlagOn(1, 11305394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1303800)


def Event11305396():
    """ 11305396: Event 11305396 """
    IfHasTAEEvent(0, 1300800, tae_event_id=600)
    DisableCharacter(1300800)
    DisableFlagRange((11305320, 11305326))
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1300800, UpdateAuthority.Forced)
    EnableRandomFlagInRange((11305320, 11305326))
    EnableFlag(11305329)
    IfFlagOff(-1, 11305329)
    IfTimeElapsed(-1, 5.0)
    IfConditionTrue(0, input_condition=-1)
    Wait(3.0)
    EnableCharacter(1300800)
    SkipLinesIfFlagOff(1, 11305320)
    Move(1300800, destination=1302600, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305321)
    Move(1300800, destination=1302602, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305322)
    Move(1300800, destination=1302604, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305323)
    Move(1300800, destination=1302605, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305324)
    Move(1300800, destination=1302606, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305325)
    Move(1300800, destination=1302608, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfFlagOff(1, 11305326)
    Move(1300800, destination=1302612, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    WaitFrames(1)
    EnableCharacter(1300800)
    ForceAnimation(1300800, 7000, wait_for_completion=True)
    Restart()


def Event11300882():
    """ 11300882: Event 11300882 """
    IfFlagOn(1, 11305329)
    IfFlagOn(2, 11305329)
    IfFlagOn(3, 11305329)
    IfFlagOn(4, 11305329)
    IfFlagOn(5, 11305329)
    IfFlagOn(6, 11305329)
    IfFlagOn(7, 11305329)
    IfFlagOn(1, 11305320)
    IfFlagOn(2, 11305321)
    IfFlagOn(3, 11305322)
    IfFlagOn(4, 11305323)
    IfFlagOn(5, 11305324)
    IfFlagOn(6, 11305325)
    IfFlagOn(7, 11305326)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(11305320)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11305321)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11305322)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11305323)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(11305324)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(11305325)
    SkipLinesIfFinishedConditionFalse(1, 7)
    EnableFlag(11305326)
    DisableFlag(11305329)
    Restart()


def Event11305397():
    """ 11305397: Event 11305397 """
    EndIfClient()
    SkipLinesIfFlagOn(4, 11305310)
    IfFlagOff(1, 11305399)
    IfHasTAEEvent(1, 1300800, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305310)
    DisableFlagRange((11305300, 11305306))
    EnableRandomFlagInRange((11305300, 11305306))
    SkipLinesIfFlagOff(2, 11305300)
    SkipLinesIfFlagRangeAnyOn(1, (11305251, 11305252))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305301)
    SkipLinesIfFlagRangeAnyOn(1, (11305253, 11305254))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305302)
    SkipLinesIfFlagRangeAnyOn(1, (11305255, 11305256))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305303)
    SkipLinesIfFlagRangeAnyOn(1, (11305257, 11305258))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305304)
    SkipLinesIfFlagRangeAnyOn(1, (11305259, 11305260))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305305)
    SkipLinesIfFlagRangeAnyOn(1, (11305261, 11305262))
    DisableFlag(11305310)
    SkipLinesIfFlagOff(2, 11305306)
    SkipLinesIfFlagRangeAnyOn(1, (11305263, 11305264))
    DisableFlag(11305310)
    RestartIfFlagOn(11305310)
    IfDoesNotHaveTAEEvent(0, 1300800, tae_event_id=700)
    Restart()


def Event11305398():
    """ 11305398: Event 11305398 """
    IfHealthLessThanOrEqual(0, 1300800, 0.30000001192092896)
    EnableFlag(11305399)
    AICommand(1300800, command_id=1, slot=1)
    ReplanAI(1300800)
    RunEvent(11305330, slot=0, args=(1300801, 11305251))
    RunEvent(11305330, slot=1, args=(1300802, 11305252))
    RunEvent(11305330, slot=2, args=(1300803, 11305253))
    RunEvent(11305330, slot=3, args=(1300804, 11305254))
    RunEvent(11305330, slot=4, args=(1300805, 11305255))
    RunEvent(11305330, slot=5, args=(1300806, 11305256))
    RunEvent(11305330, slot=6, args=(1300807, 11305257))
    RunEvent(11305330, slot=7, args=(1300808, 11305258))
    RunEvent(11305330, slot=8, args=(1300809, 11305259))
    RunEvent(11305330, slot=9, args=(1300810, 11305260))
    RunEvent(11305330, slot=10, args=(1300811, 11305261))
    RunEvent(11305330, slot=11, args=(1300812, 11305262))
    RunEvent(11305330, slot=12, args=(1300813, 11305263))
    RunEvent(11305330, slot=13, args=(1300814, 11305264))
    IfFlagRangeAllOff(0, (11305251, 11305264))
    AICommand(1300800, command_id=2, slot=1)
    ReplanAI(1300800)
    IfFlagOn(1, 11305399)
    IfHasTAEEvent(1, 1300800, tae_event_id=700)
    IfConditionTrue(0, input_condition=1)
    AICommand(1300800, command_id=1, slot=1)
    ReplanAI(1300800)
    RunEvent(11305350, slot=10, args=(11305251, 11305252, 1300801, 1300802, 1302602, 1302603, 11305300))
    RunEvent(11305350, slot=11, args=(11305253, 11305254, 1300803, 1300804, 1302604, 1302605, 11305301))
    RunEvent(11305350, slot=12, args=(11305255, 11305256, 1300805, 1300806, 1302607, 1302608, 11305302))
    RunEvent(11305350, slot=13, args=(11305257, 11305258, 1300807, 1300808, 1302609, 1302612, 11305303))


def Event11305330(_, arg_0_3: int, arg_4_7: int):
    """ 11305330: Event 11305330 """
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfFlagOff(0, arg_4_7)
    AICommand(arg_0_3, command_id=-1, slot=1)
    ReplanAI(arg_0_3)


def Event11305350(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int,
                  arg_24_27: int):
    """ 11305350: Event 11305350 """
    SkipLinesIfFlagOn(5, 11305399)
    IfHost(1)
    IfFlagOff(1, 11305310)
    IfFlagOn(1, arg_24_27)
    IfConditionTrue(0, input_condition=1)
    WaitForNetworkApproval(max_seconds=3.0)
    DisableFlag(arg_24_27)
    AddSpecialEffect(arg_8_11, 5450)
    AddSpecialEffect(arg_12_15, 5450)
    Move(arg_8_11, destination=arg_16_19, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Move(arg_12_15, destination=arg_20_23, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ReplanAI(arg_8_11)
    ReplanAI(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    EndIfFlagOn(11305399)
    RestartEvent(11305250, slot=0)
    Restart()


def Event11305370(_, arg_0_3: int, arg_4_7: int):
    """ 11305370: Event 11305370 """
    IfFlagOn(1, arg_4_7)
    IfHasTAEEvent(1, arg_0_3, tae_event_id=710)
    IfHealthLessThanOrEqual(2, 1300800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(3, 1)
    AICommand(arg_0_3, command_id=1, slot=1)
    ReplanAI(arg_0_3)
    IfHasTAEEvent(0, arg_0_3, tae_event_id=710)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    DisableCharacter(arg_0_3)
    DisableFlag(arg_4_7)
    EndIfFinishedConditionTrue(2)
    RestartEvent(11305250, slot=0)
    RestartIfFlagOff(arg_4_7)


def Event11305250():
    """ 11305250: Event 11305250 """
    IfFlagOn(0, 11305392)
    AIEvent(1300800, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300801, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300802, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300803, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300804, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300805, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300806, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300807, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300808, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300809, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300810, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300811, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300812, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300813, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    AIEvent(1300814, command_id=0, slot=0, first_event_flag=11305251, last_event_flag=11305264)
    ReplanAI(1300800)
    ReplanAI(1300801)
    ReplanAI(1300802)
    ReplanAI(1300803)
    ReplanAI(1300804)
    ReplanAI(1300805)
    ReplanAI(1300806)
    ReplanAI(1300807)
    ReplanAI(1300808)
    ReplanAI(1300809)
    ReplanAI(1300810)
    ReplanAI(1300811)
    ReplanAI(1300812)
    ReplanAI(1300813)
    ReplanAI(1300814)
    IfCharacterDead(0, 1300800)
    End()


def StatueSpikeTrap(_, statue: int, hazard_flag: int):
    """ 11300700: Now doesn't happen when the player has the Skeleton Keys. """
    IfPlayerDoesNotHaveGood(1, CommonGoods.SkeletonKeys)
    IfEntityWithinDistance(1, statue, PLAYER, radius=1.5)
    IfConditionTrue(0, 1)
    CreateHazard(hazard_flag, statue, model_point=100, behavior_param_id=5120, target_type=DamageTargetType.Character,
                 radius=0.10000000149011612, life=1.0, repetition_time=0.0)
    CreateHazard(hazard_flag, statue, model_point=101, behavior_param_id=5120, target_type=DamageTargetType.Character,
                 radius=0.10000000149011612, life=1.0, repetition_time=0.0)
    CreateHazard(hazard_flag, statue, model_point=102, behavior_param_id=5120, target_type=DamageTargetType.Character,
                 radius=0.10000000149011612, life=1.0, repetition_time=0.0)
    ForceAnimation(statue, 0, wait_for_completion=True)
    Restart()


def Event11300300():
    """ 11300300: Event 11300300 """
    IfFlagOff(0, 11300402)
    CreateHazard(11300301, 1301102, model_point=2, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=0.5, life=10.0, repetition_time=5.0)
    CreateHazard(11300302, 1301102, model_point=4, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300303, 1301102, model_point=6, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300304, 1301102, model_point=8, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300305, 1301102, model_point=10, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300306, 1301102, model_point=12, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300307, 1301102, model_point=14, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300308, 1301102, model_point=15, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=0.5, life=10.0, repetition_time=5.0)
    IfFlagOn(0, 11300402)
    RemoveObjectFlag(11300301)
    RemoveObjectFlag(11300302)
    RemoveObjectFlag(11300303)
    RemoveObjectFlag(11300304)
    RemoveObjectFlag(11300305)
    RemoveObjectFlag(11300306)
    RemoveObjectFlag(11300307)
    RemoveObjectFlag(11300308)
    Restart()


def Event11300350():
    """ 11300350: Event 11300350 """
    IfFlagOff(0, 11300403)
    CreateHazard(11300351, 1301103, model_point=2, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=0.5, life=10.0, repetition_time=5.0)
    CreateHazard(11300352, 1301103, model_point=4, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300353, 1301103, model_point=6, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300354, 1301103, model_point=8, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300355, 1301103, model_point=10, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300356, 1301103, model_point=12, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300357, 1301103, model_point=14, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300358, 1301103, model_point=33, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300359, 1301103, model_point=35, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300360, 1301103, model_point=37, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=1.0, life=10.0, repetition_time=5.0)
    CreateHazard(11300361, 1301103, model_point=39, behavior_param_id=5100, target_type=DamageTargetType.Character,
                 radius=0.5, life=10.0, repetition_time=5.0)
    IfFlagOn(0, 11300403)
    RemoveObjectFlag(11300351)
    RemoveObjectFlag(11300352)
    RemoveObjectFlag(11300353)
    RemoveObjectFlag(11300354)
    RemoveObjectFlag(11300355)
    RemoveObjectFlag(11300356)
    RemoveObjectFlag(11300357)
    RemoveObjectFlag(11300358)
    RemoveObjectFlag(11300359)
    RemoveObjectFlag(11300360)
    RemoveObjectFlag(11300361)
    Restart()


def Event11300900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300900: Event 11300900 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_8_11, 2)
    EndOfAnimation(arg_4_7, 2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    End()
    EnableNavmeshType(arg_12_15, NavmeshType.Solid)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    ForceAnimation(arg_8_11, 1)
    DisableNavmeshType(arg_12_15, NavmeshType.Solid)


def Event11305030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11305030: Event 11305030 """
    SkipLinesIfFlagOff(4, arg_0_3)
    DisableObjectActivation(arg_12_15, obj_act_id=3011)
    EndOfAnimation(arg_16_19, 0)
    EndOfAnimation(arg_12_15, 2)
    SkipLines(2)
    DisableObjectActivation(arg_12_15, obj_act_id=3012)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    SkipLinesIfFinishedConditionTrue(6, 2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 3)
    WaitFrames(140)
    EnableObjectActivation(arg_12_15, obj_act_id=3012)
    DisableNavmeshType(arg_20_23, NavmeshType.Solid)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_16_19, 1)
    WaitFrames(140)
    EnableObjectActivation(arg_12_15, obj_act_id=3011)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    Restart()


def Event11305032(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11305032: Event 11305032 """
    IfObjectActivated(1, obj_act_id=arg_0_3)
    IfObjectActivated(2, obj_act_id=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(arg_8_11)
    Restart()
    EnableFlag(arg_12_15)
    Restart()


def CoffinExit():
    """ 11305000: Event 11305000 """
    DisableNetworkSync()
    IfSingleplayer(1)
    IfInsideMap(1, game_map=CATACOMBS)
    IfFlagOff(1, Flags.Exit2Disabled)
    IfCharacterInsideRegion(1, PLAYER, region=1302700)
    IfPlayerHasGood(1, 109, including_box=False)
    IfConditionTrue(0, input_condition=1)
    Wait(10.0)
    RestartIfMultiplayer()
    IfCharacterInsideRegion(6, PLAYER, region=1302700)
    RestartIfConditionFalse(6)
    IfHealthLessThanOrEqual(7, PLAYER, 0.0)
    RestartIfConditionTrue(7)
    EnableFlag(Flags.Exit2Activated)
    WaitFrames(1)
    EnableObjectActivation(1311300, obj_act_id=-1)
    ResetStandbyAnimationSettings(PLAYER)
    Restart()


@RestartOnRest
def Event11305001():
    """ 11305001: Event 11305001 """
    IfCharacterInsideRegion(1, PLAYER, region=1302700)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11305006)
    DisableObjectActivation(1301104, obj_act_id=3060)
    EnableObjectActivation(1301104, obj_act_id=3061)
    RestartEvent(11305002, slot=0)
    RestartEvent(11305009, slot=0)
    Restart()


@RestartOnRest
def Event11305002():
    """ 11305002: Event 11305002 """
    DisableNetworkSync()
    IfFlagOn(0, 11305006)
    DisableFlag(11305006)
    Wait(5.0)
    EnableFlag(11305008)
    Restart()


def Event11305003():
    """ 11305003: Event 11305003 """
    IfFlagOn(0, 11305008)
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    DisableFlag(11305006)
    DisableFlag(11305008)
    RestartEvent(11305000, slot=0)
    RestartEvent(11305001, slot=0)
    RestartEvent(11305002, slot=0)
    Restart()


@RestartOnRest
def Event11305004():
    """ 11305004: Event 11305004 """
    IfCharacterTargeting(1, 1300300, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 4130)
    IfConditionTrue(0, input_condition=1)
    ClearTargetList(1300300)
    ReplanAI(1300300)
    Restart()


def Event11305009():
    """ 11305009: Event 11305009 """
    IfAllPlayersOutsideRegion(1, region=1302700)
    IfEntityWithinDistance(1, 1301104, PLAYER, radius=10.0)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1301104, obj_act_id=3060)
    DisableObjectActivation(1301104, obj_act_id=3061)
    Restart()


def Event11300420(_, arg_0_3: int):
    """ 11300420: Event 11300420 """
    DisableNetworkSync()
    WaitFrames(1)
    IfEntityWithinDistance(1, 1301104, arg_0_3, radius=10.0)
    IfCharacterInsideRegion(1, arg_0_3, region=1302700)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7151, death_animation=6082)
    IfEntityWithinDistance(2, 1301104, arg_0_3, radius=10.0)
    IfCharacterOutsideRegion(2, arg_0_3, region=1302700)
    IfConditionTrue(0, input_condition=2)
    ResetStandbyAnimationSettings(arg_0_3)
    Restart()


def Event11300100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11300100: Event 11300100 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_8_11)
    End()
    IfFlagOff(1, arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    DestroyObject(arg_8_11, slot=1)
    CreateTemporaryVFX(130000, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=arg_12_15)


def Event11300150():
    """ 11300150: Event 11300150 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(1301020, slot=1)
    End()
    DisableAI(1300050)
    IfCharacterInsideRegion(0, PLAYER, region=1302020)
    EnableAI(1300050)
    DestroyObject(1301020, slot=1)
    PlaySoundEffect(anchor_entity=1301020, sound_type=SoundType.a_Ambient, sound_id=303600000)


def Event11300160():
    """ 11300160: Event 11300160 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1301050)
    End()
    IfObjectDestroyed(0, 1301050)
    EnableFlag(11300160)


def IllusoryWallInvincible():
    """ 11300161: Piercing Eye needed. """
    if FlagEnabled(11300160):
        return
    EnableObjectInvulnerability(1301050)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1301050)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


def RevealLadderAfterBoss():
    """ 11300200: Event 11300200 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1301040, 0)
    End()
    IfFlagOn(0, Flags.Boss1Dead)
    ForceAnimation(1301040, 0)


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11302080: All-in-one boss event for simplicity. """
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteVFX(fog_1_sfx, erase_root_only=False)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteVFX(fog_2_sfx, erase_root_only=False)

    if dead_flag:
        DisableCharacter(boss)
        if twin_enabled:
            DisableCharacter(boss_twin)
        return

    DisableCharacter(boss)
    if twin_enabled:
        DisableCharacter(boss_twin)

    Await(trigger_region)
    EnableFlag(CommonFlags.InBossBattle)

    EnableObject(fog_1_object)
    CreateVFX(fog_1_sfx)
    if fog_2_object != 0:
        EnableObject(fog_2_object)
        CreateVFX(fog_2_sfx)

    if twin_enabled:
        EnableCharacter(boss_twin)
        EnableInvincibility(boss_twin)
        ForceAnimation(boss_twin, 10)
    EnableCharacter(boss)
    EnableInvincibility(boss)
    ForceAnimation(boss, 10)
    if twin_enabled:
        SetTeamType(boss, TeamType.Enemy)
        SetTeamType(boss_twin, TeamType.Enemy)
    Wait(2.0)
    ResetAnimation(boss)
    ReplanAI(boss)
    if twin_enabled:
        ResetAnimation(boss_twin)
        ReplanAI(boss_twin)
    DisableInvincibility(boss)
    if twin_enabled:
        DisableInvincibility(boss_twin)

    EnableSoundEvent(music_id)
    EnableBossHealthBar(boss, boss_name, slot=0)
    if twin_enabled:
        EnableBossHealthBar(boss_twin, boss_twin_name, slot=1)

    Await(IsDead(boss) and (not twin_enabled or IsDead(boss_twin)))
    DisableFlag(CommonFlags.InBossBattle)

    EnableFlag(dead_flag)
    DisableBossHealthBar(boss, boss_name, slot=0)  # Will disable twin's bar automatically.
    DisableObject(fog_1_object)
    DeleteVFX(fog_1_sfx, erase_root_only=True)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteVFX(fog_2_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11312260: Invasion is triggered. Human not needed. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    IfHost(1)
    IfFlagOff(1, dead_flag)
    IfCharacterInsideRegion(1, PLAYER, region=trigger)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableCharacter(invader)
    ForceAnimation(invader, PlayerAnimations.SummonSpawn, wait_for_completion=True)
    ReplanAI(invader)
    SetTeamType(invader, TeamType.BlackPhantom)
    DisplayBattlefieldMessage(invasion_message, 0)

    # TODO: If player dies while invader is active (two possible outcomes here), give them a Black Eye Orb and register
    #  future possible vengeance invasion by checking that flag in the run manager.
    Await(IsDead(invader))

    DisplayBattlefieldMessage(dead_message, 0)
    EnableFlag(dead_flag)


def DepartLevelUnconditional(
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag,
        end_trigger_flag: Flag):
    """ 11302200: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlag(_, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
                      end_trigger_flag: Flag):
    """ 11302210: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11303000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11300600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11305810: Mimic is activated by the player. """
    IfHealthGreaterThan(1, mimic, 0.0)
    IfCharacterBackreadEnabled(1, mimic)
    IfCharacterHasSpecialEffect(1, mimic, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(1, prompt_text=10010400, anchor_entity=mimic, anchor_type=CoordEntityType.Character,
                   facing_angle=45.0, max_distance=1.2000000476837158, model_point=7,
                   trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=mimic, destination_type=CoordEntityType.Character, model_point=100,
         copy_draw_parent=mimic)
    ForceAnimation(PLAYER, 7521)
    AICommand(mimic, command_id=10, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def ControlMimicState(_, mimic: Character):
    """ 11305820: Mimic state control. """
    IfCharacterDoesNotHaveSpecialEffect(1, mimic, 5420)
    IfAttacked(1, mimic, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    IfCharacterBackreadDisabled(7, mimic)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, mimic, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, mimic, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, mimic, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, mimic, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(mimic, 3006, wait_for_completion=True)
    ReplanAI(mimic)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    Restart()


@RestartOnRest
def HitMimicWithTalisman(_, mimic: Character):
    """ 11305830: Mimic goes to sleep. """
    IfCharacterHasSpecialEffect(1, mimic, 5421)
    IfCharacterHasSpecialEffect(1, mimic, 3150)
    IfCharacterHasSpecialEffect(2, mimic, 5420)
    IfCharacterHasSpecialEffect(2, mimic, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(mimic, command_id=200, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(mimic, command_id=210, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, mimic, 5420)
    IfCharacterHasSpecialEffect(-2, mimic, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def TalismanWearsOffMimic(_, mimic: Character):
    """ 11305840: Mimic wakes up again. """
    IfCharacterHasSpecialEffect(1, mimic, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, mimic, 3150)
    IfCharacterHasSpecialEffect(2, mimic, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, mimic, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(mimic, command_id=201, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(mimic, command_id=211, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, mimic, 5420)
    IfCharacterHasSpecialEffect(-2, mimic, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def MimicReturnsToChest(_, mimic: Character, mimic_nest: Region):
    """ 11305850: Mimic enters chest form. """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, mimic, region=mimic_nest)
    IfCharacterBackreadDisabled(1, mimic)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(mimic, 5421)
    ClearTargetList(mimic)
    ReplanAI(mimic)
    Move(mimic, destination=mimic_nest, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, mimic)
    Restart()


@RestartOnRest
def ReplanMimicAIOnLoad(_, mimic: int):
    """ 11305860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11302270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11302999: Activate Abyss portal. """
    if CommonFlags.DisableAbyssPortal:
        DeleteVFX(fx_id, erase_root_only=False)
        return
    Await(ActionButton(
        CommonTexts.DelveIntoAbyss, portal, facing_angle=180.0, max_distance=2.0,
        anchor_type=CoordEntityType.Character))

    DisableFlag(CommonFlags.AbyssBattleRequestComplete)
    EnableFlag(CommonFlags.AbyssBattleRequest)
    # Wait for mod to generate Abyss map.
    Await(CommonFlags.AbyssBattleRequestComplete)
    EnableFlag(CommonFlags.DisableAbyssPortal)
    EnableFlag(CommonFlags.AbyssBattleActive)
    WarpToMap(NEW_LONDO_RUINS, 1600243)


def RegisterBoss2Ladder():
    """ 11300450: Register upper ladder only after boss 2 is dead.

    TODO: No requirement at the moment (boss not operational).
    """
    # Await(Flags.Boss2Dead)
    RegisterLadder(start_climbing_flag=11300026, stop_climbing_flag=11300027, obj=1301148)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11302950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11302960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
