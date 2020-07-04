from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_14


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_25, State_26]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_13


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=8)
        SetFlagState(flag=71510037, state=1)
        SetFlagState(flag=844, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_8
        if GetFlagState(844) == 0 and (GetFlagState(11510596) == 0 or GetFlagState(11510580) == 0):
            return State_42
        if GetFlagState(844) == 0:
            return State_47


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        DebugEvent(message='誓約を変更しない')
        SetFlagState(flag=71510038, state=1)

    def test(self):
        return State_26


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=8)
        RequestUnlockTrophy(9)

    def test(self):
        if IsMultiplayerInProgress() == 1:
            return State_50
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_29
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_3
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_8
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_7
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_7


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_6, State_50]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_3, State_6, State_47, State_50]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_13, State_19]

    def enter(self):
        AddTalkListData(menu_index=2, menu_text=15000264, required_flag=858)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000200, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_16
        if GetTalkListEntryResult() == 0:
            return State_20
        if GetTalkListEntryResult() == 4:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_16
        if GetTalkListEntryResult() == 3:
            return State_24
        if GetTalkListEntryResult() == 2:
            return State_41

    def exit(self):
        ClearTalkListData()


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_11, State_15, State_16]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_20


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_15, State_16]

    def test(self):
        if GetDistanceToPlayer() >= 17:
            return State_10
        else:
            return State_23


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=22000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17
        if HasTalkEnded() == 1:
            return State_30


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_1, State_7, State_35, State_39, State_45]

    def test(self):
        return State_9
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 18:
        #     return State_20


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_0, State_18, State_20, State_28]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if GetFlagState(11510593) == 0 and GetFlagState(71510036) == 0 and GetFlagState(11516102) == 0 and GetDistanceToPlayer() <= 12 and GetFlagState(1241) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 12 and GetFlagState(1242) == 0:
            return State_27
        if GetFlagState(11515350) == 1:
            return State_51


class State_15(State):
    """ 15: No description. """

    def enter(self):
        CloseMenu()

    def test(self):
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_11
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_10


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_11
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_10


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_12, State_21, State_25, State_26, State_27, State_31]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_18


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_14


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_30, State_32]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_9
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 18:
        #     return State_20


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_2, State_8, State_9, State_10, State_13, State_19, State_23, State_29, State_33, State_40, State_42, State_43, State_46]

    def enter(self):
        SetFlagState(flag=11515350, state=0)

    def test(self):
        return State_14


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=22000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17
        if HasTalkEnded() == 1:
            return State_22


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71510036, state=1)

    def test(self):
        return State_24


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        SetFlagState(flag=71510041, state=1)
        SetFlagState(flag=71510042, state=0)

    def test(self):
        return State_20


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_9, State_22]

    def test(self):
        if ComparePlayerStatus(11, 0, 8) == 1:
            return State_6
        if IsMultiplayerInProgress() == 1:
            return State_50
        else:
            return State_5


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        TalkToPlayer(conversation=22001000, unk1=-1, unk2=-1)
        DebugEvent(message='誓約したあと')

    def test(self):
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        TalkToPlayer(conversation=22001100, unk1=-1, unk2=-1)
        DebugEvent(message='誓約しなかったあと')

    def test(self):
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=22000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17
        if HasTalkEnded() == 1:
            return State_28


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        SetFlagState(flag=71510035, state=1)
        SetFlagState(flag=11510593, state=1)
        SetFlagState(flag=11516102, state=1)

    def test(self):
        return State_14


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_5, State_6, State_47, State_50]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71510039, state=1)

    def test(self):
        return State_19


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=22000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_17
        if HasTalkEnded() == 1:
            return State_32


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71510039, state=0)

    def test(self):
        return State_19


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_34, State_36, State_37]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DebugEvent(message='捧げる')
        ChangePlayerStats(unk1=15, unk2=0, unk3=1)
        PlayerEquipmentQuantityChange(3, 374, -1)
        SetFlagState(flag=844, state=1)

    def test(self):
        if DoesSelfHaveSpEffect(22, 10) == 1 and GetFlagState(844) == 0 and (GetFlagState(11510597) == 0 or GetFlagState(11510581) == 0):
            return State_43
        if DoesSelfHaveSpEffect(22, 80) == 1 and GetFlagState(844) == 0:
            return State_49
        if DoesSelfHaveSpEffect(22, 30) == 1 and GetFlagState(844) == 0:
            return State_49
        if DoesSelfHaveSpEffect(22, 10) == 1 and GetFlagState(844) == 0:
            return State_49
        if GetFlagState(844) == 0:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_33


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_36, State_37]

    def enter(self):
        DebugEvent(message='捧げない')

    def test(self):
        return State_13


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020204, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_33
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_35
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_35
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_37


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        DebugEvent(message='DECIDE_NUMBER')
        OpenGenericDialog(unk1=3, text_id=10020204, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_33
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_35
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_35
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_34


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010784, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_40
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_39


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_38, State_48, State_49]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_38, State_48, State_49]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_9]

    def test(self):
        if ComparePlayerStatus(22, 0, 100) == 1:
            return State_44
        if IsEquipmentIDObtained(3, 374) == 0:
            return State_38
        else:
            return State_36


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        SetFlagState(flag=11510596, state=1)
        SetFlagState(flag=11510580, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 15:
            return State_20
        if IsMenuOpen(63) == 0:
            return State_47


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=11510597, state=1)
        SetFlagState(flag=11510581, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 15:
            return State_20
        if IsMenuOpen(63) == 0:
            return State_49


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010794, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_46
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_45
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_45


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_3, State_42]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わしました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_8
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_25
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_25


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010796, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ポイントアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_40
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_39


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_34, State_43]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010797, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ランクアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_40
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_39


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_5, State_24]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010747, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='マルチプレイ中')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_8
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_7
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_7


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)

    def test(self):
        if GetFlagState(11515350) == 1 and GetFlagState(71510037) == 0 and GetDistanceToPlayer() <= 12 and GetFlagState(1240) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 12:
            return State_21
        if GetFlagState(11515350) == 1 and GetFlagState(71510039) == 0 and GetDistanceToPlayer() <= 12 and GetFlagState(71510037) == 1 and GetFlagState(1240) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 12:
            return State_12
        if GetFlagState(11515350) == 1 and GetFlagState(71510039) == 1 and GetDistanceToPlayer() <= 12 and GetFlagState(71510037) == 1 and GetFlagState(1240) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 12:
            return State_31
