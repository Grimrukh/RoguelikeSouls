from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_47


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        SetFlagState(flag=71510079, state=1)

    def test(self):
        return State_3


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=11000600, unk1=-1, unk2=-1)
        SetFlagState(flag=71510079, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_12


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1, State_4, State_5, State_29, State_31, State_33]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_9


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_3


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        SetFlagState(flag=71510075, state=1)

    def test(self):
        return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=11000500, unk1=-1, unk2=-1)
        SetFlagState(flag=71510075, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_5
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=11001300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7, State_14, State_15, State_18, State_19, State_21, State_23, State_27, State_37, State_38, State_41, State_58, State_60, State_61, State_63, State_65]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_35
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71510079) == 0 and GetSelfHP() <= 90 and GetFlagState(11510591) == 0:
            return State_2
        if GetFlagState(1033) == 1:
            return State_4
        if GetFlagState(71510078) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71510077) == 1:
            return State_34
        if GetFlagState(71510077) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71510076) == 1:
            return State_32
        if GetFlagState(71510076) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71510075) == 1:
            return State_30
        if GetFlagState(71510075) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_6
        if GetFlagState(71510078) == 1:
            return State_4
        else:
            return State_4

    def exit(self):
        RemoveMyAggro()


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_3, State_10, State_11, State_13, State_17, State_26, State_36, State_39, State_40, State_42, State_43, State_47, State_50, State_52, State_55, State_56, State_57, State_66, State_67, State_73, State_75, State_189, State_192]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1034) == 0 and GetDistanceToPlayer() <= 5:
            return State_35
        if GetFlagState(1033) == 1 and IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_44
        if ((((((((GetFlagState(71510087) == 0 and (GetFlagState(1230) == 0 or GetFlagState(1241) == 1 or GetFlagState(1242) == 1)) and HasDisableTalkPeriodElapsed() == 1) and IsTalkingToSomeoneElse() == 0) and CheckSelfDeath() == 0) and IsCharacterDisabled() == 0) and IsClientPlayer() == 0) and GetRelativeAngleBetweenPlayerAndSelf() <= 180) and GetDistanceToPlayer() <= 10) and GetDistanceToPlayer() <= 10:
            return State_38
        if GetFlagState(71510080) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and ComparePlayerStatus(11, 0, 8) == 1 and GetFlagState(71510088) == 0:
            return State_37
        if GetFlagState(71510089) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1031) == 1:
            return State_41
        if GetFlagState(71510082) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1036) == 1 and GetFlagState(11516100) == 1 and GetFlagState(71510080) == 1:
            return State_61
        if GetFlagState(71510082) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1036) == 1 and GetFlagState(11516100) == 0 and GetFlagState(71510080) == 1 and GetFlagState(71510083) == 1:
            return State_63
        if GetFlagState(71510082) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1036) == 1 and GetFlagState(11516100) == 0 and GetFlagState(71510080) == 1 and GetFlagState(71510083) == 0:
            return State_21
        if GetFlagState(71510082) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1036) == 1 and GetFlagState(71510080) == 1:
            return State_19
        if GetFlagState(71510080) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11516100) == 1 and GetFlagState(71510092) == 1:
            return State_60
        if GetFlagState(71510080) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11516100) == 0 and GetFlagState(71510092) == 1:
            return State_18
        if GetFlagState(71510080) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71510092) == 0 and GetFlagState(1030) == 0:
            return State_58
        if GetFlagState(71510080) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71510092) == 0 and GetFlagState(1036) == 0:
            return State_15
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1033) == 0 and GetFlagState(1034) == 0:
            return State_10
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_11
        if IsAttackedBySomeone() == 1 and GetFlagState(1034) == 0:
            return State_14


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_9


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_9


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_2, State_6, State_7, State_15, State_17, State_18, State_19, State_21, State_23, State_27, State_30, State_32, State_34, State_36, State_37, State_38, State_41, State_58, State_60, State_61, State_63, State_65]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_13


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_9


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_8


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71510080, state=1)
        SetFlagState(flag=11516100, state=1)
        SetFlagState(flag=71510092, state=1)

    def test(self):
        return State_55


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        TalkToPlayer(conversation=11000700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_9
        if GetDistanceToPlayer() >= 5:
            return State_12


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71510082, state=1)
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_55


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71510083, state=1)
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_55


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=11000400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        SetFlagState(flag=71510084, state=1)

    def test(self):
        return State_52


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_2, State_6, State_30, State_32, State_34]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_35

    def exit(self):
        RemoveMyAggro()


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=11000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71510090, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_9


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=11001400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_46
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71510085, state=1)

    def test(self):
        return State_52


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71510076, state=1)

    def test(self):
        return State_3


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=11000510, unk1=-1, unk2=-1)
        SetFlagState(flag=71510076, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71510077, state=1)

    def test(self):
        return State_3


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=11000520, unk1=-1, unk2=-1)
        SetFlagState(flag=71510077, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71510078, state=1)

    def test(self):
        return State_3


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=11000530, unk1=-1, unk2=-1)
        SetFlagState(flag=71510078, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_8, State_9, State_25, State_53, State_54, State_75]

    def test(self):
        if ComparePlayerStatus(12, 0, 1) == 1:
            return State_17
        if ComparePlayerStatus(12, 0, 0) == 1:
            return State_36


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        TalkToPlayer(conversation=11000750, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_9
        if GetDistanceToPlayer() >= 5:
            return State_12


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11001200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11510591, state=1)
        SetFlagState(flag=71510087, state=1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_12


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71510087, state=1)
        SetFlagState(flag=11510591, state=1)

    def test(self):
        return State_9


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71510088, state=1)
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_9


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        SetFlagState(flag=71510089, state=1)

    def test(self):
        return State_9


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=11001000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71510091, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_9


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_9]

    def test(self):
        if GetFlagState(71510091) == 0 and (GetFlagState(1230) == 0 or GetFlagState(1241) == 1 or GetFlagState(1242) == 1):
            return State_43
        if GetFlagState(1232) == 0 and GetFlagState(71510090) == 0:
            return State_26


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_18, State_60]

    def enter(self):
        SetFlagState(flag=71510081, state=1)
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_55
        # UNREACHABLE:
        # if 1:
        #     return State_55


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        SetFlagState(flag=71510086, state=1)

    def test(self):
        return State_52


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71510090, state=0)
        SetFlagState(flag=71510091, state=0)

    def test(self):
        return State_9


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_49]

    def test(self):
        if GetFlagState(71510085) == 0 and GetFlagState(1036) == 1:
            return State_7
        if GetFlagState(71510084) == 1 and GetFlagState(71510086) == 0:
            return State_27
        if GetFlagState(71510084) == 0:
            return State_23
        else:
            return State_65


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_52, State_55]

    def enter(self):
        AddTalkListData(menu_index=3, menu_text=15000230, required_flag=716)
        AddTalkListData(menu_index=1, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_54
        if GetTalkListEntryResult() == 0:
            return State_56
        if GetTalkListEntryResult() == 1:
            return State_48
        if GetTalkListEntryResult() == 4:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_54
        if GetTalkListEntryResult() == 3:
            return State_74

    def exit(self):
        ClearTalkListData()


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_51, State_53, State_54]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_9


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_53, State_54]

    def test(self):
        if GetDistanceToPlayer() >= 25:
            return State_50
        else:
            return State_57


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_24, State_28, State_46, State_65, State_72, State_188, State_191]

    def test(self):
        return State_49
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_9


