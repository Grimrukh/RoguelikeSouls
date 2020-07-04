from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_28


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_55


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=4)
        SetFlagState(flag=71600021, state=1)
        SetFlagState(flag=845, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_9
        if GetFlagState(11600594) == 0 and GetFlagState(845) == 0:
            return State_119
        if GetFlagState(845) == 0:
            return State_127


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        DebugEvent(message='誓約を変更しない')

    def test(self):
        return State_1


class State_5(State):
    """ 5: No description. """

    def enter(self):
        TalkToPlayer(conversation=-1, unk1=-1, unk2=-1)
        DebugEvent(message='誓約結ぶ前会話')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=4)
        RequestUnlockTrophy(12)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 0:
            return State_3
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 1:
            return State_128


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_8
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_8


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7, State_127]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_55


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_3, State_7, State_127, State_128]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_10(State):
    """ 10: No description. """

    def enter(self):
        TalkToPlayer(conversation=-1, unk1=-1, unk2=-1)
        DebugEvent(message='誓約したあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_11(State):
    """ 11: No description. """

    def enter(self):
        TalkToPlayer(conversation=-1, unk1=-1, unk2=-1)
        DebugEvent(message='誓約しなかったあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_24, State_28]

    def enter(self):
        TalkToPlayer(conversation=44002200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_28
        if GetDistanceToPlayer() >= 15:
            return State_20


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_14, State_90]

    def enter(self):
        SetFlagState(flag=71600004, state=1)
        SetFlagState(flag=11600590, state=1)

    def test(self):
        return State_15


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002200, unk1=-1, unk2=-1)
        SetFlagState(flag=71600004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_13
        if GetDistanceToPlayer() >= 16:
            return State_20


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_13, State_16, State_17, State_84, State_86, State_88]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_28


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_15


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_18, State_91]

    def enter(self):
        SetFlagState(flag=71600000, state=1)

    def test(self):
        return State_15


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002000, unk1=-1, unk2=-1)
        SetFlagState(flag=71600000, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_5, State_10, State_11, State_22, State_29, State_31, State_33, State_34, State_35, State_41, State_42, State_46, State_47, State_49, State_54, State_60, State_64, State_65, State_67, State_71, State_72, State_74, State_76, State_79, State_82, State_99, State_101, State_103, State_105, State_106, State_107, State_108, State_109]

    def enter(self):
        ClearTalkProgressData()
        ForceEndTalk(unk1=3)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_97
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(71600004) == 0 and GetSelfHP() <= 90 and GetFlagState(831) == 1:
            return State_90
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(71600004) == 0 and GetSelfHP() <= 90 and GetFlagState(831) == 0:
            return State_14
        if GetFlagState(1675) == 1:
            return State_16
        if GetFlagState(71600003) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600002) == 1 and GetFlagState(831) == 1:
            return State_94
        if GetFlagState(71600002) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600001) == 1 and GetFlagState(831) == 1:
            return State_93
        if GetFlagState(71600001) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600000) == 1 and GetFlagState(831) == 1:
            return State_92
        if GetFlagState(71600000) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(831) == 1:
            return State_91
        if GetFlagState(71600003) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600002) == 1 and GetFlagState(831) == 0:
            return State_89
        if GetFlagState(71600002) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600001) == 1 and GetFlagState(831) == 0:
            return State_87
        if GetFlagState(71600001) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71600000) == 1 and GetFlagState(831) == 0:
            return State_85
        if GetFlagState(71600000) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(831) == 0:
            return State_18
        if GetFlagState(71600003) == 1:
            return State_16
        else:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_5, State_10, State_11, State_12, State_14, State_18, State_23, State_29, State_31, State_33, State_34, State_35, State_41, State_42, State_46, State_47, State_49, State_54, State_60, State_64, State_65, State_67, State_71, State_72, State_74, State_76, State_79, State_82, State_85, State_87, State_89, State_90, State_91, State_92, State_93, State_94, State_95, State_96, State_99, State_101, State_103, State_105, State_106, State_107, State_108, State_109]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if GetFlagState(71600004) == 1:
            return State_132
        else:
            return State_21


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_28


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_19


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        TalkToPlayer(conversation=44002200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_28
        if GetDistanceToPlayer() >= 15:
            return State_20


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_14, State_18, State_85, State_87, State_89, State_90, State_91, State_92, State_93, State_94]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(831) == 1:
            return State_95
        if CheckSelfDeath() == 1 and GetFlagState(831) == 0:
            return State_12

    def exit(self):
        RemoveMyAggro()


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_6, State_7, State_113, State_114, State_115, State_121, State_127, State_129, State_130]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_97
        else:
            return State_28


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_28


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_28


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_0, State_2, State_9, State_12, State_15, State_21, State_23, State_25, State_26, State_27, State_34, State_36, State_37, State_43, State_52, State_55, State_56, State_58, State_60, State_61, State_66, State_68, State_69, State_73, State_75, State_77, State_80, State_83, State_95, State_96, State_100, State_102, State_104, State_109, State_110, State_117, State_119, State_120, State_123, State_124, State_132]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1676) == 0 and GetFlagState(831) == 1 and GetDistanceToPlayer() <= 15:
            return State_95
        if CheckSelfDeath() == 1 and GetFlagState(1676) == 0 and GetFlagState(831) == 0 and GetDistanceToPlayer() <= 15:
            return State_12
        if GetFlagState(71600023) == 0 and GetFlagState(1678) == 1 and GetDistanceToPlayer() <= 10 and GetFlagState(71800035) == 1 and GetFlagState(831) == 0 and GetFlagState(830) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetFlagState(1675) == 0 and GetFlagState(1676) == 0 and GetFlagState(1677) == 0:
            return State_103
        if GetFlagState(71600022) == 0 and GetFlagState(1678) == 1 and GetDistanceToPlayer() <= 10 and GetFlagState(71800035) == 0 and GetFlagState(831) == 0 and GetFlagState(830) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetFlagState(1675) == 0 and GetFlagState(1676) == 0 and GetFlagState(1677) == 0:
            return State_101
        if GetFlagState(71600017) == 0 and GetFlagState(823) == 1 and GetDistanceToPlayer() <= 10 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 10 and GetFlagState(831) == 1 and GetFlagState(1675) == 0 and GetFlagState(1676) == 0 and GetFlagState(1677) == 0:
            return State_82
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600011) == 0 and GetFlagState(71600005) == 1 and GetFlagState(1672) == 1 and GetFlagState(71600010) == 0:
            return State_47
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600011) == 1 and GetFlagState(71600013) == 0:
            return State_49
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600010) == 1 and GetFlagState(71600012) == 0:
            return State_46
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600006) == 1 and GetFlagState(71600008) == 0 and GetFlagState(11500200) == 1:
            return State_99
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600007) == 1 and GetFlagState(71600006) == 0:
            return State_35
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600016) == 0 and GetFlagState(15) == 1:
            return State_76
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600015) == 0 and GetFlagState(1674) == 1 and GetFlagState(831) == 1:
            return State_74
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600014) == 0 and GetFlagState(1673) == 1 and GetFlagState(831) == 1:
            return State_72
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(1672) == 1 and GetFlagState(71600009) == 1 and GetFlagState(831) == 1:
            return State_34
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600020) == 1 and GetFlagState(831) == 1:
            return State_106
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600020) == 1 and GetFlagState(831) == 0:
            return State_33
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600020) == 0 and GetFlagState(71600006) == 1 and GetFlagState(831) == 1:
            return State_105
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600010) == 0 and GetFlagState(71600005) == 0 and GetFlagState(1672) == 1 and GetFlagState(71600011) == 0:
            return State_71
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600020) == 0 and GetFlagState(71600006) == 1 and GetFlagState(831) == 0:
            return State_29
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71600007) == 0 and GetFlagState(1671) == 1 and GetFlagState(71600006) == 0:
            return State_31
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 5):
            return State_26
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetFlagState(1675) == 0 and GetFlagState(1676) == 0 and GetFlagState(1677) == 0:
            return State_27
        if IsAttackedBySomeone() == 1 and GetFlagState(1676) == 0:
            return State_22


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_29, State_105]

    def enter(self):
        SetFlagState(flag=71600020, state=1)

    def test(self):
        return State_58


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        SetFlagState(flag=71600005, state=1)

    def test(self):
        return State_40


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_42, State_81]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_28


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_40, State_45]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        DebugEvent(message='話を聞く')
        SetFlagState(flag=71600006, state=1)

    def test(self):
        return State_99


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        DebugEvent(message='話を聞かない')
        SetFlagState(flag=71600007, state=1)

    def test(self):
        return State_42


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_32, State_35]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_37
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_39
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_38


