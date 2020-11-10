"""
linked:


strings:

"""
from soulstruct.events.darksouls1 import *
from .common_constants import *
from .firelink_constants import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(11020992, obj=1021960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=10)
    SkipLinesIfFlagOff(4, 11020300)
    SkipLinesIfFlagOn(2, 11020302)
    EndOfAnimation(1021000, 11)
    SkipLines(1)
    EndOfAnimation(1021000, 12)

    RunEvent(11025050)  # Crow now invincible.
    RunEvent(11020020)
    RunEvent(11020021)
    RunEvent(11020105)
    RunEvent(11020106)
    RunEvent(11020108)
    RunEvent(11020350)
    # New Londo gate permanently shut. (Also copied to two other places.)
    RunEvent(11020351)
    RunEvent(11020352)

    SetTeamType(Chrs.Crow, TeamType.WhitePhantom)
    EnableInvincibility(Chrs.Crow)

    PrologueEvent()
    ShowUncurlMessage()

    # Bonfire options (equipment and run options).
    GetStartingEquipment(0, Flags.GetWarriorEquipment, ItemLots.WarriorEquipment, 0)
    GetStartingEquipment(1, Flags.GetKnightEquipment, ItemLots.KnightEquipment, 0)
    GetStartingEquipment(2, Flags.GetWandererEquipment, ItemLots.WandererEquipment, 0)
    GetStartingEquipment(3, Flags.GetThiefEquipment, ItemLots.ThiefEquipment, CommonFlags.PolishedKeyObtained)
    GetStartingEquipment(4, Flags.GetBarbarianEquipment, ItemLots.BarbarianEquipment, 0)
    GetStartingEquipment(5, Flags.GetHunterEquipment, ItemLots.HunterEquipment, 0)
    GetStartingEquipment(6, Flags.GetSorcererEquipment, ItemLots.SorcererEquipment, 0)
    GetStartingEquipment(7, Flags.GetClericEquipment, ItemLots.ClericEquipment, 0)
    ActivateOneLifeMode()

    StartRun()

    if InsideMap(FIRELINK_SHRINE):
        DisableFlag(CommonFlags.RunHasStarted)  # In case of glitches.


def Preconstructor():
    """ 50: Event 50 """
    if InsideMap(FIRELINK_SHRINE):
        SetRespawnPoint(1022960)

    if CommonFlags.RequestFirelinkSpawnReset:
        SetRespawnPoint(1022960)
        DisableFlag(CommonFlags.RequestFirelinkSpawnReset)

    ForceAnimation(Chrs.Logan, 7830, loop=True)
    ForceAnimation(Chrs.Quelana, 7885, loop=True)
    ForceAnimation(Chrs.LobosJr, 7009, loop=True)

    ControlAllyAppearance(0, Chrs.Solaire, CommonFlags.SolaireRescued)
    ControlAllyAppearance(1, Chrs.Siegmeyer, CommonFlags.SiegmeyerRescued)
    ControlAllyAppearance(2, Chrs.Logan, CommonFlags.LoganRescued)
    ControlAllyAppearance(3, Chrs.Quelana, CommonFlags.QuelanaRescued)
    ControlAllyAppearance(4, Chrs.Havel, CommonFlags.HavelRescued)
    ControlAllyAppearance(5, Chrs.Mornstein, CommonFlags.MornsteinRescued)
    ControlAllyAppearance(6, Chrs.LobosJr, CommonFlags.LobosJrRescued)

    ReceiveGiftFromAlly(
        0, Chrs.Alvina, CommonFlags.LordvesselObtained, ItemLots.AlvinaGift, CommonTexts.ReceiveGiftAlvina, 4.0)
    ReceiveGiftFromAlly(
        1, Chrs.Solaire, CommonFlags.SolaireRescued, ItemLots.SolaireGift, CommonTexts.ReceiveGiftSolaire, 2.0)
    ReceiveGiftFromAlly(
        2, Chrs.Siegmeyer, CommonFlags.SiegmeyerRescued, ItemLots.SiegmeyerGift, CommonTexts.ReceiveGiftSiegmeyer, 2.0)
    ReceiveGiftFromAlly(
        3, Chrs.Logan, CommonFlags.LoganRescued, ItemLots.LoganGift, CommonTexts.ReceiveGiftLogan, 2.0)
    ReceiveGiftFromAlly(
        4, Chrs.Quelana, CommonFlags.QuelanaRescued, ItemLots.QuelanaGift, CommonTexts.ReceiveGiftQuelana, 2.0)
    ReceiveGiftFromAlly(
        5, Chrs.Havel, CommonFlags.HavelRescued, ItemLots.HavelGift, CommonTexts.ReceiveGiftHavel, 2.0)
    ReceiveGiftFromAlly(
        6, Chrs.Mornstein, CommonFlags.MornsteinRescued, ItemLots.MornsteinGift, CommonTexts.ReceiveGiftMornstein, 2.0)
    ReceiveGiftFromAlly(
        7, Chrs.LobosJr, CommonFlags.LobosJrRescued, ItemLots.LobosJrGift, CommonTexts.ReceiveGiftLobosJr, 2.0)


