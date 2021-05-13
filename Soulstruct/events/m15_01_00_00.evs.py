"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from common_constants import *
from anor_londo_constants import *


def Constructor():
    """ 0: Event 0 """
    # O&S room boss battle.
    BossBattleExtraFog(
        0,
        Chrs.Boss1, Chrs.Boss1Twin, Flags.Boss1IsTwin,
        Regions.Boss1Trigger, Flags.Boss1Dead, 1513800,
        ItemLots.Boss1Reward,
        1511990, 1511991, 1511992, 1511993,
        1000, 1000,
        1511988, 1511989,
    )

    RegisterBonfire(11510992, obj=1511960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11510010, stop_climbing_flag=11510011, obj=1511140)
    RegisterLadder(start_climbing_flag=11510012, stop_climbing_flag=11510013, obj=1511141)

    # Delete Lautrec fog in palace.
    DisableObject(1511750)
    DeleteVFX(1511751, erase_root_only=False)
    DisableObject(1511752)
    DeleteVFX(1511753, erase_root_only=False)
    DisableObject(1511754)
    DeleteVFX(1511755, erase_root_only=False)

    # Disable Gwyndolin fog.
    DisableObject(1511890)
    DeleteVFX(1511891, erase_root_only=False)
    DisableObject(1511892)
    DeleteVFX(1511893, erase_root_only=False)

    DisableFlag(11510304)
    SkipLinesIfClient(2)
    DisableObject(1511994)
    DeleteVFX(1511995, erase_root_only=False)
    DisableObject(1511310)
    DisableCollision(1513301)
    DisableCollision(1513302)
    DisableCollision(1513303)
    SkipLinesIfFlagOff(1, 11510300)
    SkipLinesIfFlagOff(6, 11510303)
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(1511300, 53)
    EnableCollision(1513303)
    SkipLines(13)
    SkipLinesIfFlagOff(6, 11510302)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 50)
    EnableCollision(1513302)
    SkipLines(6)
    SkipLinesIfFlagOff(5, 11510301)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 51)
    EnableCollision(1513301)

    DisableObject(1511450)
    DisableFlag(11510460)
    DisableObject(1511700)
    DeleteVFX(1511701, False)
    DisableObject(1511702)
    DeleteVFX(1511703, False)

    # Palace door.
    RunEvent(11510200)
    RunEvent(11510201)
    # Break chandelier.
    RunEvent(11510100)
    # Blacksmith shortcut.
    RunEvent(11510210)
    RunEvent(11510211)
    # First activation of gondola.
    RunEvent(11510220)
    # Main gondola activation and other stuff.
    RunEvent(11510300)
    RunEvent(11510319)
    RunEvent(11510340)
    RunEvent(11510350)
    RunEvent(11510310)
    # Gwynevere's door.
    RunEvent(11510110)
    # Kill Gwynevere (she is currently invincible, so Dark Anor Londo can't be reached).
    RunEvent(11510400)
    # Darkmoon statue (now requires Piercing Eye).
    GwynStatueDisappears()

    # TODO: Make this Painted World event just like the others. Painting always appears there once, but then vanishes.
    RunEvent(11510230)
    RunEvent(11515050)
    RunEvent(11510120)
    RunEvent(11510130)
    RunEvent(11510131)

    # TODO: Inspect this Black Eye Orb event for using it elsewhere.
    # RunEvent(11510150)

    BreakIllusoryWall()
    IllusoryWallInvincible()

    # One-way shortcut doors.
    RunEvent(11510260, slot=0, args=(11510251, 1512251, 1512250))
    RunEvent(11510260, slot=1, args=(11510257, 1512253, 1512252))
    RunEvent(11510260, slot=2, args=(11510258, 1512255, 1512254))

    ActivatePostBossElevators()

    # Gwyndolin music disabled.
    DisableSoundEvent(1513802)

    # New simple Lordvessel getter from Gwynevere.
    GetLordvessel()

    # Rescue Solaire in Gwyn's Tomb.
    RescueSolaire()

    # Get Piercing Eye from a random Rare enemy (maybe).
    GetReward(0, 1510137, CommonItemLots.PiercingEyeLot, CommonFlags.PiercingEyeObtained)

    # Mimics
    OpenMimic(0, Chrs.Mimic)
    ControlMimicState(0, Chrs.Mimic)
    HitMimicWithTalisman(0, Chrs.Mimic)
    TalismanWearsOffMimic(0, Chrs.Mimic)
    MimicReturnsToChest(0, Chrs.Mimic, Regions.MimicNest)
    ReplanMimicAIOnLoad(0, Chrs.Mimic)

    # Chests.
    OpenChest(0, 1511650, 11510600)
    OpenChest(1, 1511651, 11510601)
    OpenChest(2, 1511652, 11510602)
    OpenChest(3, 1511653, 11510603)
    OpenChest(4, 1511654, 11510604)

    for enemy in range(100):
        DespawnEnemy(enemy, 1510100 + enemy)

    DepartWithDemons()
    DepartLevelUnconditional(
        1, Objects.Exit2Prompt, CommonTexts.DepartLevel, Flags.Exit2Disabled, Flags.Exit2Activated)
    DepartWithGwynevereBonfire()

    ActivateAbyssPortal(0, 1510997, 1510998)


