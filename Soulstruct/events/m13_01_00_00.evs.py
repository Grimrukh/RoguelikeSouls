"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .tomb_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattle(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1313800,
        ItemLots.Boss1Reward,
        1311990, 1311991, 0, 0,
        1000, 1000,
    )

    RegisterBonfire(11310992, obj=1311960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11310010, stop_climbing_flag=11310011, obj=1311140)
    RegisterLadder(start_climbing_flag=11310012, stop_climbing_flag=11310013, obj=1311141)
    RegisterLadder(start_climbing_flag=11310014, stop_climbing_flag=11310015, obj=1311142)
    RegisterLadder(start_climbing_flag=11310016, stop_climbing_flag=11310017, obj=1311143)
    RegisterLadder(start_climbing_flag=11310018, stop_climbing_flag=11310019, obj=1311144)
    RegisterLadder(start_climbing_flag=11310020, stop_climbing_flag=11310021, obj=1311145)
    RegisterLadder(start_climbing_flag=11310022, stop_climbing_flag=11310023, obj=1311146)
    RegisterLadder(start_climbing_flag=11310024, stop_climbing_flag=11310025, obj=1311147)
    RegisterLadder(start_climbing_flag=11310026, stop_climbing_flag=11310027, obj=1311148)

    DisableFlag(401)  # Invasions allowed.
    EnableFlag(11310095)  # Golden fog gone.
    DisableObject(1311710)
    DeleteFX(1311711, erase_root_only=False)

    # Giant fog (1311994, 1311995) blocks return to Catacombs.
    DisableObject(1311700)
    DeleteFX(1311701, erase_root_only=False)

    # Light ball control.
    LightBallControl()

    # Disable Nito coffin stuff.
    DisableCharacter(1310810)
    DisableObject(1311300)
    DisableObjectActivation(1311300, obj_act_id=-1)

    BreakIllusoryWall()
    IllusoryWallInvincible()

    # Chests.
    OpenChest(0, 1311650, 11310600)
    OpenChest(1, 1311651, 11310601)
    OpenChest(2, 1311652, 11310602)
    OpenChest(3, 1311653, 11310603)
    OpenChest(4, 1311654, 11310604)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # Despawn rare/red phantom enemies.
    for enemy in range(100):
        DespawnEnemy(enemy, 1310100 + enemy)

    # Too lazy to add a permanent item corpse to the pit with the Piercing Eye. Player can use a Homeward Bone.
    # But I will add the Piercing Eye to an enemy.
    GetReward(0, 1310130, CommonItemLots.PiercingEyeLot, CommonFlags.PiercingEyeObtained)

    # Only one exit prompt.
    ActivateExitBonfire()

    ActivateAbyssPortal(0, 1310997, 1310998)


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
def LightBallControl():
    """ 11315100: Event 11315100 """
    RunEvent(11315091)
    RunEvent(11315092)
    RunEvent(11315150, slot=0, args=(11315100, 1313200, 11315101))
    RunEvent(11315150, slot=1, args=(11315101, 1313201, 11315102))
    RunEvent(11315150, slot=2, args=(11315102, 1313202, 11315103))
    RunEvent(11315150, slot=3, args=(11315103, 1313203, 11315104))
    RunEvent(11315150, slot=4, args=(11315104, 1313204, 11315105))
    RunEvent(11315150, slot=5, args=(11315105, 1313205, 11315106))
    RunEvent(11315150, slot=6, args=(11315106, 1313206, 11315107))
    RunEvent(11315150, slot=7, args=(11315107, 1313207, 11315108))
    RunEvent(11315150, slot=8, args=(11315108, 1313208, 11315109))
    RunEvent(11315150, slot=9, args=(11315109, 1313209, 11315110))
    RunEvent(11315150, slot=10, args=(11315110, 1313210, 11315111))
    RunEvent(11315150, slot=11, args=(11315111, 1313211, 11315112))
    RunEvent(11315150, slot=12, args=(11315112, 1313212, 11315113))
    RunEvent(11315150, slot=13, args=(11315113, 1313213, 11315114))
    RunEvent(11315150, slot=14, args=(11315114, 1313214, 11315115))
    RunEvent(11315150, slot=15, args=(11315115, 1313215, 11315116))
    RunEvent(11315150, slot=16, args=(11315116, 1313216, 11315117))
    RunEvent(11315150, slot=17, args=(11315117, 1313217, 11315118))
    RunEvent(11315150, slot=18, args=(11315118, 1313218, 11315119))
    RunEvent(11315150, slot=19, args=(11315119, 1313219, 11315120))
    RunEvent(11315150, slot=20, args=(11315120, 1313220, 11315121))
    RunEvent(11315150, slot=21, args=(11315121, 1313221, 11315122))
    RunEvent(11315150, slot=22, args=(11315122, 1313222, 11315123))
    RunEvent(11315150, slot=23, args=(11315123, 1313223, 11315124))
    RunEvent(11315150, slot=24, args=(11315100, 1313224, 11315125))
    RunEvent(11315150, slot=25, args=(11315125, 1313225, 11315126))
    RunEvent(11315150, slot=26, args=(11315126, 1313226, 11315127))
    RunEvent(11315150, slot=27, args=(11315127, 1313227, 11315128))
    RunEvent(11315150, slot=28, args=(11315128, 1313228, 11315129))
    RunEvent(11315150, slot=29, args=(11315129, 1313229, 11315130))
    RunEvent(11315150, slot=30, args=(11315130, 1313230, 11315131))
    RunEvent(11315150, slot=31, args=(11315131, 1313231, 11315132))
    RunEvent(11315150, slot=32, args=(11315132, 1313232, 11315133))
    RunEvent(11315150, slot=33, args=(11315133, 1313233, 11315134))
    RunEvent(11315150, slot=34, args=(11315134, 1313234, 11315135))
    RunEvent(11315150, slot=35, args=(11315135, 1313235, 11315136))
    RunEvent(11315150, slot=36, args=(11315136, 1313236, 11315137))
    RunEvent(11315150, slot=37, args=(11315137, 1313237, 11315138))
    RunEvent(11315150, slot=38, args=(11315138, 1313238, 11315139))
    RunEvent(11315150, slot=39, args=(11315139, 1313239, 11315140))
    RunEvent(11315150, slot=40, args=(11315140, 1313240, 11315141))
    RunEvent(11315150, slot=41, args=(11315141, 1313241, 11315142))
    RunEvent(11315150, slot=42, args=(11315142, 1313242, 11315143))
    RunEvent(11315150, slot=43, args=(11315143, 1313243, 11315144))
    RunEvent(11315150, slot=44, args=(11315144, 1313244, 11315145))
    RunEvent(11315150, slot=45, args=(11315145, 1313245, 11315146))
    RunEvent(11315150, slot=46, args=(11315146, 1313246, 11315147))
    RunEvent(11315150, slot=47, args=(11315147, 1313247, 11315148))
    RunEvent(11315150, slot=48, args=(11315148, 1313248, 11315149))


