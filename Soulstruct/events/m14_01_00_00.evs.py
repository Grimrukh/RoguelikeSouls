"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .izalith_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(  # Centipede Demon arena
        0,
        Chrs.RuinsBoss1, Chrs.RuinsBoss1Twin, Flags.RuinsBoss1IsTwin,
        Regions.RuinsBoss1Trigger, Flags.RuinsBoss1Dead, 1413802,  # Music ID changed to Ceaseless.
        ItemLots.RuinsBoss1Reward,
        1411890, 1411891, 0, 0,  # Exit fog is permanent (prompt).
        1000, 1000,
    )

    # TODO: Repair boss fight here. Auto-killed until then (for departure up top).
    EnableFlag(Flags.RuinsBoss2Dead)
    # BossBattle(  # Ceaseless Discharge arena
    #     1,
    #     Chrs.RuinsBoss2, Chrs.RuinsBoss2Twin, Flags.RuinsBoss2IsTwin,
    #     Regions.RuinsBoss2Trigger, Flags.RuinsBoss2Dead, 1413801,
    #     ItemLots.RuinsBoss2Reward,
    #     1411790, 1411791, 1411792, 1411793,  # Double entrance fog.
    #     1000, 1000,
    # )

    RegisterBonfire(11410992, obj=1411960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)

    # DisableObject(1411994)  # Repurposed as Ruins exit prompt.
    # DeleteFX(1411995, erase_root_only=False)
    DisableObject(1411996)
    DeleteFX(1411997, erase_root_only=False)
    DisableObject(1411998)
    DeleteFX(1411999, erase_root_only=False)
    DisableObject(1411988)
    DeleteFX(1411989, erase_root_only=False)
    # DisableObject(1411986)  # Repurposed as Izalith exit prompt.
    # DeleteFX(1411987, erase_root_only=False)
    DisableObject(1411984)
    DeleteFX(1411985, erase_root_only=False)
    DisableObject(1411982)
    DeleteFX(1411983, erase_root_only=False)

    # Bed of Chaos orbs (now always destroyed).
    EnableFlag(11410291)
    EnableFlag(11410292)
    SkipLinesIfFlagOff(3, 11410291)
    DisableObject(1411121)
    DeleteFX(1413400, erase_root_only=True)
    DeleteFX(1413410, erase_root_only=True)
    SkipLinesIfFlagOff(3, 11410292)
    DisableObject(1411122)
    DeleteFX(1413401, erase_root_only=True)
    DeleteFX(1413411, erase_root_only=True)

    # Golden fog gone.
    DisableObject(1411710)
    DeleteFX(1411711, erase_root_only=False)
    DisableFlag(402)  # Invasions allowed (theoretically).

    # Ceaseless and Firesage fogs gone.
    DisableObject(1411790)
    DeleteFX(1411791, erase_root_only=False)
    DisableObject(1411410)
    DeleteFX(1411411, erase_root_only=False)
    DisableObject(1411412)
    DeleteFX(1411413, erase_root_only=False)

    # Lava drained.
    DisableObject(1411100)
    DisableCollision(1413100)
    DisableSoundEvent(1413805)

    # Bring elevator down.
    EndOfAnimation(1411400, 0)

    SewerCeilingBreaks()
    BreakIllusoryWall()
    IllusoryWallInvincible()
    SlideInvincibility()

    # Bed of Chaos stuff.
    RunEvent(11410260)
    BedOfChaosCentralFloorBreaks()  # Now requires main boss to be dead.
    RunEvent(11410201, slot=0, args=(1411210, 462000000))
    RunEvent(11410201, slot=1, args=(1411211, 462100000))
    RunEvent(11410201, slot=2, args=(1411212, 462200000))
    RunEvent(11410201, slot=3, args=(1411213, 462300000))
    RunEvent(11410201, slot=4, args=(1411214, 462400000))
    RunEvent(11410201, slot=5, args=(1411215, 462500000))
    RunEvent(11410201, slot=6, args=(1411216, 462600000))
    RunEvent(11410201, slot=7, args=(1411217, 462700000))
    RunEvent(11410201, slot=8, args=(1411218, 462800000))
    RunEvent(11410201, slot=9, args=(1411219, 462900000))
    RunEvent(11410201, slot=10, args=(1411220, 463000000))
    RunEvent(11410201, slot=11, args=(1411221, 463100000))
    RunEvent(11410201, slot=12, args=(1411222, 463200000))
    RunEvent(11410250)  # Roots invulnerable until orbs destroyed.

    # Rescue Quelana.
    RescueQuelana()

    # Unused boss music boxes (Ceaseless and Firesage).
    DisableSoundEvent(1413801)
    DisableSoundEvent(1413803)

    # Izalith boss battle handled with original Bed of Chaos events (but no entrance fog).
    DisableObject(1411990)
    DeleteFX(1411991, erase_root_only=False)
    DisableSoundEvent(1413800)
    if Flags.IzalithBoss1Dead:
        RunEvent(11415392, slot=0, args=(1001,), arg_types="h")
    else:
        RunEvent(11415393)
        RunEvent(11415392, slot=0, args=(1001,), arg_types="h")
        BedOfChaosDeath()  # Enables exit bonfire.
        RunEvent(11415394)
        RunEvent(11415395)
        RunEvent(11415396)
        RunEvent(11415397)
        RunEvent(11415398)
        RunEvent(11415300)

    # Chests.
    OpenChest(0, 1411650, 11410600)
    OpenChest(1, 1411651, 11410601)
    OpenChest(2, 1411652, 11410602)
    OpenChest(3, 1411653, 11410603)
    OpenChest(4, 1411653, 11410604)

    # Mimics
    OpenMimic(0, Chrs.RuinsMimic)
    ControlMimicState(0, Chrs.RuinsMimic)
    HitMimicWithTalisman(0, Chrs.RuinsMimic)
    TalismanWearsOffMimic(0, Chrs.RuinsMimic)
    MimicReturnsToChest(0, Chrs.RuinsMimic, Regions.RuinsMimicNest)
    ReplanMimicAIOnLoad(0, Chrs.RuinsMimic)

    OpenMimic(1, Chrs.IzalithMimic)
    ControlMimicState(1, Chrs.IzalithMimic)
    HitMimicWithTalisman(1, Chrs.IzalithMimic)
    TalismanWearsOffMimic(1, Chrs.IzalithMimic)
    MimicReturnsToChest(1, Chrs.IzalithMimic, Regions.IzalithMimicNest)
    ReplanMimicAIOnLoad(1, Chrs.IzalithMimic)

    # Despawn rare/red phantom enemies.
    for enemy in range(100):
        DespawnEnemy(enemy, 1410100 + enemy)
    for enemy in range(100):
        DespawnEnemy(100 + enemy, 1410400 + enemy)

    DepartLevelIfFlagWithFailure_Object(
        0, Objects.RuinsExit1Prompt, CommonTexts.DepartLevel, CommonTexts.DemonicMagicBlocks,
        Flags.RuinsExit1Disabled, Flags.RuinsBoss2Dead, Flags.RuinsExit1Activated)
    DepartLevelWithKey_Region(0, Regions.RuinsExit2Prompt, CommonTexts.DepartLevel, CommonTexts.HolySigilRequired,
                              Flags.RuinsExit2Disabled, CommonGoods.HolySigil, Flags.RuinsExit2Activated)  # Elevator
    DepartLevelIfFlag(0, Objects.RuinsExit3Prompt, CommonTexts.DepartLevel, Flags.RuinsExit3Disabled,
                      Flags.RuinsBoss1Dead, Flags.RuinsExit3Activated)  # After Centipede boss
    DepartLevelWithKey_Region(
        1, Regions.RuinsExit4Prompt, CommonTexts.DepartLevel, CommonTexts.GiantKeyRequired,
        Flags.RuinsExit4Disabled, CommonGoods.GiantKey, Flags.RuinsExit4Activated)  # Shortcut door

    DepartLevelWithKey(0, Objects.IzalithExit1Prompt, CommonTexts.DepartLevel, CommonTexts.GiantKeyRequired,
                       Flags.IzalithExit1Disabled, CommonGoods.GiantKey, Flags.IzalithExit1Activated)  # Shortcut door
    DepartLevelUnconditional(1, Objects.IzalithExit2Prompt, CommonTexts.DepartLevel, Flags.IzalithExit2Disabled,
                             Flags.IzalithExit2Activated)  # Lava dome exit (to Centipede)
    ActivateExitBonfire()

    ActivateAbyssPortal(0, 1410997, 1410998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, 6990, 6991, Chrs.RuinsInvader, Regions.RuinsInvaderTrigger, Flags.RuinsInvaderDead)
    InvaderTrigger(1, 6990, 6991, Chrs.IzalithInvader, Regions.IzalithInvaderTrigger, Flags.IzalithInvaderDead)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


