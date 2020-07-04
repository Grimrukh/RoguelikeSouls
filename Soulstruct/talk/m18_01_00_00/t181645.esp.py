from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_2


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=55000200, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 10:
            return State_3
        if HasTalkEnded() == 1:
            return State_9


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_0, State_4, State_6, State_8, State_9, State_11]

    def enter(self):
        DebugEvent(message='待機')

    def test(self):
        if GetFlagState(71810093) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(11815102) == 1 and GetFlagState(11815151) == 1:
            return State_10
        if GetFlagState(71810092) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(11815101) == 1 and GetFlagState(11815151) == 1:
            return State_1
        if GetFlagState(71810091) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(11816100) == 0 and GetFlagState(71810090) == 1 and GetFlagState(11815151) == 1:
            return State_5
        if GetFlagState(71810090) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(11816100) == 0 and GetFlagState(11815151) == 1:
            return State_7


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1, State_5, State_7, State_10]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_2


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=55000100, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 10:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        SetFlagState(flag=71810091, state=1)
        SetFlagState(flag=11816100, state=1)
        SetFlagState(flag=71810090, state=0)

    def test(self):
        return State_2


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=55000000, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 10:
            return State_3
        if HasTalkEnded() == 1:
            return State_8


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71810090, state=1)
        SetFlagState(flag=11816100, state=1)
        SetFlagState(flag=71810091, state=0)

    def test(self):
        return State_2


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        SetFlagState(flag=71810092, state=1)

    def test(self):
        return State_2


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        TalkToPlayer(conversation=55000300, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 10:
            return State_3
        if HasTalkEnded() == 1:
            return State_11


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        SetFlagState(flag=71810093, state=1)

    def test(self):
        return State_2