def Preconstructor():
    """ 50: Event 50 """
    # NOTE: Gwynevere's story flags aren't reset each run.
    InvaderTrigger(0, 6990, 6991, Chrs.Invader, Regions.InvaderTrigger, Flags.InvaderDead)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


def Event11510100():
    """ 11510100: Event 11510100 """
    SkipLinesIfThisEventOff(8)
    PostDestruction(1511100, slot=1)
    PostDestruction(1511102, slot=1)
    EndOfAnimation(1511600, 111)
    EndOfAnimation(1511101, 0)
    EndOfAnimation(1511102, 1)
    EnableObjectInvulnerability(1511101)
    EnableTreasure(1511600)
    End()
    DisableTreasure(1511600)
    SkipLinesIfClient(1)
    CreateObjectVFX(99010, obj=1511600, model_point=90)
    ForceAnimation(1511600, 110, loop=True)
    IfObjectDestroyed(0, 1511100)
    ForceAnimation(1511600, 111)
    ForceAnimation(1511101, 0)
    ForceAnimation(1511102, 0, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(1511600, erase_root=True)
    EnableTreasure(1511600)
    DestroyObject(1511102, slot=1)


def Event11510110():
    """ 11510110: Event 11510110 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1511010, 0)
    End()
    IfActionButton(0, prompt_text=10010400, anchor_entity=1511010, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    Move(PLAYER, destination=1511010, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 7120)
    ForceAnimation(1511010, 0)


def Event11510200():
    """ 11510200: Event 11510200 """
    SkipLinesIfThisEventOff(4)
    DisableObjectActivation(1511001, obj_act_id=-1)
    EndOfAnimation(1511000, 0)
    EndOfAnimation(1511001, 0)
    End()
    IfFlagOff(1, 11510700)
    IfActionButton(1, prompt_text=10010502, anchor_entity=1511001, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=102, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=1511001, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511001, 0, wait_for_completion=True)
    ForceAnimation(1511000, 0)


def Event11510201():
    """ 11510201: Event 11510201 """
    DisableNetworkSync()
    IfFlagOff(1, 11510200)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1512000, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1511000)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010160, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11510210():
    """ 11510210: Event 11510210 """
    SkipLinesIfThisEventOff(2)
    EndOfAnimation(1511200, 0)
    End()
    EnableNavmeshType(1513200, NavmeshType.Solid)
    IfActionButton(0, prompt_text=10010400, anchor_entity=1511200, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=101, trigger_attribute=TriggerAttribute.All)
    Move(PLAYER, destination=1511200, destination_type=CoordEntityType.Object, model_point=121, short_move=True)
    ForceAnimation(PLAYER, 7110)
    ForceAnimation(1511200, 0)
    DisableNavmeshType(1513200, NavmeshType.Solid)


def Event11510211():
    """ 11510211: Event 11510211 """
    DisableNetworkSync()
    IfFlagOff(1, 11510210)
    IfActionButton(1, prompt_text=10010400, anchor_entity=1511200, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=100, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010161, anchor_entity=1511200, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11510220():
    """ 11510220: Event 11510220 """
    SkipLinesIfThisEventOn(1)
    IfCharacterInsideRegion(0, PLAYER, region=1512350)
    ForceAnimation(1511050, 0)


def Event11510260(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11510260: Event 11510260 """
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


def Event11510300():
    """ 11510300: Event 11510300 """
    IfFlagOff(1, 11510301)
    IfActionButton(1, prompt_text=10010502, anchor_entity=1511300, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=102, trigger_attribute=TriggerAttribute.All)
    IfFlagOff(2, 11510303)
    IfActionButton(2, prompt_text=10010502, anchor_entity=1511300, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=104, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(3, 11510305)
    IfFlagOff(3, 11510303)
    IfActionButton(3, prompt_text=10010501, anchor_entity=1511301, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(4, 11510305)
    IfFlagOn(4, 11510303)
    IfActionButton(4, prompt_text=10010501, anchor_entity=1511302, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(5, 11510305)
    IfFlagOff(5, 11510301)
    IfActionButton(5, prompt_text=10010501, anchor_entity=1511303, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(6, 11510305)
    IfFlagOff(6, 11510302)
    IfActionButton(6, prompt_text=10010501, anchor_entity=1511304, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11515300)
    SkipLinesIfFlagOn(20, 11510305)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10, wait_for_completion=True)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(cutscene_id=150100, skippable=True, fade_out=False, player_id=PLAYER, rotation=-90,
                 relative_rotation_axis_x=337.5, relative_rotation_axis_z=255.0, vertical_translation=-12.0)
    SkipLines(4)
    SkipLinesIfFlagOff(2, 11510304)
    PlayCutscene(cutscene_id=150100, skippable=False, fade_out=False, player_id=PLAYER, rotation=-90,
                 relative_rotation_axis_x=337.5, relative_rotation_axis_z=255.0, vertical_translation=-12.0)
    SkipLines(1)
    PlayCutscene(150100, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(1511300, 0)
    DisableCollision(1513303)
    EnableCollision(1513302)
    DisableFlag(11510303)
    EnableFlag(11510302)
    DisableFlag(11510304)
    EnableFlag(11510305)
    DisableFlag(11515300)
    Restart()
    SkipLinesIfFlagOff(33, 11510303)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=0, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 4)
    Move(PLAYER, destination=1511302, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511302, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=1, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=0, args=(0, 1, 1513301, 11510303, 11510301, 11, 180, 360))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 10)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=2, args=(0, 1513303, 1513302, 11510303, 11510302, 180))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(32, 11510302)
    SkipLinesIfFinishedConditionFalse(6, 1)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=103, short_move=True)
    ForceAnimation(PLAYER, 8021)
    ForceAnimation(1511300, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=3, args=(1, 1513302, 1513301, 11510302, 11510301, 360))
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=4, args=(3, 1513302, 1513303, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 13)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=5, args=(3, 1513302, 1513303, 11510302, 11510303, 180))
    SkipLinesIfFinishedConditionFalse(7, 5)
    Move(PLAYER, destination=1511303, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511303, 1)
    ForceAnimation(1511300, 11)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=6, args=(1, 1513302, 1513301, 11510302, 11510301, 360))
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(25, 11510301)
    SkipLinesIfFinishedConditionFalse(6, 2)
    Move(PLAYER, destination=1511300, destination_type=CoordEntityType.Object, model_point=101, short_move=True)
    ForceAnimation(PLAYER, 8020)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=7, args=(2, 1513301, 1513302, 11510301, 11510302, 360))
    SkipLinesIfFinishedConditionFalse(7, 3)
    Move(PLAYER, destination=1511301, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511301, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515330, slot=1, args=(2, 3, 1513303, 11510301, 11510303, 13, 360, 180))
    SkipLinesIfFinishedConditionFalse(7, 6)
    Move(PLAYER, destination=1511304, destination_type=CoordEntityType.Object, model_point=191, short_move=True)
    ForceAnimation(PLAYER, 8000)
    ForceAnimation(1511304, 1)
    ForceAnimation(1511300, 12)
    WaitFrames(130)
    IfFramesElapsed(0, 0)
    RunEvent(11515320, slot=8, args=(2, 1513301, 1513302, 11510301, 11510302, 360))
    IfFlagOff(0, 11515300)
    Restart()
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11510319():
    """ 11510319: Event 11510319 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1512310)
    EnableFlag(11510304)
    IfCharacterOutsideRegion(0, PLAYER, region=1512310)
    DisableFlag(11510304)
    Restart()


def Event11515320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11515320: Event 11515320 """
    DisableCollision(arg_4_7)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(arg_20_23)
    IfTimeElapsed(0, 0.0)
    DisableObject(1511310)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11515330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int,
                  arg_24_27: int, arg_28_31: int):
    """ 11515330: Event 11515330 """
    DisableCollision(1513301)
    DisableCollision(1513302)
    DisableCollision(1513303)
    EnableObject(1511310)
    ForceAnimation(1511300, arg_0_3)
    ForceAnimation(1511310, arg_0_3)
    WaitFrames(arg_24_27)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(1511300, arg_20_23)
    WaitFrames(130)
    IfTimeElapsed(0, 0.0)
    ForceAnimation(1511300, arg_4_7)
    ForceAnimation(1511310, arg_4_7)
    WaitFrames(arg_28_31)
    IfTimeElapsed(0, 0.0)
    DisableObject(1511310)
    EnableCollision(arg_8_11)
    DisableFlag(arg_12_15)
    EnableFlag(arg_16_19)
    EnableFlag(11515301)
    SkipLinesIfSingleplayer(1)
    Wait(2.0)
    DisableFlag(11515300)