def Event11415390():
    """ 11415390: Event 11415390 """
    IfFlagOff(1, Flags.IzalithBoss1Dead)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1412998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1411990,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1412997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11415393():
    """ 11415393: Event 11415393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, Flags.IzalithBoss1Dead)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    # ActivateMultiplayerBuffs(1410800)


@RestartOnRest
def Event11415392(_, boss_name: short):
    """ 11415392: Event 11415392 """
    if Flags.IzalithBoss1Dead:
        DisableCharacter(1410800)
        DisableCharacter(1410801)
        DisableCharacter(1410802)
        DisableCharacter(Chrs.IzalithBoss1)  # not killed
        Kill(1410800, award_souls=False)
        Kill(1410801, award_souls=False)
        Kill(1410802, award_souls=False)
        return
    SkipLinesIfFlagRangeAnyOn(1, (11410291, 11410292))
    DisableCharacter(1410800)
    SkipLinesIfFlagRangeAllOff(1, (11410291, 11410292))
    ResetStandbyAnimationSettings(1410801)
    EnableInvincibility(1410800)
    EnableInvincibility(1410801)
    DisableHealthBar(1410800)
    DisableHealthBar(1410801)
    DisableHealthBar(Chrs.IzalithBoss1)
    DisableAI(1410801)
    DisableAI(Chrs.IzalithBoss1)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=1)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagRangeAnyOn(2, (11410291, 11410292))
    ResetStandbyAnimationSettings(1410801)
    ForceAnimation(1410801, 9060)
    EnableAI(1410801)
    EnableAI(Chrs.IzalithBoss1)
    EnableBossHealthBar(1410802, name=5400, slot=0)
    EnableBossHealthBar(Chrs.IzalithBoss1, name=boss_name, slot=1)  # TODO: Too hard to inject name.


def BedOfChaosDeath():
    """ 11410001: Event 11410001 """
    # This event only runs if Bed is still alive.
    IfCharacterDead(0, 1410802)
    EnableFlag(Flags.IzalithBoss1Dead)
    DisplayBanner(BannerType.VictoryAchieved)
    PlaySoundEffect(PLAYER, SoundType.s_SFX, 777777777)
    DisableBossHealthBar(1410802, name=5400, slot=0)
    SetLockedCameraSlot(game_map=LOST_IZALITH, camera_slot=0)
    DisableObject(1411990)
    DeleteFX(1411991, erase_root_only=True)
    DisableNetworkSync()


def ActivateExitBonfire():
    """ 11412240: Exit bonfire appears and can be activated. """
    if not Flags.IzalithBoss1Dead:
        DisableObject(Objects.IzalithExit3Prompt)
        CreateTemporaryFX(90014, anchor_entity=Objects.IzalithExit3Prompt, anchor_type=CoordEntityType.Object,
                          model_point=-1)
        Await(Flags.IzalithBoss1Dead)
        Wait(4.0)
        EnableObject(Objects.IzalithExit3Prompt)
        if not CommonFlags.IzalithBossDefeated:
            if CommonFlags.LordvesselObtained:
                DisplayStatus(CommonTexts.MoreTreasureUnlocked)
                EnableFlag(CommonFlags.IzalithBossDefeated)
            else:
                DisplayStatus(CommonTexts.LordvesselNotObtained)

    Wait(2.0)
    EnableObject(Objects.IzalithExit3Prompt)

    # TODO: End disable flag is being accidentally enabled somewhere, when it's not even possible. Removing for now.

    if FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 3) or CommonFlags.KilnAvailable:
        # Go to Chasm or Kiln (mod will figure out which).
        Await(ActionButton(
            CommonTexts.DepartLevel, Objects.IzalithExit3Prompt, max_distance=2.0))
        EnableFlag(Flags.IzalithExit3Activated)
    else:
        # Go back to Firelink.
        Await(ActionButton(
            CommonTexts.ReturnToFirelink, Objects.IzalithExit3Prompt, max_distance=2.0))
        AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


def Event11415394():
    """ 11415394: Event 11415394 """
    DisableNetworkSync()
    IfFlagOff(1, Flags.IzalithBoss1Dead)
    IfFlagOn(1, 11415392)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11415391)
    IfCharacterInsideRegion(1, PLAYER, region=1412990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1413800)


def Event11415395():
    """ 11415395: Event 11415395 """
    DisableNetworkSync()
    IfFlagOn(1, Flags.IzalithBoss1Dead)
    IfFlagOn(1, 11415394)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1413800)


@RestartOnRest
def Event11415396():
    """ 11415396: Bed of Chaos orb destruction (now always destroyed, no cutscenes). """
    EnableCharacter(1410800)
    AddSpecialEffect(1410800, 5130)
    EnableFlag(11410000)
    ResetStandbyAnimationSettings(1410800)
    WaitFrames(1)
    ResetAnimation(1410800, disable_interpolation=True)


@RestartOnRest
def Event11415397():
    """ 11415397: Event 11415397 """
    EnableInvincibility(1410802)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableInvincibility(1410802)
    IfHealthLessThanOrEqual(0, 1410802, 0.0)
    DisableInvincibility(1410800)
    DisableInvincibility(1410801)
    Kill(1410800, award_souls=True)
    Kill(1410801, award_souls=False)


@RestartOnRest
def Event11415398():
    """ 11415398: Event 11415398 """
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=2, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=2, slot=0)
    ReplanAI(1410801)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    SkipLinesIfFlagOn(1, 11410000)
    IfFlagOn(1, 11415396)
    IfConditionTrue(0, input_condition=1)
    IfCharacterBackreadEnabled(0, 1410800)
    AICommand(1410800, command_id=3, slot=0)
    ReplanAI(1410800)
    AICommand(1410801, command_id=3, slot=0)
    ReplanAI(1410801)


def SlideInvincibility():
    """ 11415399: Event 11415399 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1412110)
    EnableInvincibility(PLAYER)
    IfCharacterOutsideRegion(0, PLAYER, region=1412110)
    Wait(3.0)
    DisableInvincibility(PLAYER)


