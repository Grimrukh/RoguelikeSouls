"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .lake_constants import *


def Constructor():
    """ 0: Event 0 """
    # TODO: Speedster offerings in Ash Lake? (Low priority)
    RegisterBonfire(11320992, obj=1321960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11320984, obj=1321970, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    # RegisterLadder(start_climbing_flag=11320010, stop_climbing_flag=11320011, obj=1321140)  # Prompt ladder.
    RegisterLadder(start_climbing_flag=11320012, stop_climbing_flag=11320013, obj=1321141)
    RegisterLadder(start_climbing_flag=11320014, stop_climbing_flag=11320015, obj=1321142)
    RegisterLadder(start_climbing_flag=11320016, stop_climbing_flag=11320017, obj=1321143)
    RegisterStatue(1321900, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321901, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321902, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321903, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321904, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321905, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321906, game_map=ASH_LAKE, statue_type=StatueType.Stone)
    RegisterStatue(1321907, game_map=ASH_LAKE, statue_type=StatueType.Stone)

    DisableObject(1321994)
    DeleteFX(1321995, erase_root_only=False)
    # Fog 1321700 (old checkpoint) not deleted, used as prompt on both sides.

    # Stone Dragon and tail.
    RunEvent(11325000)
    RunEvent(11320800)
    RunEvent(11325001)
    RunEvent(11320200, slot=0, args=(1321200, 11320200))
    RunEvent(11320200, slot=1, args=(1321201, 11320201))
    IllusoryWallInvincible(0, 1321200, 11320200)
    IllusoryWallInvincible(1, 1321201, 11320201)
    RunEvent(11320580)

    # Hydra stuff.
    SkipLinesIfFlagOff(2, 11320100)
    RunEvent(11320100)
    SkipLines(3)
    RunEvent(11320110)
    RunEvent(11320100)
    RunEvent(11325100)
    RunEvent(11320101)

    # Siegmeyer rescue.
    RescueSiegmeyer()

    # Chests.
    OpenChest(0, 1321650, 11320600)
    OpenChest(1, 1321651, 11320601)
    OpenChest(2, 1321652, 11320602)
    OpenChest(3, 1321653, 11320603)
    OpenChest(4, 1321654, 11320604)
    OpenChest(10, 1321660, 11320610)
    OpenChest(11, 1321661, 11320611)
    OpenChest(12, 1321662, 11320612)
    OpenChest(13, 1321663, 11320613)
    OpenChest(14, 1321664, 11320614)

    # Mimics
    OpenMimic(0, Chrs.HollowMimic)
    ControlMimicState(0, Chrs.HollowMimic)
    HitMimicWithTalisman(0, Chrs.HollowMimic)
    TalismanWearsOffMimic(0, Chrs.HollowMimic)
    MimicReturnsToChest(0, Chrs.HollowMimic, Regions.HollowMimicNest)
    ReplanMimicAIOnLoad(0, Chrs.HollowMimic)

    OpenMimic(1, Chrs.LakeMimic)
    ControlMimicState(1, Chrs.LakeMimic)
    HitMimicWithTalisman(1, Chrs.LakeMimic)
    TalismanWearsOffMimic(1, Chrs.LakeMimic)
    MimicReturnsToChest(1, Chrs.LakeMimic, Regions.LakeMimicNest)
    ReplanMimicAIOnLoad(1, Chrs.LakeMimic)

    for enemy in range(100):
        DespawnEnemy(enemy, 1320100 + enemy)
    for enemy in range(100):
        DespawnEnemy(100 + enemy, 1320400 + enemy)

    DepartLevelUnconditional(
        0, Objects.HollowExit1Prompt, CommonTexts.DepartLevel, Flags.HollowExit1Disabled, Flags.HollowExit1Activated,
        CommonFlags.InGreatHollow)
    DepartLevelUnconditional(
        1, Objects.HollowExit2Prompt, CommonTexts.DepartLevel, Flags.HollowExit2Disabled, Flags.HollowExit2Activated,
        CommonFlags.InGreatHollow)
    DepartLevelUnconditional(
        2, Objects.LakeExit1Prompt, CommonTexts.DepartLevel, Flags.LakeExit1Disabled, Flags.LakeExit1Activated,
        CommonFlags.InAshLake)
    DepartLevelUnconditional_Region(
        0, Regions.LakeExit2Prompt, CommonTexts.DepartLevel, Flags.LakeExit2Disabled, Flags.LakeExit2Activated,
        CommonFlags.InAshLake)

    ActivateAbyssPortal(0, 1320997, 1320998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, 6990, 6991, Chrs.HollowInvader, Regions.HollowInvaderTrigger, Flags.HollowInvaderDead)
    InvaderTrigger(1, 6990, 6991, Chrs.LakeInvader, Regions.LakeInvaderTrigger, Flags.LakeInvaderDead)

    # Stone Dragon immortality.
    EnableImmortality(Chrs.StoneDragon)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


@RestartOnRest
def Event11325090():
    """ 11325090: Event 11325090 """
    DisableCharacter(1320900)
    IfBlackWorldTendencyComparison(-1, comparison_type=ComparisonType.GreaterThan, value=50)
    IfFlagOn(-1, 11325090)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11325090)
    EnableCharacter(1320900)
    IfBlackWorldTendencyComparison(0, comparison_type=ComparisonType.LessThanOrEqual, value=50)
    Kill(1320900, award_souls=False)


