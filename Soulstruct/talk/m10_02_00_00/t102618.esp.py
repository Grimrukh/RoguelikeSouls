from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_15


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        OpenRegularShop(2400, 2499)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_18
        if IsMenuOpen(11) == 0:
            return State_3


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1, State_13, State_22]

    def enter(self):
        AddTalkListData(menu_index=2, menu_text=15000240, required_flag=-1)
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if GetTalkListEntryResult() == 0:
            return State_24
        if GetTalkListEntryResult() == 1:
            return State_2
        if GetTalkListEntryResult() == 4:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if GetTalkListEntryResult() == 2:
            return State_61

    def exit(self):
        ClearTalkListData()


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_18, State_19]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_15


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_18, State_19]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_4
        else:
            return State_26


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71600039, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28003400, unk1=-1, unk2=-1)
        SetFlagState(flag=71600039, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_30
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_20


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_10, State_48, State_50, State_52]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_15


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        SetFlagState(flag=71600035, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28003300, unk1=-1, unk2=-1)
        SetFlagState(flag=71600035, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_30
        if HasTalkEnded() == 1:
            return State_10
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_12(State):
    """ 12: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_55, State_56, State_59, State_64]

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_15


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_12, State_23, State_25, State_28, State_31, State_32, State_33, State_34, State_35, State_36, State_37, State_38, State_40, State_41, State_42, State_44, State_45, State_46, State_47]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_29
        if GetFlagState(71600039) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1314) == 1:
            return State_9
        if GetFlagState(71600038) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600037) == 1:
            return State_53
        if GetFlagState(71600037) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600036) == 1:
            return State_51
        if GetFlagState(71600036) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600035) == 1:
            return State_49
        if GetFlagState(71600035) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_11
        if GetFlagState(71600038) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_0, State_4, State_8, State_13, State_16, State_17, State_18, State_21, State_22, State_24, State_26, State_27, State_29, State_54, State_60, State_62, State_65]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1315) == 0 and GetDistanceToPlayer() <= 5:
            return State_27
        if GetFlagState(71600051) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_42
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71600051) == 0:
            return State_38
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1314) == 0 and GetFlagState(1315) == 0:
            return State_16
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_17
        if IsAttackedBySomeone() == 1 and GetFlagState(1315) == 0:
            return State_23


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_15


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_15


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_29
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4
        else:
            return State_15


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_29
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_7, State_11, State_12, State_25, State_27, State_28, State_29, State_31, State_32, State_33, State_34, State_35, State_36, State_37, State_38, State_40, State_41, State_42, State_44, State_45, State_46, State_47, State_49, State_51, State_53]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_21


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_15


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_39, State_43]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_15


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_14


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        return State_15


class State_25(State):
    """ 25: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        return State_15


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_15, State_30]

    def enter(self):
        TalkToPlayer(conversation=28003500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1 and HasTalkEnded() == 1:
            return State_15
        if GetDistanceToPlayer() >= 5:
            return State_20


class State_28(State):
    """ 28: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_14, State_18, State_19, State_62]

    def enter(self):
        TalkToPlayer(conversation=28003500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_15
        if GetDistanceToPlayer() >= 5:
            return State_20


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_7, State_11, State_49, State_51, State_53]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_27

    def exit(self):
        RemoveMyAggro()


class State_31(State):
    """ 31: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001540, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_32(State):
    """ 32: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_33(State):
    """ 33: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_34(State):
    """ 34: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_35(State):
    """ 35: No description. """

    def enter(self):
        TalkToPlayer(conversation=28000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_36(State):
    """ 36: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001520, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_37(State):
    """ 37: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001530, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=28001300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71600051, state=1)

    def test(self):
        return State_22


class State_40(State):
    """ 40: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_41(State):
    """ 41: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001010, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=28001400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        SetFlagState(flag=71600052, state=1)

    def test(self):
        return State_22


class State_44(State):
    """ 44: No description. """

    def enter(self):
        TalkToPlayer(conversation=28002000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_45(State):
    """ 45: No description. """

    def enter(self):
        TalkToPlayer(conversation=28002100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_46(State):
    """ 46: No description. """

    def enter(self):
        TalkToPlayer(conversation=28002200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_47(State):
    """ 47: No description. """

    def enter(self):
        TalkToPlayer(conversation=28001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=71600036, state=1)

    def test(self):
        return State_8


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28003310, unk1=-1, unk2=-1)
        SetFlagState(flag=71600036, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_30
        if HasTalkEnded() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        SetFlagState(flag=71600037, state=1)

    def test(self):
        return State_8


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28003320, unk1=-1, unk2=-1)
        SetFlagState(flag=71600037, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_30
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        SetFlagState(flag=71600038, state=1)

    def test(self):
        return State_8


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28003330, unk1=-1, unk2=-1)
        SetFlagState(flag=71600038, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_30
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        DebugEvent(message='解呪する')
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)
        SetFlagState(flag=754, state=1)

    def test(self):
        return State_13


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        DebugEvent(message='解呪しない')

    def test(self):
        return State_13


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020060, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_54
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_56
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_56
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_55


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010761, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性が足りない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_60
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_59
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_59


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(751) == 0:
            return State_63
        if ComparePlayerStatus(10, 0, 0) == 1:
            return State_58
        else:
            return State_57


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_57, State_58, State_63]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_29
        else:
            return State_15


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010733, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='呪われていない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_65
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_64
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_64


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15