class State_41(State):
    """ 41: No description. """

    def enter(self):
        TalkToPlayer(conversation=44000200, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        TalkToPlayer(conversation=44000400, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_40, State_45]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_97
        else:
            return State_28


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        DebugEvent(message='話を聞く')
        SetFlagState(flag=71600010, state=1)

    def test(self):
        return State_46


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_70, State_98]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_37
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_48
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_48
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_44


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_28, State_44]

    def enter(self):
        TalkToPlayer(conversation=44001000, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_100
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_70
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        DebugEvent(message='願いを聞かない')
        SetFlagState(flag=71600011, state=1)

    def test(self):
        return State_49


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_28, State_48]

    def enter(self):
        TalkToPlayer(conversation=44001300, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_81
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        if ComparePlayerStatus(11, 0, 4) == 1:
            return State_7
        else:
            return State_6


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_55, State_58, State_125]

    def enter(self):
        AddTalkListData(menu_index=6, menu_text=15000251, required_flag=854)
        AddTalkListData(menu_index=5, menu_text=15000261, required_flag=854)
        AddTalkListData(menu_index=2, menu_text=15000200, required_flag=71600020)
        AddTalkListData(menu_index=1, menu_text=15000150, required_flag=71600012)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_57
        if GetTalkListEntryResult() == 0:
            return State_59
        if GetTalkListEntryResult() == 4:
            return State_59
        if GetTalkListEntryResult() == 2:
            return State_50
        if GetTalkListEntryResult() == 1:
            return State_78
        if GetTalkListEntryResult() == 3:
            return State_63
        if GetTalkListEntryResult() == 5:
            return State_118
        if GetTalkListEntryResult() == 6:
            return State_126

    def exit(self):
        ClearTalkListData()


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_53, State_56, State_57]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_28


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_56, State_57]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_52
        if HasTalkEnded() == 1:
            return State_61


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        TalkToPlayer(conversation=44001800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_1, State_8, State_62, State_64, State_108, State_112, State_116, State_122]

    def test(self):
        return State_51
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_28


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_125]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_97
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_53
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_52
        else:
            return State_28


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_97
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_53
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_52


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_30, State_33, State_106]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_51
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 15:
        #     return State_28


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        if GetFlagState(831) == 0:
            return State_60
        if GetFlagState(831) == 1:
            return State_109
        else:
            return State_69


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=44000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_53]

    def test(self):
        return State_28


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_54, State_107]

    def enter(self):
        SetFlagState(flag=71600018, state=1)

    def test(self):
        return State_55


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        if GetFlagState(71600018) == 1 and GetFlagState(71600012) == 1 and GetFlagState(831) == 1:
            return State_108
        if GetFlagState(71600018) == 1 and GetFlagState(71600012) == 1 and GetFlagState(831) == 0:
            return State_64
        if GetFlagState(831) == 1:
            return State_107
        if GetFlagState(831) == 0:
            return State_54


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        TalkToPlayer(conversation=44001900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        TalkToPlayer(conversation=44001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        SetFlagState(flag=825, state=1)

    def test(self):
        return State_28


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        TalkToPlayer(conversation=44001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_68
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        SetFlagState(flag=821, state=1)

    def test(self):
        return State_28


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_28


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        SetFlagState(flag=71600009, state=1)

    def test(self):
        return State_45


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000010, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_98
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        SetFlagState(flag=71600014, state=1)
        SetFlagState(flag=825, state=1)

    def test(self):
        return State_28


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        SetFlagState(flag=71600015, state=1)

    def test(self):
        return State_28


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        SetFlagState(flag=71600016, state=1)

    def test(self):
        return State_28


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        if GetFlagState(831) == 1:
            return State_65
        if GetFlagState(831) == 0:
            return State_67


class State_79(State):
    """ 79: No description. """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000110, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 20:
            return State_20


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_99]

    def enter(self):
        SetFlagState(flag=71600008, state=1)

    def test(self):
        return State_28


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=11600590, state=1)
        SetFlagState(flag=71600013, state=1)

    def test(self):
        return State_36


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001010, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_83
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 20:
            return State_20


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_82]

    def enter(self):
        SetFlagState(flag=71600017, state=1)

    def test(self):
        return State_28


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_85, State_92]

    def enter(self):
        SetFlagState(flag=71600001, state=1)

    def test(self):
        return State_15


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002010, unk1=-1, unk2=-1)
        SetFlagState(flag=71600001, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_87, State_93]

    def enter(self):
        SetFlagState(flag=71600002, state=1)

    def test(self):
        return State_15


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002020, unk1=-1, unk2=-1)
        SetFlagState(flag=71600002, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_89, State_94]

    def enter(self):
        SetFlagState(flag=71600003, state=1)

    def test(self):
        return State_15


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002100, unk1=-1, unk2=-1)
        SetFlagState(flag=71600003, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002500, unk1=-1, unk2=-1)
        SetFlagState(flag=71600004, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_13
        if GetDistanceToPlayer() >= 16:
            return State_20


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002300, unk1=-1, unk2=-1)
        SetFlagState(flag=71600000, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_17
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002310, unk1=-1, unk2=-1)
        SetFlagState(flag=71600001, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002320, unk1=-1, unk2=-1)
        SetFlagState(flag=71600002, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=44002400, unk1=-1, unk2=-1)
        SetFlagState(flag=71600003, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_24, State_28]

    def enter(self):
        TalkToPlayer(conversation=44002500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_28
        if GetDistanceToPlayer() >= 15:
            return State_20


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        TalkToPlayer(conversation=44002500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_28
        if GetDistanceToPlayer() >= 15:
            return State_20


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_19, State_25, State_43, State_56, State_57]

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(831) == 1 and GetDistanceToPlayer() <= 15:
            return State_96
        if CheckSelfDeath() == 1 and GetFlagState(831) == 0 and GetDistanceToPlayer() <= 15:
            return State_23


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        SetFlagState(flag=71600009, state=1)
        SetFlagState(flag=71600006, state=1)
        SetFlagState(flag=71600007, state=1)
        SetFlagState(flag=71600008, state=1)
        SetFlagState(flag=71600024, state=1)

    def test(self):
        return State_45


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_28, State_38]

    def enter(self):
        TalkToPlayer(conversation=44000200, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_80
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=821, state=1)
        SetFlagState(flag=71600012, state=1)

    def test(self):
        return State_28


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44002200, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_102
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 20:
            return State_20


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_101]

    def enter(self):
        SetFlagState(flag=71600022, state=1)
        SetFlagState(flag=11600590, state=1)

    def test(self):
        return State_28


