"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .darkroot_constants import *


def Constructor():
    """ 0: Event 0 """
    # Sif arena
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1203800,
        ItemLots.Boss1Reward,
        1201990, 1201991, 0, 0,
        1000, 1000,
    )

    RegisterBonfire(11200992, obj=1201960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11200010, stop_climbing_flag=11200011, obj=1201140)
    RegisterLadder(start_climbing_flag=11200012, stop_climbing_flag=11200013, obj=1201141)

    CreateProjectileOwner(1200090)

    SkipLinesIfClient(10)
    DisableObject(1201994)
    DeleteFX(1201995, erase_root_only=False)
    DisableObject(1201996)
    DeleteFX(1201997, erase_root_only=False)
    DisableObject(1201998)
    DeleteFX(1201999, erase_root_only=False)
    DisableObject(1201988)
    DeleteFX(1201989, erase_root_only=False)
    DisableObject(1201986)
    DeleteFX(1201987, erase_root_only=False)
    DisableObject(1201700)
    DeleteFX(1201701, False)

    # Crest door now opens with Holy Sigil.
    RunEvent(11200100, slot=0, args=(11200110, 1201000, 120020, 1202500, 0, 61200500))
    RunEvent(11200110, slot=0, args=(11200100, 1201000, 1202500, 0))

    # Grave arena door.
    RunEvent(11200100, slot=1, args=(11200111, 1201010, 120021, 1202501, 1, 61200501))
    RunEvent(11200110, slot=1, args=(11200101, 1201010, 1202501, 1))

    BreakIllusoryWall()
    IllusoryWallInvincible()

    # Five chests.
    OpenChest(0, 1201650, 11200600)
    OpenChest(1, 1201651, 11200601)
    OpenChest(2, 1201652, 11200602)
    OpenChest(3, 1201653, 11200603)
    OpenChest(4, 1201654, 11200604)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # Butterfly events left alone.
    DisableSoundEvent(1203801)
    SkipLinesIfFlagOff(6, 11200900)
    RunEvent(11205382)
    DisableObject(1201890)
    DeleteFX(1201891, erase_root_only=False)
    DisableObject(1201892)
    DeleteFX(1201893, erase_root_only=False)
    SkipLines(17)
    RunEvent(11205380)
    RunEvent(11205381)
    RunEvent(11205383)
    RunEvent(11205382)
    RunEvent(11200900)
    RunEvent(11205384)
    RunEvent(11205385)
    RunEvent(11205120, slot=0, args=(1202220, 1202180))
    RunEvent(11205120, slot=1, args=(1202221, 1202181))
    RunEvent(11205120, slot=2, args=(1202222, 1202182))
    RunEvent(11205120, slot=3, args=(1202223, 1202183))
    RunEvent(11205120, slot=4, args=(1202224, 1202184))
    RunEvent(11205120, slot=5, args=(1202225, 1202185))
    RunEvent(11205120, slot=6, args=(1202226, 1202186))
    RunEvent(11205120, slot=7, args=(1202227, 1202187))
    RunEvent(11205120, slot=8, args=(1202228, 1202188))
    RunEvent(11205120, slot=9, args=(1202229, 1202189))

    # Hydra stuff (note Hydra ID shifted to 1200810+).
    HydraDeath()
    RunEvent(11205300, slot=0, args=(1, 3530, 3530, 1200811, 91, 0, 1, 5430), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=1, args=(2, 3531, 3531, 1200812, 92, 1, 2, 5431), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=2, args=(3, 3532, 3532, 1200813, 93, 2, 3, 5432), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=3, args=(4, 3533, 3533, 1200814, 94, 3, 4, 5433), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=4, args=(5, 3534, 3534, 1200815, 95, 4, 5, 5434), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=5, args=(6, 3535, 3535, 1200816, 96, 5, 6, 5435), arg_types='hhiiiBBi')
    RunEvent(11205300, slot=6, args=(8, 3536, 3536, 1200817, 97, 6, 7, 5436), arg_types='hhiiiBBi')

    # Rescue Logan.
    RescueLogan()

    for enemy in range(100):
        DespawnEnemy(enemy, 1200100 + enemy)

    GetReward(0, 1200130, CommonItemLots.RustedKeyLot)
    GetReward(1, 1200131, CommonItemLots.HolySigilLot)
    GetReward(2, 1200131, CommonItemLots.HolySigilLot)

    DepartLevelWithKey_Object(
        0, Objects.Exit1Prompt, CommonTexts.DepartLevel, CommonTexts.RustedKeyRequired,
        Flags.Exit1Disabled, CommonGoods.RustedKey, Flags.Exit1Activated)

    DepartLevelIfFlagWithFailure_Object(
        0, Objects.Exit2Prompt, CommonTexts.DepartLevel, CommonTexts.ButterflyMustBeDefeated,
        Flags.Exit2Disabled, Flags.ButterflyDead, Flags.Exit2Activated)

    DepartLevelWithKey_Region(
        0, Regions.Exit3Prompt, CommonTexts.DepartLevel, CommonTexts.HolySigilRequired,
        Flags.Exit3Disabled, CommonGoods.HolySigil, Flags.Exit3Activated)

    DepartLevelIfFlag_Region(
        0, Regions.Exit4Prompt, CommonTexts.DepartLevel, Flags.Exit4Disabled, Flags.Boss1Dead,
        Flags.Exit4Activated)

    ActivateAbyssPortal(0, 1200997, 1200998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, Chrs.Invader, Regions.InvaderSpawnPoint, Regions.InvaderTrigger,
                   Flags.InvaderSummoned, Flags.InvaderDismissed, Flags.InvaderDead)
    InvaderKilled(0, Chrs.Invader, Flags.InvaderDead)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