def Event11415300():
    """ 11415300: Event 11415300 """
    EndIfFlagOn(Flags.IzalithBoss1Dead)
    SkipLinesIfThisEventOn(2)
    EnableFlag(11415300)
    EnableObjectInvulnerability(1411120)
    IfFlagOff(1, 11410291)
    IfObjectDestroyed(1, 1411121)
    IfFlagOff(2, 11410292)
    IfObjectDestroyed(2, 1411122)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfFlagOn(-1, Flags.IzalithBoss1Dead)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(Flags.IzalithBoss1Dead)
    SkipLinesIfFinishedConditionFalse(4, 1)
    EnableFlag(11410291)
    DeleteFX(1413400, erase_root_only=True)
    DeleteFX(1413410, erase_root_only=True)
    Restart()
    EnableFlag(11410292)
    DeleteFX(1413401, erase_root_only=True)
    DeleteFX(1413411, erase_root_only=True)
    Restart()


def BedOfChaosCentralFloorBreaks():
    """ 11410200: Event 11410200 """
    if THIS_FLAG:
        DisableObject(1411200)
        DisableObject(1411201)
        DisableObject(1411202)
        DisableObject(1411203)
        DisableObject(1411204)
        return
    RestoreObject(1411200)
    RestoreObject(1411201)
    RestoreObject(1411202)
    RestoreObject(1411203)
    RestoreObject(1411204)
    EnableObjectInvulnerability(1411200)
    EnableObjectInvulnerability(1411201)
    EnableObjectInvulnerability(1411202)
    EnableObjectInvulnerability(1411203)
    EnableObjectInvulnerability(1411204)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfCharacterInsideRegion(1, PLAYER, region=1412100)
    IfCharacterDead(1, Chrs.IzalithBoss1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11410200)
    DisableObjectInvulnerability(1411200)
    DisableObjectInvulnerability(1411201)
    DisableObjectInvulnerability(1411202)
    DisableObjectInvulnerability(1411203)
    DisableObjectInvulnerability(1411204)
    CreateTemporaryFX(140009, anchor_entity=1411202, anchor_type=CoordEntityType.Object, model_point=-1)
    DestroyObject(1411200, slot=1)
    PlaySoundEffect(anchor_entity=1411200, sound_type=SoundType.o_Object, sound_id=463300000)
    WaitFrames(4)
    DestroyObject(1411201, slot=1)
    PlaySoundEffect(anchor_entity=1411201, sound_type=SoundType.o_Object, sound_id=463400000)
    WaitFrames(3)
    DestroyObject(1411202, slot=1)
    PlaySoundEffect(anchor_entity=1411202, sound_type=SoundType.o_Object, sound_id=463500000)
    WaitFrames(2)
    DestroyObject(1411203, slot=1)
    PlaySoundEffect(anchor_entity=1411203, sound_type=SoundType.o_Object, sound_id=463600000)
    WaitFrames(1)
    DestroyObject(1411204, slot=1)
    PlaySoundEffect(anchor_entity=1411204, sound_type=SoundType.o_Object, sound_id=463700000)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(1411200)
    DisableObject(1411203)
    DisableObject(1411204)


