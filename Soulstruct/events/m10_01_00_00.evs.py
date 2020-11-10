"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .burg_constants import *


def Constructor():
    """ 0: Event 0 """
    # Taurus Demon arena
    BossBattle(
        0,
        Chrs.BurgBoss1, Chrs.BurgBoss1Twin, Flags.BurgBoss1IsTwin,
        Regions.BurgBoss1Trigger, Flags.BurgBoss1Dead, 1013802,
        ItemLots.BurgBoss1Reward,
        1011890, 1011891, 1011892, 1011893,
        1000, 1000,
    )

    # Watchtower Basement arena
    BossBattle(
        1,
        Chrs.BurgBoss2, Chrs.BurgBoss2Twin, Flags.BurgBoss2IsTwin,
        Regions.BurgBoss2Trigger, Flags.BurgBoss2Dead, 1013803,
        ItemLots.BurgBoss2Reward,
        1011790, 1011791, 0, 0,
        1000, 1000,
    )

    # Bell Gargoyles arena
    BossBattle(
        2,
        Chrs.ParishBoss1, Chrs.ParishBoss1Twin, Flags.ParishBoss1IsTwin,
        Regions.ParishBoss1Trigger, Flags.ParishBoss1Dead, 1013800,
        ItemLots.ParishBoss1Reward,
        1011990, 1011991, 1011992, 1011993,
        1000, 1000,
    )

    # Titanite Demon arena
    # TODO: Fog VFX is too narrow.
    BossBattle(
        3,
        Chrs.ParishBoss2, Chrs.ParishBoss2Twin, Flags.ParishBoss2IsTwin,
        Regions.ParishBoss2Trigger, Flags.ParishBoss2Dead, 1013804,
        ItemLots.ParishBoss2Reward,
        1011690, 1011691, 0, 0,  # "Exit" fog is always present for departure prompt.
        1000, 1000,
    )

    CreateBonfiresLaddersHazards()
    DisableFlag(11010580)
    SkipLinesIfFlagOff(2, 61010610)
    EndOfAnimation(1011101, 2)
    EnableNavmeshType(1013100, NavmeshType.Solid)
    SkipLinesIfClient(24)
    DisableObject(1011994)
    DeleteFX(1011995, erase_root_only=False)
    DisableObject(1011996)
    DeleteFX(1011997, erase_root_only=False)
    DisableObject(1011998)
    DeleteFX(1011999, erase_root_only=False)
    DisableObject(1011988)
    DeleteFX(1011989, erase_root_only=False)
    DisableObject(1011986)
    DeleteFX(1011987, erase_root_only=False)
    DisableObject(1011984)
    DeleteFX(1011985, erase_root_only=False)
    DisableObject(1011982)
    DeleteFX(1011983, erase_root_only=False)
    DisableObject(1011980)
    DeleteFX(1011981, erase_root_only=False)
    DisableObject(1011978)
    DeleteFX(1011979, erase_root_only=False)
    DisableObject(1011976)
    DeleteFX(1011977, erase_root_only=False)
    DisableObject(1011974)
    DeleteFX(1011975, erase_root_only=False)
    DisableObject(1011972)
    DeleteFX(1011973, erase_root_only=False)
    DisableObject(1011700)
    DeleteFX(1011701, False)
    DisableObject(1011702)
    DeleteFX(1011703, False)

    # Keep portcullis closed.
    EndOfAnimation(1011121, 3)

    ApplyShortcutSpEffect(0, 11010160, 1012401, 1012400)
    KeepDoorOpen(0, 11010160, 1011314)
    RunEvent(11010170, slot=2, args=(11010172, 1011311))  # Basement door disabled; no key required.
    RunEvent(11010190, slot=0, args=(11010190, 10010862, 1011308, 10010883, CommonGoods.PolishedKey))  # Lautrec cell.
    RunEvent(11010190, slot=1, args=(11010191, 10010860, 1011315, 10010883, CommonGoods.RustedKey))  # Watchtower upper.

    # Parish gate stuff.
    RunEvent(11015185)
    RunEvent(11010611)
    RunEvent(11010650)
    RunEvent(11010601)
    RunEvent(11015116)
    RunEvent(11010609)
    RunEvent(11010607)

    RingBell()
    KickDownLadder()
    HellkiteBreaksSpire()

    RoofAmbience()

    # Hellkite
    SkipLinesIfFlagOff(2, 11010900)
    RunEvent(11010900)
    SkipLines(29)
    RunEvent(11010899)
    RunEvent(11010900)
    RunEvent(11010782)
    RunEvent(11010783)
    RunEvent(11010790)
    RunEvent(11010791)
    RunEvent(11015301)
    RunEvent(11010784)
    RunEvent(11015302)
    RunEvent(11015303)
    RunEvent(11015304)
    RunEvent(11010851)
    RunEvent(11010852)
    RunEvent(11010890, slot=0, args=(11015320, 11015321, 11015322, 11015323, 11015324, 11015325, 11015326))
    RunEvent(11010890, slot=1, args=(11015327, 11015328, 11015329, 11015330, 11015331, 11015332, 11015333))
    RunEvent(11010890, slot=2, args=(11015334, 11015335, 11015336, 11015337, 11015338, 11015339, 11015340))
    RunEvent(11010850)
    RunEvent(11015307)
    RunEvent(11015308)
    RunEvent(11010200, slot=0, args=(10, 3000))
    RunEvent(11010200, slot=1, args=(20, 3001))
    RunEvent(11010200, slot=2, args=(30, 3002))
    RunEvent(11010200, slot=3, args=(40, 3009))
    RunEvent(11010200, slot=4, args=(50, 3010))
    RunEvent(11010200, slot=5, args=(60, 7004))
    RunEvent(11010200, slot=6, args=(70, 7005))
    RunEvent(11010200, slot=7, args=(80, 7008))
    RunEvent(11010200, slot=8, args=(90, 7009))
    RunEvent(11010200, slot=9, args=(100, 7011))

    # Lower Burg doors open on their own, mysteriously.
    OpenLowerBurgDoor(0, 1011250, 1012150)
    OpenLowerBurgDoor(1, 1011251, 1012150)
    OpenLowerBurgDoor(2, 1011252, 1012150)
    OpenLowerBurgDoor(3, 1011253, 1012151)
    OpenLowerBurgDoor(4, 1011254, 1012151)
    OpenLowerBurgDoor(5, 1011255, 1012151)

    # Five chests per level.
    OpenChest(0, 1011650, 11010600)
    OpenChest(1, 1011651, 11010601)
    OpenChest(2, 1011652, 11010602)
    OpenChest(3, 1011653, 11010603)
    OpenChest(4, 1011654, 11010604)
    OpenChest(10, 1011660, 11010610)
    OpenChest(11, 1011661, 11010611)
    OpenChest(12, 1011662, 11010612)
    OpenChest(13, 1011663, 11010613)
    OpenChest(14, 1011664, 11010614)

    # Mimics
    OpenMimic(0, Chrs.BurgMimic)
    ControlMimicState(0, Chrs.BurgMimic)
    HitMimicWithTalisman(0, Chrs.BurgMimic)
    TalismanWearsOffMimic(0, Chrs.BurgMimic)
    MimicReturnsToChest(0, Chrs.BurgMimic, Regions.BurgMimicNest)
    ReplanMimicAIOnLoad(0, Chrs.BurgMimic)
    OpenMimic(1, Chrs.ParishMimic)
    ControlMimicState(1, Chrs.ParishMimic)
    HitMimicWithTalisman(1, Chrs.ParishMimic)
    TalismanWearsOffMimic(1, Chrs.ParishMimic)
    MimicReturnsToChest(1, Chrs.ParishMimic, Regions.ParishMimicNest)
    ReplanMimicAIOnLoad(1, Chrs.ParishMimic)

    # Despawn enemies.
    for enemy in range(100):
        DespawnEnemy(enemy, 1010100 + enemy)
    for enemy in range(100):
        DespawnEnemy(100 + enemy, 1010400 + enemy)

    # Key rewards
    GetReward(0, 1010130, CommonItemLots.RustedKeyLot, CommonFlags.RustedKeyObtained)
    GetReward(1, 1010131, CommonItemLots.TarnishedKeyLot, CommonFlags.TarnishedKeyObtained)
    GetReward(2, 1010132, CommonItemLots.PolishedKeyLot, CommonFlags.PolishedKeyObtained)
    GetReward(3, 1010430, CommonItemLots.HolySigilLot, CommonFlags.HolySigilObtained)

    # Rescue Lobos Jr.
    RescueLobosJr()

    DepartLevelUnconditional_Object(  # Above bridge
        0, Objects.BurgExit1Prompt, CommonTexts.DepartLevel, Flags.BurgExit1Disabled, Flags.BurgExit1Activated,
        CommonFlags.InUndeadBurg)
    DepartLevelUnconditional_Object(  # Below bridge
        1, Objects.BurgExit2Prompt, CommonTexts.DepartLevel, Flags.BurgExit2Disabled, Flags.BurgExit2Activated,
        CommonFlags.InUndeadBurg)
    DepartLevelWithKey_Object(  # Aqueduct (near)
        0, Objects.BurgExit3Prompt, CommonTexts.DepartLevel, CommonTexts.PolishedKeyRequired, Flags.BurgExit3Disabled,
        CommonGoods.PolishedKey, Flags.BurgExit3Activated,
        CommonFlags.InUndeadBurg)
    DepartLevelWithKey_Object(  # Aqueduct (far)
        1, Objects.BurgExit4Prompt, CommonTexts.DepartLevel, CommonTexts.PolishedKeyRequired, Flags.BurgExit4Disabled,
        CommonGoods.PolishedKey, Flags.BurgExit4Activated,
        CommonFlags.InUndeadBurg)
    DepartLevelIfFlag_Object(  # Watchtower Basement
        0, Objects.BurgExit5Prompt, CommonTexts.DepartLevel, Flags.BurgExit5Disabled, Flags.BurgBoss2Dead,
        Flags.BurgExit5Activated,
        CommonFlags.InUndeadBurg)
    DepartLevelWithKey_Object(  # Depths
        2, Objects.BurgExit6Prompt, CommonTexts.DepartLevel, CommonTexts.TarnishedKeyRequired, Flags.BurgExit6Disabled,
        CommonGoods.PolishedKey, Flags.BurgExit6Activated,
        CommonFlags.InUndeadBurg)

    DepartLevelIfFlagWithFailure_Object(  # Sen's Fortress
        6, Objects.ParishExit1Prompt, CommonTexts.DepartLevel, Flags.ParishExit1Disabled, Flags.ParishBoss1Dead,
        CommonTexts.BellMustBeRung, Flags.ParishExit1Activated,
        CommonFlags.InUndeadParish)
    DepartLevelIfFlag_Object(  # Titanite Room
        1, Objects.ParishExit2Prompt, CommonTexts.DepartLevel, Flags.ParishExit2Disabled, Flags.ParishBoss2Dead,
        Flags.ParishExit2Activated,
        CommonFlags.InUndeadParish)
    DepartLevelWithKey_Region(  # Parish elevator
        0, Regions.ParishExit3Prompt, CommonTexts.DepartLevel, CommonTexts.HolySigilRequired, Flags.ParishExit3Disabled,
        CommonGoods.HolySigil, Flags.ParishExit3Activated,
        CommonFlags.InUndeadParish)
    DepartLevelUnconditional_Object(  # Rat room
        2, Objects.ParishExit4Prompt, CommonTexts.DepartLevel, Flags.ParishExit4Disabled, Flags.ParishExit4Activated,
        CommonFlags.InUndeadParish)

    ActivateAbyssPortal(0, 1010997, 1010998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, 6990, 6991, Chrs.BurgInvader, Regions.BurgInvaderTrigger, Flags.BurgInvaderDead)
    InvaderTrigger(1, 6990, 6991, Chrs.ParishInvader, Regions.ParishInvaderTrigger, Flags.ParishInvaderDead)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