@UnknownRestart
def Event11315150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11315150: Event 11315150 """
    DisableNetworkSync()
    SkipLinesIfFlagOn(4, 11315090)
    DeleteFX(arg_4_7, erase_root_only=False)
    IfFlagOn(1, 11315090)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    CreateFX(arg_4_7)
    EnableFlag(arg_8_11)
    IfFlagOff(0, 11315090)
    DeleteFX(arg_4_7, erase_root_only=True)
    DisableFlag(arg_8_11)
    Restart()


@UnknownRestart
def Event11315091():
    """ 11315091: Event 11315091 """
    IfSkullLanternActive(1)
    IfTimeElapsed(1, 2.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11315090)
    RestartEvent(11315092, slot=0)
    Restart()


@UnknownRestart
def Event11315092():
    """ 11315092: Event 11315092 """
    DisableNetworkSync()
    IfFlagOn(0, 11315090)
    Wait(3.0)
    DisableFlag(11315090)
    Restart()


def BreakIllusoryWall():
    """ 11310100: Event 11310100 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1311400)
    End()
    IfObjectDestroyed(0, 1311400)
    End()


def IllusoryWallInvincible():
    """ 11310101: Piercing Eye needed. """
    if FlagEnabled(11310100):
        return
    EnableObjectInvulnerability(1311400)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1311400)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: int,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11312080: All-in-one boss event for simplicity. """
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


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11310600: Open chest. """
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
def DespawnEnemy(_, enemy: int):
    """ 11313000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11315810: Mimic is activated by the player. """
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
    """ 11315820: Mimic state control. """
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
    """ 11315830: Mimic goes to sleep. """
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
    """ 11315840: Mimic wakes up again. """
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
    """ 11315850: Mimic enters chest form. """
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
    """ 11315860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: int, item_lot_flag: Flag):
    """ 11312270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11312999: Activate Abyss portal. """
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


def ActivateExitBonfire():
    """ 11312200: Defeat boss to make bonfire appear and finish level. """
    if not Flags.Boss1Dead:
        DisableObject(Objects.Exit2Prompt)
        Await(Flags.Boss1Dead)
        CreateTemporaryFX(90014, anchor_entity=Objects.Exit2Prompt, anchor_type=CoordEntityType.Object, model_point=-1)
        Wait(4.0)  # Give banner time.
        EnableObject(Objects.Exit2Prompt)
        if not CommonFlags.TombBossDefeated:
            if CommonFlags.LordvesselObtained:
                DisplayStatus(CommonTexts.MoreTreasureUnlocked)
                EnableFlag(CommonFlags.TombBossDefeated)
            else:
                DisplayStatus(CommonTexts.LordvesselNotObtained)

    if FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 3) or CommonFlags.KilnAvailable:
        # Go to Chasm or Kiln (mod will figure out which).
        Await(not Flags.Exit2Disabled and ActionButton(CommonTexts.DepartLevel, Objects.Exit2Prompt,
                                                       max_distance=2.0))
        EnableFlag(Flags.Exit2Activated)
    else:
        # Go back to Firelink.
        Await(not Flags.Exit2Disabled and ActionButton(
            CommonTexts.ReturnToFirelink, Objects.Exit2Prompt, max_distance=2.0))
        AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11312950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11312960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
