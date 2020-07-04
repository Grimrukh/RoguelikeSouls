from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_14


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        TalkToPlayer(conversation=15000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_26


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_1


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        OpenRegularShop(2200, 2299)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_17
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
        return [State_4, State_12, State_21]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000350, required_flag=284)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if GetTalkListEntryResult() == 0:
            return State_23
        if GetTalkListEntryResult() == 3:
            return State_28
        if GetTalkListEntryResult() == 1:
            return State_5
        if GetTalkListEntryResult() == 4:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_18
        if GetTalkListEntryResult() == 2:
            return State_56

    def exit(self):
        ClearTalkListData()


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_8, State_17, State_18]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_14


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_17, State_18, State_36]

    def enter(self):
        TalkToPlayer(conversation=15000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if GetDistanceToPlayer() >= 12:
            return State_7
        if HasTalkEnded() == 1:
            return State_27


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_10, State_45, State_47, State_49]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_14


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_9


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=15000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_32, State_43, State_57, State_61, State_63, State_64, State_66]

    def test(self):
        return State_6
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_14


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_1, State_8, State_11, State_22, State_24, State_26, State_30, State_31, State_34, State_40, State_41, State_42, State_44, State_59, State_60, State_62, State_65]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_51
        if GetFlagState(1124) == 1:
            return State_10
        if GetFlagState(71200012) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200011) == 1:
            return State_50
        if GetFlagState(71200011) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200010) == 1:
            return State_48
        if GetFlagState(71200010) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_46
        if GetFlagState(71200012) == 1:
            return State_10
        else:
            return State_10

    def exit(self):
        RemoveMyAggro()


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_0, State_1, State_7, State_9, State_12, State_15, State_16, State_17, State_20, State_21, State_23, State_26, State_27, State_29, State_33, State_35, State_51, State_53]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1125) == 0 and GetDistanceToPlayer() <= 5:
            return State_33
        if GetFlagState(71200000) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1121) == 1:
            return State_24
        if GetFlagState(71200002) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1121) == 1 and GetFlagState(71200001) == 0 and GetFlagState(71200000) == 1:
            return State_34
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71200006) == 1 and GetFlagState(11206100) == 1:
            return State_30
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1130) == 1:
            return State_59
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71200001) == 0 and GetFlagState(71200002) == 1 and GetFlagState(1123) == 0:
            return State_41
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71200002) == 0 and GetFlagState(71200001) == 1 and GetFlagState(1123) == 0:
            return State_40
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1123) == 1:
            return State_11
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1120) == 0 and GetFlagState(1124) == 0 and GetFlagState(1125) == 0 and GetFlagState(1126) == 0 and GetFlagState(1122) == 0 and GetFlagState(1129) == 0:
            return State_15
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_16
        if IsAttackedBySomeone() == 1 and GetFlagState(1125) == 0:
            return State_22


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_14


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_14


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_4, State_56]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_51
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7
        else:
            return State_14


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_51
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_8
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_7


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_1, State_11, State_24, State_26, State_30, State_31, State_33, State_34, State_40, State_41, State_42, State_44, State_46, State_48, State_50, State_51, State_59, State_60, State_62, State_65]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_20


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_14


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_11, State_59]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_6
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_14


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_13


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_3
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_2
        else:
            return State_14


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=15000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        SetFlagState(flag=71200000, state=1)

    def test(self):
        return State_39


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=15000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71200006, state=1)
        SetFlagState(flag=11206100, state=1)

    def test(self):
        return State_14


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71210091) == 1 and GetFlagState(1130) == 1 and GetFlagState(11206104) == 0:
            return State_65
        if GetFlagState(71210090) == 1 and GetFlagState(1130) == 1 and GetFlagState(11206102) == 0:
            return State_62
        if GetFlagState(1130) == 1 and GetFlagState(71210092) == 1 and GetFlagState(71210091) == 0:
            return State_60
        if GetFlagState(71200005) == 1 and GetFlagState(11206103) == 0:
            return State_44
        if GetFlagState(71200004) == 1:
            return State_42
        if GetFlagState(71200004) == 0:
            return State_31


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71200006, state=0)

    def test(self):
        return State_14


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=15000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=15001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71200004, state=1)

    def test(self):
        return State_12


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_14, State_52]

    def enter(self):
        TalkToPlayer(conversation=15000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_14
        if GetDistanceToPlayer() >= 5:
            return State_19


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=15000020, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_54, State_55]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_14


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_39, State_58]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_8


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        DebugEvent(message='魔術を教わる')
        SetFlagState(flag=71200001, state=1)

    def test(self):
        return State_40


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        DebugEvent(message='魔術を教わらない')
        SetFlagState(flag=71200002, state=1)

    def test(self):
        return State_41


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_25, State_34]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_36
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_37


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_14, State_37]

    def enter(self):
        TalkToPlayer(conversation=15000050, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_14, State_38]

    def enter(self):
        TalkToPlayer(conversation=15000100, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=15001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        SetFlagState(flag=71200005, state=1)
        SetFlagState(flag=11206103, state=1)

    def test(self):
        return State_12


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=15001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71200010, state=1)

    def test(self):
        return State_9


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=15000220, unk1=-1, unk2=-1)
        SetFlagState(flag=71200010, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_52
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        SetFlagState(flag=71200011, state=1)

    def test(self):
        return State_9


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=15000240, unk1=-1, unk2=-1)
        SetFlagState(flag=71200011, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_52
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=71200012, state=1)

    def test(self):
        return State_9


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=15000260, unk1=-1, unk2=-1)
        SetFlagState(flag=71200012, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_52
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_13, State_17, State_18, State_53]

    def enter(self):
        TalkToPlayer(conversation=15000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_14
        if GetDistanceToPlayer() >= 5:
            return State_19


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_46, State_48, State_50]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_33

    def exit(self):
        RemoveMyAggro()


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_39, State_58]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_51
        else:
            return State_14


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        DebugEvent(message='状態遷移フラグたてる')
        SetFlagState(flag=11200590, state=1)

    def test(self):
        return State_35


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        DebugEvent(message='状態遷移フラグたてる')
        SetFlagState(flag=11200591, state=1)

    def test(self):
        return State_35


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9013, 1)
        AcquireGesture(13)
        SetFlagState(flag=284, state=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_17
        if IsMenuOpen(63) == 0:
            return State_58


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_12


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_36
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_57
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_57


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=15000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=56000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        SetFlagState(flag=71210090, state=1)
        SetFlagState(flag=11206102, state=1)

    def test(self):
        return State_12


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=56000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=71210091, state=1)
        SetFlagState(flag=11206104, state=1)

    def test(self):
        return State_12


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71210092, state=1)

    def test(self):
        return State_12


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=56000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_19


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        SetFlagState(flag=71210093, state=1)

    def test(self):
        return State_12