@RestartOnRest
def ControlAllyAppearance(_, ally: Character, rescued_flag: Flag):
    """ 11022200: Enable ally once rescued. """
    SetTeamType(ally, TeamType.WhitePhantom)
    EnableInvincibility(ally)
    if not FlagEnabled(11020500):
        return
    if not rescued_flag:
        DisableCharacter(ally)
        return


def ReceiveGiftFromAlly(_, ally: Character, rescued_flag: Flag, gift: ItemLotParam, prompt: Text, distance: float):
    """ 11022210: Get gift starting ring from ally. """
    if not rescued_flag:
        return
    Await(ActionButton(prompt, ally, anchor_type=CoordEntityType.Character, max_distance=distance))
    if CommonFlags.TwoAllyGiftsReceived:
        DisplayDialog(CommonTexts.TwoGiftsAlreadyReceived, ally)
        return RESTART
    AwardItemLot(gift)
    if CommonFlags.OneAllyGiftReceived:
        DisableFlag(CommonFlags.OneAllyGiftReceived)
        EnableFlag(CommonFlags.TwoAllyGiftsReceived)
    else:
        EnableFlag(CommonFlags.OneAllyGiftReceived)
    return


def Event11020300():
    """ 11020300: Event 11020300 """
    SkipLinesIfThisEventOff(2)
    RunEvent(11020301)
    End()
    IfThisEventOff(1)
    IfCharacterInsideRegion(1, PLAYER, region=1022003)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11020300)
    EnableFlag(11020302)
    ForceAnimation(1021000, 0, wait_for_completion=True)
    IfCharacterOutsideRegion(2, PLAYER, region=1022001)
    IfCharacterOutsideRegion(2, PLAYER, region=1022002)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()


