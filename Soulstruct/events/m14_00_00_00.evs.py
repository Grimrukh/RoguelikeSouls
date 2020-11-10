"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .blighttown_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1403800,
        ItemLots.Boss1Reward,
        1401990, 1401991, 0, 0,  # Exit fog is permanent (exit prompt).
        1000, 1000,
    )

    BossBattle(
        1,
        Chrs.Boss2, Chrs.Boss2Twin, Flags.Boss2IsTwin,
        Regions.Boss2Trigger, Flags.Boss2Dead, 1403802,
        ItemLots.Boss2Reward,
        1401890, 1401891, 0, 0,  # Exit fog is permanent (exit prompt).
        1000, 1000,
    )

    RegisterBonfire(11400992, obj=1401960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11400010, stop_climbing_flag=11400011, obj=1401140)
    RegisterLadder(start_climbing_flag=11400012, stop_climbing_flag=11400013, obj=1401141)
    RegisterLadder(start_climbing_flag=11400014, stop_climbing_flag=11400015, obj=1401142)
    RegisterLadder(start_climbing_flag=11400016, stop_climbing_flag=11400017, obj=1401143)
    RegisterLadder(start_climbing_flag=11400018, stop_climbing_flag=11400019, obj=1401144)
    RegisterLadder(start_climbing_flag=11400020, stop_climbing_flag=11400021, obj=1401145)
    RegisterLadder(start_climbing_flag=11400022, stop_climbing_flag=11400023, obj=1401146)
    RegisterLadder(start_climbing_flag=11400024, stop_climbing_flag=11400025, obj=1401147)
    RegisterLadder(start_climbing_flag=11400026, stop_climbing_flag=11400027, obj=1401148)
    RegisterLadder(start_climbing_flag=11400028, stop_climbing_flag=11400029, obj=1401149)
    RegisterLadder(start_climbing_flag=11400030, stop_climbing_flag=11400031, obj=1401150)
    RegisterLadder(start_climbing_flag=11400032, stop_climbing_flag=11400033, obj=1401151)
    RegisterLadder(start_climbing_flag=11400034, stop_climbing_flag=11400035, obj=1401152)
    RegisterLadder(start_climbing_flag=11400036, stop_climbing_flag=11400037, obj=1401153)
    RegisterLadder(start_climbing_flag=11400038, stop_climbing_flag=11400039, obj=1401154)
    RegisterLadder(start_climbing_flag=11400040, stop_climbing_flag=11400041, obj=1401155)
    RegisterLadder(start_climbing_flag=11400042, stop_climbing_flag=11400043, obj=1401156)
    RegisterLadder(start_climbing_flag=11400044, stop_climbing_flag=11400045, obj=1401157)
    RegisterLadder(start_climbing_flag=11400046, stop_climbing_flag=11400047, obj=1401158)
    RegisterLadder(start_climbing_flag=11400048, stop_climbing_flag=11400049, obj=1401159)
    RegisterLadder(start_climbing_flag=11400050, stop_climbing_flag=11400051, obj=1401160)
    RegisterLadder(start_climbing_flag=11400052, stop_climbing_flag=11400053, obj=1401161)
    RegisterLadder(start_climbing_flag=11400054, stop_climbing_flag=11400055, obj=1401162)
    RegisterLadder(start_climbing_flag=11400056, stop_climbing_flag=11400057, obj=1401163)
    RegisterLadder(start_climbing_flag=11400058, stop_climbing_flag=11400059, obj=1401164)
    RegisterLadder(start_climbing_flag=11400060, stop_climbing_flag=11400061, obj=1401165)
    RegisterLadder(start_climbing_flag=11400062, stop_climbing_flag=11400063, obj=1401166)
    RegisterLadder(start_climbing_flag=11400064, stop_climbing_flag=11400065, obj=1401167)
    RegisterLadder(start_climbing_flag=11400066, stop_climbing_flag=11400067, obj=1401168)
    RegisterLadder(start_climbing_flag=11400068, stop_climbing_flag=11400069, obj=1401169)
    RegisterLadder(start_climbing_flag=11400070, stop_climbing_flag=11400071, obj=1401170)

    DisableObject(1401994)
    DeleteFX(1401995, erase_root_only=False)
    DisableObject(1401996)
    DeleteFX(1401997, erase_root_only=False)
    DisableObject(1401998)
    DeleteFX(1401999, erase_root_only=False)
    DisableObject(1401702)
    DeleteFX(1401703, erase_root_only=False)

    # Wall Hugger dies.
    RunEvent(11400900)

    # Squeaky floors.
    RunEvent(11405100, slot=0, args=(1401000, 1402000, 1402001, 1402002))
    RunEvent(11405110, slot=0, args=(1401002, 1402020, 1402021, 1402022, 1402023, 1402024))

    # Mosquito spawners.
    RunEvent(11400100, slot=0, args=(11405340, 1402200, 1403000))
    RunEvent(11400100, slot=1, args=(11405341, 1402201, 1403001))
    RunEvent(11400100, slot=2, args=(11405342, 1402202, 1403002))

    # Rescue Havel.
    RescueHavel()

    # Mimic.
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # Chests.
    OpenChest(0, 1401650, 11400600)
    OpenChest(1, 1401651, 11400601)
    OpenChest(2, 1401652, 11400602)
    OpenChest(3, 1401653, 11400603)
    OpenChest(4, 1401654, 11400604)

    for enemy in range(100):
        DespawnEnemy(enemy, 1400100 + enemy)

    DepartLevelUnconditional(  # Depths exit
        0, Regions.Exit1Prompt, CommonTexts.DepartLevel, Flags.Exit1Disabled, Flags.Exit1Activated)
    DepartLevelIfFlag(  # Valley exit
        0, Objects.Exit2Prompt, CommonTexts.DepartLevel, Flags.Exit2Disabled, Flags.Boss2Dead, Flags.Exit2Activated)
    DepartLevelUnconditional(  # Great Hollow exit (past first illusory wall)
        1, Regions.Exit3Prompt, CommonTexts.DepartLevel, Flags.Exit3Disabled, Flags.Exit3Activated)
    DepartLevelIfFlag(  # Quelaag exit
        1, Objects.Exit4Prompt, CommonTexts.DepartLevel, Flags.Exit4Disabled, Flags.Boss1Dead, Flags.Exit4Activated)

    # Tarnished Key is not needed in this map, but just for fun.
    GetReward(0, 1400130, CommonItemLots.TarnishedKeyLot, CommonFlags.TarnishedKeyObtained)

    ActivateAbyssPortal(0, 1400997, 1400998)


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