def CreateBonfiresLaddersHazards():
    """ 11010008: Event 11010008 """
    RegisterBonfire(11010992, obj=1011960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11010984, obj=1011970, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11010010, stop_climbing_flag=11010011, obj=1011140)
    RegisterLadder(start_climbing_flag=11010012, stop_climbing_flag=11010013, obj=1011141)
    RegisterLadder(start_climbing_flag=11010014, stop_climbing_flag=11010015, obj=1011142)
    RegisterLadder(start_climbing_flag=11010016, stop_climbing_flag=11010017, obj=1011143)
    RegisterLadder(start_climbing_flag=11010018, stop_climbing_flag=11010019, obj=1011144)
    RegisterLadder(start_climbing_flag=11010020, stop_climbing_flag=11010021, obj=1011145)
    RegisterLadder(start_climbing_flag=11010022, stop_climbing_flag=11010023, obj=1011146)
    RegisterLadder(start_climbing_flag=11010024, stop_climbing_flag=11010025, obj=1011147)
    RegisterLadder(start_climbing_flag=11010026, stop_climbing_flag=11010027, obj=1011148)
    RegisterLadder(start_climbing_flag=11010030, stop_climbing_flag=11010031, obj=1011150)
    RegisterLadder(start_climbing_flag=11010032, stop_climbing_flag=11010033, obj=1011151)
    RegisterLadder(start_climbing_flag=11010034, stop_climbing_flag=11010035, obj=1011152)
    CreateHazard(11010300, 1011450, model_point=200, behavior_param_id=5000, target_type=DamageTargetType.Character,
                 radius=1.2000000476837158, life=0.0, repetition_time=1.0)
    CreateHazard(11010308, 1011407, model_point=100, behavior_param_id=5000, target_type=DamageTargetType.Character,
                 radius=0.699999988079071, life=0.0, repetition_time=1.0)
    CreateHazard(11010309, 1011408, model_point=100, behavior_param_id=5000, target_type=DamageTargetType.Character,
                 radius=0.699999988079071, life=0.0, repetition_time=1.0)


def EnterParishBoss1Fog():
    """ 11015390: Event 11015390 """
    IfFlagOff(1, 3)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1012998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1011990,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def ParishBoss1BattleStart():
    """ 11015393: Event 11015393 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 3)
    IfCharacterInsideRegion(1, PLAYER, region=1012996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(Chrs.ParishBoss1)
    if not Flags.ParishBoss1IsTwin:
        return
    ActivateMultiplayerBuffs(Chrs.ParishBoss1Twin)


@RestartOnRest
def ControlParishBoss1Behavior():
    """ 11015392: Event 11015392 """
    if Flags.ParishBoss1Dead:
        DisableCharacter(Chrs.ParishBoss1)
        DisableCharacter(Chrs.ParishBoss1Twin)
        Kill(Chrs.ParishBoss1, award_souls=False)
        Kill(Chrs.ParishBoss1Twin, award_souls=False)
        return

    DisableAI(Chrs.ParishBoss1)
    DisableAI(Chrs.ParishBoss1Twin)
    IfFlagOn(1, 11015393)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    EnableAI(Chrs.ParishBoss1)
    EnableBossHealthBar(Chrs.ParishBoss1, name=5350, slot=0)
    if not Flags.ParishBoss1IsTwin:
        return
    EnableAI(Chrs.ParishBoss1Twin)
    EnableBossHealthBar(Chrs.ParishBoss1Twin, name=5350, slot=1)


def ParishBoss1Death():
    """ 11010001: Event 11010001 """
    IfCharacterDead(1, Chrs.ParishBoss1)
    if Flags.ParishBoss1IsTwin:
        IfCharacterDead(1, Chrs.ParishBoss1Twin)
    IfConditionTrue(0, 1)

    EnableFlag(Flags.ParishBoss1Dead)
    DisableObject(1011990)
    DeleteFX(1011991, erase_root_only=True)
    DisableObject(1011992)
    DeleteFX(1011993, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)


def ParishBoss1MusicOn():
    """ 11015394: Event 11015394 """
    DisableNetworkSync()
    IfFlagOff(1, Flags.ParishBoss1Dead)
    IfFlagOn(1, 11015392)
    IfCharacterInsideRegion(1, PLAYER, region=1012990)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013801)
    EnableSoundEvent(1013800)


def ParishBoss1MusicOff():
    """ 11015395: Event 11015395 """
    DisableNetworkSync()
    IfFlagOn(1, 11015394)
    IfFlagOn(1, Flags.ParishBoss1Dead)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013800)
    EnableSoundEvent(1013801)


def Event11015380():
    """ 11015380: Event 11015380 """
    IfFlagOff(1, 11010901)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1012898, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1011890,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015381():
    """ 11015381: Event 11015381 """
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1012898, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1011890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012897)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015383():
    """ 11015383: Event 11015383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010901)
    IfCharacterInsideRegion(1, PLAYER, region=1012896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1010700, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1010700)


