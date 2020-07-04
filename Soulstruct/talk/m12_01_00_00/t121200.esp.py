from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_1


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_0, State_2, State_3, State_14, State_15, State_16]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 1.6:
            return State_2
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 1.6):
            return State_3
        if GetFlagState(765) == 1 and GetOneLineHelpStatus() == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 1.6:
            return State_17
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 1.6 and GetOneLineHelpStatus() == 1:
            return State_10


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=10010130)

    def test(self):
        return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_1


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_6, State_7, State_8, State_10, State_12]

    def enter(self):
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=1, menu_text=15000400, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000405, required_flag=-1)
        AddTalkListData(menu_index=3, menu_text=15000410, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000415, required_flag=-1)
        AddTalkListData(menu_index=5, menu_text=15000416, required_flag=-1)
        AddTalkListData(menu_index=6, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsPlayerDead() == 1:
            return State_13
        if HasPlayerBeenAttacked() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_13
        if GetTalkListEntryResult() == 6:
            return State_11
        if GetTalkListEntryResult() == 0:
            return State_11
        if GetTalkListEntryResult() == 1:
            return State_6
        if GetTalkListEntryResult() == 2:
            return State_5
        if GetTalkListEntryResult() == 3:
            return State_12
        if GetTalkListEntryResult() == 4:
            return State_7
        if GetTalkListEntryResult() == 5:
            return State_8

    def exit(self):
        ClearTalkListData()


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenArenaRanking(5)

    def test(self):
        if HasPlayerBeenAttacked() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_9
        if IsRankingMenuOpen(5) == 0:
            return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenArenaRanking(0)

    def test(self):
        if HasPlayerBeenAttacked() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_9
        if IsRankingMenuOpen(0) == 0:
            return State_4


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenArenaRanking(20)

    def test(self):
        if HasPlayerBeenAttacked() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_9
        if IsRankingMenuOpen(20) == 0:
            return State_4


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenArenaRanking(15)

    def test(self):
        if HasPlayerBeenAttacked() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_9
        if IsRankingMenuOpen(15) == 0:
            return State_4


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_5, State_6, State_7, State_8, State_12]

    def enter(self):
        CloseMenu()

    def test(self):
        return State_13


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()

    def test(self):
        if GetDistanceToPlayer() >= 2:
            return State_13
        else:
            return State_4


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        return State_13


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenArenaRanking(10)

    def test(self):
        if HasPlayerBeenAttacked() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 2:
            return State_9
        if IsRankingMenuOpen(10) == 0:
            return State_4


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_4, State_9, State_10, State_11]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')

    def test(self):
        return State_14


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマーをクリア\u3000待機へ')

    def test(self):
        return State_1


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_1


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_1


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=150401, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='オフライン')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsPlayerDead() == 1 or HasPlayerBeenAttacked() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_15
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_16
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_16
