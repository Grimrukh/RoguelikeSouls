from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_6


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
        return [State_8, State_12, State_19, State_27, State_30, State_32, State_34, State_36, State_38, State_39, State_40, State_42, State_43, State_44, State_46, State_47, State_52, State_53]

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
        return [State_0, State_2, State_4, State_5, State_11, State_17, State_20, State_21, State_23, State_24, State_25, State_38, State_39, State_52, State_53, State_55, State_56]

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1435) == 0 and GetDistanceToPlayer() <= 5:
            return State_38
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1431) == 1 and GetFlagState(71320006) == 1:
            return State_47
        if GetFlagState(11006100) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71320006) == 1:
            return State_44
        if GetFlagState(71320006) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_42
        if GetFlagState(71320006) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_40
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1434) == 0 and GetFlagState(1435) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1435) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_19, State_27, State_40, State_42, State_43, State_44, State_46, State_47, State_52, State_53]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_39
        if GetDistanceToPlayer() <= 5 and GetFlagState(71320005) == 0 and GetSelfHP() <= 90 and IsPlayerAttacking() == 1:
            return State_12
        if GetFlagState(1434) == 1:
            return State_10
        if GetFlagState(71320004) == 1:
            return State_10
        if GetFlagState(71320004) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(71320003) == 1 and IsPlayerAttacking() == 1:
            return State_36
        if GetFlagState(71320003) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(71320002) == 1 and IsPlayerAttacking() == 1:
            return State_34
        if GetFlagState(71320002) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(71320001) == 1 and IsPlayerAttacking() == 1:
            return State_32
        if GetFlagState(71320001) == 0 and GetDistanceToPlayer() <= 5 and GetFlagState(71320000) == 1 and IsPlayerAttacking() == 1:
            return State_30
        if GetFlagState(71320000) == 0 and GetDistanceToPlayer() <= 5 and IsPlayerAttacking() == 1:
            return State_8
        else:
            return State_10

    def exit(self):
        RemoveMyAggro()


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=36000600, unk1=-1, unk2=-1)
        SetFlagState(flag=71320000, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71320000, state=1)

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
        return [State_9, State_10, State_13, State_31, State_33, State_35, State_37]

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
        TalkToPlayer(conversation=36000700, unk1=-1, unk2=-1)
        SetFlagState(flag=71320005, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71320005, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_8, State_12, State_30, State_32, State_34, State_36]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_38

    def exit(self):
        RemoveMyAggro()


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if GetFlagState(1431) == 1:
            return State_60
        if GetFlagState(1430) == 1:
            return State_48


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_20, State_23, State_48, State_60]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000350, required_flag=288)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_24
        if GetTalkListEntryResult() == 3:
            return State_26
        if GetTalkListEntryResult() == 1:
            return State_15
        if GetTalkListEntryResult() == 4:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_22
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if GetTalkListEntryResult() == 2:
            return State_54

    def exit(self):
        ClearTalkListData()


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_18, State_21, State_22]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_21, State_22]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_17
        else:
            return State_25


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=36000900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19, State_49, State_50, State_51, State_57]

    def test(self):
        return State_16
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_48, State_54, State_60]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_39
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_18
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_17
        else:
            return State_6


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_39
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_18
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_17


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_41, State_45, State_47, State_59]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_16
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_28
        if DidYouDoSomethingInTheMenu(11) == 0:
            return State_29
        else:
            return State_6


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_18]

    def test(self):
        return State_6


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1 and GetFlagState(71320011) == 0 and GetFlagState(1431) == 1 and GetFlagState(71320010) == 1:
            return State_46
        if DidYouDoSomethingInTheMenu(11) == 1 and GetFlagState(71320010) == 0 and GetFlagState(71320009) == 1 and GetFlagState(2) == 1:
            return State_43
        if DidYouDoSomethingInTheMenu(11) == 1 and GetFlagState(71320009) == 0:
            return State_27
        else:
            return State_19


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=36001000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_52


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_53


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=36000610, unk1=-1, unk2=-1)
        SetFlagState(flag=71320001, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71320001, state=1)

    def test(self):
        return State_11


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=36000620, unk1=-1, unk2=-1)
        SetFlagState(flag=71320002, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71320002, state=1)

    def test(self):
        return State_11


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=36000630, unk1=-1, unk2=-1)
        SetFlagState(flag=71320003, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71320003, state=1)

    def test(self):
        return State_11


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=36000640, unk1=-1, unk2=-1)
        SetFlagState(flag=71320004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        SetFlagState(flag=71320004, state=1)

    def test(self):
        return State_11


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_6, State_14]

    def enter(self):
        ForceCloseMenu()
        TalkToPlayer(conversation=36000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_7, State_21, State_22, State_56]

    def enter(self):
        ForceCloseMenu()
        TalkToPlayer(conversation=36000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_6


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=36000000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        SetFlagState(flag=71320006, state=1)
        SetFlagState(flag=11006100, state=1)

    def test(self):
        return State_23


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=36000020, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=36001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=36000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71320008, state=1)

    def test(self):
        return State_23


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=36001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=36000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        OpenRegularShop(1500, 1569)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_21
        if IsMenuOpen(11) == 0:
            return State_16


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        SetFlagState(flag=71320009, state=1)

    def test(self):
        return State_20


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        SetFlagState(flag=71320010, state=1)

    def test(self):
        return State_20


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71320011, state=1)

    def test(self):
        return State_20


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=36000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=36000500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9004, 1)
        AcquireGesture(4)
        SetFlagState(flag=288, state=0)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_21
        if IsMenuOpen(63) == 0:
            return State_58


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_39
        else:
            return State_6


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_20


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_55
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_57
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_57


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        SetFlagState(flag=71320007, state=1)
        SetFlagState(flag=11006100, state=1)

    def test(self):
        return State_23


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        OpenRegularShop(1500, 1599)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_21
        if IsMenuOpen(11) == 0:
            return State_16
