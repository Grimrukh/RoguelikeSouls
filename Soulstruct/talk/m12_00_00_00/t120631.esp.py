from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_31


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
        return [State_8, State_12, State_14, State_16, State_17, State_18, State_20, State_22, State_24, State_26, State_28]

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
        return [State_2, State_4, State_5, State_11, State_15, State_16, State_17, State_25, State_26, State_29, State_30, State_31, State_32]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if IsClientPlayer() == 1:
            return State_32
        if CheckSelfDeath() == 1 and GetFlagState(1604) == 0 and GetDistanceToPlayer() <= 5:
            return State_17
        if GetFlagState(1603) == 1 and IsPlayerDead() == 1 and GetFlagState(71200029) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_30
        if GetFlagState(1603) == 1 and GetFlagState(71200025) == 0 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetSelfHP() <= 40 and GetFlagState(71200029) == 0:
            return State_24
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1600) == 1 and GetFlagState(71200027) == 0 and GetFlagState(71200026) == 1 and GetFlagState(11200597) == 1:
            return State_28
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1600) == 1 and GetFlagState(71200026) == 1:
            return State_16
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1600) == 1 and GetFlagState(71200026) == 0:
            return State_14
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1603) == 0 and GetFlagState(1604) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1604) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_16, State_28]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_26
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200024) == 0 and GetSelfHP() <= 90:
            return State_12
        if GetFlagState(1603) == 1:
            return State_10
        if GetFlagState(71200020) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_8
        if GetFlagState(71200020) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200021) == 0:
            return State_18
        if GetFlagState(71200021) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200022) == 0:
            return State_20
        if GetFlagState(71200022) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200023) == 0:
            return State_22
        if GetFlagState(71200023) == 1:
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
        TalkToPlayer(conversation=41000300, unk1=-1, unk2=-1)
        SetFlagState(flag=71200020, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71200020, state=1)

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
        return [State_9, State_10, State_13, State_19, State_21, State_23]

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
        TalkToPlayer(conversation=41000400, unk1=-1, unk2=-1)
        SetFlagState(flag=71200024, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71200024, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41000000, unk1=-1, unk2=-1)
        SetFlagState(flag=11400582, state=1)

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
        SetFlagState(flag=71200026, state=1)
        SetFlagState(flag=11200595, state=1)

    def test(self):
        return State_6


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_6, State_27]

    def enter(self):
        TalkToPlayer(conversation=41000600, unk1=-1, unk2=-1)
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
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41000310, unk1=-1, unk2=-1)
        SetFlagState(flag=71200021, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        SetFlagState(flag=71200021, state=1)

    def test(self):
        return State_11


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41000320, unk1=-1, unk2=-1)
        SetFlagState(flag=71200022, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=71200022, state=1)

    def test(self):
        return State_11


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41000330, unk1=-1, unk2=-1)
        SetFlagState(flag=71200023, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        SetFlagState(flag=71200023, state=1)

    def test(self):
        return State_11


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41000500, unk1=-1, unk2=-1)
        SetFlagState(flag=71200025, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_27
        if HasTalkEnded() == 1:
            return State_25
        if GetDistanceToPlayer() >= 15:
            return State_3


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        SetFlagState(flag=71200025, state=1)

    def test(self):
        return State_6


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_8, State_12, State_18, State_20, State_22, State_24]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17

    def exit(self):
        RemoveMyAggro()


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        SetFlagState(flag=71200027, state=1)

    def test(self):
        return State_6


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=41000700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71200029, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71200029, state=0)

    def test(self):
        return State_6


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DebugEvent(message='クライアント用待機')

    def test(self):
        if IsClientPlayer() == 0:
            return State_6