def Event11410201(_, arg_0_3: int, arg_4_7: int):
    """ 11410201: Event 11410201 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    RestoreObject(arg_0_3)
    EnableObjectInvulnerability(arg_0_3)
    IfFlagOn(-1, 11410291)
    IfFlagOn(-1, 11410292)
    IfConditionTrue(0, input_condition=-1)
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=8.0)
    DisableObjectInvulnerability(arg_0_3)
    DestroyObject(arg_0_3, slot=1)
    CreateTemporaryFX(140008, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=arg_4_7)
    DisableNetworkSync()
    Wait(10.0)
    DisableObject(arg_0_3)


def Event11410250():
    """ 11410250: Event 11410250 """
    EndIfFlagRangeAllOn((11410291, 11410292))
    EnableObjectInvulnerability(1411250)
    EnableObjectInvulnerability(1411251)
    EnableObjectInvulnerability(1411252)
    EnableObjectInvulnerability(1411253)
    EnableObjectInvulnerability(1411254)
    EnableObjectInvulnerability(1411255)
    EnableObjectInvulnerability(1411256)
    EnableObjectInvulnerability(1411257)
    EnableObjectInvulnerability(1411258)
    EnableObjectInvulnerability(1411259)
    EnableObjectInvulnerability(1411260)
    EnableObjectInvulnerability(1411261)
    EnableObjectInvulnerability(1411262)
    EnableObjectInvulnerability(1411263)
    EnableObjectInvulnerability(1411264)
    EnableObjectInvulnerability(1411265)
    EnableObjectInvulnerability(1411266)
    EnableObjectInvulnerability(1411267)
    EnableObjectInvulnerability(1411268)
    EnableObjectInvulnerability(1411269)
    EnableObjectInvulnerability(1411270)
    EnableObjectInvulnerability(1411271)
    EnableObjectInvulnerability(1411272)
    EnableObjectInvulnerability(1411273)
    EnableObjectInvulnerability(1411274)
    EnableObjectInvulnerability(1411275)
    EnableObjectInvulnerability(1411276)
    EnableObjectInvulnerability(1411277)
    EnableObjectInvulnerability(1411278)
    EnableObjectInvulnerability(1411279)
    EnableObjectInvulnerability(1411280)
    EnableObjectInvulnerability(1411281)
    EnableObjectInvulnerability(1411282)
    EnableObjectInvulnerability(1411283)
    EnableObjectInvulnerability(1411284)
    EnableObjectInvulnerability(1411285)
    EnableObjectInvulnerability(1411286)
    EnableObjectInvulnerability(1411287)
    EnableObjectInvulnerability(1411288)
    EnableObjectInvulnerability(1411289)
    EnableObjectInvulnerability(1411290)
    EnableObjectInvulnerability(1411291)
    EnableObjectInvulnerability(1411292)
    EnableObjectInvulnerability(1411293)
    EnableObjectInvulnerability(1411294)
    EnableObjectInvulnerability(1411295)
    EnableObjectInvulnerability(1411296)
    EnableObjectInvulnerability(1411297)
    IfFlagOn(1, 11410291)
    IfFlagOn(1, 11410292)
    IfConditionTrue(0, input_condition=1)
    DisableObjectInvulnerability(1411250)
    DisableObjectInvulnerability(1411251)
    DisableObjectInvulnerability(1411252)
    DisableObjectInvulnerability(1411253)
    DisableObjectInvulnerability(1411254)
    DisableObjectInvulnerability(1411255)
    DisableObjectInvulnerability(1411256)
    DisableObjectInvulnerability(1411257)
    DisableObjectInvulnerability(1411258)
    DisableObjectInvulnerability(1411259)
    DisableObjectInvulnerability(1411260)
    DisableObjectInvulnerability(1411261)
    DisableObjectInvulnerability(1411262)
    DisableObjectInvulnerability(1411263)
    DisableObjectInvulnerability(1411264)
    DisableObjectInvulnerability(1411265)
    DisableObjectInvulnerability(1411266)
    DisableObjectInvulnerability(1411267)
    DisableObjectInvulnerability(1411268)
    DisableObjectInvulnerability(1411269)
    DisableObjectInvulnerability(1411270)
    DisableObjectInvulnerability(1411271)
    DisableObjectInvulnerability(1411272)
    DisableObjectInvulnerability(1411273)
    DisableObjectInvulnerability(1411274)
    DisableObjectInvulnerability(1411275)
    DisableObjectInvulnerability(1411276)
    DisableObjectInvulnerability(1411277)
    DisableObjectInvulnerability(1411278)
    DisableObjectInvulnerability(1411279)
    DisableObjectInvulnerability(1411280)
    DisableObjectInvulnerability(1411281)
    DisableObjectInvulnerability(1411282)
    DisableObjectInvulnerability(1411283)
    DisableObjectInvulnerability(1411284)
    DisableObjectInvulnerability(1411285)
    DisableObjectInvulnerability(1411286)
    DisableObjectInvulnerability(1411287)
    DisableObjectInvulnerability(1411288)
    DisableObjectInvulnerability(1411289)
    DisableObjectInvulnerability(1411290)
    DisableObjectInvulnerability(1411291)
    DisableObjectInvulnerability(1411292)
    DisableObjectInvulnerability(1411293)
    DisableObjectInvulnerability(1411294)
    DisableObjectInvulnerability(1411295)
    DisableObjectInvulnerability(1411296)
    DisableObjectInvulnerability(1411297)


def BreakIllusoryWall():
    """ 11410360: Event 11410360 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1411360)
    End()
    IfObjectDestroyed(0, 1411360)
    EnableFlag(11410360)