def Event11205380():
    """ 11205380: Event 11205380 """
    IfFlagOff(1, 11200900)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202898, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=1201890, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205381():
    """ 11205381: Event 11205381 """
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205383)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfDialogPromptActivated(1, prompt_text=10010403, anchor_entity=1202898, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=1201890)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1202894)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11205383():
    """ 11205383: Event 11205383 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11200900)
    IfCharacterInsideRegion(1, PLAYER, region=1202896)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    AddSpecialEffect(PLAYER, 5500)


@RestartOnRest
def Event11205382():
    """ 11205382: Event 11205382 """
    DisableCharacter(1200090)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(Chrs.MoonlightButterfly, UpdateAuthority.Forced)
    SkipLinesIfFlagOff(3, Flags.ButterflyDead)
    DisableCharacter(Chrs.MoonlightButterfly)
    Kill(Chrs.MoonlightButterfly, award_souls=False)
    End()
    DisableHealthBar(Chrs.MoonlightButterfly)
    DisableAI(Chrs.MoonlightButterfly)
    SetStandbyAnimationSettings(Chrs.MoonlightButterfly, standby_animation=7000)
    IfFlagOn(0, 11205383)
    SetStandbyAnimationSettings(Chrs.MoonlightButterfly, cancel_animation=7001)
    EnableAI(Chrs.MoonlightButterfly)
    EnableBossHealthBar(Chrs.MoonlightButterfly, name=3230, slot=0)


def Event11200900():
    """ 11200900: Event 11200900 """
    IfCharacterDead(0, Chrs.MoonlightButterfly)
    CancelSpecialEffect(PLAYER, 5500)
    EnableFlag(11200900)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableBossHealthBar(Chrs.MoonlightButterfly, name=3230, slot=0)
    DisableObject(1201890)
    DeleteFX(1201891, erase_root_only=True)
    DisableObject(1201892)
    DeleteFX(1201893, erase_root_only=True)
    AwardItemLot(32300000)


def Event11205384():
    """ 11205384: Event 11205384 """
    DisableNetworkSync()
    IfFlagOff(1, 11200900)
    IfFlagOn(1, 11205382)
    SkipLinesIfHost(1)
    IfFlagOn(1, 11205381)
    IfCharacterInsideRegion(1, PLAYER, region=1202890)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1203801)


def Event11205385():
    """ 11205385: Event 11205385 """
    DisableNetworkSync()
    IfFlagOn(1, 11200900)
    IfFlagOn(1, 11205384)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1203801)


def Event11205120(_, arg_0_3: int, arg_4_7: int):
    """ 11205120: Event 11205120 """
    IfCharacterInsideRegion(1, Chrs.MoonlightButterfly, region=arg_0_3)
    IfHasTAEEvent(1, Chrs.MoonlightButterfly, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(Chrs.MoonlightButterfly, destination=arg_4_7, destination_type=CoordEntityType.Region, model_point=-1,
         short_move=True)
    IfDoesNotHaveTAEEvent(0, Chrs.MoonlightButterfly, tae_event_id=10)
    Restart()


def Event11200100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11200100: Event 11200100 """
    SkipLinesIfFlagOn(1, arg_20_23)
    SkipLinesIfThisEventSlotOff(2)
    EndOfAnimation(arg_4_7, 1)
    End()
    CreateObjectFX(arg_8_11, obj=arg_4_7, model_point=200)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    IfPlayerHasGood(1, CommonGoods.HolySigil, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=True, line_intersects=arg_4_7, 
                            boss_version=True)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_20_23)
    RotateToFaceEntity(PLAYER, arg_4_7)
    ForceAnimation(PLAYER, 7114, wait_for_completion=True)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    SkipLinesIfClient(1)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisplayDialog(10010861, anchor_entity=arg_4_7, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    ForceAnimation(arg_4_7, 1)
    DeleteObjectFX(arg_4_7, erase_root=True)


def Event11200110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11200110: Event 11200110 """
    DisableNetworkSync()
    IfFlagOn(-1, arg_0_3)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    IfFlagOn(1, 703)
    SkipLinesIfEqual(1, left=arg_12_15, right=1)
    IfPlayerDoesNotHaveGood(1, CommonGoods.HolySigil, including_box=False)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=arg_4_7)
    IfClient(2)
    IfDialogPromptActivated(2, prompt_text=10010400, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Region, 
                            facing_angle=0.0, max_distance=0.0, human_or_hollow_only=False, line_intersects=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(arg_0_3)
    DisplayDialog(10010160, anchor_entity=arg_4_7, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def BreakIllusoryWall():
    """ 11200120: Event 11200120 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1201300)
    End()
    IfObjectDestroyed(0, 1201300)
    EnableFlag(11200120)