class State_103(State):
    """ 103: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44001300, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_104
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 20:
            return State_20


class State_104(State):
    """ 104: No description. """

    def previous_states(self):
        return [State_103]

    def enter(self):
        SetFlagState(flag=71600023, state=1)
        SetFlagState(flag=11600590, state=1)

    def test(self):
        return State_28


class State_105(State):
    """ 105: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000550, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_106(State):
    """ 106: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=44000650, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_107(State):
    """ 107: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        TalkToPlayer(conversation=44001850, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_108(State):
    """ 108: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        TalkToPlayer(conversation=44001950, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_109(State):
    """ 109: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=44000850, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_20


class State_110(State):
    """ 110: No description. """

    def previous_states(self):
        return [State_111, State_113, State_114, State_131]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_111(State):
    """ 111: No description. """

    def previous_states(self):
        return [State_114]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        DebugEvent(message='捧げる')
        ChangePlayerStats(unk1=15, unk2=0, unk3=1)
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)
        SetFlagState(flag=845, state=1)

    def test(self):
        if DoesSelfHaveSpEffect(18, 10) == 1 and GetFlagState(11600595) == 0 and GetFlagState(845) == 0:
            return State_120
        if DoesSelfHaveSpEffect(18, 30) == 1 and GetFlagState(845) == 0 and (GetFlagState(11600596) == 0 or GetFlagState(11600580) == 0 or GetFlagState(11600581) == 0 or GetFlagState(11600582) == 0 or GetFlagState(11600583) == 0):
            return State_124
        if DoesSelfHaveSpEffect(18, 80) == 1 and GetFlagState(845) == 0:
            return State_130
        if DoesSelfHaveSpEffect(18, 30) == 1 and GetFlagState(845) == 0:
            return State_130
        if DoesSelfHaveSpEffect(18, 10) == 1 and GetFlagState(845) == 0:
            return State_130
        if GetFlagState(845) == 0:
            return State_129
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_110


