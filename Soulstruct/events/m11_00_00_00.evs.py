"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .painted_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1103800,
        ItemLots.Boss1Reward,
        1101990, 1101991, 0, 0,
        1000, 1000,
    )

    RegisterLadder(start_climbing_flag=11100010, stop_climbing_flag=11100011, obj=1101140)
    RegisterLadder(start_climbing_flag=11100014, stop_climbing_flag=11100015, obj=1101142)
    RegisterLadder(start_climbing_flag=11100016, stop_climbing_flag=11100017, obj=1101143)

    DisableObject(1101702)
    DeleteFX(1101703, False)

    # Undead Dragon always goes back to sleep on reload.
    SkipLinesIfClient(1)
    DisableFlag(11100410)

    # Shortcut door.
    RunEvent(11100030)
    RunEvent(11100031)
    GiantDoorSealed()
    TurnSewerWheel()
    RunEvent(11100120, slot=0, args=(11100120, 10010861, 1101250))  # Now requires Tarnished Key.

    RunEvent(11100200)

    # Five chests.
    OpenChest(0, 1101650, 11100600)
    OpenChest(1, 1101651, 11100601)
    OpenChest(2, 1101652, 11100602)
    OpenChest(3, 1101653, 11100603)
    OpenChest(4, 1101654, 11100604)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # TODO: Keep these corpses hanging from ropes. Renumber them to be "extra" item lots?
    RunEvent(11100070, slot=0, args=(1101120, 1101600, 120, 121))
    RunEvent(11100070, slot=1, args=(1101121, 1101601, 125, 126))

    # Undead Dragon stuff.
    SkipLinesIfFlagOff(1, 11100400)
    DisableCharacter(1100170)
    UndeadDragonDeath()
    UndeadDragonAwakens()
    RunEvent(11100100, slot=0, args=(1101180, 1103000))
    RunEvent(11100100, slot=1, args=(1101181, 1103001))
    UndeadDragonWingFallsOff()

    GetReward(0, 1100130, CommonItemLots.PiercingEyeLot, CommonFlags.PiercingEyeObtained)

    for enemy in range(100):
        DespawnEnemy(enemy, 1100100 + enemy)

    ActivateExitDrop()  # Continue to a new level.


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


def Event11100070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11100070: Event 11100070 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_4_7, arg_12_15)
    PostDestruction(arg_0_3, slot=1)
    EnableTreasure(arg_4_7)
    End()
    DisableTreasure(arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectFX(99005, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)


@RestartOnRest
def UndeadDragonAwakens():
    """ 11105370: Event 11105370 """
    SkipLinesIfFlagOff(2, 11100410)
    ResetStandbyAnimationSettings(1100170)
    End()
    IfCharacterType(3, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=3)
    IfCharacterInsideRegion(1, PLAYER, region=1102070)
    IfConditionFalse(2, input_condition=3)
    IfAttacked(2, 1100170, attacking_character=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(11100410)
    ResetStandbyAnimationSettings(1100170)
    ForceAnimation(1100170, 9060)
    PlaySoundEffect(anchor_entity=1102080, sound_type=SoundType.a_Ambient, sound_id=110003420)


@RestartOnRest
def UndeadDragonWingFallsOff():
    """ 11105371: Event 11105371 """
    DisableCharacter(1100172)
    SkipLinesIfThisEventOff(4)
    IfCharacterBackreadEnabled(0, 1100170)
    SetDisplayMask(1100170, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(1100170, bit_index=1, switch_type=OnOffChange.On)
    End()
    IfHasTAEEvent(0, 1100170, tae_event_id=400)
    SetDisplayMask(1100170, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(1100170, bit_index=1, switch_type=OnOffChange.On)
    Move(1100172, destination=1100170, destination_type=CoordEntityType.Character, model_point=30,
         copy_draw_parent=1100170)
    EnableCharacter(1100172)
    ForceAnimation(1100172, 8100, wait_for_completion=True)
    DisableCharacter(1100172)


def Event11100100(_, arg_0_3: int, arg_4_7: int):
    """ 11100100: Event 11100100 """
    SkipLinesIfThisEventSlotOff(4)
    DestroyObject(arg_0_3, slot=1)
    ForceAnimation(arg_0_3, 0)
    DeleteFX(arg_4_7, erase_root_only=False)
    End()
    IfObjectDestroyed(0, arg_0_3)
    DeleteFX(arg_4_7, erase_root_only=True)


@RestartOnRest
def UndeadDragonDeath():
    """ 11100400: Event 11100400 """
    EnableImmortality(1100171)
    EnableInvincibility(1100171)
    DisableHealthBar(1100171)
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1100170)
    End()
    SetBackreadStateAlternate(1100170, state=True)
    DisableGravity(1100170)
    IfCharacterDead(0, 1100170)
    EnableFlag(11100400)


def Event11100030():
    """ 11100030: Event 11100030 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(1101130, 2)
    DisableNavmeshType(1102040, NavmeshType.Solid)
    End()
    EnableNavmeshType(1102040, NavmeshType.Solid)
    IfFlagOff(1, 11100700)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1101130, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1102090, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1101130, 1, wait_for_completion=True)
    DisableNavmeshType(1102040, NavmeshType.Solid)


def Event11100031():
    """ 11100031: Event 11100031 """
    DisableNetworkSync()
    IfFlagOff(1, 11100030)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1101130, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=101, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entity=1101130, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11100120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11100120: Event 11100120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)


def TurnSewerWheel():
    """ 11100135: Event 11100135 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(1101160, 1)
    EndOfAnimation(1101170, 1)
    DisableNavmeshType(1102041, NavmeshType.Solid)
    End()
    IfActionButton(0, prompt_text=10010503, anchor_entity=1101150, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    DisableObject(1101018)
    DisableObject(1101019)
    DisableObject(1101020)
    Move(PLAYER, destination=1101150, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8010)
    ForceAnimation(1101150, 1, wait_for_completion=True)
    SkipLinesIfSingleplayer(2)
    PlayCutscene(110000, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(110000, skippable=True, fade_out=False, player_id=PLAYER)
    ForceAnimation(1101160, 1)
    ForceAnimation(1101170, 1)
    DisableNavmeshType(1102041, NavmeshType.Solid)


def GiantDoorSealed():
    """ 11100136: Event 11100136 """
    DisableNetworkSync()
    IfFlagOff(1, 11100135)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1101170, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010160, anchor_entity=1101170, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11100600: Open chest. """
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
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11102080: All-in-one boss event for simplicity. """
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
    """ 11102260: Invasion is triggered. Human not needed. """
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


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11103000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11105810: Mimic is activated by the player. """
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
    """ 11105820: Mimic state control. """
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
    """ 11105830: Mimic goes to sleep. """
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
    """ 11105840: Mimic wakes up again. """
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
    """ 11105850: Mimic enters chest form. """
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
    """ 11105860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11102270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


def ActivateExitDrop():
    """ 11102200: Exit Painted World after defeating the boss. Continues on to next level, as though you beat
    the level you entered the Painting in. """
    Await(not Flags.Exit2Activated and Flags.Boss1Dead and ActionButton(
        CommonTexts.DepartLevel, Regions.Exit2Prompt, anchor_type=CoordEntityType.Region))
    EnableFlag(Flags.Exit2Activated)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11102950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11102960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
