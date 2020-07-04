"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .archives_constants import *


def Constructor():
    """ 0: Event 0 """
    # Tower battle (for Mornstein, not an exit)
    BossBattleExtraFog(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1703801,
        ItemLots.Boss1Reward,
        1701890, 1701891, 1701892, 1701893,
        1000, 1000,
        1701894, 1701895,  # extra fog
    )

    # Cave battle
    BossBattle(
        0,
        Chrs.Boss2, Chrs.Boss2Twin, Flags.Boss2IsTwin,
        Regions.Boss2Trigger, Flags.Boss2Dead, 1703800,
        ItemLots.Boss2Reward,
        1701990, 1701991, 0, 0,  # No exit fog.
        1000, 1000,
    )

    RegisterBonfire(11700992, obj=1701960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11700010, stop_climbing_flag=11700011, obj=1701140)
    RegisterLadder(start_climbing_flag=11700012, stop_climbing_flag=11700013, obj=1701141)
    RegisterLadder(start_climbing_flag=11700014, stop_climbing_flag=11700015, obj=1701142)
    RegisterLadder(start_climbing_flag=11700016, stop_climbing_flag=11700017, obj=1701143)
    RegisterStatue(1701900, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701901, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701902, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701903, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701904, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701905, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701906, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)
    RegisterStatue(1701907, game_map=DUKES_ARCHIVES, statue_type=StatueType.Crystal)

    DisableObject(1701994)
    DeleteFX(1701995, erase_root_only=False)
    DisableObject(1701996)
    DeleteFX(1701997, erase_root_only=False)

    # TODO: Confirm it's fine to leave flag 61700105 off (alarm).
    DisableObject(1701706)
    DeleteFX(1701707)
    DisableSoundEvent(1703500)  # Disable alarm sound.

    # Golden fog (1701710/1701711) left on with no prompt.
    # Crystal mass in tower deleted.

    # Descending stairs before garden.
    RunEvent(11700110)
    # Moving bookshelves (to garden).
    RunEvent(11700120, slot=0, args=(11700120, 1701120, 1701121, 0, 0))
    # "Shortcut" moving bookshelf is automatically moved.
    EndOfAnimation(1701125, 1)
    # Elevators.
    RunEvent(11700160, slot=0, args=(11700100, 1701100, 11700210, 11700211, 11705090, 11705180, 11705181))
    RunEvent(11700105, slot=0, args=(11700100, 1701100, 1701101, 1701102, 11705090, 11705180, 11705181))
    RunEvent(11700160, slot=1, args=(11700102, 1701130, 11700220, 11700221, 11705091, 11705182, 11705183))
    RunEvent(11700105, slot=2, args=(11700102, 1701130, 1701131, 1701132, 11705091, 11705182, 11705183))
    RunEvent(11700090, slot=0, args=(11700100, 0, 1701101, 11705090), arg_types='iBii')
    RunEvent(11700090, slot=1, args=(11700100, 1, 1701102, 11705090), arg_types='iBii')
    RunEvent(11700090, slot=2, args=(11700102, 0, 1701131, 11705091), arg_types='iBii')
    RunEvent(11700090, slot=3, args=(11700102, 1, 1701132, 11705091), arg_types='iBii')

    # Rotating staircases.
    RunEvent(11705150, slot=0, args=(11700205, 1701200, 1701210))
    RunEvent(11700200, slot=0, args=(11700205, 1701200, 1701201, 1703200, 1703201, 1703010, 1703011, 11705151))
    RunEvent(11700200, slot=1, args=(11700205, 1701210, 1701211, 1703210, 1703211, 1703012, 1703013, 11705152))

    # Wall hitboxes on elevators.
    RunEvent(11700150, slot=0, args=(1703100, 1702780))
    RunEvent(11700150, slot=1, args=(1703101, 1702781))

    # Prison doors (leaving).
    RunEvent(11700300, slot=0, args=(11700300, 10010863, 1701500))
    RunEvent(11700300, slot=1, args=(11700311, 10010879, 1701501))
    RunEvent(11700300, slot=2, args=(11700302, 10010863, 1701502))
    RunEvent(11700300, slot=3, args=(11700313, 10010879, 1701503))
    RunEvent(11700300, slot=4, args=(11700304, 10010863, 1701504))
    RunEvent(11700300, slot=5, args=(11700305, 10010863, 1701505))
    RunEvent(11700300, slot=6, args=(11700320, 10010865, 1701506))

    CaveBossImmortality()

    # Butterfly stuff.
    RunEvent(11705160, slot=0, args=(1700350, 3.0), arg_types='if')
    RunEvent(11705160, slot=1, args=(1700351, 3.0), arg_types='if')
    RunEvent(11705160, slot=2, args=(1700352, 10.0), arg_types='if')
    RunEvent(11705280, slot=0, args=(1700350, 32300100))  # Both rewards are Crystal Embers.
    RunEvent(11705280, slot=1, args=(1700351, 32300110))

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # No keys dropped in this map.

    # Five chests.
    OpenChest(0, 1701650, 11700600)
    OpenChest(1, 1701651, 11700601)
    OpenChest(2, 1701652, 11700602)
    OpenChest(3, 1701653, 11700603)
    OpenChest(4, 1701654, 11700604)

    # Despawn rare/red phantom enemies.
    for enemy in range(100):
        DespawnEnemy(enemy, 1700100 + enemy)

    # Only one exit prompt.
    ActivateExitBonfire()

    ActivateAbyssPortal(0, 1700997, 1700998)


