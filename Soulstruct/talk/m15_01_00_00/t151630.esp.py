from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_3


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_3


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_4, State_6]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_0, State_1, State_5, State_7]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if GetFlagState(8103) == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(8104) == 0 and GetFlagState(1578) == 1 and GetFlagState(11510700) == 1:
            return State_6
        if GetFlagState(8103) == 0 and GetDistanceToPlayer() <= 15 and GetFlagState(1578) == 1 and GetFlagState(11510700) == 1:
            return State_4


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=40020200, unk1=-1, unk2=-1)
        SetFlagState(flag=11510598, state=1)
        SetFlagState(flag=8103, state=1)
        SetFlagState(flag=8104, state=1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 16:
            return State_2
        if HasTalkEnded() == 1:
            return State_5


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        SetFlagState(flag=8103, state=1)
        SetFlagState(flag=11510598, state=1)
        SetFlagState(flag=8104, state=1)

    def test(self):
        return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=40020300, unk1=-1, unk2=-1)
        SetFlagState(flag=11510598, state=1)
        SetFlagState(flag=8104, state=1)
        ForceCloseMenu()

    def test(self):
        if GetDistanceToPlayer() >= 16:
            return State_2
        if HasTalkEnded() == 1:
            return State_7


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        SetFlagState(flag=8104, state=1)
        SetFlagState(flag=11510598, state=1)

    def test(self):
        return State_3


class State_8(State):
    """ 8: No description. """
