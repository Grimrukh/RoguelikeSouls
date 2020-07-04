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
        return [State_8, State_12, State_14, State_16, State_17, State_19, State_21, State_23, State_25, State_27, State_28, State_30, State_32, State_34, State_39, State_40, State_44, State_50, State_58, State_60, State_61, State_63, State_66, State_68, State_73, State_74, State_77, State_80, State_81, State_82, State_84, State_85, State_87, State_88, State_89, State_91]

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
        return [State_0, State_2, State_4, State_5, State_11, State_16, State_25, State_35, State_41, State_44, State_48, State_51, State_52, State_54, State_56, State_60, State_65, State_75, State_79, State_83, State_84]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1823) == 0 and GetDistanceToPlayer() <= 7:
            return State_16
        if GetFlagState(71210068) == 0 and GetFlagState(11210539) == 1 and GetDistanceToPlayer() <= 7 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 7 and GetFlagState(1821) == 1 and GetFlagState(11210592) == 1 and GetFlagState(1822) == 0:
            return State_77
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210074) == 1 and GetFlagState(71210076) == 0 and GetFlagState(11210004) == 0:
            return State_73
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210075) == 1 and GetFlagState(71210077) == 0 and GetFlagState(11210004) == 0:
            return State_74
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210070) == 1 and GetFlagState(71210074) == 0 and GetFlagState(71210075) == 0 and GetFlagState(11210004) == 0:
            return State_39
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210071) == 1 and GetFlagState(71210073) == 0 and GetFlagState(11210004) == 0:
            return State_40
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(11210004) == 1 and GetFlagState(71210065) == 1:
            return State_34
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(11210592) == 0 and GetFlagState(11210004) == 1 and GetFlagState(71210065) == 0 and GetFlagState(71210061) == 0:
            return State_87
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(11210004) == 1 and GetFlagState(71210061) == 1 and GetFlagState(11210592) == 0 and GetFlagState(71210065) == 0:
            return State_88
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(11210004) == 1 and GetFlagState(71210065) == 0 and GetFlagState(11210592) == 1:
            return State_32
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(11210004) == 0 and GetFlagState(11210592) == 1:
            return State_30
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210067) == 0 and GetFlagState(11210051) == 1 and GetFlagState(71210061) == 1 and GetFlagState(11210004) == 0:
            return State_27
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210061) == 1 and GetFlagState(11216102) == 1:
            return State_28
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1821) == 1 and GetFlagState(71210061) == 1 and GetFlagState(11216102) == 0:
            return State_14
        if GetFlagState(1821) == 1 and GetFlagState(71210061) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1:
            return State_23
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetFlagState(1822) == 0 and GetFlagState(1823) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 5):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1823) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_23, State_27, State_28, State_30, State_32, State_34, State_39, State_40, State_44, State_49, State_50, State_58, State_60, State_61, State_63, State_66, State_68, State_73, State_74, State_77, State_80, State_81, State_82, State_84, State_87, State_88, State_89, State_91]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_25
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7 and GetFlagState(71210060) == 0 and GetSelfHP() <= 90:
            return State_12
        if GetFlagState(1822) == 1:
            return State_10
        if GetFlagState(71210058) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7 and GetFlagState(71210059) == 0:
            return State_85
        if GetFlagState(71210057) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7 and GetFlagState(71210058) == 0:
            return State_21
        if GetFlagState(71210056) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7 and GetFlagState(71210057) == 0:
            return State_19
        if GetFlagState(71210055) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7 and GetFlagState(71210056) == 0:
            return State_17
        if GetFlagState(71210055) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 7:
            return State_8
        if GetFlagState(71210059) == 1:
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
        TalkToPlayer(conversation=58005000, unk1=-1, unk2=-1)
        SetFlagState(flag=71210055, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71210055, state=1)

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
        return [State_9, State_10, State_13, State_18, State_20, State_22, State_86]

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
        TalkToPlayer(conversation=58005100, unk1=-1, unk2=-1)
        SetFlagState(flag=71210060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71210060, state=1)
        SetFlagState(flag=11210911, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71210062, state=1)
        SetFlagState(flag=11216102, state=1)

    def test(self):
        return State_54


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6, State_26]

    def enter(self):
        TalkToPlayer(conversation=58005401, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 8:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=58005010, unk1=-1, unk2=-1)
        SetFlagState(flag=71210056, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        SetFlagState(flag=71210056, state=1)

    def test(self):
        return State_11


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=58005020, unk1=-1, unk2=-1)
        SetFlagState(flag=71210057, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71210057, state=1)

    def test(self):
        return State_11


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=58005030, unk1=-1, unk2=-1)
        SetFlagState(flag=71210058, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71210058, state=1)

    def test(self):
        return State_11


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58000000, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        SetFlagState(flag=71210061, state=1)
        SetFlagState(flag=11216102, state=1)

    def test(self):
        return State_54


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_7, State_41, State_52, State_53]

    def enter(self):
        TalkToPlayer(conversation=58005401, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 8:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_8, State_12, State_17, State_19, State_21, State_85]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        SetFlagState(flag=71210063, state=1)
        SetFlagState(flag=11216102, state=1)

    def test(self):
        return State_54


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71210064, state=1)

    def test(self):
        return State_54


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32, State_87, State_88]

    def enter(self):
        SetFlagState(flag=71210065, state=1)

    def test(self):
        return State_54


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58002500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_78
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_38, State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        DebugEvent(message='困ってる')
        SetFlagState(flag=71210070, state=1)

    def test(self):
        return State_39


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        DebugEvent(message='困ってない')
        SetFlagState(flag=71210071, state=1)
        SetFlagState(flag=11216103, state=1)

    def test(self):
        if GetFlagState(71210073) == 1:
            return State_80
        if GetFlagState(71210073) == 0:
            return State_40


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_27, State_50]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)
        SetFlagState(flag=71210067, state=1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_35
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_37
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_37
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_36


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_6, State_36]

    def enter(self):
        TalkToPlayer(conversation=58000400, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_6, State_37]

    def enter(self):
        TalkToPlayer(conversation=58000600, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_38, State_72]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_25
        else:
            return State_6


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71210072, state=1)

    def test(self):
        return State_72


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        SetFlagState(flag=71210073, state=1)

    def test(self):
        return State_51


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=58001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        OpenRegularShop(6600, 6699)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_52
        if IsMenuOpen(11) == 0:
            return State_47


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_47]

    def test(self):
        return State_45


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_45, State_51, State_54]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_53
        if GetTalkListEntryResult() == 0:
            return State_55
        if GetTalkListEntryResult() == 3:
            return State_57
        if GetTalkListEntryResult() == 1:
            return State_46
        if GetTalkListEntryResult() == 4:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_53

    def exit(self):
        ClearTalkListData()


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_49, State_52, State_53]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_52, State_53]

    def enter(self):
        TalkToPlayer(conversation=58001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if GetDistanceToPlayer() >= 12:
            return State_48
        if HasTalkEnded() == 1:
            return State_56


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_43, State_62, State_64, State_67, State_69, State_76, State_80, State_81, State_83, State_90, State_92]

    def test(self):
        return State_47
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 7:
        #     return State_6


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_25
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_49
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_48
        else:
            return State_6


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_25
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_49
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_48


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_15, State_24, State_29, State_31, State_33, State_78]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_47
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 7:
        #     return State_6


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_47]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1 or DidYouDoSomethingInTheMenu(11) == 0:
            return State_59
        else:
            return State_65


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=11215202, state=1)

    def test(self):
        return State_6


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_47]

    def test(self):
        if GetFlagState(11210004) == 1 and GetFlagState(11210593) == 0 and GetFlagState(71210083) == 1:
            return State_82
        if GetFlagState(71210072) == 1 and GetFlagState(71210074) == 0 and GetFlagState(11216103) == 0 and GetFlagState(11210004) == 0:
            return State_58
        if GetFlagState(71210067) == 1 and GetFlagState(71210070) == 0 and GetFlagState(11216103) == 0 and GetFlagState(11210004) == 0:
            return State_50
        if GetFlagState(11210051) == 1 and GetFlagState(71210083) == 0:
            return State_68
        if GetFlagState(71210079) == 0 and GetFlagState(11210051) == 0:
            return State_61
        if GetFlagState(71210081) == 1 and GetFlagState(11216103) == 0 and GetFlagState(71210078) == 0 and GetFlagState(71210069) == 1 and GetFlagState(11210002) == 0:
            return State_91
        if GetFlagState(71210081) == 1 and GetFlagState(11216103) == 0 and GetFlagState(71210069) == 0:
            return State_89
        if GetFlagState(71210081) == 1 and GetFlagState(11216103) == 0:
            return State_63
        else:
            return State_66


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58001000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_72
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_55]

    def test(self):
        if GetFlagState(11210004) == 1:
            return State_84
        if GetFlagState(11210592) == 1:
            return State_60
        if GetFlagState(11210592) == 0:
            return State_44


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=58001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58001700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=71210079, state=1)

    def test(self):
        return State_51


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58002000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        SetFlagState(flag=71210082, state=1)

    def test(self):
        return State_51


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_6


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58001900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        SetFlagState(flag=71210081, state=1)
        SetFlagState(flag=11216103, state=1)

    def test(self):
        return State_51


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58002100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_68]

    def enter(self):
        SetFlagState(flag=71210083, state=1)

    def test(self):
        return State_51


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        DebugEvent(message='あきらめない')
        SetFlagState(flag=71210074, state=1)

    def test(self):
        return State_73


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        DebugEvent(message='諦める')
        SetFlagState(flag=71210075, state=1)
        SetFlagState(flag=11216103, state=1)

    def test(self):
        if GetFlagState(71210077) == 1:
            return State_81
        if GetFlagState(71210077) == 0:
            return State_74


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_42, State_58]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_35
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_71
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_71
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_70


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_6, State_70]

    def enter(self):
        TalkToPlayer(conversation=58000500, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_6, State_71]

    def enter(self):
        TalkToPlayer(conversation=58000700, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_76
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_73]

    def enter(self):
        SetFlagState(flag=11210592, state=1)
        SetFlagState(flag=71210076, state=1)

    def test(self):
        return State_6


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        SetFlagState(flag=71210077, state=1)

    def test(self):
        return State_51


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=58000520, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71210068, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_79
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 12:
            return State_3


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71210066, state=1)

    def test(self):
        return State_54


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_77]

    def enter(self):
        SetFlagState(flag=71210068, state=1)

    def test(self):
        return State_6


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        TalkToPlayer(conversation=58000900, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        TalkToPlayer(conversation=58001100, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58002200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_83
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_82]

    def enter(self):
        SetFlagState(flag=71210084, state=1)
        SetFlagState(flag=11210593, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 8:
            return State_6
        if IsMenuOpen(63) == 0:
            return State_51


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=58001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=58005040, unk1=-1, unk2=-1)
        SetFlagState(flag=71210059, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_26
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_3


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_85]

    def enter(self):
        SetFlagState(flag=71210059, state=1)

    def test(self):
        return State_11


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58002300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=58002400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58002600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_90
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        SetFlagState(flag=71210069, state=1)

    def test(self):
        return State_51


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        TalkToPlayer(conversation=58002700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_92
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_3


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_91]

    def enter(self):
        SetFlagState(flag=71210078, state=1)

    def test(self):
        return State_51