@RestartOnRest
def Event11015382():
    """ 11015382: Event 11015382 """
    SkipLinesIfThisEventOff(2)
    ResetStandbyAnimationSettings(1010700)
    End()
    DisableAI(1010700)
    SetStandbyAnimationSettings(1010700, standby_animation=9001)
    DisableHealthBar(1010700)
    IfAttacked(1, 1010700, attacking_character=PLAYER)
    IfHost(2)
    IfCharacterInsideRegion(2, PLAYER, region=1012701)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010005)
    ResetStandbyAnimationSettings(1010700)
    ForceAnimation(1010700, 9061, wait_for_completion=True)
    EnableAI(1010700)


def Event11015384():
    """ 11015384: Event 11015384 """
    DisableNetworkSync()
    IfFlagOff(1, 11010901)
    IfFlagOn(1, 11015382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015381)
    IfCharacterInsideRegion(1, PLAYER, region=1012890)
    IfConditionTrue(0, input_condition=1)
    EnableBossHealthBar(1010700, name=2250, slot=0)
    EnableSoundEvent(1013802)


def Event11015385():
    """ 11015385: Event 11015385 """
    DisableNetworkSync()
    IfFlagOn(1, 11015384)
    IfFlagOn(1, 11010901)
    IfConditionTrue(0, input_condition=1)
    DisableBossHealthBar(1010700, name=2250, slot=0)
    DisableSoundEvent(1013802)


def Event11015386():
    """ 11015386: Event 11015386 """
    EndIfClient()
    IfHasTAEEvent(1, 1010700, tae_event_id=700)
    IfHasTAEEvent(2, 1010700, tae_event_id=710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    Move(1010700, destination=1012741, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLines(1)
    Move(1010700, destination=1012740, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Restart()


@RestartOnRest
def Event11010901():
    """ 11010901: Event 11010901 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(1010700)
    Kill(1010700, award_souls=False)
    End()
    IfHealthLessThanOrEqual(0, 1010700, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1010700, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1010700)
    EnableFlag(11010901)
    KillBoss(1010700)
    DisableObject(1011890)
    DeleteFX(1011891, erase_root_only=True)
    DisableObject(1011892)
    DeleteFX(1011893, erase_root_only=True)


def Event11015370():
    """ 11015370: Event 11015370 """
    IfFlagOff(1, 11010902)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1012888, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1011790,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012887)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11015371():
    """ 11015371: Event 11015371 """
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015373)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1012888, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1011790)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1012887)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11015373():
    """ 11015373: Event 11015373 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11010902)
    IfCharacterInsideRegion(1, PLAYER, region=1012886)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    ActivateMultiplayerBuffs(1010750)
    EnableFlag(11010597)


@RestartOnRest
def Event11015372():
    """ 11015372: Event 11015372 """
    SkipLinesIfThisEventOn(5)
    DisableAI(1010750)
    IfFlagOn(1, 11015373)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010750)
    EnableBossHealthBar(1010750, name=2240, slot=0)


def Event11015374():
    """ 11015374: Event 11015374 """
    DisableNetworkSync()
    IfFlagOff(1, 11010902)
    IfFlagOn(1, 11015372)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11015371)
    IfCharacterInsideRegion(1, PLAYER, region=1012880)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1013803)


def Event11015375():
    """ 11015375: Event 11015375 """
    DisableNetworkSync()
    IfFlagOn(1, 11015374)
    IfFlagOn(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1013803)


@RestartOnRest
def Event11010902():
    """ 11010902: Event 11010902 """
    SkipLinesIfThisEventOff(7)
    DisableCharacter(1010750)
    DisableCharacter(1010500)
    DisableCharacter(1010501)
    Kill(1010750, award_souls=False)
    Kill(1010500, award_souls=False)
    Kill(1010501, award_souls=False)
    End()
    DisableCharacter(1010510)
    DisableCharacter(1010511)
    Kill(1010510, award_souls=False)
    Kill(1010511, award_souls=False)
    IfHealthLessThanOrEqual(0, 1010750, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1010750, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1010750)
    EnableFlag(11010902)
    KillBoss(1010750)
    DisableObject(1011790)
    DeleteFX(1011791, erase_root_only=True)


@RestartOnRest
def Event11010903():
    """ 11010903: Event 11010903 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1010310)
    End()
    IfCharacterDead(0, 1010310)
    EnableFlag(11010903)


@RestartOnRest
def Event11015110():
    """ 11015110: Event 11015110 """
    SkipLinesIfThisEventOff(2)
    PostDestruction(1011103, slot=1)
    End()
    DisableAI(1010102)
    IfEntityWithinDistance(1, PLAYER, 1010102, radius=5.0)
    IfObjectDestroyed(2, 1011103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(1010102, 3000, wait_for_completion=True)
    EnableAI(1010102)


@RestartOnRest
def Event11015111():
    """ 11015111: Event 11015111 """
    EndIfThisEventOn()
    DisableAI(1010110)
    IfCharacterInsideRegion(1, PLAYER, region=1012110)
    IfAttacked(2, 1010110, attacking_character=PLAYER)
    IfEntityWithinDistance(3, 1010110, PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 1)
    ForceAnimation(1010110, 13005, wait_for_completion=True)
    EnableAI(1010110)


@RestartOnRest
def Event11015113():
    """ 11015113: Event 11015113 """
    EndIfThisEventOn()
    DisableAI(1010200)
    IfCharacterInsideRegion(-1, PLAYER, region=1012050)
    IfAttacked(-1, 1010200, attacking_character=PLAYER)
    IfEntityWithinDistance(-1, 1010200, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010200)


@RestartOnRest
def Event11015112():
    """ 11015112: Event 11015112 """
    EndIfThisEventOn()
    DisableAI(1010111)
    IfAttacked(-3, 1010111, attacking_character=PLAYER)
    IfCharacterInsideRegion(-3, PLAYER, region=1012122)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=1012121)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(1010111)
    EndIfFinishedConditionTrue(1)
    SetNest(1010111, 1012120)
    AICommand(1010111, command_id=10, slot=0)
    ReplanAI(1010111)
    IfCharacterInsideRegion(-2, PLAYER, region=1012122)
    IfAttacked(-2, 1010111, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-2)
    AICommand(1010111, command_id=-1, slot=0)
    ReplanAI(1010111)


@RestartOnRest
def Event11015130():
    """ 11015130: Event 11015130 """
    DisableCharacter(1010400)
    EndIfFlagOn(11010710)
    IfObjectDestroyed(0, 1011000)
    EnableCharacter(1010400)
    SkipLinesIfFlagOn(4, 11015130)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    ForceAnimation(1010400, 500, wait_for_completion=True)
    SetNest(1010400, 1012060)
    AICommand(1010400, command_id=10, slot=0)
    ReplanAI(1010400)
    EnableFlag(11015130)
    IfCharacterInsideRegion(0, 1010400, region=1012060)
    AICommand(1010400, command_id=-1, slot=0)
    ReplanAI(1010400)


@RestartOnRest
def Event11010710():
    """ 11010710: Event 11010710 """
    DisableCharacter(1010400)
    EndIfFlagOn(11010710)
    IfCharacterDead(0, 1010400)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(33006000, host_only=True)


@RestartOnRest
def Event11010111():
    """ 11010111: Event 11010111 """
    EndIfThisEventOn()
    DisableAI(1010130)
    IfAttacked(1, 1010130, attacking_character=PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=1012170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010111)
    EnableAI(1010130)
    EndIfFinishedConditionTrue(1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011318, obj_act_id=-1, relative_index=3)
    Move(1010130, destination=1012171, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1010130, 7000)
    Wait(0.20000000298023224)
    ForceAnimation(1011318, 2, wait_for_completion=True)
    EnableFlag(61010518)
    DisableNetworkSync()
    Wait(4.0)
    DisableObjectActivation(1011318, obj_act_id=1318, relative_index=0)
    DisableObjectActivation(1011318, obj_act_id=1318, relative_index=1)
    EnableObjectActivation(1011318, obj_act_id=1318, relative_index=2)
    EnableObjectActivation(1011318, obj_act_id=1318, relative_index=3)


@RestartOnRest
def Event11010120():
    """ 11010120: Event 11010120 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1011102, 0)
    End()
    DisableAI(1010103)
    IfAttacked(-1, 1010103, attacking_character=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=1012101)
    IfConditionTrue(0, input_condition=-1)
    DisableNetworkSync()
    ResetAnimation(1010103, disable_interpolation=False)
    ForceAnimation(1010103, 3006)
    Wait(0.5)
    CreateObjectFX(100100, obj=1011102, model_point=1)
    ForceAnimation(1011102, 0)
    Wait(0.5)
    EnableAI(1010103)
    CreateHazard(11010121, 1011102, model_point=1, behavior_param_id=5020, target_type=DamageTargetType.Character,
                 radius=0.6000000238418579, life=3.0, repetition_time=0.0)
    Wait(3.0)
    DeleteObjectFX(1011102, erase_root=True)