class State_53(State):
    """ 53: No description. """

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_35
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_51
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_50


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_35
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_51
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_50


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_16, State_20, State_22, State_45, State_59, State_62, State_64]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_49
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_9


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_49]

    def test(self):
        return State_9


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        return State_9


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000020, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        SetFlagState(flag=71510092, state=1)
        SetFlagState(flag=11516100, state=1)
        SetFlagState(flag=71510080, state=1)
        SetFlagState(flag=71510082, state=1)

    def test(self):
        return State_55


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000120, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000340, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_55


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        TalkToPlayer(conversation=11000320, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        SetFlagState(flag=71510083, state=0)
        SetFlagState(flag=11516100, state=1)

    def test(self):
        return State_55


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=11000120, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_12


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_9


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_9


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_90


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        DebugEvent(message='強化しない')

    def test(self):
        return State_66


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010890, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_67
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_69
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_69
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 390) == 1 and IsGenericDialogOpen() == 0:
            return State_76
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 391) == 1 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 392) == 1 and IsGenericDialogOpen() == 0:
            return State_108
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 393) == 1 and IsGenericDialogOpen() == 0:
            return State_124
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 394) == 1 and IsGenericDialogOpen() == 0:
            return State_140
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 395) == 1 and IsGenericDialogOpen() == 0:
            return State_156
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 396) == 1 and IsGenericDialogOpen() == 0:
            return State_172


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010760, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_73
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_72
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_72


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_52


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_9


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_49]

    def test(self):
        if IsEquipmentIDObtained(3, 215) == 1 or IsEquipmentIDObtained(3, 214) == 1:
            return State_187
        if IsEquipmentIDObtained(3, 390) == 0 and IsEquipmentIDObtained(3, 391) == 0 and IsEquipmentIDObtained(3, 392) == 0 and IsEquipmentIDObtained(3, 393) == 0 and IsEquipmentIDObtained(3, 394) == 0 and IsEquipmentIDObtained(3, 395) == 0 and IsEquipmentIDObtained(3, 396) == 0:
            return State_71
        if IsEquipmentIDObtained(3, 390) == 1 or IsEquipmentIDObtained(3, 391) == 1 or IsEquipmentIDObtained(3, 392) == 1 or IsEquipmentIDObtained(3, 393) == 1 or IsEquipmentIDObtained(3, 394) == 1 or IsEquipmentIDObtained(3, 395) == 1 or IsEquipmentIDObtained(3, 396) == 1:
            return State_70


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_70, State_71, State_187, State_190]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_35
        else:
            return State_9


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 390, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_68
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_77
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_78
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_79
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_80
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_81
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_82
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_83
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_84
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_85
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_86
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_87
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_88
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_89


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_90


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_90


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_90


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_90


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_90


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_90


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_90


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_90


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_90


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_90


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_90


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_90


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_90


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_68, State_77, State_78, State_79, State_80, State_81, State_82, State_83, State_84, State_85, State_86, State_87, State_88, State_89]

    def test(self):
        return State_190


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_106


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 391, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_91
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_93
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_94
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_95
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_96
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_97
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_98
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_99
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_100
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_101
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_102
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_103
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_104
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_105


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_106


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_106


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_106


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_106


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_106


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_106


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_106


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_106


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_106


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_106