def IllusoryWallInvincible():
    """ 11410361: Piercing Eye needed. """
    if FlagEnabled(11410360):
        return
    EnableObjectInvulnerability(1411360)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1411360)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


def Event11410402():
    """ 11410402: Event 11410402 """
    DisableNetworkSync()
    IfFlagOff(-2, 11410410)
    IfMultiplayer(-2)
    IfConditionTrue(1, input_condition=-2)
    IfActionButton(1, prompt_text=10010510, anchor_entity=1411400, anchor_type=CoordEntityType.Object,
                   facing_angle=180.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010170, anchor_entity=1411400, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    Restart()


@RestartOnRest
def Event11415200():
    """ 11415200: Event 11415200 """
    RunEvent(11415201, slot=0, args=(1410500, 1, 3290, 3290, 11415201), arg_types='ihhii')
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 0, 1), arg_types='iiBB')
    RunEvent(5200, slot=-1, args=(1410500, 11415201, 2, 3), arg_types='iiBB')
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411500, 1411501, 120, 123), arg_types='iiiihh')
    RunEvent(5201, slot=-1, args=(1410500, 11415201, 1411502, 1411503, 126, 129), arg_types='iiiihh')
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410550, 1410551, 120, 123))
    RunEvent(5202, slot=-1, args=(1410500, 11415201, 1410552, 1410553, 126, 129))
    RunEvent(11415201, slot=1, args=(1410500, 2, 3291, 3291, 11415202), arg_types='ihhii')
    RunEvent(5200, slot=-1, args=(1410500, 11415202, 5, 11), arg_types='iiBB')
    RunEvent(5201, slot=-1, args=(1410500, 11415202, 1411504, 1411505, 135, 137), arg_types='iiiihh')
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410554, 1410555, 135, 137))
    RunEvent(5202, slot=-1, args=(1410500, 11415202, 1410556, 1410557, 153, 155))
    RunEvent(11415201, slot=2, args=(1410500, 3, 3292, 3292, 11415203), arg_types='ihhii')
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 6, 7), arg_types='iiBB')
    RunEvent(5200, slot=-1, args=(1410500, 11415203, 8, 10), arg_types='iiBB')
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411506, 1411507, 138, 141), arg_types='iiiihh')
    RunEvent(5201, slot=-1, args=(1410500, 11415203, 1411508, 1411509, 144, 150), arg_types='iiiihh')
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410558, 1410559, 138, 141))
    RunEvent(5202, slot=-1, args=(1410500, 11415203, 1410560, 1410561, 144, 150))
    RunEvent(11415201, slot=3, args=(1410500, 4, 3293, 3293, 11415204), arg_types='ihhii')
    RunEvent(5200, slot=-1, args=(1410500, 11415204, 4, 9), arg_types='iiBB')
    RunEvent(5201, slot=-1, args=(1410500, 11415204, 1411510, 1411511, 132, 134), arg_types='iiiihh')
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410562, 1410563, 132, 134))
    RunEvent(5202, slot=-1, args=(1410500, 11415204, 1410564, 1410565, 150, 152))


