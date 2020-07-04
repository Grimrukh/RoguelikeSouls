from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_16


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_13, State_16]

    def enter(self):
        TalkToPlayer(conversation=43001900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3, State_69]

    def enter(self):
        SetFlagState(flag=71800024, state=1)
        SetFlagState(flag=11020598, state=1)

    def test(self):
        return State_4


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43001900, unk1=-1, unk2=-1)
        SetFlagState(flag=71800024, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_2
        if GetDistanceToPlayer() >= 16:
            return State_9


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_2, State_5, State_6, State_63, State_65, State_67, State_82]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_16


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7, State_70]

    def enter(self):
        SetFlagState(flag=71800020, state=1)

    def test(self):
        return State_4


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43001700, unk1=-1, unk2=-1)
        SetFlagState(flag=71800020, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_11, State_17, State_18, State_20, State_21, State_22, State_28, State_29, State_31, State_35, State_36, State_42, State_45, State_46, State_48, State_52, State_53, State_55, State_57, State_61, State_78, State_84, State_86, State_87, State_88, State_89]

    def enter(self):
        ClearTalkProgressData()
        ForceEndTalk(unk1=3)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_76
        if GetFlagState(1650) == 1 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_83
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(71800024) == 0 and GetSelfHP() <= 90 and GetFlagState(830) == 1:
            return State_69
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(71800024) == 0 and GetSelfHP() <= 90 and GetFlagState(830) == 0:
            return State_3
        if GetFlagState(1646) == 1:
            return State_5
        if GetFlagState(71800023) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800022) == 1 and GetFlagState(830) == 1:
            return State_73
        if GetFlagState(71800022) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800021) == 1 and GetFlagState(830) == 1:
            return State_72
        if GetFlagState(71800021) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800020) == 1 and GetFlagState(830) == 1:
            return State_71
        if GetFlagState(71800020) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(830) == 1:
            return State_70
        if GetFlagState(71800023) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800022) == 1 and GetFlagState(830) == 0:
            return State_68
        if GetFlagState(71800022) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800021) == 1 and GetFlagState(830) == 0:
            return State_66
        if GetFlagState(71800021) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800020) == 1 and GetFlagState(830) == 0:
            return State_64
        if GetFlagState(71800020) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(830) == 0:
            return State_7
        if GetFlagState(71800023) == 1:
            return State_5
        else:
            return State_5

    def exit(self):
        RemoveMyAggro()


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_1, State_3, State_7, State_12, State_17, State_18, State_20, State_21, State_22, State_28, State_29, State_31, State_36, State_42, State_45, State_46, State_48, State_52, State_53, State_55, State_57, State_61, State_64, State_66, State_68, State_69, State_70, State_71, State_72, State_73, State_74, State_75, State_78, State_83, State_84, State_86, State_87, State_88, State_89]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if GetFlagState(71800024) == 1:
            return State_112
        else:
            return State_10


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_16


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_8


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        TalkToPlayer(conversation=43001900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_3, State_7, State_64, State_66, State_68, State_69, State_70, State_71, State_72, State_73, State_83]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(830) == 1:
            return State_74
        if CheckSelfDeath() == 1 and GetFlagState(830) == 0:
            return State_1

    def exit(self):
        RemoveMyAggro()


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_16


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_16


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_0, State_1, State_4, State_10, State_12, State_14, State_15, State_21, State_23, State_24, State_30, State_32, State_34, State_37, State_40, State_42, State_43, State_47, State_49, State_50, State_54, State_56, State_58, State_60, State_62, State_74, State_75, State_81, State_85, State_89, State_112]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1647) == 0 and GetFlagState(830) == 1 and GetDistanceToPlayer() <= 15:
            return State_74
        if CheckSelfDeath() == 1 and GetFlagState(1647) == 0 and GetFlagState(830) == 0 and GetDistanceToPlayer() <= 15:
            return State_1
        if GetFlagState(71800038) == 0 and GetFlagState(1649) == 1 and GetDistanceToPlayer() <= 10 and GetFlagState(830) == 0 and GetFlagState(831) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetFlagState(1647) == 0:
            return State_84
        if GetFlagState(71800034) == 0 and GetFlagState(830) == 1 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetFlagState(822) == 1 and GetFlagState(11800100) == 0 and GetFlagState(1647) == 0:
            return State_61
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800033) == 0 and GetFlagState(71800039) == 1 and GetFlagState(1643) == 1:
            return State_31
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800026) == 1 and GetFlagState(71800029) == 0 and GetFlagState(11500200) == 1:
            return State_78
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800026) == 1 and GetFlagState(71800028) == 0:
            return State_28
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800027) == 1 and GetFlagState(71800026) == 0:
            return State_22
        if GetFlagState(71800025) == 0 and GetFlagState(1641) == 1 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10:
            return State_57
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800037) == 0 and GetFlagState(1645) == 1 and GetFlagState(830) == 1:
            return State_55
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800035) == 0 and GetFlagState(1644) == 1 and GetFlagState(830) == 1:
            return State_53
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(1643) == 1 and GetFlagState(71800033) == 1 and GetFlagState(830) == 1:
            return State_21
        if GetFlagState(71800030) == 0 and GetFlagState(1650) == 1 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10:
            return State_20
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800026) == 1 and GetFlagState(830) == 1:
            return State_86
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800026) == 1 and GetFlagState(830) == 0:
            return State_17
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800033) == 0 and GetFlagState(71800039) == 0 and GetFlagState(1643) == 1:
            return State_52
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetOneLineHelpStatus() == 1 and GetFlagState(71800026) == 0 and GetFlagState(1642) == 1 and GetFlagState(71800027) == 0:
            return State_18
        if GetOneLineHelpStatus() == 1 and GetPlayerYDistance() > 2:
            return State_14
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3.5):
            return State_14
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.5 and GetFlagState(1646) == 0 and GetFlagState(1647) == 0 and GetFlagState(1648) == 0 and GetFlagState(1650) == 0 and GetFlagState(1641) == 0:
            return State_15
        if IsAttackedBySomeone() == 1 and GetFlagState(1647) == 0:
            return State_11


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        SetFlagState(flag=71800039, state=1)

    def test(self):
        return State_27


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000400, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_81
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_16


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_27, State_90, State_91, State_93, State_94, State_95, State_96, State_97, State_98, State_99, State_100, State_101, State_102, State_103, State_104, State_105, State_106, State_107, State_108, State_109, State_110]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_16


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='話を聞く')
        SetFlagState(flag=71800026, state=1)

    def test(self):
        if GetFlagState(11500200) == 1:
            return State_78
        else:
            return State_28


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='話を聞かない')
        SetFlagState(flag=71800027, state=1)

    def test(self):
        return State_29


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_19, State_22]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_26
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_26
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_25


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_16, State_25]

    def enter(self):
        TalkToPlayer(conversation=43000250, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=43000140, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_27, State_90, State_91, State_93, State_94, State_95, State_96, State_97, State_98, State_99, State_100, State_101, State_102, State_103, State_104, State_105, State_106, State_107, State_108, State_109, State_110]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_76
        else:
            return State_16


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        SetFlagState(flag=71800028, state=1)
        SetFlagState(flag=71800029, state=1)

    def test(self):
        return State_16


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_37, State_40, State_80, State_92]

    def enter(self):
        AddTalkListData(menu_index=5, menu_text=15000141, required_flag=-1)
        AddTalkListData(menu_index=1, menu_text=15000150, required_flag=822)
        AddTalkListData(menu_index=6, menu_text=15000300, required_flag=781)
        AddTalkListData(menu_index=7, menu_text=15000301, required_flag=782)
        AddTalkListData(menu_index=8, menu_text=15000302, required_flag=783)
        AddTalkListData(menu_index=9, menu_text=15000303, required_flag=784)
        AddTalkListData(menu_index=10, menu_text=15000304, required_flag=785)
        AddTalkListData(menu_index=11, menu_text=15000305, required_flag=786)
        AddTalkListData(menu_index=12, menu_text=15000306, required_flag=787)
        AddTalkListData(menu_index=13, menu_text=15000307, required_flag=788)
        AddTalkListData(menu_index=14, menu_text=15000308, required_flag=789)
        AddTalkListData(menu_index=15, menu_text=15000309, required_flag=790)
        AddTalkListData(menu_index=2, menu_text=15000000, required_flag=71800035)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=1642)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_39
        if GetTalkListEntryResult() == 0:
            return State_41
        if GetTalkListEntryResult() == 4:
            return State_41
        if GetTalkListEntryResult() == 1:
            return State_59
        if GetTalkListEntryResult() == 3:
            return State_44
        if GetTalkListEntryResult() == 2:
            return State_111
        if GetTalkListEntryResult() == 5:
            return State_79
        if GetTalkListEntryResult() == 6:
            return State_90
        if GetTalkListEntryResult() == 7:
            return State_93
        if GetTalkListEntryResult() == 8:
            return State_95
        if GetTalkListEntryResult() == 9:
            return State_97
        if GetTalkListEntryResult() == 10:
            return State_99
        if GetTalkListEntryResult() == 11:
            return State_101
        if GetTalkListEntryResult() == 12:
            return State_103
        if GetTalkListEntryResult() == 13:
            return State_105
        if GetTalkListEntryResult() == 14:
            return State_107
        if GetTalkListEntryResult() == 15:
            return State_109

    def exit(self):
        ClearTalkListData()


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_35, State_38, State_39]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_16


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_38, State_39]

    def enter(self):
        TalkToPlayer(conversation=43000950, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if GetDistanceToPlayer() >= 20:
            return State_34
        if HasTalkEnded() == 1:
            return State_43


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=43000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36, State_45, State_87, State_88]

    def test(self):
        return State_33
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_16


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_76
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_35
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_34


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_76
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_35
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_34


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_17, State_86]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_33
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_16


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_33]

    def test(self):
        if GetFlagState(830) == 0:
            return State_42
        if GetFlagState(830) == 1:
            return State_89
        else:
            return State_50


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        TalkToPlayer(conversation=43000950, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_35]

    def test(self):
        return State_16


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_33]

    def test(self):
        if GetFlagState(1642) == 1 and GetFlagState(830) == 0:
            return State_36
        if GetFlagState(1642) == 1 and GetFlagState(830) == 1:
            return State_87


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_111]

    def enter(self):
        TalkToPlayer(conversation=43001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=43001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=824, state=1)

    def test(self):
        return State_16


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=43001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48, State_51, State_77]

    def enter(self):
        SetFlagState(flag=820, state=1)

    def test(self):
        return State_16


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_16


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71800033, state=1)
        SetFlagState(flag=71800026, state=1)
        SetFlagState(flag=71800027, state=1)
        SetFlagState(flag=71800028, state=1)
        SetFlagState(flag=71800029, state=1)

    def test(self):
        return State_49


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        SetFlagState(flag=71800035, state=1)
        SetFlagState(flag=824, state=1)

    def test(self):
        return State_16


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        SetFlagState(flag=71800037, state=1)

    def test(self):
        return State_16


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000000, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_58
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71800025, state=1)

    def test(self):
        return State_16


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_33]

    def test(self):
        if GetFlagState(830) == 1:
            return State_46
        if GetFlagState(830) == 0:
            return State_48


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        SetFlagState(flag=71800029, state=1)
        SetFlagState(flag=71800028, state=1)

    def test(self):
        return State_16


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001010, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_62
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=71800034, state=1)

    def test(self):
        return State_16


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_64, State_71]

    def enter(self):
        SetFlagState(flag=71800021, state=1)

    def test(self):
        return State_4


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43001710, unk1=-1, unk2=-1)
        SetFlagState(flag=71800021, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_66, State_72]

    def enter(self):
        SetFlagState(flag=71800022, state=1)

    def test(self):
        return State_4


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43001720, unk1=-1, unk2=-1)
        SetFlagState(flag=71800022, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_68, State_73]

    def enter(self):
        SetFlagState(flag=71800023, state=1)

    def test(self):
        return State_4


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43001730, unk1=-1, unk2=-1)
        SetFlagState(flag=71800023, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43011900, unk1=-1, unk2=-1)
        SetFlagState(flag=71800024, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_2
        if GetDistanceToPlayer() >= 16:
            return State_9


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43011700, unk1=-1, unk2=-1)
        SetFlagState(flag=71800020, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43011710, unk1=-1, unk2=-1)
        SetFlagState(flag=71800021, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43011720, unk1=-1, unk2=-1)
        SetFlagState(flag=71800022, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43011730, unk1=-1, unk2=-1)
        SetFlagState(flag=71800023, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_13, State_16]

    def enter(self):
        TalkToPlayer(conversation=43011900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        TalkToPlayer(conversation=43011900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_8, State_30, State_38, State_39]

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(830) == 1 and GetDistanceToPlayer() <= 15:
            return State_75
        if CheckSelfDeath() == 1 and GetFlagState(830) == 0 and GetDistanceToPlayer() <= 15:
            return State_12


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=71800033, state=1)
        SetFlagState(flag=71800039, state=1)
        SetFlagState(flag=71800026, state=1)
        SetFlagState(flag=71800027, state=1)
        SetFlagState(flag=71800028, state=1)
        SetFlagState(flag=71800029, state=1)

    def test(self):
        return State_49


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_16, State_25]

    def enter(self):
        TalkToPlayer(conversation=43000250, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_33]

    def test(self):
        return State_80


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DebugEvent(message='売却ショップ')
        OpenSellShop(-1, -1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_38
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_38
        if IsMenuOpen(64) == 0:
            return State_33


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=71800030, state=1)

    def test(self):
        return State_16


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_83]

    def test(self):
        return State_4


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        TalkToPlayer(conversation=43000500, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_13
        if HasTalkEnded() == 1:
            return State_82
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_9


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43001900, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_85
        if GetDistanceToPlayer() >= 15:
            return State_9


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        SetFlagState(flag=71800038, state=1)
        SetFlagState(flag=11020598, state=1)

    def test(self):
        return State_16


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=43000350, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=43000850, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_111]

    def enter(self):
        TalkToPlayer(conversation=43001350, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        TalkToPlayer(conversation=43000950, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020250, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_91


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_90]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1010, -1)
        PlayerEquipmentQuantityChange(3, 1000, 5)
        OpenGenericDialog(unk1=7, text_id=10010900, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_90, State_91, State_93, State_94, State_95, State_96, State_97, State_98, State_99, State_100, State_101, State_102, State_103, State_104, State_105, State_106, State_107, State_108, State_109, State_110]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ForceCloseGenericDialog()

    def test(self):
        return State_33


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020251, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_94


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_93]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1020, -1)
        PlayerEquipmentQuantityChange(3, 1000, 5)
        OpenGenericDialog(unk1=7, text_id=10010901, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020252, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_96


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_95]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1030, -1)
        PlayerEquipmentQuantityChange(3, 1010, 3)
        OpenGenericDialog(unk1=7, text_id=10010902, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020253, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_98


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1040, -1)
        PlayerEquipmentQuantityChange(3, 1020, 3)
        OpenGenericDialog(unk1=7, text_id=10010903, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020254, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_100


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_99]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1050, -1)
        PlayerEquipmentQuantityChange(3, 1020, 3)
        OpenGenericDialog(unk1=7, text_id=10010904, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020255, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_102


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_101]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1060, -1)
        PlayerEquipmentQuantityChange(3, 1020, 3)
        OpenGenericDialog(unk1=7, text_id=10010905, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_103(State):
    """ 103: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020256, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_104


class State_104(State):
    """ 104: No description. """

    def previous_states(self):
        return [State_103]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1070, -1)
        PlayerEquipmentQuantityChange(3, 1030, 2)
        OpenGenericDialog(unk1=7, text_id=10010906, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_105(State):
    """ 105: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020257, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_106


class State_106(State):
    """ 106: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1080, -1)
        PlayerEquipmentQuantityChange(3, 1040, 2)
        OpenGenericDialog(unk1=7, text_id=10010907, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_107(State):
    """ 107: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020258, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_108


class State_108(State):
    """ 108: No description. """

    def previous_states(self):
        return [State_107]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1090, -1)
        PlayerEquipmentQuantityChange(3, 1050, 2)
        OpenGenericDialog(unk1=7, text_id=10010908, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_109(State):
    """ 109: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020259, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_110


class State_110(State):
    """ 110: No description. """

    def previous_states(self):
        return [State_109]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 1100, -1)
        PlayerEquipmentQuantityChange(3, 1060, 2)
        OpenGenericDialog(unk1=7, text_id=10010909, unk2=1, unk3=0, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_24
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_92
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_92


class State_111(State):
    """ 111: No description. """

    def previous_states(self):
        return [State_33]

    def test(self):
        if GetFlagState(1642) == 0 and GetFlagState(830) == 0:
            return State_45
        if GetFlagState(1642) == 0 and GetFlagState(830) == 1:
            return State_88


class State_112(State):
    """ 112: No description. """

    def previous_states(self):
        return [State_9]

    def enter(self):
        SetFlagState(flag=11020598, state=1)
        ForceEndTalk(unk1=0)

    def test(self):
        return State_16