class State_112(State):
    """ 112: No description. """

    def previous_states(self):
        return [State_113, State_114]

    def enter(self):
        DebugEvent(message='捧げない')

    def test(self):
        return State_55


class State_113(State):
    """ 113: No description. """

    def previous_states(self):
        return [State_118]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020201, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_110
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_112
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_112
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 0:
            return State_114
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 1:
            return State_114
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_25


class State_114(State):
    """ 114: No description. """

    def previous_states(self):
        return [State_113]

    def enter(self):
        DebugEvent(message='DECIDE_NUMBER')
        OpenGenericDialog(unk1=3, text_id=10020201, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_110
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_112
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_112
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 0:
            return State_111
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0 and GetFlagState(831) == 1:
            return State_131
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_25


class State_115(State):
    """ 115: No description. """

    def previous_states(self):
        return [State_118]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010781, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_117
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_116
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_116


class State_116(State):
    """ 116: No description. """

    def previous_states(self):
        return [State_115, State_129, State_130]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_55


class State_117(State):
    """ 117: No description. """

    def previous_states(self):
        return [State_115, State_129, State_130]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_118(State):
    """ 118: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        if ComparePlayerStatus(18, 0, 100) == 1:
            return State_121
        if ComparePlayerStatus(10, 0, 0) == 1:
            return State_115
        else:
            return State_113


class State_119(State):
    """ 119: No description. """

    def previous_states(self):
        return [State_3, State_128]

    def enter(self):
        SetFlagState(flag=11600594, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_28
        if IsMenuOpen(63) == 0:
            return State_127


class State_120(State):
    """ 120: No description. """

    def previous_states(self):
        return [State_111, State_131]

    def enter(self):
        SetFlagState(flag=11600595, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_28
        if IsMenuOpen(63) == 0 and DoesSelfHaveSpEffect(18, 30) == 1 and GetFlagState(846) == 0 and (GetFlagState(11600596) == 0 or GetFlagState(11600580) == 0 or GetFlagState(11600581) == 0 or GetFlagState(11600582) == 0 or GetFlagState(11600583) == 0):
            return State_124
        if IsMenuOpen(63) == 0:
            return State_130


class State_121(State):
    """ 121: No description. """

    def previous_states(self):
        return [State_118]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010791, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='MAX')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_123
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_122
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_122


class State_122(State):
    """ 122: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_55


class State_123(State):
    """ 123: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_28


class State_124(State):
    """ 124: No description. """

    def previous_states(self):
        return [State_111, State_120, State_131]

    def enter(self):
        SetFlagState(flag=11600596, state=1)
        SetFlagState(flag=11600580, state=1)
        SetFlagState(flag=11600581, state=1)
        SetFlagState(flag=11600582, state=1)
        SetFlagState(flag=11600583, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_28
        if IsMenuOpen(63) == 0:
            return State_130


class State_125(State):
    """ 125: No description. """

    def previous_states(self):
        return [State_126]

    def enter(self):
        OpenRegularShop(6100, 6199)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_56
        if IsMenuOpen(11) == 0:
            return State_51


class State_126(State):
    """ 126: No description. """

    def previous_states(self):
        return [State_51]

    def test(self):
        return State_125


class State_127(State):
    """ 127: No description. """

    def previous_states(self):
        return [State_3, State_119, State_128]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わした')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_8
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_8


class State_128(State):
    """ 128: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=4)
        SetFlagState(flag=71600021, state=1)
        SetFlagState(flag=846, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12 or IsAttackedBySomeone() == 1:
            return State_9
        if GetFlagState(11600594) == 0 and GetFlagState(846) == 0:
            return State_119
        if GetFlagState(846) == 0:
            return State_127


class State_129(State):
    """ 129: No description. """

    def previous_states(self):
        return [State_111, State_131]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010796, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ポイントアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_117
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_116
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_116


class State_130(State):
    """ 130: No description. """

    def previous_states(self):
        return [State_111, State_120, State_124, State_131]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010797, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ランクアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_117
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_116
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_116


class State_131(State):
    """ 131: No description. """

    def previous_states(self):
        return [State_114]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        DebugEvent(message='捧げる')
        ChangePlayerStats(unk1=15, unk2=0, unk3=1)
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)
        SetFlagState(flag=846, state=1)

    def test(self):
        if DoesSelfHaveSpEffect(18, 10) == 1 and GetFlagState(11600595) == 0 and GetFlagState(846) == 0:
            return State_120
        if DoesSelfHaveSpEffect(18, 30) == 1 and GetFlagState(846) == 0 and (GetFlagState(11600596) == 0 or GetFlagState(11600580) == 0 or GetFlagState(11600581) == 0 or GetFlagState(11600582) == 0 or GetFlagState(11600583) == 0):
            return State_124
        if DoesSelfHaveSpEffect(18, 80) == 1 and GetFlagState(846) == 0:
            return State_130
        if DoesSelfHaveSpEffect(18, 30) == 1 and GetFlagState(846) == 0:
            return State_130
        if DoesSelfHaveSpEffect(18, 10) == 1 and GetFlagState(846) == 0:
            return State_130
        if GetFlagState(846) == 0:
            return State_129
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 12:
            return State_110


class State_132(State):
    """ 132: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=11600590, state=1)
        ForceEndTalk(unk1=0)

    def test(self):
        return State_28