class State_103(State):
    """ 103: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_106


class State_104(State):
    """ 104: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_106


class State_105(State):
    """ 105: No description. """

    def previous_states(self):
        return [State_92]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_106


class State_106(State):
    """ 106: No description. """

    def previous_states(self):
        return [State_91, State_93, State_94, State_95, State_96, State_97, State_98, State_99, State_100, State_101, State_102, State_103, State_104, State_105]

    def test(self):
        return State_190


class State_107(State):
    """ 107: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_122


class State_108(State):
    """ 108: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 392, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_107
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_109
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_110
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_111
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_112
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_113
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_114
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_115
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_116
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_117
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_118
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_119
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_120
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_121


class State_109(State):
    """ 109: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_122


class State_110(State):
    """ 110: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_122


class State_111(State):
    """ 111: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_122


class State_112(State):
    """ 112: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_122


class State_113(State):
    """ 113: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_122


class State_114(State):
    """ 114: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_122


class State_115(State):
    """ 115: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_122


class State_116(State):
    """ 116: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_122


class State_117(State):
    """ 117: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_122


class State_118(State):
    """ 118: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_122


class State_119(State):
    """ 119: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_122


class State_120(State):
    """ 120: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_122


class State_121(State):
    """ 121: No description. """

    def previous_states(self):
        return [State_108]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_122


class State_122(State):
    """ 122: No description. """

    def previous_states(self):
        return [State_107, State_109, State_110, State_111, State_112, State_113, State_114, State_115, State_116, State_117, State_118, State_119, State_120, State_121]

    def test(self):
        return State_190


class State_123(State):
    """ 123: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_138


class State_124(State):
    """ 124: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 393, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_123
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_125
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_126
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_127
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_128
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_129
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_130
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_131
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_132
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_133
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_134
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_135
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_136
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_137


class State_125(State):
    """ 125: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_138


class State_126(State):
    """ 126: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_138


class State_127(State):
    """ 127: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_138


class State_128(State):
    """ 128: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_138


class State_129(State):
    """ 129: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_138


class State_130(State):
    """ 130: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_138


class State_131(State):
    """ 131: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_138


class State_132(State):
    """ 132: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_138


class State_133(State):
    """ 133: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_138


class State_134(State):
    """ 134: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_138


class State_135(State):
    """ 135: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_138


class State_136(State):
    """ 136: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_138


