from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_Default(State):
    """ 0: No description. """

    def test(self):
        return State_AwaitTalk


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_GiveRing


class State_ForceEndTalk(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_InterruptTalk]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_AwaitTalk


class State_InterruptTalk(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_8, State_12, State_SayFirstLines, State_16, State_SayRingLines, State_18, State_SayReassuranceLines]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_ForceEndTalk


class State_DisableTalkPrompt(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_AwaitTalk


class State_EnableTalkPrompt(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_AwaitTalk


class State_AwaitTalk(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_Default, State_ForceEndTalk, State_DisableTalkPrompt, State_EnableTalkPrompt, State_11, State_FinishedFirstLines, State_16, State_SayRingLines, State_18, State_AssuranceLinesDone]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(1850) == 1 and GetFlagState(71020001) == 0:
            return State_SayReassuranceLines
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71020000) == 1:
            return State_SayRingLines
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71020000) == 0:
            return State_SayFirstLines
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4:
            return State_EnableTalkPrompt  # Enable Talk prompt.
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 4):
            return State_DisableTalkPrompt


class State_GiveRing(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_SayFirstLines, State_SayRingLines, State_SayReassuranceLines]

    def enter(self):
        GetItemFromItemLot(51000)
        SetFlagState(11022000, 1)
        ClearTalkProgressData()

    def test(self):
        return State_AwaitTalk


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_GiveRing]

    def enter(self):
        TalkToPlayer(conversation=20000800, unk1=-1, unk2=-1)
        SetFlagState(flag=71310030, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_InterruptTalk


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71310030, state=1)

    def test(self):
        return State_11


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_GiveRing]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_11


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_9, State_10, State_13]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_AwaitTalk


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_GiveRing]

    def enter(self):
        TalkToPlayer(conversation=20000600, unk1=-1, unk2=-1)
        SetFlagState(flag=71310031, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_InterruptTalk


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71310031, state=1)

    def test(self):
        return State_11


class State_SayFirstLines(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=23010040, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_FinishedFirstLines
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_InterruptTalk


class State_FinishedFirstLines(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_SayFirstLines]

    def enter(self):
        SetFlagState(flag=71020000, state=1)

    def test(self):
        return State_AwaitTalk


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_AwaitTalk, State_19]

    def enter(self):
        TalkToPlayer(conversation=20000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_AwaitTalk
        if GetDistanceToPlayer() >= 5:
            return State_InterruptTalk


class State_SayRingLines(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=23010020, unk1=-1, unk2=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_InterruptTalk
        if HasTalkEnded() == 1:
            return State_GiveRing


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_GiveRing]

    def enter(self):
        TalkToPlayer(conversation=20000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_AwaitTalk
        if GetDistanceToPlayer() >= 5:
            return State_InterruptTalk


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_8, State_12]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_SayReassuranceLines(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_AwaitTalk]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=23010120, unk1=-1, unk2=-1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_AssuranceLinesDone
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_InterruptTalk


class State_AssuranceLinesDone(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_SayReassuranceLines]

    def enter(self):
        SetFlagState(flag=71020001, state=1)

    def test(self):
        return State_AwaitTalk
