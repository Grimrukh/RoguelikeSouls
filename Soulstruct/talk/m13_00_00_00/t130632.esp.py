from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_66


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
        return [State_8, State_12, State_20, State_21, State_23, State_25, State_27, State_29, State_31, State_33, State_35, State_37, State_39, State_40, State_43, State_44, State_45, State_47, State_48, State_49, State_50, State_51, State_52, State_53, State_54, State_58]

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
        return [State_2, State_4, State_5, State_11, State_16, State_22, State_39, State_40, State_44, State_48, State_49, State_50, State_51, State_55, State_57, State_60, State_61, State_65, State_66, State_67, State_68, State_69]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1628) == 0 and GetDistanceToPlayer() <= 5:
            return State_14
        if GetFlagState(1627) == 1 and IsPlayerDead() == 1 and GetFlagState(71310075) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_56
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1621) == 1:
            return State_42
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1620) == 1:
            return State_41
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1628) == 0 and GetFlagState(1627) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1628) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_20, State_21, State_43, State_44, State_45, State_47, State_48, State_49, State_50, State_51, State_52, State_53, State_54]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310065) == 0 and GetSelfHP() <= 90 and GetFlagState(1620) == 1:
            return State_58
        if GetFlagState(71310063) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1638) == 1 and ComparePlayerStatus(12, 0, 0) == 1 and GetSelfHP() <= 90 and GetFlagState(1621) == 1:
            return State_37
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310061) == 0 and GetSelfHP() <= 90 and GetFlagState(1638) == 1 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1621) == 1:
            return State_12
        if GetFlagState(71310064) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1638) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetSelfHP() <= 90 and GetFlagState(1621) == 1:
            return State_29
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310062) == 0 and GetSelfHP() <= 90 and GetFlagState(1638) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1621) == 1:
            return State_35
        if GetFlagState(1627) == 1:
            return State_10
        if GetFlagState(71310060) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1620) == 1 and GetFlagState(71310059) == 1:
            return State_33
        if GetFlagState(71310059) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1620) == 1 and GetFlagState(71310058) == 1:
            return State_31
        if GetFlagState(71310058) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1620) == 1:
            return State_27
        if GetFlagState(71310057) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1621) == 1 and GetFlagState(71310056) == 1:
            return State_25
        if GetFlagState(71310056) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1621) == 1 and GetFlagState(71310055) == 1:
            return State_23
        if GetFlagState(71310055) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1621) == 1:
            return State_8
        if GetFlagState(71310057) == 1:
            return State_10
        if GetFlagState(71310060) == 1:
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
        TalkToPlayer(conversation=42000840, unk1=-1, unk2=-1)
        SetFlagState(flag=71310055, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71310055, state=1)

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
        return [State_9, State_10, State_13, State_24, State_26, State_28, State_30, State_32, State_34, State_36, State_38, State_59]

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
        TalkToPlayer(conversation=42000900, unk1=-1, unk2=-1)
        SetFlagState(flag=71310061, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71310061, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6, State_7, State_15, State_22]

    def test(self):
        if GetFlagState(1621) == 1:
            return State_40
        if GetFlagState(1620) == 1:
            return State_39


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_8, State_12, State_23, State_25, State_27, State_29, State_31, State_33, State_35, State_37, State_58]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14

    def exit(self):
        RemoveMyAggro()


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DebugEvent(message='はい')
        SetFlagState(flag=71310066, state=1)
        SetFlagState(flag=1638, state=1)
        SetFlagState(flag=1637, state=1)

    def test(self):
        return State_20


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DebugEvent(message='いいえ')
        SetFlagState(flag=71310067, state=1)
        SetFlagState(flag=1637, state=1)

    def test(self):
        return State_21


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)
        SetFlagState(flag=1637, state=1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_16
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_18
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_18
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_17


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_17, State_41]

    def enter(self):
        TalkToPlayer(conversation=42000020, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_68
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_18, State_41]

    def enter(self):
        TalkToPlayer(conversation=42000040, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_19, State_64]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        else:
            return State_6


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42000850, unk1=-1, unk2=-1)
        SetFlagState(flag=71310056, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        SetFlagState(flag=71310056, state=1)

    def test(self):
        return State_11


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42000860, unk1=-1, unk2=-1)
        SetFlagState(flag=71310057, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        SetFlagState(flag=71310057, state=1)

    def test(self):
        return State_11


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42001240, unk1=-1, unk2=-1)
        SetFlagState(flag=71310058, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        SetFlagState(flag=71310058, state=1)

    def test(self):
        return State_11


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42000970, unk1=-1, unk2=-1)
        SetFlagState(flag=71310064, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        SetFlagState(flag=71310064, state=1)

    def test(self):
        return State_11


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42001250, unk1=-1, unk2=-1)
        SetFlagState(flag=71310059, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71310059, state=1)

    def test(self):
        return State_11


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42001260, unk1=-1, unk2=-1)
        SetFlagState(flag=71310060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        SetFlagState(flag=71310060, state=1)

    def test(self):
        return State_11


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42000920, unk1=-1, unk2=-1)
        SetFlagState(flag=71310062, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        SetFlagState(flag=71310062, state=1)

    def test(self):
        return State_11


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42000950, unk1=-1, unk2=-1)
        SetFlagState(flag=71310063, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71310063, state=1)

    def test(self):
        return State_11


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=42001400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=42001000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71310066) == 0 and GetFlagState(71310067) == 0:
            return State_43
        if GetFlagState(71310067) == 1 and GetFlagState(71310076) == 0:
            return State_21
        if GetFlagState(71310066) == 1 and GetFlagState(71310076) == 0:
            return State_20
        if GetFlagState(1637) == 1:
            return State_44


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(11300591) == 1:
            return State_50
        if GetFlagState(71310070) == 1 and GetFlagState(11300591) == 0:
            return State_52
        if GetFlagState(1637) == 0 and GetFlagState(11300590) == 1:
            return State_49
        if GetFlagState(1637) == 0:
            return State_45
        if GetFlagState(71310071) == 1:
            return State_63
        if GetFlagState(71310070) == 1:
            return State_51
        if GetFlagState(71310070) == 0 and GetFlagState(71310071) == 0 and GetFlagState(1637) == 1:
            return State_47


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_46
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_3


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        SetFlagState(flag=71310068, state=1)
        SetFlagState(flag=11300590, state=1)

    def test(self):
        if IsMenuOpen(63) == 0:
            return State_48


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000210, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_42, State_65]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000510, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_42, State_62]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42000650, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        TalkToPlayer(conversation=42001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310075, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(1620) == 1:
            return State_67
        if ComparePlayerStatus(12, 0, 0) == 1:
            return State_57
        if ComparePlayerStatus(12, 0, 1) == 1:
            return State_55


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        TalkToPlayer(conversation=42001110, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310075, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42001300, unk1=-1, unk2=-1)
        SetFlagState(flag=71310065, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        SetFlagState(flag=71310065, state=1)

    def test(self):
        return State_11


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_53, State_54]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        DebugEvent(message='はい')
        SetFlagState(flag=71310070, state=1)

    def test(self):
        return State_52


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_42, State_64]

    def enter(self):
        DebugEvent(message='奇跡を教わらない')
        SetFlagState(flag=71310071, state=1)

    def test(self):
        if ComparePlayerStatus(12, 0, 1) == 1:
            return State_53
        if ComparePlayerStatus(12, 0, 0) == 1:
            return State_54


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_61
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_62


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=71310072, state=1)
        SetFlagState(flag=11300591, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_6
        if IsMenuOpen(63) == 0:
            return State_50


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71310075, state=0)

    def test(self):
        return State_6


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        TalkToPlayer(conversation=42001500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310075, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=71310076, state=1)

    def test(self):
        return State_6


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71310077, state=1)

    def test(self):
        return State_6