def Preconstructor():
    """ 50: Event 50 """
    RescueMornstein()
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


@RestartOnRest
def RescueMornstein():
    """ 11700801: Mornstein rescued after tower boss defeated. """
    if CommonFlags.MornsteinRescued:
        DisableCharacter(Chrs.Mornstein)
        return
    EnableInvincibility(Chrs.Mornstein)
    Await(Flags.Boss1Dead)
    EnableFlag(CommonFlags.MornsteinRescued)
    Wait(3.0)
    # No sound effect.
    DisplayBattlefieldMessage(CommonTexts.MornsteinRescued, 0)
    ForceAnimation(Chrs.Mornstein, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Mornstein)


@RestartOnRest
def CaveBossImmortality():
    """ 11700800: Cave boss(es) are immortal until Crystal is destroyed. """
    EnableObjectInvulnerability(1701800)
    AddSpecialEffect(Chrs.Boss2, 5440)
    AddSpecialEffect(Chrs.Boss2, 5441)
    AddSpecialEffect(Chrs.Boss2, 5442)
    AddSpecialEffect(Chrs.Boss2, 5443)
    AddSpecialEffect(Chrs.Boss2Twin, 5440)
    AddSpecialEffect(Chrs.Boss2Twin, 5441)
    AddSpecialEffect(Chrs.Boss2Twin, 5442)
    AddSpecialEffect(Chrs.Boss2Twin, 5443)
    EnableImmortality(Chrs.Boss2)
    EnableImmortality(Chrs.Boss2Twin)
    CreateObjectFX(170004, obj=1701800, model_point=100)

    # Crystal is invulnerable until boss battle is triggered.
    Await(Regions.Boss2Trigger)
    DisableObjectInvulnerability(1701800)

    IfObjectDestroyed(0, 1701800)
    DeleteObjectFX(1703100, erase_root=True)
    CancelSpecialEffect(Chrs.Boss2, 5440)
    CancelSpecialEffect(Chrs.Boss2, 5441)
    CancelSpecialEffect(Chrs.Boss2, 5442)
    CancelSpecialEffect(Chrs.Boss2, 5443)
    CancelSpecialEffect(Chrs.Boss2Twin, 5440)
    CancelSpecialEffect(Chrs.Boss2Twin, 5441)
    CancelSpecialEffect(Chrs.Boss2Twin, 5442)
    CancelSpecialEffect(Chrs.Boss2Twin, 5443)
    DisableImmortality(Chrs.Boss2)
    DisableImmortality(Chrs.Boss2Twin)


