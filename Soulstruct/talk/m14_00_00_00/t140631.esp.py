from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_47


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
        return [State_8, State_12, State_14, State_29, State_30, State_32, State_34, State_36, State_38, State_39, State_40, State_42, State_52]

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
        return [State_2, State_4, State_5, State_11, State_20, State_22, State_23, State_25, State_26, State_27, State_36, State_44, State_46, State_47, State_49, State_50, State_51, State_52, State_53, State_54, State_57]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if IsClientPlayer() == 1:
            return State_57
        if CheckSelfDeath() == 1 and GetFlagState(1604) == 0 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_46
        if GetFlagState(1603) == 1 and GetFlagState(71200065) == 0 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetSelfHP() <= 40 and GetFlagState(71200077) == 0:
            return State_52
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1601) == 1:
            return State_37
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1603) == 0 and GetFlagState(1604) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1604) == 0 and GetFlagState(1608) == 0 and GetFlagState(1609) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_29, State_38, State_39, State_40, State_42]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71200064) == 0 and GetSelfHP() <= 90 and GetFlagState(1194) == 0:
            return State_12
        if GetFlagState(1607) == 1:
            return State_10
        if GetFlagState(1606) == 1:
            return State_10
        if GetFlagState(1603) == 1:
            return State_10
        if GetFlagState(71200063) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1601) == 1 and GetFlagState(71200062) == 1:
            return State_34
        if GetFlagState(71200062) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1601) == 1 and GetFlagState(71200061) == 1:
            return State_32
        if GetFlagState(71200061) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1601) == 1 and GetFlagState(71200060) == 1:
            return State_30
        if GetFlagState(71200060) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1601) == 1:
            return State_8
        if GetFlagState(71200063) == 1:
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
        TalkToPlayer(conversation=41011600, unk1=-1, unk2=-1)
        SetFlagState(flag=71200060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71200060, state=1)

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
        return [State_9, State_10, State_13, State_31, State_33, State_35]

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
        TalkToPlayer(conversation=41011700, unk1=-1, unk2=-1)
        SetFlagState(flag=71300059, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71200064, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41010100, unk1=-1, unk2=-1)

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
        SetFlagState(flag=71200067, state=1)
        SetFlagState(flag=11406106, state=1)

    def test(self):
        return State_25


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6, State_7, State_17, State_23, State_24, State_54]

    def test(self):
        return State_36


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_8, State_12, State_30, State_32, State_34, State_52]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        return State_45


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_22, State_25, State_45]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000011, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=2, menu_text=15000350, required_flag=281)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_26
        if GetTalkListEntryResult() == 1:
            return State_18
        if GetTalkListEntryResult() == 4:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_24
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if GetTalkListEntryResult() == 2:
            return State_48

    def exit(self):
        ClearTalkListData()


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_21, State_23, State_24]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_23, State_24]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_20
        else:
            return State_27


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_55]

    def test(self):
        return State_19
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_45, State_48]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_21
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_20
        else:
            return State_6


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_21
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_20


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_15, State_41, State_43]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_19
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1:
            return State_28
        else:
            return State_6


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_21]

    def test(self):
        return State_6


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetRNGSeed()

    def test(self):
        if GetFlagState(71200080) == 0:
            return State_29
        if GetFlagState(71200081) == 0:
            return State_38
        else:
            return State_39


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=41010300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41011610, unk1=-1, unk2=-1)
        SetFlagState(flag=71200061, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71200061, state=1)

    def test(self):
        return State_11


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41011620, unk1=-1, unk2=-1)
        SetFlagState(flag=71200062, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71200062, state=1)

    def test(self):
        return State_11


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=41011630, unk1=-1, unk2=-1)
        SetFlagState(flag=71200063, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71200063, state=1)

    def test(self):
        return State_11


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=41011900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71200067) == 1 and GetFlagState(11406106) == 0:
            return State_42
        if GetFlagState(71200066) == 1:
            return State_14
        if GetFlagState(71200066) == 0:
            return State_40


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        TalkToPlayer(conversation=41010400, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41010000, unk1=-1, unk2=-1)

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
        SetFlagState(flag=71200066, state=1)

    def test(self):
        return State_25


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41010200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        SetFlagState(flag=71200068, state=1)

    def test(self):
        return State_25


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        TalkToPlayer(conversation=41012000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71200077, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        OpenRegularShop(1700, 1799)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_23
        if IsMenuOpen(11) == 0:
            return State_19


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(1603) == 1 and GetFlagState(71200077) == 0:
            return State_44
        else:
            return State_6


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        ShuffleRNGSeed(100)
        SetFlagState(flag=71200077, state=0)
        SetFlagState(flag=71200078, state=0)
        SetFlagState(flag=71200079, state=0)

    def test(self):
        return State_6


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9010, 1)
        AcquireGesture(10)
        SetFlagState(flag=281, state=0)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_23
        if IsMenuOpen(63) == 0:
            return State_56


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        SetFlagState(flag=71200080, state=1)

    def test(self):
        return State_6


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71200081, state=1)

    def test(self):
        return State_6


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71200080, state=0)
        SetFlagState(flag=71200081, state=0)

    def test(self):
        return State_6


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=41011800, unk1=-1, unk2=-1)
        SetFlagState(flag=71200065, state=1)
        SetFlagState(flag=71200064, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 15:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        else:
            return State_6


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_22


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_53
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_55
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_55


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DebugEvent(message='クライアント用待機')

    def test(self):
        if IsClientPlayer() == 0:
            return State_6
