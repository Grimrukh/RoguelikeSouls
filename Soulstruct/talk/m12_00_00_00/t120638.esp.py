from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_7


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_7


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_7


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DebugEvent(message='勧誘を受ける')

    def test(self):
        return State_21


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DebugEvent(message='勧誘を受けない')
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_22


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000000, unk1=-1, unk2=-1)
        DebugEvent(message='初対面')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_3


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_0, State_1, State_2, State_10, State_11, State_12, State_18, State_20, State_25, State_26, State_34, State_37, State_38, State_39, State_40, State_45, State_46, State_48, State_50, State_52, State_53, State_58, State_61]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)
        SetFlagState(flag=11205050, state=0)

    def test(self):
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(1712) == 1 and GetFlagState(11200596) == 0:
            return State_36
        if GetFlagState(71200043) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 20:
            return State_15
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200037) == 0 and GetFlagState(71200039) == 0 and GetFlagState(71200047) == 0 and GetFlagState(705) == 1 and ComparePlayerStatus(11, 5, 7) == 1 and GetFlagState(71200035) == 0 and GetFlagState(11200592) == 1:
            return State_62
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200037) == 0 and GetFlagState(71200039) == 0 and GetFlagState(71200047) == 0 and GetFlagState(705) == 1 and ComparePlayerStatus(11, 0, 7) == 1 and GetFlagState(71200035) == 0:
            return State_60
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200047) == 1 and ComparePlayerStatus(11, 5, 7) == 1:
            return State_56
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(11200592) == 1 and GetFlagState(71200037) == 0:
            return State_54
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200047) == 1 and GetFlagState(11200592) == 0:
            return State_47
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200040) == 1 and GetFlagState(71200037) == 0:
            return State_35
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200048) == 0 and GetFlagState(71200047) == 0 and GetFlagState(71200039) == 1:
            return State_29
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200036) == 1 and GetFlagState(71200039) == 0:
            return State_23
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200037) == 1 and GetFlagState(11200593) == 1 and GetFlagState(11200594) == 0 and ComparePlayerStatus(14, 4, 3) == 1:
            return State_33
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200037) == 1 and GetFlagState(71200038) == 0 and GetFlagState(11200593) == 0 and ComparePlayerStatus(14, 4, 1) == 1:
            return State_32
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(11206101) == 0 and GetFlagState(71200046) == 0 and ComparePlayerStatus(14, 4, 4) == 1:
            return State_51
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200037) == 1:
            return State_53
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200035) == 1 and GetFlagState(71200042) == 1:
            return State_20
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71200035) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3.5):
            return State_11
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetFlagState(1711) == 0 and GetFlagState(11200596) == 0:
            return State_10
        if IsAttackedBySomeone() == 1 and GetFlagState(1711) == 0:
            return State_19


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        TalkToPlayer(conversation=48000100, unk1=-1, unk2=-1)
        DebugEvent(message='Yes')

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        TalkToPlayer(conversation=48000700, unk1=-1, unk2=-1)
        DebugEvent(message='No')

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_7


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_7


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_13, State_14]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_7


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_12


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71200043, state=1)

    def test(self):
        return State_12


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_7, State_16, State_48]

    def enter(self):
        TalkToPlayer(conversation=48000800, unk1=-1, unk2=-1)
        SetFlagState(flag=71200043, state=1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_14
        if GetDistanceToPlayer() >= 23:
            return State_17


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_5, State_8, State_9, State_19, State_20, State_23, State_29, State_30, State_32, State_33, State_35, State_36, State_47, State_51, State_53, State_54, State_56, State_59, State_60, State_62]

    def enter(self):
        ClearTalkProgressData()
        SetFlagState(flag=11205050, state=0)

    def test(self):
        if GetFlagState(71200043) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 20:
            return State_15
        if GetFlagState(71200043) == 1:
            return State_13
        else:
            return State_13

    def exit(self):
        RemoveMyAggro()


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_5, State_8, State_9, State_15, State_20, State_23, State_29, State_30, State_32, State_33, State_35, State_36, State_47, State_51, State_53, State_54, State_56, State_59, State_60, State_62]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if ComparePlayerStatus(11, 5, 7) == 1:
            return State_58
        else:
            return State_18


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_7


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_16


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000702, unk1=-1, unk2=-1)
        DebugEvent(message='Noあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        SetFlagState(flag=71200036, state=1)
        SetFlagState(flag=71200035, state=1)

    def test(self):
        return State_8


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        SetFlagState(flag=71200042, state=1)
        SetFlagState(flag=71200035, state=1)

    def test(self):
        return State_9


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000100, unk1=-1, unk2=-1)
        DebugEvent(message='Yesあと')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_8, State_23, State_35, State_56, State_63]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_26
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_27


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_30, State_31]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_7


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_7


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='勧誘を受ける')
        SetFlagState(flag=71200039, state=1)

    def test(self):
        return State_29


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='勧誘を受けない')
        SetFlagState(flag=71200040, state=1)
        SetFlagState(flag=71200039, state=1)
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_30


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_7, State_27]

    def enter(self):
        TalkToPlayer(conversation=48000200, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yes')
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_28, State_42]

    def enter(self):
        TalkToPlayer(conversation=48000500, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-No')

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_54, State_59]

    def enter(self):
        SetFlagState(flag=71200037, state=1)
        SetFlagState(flag=71200039, state=1)

    def test(self):
        return State_25


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000300, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yesあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_17


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000400, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yesあと2')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_17


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71200038, state=1)
        SetFlagState(flag=11200593, state=1)
        SetFlagState(flag=11400582, state=1)

    def test(self):
        return State_7


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000600, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Noあと')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000900, unk1=-1, unk2=-1)
        DebugEvent(message='裏切った')
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 20:
            return State_17


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        SetFlagState(flag=71200044, state=1)
        SetFlagState(flag=11200596, state=1)

    def test(self):
        return State_7


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        SetFlagState(flag=71200045, state=1)
        SetFlagState(flag=11206101, state=1)
        SetFlagState(flag=11200594, state=1)

    def test(self):
        return State_7


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_47, State_59]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_7


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_7


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=7)
        SetFlagState(flag=71200047, state=1)
        SetFlagState(flag=848, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_46
        if GetFlagState(848) == 0:
            return State_55


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        DebugEvent(message='誓約を変更しない')
        SetFlagState(flag=71200048, state=1)
        SetFlagState(flag=71200040, state=1)
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_30


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=1)
        ChangePlayerStats(unk1=31, unk2=5, unk3=7)
        RequestUnlockTrophy(11)

    def test(self):
        if IsMultiplayerInProgress() == 1:
            return State_57
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_40
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_42
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_42
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_41


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71200047, state=1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_46
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_45
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_45


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44, State_57]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_7


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_41, State_44, State_55, State_57]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_7


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_7, State_55]

    def enter(self):
        TalkToPlayer(conversation=48000210, unk1=-1, unk2=-1)
        DebugEvent(message='誓約したあと')
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_50
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_17


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_6, State_24, State_43, State_44, State_55, State_57]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if GetFlagState(71200043) == 0 and GetDistanceToPlayer() <= 20:
            return State_15
        else:
            return State_7


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_29]

    def test(self):
        if ComparePlayerStatus(11, 0, 7) == 1:
            return State_44
        if IsMultiplayerInProgress() == 1:
            return State_57
        else:
            return State_43


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        SetFlagState(flag=11200592, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_7
        if IsMenuOpen(63) == 0:
            return State_54


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48001000, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yesあと2')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        SetFlagState(flag=71200046, state=1)

    def test(self):
        return State_7


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000320, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yesあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_7, State_50]

    def enter(self):
        TalkToPlayer(conversation=48000220, unk1=-1, unk2=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わしました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_46
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(11200592) == 1:
            return State_59
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0 and GetFlagState(11200592) == 1:
            return State_59
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_47
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_47


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000103, unk1=-1, unk2=-1)
        DebugEvent(message='Yesあと')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_43, State_49]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010747, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='マルチプレイ中')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_46
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_45
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_45


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ForceEndTalk(unk1=0)
        SetFlagState(flag=11205050, state=0)

    def test(self):
        return State_7


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        TalkToPlayer(conversation=48000221, unk1=-1, unk2=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17
        if HasTalkEnded() == 1:
            return State_39


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000320, unk1=-1, unk2=-1)
        DebugEvent(message='Yes-Yesあと1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        SetFlagState(flag=71200037, state=1)
        SetFlagState(flag=71200039, state=1)
        SetFlagState(flag=71200047, state=1)
        SetFlagState(flag=71200035, state=1)
        SetFlagState(flag=11206101, state=1)

    def test(self):
        return State_7


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=48000103, unk1=-1, unk2=-1)
        DebugEvent(message='Yesあと')
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=11205050, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1:
            return State_16
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=71200037, state=1)
        SetFlagState(flag=71200039, state=1)
        SetFlagState(flag=71200047, state=1)
        SetFlagState(flag=71200035, state=1)
        SetFlagState(flag=11206101, state=1)

    def test(self):
        return State_24
