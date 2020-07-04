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
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if GetTalkListEntryResult() == 0:
            return State_24
        if GetTalkListEntryResult() == 3:
            return State_27
        if GetTalkListEntryResult() == 1:
            return State_2
        if GetTalkListEntryResult() == 4:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if GetTalkListEntryResult() == 2:
            return State_83

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
        SetFlagState(flag=71600034, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28002400, unk1=-1, unk2=-1)
        SetFlagState(flag=71600034, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_20


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_10, State_63, State_65, State_67]

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
        SetFlagState(flag=71600030, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28002300, unk1=-1, unk2=-1)
        SetFlagState(flag=71600030, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_10
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_75]

    def enter(self):
        TalkToPlayer(conversation=28000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_56, State_58, State_60, State_62, State_77, State_78, State_81, State_88]

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_15


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_12, State_23, State_25, State_29, State_33, State_34, State_37, State_39, State_41, State_43, State_45, State_47, State_49, State_51, State_53, State_55, State_57, State_59, State_61, State_85]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_31
        if GetFlagState(71600034) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1314) == 1:
            return State_9
        if GetFlagState(71600033) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600032) == 1:
            return State_68
        if GetFlagState(71600032) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600031) == 1:
            return State_66
        if GetFlagState(71600031) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600030) == 1:
            return State_64
        if GetFlagState(71600030) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_11
        if GetFlagState(71600033) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_0, State_4, State_8, State_13, State_16, State_17, State_18, State_21, State_22, State_24, State_26, State_28, State_31, State_35, State_50, State_52, State_72, State_73, State_76, State_82, State_84, State_89]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1315) == 0 and GetDistanceToPlayer() <= 5:
            return State_28
        if GetFlagState(13) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_34
        if GetFlagState(71600061) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_53
        if GetFlagState(1312) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(71600061) == 0:
            return State_36
        if GetFlagState(11600592) == 1 and GetFlagState(71600060) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_33
        if GetFlagState(1311) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(11600592) == 0:
            return State_42
        if GetFlagState(751) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_74
        if GetFlagState(751) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_75
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
            return State_31
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
            return State_31
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_7, State_11, State_12, State_25, State_28, State_29, State_31, State_33, State_34, State_37, State_39, State_41, State_43, State_45, State_47, State_49, State_51, State_53, State_55, State_57, State_59, State_61, State_64, State_66, State_68, State_85]

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
        return [State_30, State_38, State_40, State_48, State_54, State_69, State_70, State_71, State_86]

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

    def previous_states(self):
        return [State_74]

    def enter(self):
        TalkToPlayer(conversation=28000400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_70
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
        return [State_3]

    def test(self):
        if GetFlagState(1312) == 1 and GetFlagState(11606100) == 0 and GetFlagState(71600059) == 1:
            return State_61
        if GetFlagState(1312) == 1:
            return State_59
        if GetFlagState(1311) == 1:
            return State_57
        else:
            return State_55


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_15, State_32]

    def enter(self):
        TalkToPlayer(conversation=28002500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_15
        if GetDistanceToPlayer() >= 5:
            return State_20


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_75]

    def enter(self):
        TalkToPlayer(conversation=28000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        SetFlagState(flag=71600040, state=1)
        SetFlagState(flag=71600062, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_22


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_14, State_18, State_19, State_84]

    def enter(self):
        TalkToPlayer(conversation=28002500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_15
        if GetDistanceToPlayer() >= 5:
            return State_20


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_7, State_11, State_64, State_66, State_68]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_28

    def exit(self):
        RemoveMyAggro()


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_15, State_72]

    def enter(self):
        TalkToPlayer(conversation=28001540, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=28001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        SetFlagState(flag=71600060, state=1)

    def test(self):
        return State_15


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(1644) == 1:
            return State_49
        if GetFlagState(1644) == 0:
            return State_51


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        TalkToPlayer(conversation=28000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=71600045, state=1)

    def test(self):
        return State_22


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_75]

    def enter(self):
        TalkToPlayer(conversation=28000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=71600043, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_22


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        TalkToPlayer(conversation=28000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_71
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(71600062) == 1:
            return State_43
        if GetFlagState(71600062) == 0:
            return State_45


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=28001520, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_20


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        SetFlagState(flag=71600053, state=1)

    def test(self):
        return State_72


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=28001530, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_46
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_20


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        SetFlagState(flag=71600054, state=1)
        SetFlagState(flag=71600062, state=1)
        SetFlagState(flag=71600040, state=1)

    def test(self):
        return State_72


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_74, State_75]

    def enter(self):
        TalkToPlayer(conversation=28000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        SetFlagState(flag=71600046, state=1)

    def test(self):
        return State_22


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        TalkToPlayer(conversation=28001000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=71600047, state=1)
        SetFlagState(flag=71600061, state=1)

    def test(self):
        return State_15


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        TalkToPlayer(conversation=28001010, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        SetFlagState(flag=71600048, state=1)
        SetFlagState(flag=71600061, state=1)

    def test(self):
        return State_15


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=28001700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        SetFlagState(flag=71600055, state=1)

    def test(self):
        return State_22


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=28002000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        SetFlagState(flag=71600057, state=1)

    def test(self):
        return State_13


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=28002100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71600058, state=1)

    def test(self):
        return State_13


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=28002200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71600059, state=1)
        SetFlagState(flag=11606100, state=1)

    def test(self):
        return State_13


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=28001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=71600049, state=1)

    def test(self):
        return State_13


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        SetFlagState(flag=71600031, state=1)

    def test(self):
        return State_8


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28002310, unk1=-1, unk2=-1)
        SetFlagState(flag=71600031, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        SetFlagState(flag=71600032, state=1)

    def test(self):
        return State_8


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28002320, unk1=-1, unk2=-1)
        SetFlagState(flag=71600032, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_68]

    def enter(self):
        SetFlagState(flag=71600033, state=1)

    def test(self):
        return State_8


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=28002330, unk1=-1, unk2=-1)
        SetFlagState(flag=71600033, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71600042, state=1)

    def test(self):
        return State_22


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        SetFlagState(flag=71600044, state=1)

    def test(self):
        return State_22


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        SetFlagState(flag=71600041, state=1)
        SetFlagState(flag=71600062, state=1)

    def test(self):
        return State_22


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_44, State_46]

    def enter(self):
        SetFlagState(flag=11600592, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_15
        if IsMenuOpen(63) == 0:
            return State_33


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=11600593, state=1)
        SetFlagState(flag=71600050, state=1)

    def test(self):
        return State_15


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(71600041) == 0 and GetFlagState(71600040) == 0 and GetFlagState(71600062) == 0:
            return State_41
        if GetFlagState(71600040) == 1 and GetFlagState(71600041) == 0 and GetFlagState(71600044) == 0:
            return State_25
        if GetFlagState(71600060) == 1:
            return State_47
        if GetFlagState(71600063) == 1 and GetFlagState(11406102) == 0:
            return State_37
        else:
            return State_85


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(71600040) == 0 and GetFlagState(71600041) == 0 and GetFlagState(11406102) == 0 and GetFlagState(71600062) == 0:
            return State_29
        if GetFlagState(71600060) == 1:
            return State_47
        if GetFlagState(71600040) == 0 and GetFlagState(71600041) == 1 and GetFlagState(71600042) == 0:
            return State_12
        if GetFlagState(11406102) == 0:
            return State_39
        else:
            return State_85


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DebugEvent(message='解呪する')
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)
        SetFlagState(flag=754, state=1)
        SetFlagState(flag=71600063, state=1)

    def test(self):
        return State_13


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DebugEvent(message='解呪しない')

    def test(self):
        return State_13


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020060, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_76
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_78
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_78
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_77


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010761, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性が足りない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_82
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_81
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_81


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(751) == 0:
            return State_87
        if ComparePlayerStatus(10, 0, 0) == 1:
            return State_80
        else:
            return State_79


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_79, State_80, State_87]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_31
        else:
            return State_15


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_74, State_75]

    def enter(self):
        TalkToPlayer(conversation=28000250, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_85]

    def enter(self):
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_22


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010733, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='呪われていない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_89
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_88
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_88


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_13


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15
