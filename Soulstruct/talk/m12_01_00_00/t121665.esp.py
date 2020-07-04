from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_1


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_0, State_5, State_6]

    def enter(self):
        DebugEvent(message='最初')

    def test(self):
        if DoesPlayerHaveSpEffect() >= 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and CheckSpecificPersonGenericDialogIsOpen() == 1:
            return State_4
        if GetOneLineHelpStatus() == 1 and (GetWhetherEnemiesAreNearby(14, 1) == 1 or IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_6
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and GetOneLineHelpStatus() == 1 and CheckSpecificPersonGenericDialogIsOpen() == 1:
            return State_4
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and GetOneLineHelpStatus() == 1 and CheckSpecificPersonGenericDialogIsOpen() == 0:
            return State_2
        if GetOneLineHelpStatus() == 0 and GetWhetherEnemiesAreNearby(15, 1) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2:
            return State_5


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_3


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=150400, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_6
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_6
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_6


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        Command_talk_1_77()
        StartBonfireAnimLoop()
        ReportConversationEndToHavokBehavior(5)
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()
        SetFlagState(flag=760, state=0)

    def test(self):
        if GetWhetherEnemiesAreNearby(14, 1) == 1 or IsPlayerDead() == 1 or CheckSelfDeath() == 1:
            return State_7
        if GetTalkListEntryResult() == 0:
            return State_9


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=10010135)

    def test(self):
        return State_1


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_1, State_3, State_8]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_4, State_9]

    def enter(self):
        OpenConversationChoicesMenu()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_8


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマーをクリア\u3000待機へ')

    def test(self):
        return State_6


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_7