def Event11010101(_, arg_0_3: int, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int):
    """ 11010101: Event 11010101 """
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_0_3, arg_4_7)
    End()
    IfActionButton(0, prompt_text=10010400, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=arg_8_9, trigger_attribute=TriggerAttribute.All)
    Move(PLAYER, destination=arg_0_3, destination_type=CoordEntityType.Object, model_point=arg_12_15, short_move=True)
    ForceAnimation(PLAYER, arg_16_19)
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event11010125():
    """ 11010125: Event 11010125 """
    EndIfThisEventOn()
    DisableCharacter(1010104)
    Move(1010104, destination=1012130, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    IfThisEventOn(0)
    EnableCharacter(1010104)


@RestartOnRest
def Event11010126():
    """ 11010126: Event 11010126 """
    EndIfThisEventOn()
    IfFlagOn(0, 51010030)
    EnableFlag(11010125)


@RestartOnRest
def OpenLowerBurgDoor(_, door: int, trigger_region: int):
    """ 11010130: Event 11010130 """
    if THIS_SLOT_FLAG:
        EndOfAnimation(door, 2)
        return
    IfCharacterInsideRegion(0, PLAYER, region=trigger_region)
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    Wait(0.1)
    ForceAnimation(door, 2)


def ApplyShortcutSpEffect(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010150: Event 11010150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


def KeepDoorOpen(_, arg_0_3: int, arg_4_7: int):
    """ 11010160: Event 11010160 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    Wait(2.0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_4_7, obj_act_id=-1, relative_index=3)


def Event11010170(_, arg_0_3: int, arg_8_11: int):
    """ 11010170: Event 11010170 """
    if THIS_SLOT_FLAG:
        DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
        DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
        DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
        DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
        return
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11010190(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11010190: Event 11010190 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(arg_12_15, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    SkipLines(1)
    DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def KickDownLadder():
    """ 11010100: Event 11010100 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1011149, 0)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011149)
    End()
    IfActionButton(0, prompt_text=10010500, anchor_entity=1011149, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=194, trigger_attribute=TriggerAttribute.All)
    EnableFlag(11010100)
    Move(PLAYER, destination=1011149, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1011149, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11010028, stop_climbing_flag=11010029, obj=1011149)


def Event11010400(_, arg_0_3: int, arg_4_7: int):
    """ 11010400: Event 11010400 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(arg_0_3, 101)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    ForceAnimation(arg_0_3, 100, loop=True)
    IfObjectDestroyed(0, arg_4_7)
    ForceAnimation(arg_0_3, 101, wait_for_completion=True)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event11015250(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 11015250: Event 11015250 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    DisableCharacterCollision(arg_0_3)
    IfEntityWithinDistance(0, PLAYER, arg_4_7, radius=arg_8_11)
    DisableNetworkSync()
    Wait(arg_12_15)
    EnableCharacterCollision(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=9060)


def Event11015185():
    """ 11015185: Event 11015185 """
    IfFlagOn(1, 61010610)
    IfObjectActivated(1, obj_act_id=11010650)
    IfFlagOff(2, 61010610)
    IfObjectActivated(2, obj_act_id=11010650)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015180)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015181)
    Restart()
    EnableFlag(11015182)
    Restart()


def Event11010611():
    """ 11010611: Event 11010611 """
    DisableNetworkSync()
    IfFramesElapsed(1, 10)
    IfInsideMap(1, game_map=UNDEAD_BURG)
    IfConditionTrue(0, input_condition=1)
    EnableObjectActivation(1011100, obj_act_id=-1)


def Event11010650():
    """ 11010650: Church gate object activation. """
    IfFlagOn(1, 11015181)
    IfHost(1)
    IfFlagOn(2, 11015182)
    IfHost(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015180)
    DisableFlag(11015181)
    DisableFlag(11015182)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(2, 61010610)
    RunEvent(11010611)
    Restart()
    EnableNavmeshType(1013100, NavmeshType.Solid)
    EnableFlag(11010605)
    ForceAnimation(1011101, 2)
    WaitFrames(60)
    RunEvent(11010611)
    Restart()
    SkipLinesIfFlagOff(2, 61010610)
    RunEvent(11010611)
    Restart()
    DisableNavmeshType(1013100, NavmeshType.Solid)
    ForceAnimation(1011101, 4)
    WaitFrames(200)
    RunEvent(11010611)
    Restart()


def Event11010601():
    """ 11010601: Event 11010601 """
    IfFlagOn(0, 11010605)
    DisableFlag(11010605)
    Wait(0.5)
    CreateHazard(11010602, 1011101, model_point=42, behavior_param_id=5010, target_type=DamageTargetType.Character,
                 radius=0.6000000238418579, life=0.5, repetition_time=0.0)
    CreateHazard(11010603, 1011101, model_point=43, behavior_param_id=5010, target_type=DamageTargetType.Character,
                 radius=0.6000000238418579, life=0.5, repetition_time=0.0)
    CreateHazard(11010604, 1011101, model_point=44, behavior_param_id=5010, target_type=DamageTargetType.Character,
                 radius=0.6000000238418579, life=0.5, repetition_time=0.0)
    Restart()


@RestartOnRest
def Event11015116():
    """ 11015116: Event 11015116 """
    IfFlagOff(1, 61010610)
    IfFlagOff(1, 11010607)
    IfFlagOff(1, 11010650)
    IfCharacterInsideRegion(1, PLAYER, region=1012200)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015115)
    IfFlagOn(-1, 11015181)
    IfFlagOn(-1, 61010610)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11015115)


@RestartOnRest
def Event11010609():
    """ 11010609: Event 11010609 """
    DisableNetworkSync()
    IfFlagOn(1, 11015115)
    IfFlagOff(1, 61010610)
    IfConditionTrue(0, input_condition=1)
    ActivateObject(1011100, obj_act_id=-1, relative_index=-1)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event11010607():
    """ 11010607: Event 11010607 """
    SkipLinesIfThisEventOff(3)
    Move(6010, destination=1012201, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(6010, 1012201)
    End()
    IfCharacterInsideRegion(1, 6010, region=1012771)
    IfEntityWithinDistance(1, 6010, 1011100, radius=3.0)
    IfFlagOn(1, 11015181)
    IfConditionTrue(0, input_condition=1)
    SetNest(6010, 1012201)
    ClearTargetList(6010)
    ReplanAI(6010)


@RestartOnRest
def Event11010608():
    """ 11010608: Event 11010608 """
    IfFlagOn(1, 61010610)
    IfCharacterBackreadEnabled(1, 1010310)
    IfCharacterInsideRegion(1, 1010310, region=1012771)
    IfConditionTrue(0, input_condition=1)
    AICommand(1010310, command_id=1, slot=0)
    SetNest(1010310, 1012773)
    IfFlagOff(0, 61010610)
    AICommand(1010310, command_id=-1, slot=0)
    SetNest(1010310, 1012772)
    Restart()


def Event11010621():
    """ 11010621: Event 11010621 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1011121, 4)
    DisableObjectActivation(1011120, obj_act_id=-1)
    End()
    EndOfAnimation(1011121, 3)
    # IfObjectActivated(0, obj_act_id=11010620)
    # ForceAnimation(1011121, 4)