@UnknownRestart
def Event11415201(_, arg_0_3: int, arg_4_5: short, arg_6_7: short, arg_8_11: int, arg_12_15: int):
    """ 11415201: Event 11415201 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(arg_0_3, npc_part_id=arg_6_7, part_index=arg_4_5, part_health=100, damage_correction=1.0,
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(0, arg_0_3, npc_part_id=arg_8_11, value=0)
    DisableFlag(11415290)
    DisableFlag(11415291)
    SkipLinesIfClient(1)
    EnableRandomFlagInRange((11415290, 11415291))
    EnableFlag(arg_12_15)
    SkipLinesIfFlagOff(2, 11415290)
    ForceAnimation(arg_0_3, 8000)
    SkipLines(1)
    ForceAnimation(arg_0_3, 8010)


@UnknownRestart
def Event5200(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 5200: Event 5200 """
    SkipLinesIfFlagOn(6, arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SetDisplayMask(arg_0_3, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=arg_9_9, switch_type=OnOffChange.On)


@UnknownRestart
def Event5201(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_17: short, arg_18_19: short):
    """ 5201: Event 5201 """
    DisableObject(arg_8_11)
    DisableObject(arg_12_15)
    EndIfFlagOn(arg_4_7)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableObject(arg_8_11)
    EnableObject(arg_12_15)
    MoveObjectToCharacter(arg_8_11, character=arg_0_3, model_point=arg_16_17)
    MoveObjectToCharacter(arg_12_15, character=arg_0_3, model_point=arg_18_19)
    DestroyObject(arg_8_11, slot=1)
    DestroyObject(arg_12_15, slot=1)


@UnknownRestart
def Event5202(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 5202: Event 5202 """
    EndIfFlagOn(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableCharacter(arg_12_15)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    Move(arg_8_11, destination=arg_0_3, destination_type=CoordEntityType.Character, model_point=arg_16_19,
         copy_draw_parent=arg_0_3)
    Move(arg_12_15, destination=arg_0_3, destination_type=CoordEntityType.Character, model_point=arg_20_23,
         copy_draw_parent=arg_0_3)
    EnableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    ForceAnimation(arg_8_11, 7000)
    ForceAnimation(arg_12_15, 7000)


def SewerCeilingBreaks():
    """ 11410350: Event 11410350 """
    SkipLinesIfThisEventOff(5)
    DisableObject(1411350)
    PostDestruction(1411351, slot=1)
    EndOfAnimation(1411600, 116)
    EnableTreasure(1411600)
    End()
    DisableObject(1411351)
    DisableTreasure(1411600)
    CreateObjectFX(99010, obj=1411600, model_point=90)
    ForceAnimation(1411600, 115, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=1412350)
    IfObjectDestroyed(-1, 1411350)
    IfConditionTrue(0, input_condition=-1)
    DisableObject(1411350)
    EnableObject(1411351)
    CreateTemporaryFX(140001, anchor_entity=1411351, anchor_type=CoordEntityType.Object, model_point=-1)
    PlaySoundEffect(anchor_entity=1411351, sound_type=SoundType.o_Object, sound_id=481000001)
    DestroyObject(1411351, slot=1)
    ForceAnimation(1411600, 116, wait_for_completion=True)
    EnableTreasure(1411600)
    DeleteObjectFX(1411600, erase_root=True)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11410600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11410260():
    """ 11410260: Event 11410260 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfTimeElapsed(1, 3.0)
    IfConditionTrue(0, input_condition=1)
    ActivateKillplaneForModel(game_map=LOST_IZALITH, y_threshold=-400.0, target_model_id=3240)
    Restart()


def Event11410510(_, arg_0_3: int, arg_4_7: int):
    """ 11410510: Event 11410510 """
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11410520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410520: Event 11410520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410501(_, arg_0_3: int, arg_4_7: int):
    """ 11410501: Event 11410501 """
    IfFlagOn(-2, 1503)
    IfFlagOn(-2, 1505)
    IfFlagOn(-2, 1506)
    IfFlagOn(-2, 1507)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventSlotOn(2)
    IfFlagOn(3, arg_4_7)
    IfThisEventSlotOff(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 3)
    DisableCharacter(arg_0_3)
    IfFlagOn(0, 703)
    EnableFlag(arg_4_7)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11410530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410530: Event 11410530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfFlagOn(1, 11410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11410531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410531: Event 11410531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOff(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    EnableCharacter(6004)
    SetTeamTypeAndExitStandbyAnimation(6004, TeamType.HostileAlly)
    SaveRequest()


def Event11410532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410532: Event 11410532 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1009)
    IfFlagOn(1, 800)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412510)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1412500, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1413000)
    EnableFlag(11410580)
    IfCharacterBackreadEnabled(0, arg_0_3)
    SetNest(arg_0_3, 1412500)


def Event11410533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410533: Event 11410533 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1003)
    IfFlagOn(1, 11410595)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1004)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11410534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410534: Event 11410534 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1002)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410540: Event 11410540 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1502)
    IfFlagOn(1, 11400590)
    IfInsideMap(1, game_map=LOST_IZALITH)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(814)


