from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_20


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_18


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_29


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=2)
        SetFlagState(flag=71510024, state=1)
        SetFlagState(flag=844, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_8
        if GetFlagState(844) == 0:
            return State_43
        if GetFlagState(844) == 0:
            return State_44


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        DebugEvent(message='誓約を変更しない')

    def test(self):
        return State_1


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=2)
        RequestUnlockTrophy(8)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_8
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_7
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_7


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_18


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_3, State_6, State_44]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_29


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        TalkToPlayer(conversation=21000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_32


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_9


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_18, State_27]

    def enter(self):
        AddTalkListData(menu_index=2, menu_text=15000200, required_flag=-1)
        AddTalkListData(menu_index=1, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if GetTalkListEntryResult() == 0:
            return State_46
        if GetTalkListEntryResult() == 4:
            return State_46
        if GetTalkListEntryResult() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_24
        if GetTalkListEntryResult() == 2:
            return State_35

    def exit(self):
        ClearTalkListData()


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_14, State_23, State_24]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_29


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_23, State_24]

    def enter(self):
        TalkToPlayer(conversation=21000300, unk1=-1, unk2=-1)

    def test(self):
        if GetDistanceToPlayer() >= 15:
            return State_13
        if HasTalkEnded() == 1:
            return State_33


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        if GetFlagState(11515351) == 1:
            return State_29
        else:
            return State_20


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_15


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        TalkToPlayer(conversation=21000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_1, State_7, State_53, State_55]

    def test(self):
        return State_12
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_29


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_9, State_17, State_28, State_30, State_32, State_38, State_39, State_41, State_47, State_50, State_52, State_54, State_56]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 15:
            return State_36
        if GetFlagState(1231) == 1:
            return State_16
        if GetFlagState(71510028) == 1:
            return State_16
        else:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_0, State_9, State_15, State_21, State_22, State_26, State_29, State_32, State_34, State_36, State_46, State_48, State_57]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=30)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1232) == 0 and GetDistanceToPlayer() <= 15:
            return State_34
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 12 and GetOneLineHelpStatus() == 1 and GetFlagState(71510020) == 1:
            return State_45
        if GetFlagState(1230) == 1 and GetFlagState(71510020) == 0 and GetDistanceToPlayer() <= 16 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 16:
            return State_56
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 12 and GetFlagState(1231) == 0 and GetFlagState(1232) == 0:
            return State_21
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 12):
            return State_22
        if IsAttackedBySomeone() == 1 and GetFlagState(1232) == 0:
            return State_28


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        DisplayOneLineHelp(text_id=10010210)

    def test(self):
        return State_20


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_20


class State_23(State):
    """ 23: No description. """

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 15:
            return State_36
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_14
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_13


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 15:
            return State_36
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_14
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_13


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_9, State_17, State_30, State_32, State_34, State_36, State_38, State_39, State_41, State_47, State_50, State_52, State_54, State_56]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_26


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_20


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_17, State_42, State_51]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_12
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_29


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_19


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_2, State_8, State_13, State_15, State_18, State_27, State_31, State_33, State_37, State_40, State_43]

    def enter(self):
        SetFlagState(flag=11515351, state=0)

    def test(self):
        return State_20


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        TalkToPlayer(conversation=21000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsPlayerDead() == 1:
            return State_25


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71510021, state=1)
        SetFlagState(flag=11510592, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 15:
            return State_29
        if IsMenuOpen(63) == 0 and GetDistanceToPlayer() <= 15:
            return State_38


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        TalkToPlayer(conversation=21000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71510026, state=1)
        SetFlagState(flag=71510027, state=0)

    def test(self):
        return State_29


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        TalkToPlayer(conversation=21000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_20
        if GetDistanceToPlayer() >= 16:
            return State_25


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_12]

    def test(self):
        if ComparePlayerStatus(11, 0, 2) == 1:
            return State_6
        else:
            return State_5


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_19, State_23, State_24, State_37]

    def enter(self):
        TalkToPlayer(conversation=21000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_20
        if GetDistanceToPlayer() >= 16:
            return State_25


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_5, State_6, State_44]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 15:
            return State_36
        else:
            return State_29


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_31, State_45]

    def enter(self):
        TalkToPlayer(conversation=21000110, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_39(State):
    """ 39: No description. """

    def enter(self):
        TalkToPlayer(conversation=21000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71510022, state=1)
        SetFlagState(flag=11516101, state=1)

    def test(self):
        return State_29


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        TalkToPlayer(conversation=21000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        SetFlagState(flag=71510023, state=1)

    def test(self):
        return State_27


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        SetFlagState(flag=11510595, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 15:
            return State_29
        if IsMenuOpen(63) == 0 and GetDistanceToPlayer() <= 15:
            return State_44


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_3, State_43]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わしました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_8
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_50
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_50


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)

    def test(self):
        if GetFlagState(71510023) == 0 and GetFlagState(11800200) == 1:
            return State_41
        if GetFlagState(71510022) == 1:
            return State_17
        if GetFlagState(71510022) == 0 and GetFlagState(71510021) == 1:
            return State_38
        if GetFlagState(71510021) == 0:
            return State_30

    def exit(self):
        SetFlagState(flag=11515351, state=1)


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=11515351, state=0)

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_10
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_11
        else:
            return State_20


class State_47(State):
    """ 47: No description. """

    def enter(self):
        TalkToPlayer(conversation=21000150, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_48(State):
    """ 48: No description. """

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_12]

    def test(self):
        if GetFlagState(71510015) == 1:
            return State_54
        if GetFlagState(71510015) == 0:
            return State_52


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=21000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=71510017, state=1)

    def test(self):
        return State_27


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        TalkToPlayer(conversation=21000700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsPlayerDead() == 1:
            return State_25


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=71510015, state=1)

    def test(self):
        return State_18


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        TalkToPlayer(conversation=21000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsPlayerDead() == 1:
            return State_25


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        SetFlagState(flag=71510016, state=1)

    def test(self):
        return State_18


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceCloseMenu()
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=21000000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_57
        if GetDistanceToPlayer() >= 16:
            return State_25


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71510020, state=1)

    def test(self):
        return State_20
