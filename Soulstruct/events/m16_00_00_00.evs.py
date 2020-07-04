"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .new_londo_constants import *


def Constructor():
    """ 0: Event 0 """
    BossBattleAbyss(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1603800,
        ItemLots.Boss1Reward,
        1601990, 1601991, 0, 0,
        1000, 1000,
    )

    RegisterBonfire(11600992, obj=1601960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11600010, stop_climbing_flag=11600011, obj=1601140)
    RegisterLadder(start_climbing_flag=11600012, stop_climbing_flag=11600013, obj=1601141)

    EnableFlag(11600102)

    DisableObject(1601994)
    DeleteFX(1601995, erase_root_only=False)
    DisableObject(1601996)
    DeleteFX(1601997, erase_root_only=False)
    DisableObject(1601998)
    DeleteFX(1601999, erase_root_only=False)
    DisableSpawner(1603000)
    DisableObject(1601700)
    DeleteFX(1601701, erase_root_only=False)
    DisableObject(1601702)
    DeleteFX(1601703, erase_root_only=False)

    DisableLowerEnemiesPreDrain()
    # Flood collision/map piece control.
    ControlPrePostDrainCollisions()
    # Draining cutscene trigger.
    DrainNewLondo()
    # Pull draining lever.
    RunEvent(11600101, slot=0, args=(1601101, 11600102, 0))
    # Sluice gate (now needs Polished Key or Skeleton Keys).
    RunEvent(11600110, slot=0, args=(11600110, 10010862, 1601111))
    # Valley gate (now unlocked).
    RunEvent(11600120, slot=0, args=(11600120, 1601110))

    # Kick down bridge ladder.
    RunEvent(11600160)

    # Firelink elevator is always down, and not useable (prompt).
    EndOfAnimation(1601200, 21)
    DisableObjectActivation(1601202, obj_act_id=6101)

    RunEvent(11600199)
    RunEvent(11600210)
    RunEvent(11600251)
    RunEvent(11600220)
    RunEvent(11600252)

    # Darkroot elevator is always down, and not useable (prompt). A copy of the lift is always up in Darkroot.
    EndOfAnimation(1601230, 21)
    DisableObjectActivation(1601232, obj_act_id=6101)

    # Undead Dragon. TODO: Random valuable item lot.
    RunEvent(11600810)
    RunEvent(11600400)

    # Abyss.
    # Kill planes always disabled (no Covenant needed).
    DisableCollision(1603310)
    DisableCollision(1603311)
    # Always survive fall into Abyss.
    SurviveAbyssFall()
    # Remove event 11605360, which drags the player down into the Abyss when killed.

    # Unused Jareel arena music.
    DisableSoundEvent(1603801)

    # Chests.
    OpenChest(0, 1601650, 11600600)
    OpenChest(1, 1601651, 11600601)
    OpenChest(2, 1601652, 11600602)
    OpenChest(3, 1601653, 11600603)
    OpenChest(4, 1601654, 11600604)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    for enemy in range(100):
        DespawnEnemy(enemy, 1600100 + enemy)

    GetReward(0, 1600130, CommonItemLots.HolySigilLot)
    GetReward(1, 1600145, CommonItemLots.PiercingEyeLot)  # Just because (always lower).

    DepartLevelWithKey(  # Darkroot elevator
        0, Regions.Exit1Prompt, CommonTexts.DepartLevel, CommonTexts.HolySigilRequired, Flags.Exit1Disabled,
        CommonGoods.HolySigil, Flags.Exit1Activated)
    DepartLevelWithKey(  # Firelink elevator
        1, Regions.Exit2Prompt, CommonTexts.DepartLevel, CommonTexts.HolySigilRequired, Flags.Exit2Disabled,
        CommonGoods.HolySigil, Flags.Exit2Activated)
    DepartLevelUnconditional(  # Blighttown tunnel
        0, Regions.Exit3Prompt, CommonTexts.DepartLevel, Flags.Exit3Disabled, Flags.Exit3Activated)
    ActivateExitBonfire()  # Depart after Abyss battle won


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