def Event11410541(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410541: Event 11410541 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterAlive(-1, 1410410)
    IfCharacterAlive(-1, 1410411)
    IfCharacterAlive(-1, 1410412)
    IfCharacterAlive(-1, 1410413)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 11410590)
    IfFlagOff(2, 1512)
    IfFlagOn(2, 1504)
    IfThisEventOn(2)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.FightingAlly)
    AddSpecialEffect(arg_0_3, 90111)


def Event11410542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410542: Event 11410542 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1503)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410543(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410543: Event 11410543 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthLessThan(1, arg_0_3, 0.5)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, 1412360)


def Event11410544(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410544: Event 11410544 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1504)
    IfHealthGreaterThanOrEqual(1, arg_0_3, 0.5)
    IfCharacterDead(1, 1410410)
    IfCharacterDead(1, 1410411)
    IfCharacterDead(1, 1410412)
    IfCharacterDead(1, 1410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SetNest(arg_0_3, 1412360)


def Event11410545(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410545: Event 11410545 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1506)
    IfFlagOn(1, 11410591)
    IfThisEventOff(1)
    IfFlagOff(2, 1512)
    IfFlagOn(2, arg_12_15)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionTrue(3, 2)
    Kill(arg_0_3, award_souls=True)
    CancelSpecialEffect(arg_0_3, 90111)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11410546(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410546: Event 11410546 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfFlagOff(1, 1506)
    IfFlagOff(1, 1508)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11410547(_, arg_0_3: int):
    """ 11410547: Event 11410547 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(3)
    SkipLinesIfFlagOn(1, 11410593)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfThisEventOn(-1)
    IfFlagOn(-1, 1503)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfThisEventOn(1)
    IfFlagOff(0, 814)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=7856)


def Event11410548(_, arg_0_3: int):
    """ 11410548: Event 11410548 """
    EndIfFlagOn(1512)
    SkipLinesIfThisEventSlotOff(2)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)
    End()
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410593)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7855)


def Event11410549(_, arg_0_3: int):
    """ 11410549: Event 11410549 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1507)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableCharacter(arg_0_3)


def Event11410550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11410550: Event 11410550 """
    IfHost(1)
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1505)
    IfFlagOn(1, 11410594)
    SkipLinesIfThisEventOn(1)
    IfCharacterBackreadDisabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11415030():
    """ 11415030: Event 11415030 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6542, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6542)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, 6542)
    IfEntityWithinDistance(1, 6542, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6542, region=1412000, summon_flag=11415031, dismissal_flag=11415033)