def Event11020301():
    """ 11020301: Event 11020301 """
    IfSingleplayer(1)
    IfFlagOff(1, 11020302)
    IfCharacterInsideRegion(1, PLAYER, region=1022000)
    IfSingleplayer(2)
    IfFlagOn(2, 11020302)
    IfCharacterInsideRegion(2, PLAYER, region=1022001)
    IfSingleplayer(3)
    IfFlagOn(3, 11020302)
    IfCharacterInsideRegion(3, PLAYER, region=1022002)
    IfSingleplayer(4)
    IfFlagOff(4, 11020302)
    IfCharacterInsideRegion(4, PLAYER, region=1022003)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    SkipLinesIfFinishedConditionTrue(8, 2)
    SkipLinesIfFinishedConditionTrue(7, 3)
    EnableFlag(11020302)
    ForceAnimation(1021000, 2, wait_for_completion=True)
    IfCharacterOutsideRegion(5, PLAYER, region=1022001)
    IfCharacterOutsideRegion(5, PLAYER, region=1022002)
    IfConditionTrue(0, input_condition=5)
    ForceAnimation(1021000, 22, wait_for_completion=True)
    Restart()
    DisableFlag(11020302)
    ForceAnimation(1021000, 1, wait_for_completion=True)
    IfCharacterOutsideRegion(6, PLAYER, region=1022000)
    IfCharacterOutsideRegion(6, PLAYER, region=1022003)
    IfConditionTrue(0, input_condition=6)
    ForceAnimation(1021000, 21, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event11025050():
    """ 11025050: Event 11025050 """
    EnableImmortality(1020100)
    EnableInvincibility(1020100)


def Event11020020():
    """ 11020020: Event 11020020 """
    IfActionButton(0, prompt_text=10010506, anchor_entity=1022120, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0)
    SetStandbyAnimationSettings(PLAYER, standby_animation=7816)
    ForceAnimation(PLAYER, 7815, wait_for_completion=True)
    EnableFlag(11025060)
    WaitFrames(3)
    IfActionButton(1, prompt_text=10010507, anchor_entity=1022120, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0)
    IfCharacterOutsideRegion(2, PLAYER, region=1022120)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(11025060)
    RestartEvent(11020021, slot=0)
    ResetStandbyAnimationSettings(PLAYER)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(PLAYER, 7817, wait_for_completion=True)
    Restart()


def Event11020021():
    """ 11020021: Event 11020021 """
    DisableNetworkSync()
    IfFlagOn(0, 11025060)
    SkipLinesIfFlagOn(1, 11020000)
    Wait(20.0)
    PlayCutscene(100230, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1812110,
                 move_to_map=UNDEAD_ASYLUM)
    PlayCutscene(180130, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11020000)
    DisableFlag(11025060)
    ResetStandbyAnimationSettings(PLAYER)
    Restart()


def Event11020105():
    """ 11020105: Event 11020105 """
    DisableTreasure(1021300)
    DisableObject(1021961)
    EndIfFlagOn(11020108)
    SkipLinesIfFlagOn(5, 11020101)
    IfFlagOn(0, 11020100)
    EnableFlag(102)
    EnableTreasure(1021300)
    IfFlagOn(0, 11020101)
    DisableFlag(102)
    IfFlagOn(0, 11020108)
    RegisterBonfire(11020992, obj=1021960, reaction_distance=1.0, reaction_angle=180.0, initial_kindle_level=30)


def Event11020106():
    """ 11020106: Event 11020106 """
    DisableNetworkSync()
    IfFlagOn(1, 11020100)
    IfFlagOff(1, 11020101)
    IfActionButton(1, prompt_text=10010182, anchor_entity=1021960, anchor_type=CoordEntityType.Object,
                   facing_angle=180.0, max_distance=3.4000000953674316)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010184, anchor_entity=1021960, display_distance=3.4000000953674316,
                  button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.NoButton)
    Restart()


def Event11020108():
    """ 11020108: Event 11020108 """
    EndIfThisEventOn()
    IfFlagOn(-1, 71020022)
    IfFlagOn(-1, 71020023)
    IfConditionTrue(0, input_condition=-1)
    End()


def Event11020350():
    """ 11020350: Event 11020350 """
    SkipLinesIfThisEventOn(7)
    DisableObject(1021481)
    DisableCollision(1023510)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    EnableObject(1021481)
    EnableCollision(1023510)
    DisableObject(1021480)
    DisableCollision(1023500)
    DisableMapPiece(1023501)
    DisableCollision(1023502)


def Event11020351():
    """ 11020351: Event 11020351 """
    SkipLinesIfFlagOff(2, 0)
    DisableCollision(0)
    DisableCollision(0)
    IfCharacterInsideRegion(0, PLAYER, region=1022111)
    SkipLinesIfFlagOn(2, 710)
    Kill(PLAYER, award_souls=False)
    End()
    PlayCutscene(180060, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1802110,
                 move_to_map=KILN_OF_THE_FIRST_FLAME)
    WaitFrames(1)
    Restart()


def Event11020352():
    """ 11020352: Event 11020352 """
    IfFlagOn(0, 710)
    DisableCollision(1023600)
    DisableCollision(1023601)