def Event11510340():
    """ 11510340: Event 11510340 """
    SkipLinesIfFlagOff(8, 11515300)
    EnableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    EnableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOff(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510303)
    EnableCollision(1513310)
    DisableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    EnableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510302)
    DisableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    DisableNavmeshType(1513351, NavmeshType.Solid)
    DisableNavmeshType(1513352, NavmeshType.Solid)
    DisableNavmeshType(1513353, NavmeshType.Solid)
    EnableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    SkipLinesIfFlagOff(8, 11510301)
    EnableCollision(1513310)
    EnableNavmeshType(1513350, NavmeshType.Solid)
    EnableNavmeshType(1513351, NavmeshType.Solid)
    EnableNavmeshType(1513352, NavmeshType.Solid)
    DisableNavmeshType(1513353, NavmeshType.Solid)
    DisableNavmeshType(1513354, NavmeshType.Solid)
    IfFlagOn(0, 11515300)
    Restart()
    DisplayDialog(10010105, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()


def Event11510350():
    """ 11510350: Event 11510350 """
    IfHost(1)
    IfFlagOn(1, 11515301)
    IfFlagOn(1, 11510301)
    IfHost(2)
    IfFlagOn(2, 11515301)
    IfFlagOn(2, 11510302)
    IfHost(3)
    IfFlagOn(3, 11515301)
    IfFlagOn(3, 11510303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11515301)
    RestartIfSingleplayer()
    SkipLinesIfFinishedConditionFalse(6, 1)
    EnableFlag(11510301)
    DisableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 51)
    EnableCollision(1513301)
    Restart()
    SkipLinesIfFinishedConditionFalse(6, 2)
    DisableFlag(11510301)
    EnableFlag(11510302)
    DisableFlag(11510303)
    EndOfAnimation(1511300, 50)
    EnableCollision(1513302)
    Restart()
    DisableFlag(11510301)
    DisableFlag(11510302)
    EnableFlag(11510303)
    EndOfAnimation(1511300, 53)
    EnableCollision(1513303)
    Restart()