def SurviveAbyssFall():
    """ 11605398: Event 11605398 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=Regions.Boss1Trigger)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


def Event11605360(_, arg_0_3: int):
    """ 11605360: Event 11605360 """
    DisableNetworkSync()
    IfFlagOff(1, 13)
    IfCharacterInsideRegion(1, arg_0_3, region=1602990)
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 2200)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 6084, wait_for_completion=True)
    DisableCharacter(arg_0_3)
    EndIfNotEqual(left=arg_0_3, right=10000)
    EnableFlag(8120)


def ControlPrePostDrainCollisions():
    """ 11600150: Event 11600150 """
    SkipLinesIfFlagOn(63, Flags.NewLondoDrained)
    DisableCollision(1603250)
    DisableCollision(1603251)
    DisableCollision(1603252)
    DisableCollision(1603253)
    DisableCollision(1603254)
    DisableCollision(1603255)
    DisableCollision(1603256)
    DisableCollision(1603257)
    DisableCollision(1603258)
    DisableCollision(1603259)
    DisableCollision(1603260)
    DisableCollision(1603261)
    DisableCollision(1603262)
    DisableCollision(1603263)
    DisableCollision(1603264)
    DisableCollision(1603265)
    DisableCollision(1603266)
    DisableCollision(1603267)
    DisableMapPiece(1603110)
    DisableMapPiece(1603111)
    DisableMapPiece(1603112)
    DisableMapPiece(1603113)
    DisableMapPiece(1603114)
    DisableMapPiece(1603115)
    DisableMapPiece(1603116)
    DisableMapPiece(1603117)
    DisableMapPiece(1603118)
    DisableMapPiece(1603119)
    DisableMapPiece(1603120)
    DisableCollision(1603121)
    DisableCollision(1603122)
    IfFlagOn(0, Flags.NewLondoDrained)
    EnableCollision(1603250)
    EnableCollision(1603251)
    EnableCollision(1603252)
    EnableCollision(1603253)
    EnableCollision(1603254)
    EnableCollision(1603255)
    EnableCollision(1603256)
    EnableCollision(1603257)
    EnableCollision(1603258)
    EnableCollision(1603259)
    EnableCollision(1603260)
    EnableCollision(1603261)
    EnableCollision(1603262)
    EnableCollision(1603263)
    EnableCollision(1603264)
    EnableCollision(1603265)
    EnableCollision(1603266)
    EnableCollision(1603267)
    EnableMapPiece(1603110)
    EnableMapPiece(1603111)
    EnableMapPiece(1603112)
    EnableMapPiece(1603113)
    EnableMapPiece(1603114)
    EnableMapPiece(1603115)
    EnableMapPiece(1603116)
    EnableMapPiece(1603117)
    EnableMapPiece(1603118)
    EnableMapPiece(1603119)
    EnableMapPiece(1603120)
    EnableCollision(1603121)
    EnableCollision(1603122)
    DisableSoundEvent(1603850)
    DisableCollision(1603200)
    DisableCollision(1603201)
    DisableCollision(1603202)
    DisableCollision(1603203)
    DisableCollision(1603204)
    DisableCollision(1603205)
    DisableCollision(1603206)
    DisableCollision(1603207)
    DisableCollision(1603208)
    DisableCollision(1603209)
    DisableCollision(1603210)
    DisableCollision(1603211)
    DisableCollision(1603212)
    DisableCollision(1603213)
    DisableCollision(1603214)
    DisableCollision(1603215)
    DisableCollision(1603216)
    DisableCollision(1603217)


@RestartOnRest
def DisableLowerEnemiesPreDrain():
    """ 11605100: Event 11605100 """
    if Flags.NewLondoDrained:
        return  # All enemies enabled.

    for basic_enemy in range(50):
        DisableBackread(1600050 + basic_enemy)
    for basic_phantom in range(15):
        DisableBackread(1600115 + basic_phantom)
    for rare_enemy in range(15):
        DisableBackread(1600130 + rare_enemy)
    DisableBackread(1600170)

    Await(Flags.NewLondoDrained)

    for basic_enemy in range(50):
        EnableBackread(1600050 + basic_enemy)
    for basic_phantom in range(15):
        EnableBackread(1600115 + basic_phantom)
    for rare_enemy in range(15):
        EnableBackread(1600130 + rare_enemy)
    EnableBackread(1600170)


def DrainNewLondo():
    """ 11600100: Event 11600100 """
    SkipLinesIfFlagOn(1, 11600101)
    SkipLinesIfThisEventOff(8)
    EndOfAnimation(1601100, 10)
    DisableCollision(1603100)
    DisableCollision(1603102)
    DisableCollision(1603103)
    DisableCollision(1603104)
    DisableObject(1601120)
    DisableFlag(404)
    End()
    EnableCollision(1603103)
    EnableCollision(1603104)
    IfFlagOn(0, 11600101)
    PlayCutscene(160000, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(Flags.NewLondoDrained)
    Restart()


def Event11600101(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11600101: Event 11600101 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(1601100, arg_8_11)
    EndOfAnimation(arg_0_3, 0)
    End()
    IfDialogPromptActivated(0, prompt_text=10010502, anchor_entity=arg_0_3, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=104, human_or_hollow_only=False)
    Move(PLAYER, destination=arg_0_3, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    EndIfFlagOn(arg_4_7)
    ForceAnimation(1601100, arg_8_11, wait_for_completion=True)


def Event11600110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11600110: Event 11600110 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    if HasGood(CommonGoods.PolishedKey):
        DisplayDialog(arg_4_7, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                      number_buttons=NumberButtons.NoButton)
    else:  # Skeleton Keys
        DisplayDialog(10010883, anchor_entity=arg_8_11, display_distance=3.0, button_type=ButtonType.Yes_or_No,
                      number_buttons=NumberButtons.NoButton)
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11600120(_, arg_0_3: int, arg_8_11: int):
    """ 11600120: Event 11600120 """
    SkipLinesIfThisEventSlotOff(5)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    EnableFlag(arg_0_3)
    EndIfClient()
    DisableNetworkSync()
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=0)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=1)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=2)
    DisableObjectActivation(arg_8_11, obj_act_id=-1, relative_index=3)


def Event11600160():
    """ 11600160: Event 11600160 """
    SkipLinesIfThisEventOff(3)
    EndOfAnimation(1601142, 0)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)
    End()
    IfDialogPromptActivated(0, prompt_text=10010500, anchor_entity=1601142, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=194, human_or_hollow_only=False)
    EnableFlag(11600160)
    Move(PLAYER, destination=1601142, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 8005)
    Wait(0.5)
    ForceAnimation(1601142, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=11600014, stop_climbing_flag=11600015, obj=1601142)


def Event11600199():
    """ 11600199: Event 11600199 """
    EndIfThisEventOn()
    IfFlagOn(0, Flags.NewLondoDrained)
    EnableObjectActivation(1601211, obj_act_id=6101)
    EnableObjectActivation(1601221, obj_act_id=6101)


def Event11600210():
    """ 11600210: Event 11600210 """
    SkipLinesIfFlagOff(3, 11600211)
    EndOfAnimation(1601210, 22)
    DisableObjectActivation(1601211, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601210, 21)
    DisableObjectActivation(1601212, obj_act_id=6101)
    SkipLinesIfFlagOn(1, Flags.NewLondoDrained)
    DisableObjectActivation(1601211, obj_act_id=6101)
    IfFlagOn(1, Flags.NewLondoDrained)
    IfFlagOff(1, 11600211)
    IfCharacterInsideRegion(1, PLAYER, region=1602211)
    IfFlagOn(2, Flags.NewLondoDrained)
    IfFlagOn(2, 11600211)
    IfCharacterInsideRegion(2, PLAYER, region=1602210)
    IfObjectActivated(3, obj_act_id=11600212)
    IfObjectActivated(4, obj_act_id=11600213)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605121)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600211)
    DisableObjectActivation(1601211, obj_act_id=6101)
    ForceAnimation(1601210, 10, wait_for_completion=True)
    ForceAnimation(1601210, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602210)
    ForceAnimation(1601210, 22, wait_for_completion=True)
    EnableObjectActivation(1601212, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()
    DisableFlag(11600211)
    DisableObjectActivation(1601212, obj_act_id=6101)
    ForceAnimation(1601210, 13, wait_for_completion=True)
    ForceAnimation(1601210, 3, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602211)
    ForceAnimation(1601210, 21, wait_for_completion=True)
    EnableObjectActivation(1601211, obj_act_id=6101)
    DisableFlag(11605121)
    Restart()


def Event11600251():
    """ 11600251: Event 11600251 """
    DisableNetworkSync()
    IfFlagOff(1, 11605121)
    IfFlagOn(1, 11600211)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1601211, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605121)
    IfFlagOff(2, 11600211)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601212, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(3, Flags.NewLondoDrained)
    IfDialogPromptActivated(3, prompt_text=10010501, anchor_entity=1601211, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11600220():
    """ 11600220: Event 11600220 """
    SkipLinesIfFlagOff(3, 11600221)
    EndOfAnimation(1601220, 24)
    DisableObjectActivation(1601221, obj_act_id=6101)
    SkipLines(2)
    EndOfAnimation(1601220, 21)
    DisableObjectActivation(1601222, obj_act_id=6101)
    SkipLinesIfFlagOn(1, Flags.NewLondoDrained)
    DisableObjectActivation(1601221, obj_act_id=6101)
    IfFlagOn(1, Flags.NewLondoDrained)
    IfFlagOff(1, 11600221)
    IfCharacterInsideRegion(1, PLAYER, region=1602221)
    IfFlagOn(2, Flags.NewLondoDrained)
    IfFlagOn(2, 11600221)
    IfCharacterInsideRegion(2, PLAYER, region=1602220)
    IfObjectActivated(3, obj_act_id=11600222)
    IfObjectActivated(4, obj_act_id=11600223)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11605122)
    SkipLinesIfFinishedConditionTrue(10, 2)
    SkipLinesIfFinishedConditionTrue(9, 4)
    EnableFlag(11600221)
    DisableObjectActivation(1601221, obj_act_id=6101)
    ForceAnimation(1601220, 10, wait_for_completion=True)
    ForceAnimation(1601220, 4, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602220)
    ForceAnimation(1601220, 24, wait_for_completion=True)
    EnableObjectActivation(1601222, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()
    DisableFlag(11600221)
    DisableObjectActivation(1601222, obj_act_id=6101)
    ForceAnimation(1601220, 15, wait_for_completion=True)
    ForceAnimation(1601220, 5, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=1602221)
    ForceAnimation(1601220, 21, wait_for_completion=True)
    EnableObjectActivation(1601221, obj_act_id=6101)
    DisableFlag(11605122)
    Restart()


def Event11600252():
    """ 11600252: Event 11600252 """
    DisableNetworkSync()
    IfFlagOff(1, 11605122)
    IfFlagOn(1, 11600221)
    IfDialogPromptActivated(1, prompt_text=10010501, anchor_entity=1601221, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(2, 11605122)
    IfFlagOff(2, 11600221)
    IfDialogPromptActivated(2, prompt_text=10010501, anchor_entity=1601222, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfFlagOff(3, Flags.NewLondoDrained)
    IfDialogPromptActivated(3, prompt_text=10010501, anchor_entity=1601221, anchor_type=CoordEntityType.Object, 
                            facing_angle=60.0, max_distance=1.5, model_point=192, human_or_hollow_only=False)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.NoButton)
    Restart()


@RestartOnRest
def Event11600810():
    """ 11600810: Event 11600810 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1600500)
    End()
    IfCharacterDead(0, 1600500)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    EndIfConditionFalse(-1)
    AwardItemLot(34200200, host_only=True)


