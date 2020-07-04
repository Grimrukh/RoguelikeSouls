from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_19


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        TalkToPlayer(conversation=23010300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_31


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_1


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        OpenRegularShop(3000, 3099)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22
        if IsMenuOpen(11) == 0:
            return State_6


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_4, State_17, State_26, State_82]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000190, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_23
        if GetTalkListEntryResult() == 0:
            return State_28
        if GetTalkListEntryResult() == 3:
            return State_34
        if GetTalkListEntryResult() == 1:
            return State_5
        if GetTalkListEntryResult() == 2:
            return State_82
        if GetTalkListEntryResult() == 4:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_23

    def exit(self):
        ClearTalkListData()


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_8, State_22, State_23]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_22, State_23, State_42, State_66]

    def enter(self):
        TalkToPlayer(conversation=23010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if GetDistanceToPlayer() >= 12:
            return State_7
        if HasTalkEnded() == 1:
            return State_32


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        SetFlagState(flag=71000005, state=1)

    def test(self):
        return State_11


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=23010800, unk1=-1, unk2=-1)
        SetFlagState(flag=71000005, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_24


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9, State_12, State_13, State_53, State_55]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_19


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_11


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71000004, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=23010700, unk1=-1, unk2=-1)
        SetFlagState(flag=71000004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23010100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_33, State_58, State_60, State_72, State_77]

    def test(self):
        return State_6
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_19


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_1, State_8, State_15, State_16, State_27, State_29, State_31, State_36, State_37, State_39, State_46, State_47, State_49, State_51, State_57, State_59, State_61, State_63, State_64, State_69, State_70, State_76, State_78, State_80, State_81]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_73
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71000005) == 0 and GetSelfHP() <= 90:
            return State_10
        if GetFlagState(1253) == 1:
            return State_12
        if GetFlagState(71000004) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        if GetFlagState(71000004) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71000016) == 0:
            return State_54
        if GetFlagState(71000016) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71000017) == 0:
            return State_56
        if GetFlagState(71000017) == 1:
            return State_12
        else:
            return State_12

    def exit(self):
        RemoveMyAggro()


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_0, State_1, State_7, State_11, State_17, State_20, State_21, State_22, State_25, State_26, State_28, State_31, State_32, State_35, State_38, State_41, State_50, State_51, State_73, State_75, State_79]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1254) == 0 and GetDistanceToPlayer() <= 5:
            return State_38
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11025021) == 1:
            return State_36
        if GetFlagState(11020103) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11020102) == 1 and GetFlagState(71000022) == 1 and GetFlagState(11026102) == 0 and GetFlagState(71000020) == 0:
            return State_61
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71000020) == 1 and GetFlagState(11020102) == 1 and GetFlagState(11020103) == 1:
            return State_63
        if GetFlagState(71000001) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71000015) == 0:
            return State_39
        if GetFlagState(71000001) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_29
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71000015) == 1 and GetFlagState(71000022) == 0 and GetFlagState(740) == 1:
            return State_81
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71000015) == 1 and GetFlagState(71000022) == 0 and GetFlagState(740) == 0:
            return State_46
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71000015) == 1:
            return State_15
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1253) == 0 and GetFlagState(1254) == 0:
            return State_20
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_21
        if IsAttackedBySomeone() == 1 and GetFlagState(1254) == 0:
            return State_27


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_19


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_19


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_4, State_82]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_73
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7
        else:
            return State_19


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_73
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_1, State_10, State_14, State_15, State_16, State_29, State_31, State_36, State_37, State_38, State_39, State_46, State_47, State_49, State_51, State_54, State_56, State_57, State_59, State_61, State_63, State_64, State_69, State_70, State_73, State_76, State_78, State_80, State_81]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_15, State_52, State_63, State_65]

    def enter(self):
        ClearTalkActionState()
        SetFlagState(flag=365, state=1)

    def test(self):
        return State_6
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_19


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_18


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1 or DidYouDoSomethingInTheMenu(4) == 1:
            return State_2
        if DidYouDoSomethingInTheMenu(11) == 0 or DidYouDoSomethingInTheMenu(4) == 0:
            return State_3
        else:
            return State_19


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23010000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        SetFlagState(flag=71000001, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        return State_45


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=23010400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11025021, state=1)

    def test(self):
        return State_19


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        SetFlagState(flag=71000003, state=1)

    def test(self):
        return State_17


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71000020) == 1 and GetFlagState(11020102) == 1 and GetFlagState(11020103) == 0 and GetFlagState(71000021) == 1:
            return State_64
        if GetFlagState(71000019) == 1 and GetFlagState(11026102) == 0 and GetFlagState(71000021) == 0:
            return State_37
        if GetFlagState(71000018) == 1 and GetFlagState(11026102) == 0 and GetFlagState(71000019) == 0:
            return State_59
        if GetFlagState(71000003) == 1 and GetFlagState(71000018) == 0:
            return State_57
        if GetFlagState(71000003) == 0:
            return State_16
        if GetFlagState(71000003) == 1 and GetFlagState(740) == 1:
            return State_76
        if GetFlagState(71000003) == 1 and GetFlagState(740) == 0:
            return State_78


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        SetFlagState(flag=11025021, state=0)

    def test(self):
        return State_19


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23010600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_72
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_19, State_74]

    def enter(self):
        TalkToPlayer(conversation=23010900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 5:
            return State_24


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23010120, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        DebugEvent(message='人間性取り戻した')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71000002, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        return State_45


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_19


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_8


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        DebugEvent(message='呪術を教わる')
        SetFlagState(flag=71000015, state=1)

    def test(self):
        if GetFlagState(740) == 1:
            return State_81
        if GetFlagState(740) == 0:
            return State_46


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        DebugEvent(message='呪術を教わらない')

    def test(self):
        return State_47


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_30, State_40]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_42
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_44
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(71000002) == 0:
            return State_44
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0 and GetFlagState(71000002) == 1:
            return State_44
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0 and GetFlagState(71000002) == 0:
            return State_43
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(71000002) == 1:
            return State_43


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_19, State_43]

    def enter(self):
        TalkToPlayer(conversation=23010020, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_79
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_24


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=23010040, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_48(State):
    """ 48: No description. """

    def enter(self):
        DebugEvent(message='素養無し')

    def test(self):
        if GetFlagState(71000014) == 0:
            return State_49
        if GetFlagState(71000014) == 1:
            return State_51


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=23010010, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=71000014, state=1)

    def test(self):
        return State_19


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=23010250, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_80, State_83]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_26


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        SetFlagState(flag=71000016, state=1)

    def test(self):
        return State_11


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=23010720, unk1=-1, unk2=-1)
        SetFlagState(flag=71000016, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71000017, state=1)

    def test(self):
        return State_11


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=23010740, unk1=-1, unk2=-1)
        SetFlagState(flag=71000017, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71000018, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        return State_17


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71000019, state=1)

    def test(self):
        return State_17


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23011400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61, State_64]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_66
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_68
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_68
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_67


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=23011501, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011402, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_26


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_8


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        DebugEvent(message='上位呪術教えたフラグセット')
        SetFlagState(flag=11020103, state=1)

    def test(self):
        return State_69


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        DebugEvent(message='上位呪術を教えない')

    def test(self):
        return State_70


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        TalkToPlayer(conversation=23011500, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_71
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_68]

    def enter(self):
        TalkToPlayer(conversation=23011600, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_71
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_69, State_70]

    def enter(self):
        SetFlagState(flag=71000020, state=1)

    def test(self):
        return State_65
        # UNREACHABLE:
        # if 1:
        #     return State_65


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71000021, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        return State_17


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_18, State_22, State_23, State_75]

    def enter(self):
        TalkToPlayer(conversation=23010900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 5:
            return State_24


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_10, State_14, State_54, State_56]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_38

    def exit(self):
        RemoveMyAggro()


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_45, State_62]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_73
        else:
            return State_19


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_76, State_78]

    def test(self):
        return State_17


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=23011720, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DebugEvent(message='アイテム譲渡')
        SetFlagState(flag=71000022, state=1)
        SetFlagState(flag=11020602, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_19
        if IsMenuOpen(63) == 0:
            return State_80


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        TalkToPlayer(conversation=23010030, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_19, State_43]

    def enter(self):
        TalkToPlayer(conversation=23010050, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_83
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        CollectJustPyromancyFlame()
        CombineMenuFlagAndEventFlag(365, 331)
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22
        if IsMenuOpen(13) == 0:
            return State_6


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_81]

    def enter(self):
        SetFlagState(flag=71000022, state=1)
        SetFlagState(flag=11026102, state=1)

    def test(self):
        return State_52
