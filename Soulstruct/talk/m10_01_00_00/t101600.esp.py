from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_6


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_7


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_8, State_12, State_14, State_16, State_17, State_19, State_21, State_23, State_24, State_31, State_32, State_37, State_38, State_40, State_41, State_42, State_44, State_46, State_48, State_50, State_52, State_54, State_56, State_58, State_59, State_62, State_64, State_65, State_73]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_2


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_6


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_6


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_0, State_2, State_4, State_5, State_11, State_15, State_16, State_20, State_22, State_24, State_26, State_27, State_33, State_34, State_53, State_57, State_58, State_65, State_66, State_74]

    def enter(self):
        DebugEvent(message='待機')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1005) == 0 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100092) == 1 and GetFlagState(71100091) == 0 and GetFlagState(1007) == 1:
            return State_59
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100098) == 1 and GetFlagState(71100097) == 0 and GetFlagState(1007) == 1:
            return State_59
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100097) == 1 and GetFlagState(71100091) == 0 and GetFlagState(1007) == 1 and GetFlagState(71100092) == 0:
            return State_62
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100093) == 1 and GetFlagState(71100094) == 0 and GetFlagState(1007) == 1:
            return State_56
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100094) == 1 and GetFlagState(1007) == 1 and GetFlagState(71100095) == 0:
            return State_58
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100094) == 1 and GetFlagState(1007) == 1 and GetFlagState(71100095) == 1:
            return State_65
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100097) == 0 and GetFlagState(71100098) == 0 and GetFlagState(1007) == 1 and GetStatus(6) + GetStatus(13) + GetStatus(13) + GetStatus(13) + GetStatus(13) + GetStatus(13) > 25 and ComparePlayerStatus(11, 5, 3) == 1:
            return State_54
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71100096) == 0 and GetFlagState(1007) == 1:
            return State_52
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010053) == 1 and GetFlagState(11010591) == 1 and GetFlagState(71010056) == 0:
            return State_19
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010055) == 1 and GetFlagState(71010053) == 0:
            return State_38
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010054) == 1 and GetFlagState(71010052) == 0:
            return State_23
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010053) == 1 and GetFlagState(11010591) == 0:
            return State_37
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010053) == 1 and GetFlagState(11010591) == 0:
            return State_42
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010052) == 1 and GetFlagState(71010058) == 0:
            return State_31
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010058) == 1 and GetFlagState(71010052) == 1 and GetFlagState(71010055) == 0 and GetFlagState(71010053) == 0:
            return State_41
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010056) == 1:
            return State_21
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010050) == 1 and GetFlagState(71010054) == 0 and GetFlagState(71010052) == 0 and GetFlagState(50000000) == 0:
            return State_17
        if GetFlagState(71010050) == 1 and GetFlagState(705) == 1 and GetFlagState(50000000) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_73
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71010050) == 0:
            return State_14
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1004) == 0 and GetFlagState(1005) == 0:
            return State_5
        if IsAttackedBySomeone() == 1 and GetFlagState(1005) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_17, State_19, State_21, State_23, State_31, State_32, State_37, State_38, State_40, State_41, State_42, State_52, State_54, State_56, State_58, State_59, State_62, State_64, State_65, State_73]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_24
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010064) == 0 and GetSelfHP() <= 90:
            return State_12
        if GetFlagState(1004) == 1:
            return State_10
        if GetFlagState(71010063) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010062) == 1:
            return State_50
        if GetFlagState(71010062) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010061) == 1:
            return State_48
        if GetFlagState(71010061) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010060) == 1:
            return State_46
        if GetFlagState(71010060) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010059) == 1:
            return State_44
        if GetFlagState(71010059) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_8
        if GetFlagState(71010058) == 1:
            return State_10
        else:
            return State_10

    def exit(self):
        RemoveMyAggro()


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010600, unk1=-1, unk2=-1)
        SetFlagState(flag=71010059, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71010059, state=1)

    def test(self):
        return State_11


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_11


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9, State_10, State_13, State_45, State_47, State_49, State_51]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_6


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010700, unk1=-1, unk2=-1)
        SetFlagState(flag=71010064, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71010064, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71010050, state=1)

    def test(self):
        return State_6


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6, State_25]

    def enter(self):
        TalkToPlayer(conversation=10010800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        SetFlagState(flag=71010051, state=1)

    def test(self):
        return State_30


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_6, State_34]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010310, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71010056, state=1)
        SetFlagState(flag=11010590, state=1)

    def test(self):
        return State_6


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71010057, state=1)
        SetFlagState(flag=11010590, state=1)

    def test(self):
        return State_6


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_7, State_33]

    def enter(self):
        TalkToPlayer(conversation=10010800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_8, State_12, State_44, State_46, State_48, State_50]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_32, State_40, State_64, State_72]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_30, State_36, State_60, State_61, State_69, State_71, State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        DebugEvent(message='話を聞く')
        SetFlagState(flag=71010052, state=1)

    def test(self):
        return State_31


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        DebugEvent(message='話を聞かない')
        SetFlagState(flag=71010054, state=1)

    def test(self):
        return State_32


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_18, State_23]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_29
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_29
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_6, State_28]

    def enter(self):
        TalkToPlayer(conversation=10010250, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=10010350, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_30, State_36, State_60, State_69, State_71, State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_24
        else:
            return State_6


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_37, State_42]

    def enter(self):
        DebugEvent(message='アイテムを渡す')
        SetFlagState(flag=11010591, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 8:
            return State_6
        if IsMenuOpen(63) == 0 and GetDistanceToPlayer() <= 5:
            return State_19


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        DebugEvent(message='話を聞く')
        SetFlagState(flag=71010053, state=1)

    def test(self):
        return State_37


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_38, State_41, State_43]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_35


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_6, State_35]

    def enter(self):
        TalkToPlayer(conversation=10010300, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_3


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        DebugEvent(message='願いを聞かない')
        SetFlagState(flag=71010055, state=1)

    def test(self):
        return State_40


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        TalkToPlayer(conversation=10010360, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=10010250, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=10010301, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71010058, state=1)

    def test(self):
        return State_36


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010610, unk1=-1, unk2=-1)
        SetFlagState(flag=71010060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71010060, state=1)

    def test(self):
        return State_11


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010620, unk1=-1, unk2=-1)
        SetFlagState(flag=71010061, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71010061, state=1)

    def test(self):
        return State_11


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010630, unk1=-1, unk2=-1)
        SetFlagState(flag=71010062, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        SetFlagState(flag=71010062, state=1)

    def test(self):
        return State_11


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=10010640, unk1=-1, unk2=-1)
        SetFlagState(flag=71010063, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=71010063, state=1)

    def test(self):
        return State_11


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=71100096, state=1)
        SetFlagState(flag=71010056, state=1)

    def test(self):
        return State_6


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        SetFlagState(flag=71100090, state=1)

    def test(self):
        return State_69


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_6, State_71]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022260, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71100094, state=1)

    def test(self):
        return State_6


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1 and GetFlagState(71100092) == 1:
            return State_60
        if HasTalkEnded() == 1 and GetFlagState(71100098) == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59, State_70]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=3)
        RequestUnlockTrophy(10)

    def test(self):
        if IsMultiplayerInProgress() == 1:
            return State_72
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_61


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        DebugEvent(message='誓約する')
        SetFlagState(flag=71100091, state=1)
        BreakCovenantPledge()
        ChangePlayerStats(unk1=11, unk2=5, unk3=3)
        SetFlagState(flag=843, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_27
        if GetFlagState(11010594) == 0 and GetFlagState(843) == 0:
            return State_66
        if GetDistanceToPlayer() <= 5 and GetFlagState(843) == 0:
            return State_71


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_6, State_67]

    def enter(self):
        TalkToPlayer(conversation=10022250, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_70
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        DebugEvent(message='誓約しない')
        SetFlagState(flag=71100092, state=1)

    def test(self):
        return State_64


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63, State_68]

    def enter(self):
        TalkToPlayer(conversation=10022300, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10022700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=11010594, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 8:
            return State_6
        if IsMenuOpen(63) == 0:
            return State_71


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        DebugEvent(message='望む')
        SetFlagState(flag=71100097, state=1)

    def test(self):
        return State_62


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        DebugEvent(message='望まない')
        SetFlagState(flag=71100098, state=1)

    def test(self):
        return State_64


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_55, State_59]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_68
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_68
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_67


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=71100093, state=1)

    def test(self):
        return State_60


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_61, State_66]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わしました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_56
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_56


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010747, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='マルチプレイ中')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_27
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_26
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_26


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=10010400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_74
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_73]

    def enter(self):
        SetFlagState(flag=11010590, state=1)
        SetFlagState(flag=11010591, state=1)

    def test(self):
        return State_6