def IllusoryWallInvincible():
    """ 11200121: Piercing Eye needed. """
    if FlagEnabled(11210120):
        return
    EnableObjectInvulnerability(1201300)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1201300)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


@RestartOnRest
def RescueLogan():
    """ 11200122: Break illusory wall. """
    if CommonFlags.LoganRescued:
        DisableCharacter(Chrs.Logan)
        return
    SetTeamType(Chrs.Logan, TeamType.WhitePhantom)
    EnableInvincibility(Chrs.Logan)
    ForceAnimation(Chrs.Logan, 7830, loop=True)  # sitting
    Await(FlagEnabled(11200120))
    EnableFlag(CommonFlags.LoganRescued)
    PlaySoundEffect(Chrs.Logan, SoundType.s_SFX, 777777777)
    DisplayBattlefieldMessage(CommonTexts.LoganRescued, 0)
    ForceAnimation(Chrs.Logan, 7712, wait_for_completion=True)
    Wait(2.0)
    ForceAnimation(Chrs.Logan, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Logan)


@RestartOnRest
def HydraDeath():
    """ 11200801: Event 11200801 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Chrs.Hydra)
    End()
    IfCharacterDead(-1, Chrs.Hydra)
    IfCharacterDead(1, 1200811)
    IfCharacterDead(1, 1200812)
    IfCharacterDead(1, 1200813)
    IfCharacterDead(1, 1200814)
    IfCharacterDead(1, 1200815)
    IfCharacterDead(1, 1200816)
    IfCharacterDead(1, 1200817)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Kill(Chrs.Hydra, award_souls=True)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(35300100, host_only=True)  # Piercing Eye


@RestartOnRest
def HydraHeadCut(_, arg_0_1: short, arg_2_3: short, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar,
                 arg_17_17: uchar, arg_20_23: int):
    """ 11205300: Event 11205300 """
    DisableCharacter(arg_8_11)
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(Chrs.Hydra, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Chrs.Hydra, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Chrs.Hydra, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, Chrs.Hydra)
    CreateNPCPart(Chrs.Hydra, npc_part_id=arg_2_3, part_index=arg_0_1, part_health=176, damage_correction=1.0,
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, Chrs.Hydra, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, Chrs.Hydra, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(Chrs.Hydra, disable_interpolation=False)
    Move(arg_8_11, destination=Chrs.Hydra, destination_type=CoordEntityType.Character, model_point=arg_12_15,
         copy_draw_parent=Chrs.Hydra)
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(Chrs.Hydra, 8000)
    SetDisplayMask(Chrs.Hydra, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(Chrs.Hydra, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(Chrs.Hydra, arg_20_23)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11200600: Open chest. """
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
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLot,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11202080: All-in-one boss event for simplicity. """
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


def InvaderTrigger(_, invader: Character, spawn_point: Region, trigger: Region,
                   summoned_flag: Flag, dismissed_flag: Flag, dead_flag: Flag, ):
    """ 11205200: Invasion is triggered. Human not needed. """
    DisableNetworkSync()
    EndIfFlagOn(summoned_flag)
    IfHost(1)
    IfFlagOff(1, dead_flag)
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(1, PLAYER, region=trigger)
    IfConditionTrue(0, input_condition=1)
    PlaceSummonSign(SummonSignType.BlackEyeSign, invader, region=spawn_point,
                    summon_flag=summoned_flag, dismissal_flag=dismissed_flag)
    Wait(20.0)
    Restart()


def InvaderKilled(_, invader: Character, dead_flag: Flag):
    """ 11202260: Invader in this map has been killed. Also disables them on startup. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    Await(IsDead(invader))
    EnableFlag(dead_flag)