@RestartOnRest
def Event11320110():
    """ 11320110: Event 11320110 """
    DisableFlag(11325100)
    DisableFlag(11325101)
    DisableCharacter(1320701)
    DisableCharacter(1320702)
    DisableCharacter(1320703)
    DisableCharacter(1320704)
    DisableCharacter(1320705)
    DisableCharacter(1320706)
    DisableCharacter(1320707)
    EndIfFlagOn(11320100)
    RunEvent(11325121)
    RunEvent(11325110, slot=0, args=(1, 3530, 3530, 1320701, 91, 0, 1, 5430), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=1, args=(2, 3531, 3531, 1320702, 92, 1, 2, 5431), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=2, args=(3, 3532, 3532, 1320703, 93, 2, 3, 5432), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=3, args=(4, 3533, 3533, 1320704, 94, 3, 4, 5433), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=4, args=(5, 3534, 3534, 1320705, 95, 4, 5, 5434), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=5, args=(6, 3535, 3535, 1320706, 96, 5, 6, 5435), arg_types='hhiiiBBi')
    RunEvent(11325110, slot=6, args=(8, 3536, 3536, 1320707, 97, 6, 7, 5436), arg_types='hhiiiBBi')


@RestartOnRest
def Event11325100():
    """ 11325100: Event 11325100 """
    IfCharacterBackreadEnabled(1, 1320700)
    IfHasTAEEvent(1, 1320700, tae_event_id=300)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagOn(8, 11325101)
    EnableFlag(11325101)
    Move(1320700, destination=1322700, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1320700, 3011, wait_for_completion=True)
    Move(1320700, destination=1322710, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(1320700, 1322710)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()
    DisableFlag(11325101)
    Move(1320700, destination=1322701, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(1320700, 3014, wait_for_completion=True)
    Move(1320700, destination=1322711, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(1320700, 1322711)
    ForceAnimation(1320700, 9060, wait_for_completion=True)
    ReplanAI(1320700)
    Restart()


@UnknownRestart
def Event11325110(_, arg_0_1: short, arg_2_3: short, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar,
                  arg_17_17: uchar, arg_20_23: int):
    """ 11325110: Event 11325110 """
    SkipLinesIfThisEventSlotOff(4)
    SetDisplayMask(1320700, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, arg_20_23)
    End()
    IfCharacterBackreadEnabled(0, 1320700)
    CreateNPCPart(1320700, npc_part_id=arg_2_3, part_index=arg_0_1, part_health=270, damage_correction=1.0,
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, 1320700, npc_part_id=arg_4_7, value=0)
    IfFlagOff(1, 11325120)
    IfAttacked(1, 1320700, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(2, 1320700, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ResetAnimation(1320700, disable_interpolation=False)
    Move(arg_8_11, destination=1320700, destination_type=CoordEntityType.Character, model_point=arg_12_15,
         copy_draw_parent=1320700)
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 8100)
    ForceAnimation(1320700, 8000)
    SetDisplayMask(1320700, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(1320700, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    AddSpecialEffect(1320700, arg_20_23)


@UnknownRestart
def Event11325121():
    """ 11325121: Event 11325121 """
    IfHasTAEEvent(0, 1320700, tae_event_id=500)
    EnableFlag(11325120)
    IfHasTAEEvent(0, 1320700, tae_event_id=600)
    DisableFlag(11325120)
    Restart()


@RestartOnRest
def Event11320100():
    """ 11320100: Event 11320100 """
    SkipLinesIfThisEventOff(9)
    DisableCharacter(1320700)
    DisableCharacter(1320701)
    DisableCharacter(1320702)
    DisableCharacter(1320703)
    DisableCharacter(1320704)
    DisableCharacter(1320705)
    DisableCharacter(1320706)
    DisableCharacter(1320707)
    End()
    IfCharacterDead(0, 1320700)
    AwardItemLot(35300000, host_only=False)


def Event11320101():
    """ 11320101: Event 11320101 """
    EndIfFlagOn(11320100)
    IfFlagOn(1, 11325110)
    IfFlagOn(1, 11325111)
    IfFlagOn(1, 11325112)
    IfFlagOn(1, 11325113)
    IfFlagOn(1, 11325114)
    IfFlagOn(1, 11325115)
    IfFlagOn(1, 11325116)
    IfConditionTrue(0, input_condition=1)
    Kill(1320700, award_souls=True)


def Event11325000():
    """ 11325000: Event 11325000 """
    EndIfThisEventOn()
    SetStandbyAnimationSettings(Chrs.StoneDragon, standby_animation=9000)
    IfHost(1)
    IfEntityWithinDistance(1, Chrs.StoneDragon, PLAYER, radius=30.0)
    IfConditionTrue(0, input_condition=1)
    SetStandbyAnimationSettings(Chrs.StoneDragon, cancel_animation=9060)


def Event11320800():
    """ 11320800: Event 11320800 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(Chrs.StoneDragon)
    End()
    IfCharacterDead(0, Chrs.StoneDragon)
    EnableFlag(11320800)


@RestartOnRest
def Event11325001():
    """ 11325001: Event 11325001 """
    DisableCharacter(1320801)
    EndIfFlagOn(11320800)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(Chrs.StoneDragon, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Chrs.StoneDragon, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Chrs.StoneDragon, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, Chrs.StoneDragon)
    CreateNPCPart(Chrs.StoneDragon, npc_part_id=3451, part_index=NPCPartType.Part1, part_health=200,
                  damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfCharacterPartHealthLessThanOrEqual(1, Chrs.StoneDragon, npc_part_id=3451, value=0)
    IfHealthLessThanOrEqual(2, Chrs.StoneDragon, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(Chrs.StoneDragon, 8000)
    IfHasTAEEvent(0, Chrs.StoneDragon, tae_event_id=400)
    EnableCharacter(1320801)
    Move(1320801, destination=Chrs.StoneDragon, destination_type=CoordEntityType.Character, model_point=19,
         copy_draw_parent=Chrs.StoneDragon)
    ForceAnimation(1320801, 8100)
    SetDisplayMask(Chrs.StoneDragon, bit_index=0, switch_type=OnOffChange.On)
    SetCollisionMask(Chrs.StoneDragon, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(Chrs.StoneDragon, command_id=20, slot=0)
    ReplanAI(Chrs.StoneDragon)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(34510000, host_only=True)


def Event11320200(_, arg_0_3: int, arg_4_7: int):
    """ 11320200: Event 11320200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(0, arg_0_3)
    EnableFlag(arg_4_7)


def IllusoryWallInvincible(_, wall: int, destroyed_flag: int):
    """ 11320210: Piercing Eye needed. """
    if FlagEnabled(destroyed_flag):
        return
    EnableObjectInvulnerability(wall)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(wall)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11320600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11320580():
    """ 11320580: Event 11320580 """
    IfFlagOn(0, 11325030)
    RotateToFaceEntity(PLAYER, Chrs.StoneDragon)
    ForceAnimation(PLAYER, 7910, wait_for_completion=True)
    ForceAnimation(PLAYER, 7911, loop=True)
    IfFlagOff(0, 11325030)
    ResetStandbyAnimationSettings(PLAYER)
    ForceAnimation(PLAYER, 7912, wait_for_completion=True)
    Restart()


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11322260: Invasion is triggered. Human not needed. """
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
        _, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11322200: Depart level by interacting with prompt. No conditions. """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelUnconditional_Region(
        _, prompt_region: Region, prompt_text: Text, disabled_flag: Flag, end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11322210: Depart level by interacting with prompt. No conditions. """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11323000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11325810: Mimic is activated by the player. """
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
    """ 11325820: Mimic state control. """
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
    """ 11325830: Mimic goes to sleep. """
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
    """ 11325840: Mimic wakes up again. """
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
    """ 11325850: Mimic enters chest form. """
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
    """ 11325860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


@RestartOnRest
def RescueSiegmeyer():
    """ 11320850: Rescue Siegmeyer from Crystal Golem. """
    if CommonFlags.SiegmeyerRescued:
        DisableCharacter(Chrs.Siegmeyer)
        DisableCharacter(Chrs.SiegmeyerGolem)
        return

    SetTeamType(Chrs.Siegmeyer, TeamType.WhitePhantom)
    EnableInvincibility(Chrs.Siegmeyer)
    DisableCharacter(Chrs.Siegmeyer)
    Await(IsDead(Chrs.SiegmeyerGolem))
    EnableFlag(CommonFlags.SiegmeyerRescued)
    EnableCharacter(Chrs.Siegmeyer)
    MoveToEntity(Chrs.Siegmeyer, Chrs.SiegmeyerGolem, model_point=-1)
    PlaySoundEffect(Chrs.Siegmeyer, SoundType.s_SFX, 777777777)
    DisplayBattlefieldMessage(CommonTexts.SiegmeyerRescued, 0)
    ForceAnimation(Chrs.Siegmeyer, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Siegmeyer)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11322999: Activate Abyss portal. """
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
    """ 11322950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11322960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