def RingBell():
    """ 11010700: Event 11010700 """
    if THIS_FLAG:
        DisableObjectActivation(1011110, obj_act_id=-1)
        return
    IfObjectActivated(0, obj_act_id=11010700)
    IfHealthGreaterThan(0, PLAYER, 0.0)
    PlayCutscene(100100, skippable=True, fade_out=False, player_id=PLAYER)


def Event11015170():
    """ 11015170: Event 11015170 """
    IfMultiplayerEvent(0, 10010)
    DisableNetworkSync()
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    WaitRandomSeconds(min_seconds=0.5, max_seconds=2.0)
    PlaySoundEffect(anchor_entity=1011111, sound_type=SoundType.o_Object, sound_id=130300002)
    Restart()


@RestartOnRest
def Event11010860(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11010860: Event 11010860 """
    SkipLinesIfThisEventSlotOff(3)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()
    IfCharacterDead(0, arg_0_3)
    SkipLinesIfEqual(4, left=arg_4_7, right=0)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(arg_8_11, host_only=True)
    End()


def OpenChest(_, chest: int, obj_act_id: int):
    """ 11010600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(chest, 0)
    DisableObjectActivation(chest, obj_act_id=-1)
    EnableTreasure(chest)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(10)
    EnableTreasure(chest)


def Event11010899():
    """ 11010899: Event 11010899 """
    EnableImmortality(1010300)
    DisableCharacter(1010300)
    SetNest(1010300, 1012320)
    SkipLinesIfClient(2)
    SetNetworkUpdateAuthority(1010300, UpdateAuthority.Forced)
    DisableFlag(11010782)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    SkipLinesIfConditionFalse(6, 1)
    DisableFlag(11015310)
    EnableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013211)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    DisableCharacterCollision(1010300)
    DisableGravity(1010300)
    IfFlagOn(2, 11010791)
    IfFlagOn(2, 11015311)
    SkipLinesIfConditionFalse(4, 2)
    EnableCharacter(1010300)
    Move(1010300, destination=1012320, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ResetStandbyAnimationSettings(1010300)
    SetNest(1010300, 1012340)
    RunEvent(11010805, slot=0, args=(11015320, 11015325, 7004, 11015350))
    RunEvent(11010805, slot=1, args=(11015326, 11015331, 7008, 11015350))
    RunEvent(11010805, slot=2, args=(11015332, 11015333, 7009, 11015350))
    RunEvent(11010805, slot=3, args=(11015334, 11015337, 7011, 11015350))
    RunEvent(11010805, slot=4, args=(11015338, 11015339, 7006, 11015350))
    RunEvent(11010805, slot=5, args=(11015320, 11015323, 7009, 11015351))
    RunEvent(11010805, slot=6, args=(11015324, 11015339, 7006, 11015351))
    RunEvent(11010805, slot=7, args=(11015320, 11015323, 7011, 11015352))
    RunEvent(11010805, slot=8, args=(11015324, 11015339, 7006, 11015352))
    RunEvent(11010805, slot=9, args=(11015320, 11015321, 7004, 11015353))
    RunEvent(11010805, slot=10, args=(11015322, 11015333, 7008, 11015353))
    RunEvent(11010805, slot=11, args=(11015334, 11015335, 7009, 11015353))
    RunEvent(11010805, slot=12, args=(11015336, 11015337, 7011, 11015353))
    RunEvent(11010800, slot=0, args=(11015338, 11015339, 7010, 11015353))
    RunEvent(11010800, slot=1, args=(11015320, 11015339, 7010, 11015354))


@RestartOnRest
def Event11010900():
    """ 11010900: Event 11010900 """
    SkipLinesIfThisEventOff(4)
    DisableCharacter(1010300)
    DisableCharacter(1010301)
    DisableCharacter(1010302)
    End()
    IfHealthLessThan(7, 1010300, 0.10000000149011612)
    IfFlagOff(7, 11015312)
    IfFlagOff(7, 11015300)
    IfConditionTrue(1, input_condition=7)
    IfConditionTrue(2, input_condition=7)
    IfConditionTrue(3, input_condition=7)
    IfFlagOff(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(2, 11010791)
    IfFlagOff(2, 11015311)
    IfFlagOn(3, 11010791)
    IfFlagOn(3, 11015311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(3, 1)
    ForceAnimation(1010300, 7001, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    ForceAnimation(1010300, 7007, wait_for_completion=True)
    DisableCharacter(1010300)
    End()
    DisableImmortality(1010300)
    Kill(1010300, award_souls=True)


@RestartOnRest
def Event11010790():
    """ 11010790: Event 11010790 """
    DisableGravity(1010302)
    EnableInvincibility(1010302)
    DisableCharacter(1010302)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(1010302, UpdateAuthority.Forced)
    EndIfThisEventOn()
    IfCharacterInsideRegion(0, PLAYER, region=1012301)
    EnableFlag(11010790)
    SetNetworkUpdateRate(1010302, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableCollision(1013200)
    EnableCharacter(1010302)
    Move(1010302, destination=1012300, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1010302, 7012, wait_for_completion=True)
    DisableCharacter(1010302)
    EnableCollision(1013200)


def Event11010791():
    """ 11010791: Event 11010791 """
    EndIfThisEventOn()
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOff(1, 11010782)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfCharacterInsideRegion(1, PLAYER, region=1012305)
    IfAllPlayersOutsideRegion(1, region=1012337)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    EnableFlag(11010791)
    EnableFlag(11010780)
    EnableCharacter(1010300)
    Move(1010300, destination=1012302, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7005)
    WaitFrames(395)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DisableFlag(11015310)


def HellkiteBreaksSpire():
    """ 11010780: Event 11010780 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1011290, 2)
    End()
    IfHasTAEEvent(0, 1010300, tae_event_id=1000)
    ForceAnimation(1011290, 1, wait_for_completion=True)
    ForceAnimation(1011290, 2, loop=True)


@RestartOnRest
def Event11010784():
    """ 11010784: Event 11010784 """
    IfHasTAEEvent(0, 1010300, tae_event_id=500)
    EnableFlag(11015300)
    IfHasTAEEvent(0, 1010300, tae_event_id=600)
    DisableFlag(11015300)
    Restart()


@RestartOnRest
def Event11015301():
    """ 11015301: Event 11015301 """
    DisableCharacter(1010301)
    IfCharacterBackreadEnabled(0, 1010300)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(1010300, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010300, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1010300, command_id=20, slot=0)
    End()
    CreateNPCPart(1010300, npc_part_id=3430, part_index=NPCPartType.Part1, part_health=200, damage_correction=1.0,
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, 1010300, npc_part_id=3430, value=0)
    IfFlagOff(1, 11015300)
    IfAttacked(1, 1010300, attacking_character=PLAYER)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfCharacterDead(2, 1010300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, 11015311)
    ForceAnimation(1010300, 8000)
    SkipLines(1)
    ForceAnimation(1010300, 8010)
    IfHasTAEEvent(0, 1010300, tae_event_id=400)
    SetDisplayMask(1010300, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(1010300, bit_index=1, switch_type=OnOffChange.Off)
    Move(1010301, destination=1010300, destination_type=CoordEntityType.Character, model_point=66,
         copy_draw_parent=1010300)
    EnableCharacter(1010301)
    ForceAnimation(1010301, 8100)
    AICommand(1010300, command_id=20, slot=0)
    ReplanAI(1010300)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34310000, host_only=True)


def Event11015302():
    """ 11015302: Event 11015302 """
    IfHost(-7)
    IfCharacterType(-7, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfConditionTrue(6, input_condition=1)
    IfConditionTrue(7, input_condition=1)
    IfFlagOn(2, 11010100)
    IfCharacterInsideRegion(2, PLAYER, region=1012330)
    IfCharacterInsideRegion(3, PLAYER, region=1012331)
    IfFlagOn(4, 11010100)
    IfCharacterInsideRegion(4, PLAYER, region=1012332)
    IfCharacterInsideRegion(5, PLAYER, region=1012333)
    IfFlagOn(6, 11015305)
    IfFlagOn(7, 11015317)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11015310)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(11015350)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(11015351)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(11015352)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(11015353)
    SkipLinesIfFinishedConditionTrue(2, 6)
    SkipLinesIfFinishedConditionTrue(1, 7)
    SkipLines(1)
    EnableFlag(11015354)
    DisableFlagRange((11015320, 11015339))
    SkipLinesIfClient(2)
    EnableRandomFlagInRange((11015320, 11015339))
    EnableFlag(11015313)
    Restart()


def Event11010805(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010805: Event 11010805 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SkipLinesIfNotEqual(2, left=arg_8_11, right=7011)
    EnableFlag(11015312)
    AddSpecialEffect(1010300, 4160)
    SkipLinesIfEqual(1, left=arg_8_11, right=7006)
    ForceAnimation(1010300, arg_8_11)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7004)
    WaitFrames(190)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7006)
    WaitFrames(90)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7008)
    WaitFrames(200)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7009)
    WaitFrames(180)
    SkipLinesIfNotEqual(1, left=arg_8_11, right=7011)
    WaitFrames(192)
    CancelSpecialEffect(1010300, 4160)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015312)
    DisableFlag(11015310)
    Restart()


def Event11010800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010800: Event 11010800 """
    IfHost(1)
    IfFlagOn(1, 11015310)
    IfFlagOn(1, arg_12_15)
    IfFlagRangeAnyOn(1, (arg_0_3, arg_4_7))
    IfHealthGreaterThan(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    RestartIfFlagOn(11015311)
    EnableFlag(11015311)
    EnableCharacterCollision(1010300)
    EnableGravity(1010300)
    SkipLinesIfClient(1)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ResetStandbyAnimationSettings(1010300)
    SetBackreadStateAlternate(1010300, state=True)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(1010300, 4160)
    ForceAnimation(1010300, arg_8_11)
    WaitFrames(111)
    CancelSpecialEffect(1010300, 4160)
    SetBackreadStateAlternate(1010300, state=False)
    DisableFlagRange((11015350, 11015354))
    DisableFlagRange((11015320, 11015339))
    DisableFlag(arg_12_15)
    DisableFlag(11015317)
    DisableFlag(11015310)
    Restart()


def Event11010890(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int,
                  arg_24_27: int):
    """ 11010890: Event 11010890 """
    IfFlagOn(1, 11015313)
    IfFlagOn(2, 11015313)
    IfFlagOn(3, 11015313)
    IfFlagOn(4, 11015313)
    IfFlagOn(5, 11015313)
    IfFlagOn(6, 11015313)
    IfFlagOn(7, 11015313)
    IfFlagOn(1, arg_0_3)
    IfFlagOn(2, arg_4_7)
    IfFlagOn(3, arg_8_11)
    IfFlagOn(4, arg_12_15)
    IfFlagOn(5, arg_16_19)
    IfFlagOn(6, arg_20_23)
    IfFlagOn(7, arg_24_27)
    IfConditionTrue(-7, input_condition=1)
    IfConditionTrue(-7, input_condition=2)
    IfConditionTrue(-7, input_condition=3)
    IfConditionTrue(-7, input_condition=4)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=6)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(0, input_condition=-7)
    DisableFlag(11015313)
    SkipLinesIfFinishedConditionFalse(1, 1)
    EnableFlag(arg_0_3)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(arg_4_7)
    SkipLinesIfFinishedConditionFalse(1, 3)
    EnableFlag(arg_8_11)
    SkipLinesIfFinishedConditionFalse(1, 4)
    EnableFlag(arg_12_15)
    SkipLinesIfFinishedConditionFalse(1, 5)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionFalse(1, 6)
    EnableFlag(arg_20_23)
    SkipLinesIfFinishedConditionFalse(1, 7)
    EnableFlag(arg_24_27)
    Restart()


def Event11015303():
    """ 11015303: Event 11015303 """
    IfFlagOff(1, 11015306)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11010100)
    IfCharacterInsideRegion(-7, PLAYER, region=1012332)
    IfCharacterInsideRegion(-7, PLAYER, region=1012335)
    IfCharacterInsideRegion(-7, PLAYER, region=1012336)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(2, 11015306)
    IfFlagOff(2, 11015311)
    IfFlagOn(2, 11010791)
    IfAllPlayersOutsideRegion(2, region=1012332)
    IfAllPlayersOutsideRegion(2, region=1012335)
    IfAllPlayersOutsideRegion(2, region=1012336)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015306)
    Restart()
    DisableFlag(11015306)
    RestartEvent(11015304, slot=0)
    Restart()


def Event11015304():
    """ 11015304: Event 11015304 """
    DisableNetworkSync()
    IfFlagOff(1, 11015305)
    IfFlagOn(1, 11015306)
    IfConditionTrue(0, input_condition=1)
    Wait(20.0)
    EnableFlag(11015305)
    Restart()


def Event11010850():
    """ 11010850: Event 11010850 """
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfAttacked(1, 1010300, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015317)
    Restart()


def Event11010851():
    """ 11010851: Event 11010851 """
    IfFlagOff(1, 11015316)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfAllPlayersOutsideRegion(1, region=1012338)
    IfHealthLessThan(1, 1010300, 0.699999988079071)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfFlagOn(2, 11015316)
    IfFlagOn(2, 11010791)
    IfCharacterInsideRegion(2, PLAYER, region=1012338)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    EnableFlag(11015316)
    Restart()
    DisableFlag(11015316)
    RestartEvent(11010852, slot=0)
    Restart()


def Event11010852():
    """ 11010852: Event 11010852 """
    DisableNetworkSync()
    IfFlagOff(1, 11015315)
    IfFlagOn(1, 11015316)
    IfConditionTrue(0, input_condition=1)
    Wait(60.0)
    EnableFlag(11015315)
    Restart()


@RestartOnRest
def Event11015307():
    """ 11015307: Event 11015307 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfFlagOn(1, 11015311)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    SetNest(1010300, 1012320)
    IfHasTAEEvent(0, 1010300, tae_event_id=700)
    Move(1010300, destination=1012340, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7016)
    WaitFrames(110)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    AICommand(1010300, command_id=-1, slot=1)
    DisableAI(1010300)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    DisableFlag(11015305)
    DisableFlag(11015309)
    DisableFlag(11015311)
    Restart()


def Event11015308():
    """ 11015308: Event 11015308 """
    IfFlagOff(1, 11015309)
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010791)
    IfHealthGreaterThanOrEqual(1, 1010300, 0.10000000149011612)
    IfAllPlayersOutsideRegion(1, region=1012334)
    IfFlagOn(2, 11015309)
    IfFlagOff(2, 11015310)
    IfFlagOn(2, 11010791)
    IfHealthGreaterThanOrEqual(2, 1010300, 0.10000000149011612)
    IfCharacterInsideRegion(2, PLAYER, region=1012334)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(11015309)
    AICommand(1010300, command_id=1, slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()
    DisableFlag(11015309)
    AICommand(1010300, command_id=-1, slot=1)
    ClearTargetList(1010300)
    ReplanAI(1010300)
    Restart()


def Event11010782():
    """ 11010782: Event 11010782 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(1, PLAYER, region=1012337)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(10)
    RestartIfFlagOn(11015311)
    EnableFlag(11015310)
    EnableFlag(11015312)
    DisableFlag(11010791)
    SetNetworkUpdateRate(1010300, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(1010300, 7013, wait_for_completion=True)
    DisableCharacter(1010300)
    Move(1010300, destination=1012310, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013210)


def Event11010783():
    """ 11010783: Event 11010783 """
    IfFlagOff(1, 11015310)
    IfFlagOn(1, 11010790)
    IfFlagOn(1, 11010791)
    IfFlagOff(1, 11015311)
    IfFlagOn(1, 11015315)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11015310)
    SetStandbyAnimationSettings(1010300, standby_animation=7018)
    ForceAnimation(1010300, 7017, wait_for_completion=True)
    IfHealthGreaterThanOrEqual(0, 1010300, 0.699999988079071)
    SetStandbyAnimationSettings(1010300, standby_animation=7006)
    ForceAnimation(1010300, 7019)
    WaitFrames(50)
    DisableFlag(11015315)
    DisableFlag(11015316)
    DisableFlag(11015310)
    Restart()


def Event11010200(_, arg_0_3: int, arg_4_7: int):
    """ 11010200: Event 11010200 """
    IfCharacterBackreadEnabled(1, 1010300)
    IfHasTAEEvent(1, 1010300, tae_event_id=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    HellkiteBreathControl(1010300, obj=1011060, animation_id=arg_4_7)
    IfDoesNotHaveTAEEvent(0, 1010300, tae_event_id=arg_0_3)
    Restart()


def Event11010510(_, arg_0_3: int, arg_4_7: int):
    """ 11010510: Event 11010510 """
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
    RestartIfThisEventSlotOff()
    IfFlagOn(0, 744)
    EnableFlag(744)
    IfFlagOff(0, 744)
    Restart()


def Event11010520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010520: Event 11010520 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11010501(_, arg_0_3: int, arg_4_7: int):
    """ 11010501: Event 11010501 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    EnableCharacter(arg_0_3)
    SetTeamTypeAndExitStandbyAnimation(arg_0_3, TeamType.HostileAlly)
    SetAIParamID(arg_0_3, 1)
    SaveRequest()
    RestartIfThisEventOff()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Restart()


def Event11010530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010530: Event 11010530 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1000)
    IfFlagOn(1, 11010591)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11010531(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010531: Event 11010531 """
    IfFlagOff(1, 1004)
    IfFlagOn(1, 1008)
    IfFlagOn(1, 11510594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    Move(arg_0_3, destination=1012530, destination_type=CoordEntityType.Region, model_point=-1, set_draw_parent=1013050)
    SetNest(arg_0_3, 1012530)
    EnableCharacter(arg_0_3)


def Event11010532(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010532: Event 11010532 """
    IfFlagOff(1, 1114)
    IfFlagOn(1, 1110)
    IfFlagOn(1, 11010181)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ResetStandbyAnimationSettings(arg_0_3)


def Event11010533(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010533: Event 11010533 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1174)
    IfFlagOn(1, 11310590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    ClearEventValue(600, bit_count=4)


def Event11010534(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010534: Event 11010534 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 724)
    IfCharacterAlive(1, arg_0_3)
    IfThisEventOff(1)
    IfHost(2)
    IfFlagOff(2, 1176)
    IfFlagOff(2, 1177)
    IfFlagOff(2, 1179)
    IfFlagOff(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010535(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010535: Event 11010535 """
    IfFlagOff(1, 1176)
    IfFlagOn(-7, 1175)
    IfFlagOn(-7, 1179)
    IfConditionTrue(1, input_condition=-7)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfThisEventOff(1)
    IfFlagOn(2, 1180)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11010537(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010537: Event 11010537 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOff(1, 1196)
    IfFlagOff(1, 1198)
    IfEventValueComparison(1, 600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    IfThisEventOff(1)
    IfFlagOn(2, 703)
    IfFlagOn(3, 11010599)
    IfFlagOn(3, arg_12_15)
    IfThisEventOn(3)
    IfFlagOff(4, 11010599)
    IfFlagOn(4, arg_12_15)
    IfThisEventOn(4)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, 3)
    SkipLinesIfFinishedConditionFalse(9, 1)
    EnableFlag(11010599)
    SkipLinesIfClient(3)
    EnableFlag(50006070)
    DisableFlag(50006071)
    DisableFlag(50006080)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DropMandatoryTreasure(arg_0_3)
    End()
    SkipLinesIfFinishedConditionFalse(3, 2)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    End()
    DropMandatoryTreasure(arg_0_3)


def Event11010538():
    """ 11010538: Event 11010538 """
    IfFlagOff(1, 1176)
    IfFlagOff(1, 1179)
    IfFlagOn(1, 1175)
    IfFlagOn(1, 11010596)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(11010596)
    ClearEventValue(600, bit_count=4)
    Restart()


def Event11010539():
    """ 11010539: Event 11010539 """
    EndIfClient()
    IfFlagOn(1, 1177)
    IfFlagOn(1, 50006071)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(815)


def Event11010550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010550: Event 11010550 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(1, 11010190)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11010584)


def Event11010551():
    """ 11010551: Event 11010551 """
    EndIfFlagOn(11010593)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(1011308, obj_act_id=-1, relative_index=3)
    IfFlagOn(0, 11010593)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=0)
    EnableObjectActivation(1011308, obj_act_id=-1, relative_index=1)


def Event11010552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11010552: Event 11010552 """
    IfFlagOff(1, 1574)
    IfFlagOn(1, 1570)
    IfFlagOn(-1, 3)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11010581(_, arg_0_3: int):
    """ 11010581: Event 11010581 """
    EndIfThisEventOn()
    IfFlagOn(0, 11010700)
    EnableCharacter(arg_0_3)


@RestartOnRest
def Event11010582():
    """ 11010582: Event 11010582 """
    SkipLinesIfClient(1)
    DisableFlag(11010586)
    SkipLinesIfFlagOn(4, 11010586)
    IfFlagOn(-1, 1175)
    IfFlagOn(-1, 1179)
    IfFlagOn(-1, 1181)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11010586)
    DisableCharacter(1010320)


def Event11010583():
    """ 11010583: Event 11010583 """
    EndIfClient()
    IfFlagOn(0, 744)
    IfFlagOff(0, 744)
    Wait(1.0)
    Move(6001, destination=1012010, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6001, standby_animation=7845)
    Move(6040, destination=1012011, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    Move(6072, destination=1012012, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6072, standby_animation=7880)
    Move(6190, destination=1012013, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6190, standby_animation=9000)
    DisableFlag(11015090)
    RestoreObject(1011010)
    RestartEvent(11015090, slot=0)
    Move(6230, destination=1012014, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6230, standby_animation=9000)
    Move(6300, destination=1012015, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetStandbyAnimationSettings(6300, standby_animation=7825)
    Restart()


def Event11010580():
    """ 11010580: Event 11010580 """
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    IfConditionTrue(1, input_condition=-7)
    IfFlagOn(1, 11015030)
    IfFlagOff(1, 11015031)
    IfConditionTrue(2, input_condition=-7)
    IfFlagOff(2, 11015030)
    IfFlagOn(2, 11015031)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionFalse(9, 1)
    AddSpecialEffect(PLAYER, 4170)
    SkipLinesIfClient(1)
    RotateToFaceEntity(PLAYER, 6480)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)
    ForceAnimation(PLAYER, 7896, loop=True)
    EnableFlag(11015031)
    Restart()
    CancelSpecialEffect(PLAYER, 4170)
    SkipLinesIfHost(1)
    SkipLinesIfThisEventOff(1)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)
    DisableFlag(11015031)
    Restart()


def Event11010585():
    """ 11010585: Event 11010585 """
    DisableNetworkSync()
    WaitFrames(2)
    EnableFlag(11010580)


@RestartOnRest
def Event11015090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11015090: Event 11015090 """
    EndIfFlagOn(arg_0_3)
    EndIfFlagOn(arg_4_7)
    EnableObjectInvulnerability(arg_8_11)
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(arg_8_11)
    WaitFrames(1)
    DestroyObject(arg_8_11, slot=1)
    PlaySoundEffect(anchor_entity=arg_8_11, sound_type=SoundType.o_Object, sound_id=125200000)
    EnableFlag(11015090)
    IfFlagOn(0, 703)
    End()


def Event11015100():
    """ 11015100: Event 11015100 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6540, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6001)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6540)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6540)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6540, region=1012000, summon_flag=11015102, dismissal_flag=11015106)
    DisableCharacter(6001)


def Event11015101():
    """ 11015101: Event 11015101 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015102)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6540, command_id=10, slot=0)
    ReplanAI(6540)
    IfCharacterInsideRegion(0, 6540, region=1012998)
    RotateToFaceEntity(6540, 1012997)
    ForceAnimation(6540, 7410)
    AICommand(6540, command_id=-1, slot=0)
    ReplanAI(6540)


def Event11015103():
    """ 11015103: Event 11015103 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6590, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6590)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=5, arg2=2)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, 6590)
    IfEntityWithinDistance(1, 6590, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6590, region=1012001, summon_flag=11015105, dismissal_flag=11015107)


def Event11015203():
    """ 11015203: Event 11015203 """
    IfFlagOn(0, 11015105)
    AddSpecialEffect(6590, 5450)


def Event11015104():
    """ 11015104: Event 11015104 """
    EndIfThisEventOn()
    IfFlagOn(1, 11015105)
    IfFlagOn(1, 11015393)
    IfConditionTrue(0, input_condition=1)
    AICommand(6590, command_id=10, slot=0)
    ReplanAI(6590)
    IfCharacterInsideRegion(0, 6590, region=1012998)
    RotateToFaceEntity(6590, 1012997)
    ForceAnimation(6590, 7410)
    AICommand(6590, command_id=-1, slot=0)
    ReplanAI(6590)


def Event11015900():
    """ 11015900: Event 11015900 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6540, UpdateAuthority.Forced)
    SkipLinesIfThisEventOff(1)
    DisableCharacter(6001)
    SkipLinesIfFlagOn(3, 11015106)
    IfClient(2)
    IfFlagOn(2, 11015102)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6540)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015102)
    IfFlagOff(1, 11015106)
    IfFlagOn(-1, 1004)
    IfFlagOn(-1, 1005)
    IfFlagOn(-1, 1006)
    IfFlagOn(-1, 1010)
    IfFlagOn(-1, 1011)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterBackreadEnabled(1, 6540)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6540, region=1012000, summon_flag=11015102, dismissal_flag=11015106)
    DisableCharacter(6001)


