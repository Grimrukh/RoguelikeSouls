from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_36


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
        return [State_8, State_12, State_14, State_15, State_16, State_17, State_19, State_20, State_21, State_28, State_29, State_31, State_33]

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
        return [State_2, State_4, State_5, State_11, State_15, State_17, State_23, State_24, State_30, State_32, State_33, State_34, State_36]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1548) == 0 and GetDistanceToPlayer() <= 5:
            return State_15
        if GetFlagState(1547) == 1 and IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71700053) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_34
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1545) == 1 and GetFlagState(71700051) == 1:
            return State_33
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1545) == 1 and GetFlagState(71700051) == 0:
            return State_20
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71700050) == 1 and GetFlagState(1543) == 1:
            return State_29
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71700049) == 1 and GetFlagState(1543) == 1:
            return State_28
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1543) == 1 and GetFlagState(71700049) == 0 and GetFlagState(71700050) == 0:
            return State_14
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1547) == 0 and GetFlagState(1548) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1548) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_16, State_19, State_20, State_28, State_29, State_31, State_33]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71700047) == 0 and GetSelfHP() <= 90:
            return State_12
        if GetFlagState(1547) == 1:
            return State_10
        if GetFlagState(71700046) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71700045) == 1:
            return State_21
        if GetFlagState(71700045) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_8
        if GetFlagState(71700046) == 1:
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
        TalkToPlayer(conversation=39020330, unk1=-1, unk2=-1)
        SetFlagState(flag=71700045, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71700045, state=1)

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
        return [State_9, State_10, State_13, State_22]

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
        TalkToPlayer(conversation=39020400, unk1=-1, unk2=-1)
        SetFlagState(flag=71700047, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71700047, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=39020000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_6, State_18]

    def enter(self):
        TalkToPlayer(conversation=39020500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_16(State):
    """ 16: No description. """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=38070100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_7, State_30]

    def enter(self):
        TalkToPlayer(conversation=39020500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_8, State_12, State_21]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if GetDistanceToPlayer() <= 5:
            return State_15

    def exit(self):
        RemoveMyAggro()


class State_19(State):
    """ 19: No description. """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=38070200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=39020100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=39020340, unk1=-1, unk2=-1)
        SetFlagState(flag=71700046, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71700046, state=1)

    def test(self):
        return State_11


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='YES')
        SetFlagState(flag=71700049, state=1)

    def test(self):
        return State_28


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='NO')
        SetFlagState(flag=71700050, state=1)

    def test(self):
        return State_29


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_26
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_26
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_25


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6, State_25]

    def enter(self):
        TalkToPlayer(conversation=39020020, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_6, State_26]

    def enter(self):
        TalkToPlayer(conversation=39020040, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        else:
            return State_6


class State_31(State):
    """ 31: No description. """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=38070210, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=71700051, state=1)
        SetFlagState(flag=11020606, state=1)

    def test(self):
        return State_6


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=39020200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=39020600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71700053, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_28, State_29]

    def enter(self):
        SetFlagState(flag=11020605, state=1)

    def test(self):
        return State_23
        # UNREACHABLE:
        # if 1:
        #     return State_23


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71700053, state=0)

    def test(self):
        return State_6