def DepartLevelWithKey_Region(
        _, prompt_region: Region, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
        key: Good, end_trigger_flag: Flag):
    """ 11202200: Depart level by interacting with prompt with key in inventory. """
    if not FlagEnabled(CommonFlags.InDarkroot):
        return
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and DialogPromptActivated(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and DialogPromptActivated(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0), hold=True)
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
        key: Good, end_trigger_flag: Flag):
    """ 11202205: Depart level by interacting with prompt with key in inventory. """
    if not FlagEnabled(CommonFlags.InDarkroot):
        return
    if FlagEnabled(disabled_flag):
        return

    activate_with_key = Condition(FlagDisabled(disabled_flag) and HasGood(key)
                                  and DialogPromptActivated(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0), hold=True)
    activate_without_key = Condition(FlagDisabled(disabled_flag) and not HasGood(key)
                                     and DialogPromptActivated(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0), hold=True)
    Await(activate_with_key or activate_without_key)
    if activate_with_key:
        EnableFlag(end_trigger_flag)
        DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def DepartLevelIfFlag_Region(
        _, prompt_region: Region, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
        end_trigger_flag: Flag):
    """ 11202210: Depart level by interacting with region after a flag is enabled (e.g. boss dead). """
    if not FlagEnabled(CommonFlags.InDarkroot):
        return
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and DialogPromptActivated(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlagWithFailure_Object(
        _, prompt_object: Object, prompt_text: Text, failure_text: Text,
        disabled_flag: Flag, required_flag: Flag, end_trigger_flag: Flag):
    """ 11202220: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    if not FlagEnabled(CommonFlags.InDarkroot):
        return
    activate_with_flag = Condition(
        FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and DialogPromptActivated(
            prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0),
        hold=True)
    activate_without_flag = Condition(
        FlagDisabled(disabled_flag) and not required_flag and DialogPromptActivated(
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
    """ 11203000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11205810: Mimic is activated by the player. """
    IfHealthGreaterThan(1, mimic, 0.0)
    IfCharacterBackreadEnabled(1, mimic)
    IfCharacterHasSpecialEffect(1, mimic, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfDialogPromptActivated(1, prompt_text=10010400, anchor_entity=mimic, anchor_type=CoordEntityType.Character,
                            facing_angle=45.0, max_distance=1.2000000476837158, model_point=7,
                            human_or_hollow_only=False)
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
    """ 11205820: Mimic state control. """
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
    """ 11205830: Mimic goes to sleep. """
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
    """ 11205840: Mimic wakes up again. """
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
    """ 11205850: Mimic enters chest form. """
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
    """ 11205860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLot):
    """ 11202270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11202999: Activate Abyss portal. """
    if CommonFlags.DisableAbyssPortal:
        DeleteFX(fx_id, erase_root_only=False)
        return
    Await(DialogPromptActivated(
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
    """ 11202950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11202960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