@RestartOnRest
def Event11705397():
    """ 11705397: Event 11705397 """
    DisableCharacter(1700801)
    EndIfFlagOn(14)
    SkipLinesIfThisEventOff(4)
    SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
    AICommand(1700800, command_id=20, slot=0)
    End()
    IfCharacterBackreadEnabled(0, 1700800)
    CreateNPCPart(1700800, npc_part_id=5290, part_index=NPCPartType.Part1, part_health=330, damage_correction=1.0, 
                  body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    IfHealthGreaterThan(1, 1700800, 0.0)
    IfCharacterPartHealthLessThanOrEqual(1, 1700800, npc_part_id=5290, value=0)
    IfHealthLessThanOrEqual(2, 1700800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(1700800, 8000)
    IfHasTAEEvent(0, 1700800, tae_event_id=400)
    Move(1700801, destination=1700800, destination_type=CoordEntityType.Character, model_point=150, 
         copy_draw_parent=1700800)
    EnableCharacter(1700801)
    SetDisplayMask(1700800, bit_index=1, switch_type=OnOffChange.On)
    SetCollisionMask(1700800, bit_index=1, switch_type=OnOffChange.Off)
    ForceAnimation(1700801, 8100)
    AICommand(1700800, command_id=20, slot=0)
    ReplanAI(1700800)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(52910000, host_only=True)


def Event11700160(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 11700160: Event 11700160 """
    IfFlagOff(1, arg_16_19)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfObjectActivated(2, obj_act_id=arg_8_11)
    IfObjectActivated(3, obj_act_id=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_16_19)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SkipLinesIfFinishedConditionTrue(9, 2)
    SkipLinesIfFlagOn(8, arg_0_3)
    SkipLinesIfFinishedConditionFalse(4, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 0)
    WaitFrames(105)
    EnableFlag(arg_20_23)
    IfFlagOff(0, arg_16_19)
    Restart()
    SkipLinesIfFinishedConditionFalse(4, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(arg_4_7, 2)
    WaitFrames(105)
    EnableFlag(arg_24_27)
    IfFlagOff(0, arg_16_19)
    Restart()


def Event11700105(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 11700105: Event 11700105 """
    SkipLinesIfFlagOff(4, arg_0_3)
    EndOfAnimation(arg_4_7, 11)
    EnableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLines(2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EnableObjectActivation(arg_12_15, obj_act_id=-1)
    IfHost(1)
    IfFlagOn(1, arg_20_23)
    IfHost(2)
    IfFlagOn(2, arg_24_27)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_20_23)
    DisableFlag(arg_24_27)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    DisableObjectActivation(arg_12_15, obj_act_id=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 1)
    WaitFrames(300)
    DisableFlag(arg_16_19)
    Restart()
    DisableFlag(arg_0_3)
    ForceAnimation(arg_4_7, 3)
    WaitFrames(344)
    DisableFlag(arg_16_19)
    Restart()


def Event11700090(_, arg_0_3: int, arg_4_4: uchar, arg_8_11: int, arg_12_15: int):
    """ 11700090: Event 11700090 """
    DisableNetworkSync()
    IfFlagState(1, state=arg_4_4, flag_type=FlagType.Absolute, flag=arg_0_3)
    IfFlagOff(1, arg_12_15)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=195, human_or_hollow_only=False)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010170, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11705150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11705150: Event 11705150 """
    IfDialogPromptActivated(1, prompt_text=10010503, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfDialogPromptActivated(2, prompt_text=10010503, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(7, 1)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagOn(2, arg_0_3)
    ForceAnimation(arg_4_7, 0)
    SkipLines(1)
    ForceAnimation(arg_4_7, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(105)
    SkipLinesIfFinishedConditionFalse(7, 2)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    SkipLinesIfFlagOn(2, arg_0_3)
    ForceAnimation(arg_8_11, 0)
    SkipLines(1)
    ForceAnimation(arg_8_11, 2)
    ForceAnimation(PLAYER, 8010)
    WaitFrames(105)
    EnableFlag(11705151)
    EnableFlag(11705152)
    IfFlagOff(3, 11705151)
    IfFlagOff(3, 11705152)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event11700200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int, arg_28_31: int):
    """ 11700200: Event 11700200 """
    DisableObject(arg_8_11)
    SkipLinesIfFlagOn(5, arg_0_3)
    EndOfAnimation(arg_4_7, 3)
    DisableCollision(arg_16_19)
    DisableNavmeshType(arg_20_23, NavmeshType.Solid)
    EnableNavmeshType(arg_24_27, NavmeshType.Solid)
    SkipLines(4)
    EndOfAnimation(arg_4_7, 1)
    DisableCollision(arg_12_15)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    DisableNavmeshType(arg_24_27, NavmeshType.Solid)
    IfFlagOn(0, arg_28_31)
    SkipLinesIfFlagOn(11, arg_0_3)
    ForceAnimation(arg_4_7, 1)
    DisableCollision(arg_12_15)
    EnableObject(arg_8_11)
    EnableNavmeshType(arg_20_23, NavmeshType.Solid)
    ForceAnimation(arg_8_11, 1)
    WaitFrames(180)
    DisableObject(arg_8_11)
    EnableCollision(arg_16_19)
    EnableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()
    ForceAnimation(arg_4_7, 3)
    DisableCollision(arg_16_19)
    EnableObject(arg_8_11)
    EnableNavmeshType(arg_24_27, NavmeshType.Solid)
    ForceAnimation(arg_8_11, 3)
    WaitFrames(180)
    DisableObject(arg_8_11)
    EnableCollision(arg_12_15)
    DisableFlag(arg_0_3)
    DisableFlag(arg_28_31)
    Restart()


def Event11700110():
    """ 11700110: Event 11700110 """
    SkipLinesIfThisEventOff(5)
    DisableObjectActivation(1701111, obj_act_id=-1)
    EndOfAnimation(1701110, 0)
    DisableObject(1701109)
    DisableCollision(1703220)
    End()
    DisableObject(1701109)
    DisableCollision(1703221)
    IfObjectActivated(0, obj_act_id=11700110)
    DisableCollision(1703220)
    EnableObject(1701109)
    ForceAnimation(1701110, 0)
    ForceAnimation(1701109, 0, wait_for_completion=True)
    DisableObject(1701109)
    EnableCollision(1703221)


def Event11700120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 11700120: Event 11700120 """
    SkipLinesIfThisEventSlotOff(4)
    SkipLinesIfEqual(1, left=arg_16_19, right=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1)
    EndOfAnimation(arg_4_7, arg_12_15)
    End()
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfFlagOn(-1, 11700140)
    IfObjectActivated(-1, obj_act_id=arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15)


def Event11700150(_, arg_0_3: int, arg_4_7: int):
    """ 11700150: Event 11700150 """
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    EnableCollision(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    DisableCollision(arg_0_3)
    Restart()


@RestartOnRest
def Event11705160(_, arg_0_3: int, arg_4_7: float):
    """ 11705160: Event 11705160 """
    SkipLinesIfThisEventSlotOff(2)
    ResetStandbyAnimationSettings(arg_0_3)
    End()
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=arg_4_7)
    SetStandbyAnimationSettings(arg_0_3, cancel_animation=13000)


@RestartOnRest
def Event11705250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11705250: Event 11705250 """
    EndIfThisEventSlotOn()
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfAttacked(-1, arg_4_7, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_4_7, arg_8_11, wait_for_completion=True)
    EnableAI(arg_4_7)


def Event11700300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11700300: Event 11700300 """
    EndIfClient()
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No, 
                  number_buttons=NumberButtons.NoButton)


@RestartOnRest
def Event11705280(_, butterfly: int, item_lot: int):
    """ 11705280: Event 11705280 """
    IfCharacterAlive(0, butterfly)
    IfCharacterDead(0, butterfly)
    IfCharacterHuman(-7, PLAYER)
    IfCharacterHollow(-7, PLAYER)
    EndIfConditionFalse(-7)
    AwardItemLot(item_lot, host_only=True)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11700600: Open chest. """
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
    """ 11702080: All-in-one boss event for simplicity. """
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


@RestartOnRest
def BossBattleExtraFog(
        _, boss: Character, boss_twin: Character, twin_enabled: Flag,
        trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLot,
        fog_1_object: int, fog_1_sfx: int,
        fog_2_object: int, fog_2_sfx: int,
        boss_name: short, boss_twin_name: short,
        fog_3_object: int, fog_3_sfx: int,):
    """ 11702055: All-in-one boss event for simplicity. """
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteFX(fog_1_sfx, erase_root_only=False)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteFX(fog_2_sfx, erase_root_only=False)
    if fog_3_object != 0:
        DisableObject(fog_3_object)
        DeleteFX(fog_3_sfx, erase_root_only=False)

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
    if fog_3_object != 0:
        EnableObject(fog_3_object)
        CreateFX(fog_3_sfx)

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
    if fog_3_object != 0:
        DisableObject(fog_3_object)
        DeleteFX(fog_3_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)


def InvaderTrigger(_, invader: Character, spawn_point: Region, trigger: Region,
                   summoned_flag: Flag, dismissed_flag: Flag, dead_flag: Flag, ):
    """ 11705200: Invasion is triggered. Human not needed. """
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
    """ 11702260: Invader in this map has been killed. Also disables them on startup. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    Await(IsDead(invader))
    EnableFlag(dead_flag)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11703000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


def ActivateExitBonfire():
    """ 11702200: Defeat boss to make bonfire appear and finish level. """
    if not Flags.Boss2Dead:
        DisableObject(Objects.Exit2Prompt)
        Await(Flags.Boss2Dead)
        CreateTemporaryFX(90014, anchor_entity=Objects.Exit2Prompt, anchor_type=CoordEntityType.Object, model_point=-1)
        Wait(4.0)
        EnableObject(Objects.Exit2Prompt)
        if not CommonFlags.ArchivesBossDefeated:
            if CommonFlags.LordvesselObtained:
                DisplayStatus(CommonTexts.MoreTreasureUnlocked)
                EnableFlag(CommonFlags.ArchivesBossDefeated)
            else:
                DisplayStatus(CommonTexts.LordvesselNotObtained)
    if FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 3) or CommonFlags.KilnAvailable:
        # Go to Chasm or Kiln (mod will figure out which).
        Await(not Flags.Exit2Disabled and DialogPromptActivated(
            CommonTexts.DepartLevel, Objects.Exit2Prompt, anchor_type=CoordEntityType.Object, max_distance=2.0))
        EnableFlag(Flags.Exit2Activated)
    else:
        # Go back to Firelink.
        Await(not Flags.Exit2Disabled and DialogPromptActivated(
            CommonTexts.ReturnToFirelink, Objects.Exit2Prompt, anchor_type=CoordEntityType.Object, max_distance=2.0))
        AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11705810: Mimic is activated by the player. """
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
    """ 11705820: Mimic state control. """
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
    """ 11705830: Mimic goes to sleep. """
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
    """ 11705840: Mimic wakes up again. """
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
    """ 11705850: Mimic enters chest form. """
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
    """ 11705860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11702999: Activate Abyss portal. """
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
    """ 11702950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11702960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
