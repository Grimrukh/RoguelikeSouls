"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from common_constants import *
from depths_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1003800,
        ItemLots.Boss1Reward,  # Overwritten by mod.
        1001990, 1001991, 0, 0,  # No exit fog.
        1000, 1000,
    )

    RegisterBonfire(11000992, obj=1001960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11000010, stop_climbing_flag=11000011, obj=1001140)
    RegisterStatue(1001900, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001901, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001902, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001903, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001904, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001905, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001906, game_map=DEPTHS, statue_type=StatueType.Stone)
    RegisterStatue(1001907, game_map=DEPTHS, statue_type=StatueType.Stone)

    DisableObject(1001994)
    DeleteVFX(1001995, erase_root_only=False)
    DisableObject(1001996)
    DeleteVFX(1001997, erase_root_only=False)
    DisableObject(1001700)  # Old checkpoint fog
    DeleteVFX(1001701, False)

    # Shortcut door
    SkipLinesIfFlagOff(1, 11000100)
    EndOfAnimation(1001319, 0)
    OpenShortcutDoor()
    OpenShortcutDoor_WrongSide()

    # Old bonfire chamber door now opens with Rusted Key. (Giant Key can't appear in there.)
    OpenBonfireChamberDoor(0, 11000120, 10010877, 1001315, 10010883, CommonGoods.RustedKey)

    # Five chests.
    OpenChest(0, 1001650, 11000600)
    OpenChest(1, 1001651, 11000601)
    OpenChest(2, 1001652, 11000602)
    OpenChest(3, 1001653, 11000603)
    OpenChest(4, 1001654, 11000604)

    # Tiny rats running away.
    TinyRatRun(0, 1001000, 1001000, 1)
    TinyRatRun(1, 1001001, 1001001, 1)
    TinyRatRun(2, 1001002, 1001002, 3)

    GetReward(0, 1000130, CommonItemLots.GiantKeyLot, CommonFlags.GiantKeyObtained)

    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    for enemy in range(100):
        DespawnEnemy(enemy, 1000100 + enemy)

    DepartLevelUnconditional(0, Regions.Exit1Prompt, CommonTexts.DepartLevel,
                             Flags.Exit1Disabled, Flags.Exit1Activated)
    DepartLevelIfFlag(0, Regions.Exit2Prompt, CommonTexts.DepartLevel, Flags.Exit2Disabled,
                      Flags.Boss1Dead, Flags.Exit2Activated)
    DepartLevelWithKey(0, Regions.Exit3Prompt, CommonTexts.DepartLevel, CommonTexts.GiantKeyRequired,
                       Flags.Exit3Disabled, CommonGoods.GiantKey, Flags.Exit3Activated)

    ActivateAbyssPortal(0, 1000997, 1000998)


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


def TinyRatRun(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11005000: Event 11005000 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_4_7)
    End()
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=3.0)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    DisableObject(arg_4_7)


def OpenShortcutDoor():
    """ 11000100: Event 11000100 """
    IfFlagOff(1, 11000100)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1001319, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=101, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1001319, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1001319, 0)


def OpenShortcutDoor_WrongSide():
    """ 11000101: Event 11000101 """
    DisableNetworkSync()
    IfFlagOff(1, 11000100)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1001319, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entity=1001319, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def OpenBonfireChamberDoor(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11000120: Event 11000120 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EndIfClient()
    IfPlayerHasGood(1, arg_16_19, including_box=False)
    SkipLinesIfConditionTrue(2, 1)
    DisplayDialog(arg_12_15, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)
    SkipLines(1)
    DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                  number_buttons=NumberButtons.NoButton)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11000600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


# def AllyAssistance(_, available: Flag, done: Flag):
#     """ 11002250: Ally appears to help you (once per run, if rolled) against a given boss. """
#     DisableCharacter(Chrs.Ally)
#     if not available:
#         return
#     if done:
#         return
#     Await(CommonFlags.LifeCount1)
#     Wait(5.0)
#     EnableCharacter(Chrs.Ally)
#     ForceAnimation(Chrs.Ally, 10)  # fade in
#     EnableFlag(done)


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11002260: Invasion is triggered. Human not needed. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    IfHost(1)
    IfFlagOff(1, dead_flag)
    IfCharacterInsideRegion(1, PLAYER, region=trigger)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableCharacter(invader)
    DisplayBattlefieldMessage(invasion_message, 0)
    ForceAnimation(invader, PlayerAnimations.SummonSpawn, wait_for_completion=True)
    ReplanAI(invader)
    SetTeamType(invader, TeamType.BlackPhantom)

    # TODO: If player dies while invader is active (two possible outcomes here), give them a Black Eye Orb and register
    #  future possible vengeance invasion by checking that flag in the run manager.
    Await(IsDead(invader))

    DisplayBattlefieldMessage(dead_message, 0)
    EnableFlag(dead_flag)


def DepartLevelUnconditional(_, prompt_region: Region, prompt_text: Text, disabled_flag: Flag,
                             end_trigger_flag: Flag):
    """ 11002200: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(prompt_text, prompt_region,
                                                       anchor_type=CoordEntityType.Region))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelWithKey(_, prompt_region: Region, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
                       key: GoodParam, end_trigger_flag: Flag):
    """ 11002210: Depart level by interacting with prompt with key in inventory. """
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


def DepartLevelIfFlag(_, prompt_region: Region, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
                      end_trigger_flag: Flag):
    """ 11002220: Depart level by interacting with prompt after boss is defeated. """
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11002080: All-in-one boss event for simplicity. """
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


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11003000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11005810: Mimic is activated by the player. """
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
    """ 11005820: Mimic state control. """
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
    """ 11005830: Mimic goes to sleep. """
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
    """ 11005840: Mimic wakes up again. """
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
    """ 11005850: Mimic enters chest form. """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, mimic, region=mimic_nest)
    IfCharacterBackreadDisabled(1, mimic)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(mimic, 5421)
    ClearTargetList(mimic)
    ReplanAI(mimic)
    Move(mimic, destination=mimic_nest, destination_type=CoordEntityType.Region, short_move=True, model_point=-1)
    IfCharacterBackreadEnabled(0, mimic)
    Restart()


@RestartOnRest
def ReplanMimicAIOnLoad(_, mimic: int):
    """ 11005860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11002270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11002999: Activate Abyss portal. """
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


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11002950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11002960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