def Event11020510(_, arg_0_3: int, arg_4_7: int):
    """ 11020510: Event 11020510 """
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
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020530(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020530: Event 11020530 """
    SkipLinesIfThisEventSlotOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfCharacterInsideRegion(2, arg_0_3, region=1022300)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    Kill(arg_0_3, award_souls=True)
    DisableGravity(arg_0_3)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020501():
    """ 11020501: Event 11020501 """
    IfFlagOn(1, 11010902)
    IfFlagOff(1, 11020693)
    IfFlagOff(1, 1176)
    IfFlagRangeAllOff(1, (1193, 1196))
    IfHealthLessThanOrEqual(2, 6070, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1177)
    IfAttacked(2, 6070, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(3, 6080, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1198)
    IfAttacked(3, 6080, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(4, 6090, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1214)
    IfAttacked(4, 6090, attacking_character=PLAYER)
    IfHealthLessThanOrEqual(5, 6100, 0.8999999761581421)
    SkipLinesIfFlagOn(1, 1224)
    IfAttacked(5, 6100, attacking_character=PLAYER)
    IfFlagOn(6, 1197)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(1, input_condition=-1)
    IfThisEventOn(7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFlagOn(2, 1177)
    EnableFlag(1176)
    EnableCharacter(6070)
    SetTeamType(6070, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1198)
    EnableFlag(1197)
    EnableCharacter(6080)
    SetTeamType(6080, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1214)
    EnableFlag(1213)
    EnableCharacter(6090)
    SetTeamType(6090, TeamType.HostileAlly)
    SkipLinesIfFlagOn(2, 1224)
    EnableFlag(1223)
    EnableCharacter(6100)
    SetTeamType(6100, TeamType.HostileAlly)
    SaveRequest()


def Event11020502(_, arg_0_3: int, arg_4_7: int):
    """ 11020502: Event 11020502 """
    IfFlagOff(7, 11010902)
    IfFlagOff(7, 1195)
    IfFlagOff(7, 1197)
    IfFlagOn(7, 1202)
    IfFlagOn(6, 11010902)
    IfFlagOff(6, 1195)
    IfFlagOff(6, 1197)
    IfFlagOn(6, 1193)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfThisEventOff(1)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020503(_, arg_0_3: int, arg_4_7: int):
    """ 11020503: Event 11020503 """
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1194)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileAlly)
    SaveRequest()


def Event11020504(_, arg_0_3: int, arg_4_7: int):
    """ 11020504: Event 11020504 """
    IfFlagOff(1, 1411)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttacked(1, arg_0_3, attacking_character=PLAYER)
    IfFlagOn(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 1)
    Move(arg_0_3, destination=1022700, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    SetNest(arg_0_3, 1022700)
    End()
    SetTeamType(arg_0_3, TeamType.Enemy)
    SetNest(arg_0_3, 1022700)
    AICommand(arg_0_3, command_id=1, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=1022700)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    EnableFlag(arg_4_7)


def Event11020550(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020550: Event 11020550 """
    IfFlagOff(1, 1096)
    IfFlagOff(1, 1099)
    IfFlagOn(1, 1091)
    IfFlagOn(1, 11500594)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020551(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020551: Event 11020551 """
    IfFlagOff(1, 1096)
    IfFlagOff(1, 1099)
    IfFlagOn(1, 1092)
    IfFlagOn(1, 11020603)
    IfOutsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableFlag(11020694)
    DisableCharacter(arg_0_3)


def Event11020552(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020552: Event 11020552 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1111)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020553(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020553: Event 11020553 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1112)
    IfFlagOn(1, 11020694)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020554(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020554: Event 11020554 """
    IfFlagOff(1, 1114)
    IfFlagOff(1, 1117)
    IfFlagOn(1, 1113)
    IfFlagOn(1, 723)
    IfInsideMap(1, game_map=SENS_FORTRESS)
    EndIfConditionFalse(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020555(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020555: Event 11020555 """
    IfFlagOn(1, 1140)
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1575)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-1, input_condition=2)
    IfFlagOn(-1, 11500200)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020556(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020556: Event 11020556 """
    IfFlagOn(1, 1141)
    IfFlagOn(1, 810)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020557(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020557: Event 11020557 """
    IfFlagOn(1, 1146)
    IfFlagOn(1, 11020609)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020558(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020558: Event 11020558 """
    IfFlagOn(1, 1142)
    IfFlagOn(1, 11800200)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020559():
    """ 11020559: Event 11020559 """
    IfFlagOn(1, 1170)
    IfFlagOn(1, 11010902)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1170, 1189))
    EnableFlag(1171)
    EnableCharacter(6070)
    DisableFlagRange((1210, 1219))
    EnableFlag(1211)
    EnableCharacter(6090)
    DisableFlagRange((1220, 1229))
    EnableFlag(1221)
    EnableCharacter(6100)


def Event11020560():
    """ 11020560: Event 11020560 """
    IfFlagRangeAllOff(7, (1176, 1181))
    IfFlagOn(7, 1171)
    IfFlagRangeAllOff(7, (1195, 1198))
    IfFlagOn(7, 1202)
    IfFlagRangeAllOff(7, (1213, 1215))
    IfFlagOn(7, 1211)
    IfFlagRangeAllOff(7, (1223, 1225))
    IfFlagOn(7, 1221)
    IfConditionTrue(1, input_condition=7)
    IfFlagOn(1, 11020600)
    IfThisEventOff(1)
    IfConditionTrue(2, input_condition=7)
    IfFlagOn(2, 11300005)
    IfConditionTrue(3, input_condition=7)
    IfThisEventOn(3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    ClearEventValue(600, bit_count=4)
    EnableFlag(11020693)
    DisableFlagRange((1170, 1189))
    EnableFlag(1173)
    DisableCharacter(6070)
    DisableFlagRange((1190, 1209))
    EnableFlag(1192)
    DisableCharacter(6080)
    DisableFlagRange((1210, 1219))
    EnableFlag(1216)
    DisableCharacter(6090)
    DisableFlagRange((1220, 1229))
    EnableFlag(1226)
    DisableCharacter(6100)


def Event11020564(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020564: Event 11020564 """
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1192)
    EndIfConditionFalse(1)
    SkipLinesIfFlagOn(2, 11020692)
    EnableFlag(11020692)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020565(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020565: Event 11020565 """
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1197)
    IfFlagOn(1, 1193)
    IfFlagOn(1, 11020608)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020567(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020567: Event 11020567 """
    IfFlagOn(-2, 1194)
    IfFlagOn(-2, 1195)
    IfConditionTrue(1, input_condition=-2)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1196)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11020569(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020569: Event 11020569 """
    IfFlagOff(1, 1194)
    IfFlagOff(1, 1195)
    IfFlagOff(1, 1196)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    IfFlagOn(2, 1198)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EndIfFinishedConditionTrue(1)
    DropMandatoryTreasure(arg_0_3)


def Event11020574(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020574: Event 11020574 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1251)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020575(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020575: Event 11020575 """
    IfFlagOff(1, 1253)
    IfFlagOn(1, 1252)
    IfFlagOn(1, 11020102)
    IfFlagOn(1, 11020103)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020576(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020576: Event 11020576 """
    IfFlagOff(1, 1314)
    IfFlagOn(1, 1312)
    IfFlagOn(1, 11600593)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020577(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020577: Event 11020577 """
    IfFlagOff(1, 1461)
    IfFlagOff(1, 1464)
    IfFlagOn(1, 1460)
    IfFlagOn(1, 11020597)
    IfOutsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020579(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020579: Event 11020579 """
    IfFlagOff(1, 1512)
    IfFlagOn(1, 1494)
    IfFlagOn(1, 11510590)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020583(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020583: Event 11020583 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1542)
    IfFlagOn(1, 11700593)
    IfFlagOff(1, 1512)
    IfFlagOff(1, 1513)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020584(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020584: Event 11020584 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1543)
    IfFlagOn(1, 11020605)
    IfThisEventOff(1)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1543)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020585(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020585: Event 11020585 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1544)
    IfFlagOn(1, 11410593)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020586(_, arg_0_3: int):
    """ 11020586: Event 11020586 """
    IfFlagOff(1, 1547)
    IfFlagOn(1, 1545)
    IfFlagOn(1, 11020606)
    IfThisEventOff(1)
    IfFlagOff(2, 1547)
    IfFlagOn(2, 1545)
    IfThisEventOn(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    DisableCharacter(arg_0_3)


def Event11020587(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020587: Event 11020587 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(1, 1571)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(11020690)
    EnableFlag(11020691)


def Event11020588(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 11020588: Event 11020588 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(1, 1572)
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(2, 1577)
    IfFlagOff(3, 1574)
    IfFlagOff(3, 1578)
    IfFlagOn(3, 1573)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(6, 3)
    EnableRandomFlagInRange((11025120, 11025122))
    IfFlagOn(0, 11025120)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)
    End()
    SkipLinesIfFlagOff(4, 11020691)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    EnableCharacter(arg_0_3)
    End()
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_20_23)
    EnableCharacter(arg_0_3)


def Event11020589(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020589: Event 11020589 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(-1, 1570)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 3)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    EnableFlag(11020690)


def Event11020410(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020410: Event 11020410 """
    IfFlagOff(1, 1574)
    IfFlagOff(1, 1578)
    IfFlagOn(-1, 1572)
    IfFlagOn(-1, 1573)
    IfFlagOn(-1, 1577)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(2, 812)
    IfFlagOn(2, 813)
    IfConditionTrue(-2, input_condition=2)
    IfFlagOn(-2, 11500200)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    DisableCharacter(arg_0_3)


def Event11020411(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020411: Event 11020411 """
    IfFlagOff(1, 1622)
    IfFlagOff(1, 1625)
    IfFlagOff(1, 1627)
    IfFlagOff(1, 1628)
    IfFlagOn(1, 1624)
    IfFlagOn(1, 7)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020412(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020412: Event 11020412 """
    IfFlagOff(1, 1434)
    IfFlagOff(1, 1435)
    IfFlagOn(1, 1430)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)


def Event11020413(_, arg_0_3: int, arg_4_7: int):
    """ 11020413: Event 11020413 """
    SkipLinesIfThisEventOff(2)
    DropMandatoryTreasure(arg_0_3)
    End()
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    DisableFlag(1434)
    EnableFlag(arg_4_7)


def Event11020420(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020420: Event 11020420 """
    IfFlagOn(1, 1640)
    IfFlagOn(1, 11010700)
    IfFlagOn(2, 1640)
    IfFlagOn(2, 11400200)
    IfFlagOn(3, 1641)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=9000)


def Event11020421(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020421: Event 11020421 """
    IfFlagOn(1, 1641)
    IfFlagOn(1, 11010700)
    IfFlagOn(1, 11400200)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    EnableCharacter(arg_0_3)
    SetStandbyAnimationSettings(arg_0_3, standby_animation=7003)


def Event11020422(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020422: Event 11020422 """
    IfFlagOn(1, 1642)
    IfFlagOn(1, 710)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020423(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020423: Event 11020423 """
    IfFlagOn(1, 1643)
    IfFlagOn(1, 820)
    IfFlagOn(1, 11800100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)


def Event11020424(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020424: Event 11020424 """
    IfFlagOn(1, 1649)
    IfFlagOn(1, 11020598)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11020425(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11020425: Event 11020425 """
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfFlagOn(-1, 11020598)
    IfHealthLessThanOrEqual(2, arg_0_3, 0.8999999761581421)
    IfHealthGreaterThan(2, arg_0_3, 0.0)
    IfAttacked(2, arg_0_3, attacking_character=PLAYER)
    IfEntityBeyondDistance(2, arg_0_3, PLAYER, radius=15.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_12_15)
    ForceAnimation(arg_0_3, 7005, wait_for_completion=True)
    DisableCharacter(arg_0_3)


def Event11026200():
    """ 11026200: Event 11026200 """
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    IfConditionTrue(1, input_condition=-1)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfFlagOn(1, 820)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(820)
    EnableFlag(830)
    EnableCharacter(6331)
    PlayCutscene(100240, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1802110,
                 move_to_map=KILN_OF_THE_FIRST_FLAME)
    PlayCutscene(180040, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(822)
    Restart()


def Event11026210():
    """ 11026210: Event 11026210 """
    DisableFlag(1650)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfEntityBeyondDistance(1, 6330, PLAYER, radius=30.0)
    IfFlagOff(1, 830)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(-1, 1643)
    IfFlagOn(-1, 1644)
    IfFlagOn(-1, 1645)
    EndIfConditionFalse(-1)
    DisableFlagRange((11026211, 11026213))
    EnableRandomFlagInRange((11026211, 11026213))
    EndIfFlagOn(11026211)
    EnableFlag(1650)
    SetStandbyAnimationSettings(6330, standby_animation=9001)
    IfAttacked(0, 6330, attacking_character=PLAYER)
    AddSpecialEffect(6330, 5450)
    SetStandbyAnimationSettings(6330, standby_animation=7003)
    ForceAnimation(6330, 9061, wait_for_completion=True)
    DisableFlag(1650)


def Event11020110():
    """ 11020110: Event 11020110 """
    EnableImmortality(6060)
    EndIfFlagOn(11020101)
    SkipLinesIfFlagOn(1, 11020100)
    IfFlagOn(0, 1141)
    EzstateAIRequest(6060, command_id=1702, slot=0)
    EnableFlag(11020100)
    SkipLinesIfFlagOn(4, 11020111)
    IfFlagOn(0, 11020609)
    EzstateAIRequest(6060, command_id=1701, slot=0)
    EnableFlag(11020111)
    IfHasTAEEvent(0, 6060, tae_event_id=1701)
    EnableFlag(11020101)


def StartRun():
    """ 11020200: Script runs when a run starts. (Not that much to do.) """
    Await(HasGood(600) and ActionButton(CommonTexts.StartRun, Chrs.Crow, facing_angle=180.0, max_distance=3.0))

    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)

    # Make ring modifications.
    DisableFlagRange((1961, 1967))  # disable all flags (in case this is triggered multiple times)
    if HasRing(Rings.SolaireRing):
        EnableFlag(CommonFlags.SolaireRingFlag)
    if HasRing(Rings.SiegmeyerRing):
        EnableFlag(CommonFlags.SiegmeyerRingFlag)
    if HasRing(Rings.LoganRing):
        EnableFlag(CommonFlags.LoganRingFlag)
    if HasRing(Rings.QuelanaRing):
        EnableFlag(CommonFlags.QuelanaRingFlag)
    # No need for Havel flag.
    if HasRing(Rings.MornsteinRing):
        EnableFlag(CommonFlags.MornsteinRingFlag)
    if HasRing(Rings.LobosJrRing):
        EnableFlag(CommonFlags.LobosJrRingFlag)

    DisableFlag(CommonFlags.RunSetupCompleteFlag)
    EnableFlag(CommonFlags.DoRunSetupFlag)
    Await(CommonFlags.RunSetupCompleteFlag)  # Wait until mod program has finished setting up new run.
    DisableFlag(CommonFlags.DoRunSetupFlag)

    # Calculate starting lives. May have already been set to 1 by trading four lives at Firelink bonfire.
    if HasRing(Rings.AlvinaRing):
        if FlagEnabled(CommonFlags.LifeCount1):
            # Player has traded four lives for Blessings. Give them four lives back.
            DisableFlag(CommonFlags.LifeCount1)
            EnableFlag(CommonFlags.LifeCount5)
        else:
            # Player has nine lives.
            EnableFlag(CommonFlags.LifeCount9)
    else:
        if FlagDisabled(CommonFlags.LifeCount1):
            # Player has NOT traded four lives for Blessings. Start with five lives.
            EnableFlag(CommonFlags.LifeCount5)


def PrologueEvent():
    """ 11020500: Allies vanish and Alvina appears when you pick up the Hand of Cessation. """
    DeleteFX(FXEvents.SolairePortal, False)
    DeleteFX(FXEvents.SiegmeyerPortal, False)
    DeleteFX(FXEvents.LoganPortal, False)
    DeleteFX(FXEvents.QuelanaPortal, False)
    DeleteFX(FXEvents.HavelPortal, False)
    DeleteFX(FXEvents.MornsteinPortal, False)
    DeleteFX(FXEvents.LobosJrPortal, False)
    if THIS_FLAG:
        DisableGravity(Chrs.Alvina)
        DisableCollision(Chrs.Alvina)
        EnableInvincibility(Chrs.Alvina)
        SetTeamType(Chrs.Alvina, TeamType.WhitePhantom)
        return

    DisableCharacter(1020960)  # Bonfire interaction.
    DisableCharacter(Chrs.Alvina)
    if not FlagEnabled(11020501):
        ForceAnimation(PLAYER, 7711, loop=True)
        Wait(3.0)
        ForceAnimation(PLAYER, 7712)
        EnableFlag(11020501)

    Await(HasGood(CommonGoods.HandOfCessation))

    EnableFlag(11020500)

    Wait(1.0)

    PlaySoundEffect(Chrs.Solaire, SoundType.s_SFX, 777777777)
    Wait(2.0)
    # TODO: Portal effect not working.
    CreateFX(FXEvents.SolairePortal)
    CreateFX(FXEvents.SiegmeyerPortal)
    CreateFX(FXEvents.LoganPortal)
    CreateFX(FXEvents.QuelanaPortal)
    CreateFX(FXEvents.HavelPortal)
    CreateFX(FXEvents.MornsteinPortal)
    CreateFX(FXEvents.LobosJrPortal)
    Wait(1.0)
    ForceAnimation(Chrs.Solaire, 11)
    ForceAnimation(Chrs.Siegmeyer, 11)
    ForceAnimation(Chrs.Logan, 11)
    ForceAnimation(Chrs.Quelana, 11)
    ForceAnimation(Chrs.Havel, 11)
    ForceAnimation(Chrs.Mornstein, 11)
    ForceAnimation(Chrs.LobosJr, 11)
    Wait(1.9)
    DisableCharacter(Chrs.Solaire)
    DisableCharacter(Chrs.Siegmeyer)
    DisableCharacter(Chrs.Logan)
    DisableCharacter(Chrs.Quelana)
    DisableCharacter(Chrs.Havel)
    DisableCharacter(Chrs.Mornstein)
    DisableCharacter(Chrs.LobosJr)

    DeleteFX(FXEvents.SolairePortal, True)
    DeleteFX(FXEvents.SiegmeyerPortal, True)
    DeleteFX(FXEvents.LoganPortal, True)
    DeleteFX(FXEvents.QuelanaPortal, True)
    DeleteFX(FXEvents.HavelPortal, True)
    DeleteFX(FXEvents.MornsteinPortal, True)
    DeleteFX(FXEvents.LobosJrPortal, True)

    EnableCharacter(1020960)  # Bonfire interaction.
    EnableCharacter(Chrs.Alvina)
    DisableGravity(Chrs.Alvina)
    DisableCollision(Chrs.Alvina)
    EnableInvincibility(Chrs.Alvina)
    SetTeamType(Chrs.Alvina, TeamType.WhitePhantom)
    ForceAnimation(Chrs.Alvina, 10)


def ShowUncurlMessage():
    """ 11020250: Show "fingers uncurl" message when requested (on permadeath). """
    Await(CommonFlags.ShowUncurlMessage and InsideMap(FIRELINK_SHRINE))
    DisplayStatus(CommonTexts.FingersUncurl)
    DisableFlag(CommonFlags.ShowUncurlMessage)
    return RESTART


def GetStartingEquipment(_, trigger_flag: Flag, item_lot: ItemLotParam, item_lot_flag: int):
    """ 11022400: Receive starting equipment from Firelink bonfire. """
    DisableFlag(trigger_flag)
    Await(FlagEnabled(trigger_flag))
    Wait(1.0)
    if CommonFlags.StartingEquipmentReceived:
        DisplayDialog(15000550)
        return RESTART
    AwardItemLot(item_lot, host_only=True)
    if item_lot_flag != 0:
        EnableFlag(item_lot_flag)
    EnableFlag(CommonFlags.StartingEquipmentReceived)
    return RESTART


def ActivateOneLifeMode():
    """ 11022410: Go to one-life mode for the next run and receive four Divine Blessings. """
    DisableFlag(11022410)
    Await(FlagEnabled(11022410))
    Wait(1.0)
    if FlagEnabled(1908):
        # Already done.
        DisplayDialog(15000551)
        return RESTART
    AwardItemLot(ItemLots.OneLifeModeGift)
    DisableFlagRange((1900, 1909))
    EnableFlag(1908)  # One life left.
    return RESTART