def Event11415029():
    """ 11415029: Event 11415029 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6542, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11415033)
    IfClient(2)
    IfFlagOn(2, 11415031)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6542)
    EndIfFlagOn(10)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11415031)
    IfFlagOff(1, 11415033)
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1007)
    IfCharacterBackreadEnabled(1, 6542)
    IfEntityWithinDistance(1, 6542, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6542, region=1412000, summon_flag=11415031, dismissal_flag=11415033)


def Event14015990(_, arg_0_3: int, arg_4_7: int):
    """ 14015990: Event 14015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def Event11415032():
    """ 11415032: Event 11415032 """
    EndIfThisEventOn()
    IfFlagOn(1, 11415031)
    IfFlagOn(1, 11415383)
    IfConditionTrue(0, input_condition=1)
    AICommand(6542, command_id=10, slot=0)
    ReplanAI(6542)
    IfCharacterInsideRegion(0, 6542, region=1412898)
    RotateToFaceEntity(6542, 1412897)
    ForceAnimation(6542, 7410)
    AICommand(6542, command_id=-1, slot=0)
    ReplanAI(6542)


def Event11415035():
    """ 11415035: Event 11415035 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415036)
    EndIfFlagOn(11410410)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410810)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412010)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6560, region=1412001, summon_flag=11415036, dismissal_flag=11415037)
    Wait(20.0)
    Restart()


def Event11415038():
    """ 11415038: Event 11415038 """
    DisableNetworkSync()
    EndIfClient()
    EndIfFlagOn(11415039)
    EndIfFlagOn(10)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11410811)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=1412520)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, 6561, region=1412002, summon_flag=11415039, dismissal_flag=11415040)
    Wait(20.0)
    Restart()


def Event11410810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11410810: Event 11410810 """
    SkipLinesIfHost(3)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_8_11)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_0_3)
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11412080: All-in-one boss event for simplicity. """
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteFX(fog_1_sfx, erase_root_only=False)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteFX(fog_2_sfx, erase_root_only=False)

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
    CreateFX(fog_1_sfx)
    if fog_2_object != 0:
        EnableObject(fog_2_object)
        CreateFX(fog_2_sfx)

    # Note that this event activates lava immunity.
    if twin_enabled:
        EnableCharacter(boss_twin)
        EnableInvincibility(boss_twin)
        AddSpecialEffect(boss_twin, 5152)
        ForceAnimation(boss_twin, 10)
    EnableCharacter(boss)
    EnableInvincibility(boss)
    AddSpecialEffect(boss, 5152)
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
    DeleteFX(fog_1_sfx, erase_root_only=True)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteFX(fog_2_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11412260: Invasion is triggered. Human not needed. """
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
    """ 11412200: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlag(
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
        end_trigger_flag: Flag):
    """ 11412210: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelWithKey(
        _, prompt_object: Object, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
        key: GoodParam, end_trigger_flag: Flag):
    """ 11412220: Depart level by interacting with prompt with key in inventory. """
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0), hold=True)
    Await(activate_with_key or activate_without_key)
    if activate_with_key:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def DepartLevelWithKey_Region(
        _, prompt_region: Region, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
        key: GoodParam, end_trigger_flag: Flag):
    """ 11412230: Depart level by interacting with prompt with key in inventory. """
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0), hold=True)
    Await(activate_with_key or activate_without_key)
    if activate_with_key:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def DepartLevelIfFlagWithFailure_Object(
        _, prompt_object: Object, prompt_text: Text, failure_text: Text,
        disabled_flag: Flag, required_flag: Flag, end_trigger_flag: Flag):
    """ 11412250: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    activate_with_flag = Condition(
        FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
            prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0),
        hold=True)
    activate_without_flag = Condition(
        FlagDisabled(disabled_flag) and not required_flag and ActionButton(
            prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0),
        hold=True)
    Await(activate_with_flag or activate_without_flag)
    if activate_with_flag:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11413000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11415810: Mimic is activated by the player. """
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
    """ 11415820: Mimic state control. """
    IfCharacterDoesNotHaveSpecialEffect(1, mimic, 5420)
    IfAttacked(1, mimic, attacking_character=PLAYER)
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
    """ 11415830: Mimic goes to sleep. """
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
    """ 11415840: Mimic wakes up again. """
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
    """ 11415850: Mimic enters chest form. """
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
    """ 11415860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


@RestartOnRest
def RescueQuelana():
    """ 11410850: Rescue Quelana in sewers. """
    if CommonFlags.QuelanaRescued:
        DisableCharacter(Chrs.Quelana)
        return

    SetTeamType(Chrs.Quelana, TeamType.NoTeam)
    EnableInvincibility(Chrs.Quelana)

    Await(PlayerWithinDistance(Chrs.Quelana, 5.0))

    EnableFlag(CommonFlags.QuelanaRescued)
    PlaySoundEffect(Chrs.Quelana, SoundType.s_SFX, 777777777)
    DisplayBattlefieldMessage(CommonTexts.QuelanaRescued, 0)
    ForceAnimation(Chrs.Quelana, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Quelana)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11412999: Activate Abyss portal. """
    if CommonFlags.DisableAbyssPortal:
        DeleteFX(fx_id, erase_root_only=False)
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


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11412950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11412960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