def Event11510310():
    """ 11510310: Event 11510310 """
    DisableNetworkSync()
    IfFlagOn(1, 11510301)
    IfActionButton(1, prompt_text=10010502, anchor_entity=1511300, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=102, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(2, 11510303)
    IfActionButton(2, prompt_text=10010502, anchor_entity=1511300, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=104, trigger_attribute=TriggerAttribute.All)
    IfFlagOff(-2, 11510305)
    IfFlagOn(-2, 11510303)
    IfConditionTrue(3, input_condition=-2)
    IfActionButton(3, prompt_text=10010501, anchor_entity=1511301, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOff(-3, 11510305)
    IfFlagOff(-3, 11510303)
    IfConditionTrue(4, input_condition=-3)
    IfActionButton(4, prompt_text=10010501, anchor_entity=1511302, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOff(-4, 11510305)
    IfFlagOn(-4, 11510301)
    IfConditionTrue(5, input_condition=-4)
    IfActionButton(5, prompt_text=10010501, anchor_entity=1511303, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOff(-5, 11510305)
    IfFlagOn(-5, 11510302)
    IfConditionTrue(6, input_condition=-5)
    IfActionButton(6, prompt_text=10010501, anchor_entity=1511304, anchor_type=CoordEntityType.Object,
                   facing_angle=60.0, max_distance=1.5, model_point=192, trigger_attribute=TriggerAttribute.All)
    IfFlagOn(7, 11515300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 7)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()
    IfFlagOff(0, 11515300)
    Restart()


def Event11510400():
    """ 11510400: Event 11510400 """
    DisableMapPiece(1513401)
    SkipLinesIfThisEventOff(7)
    DisableSoundEvent(1513801)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(1511400)
    End()
    EnableCharacter(1510600)
    EnableInvincibility(1510600)

    # Won't be able to progress from here as Gwynevere is invincible.
    IfCharacterDead(1, 1510600)
    IfEntityWithinDistance(1, 1510600, PLAYER, radius=15.0)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    DisableSoundEvent(1513801)
    EnableFlag(743)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterHollow(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfPlayerCovenant(1, Covenant.PrincessGuard)
    SkipLinesIfConditionFalse(4, 1)
    BetrayCurrentCovenant()
    IncrementPvPSin()
    EnableFlag(742)
    SaveRequest()
    DisableFlag(120)
    SkipLinesIfFlagOn(2, 11510900)
    PlayCutscene(150110, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(150111, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    SetMapDrawParamSlot(15, slot=1)
    SetLockedCameraSlot(game_map=ANOR_LONDO, camera_slot=1)
    DisableMapPiece(1513400)
    EnableMapPiece(1513401)
    DisableObject(1511400)
    IfPlayerHasGood(2, 2510, including_box=False)
    EndIfConditionTrue(2)
    AwardItemLot(1090, host_only=True)


def GwynStatueDisappears():
    """ 11510401: Event 11510401 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1511400)
    End()
    EnableObjectInvulnerability(1511400)
    IfFlagOn(1, 11510400)
    IfEntityWithinDistance(1, 1511400, PLAYER, radius=15.0)
    IfHost(2)
    IfPlayerHasGood(2, CommonGoods.PiercingEye)
    IfEntityWithinDistance(2, 1511400, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectInvulnerability(1511400)
    DestroyObject(1511400, slot=1)
    ForceAnimation(1511400, 0)
    PlaySoundEffect(anchor_entity=1511400, sound_type=SoundType.o_Object, sound_id=590000000)


@RestartOnRest
def Event11510450():
    """ 11510450: Event 11510450 """
    IfDoesNotHaveTAEEvent(0, 1510650, tae_event_id=600)
    IfHasTAEEvent(0, 1510650, tae_event_id=600)
    DisableCharacter(1510650)
    Wait(1.0)
    SkipLinesIfFlagOn(2, 11515110)
    RunEvent(11515110, slot=0, args=(1512710, 11515110))
    Restart()
    SkipLinesIfFlagOn(2, 11515111)
    RunEvent(11515110, slot=1, args=(1512711, 11515111))
    Restart()
    SkipLinesIfFlagOn(2, 11515112)
    RunEvent(11515110, slot=2, args=(1512712, 11515112))
    Restart()
    SkipLinesIfFlagOn(2, 11515113)
    RunEvent(11515110, slot=3, args=(1512713, 11515113))
    Restart()
    SkipLinesIfFlagOn(2, 11515114)
    RunEvent(11515110, slot=4, args=(1512714, 11515114))
    Restart()
    SkipLinesIfFlagOn(2, 11515115)
    RunEvent(11515110, slot=5, args=(1512715, 11515115))
    Restart()
    SkipLinesIfFlagOn(2, 11515116)
    RunEvent(11515110, slot=6, args=(1512716, 11515116))
    Restart()
    SkipLinesIfFlagOn(2, 11515117)
    RunEvent(11515110, slot=7, args=(1512717, 11515117))
    Restart()
    SkipLinesIfFlagOn(2, 11515118)
    RunEvent(11515110, slot=8, args=(1512718, 11515118))
    Restart()
    SkipLinesIfFlagOn(2, 11515119)
    RunEvent(11515110, slot=9, args=(1512719, 11515119))
    Restart()
    SkipLinesIfFlagOn(2, 11515120)
    RunEvent(11515110, slot=10, args=(1512720, 11515120))
    Restart()
    SkipLinesIfFlagOn(2, 11515121)
    RunEvent(11515110, slot=11, args=(1512721, 11515121))
    Restart()
    SkipLinesIfFlagOn(2, 11515122)
    RunEvent(11515110, slot=12, args=(1512722, 11515122))
    Restart()
    SkipLinesIfFlagOn(2, 11515123)
    RunEvent(11515110, slot=13, args=(1512723, 11515123))
    Restart()
    SkipLinesIfFlagOn(2, 11515124)
    RunEvent(11515110, slot=14, args=(1512724, 11515124))
    Restart()
    SkipLinesIfFlagOn(2, 11515125)
    RunEvent(11515110, slot=15, args=(1512725, 11515125))
    Restart()
    SkipLinesIfFlagOn(2, 11515126)
    RunEvent(11515110, slot=16, args=(1512726, 11515126))
    Restart()
    SkipLinesIfFlagOn(2, 11515127)
    RunEvent(11515110, slot=17, args=(1512727, 11515127))
    Restart()
    SkipLinesIfFlagOn(2, 11515128)
    RunEvent(11515110, slot=18, args=(1512728, 11515128))
    Restart()
    SkipLinesIfFlagOn(2, 11515129)
    RunEvent(11515110, slot=19, args=(1512729, 11515129))
    Restart()
    SkipLinesIfFlagOn(2, 11515130)
    RunEvent(11515110, slot=20, args=(1512730, 11515130))
    Restart()
    SkipLinesIfFlagOn(2, 11515131)
    RunEvent(11515110, slot=21, args=(1512731, 11515131))
    Restart()
    SkipLinesIfFlagOn(2, 11515132)
    RunEvent(11515110, slot=22, args=(1512732, 11515132))
    Restart()
    SkipLinesIfFlagOn(2, 11515133)
    RunEvent(11515110, slot=23, args=(1512733, 11515133))
    Restart()
    SkipLinesIfFlagOn(2, 11515134)
    RunEvent(11515110, slot=24, args=(1512734, 11515134))
    Restart()
    SkipLinesIfFlagOn(2, 11515135)
    RunEvent(11515110, slot=25, args=(1512735, 11515135))
    Restart()
    SkipLinesIfFlagOn(2, 11515136)
    RunEvent(11515110, slot=26, args=(1512736, 11515136))
    Restart()
    SkipLinesIfFlagOn(2, 11515137)
    RunEvent(11515110, slot=27, args=(1512737, 11515137))
    Restart()
    SkipLinesIfFlagOn(2, 11515138)
    RunEvent(11515110, slot=28, args=(1512738, 11515138))
    Restart()
    SkipLinesIfFlagOn(2, 11515139)
    RunEvent(11515110, slot=29, args=(1512739, 11515139))
    Restart()


@UnknownRestart
def Event11515110(_, arg_0_3: int, arg_4_7: int):
    """ 11515110: Event 11515110 """
    Move(1510650, destination=arg_0_3, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableCharacter(1510650)
    ReplanAI(1510650)
    ForceAnimation(1510650, 7000, wait_for_completion=True)
    EnableFlag(arg_4_7)
    SkipLinesIfFlagOff(2, 11515132)
    AICommand(1510650, command_id=1, slot=0)
    ReplanAI(1510650)


def Event11510230():
    """ 11510230: Event 11510230 """
    IfActionButton(0, prompt_text=10010100, anchor_entity=1512510, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0)
    IfSingleplayer(1)
    IfHost(1)
    IfPlayerHasGood(1, 384, including_box=False)
    SkipLinesIfConditionTrue(3, 1)
    SkipLinesIfClient(1)
    DisplayDialog(10010170, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel,
                  number_buttons=NumberButtons.NoButton)
    Restart()
    PlayCutscene(150135, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1102510,
                 move_to_map=PAINTED_WORLD)
    WaitFrames(1)
    SetRespawnPoint(1102511)
    SaveRequest()
    Restart()


def DepartWithDemons():
    """ 11510240: Event 11510240 """
    if Flags.Exit1Disabled:
        DisableCharacter(1510100)
        return

    EnableInvincibility(1510100)
    Await(not Flags.Exit1Disabled and ActionButton(
        CommonTexts.DepartLevel, anchor_entity=1510100, anchor_type=CoordEntityType.Character,
        facing_angle=180.0, max_distance=7.0))
    EnableFlag(Flags.Exit1Activated)


def Event11515050():
    """ 11515050: Event 11515050 """
    SkipLinesIfThisEventOff(2)
    DisableCharacter(1510100)
    End()
    DisableImmortality(1510100)
    SetStandbyAnimationSettings(1510100, standby_animation=9000)
    IfAttacked(-1, 1510100, attacker=PLAYER)
    IfFlagOn(-1, 11515050)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(11515050)
    ResetAnimation(1510100, disable_interpolation=True)
    ForceAnimation(1510100, 9060, wait_for_completion=True)
    DisableCharacter(1510100)


def Event11510120():
    """ 11510120: Event 11510120 """
    DisableNetworkSync()
    EndIfClient()
    IfFlagOn(1, 743)
    IfFlagOn(1, 12)
    IfFlagOff(1, 11510900)
    IfFlagOn(1, 11510400)
    IfCharacterInsideRegion(-1, PLAYER, region=1512400)
    IfStandingOnCollision(-1, 1513405)
    IfStandingOnCollision(-1, 1513100)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 4501)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event11510130():
    """ 11510130: Event 11510130 """
    SkipLinesIfFlagOn(5, 11510400)
    DisableCharacter(6640)
    DisableCharacter(6650)
    IfFlagOn(0, 11510400)
    EnableCharacter(6640)
    EnableCharacter(6650)
    DisableCharacter(1510500)
    DisableCharacter(1510450)
    DisableCharacter(1510452)
    DisableCharacter(1510110)
    DisableCharacter(1510111)
    DisableCharacter(1510112)
    DisableCharacter(1510113)
    DisableCharacter(1510114)
    DisableCharacter(1510115)
    DisableCharacter(1510116)
    DisableCharacter(1510117)
    DisableCharacter(1510118)
    DisableCharacter(1510119)
    DisableCharacter(1510400)
    DisableCharacter(1510401)
    DisableCharacter(1510402)
    DisableCharacter(1510403)
    DisableCharacter(1510404)
    DisableCharacter(1510405)
    DisableCharacter(1510406)
    DisableCharacter(1510407)
    DisableCharacter(1510408)
    DisableCharacter(1510409)
    DisableCharacter(1510410)
    DisableCharacter(1510411)
    DisableCharacter(1510412)
    DisableCharacter(1510413)
    EndIfFlagOn(1034)
    Move(6010, destination=1512450, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=1510452)
    SetNest(6010, 1512450)
    ResetStandbyAnimationSettings(6010)


def Event11510131():
    """ 11510131: Event 11510131 """
    EndIfClient()
    IfFlagOn(1, 11510400)
    IfInsideMap(1, game_map=ANOR_LONDO)
    IfHost(1)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    SetRespawnPoint(1512960)
    SaveRequest()


def Event11510150():
    """ 11510150: Event 11510150 """
    DisableNetworkSync()
    IfHost(1)
    IfPlayerHasGood(1, 115, including_box=False)
    IfCharacterInsideRegion(1, PLAYER, region=1512101)
    IfConditionTrue(0, input_condition=1)
    End()


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11510600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def BreakIllusoryWall():
    """ 11510215: Event 11510215 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1511210)
    End()
    IfObjectDestroyed(0, 1511210)
    End()


def IllusoryWallInvincible():
    """ 11510215: Piercing Eye needed. """
    if FlagEnabled(11510215):
        return
    EnableObjectInvulnerability(1511210)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1511210)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


@RestartOnRest
def BossBattleExtraFog(
        _, boss: Character, boss_twin: Character, twin_enabled: Flag,
        trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
        fog_1_object: int, fog_1_sfx: int,
        fog_2_object: int, fog_2_sfx: int,
        boss_name: short, boss_twin_name: short,
        fog_3_object: int, fog_3_sfx: int):
    """ 11512080: All-in-one boss event for simplicity. """
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteVFX(fog_1_sfx, erase_root_only=False)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteVFX(fog_2_sfx, erase_root_only=False)
    if fog_3_object != 0:
        DisableObject(fog_3_object)
        DeleteVFX(fog_3_sfx, erase_root_only=False)

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
    if fog_3_object != 0:
        EnableObject(fog_3_object)
        CreateVFX(fog_3_sfx)

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
    if fog_3_object != 0:
        DisableObject(fog_3_object)
        DeleteVFX(fog_3_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)


def ActivatePostBossElevators():
    """ 11512051: Two elevators after boss. """
    if Flags.Boss1Dead:
        ForceAnimation(1511401, 0, loop=True)
        ForceAnimation(1511402, 0, loop=True)
        return
    Await(Flags.Boss1Dead)
    ForceAnimation(1511401, 0, loop=True)
    ForceAnimation(1511402, 0, loop=True)


def DepartWithGwynevereBonfire():
    """ 11512200: Bonfire appears in Gwynevere's room for use as departure. """
    if not HasGood(CommonGoods.Lordvessel):
        DisableObject(Objects.Exit3Prompt)
        Await(HasGood(CommonGoods.Lordvessel))  # Given by Gwynevere.
        CreateTemporaryVFX(90014, anchor_entity=Objects.Exit3Prompt, anchor_type=CoordEntityType.Object, model_point=-1)
        Wait(4.0)
        EnableObject(Objects.Exit3Prompt)
        if not CommonFlags.LordvesselObtained:
            DisplayStatus(CommonTexts.LordvesselObtained)
            EnableFlag(CommonFlags.LordvesselObtained)

    if FlagEnabled(CommonFlags.AbyssBattleVictoryCountBase + 3) or CommonFlags.KilnAvailable:
        # Go to Chasm or Kiln (mod will figure out which).
        Await(not Flags.Exit3Disabled and ActionButton(
            CommonTexts.DepartLevel, Objects.Exit3Prompt, anchor_type=CoordEntityType.Object, max_distance=2.0))
        EnableFlag(Flags.Exit3Activated)
    else:
        # Go back to Firelink.
        Await(not Flags.Exit3Disabled and ActionButton(
            CommonTexts.ReturnToFirelink, Objects.Exit3Prompt, anchor_type=CoordEntityType.Object, max_distance=2.0))
        AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


def DepartLevelUnconditional(_, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, end_trigger_flag: Flag):
    """ 11512210: Depart level by interacting with prompt. No conditions. """
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object, max_distance=2.0))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11512260: Invasion is triggered. Human not needed. """
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


def DespawnEnemy(_, enemy: int):
    """ 11513000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11515810: Mimic is activated by the player. """
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
    """ 11515820: Mimic state control. """
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
    """ 11515830: Mimic goes to sleep. """
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
    """ 11515840: Mimic wakes up again. """
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
    """ 11515850: Mimic enters chest form. """
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
    """ 11515860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def GetLordvessel():
    """ 11510500: Get Lordvessel from Gwynevere. """
    if HasGood(CommonGoods.Lordvessel):
        return
    Await(ActionButton(10010210, Chrs.Gwynevere, anchor_type=CoordEntityType.Character,
                       facing_angle=180.0, max_distance=10.0))
    ForceAnimation(PLAYER, 7895, wait_for_completion=True)  # kneel
    ForceAnimation(PLAYER, 7896, loop=True)  # stay kneeled
    Wait(2.0)
    AwardItemLot(1090, host_only=True)
    ForceAnimation(PLAYER, 7897, wait_for_completion=True)


@RestartOnRest
def RescueSolaire():
    """ 11510850: Rescue Solaire in Gwyn's Tomb. """
    if CommonFlags.SolaireRescued:
        DisableCharacter(Chrs.Solaire)
        return
    SetTeamType(Chrs.Solaire, TeamType.WhitePhantom)
    EnableInvincibility(Chrs.Solaire)
    ForceAnimation(Chrs.Solaire, 7825, loop=True)
    Await(PlayerWithinDistance(Chrs.Solaire, 10.0))
    EnableFlag(CommonFlags.SolaireRescued)
    ForceAnimation(Chrs.Solaire, 7722, wait_for_completion=True)
    PlaySoundEffect(Chrs.Solaire, SoundType.s_SFX, 777777777)
    DisplayBattlefieldMessage(CommonTexts.SolaireRescued, 0)
    ForceAnimation(Chrs.Solaire, PlayerAnimations.StandingFadeOut)
    Wait(2.0)
    DisableCharacter(Chrs.Solaire)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11512999: Activate Abyss portal. """
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


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11512270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11512950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11512960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