def Event11015901():
    """ 11015901: Event 11015901 """
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(6590, UpdateAuthority.Forced)
    SkipLinesIfFlagOn(3, 11015107)
    IfClient(2)
    IfFlagOn(2, 11015105)
    SkipLinesIfConditionTrue(1, 2)
    DisableCharacter(6590)
    EndIfFlagOn(3)
    IfMultiplayerCount(condition=1, arg1=4, arg2=3)
    IfHost(1)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 11015105)
    IfFlagOff(1, 11015107)
    IfFlagOn(1, 11020607)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 1574)
    IfCharacterBackreadEnabled(1, 6590)
    IfEntityWithinDistance(1, 6590, PLAYER, radius=20.0)
    IfCharacterHasSpecialEffect(1, PLAYER, 28)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlueEyeSign, 6590, region=1012001, summon_flag=11015105, dismissal_flag=11015107)


def Event11015990(_, arg_0_3: int, arg_4_7: int):
    """ 11015990: Event 11015990 """
    IfFlagOn(0, arg_0_3)
    EraseNPCSummonSign(summoned_character=arg_4_7)
    IfFlagOff(0, arg_0_3)
    Restart()


def RoofAmbience():
    """ 11010690: Enable roof ambience when boss defeated. """
    DisableSoundEvent(1013801)
    Await(Flags.ParishBoss1Dead)
    EnableSoundEvent(1013801)


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11012060: All-in-one boss event for simplicity. """
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
    """ 11012260: Invasion is triggered. Human not needed. """
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


def DepartLevelUnconditional_Region(
        _, prompt_region: Region, prompt_text: Text, disabled_flag: Flag,
        end_trigger_flag: Flag):
    """ 11012200: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelUnconditional_Object(
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag,
        end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11012205: Depart level by interacting with prompt. No conditions. """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelWithKey_Region(
        _, prompt_region: Region, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
        key: GoodParam, end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11012210: Depart level by interacting with prompt with key in inventory. """
    if not FlagEnabled(in_map_flag):
        return
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region), hold=True)
    Await(activate_with_key or activate_without_key)
    if activate_with_key:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def DepartLevelWithKey_Object(
        _, prompt_object: Object, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
        key: GoodParam, end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11012215: Depart level by interacting with prompt with key in inventory. """
    if not FlagEnabled(in_map_flag):
        return
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object), hold=True)
    Await(activate_with_key or activate_without_key)
    if activate_with_key:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def DepartLevelIfFlag_Object(
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
        end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11012220: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlagWithFailure_Object(
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
        failure_text: Text, end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11012230: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    if not FlagEnabled(in_map_flag):
        return
    if FlagEnabled(disabled_flag):
        return
    activate_with_flag = Condition(FlagDisabled(disabled_flag) and required_flag
                                   and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object), hold=True)
    activate_without_flag = Condition(FlagDisabled(disabled_flag) and not required_flag
                                      and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object), hold=True)
    Await(activate_with_flag or activate_without_flag)
    if activate_with_flag:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11015810: Mimic is activated by the player. """
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
    """ 11015820: Mimic state control. """
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
    """ 11015830: Mimic goes to sleep. """
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
    """ 11015840: Mimic wakes up again. """
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
    """ 11015850: Mimic enters chest form. """
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
    """ 11015860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11012270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11013000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def RescueLobosJr():
    """ 11010950: Rescue Lobos Jr. """
    if CommonFlags.LobosJrRescued:
        DisableCharacter(Chrs.LobosJr)
        return

    EnableInvincibility(Chrs.LobosJr)

    Await(FlagEnabled(11010190))  # Parish cell opened.
    EnableFlag(CommonFlags.LobosJrRescued)
    DisplayBattlefieldMessage(CommonTexts.LobosJrRescued, 0)
    PlaySoundEffect(Chrs.LobosJr, SoundType.s_SFX, 777777777)
    ForceAnimation(Chrs.LobosJr, 10)
    Wait(2.0)
    DisableCharacter(Chrs.LobosJr)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11012999: Activate Abyss portal. """
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
    """ 11012950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11012960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