@RestartOnRest
def Event11600400():
    """ 11600400: Event 11600400 """
    DisableCharacterCollision(1600500)
    DisableGravity(1600500)
    SkipLinesIfThisEventOff(2)
    SetStandbyAnimationSettings(1600500, cancel_animation=29060)
    End()
    IfEntityWithinDistance(-1, 1600500, PLAYER, radius=10.0)
    IfAttacked(-1, 1600500, attacking_character=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ResetStandbyAnimationSettings(1600500)
    ForceAnimation(1600500, 29060)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11600600: Open chest. """
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
def BossBattleAbyss(
        _, boss: Character, boss_twin: Character, twin_enabled: Flag,
        trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLot,
        fog_1_object: int, fog_1_sfx: int,
        fog_2_object: int, fog_2_sfx: int,
        boss_name: short, boss_twin_name: short):
    """ 11602080: All-in-one boss event for simplicity. Abyss flag version. Second fog arguments just for offset."""
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteFX(fog_1_sfx, erase_root_only=False)

    if dead_flag and not CommonFlags.AbyssBattleActive:
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

    # Increment Abyss victory counter.
    if CommonFlags.AbyssBattleVictoryCountBase:
        DisableFlag(CommonFlags.AbyssBattleVictoryCountBase)
        EnableFlag(CommonFlags.AbyssBattleVictoryCountBase + 1)
    elif FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 1):
        DisableFlag(CommonFlags.AbyssBattleVictoryCountBase + 1)
        EnableFlag(CommonFlags.AbyssBattleVictoryCountBase + 2)
    elif FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 2):
        DisableFlag(CommonFlags.AbyssBattleVictoryCountBase + 2)
        EnableFlag(CommonFlags.AbyssBattleVictoryCountBase + 3)
        # No need to track Abyss victories beyond three (1943).

    if not CommonFlags.AbyssBattleActive:
        EnableFlag(dead_flag)  # Boss only flagged as dead in real New Londo battle.
    DisableBossHealthBar(boss, boss_name, slot=0)  # Will disable twin's bar automatically.
    DisableObject(fog_1_object)
    DeleteFX(fog_1_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)

    if not CommonFlags.AbyssBattleActive:
        return
    Wait(2.0)
    DisableFlag(CommonFlags.AbyssBattleActive)
    if CommonFlags.InDepths:
        WarpToMap(DEPTHS, 1000999)
    if CommonFlags.InUndeadBurg:
        WarpToMap(UNDEAD_BURG, 1010999)
    if CommonFlags.InUndeadBurg:
        WarpToMap(UNDEAD_BURG, 1010999)
    if CommonFlags.InPaintedWorld:
        WarpToMap(PAINTED_WORLD, 1100999)
    if CommonFlags.InDarkroot:
        WarpToMap(DARKROOT_GARDEN, 1200999)
    if CommonFlags.InRoyalWood:
        WarpToMap(OOLACILE, 1210999)
    if CommonFlags.InOolacileTownship:
        WarpToMap(OOLACILE, 1210999)
    if CommonFlags.InChasm:
        WarpToMap(OOLACILE, 1210999)
    if CommonFlags.InCatacombs:
        WarpToMap(CATACOMBS, 1300999)
    if CommonFlags.InTomb:
        WarpToMap(TOMB_OF_THE_GIANTS, 1310999)
    if CommonFlags.InGreatHollow:
        WarpToMap(ASH_LAKE, 1320999)
    if CommonFlags.InAshLake:
        WarpToMap(ASH_LAKE, 1320999)
    if CommonFlags.InBlighttown:
        WarpToMap(BLIGHTTOWN, 1400999)
    if CommonFlags.InDemonRuins:
        WarpToMap(LOST_IZALITH, 1410999)
    if CommonFlags.InLostIzalith:
        WarpToMap(LOST_IZALITH, 1410999)
    if CommonFlags.InSensFortress:
        WarpToMap(SENS_FORTRESS, 1500999)
    if CommonFlags.InAnorLondo:
        WarpToMap(ANOR_LONDO, 1510999)
    if CommonFlags.InNewLondoRuins:
        WarpToMap(NEW_LONDO_RUINS, 1600999)
    if CommonFlags.InDukesArchives:
        WarpToMap(DUKES_ARCHIVES, 1700999)
    if CommonFlags.InKiln:
        WarpToMap(KILN_OF_THE_FIRST_FLAME, 1800999)
    return


def InvaderTrigger(_, invader: Character, spawn_point: Region, trigger: Region,
                   summoned_flag: Flag, dismissed_flag: Flag, dead_flag: Flag, ):
    """ 11605200: Invasion is triggered. Human not needed. """
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
    """ 11602260: Invader in this map has been killed. Also disables them on startup. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    Await(IsDead(invader))
    EnableFlag(dead_flag)


def DepartLevelUnconditional(
        _, prompt_region: Region, prompt_text: Text, disabled_flag: Flag, end_trigger_flag: Flag):
    """ 11602200: Depart level by interacting with prompt in region. No conditions. """
    Await(FlagDisabled(disabled_flag) and DialogPromptActivated(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Region))
    EnableFlag(end_trigger_flag)


def DepartLevelWithKey(_, prompt_region: Region, prompt_text: Text, failure_text: Text, disabled_flag: Flag,
                       key: Good, end_trigger_flag: Flag):
    """ 11602210: Depart level by interacting with prompt with key in inventory. """
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
    else:
        DisplayDialog(failure_text)
        Wait(2.0)
        return RESTART


def ActivateExitBonfire():
    """ 11602230: Defeat boss to make bonfire appear and finish level. """
    if not Flags.Boss1Dead:
        DisableObject(Objects.Exit4Prompt)
        Await(Flags.Boss1Dead)
        CreateTemporaryFX(90014, anchor_entity=Objects.Exit4Prompt, anchor_type=CoordEntityType.Object, model_point=-1)
        Wait(4.0)  # Give banner time.
        EnableObject(Objects.Exit4Prompt)
        if not CommonFlags.NewLondoBossDefeated:
            if CommonFlags.LordvesselObtained:
                DisplayStatus(CommonTexts.MoreTreasureUnlocked)
                EnableFlag(CommonFlags.NewLondoBossDefeated)
            else:
                DisplayStatus(CommonTexts.LordvesselNotObtained)

    # TODO: Same as Izalith; disabled exit flag is being enabled somehow. Not needed anyway.
    if FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 3) or CommonFlags.KilnAvailable:
        # Go to Chasm or Kiln (mod will figure out which).
        Await(DialogPromptActivated(
            CommonTexts.DepartLevel, Objects.Exit4Prompt, max_distance=2.0))
        EnableFlag(Flags.Exit4Activated) 
    else:
        # Go back to Firelink.
        Await(DialogPromptActivated(
            CommonTexts.ReturnToFirelink, Objects.Exit4Prompt, max_distance=2.0))
        AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


def DespawnEnemy(_, enemy: int):
    """ 11603000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11605810: Mimic is activated by the player. """
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
    """ 11605820: Mimic state control. """
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
    """ 11605830: Mimic goes to sleep. """
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
    """ 11605840: Mimic wakes up again. """
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
    """ 11605850: Mimic enters chest form. """
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
    """ 11605860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetReward(_, enemy: int, item_lot: ItemLot):
    """ 11602270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11602950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11602960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