class State_137(State):
    """ 137: No description. """

    def previous_states(self):
        return [State_124]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_138


class State_138(State):
    """ 138: No description. """

    def previous_states(self):
        return [State_123, State_125, State_126, State_127, State_128, State_129, State_130, State_131, State_132, State_133, State_134, State_135, State_136, State_137]

    def test(self):
        return State_190


class State_139(State):
    """ 139: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_154


class State_140(State):
    """ 140: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 394, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_139
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_141
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_142
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_143
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_144
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_145
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_146
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_147
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_148
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_149
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_150
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_151
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_152
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_153


class State_141(State):
    """ 141: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_154


class State_142(State):
    """ 142: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_154


class State_143(State):
    """ 143: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_154


class State_144(State):
    """ 144: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_154


class State_145(State):
    """ 145: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_154


class State_146(State):
    """ 146: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_154


class State_147(State):
    """ 147: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_154


class State_148(State):
    """ 148: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_154


class State_149(State):
    """ 149: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_154


class State_150(State):
    """ 150: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_154


class State_151(State):
    """ 151: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_154


class State_152(State):
    """ 152: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_154


class State_153(State):
    """ 153: No description. """

    def previous_states(self):
        return [State_140]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_154


class State_154(State):
    """ 154: No description. """

    def previous_states(self):
        return [State_139, State_141, State_142, State_143, State_144, State_145, State_146, State_147, State_148, State_149, State_150, State_151, State_152, State_153]

    def test(self):
        return State_190


class State_155(State):
    """ 155: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_170


class State_156(State):
    """ 156: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 395, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_155
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_157
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_158
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_159
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_160
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_161
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_162
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_163
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_164
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_165
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_166
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_167
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_168
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_169


class State_157(State):
    """ 157: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_170


class State_158(State):
    """ 158: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_170


class State_159(State):
    """ 159: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_170


class State_160(State):
    """ 160: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_170


class State_161(State):
    """ 161: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_170


class State_162(State):
    """ 162: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_170


class State_163(State):
    """ 163: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_170


class State_164(State):
    """ 164: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_170


class State_165(State):
    """ 165: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_170


class State_166(State):
    """ 166: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_170


class State_167(State):
    """ 167: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_170


class State_168(State):
    """ 168: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_170


class State_169(State):
    """ 169: No description. """

    def previous_states(self):
        return [State_156]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_170


class State_170(State):
    """ 170: No description. """

    def previous_states(self):
        return [State_155, State_157, State_158, State_159, State_160, State_161, State_162, State_163, State_164, State_165, State_166, State_167, State_168, State_169]

    def test(self):
        return State_190


class State_171(State):
    """ 171: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_186


class State_172(State):
    """ 172: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 396, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_171
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_173
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_174
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_175
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_176
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_177
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_178
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_179
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_180
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_181
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_182
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_183
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_184
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_185


class State_173(State):
    """ 173: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_186


class State_174(State):
    """ 174: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_186


class State_175(State):
    """ 175: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_186


class State_176(State):
    """ 176: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_186


class State_177(State):
    """ 177: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_186


class State_178(State):
    """ 178: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_186


class State_179(State):
    """ 179: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_186


class State_180(State):
    """ 180: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_186


class State_181(State):
    """ 181: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_186


class State_182(State):
    """ 182: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_186


class State_183(State):
    """ 183: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_186


class State_184(State):
    """ 184: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_186


class State_185(State):
    """ 185: No description. """

    def previous_states(self):
        return [State_172]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_186


class State_186(State):
    """ 186: No description. """

    def previous_states(self):
        return [State_171, State_173, State_174, State_175, State_176, State_177, State_178, State_179, State_180, State_181, State_182, State_183, State_184, State_185]

    def test(self):
        return State_190


class State_187(State):
    """ 187: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010762, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_189
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_188
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_188


class State_188(State):
    """ 188: No description. """

    def previous_states(self):
        return [State_187]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_52


class State_189(State):
    """ 189: No description. """

    def previous_states(self):
        return [State_187]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_9


class State_190(State):
    """ 190: No description. """

    def previous_states(self):
        return [State_90, State_106, State_122, State_138, State_154, State_170, State_186]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010891, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='エスト瓶強化しました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_192
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_191
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_191


class State_191(State):
    """ 191: No description. """

    def previous_states(self):
        return [State_190]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_52


class State_192(State):
    """ 192: No description. """

    def previous_states(self):
        return [State_190]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_9