@RestartOnRest
def Event11400900():
    """ 11400900: Event 11400900 """
    SkipLinesIfFlagOff(2, 11400902)
    DisableCharacter(1400000)
    End()
    IfCharacterAlive(1, 1400000)
    SkipLinesIfConditionTrue(2, 1)
    EnableFlag(11400902)
    End()
    DisableNetworkSync()
    IfHealthLessThanOrEqual(0, 1400000, 0.0)
    EnableNetworkSync()
    EzstateAIRequest(1400000, command_id=1200, slot=0)
    AwardItemLot(52400000, host_only=True)  # New reward.
    Restart()


def Event11405100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11405100: Event 11405100 """
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


def Event11405110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11405110: Event 11405110 """
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableNetworkSync()
    IfCharacterOutsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_12_15)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_16_19)
    IfCharacterOutsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableNetworkSync()
    Restart()


def Event11400100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11400100: Event 11400100 """
    SkipLinesIfFlagOn(1, arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableFlag(arg_0_3)
    DisableSpawner(arg_8_11)
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    DisableFlag(arg_0_3)
    EnableSpawner(arg_8_11)
    Restart()


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11400600: Open chest. """
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
    """ 11402080: All-in-one boss event for simplicity. """
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
    """ 11402260: Invasion is triggered. Human not needed. """
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


def DepartLevelUnconditional(_, prompt_region: Region, prompt_text: Text, disabled_flag: Flag,
                             end_trigger_flag: Flag):
    """ 11402200: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlag(_, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
                      end_trigger_flag: Flag):
    """ 11402210: Depart level by interacting with object after a flag is enabled (e.g. boss dead). """
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def GetReward(_, enemy: int, item_lot: int, item_lot_flag: Flag):
    """ 11402270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11403000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11405810: Mimic is activated by the player. """
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
    """ 11405820: Mimic state control. """
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
    """ 11405830: Mimic goes to sleep. """
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
    """ 11405840: Mimic wakes up again. """
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
    """ 11405850: Mimic enters chest form. """
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
    """ 11405860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


@RestartOnRest
def RescueHavel():
    """ 11400850: Rescue Havel on top of shanty. """
    if CommonFlags.HavelRescued:
        DisableCharacter(Chrs.Havel)
        return

    SetTeamType(Chrs.Havel, TeamType.NoTeam)
    EnableInvincibility(Chrs.Havel)

    Await(PlayerWithinDistance(Chrs.Havel, 2.0))

    EnableFlag(CommonFlags.HavelRescued)
    DisplayBattlefieldMessage(CommonTexts.HavelRescued, 0)
    PlaySoundEffect(Chrs.Havel, SoundType.s_SFX, 777777777)
    ForceAnimation(Chrs.Havel, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Havel)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11402999: Activate Abyss portal. """
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
    """ 11402950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11402960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
