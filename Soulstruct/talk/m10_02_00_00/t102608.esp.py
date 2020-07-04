from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_135


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
        return [State_8, State_12, State_14, State_23, State_32, State_34, State_36, State_39, State_45, State_46, State_58, State_60, State_62, State_64, State_66, State_68, State_70, State_72, State_74, State_75, State_76, State_77, State_83, State_85, State_86, State_87, State_88, State_90, State_91, State_98, State_99, State_101, State_103, State_105, State_107, State_109, State_111, State_113, State_115, State_117, State_119, State_121, State_123, State_125, State_127]

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
        return [State_2, State_4, State_5, State_11, State_21, State_24, State_25, State_27, State_28, State_29, State_36, State_39, State_40, State_41, State_47, State_48, State_49, State_54, State_55, State_57, State_74, State_75, State_76, State_77, State_82, State_92, State_94, State_100, State_102, State_104, State_106, State_108, State_110, State_112, State_114, State_116, State_129, State_132, State_135]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1196) == 0 and GetFlagState(1198) == 0 and GetDistanceToPlayer() <= 5:
            return State_16
        if GetFlagState(1195) == 1 and IsPlayerDead() == 1 and GetFlagState(71300093) == 0 and GetDistanceToPlayer() <= 5 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_129
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1202) == 1:
            return State_78
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1195) == 0 and GetFlagState(1196) == 0 and GetFlagState(1197) == 0 and GetFlagState(1198) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1198) == 0 and GetFlagState(1196) == 0:
            return State_1
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1193) == 1:
            return State_79
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1191) == 1:
            return State_80
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1194) == 1:
            return State_81


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_23, State_32, State_34, State_36, State_39, State_45, State_46, State_83, State_85, State_86, State_87, State_88, State_90, State_91, State_98, State_99, State_101, State_103, State_105, State_107, State_109, State_111, State_113, State_115, State_117, State_119, State_121, State_123, State_125, State_127]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71300064) == 0 and GetSelfHP() <= 90 and GetFlagState(1194) == 1:
            return State_64
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71300059) == 0 and GetSelfHP() <= 90 and GetFlagState(1194) == 0:
            return State_12
        if GetFlagState(1195) == 1:
            return State_10
        if GetFlagState(1197) == 1:
            return State_10
        if GetFlagState(71300063) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 1 and GetFlagState(71300062) == 1:
            return State_72
        if GetFlagState(71300062) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 1 and GetFlagState(71300061) == 1:
            return State_70
        if GetFlagState(71300061) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 1 and GetFlagState(71300060) == 1:
            return State_68
        if GetFlagState(71300060) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 1:
            return State_66
        if GetFlagState(71300058) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 0 and GetFlagState(71300057) == 1:
            return State_62
        if GetFlagState(71300057) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 0 and GetFlagState(71300056) == 1:
            return State_60
        if GetFlagState(71300056) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 0 and GetFlagState(71300055) == 1:
            return State_58
        if GetFlagState(71300055) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1194) == 0:
            return State_8
        if GetFlagState(71300058) == 1:
            return State_10
        if GetFlagState(71300063) == 1:
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
        TalkToPlayer(conversation=18000400, unk1=-1, unk2=-1)
        SetFlagState(flag=71300055, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71300055, state=1)

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
        return [State_9, State_10, State_13, State_59, State_61, State_63, State_65, State_67, State_69, State_71, State_73]

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
        TalkToPlayer(conversation=18000500, unk1=-1, unk2=-1)
        SetFlagState(flag=71300059, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71300059, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18000250, unk1=-1, unk2=-1)

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
        SetFlagState(flag=71300077, state=1)

    def test(self):
        return State_44


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_6, State_18]

    def test(self):
        if GetFlagState(1196) == 1:
            return State_75
        if GetFlagState(1198) == 1:
            return State_74


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_7, State_25, State_26, State_47, State_57, State_100]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if GetFlagState(1196) == 1:
            return State_77
        if GetFlagState(1198) == 1:
            return State_76


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_8, State_12, State_58, State_60, State_62, State_64, State_66, State_68, State_70, State_72]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16

    def exit(self):
        RemoveMyAggro()


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_20]

    def test(self):
        return State_133


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_24, State_27, State_54, State_133, State_137]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000200, required_flag=-1)
        AddTalkListData(menu_index=5, menu_text=15000350, required_flag=280)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=1202)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_28
        if GetTalkListEntryResult() == 3:
            return State_31
        if GetTalkListEntryResult() == 1:
            return State_19
        if GetTalkListEntryResult() == 4:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_26
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_26
        if GetTalkListEntryResult() == 2:
            return State_56
        if GetTalkListEntryResult() == 5:
            return State_134

    def exit(self):
        ClearTalkListData()


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_22, State_25, State_26]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_25, State_26]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_21
        else:
            return State_29


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        TalkToPlayer(conversation=18011900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_30, State_35, State_98, State_99, State_131]

    def test(self):
        return State_20
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_133, State_134]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_22
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_21
        else:
            return State_6


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_22
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_21


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_84, State_89, State_90, State_118, State_120, State_122, State_124, State_126, State_128]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_20
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_20]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1 and GetFlagState(1193) == 0:
            return State_37
        if DidYouDoSomethingInTheMenu(11) == 0 and GetFlagState(1193) == 0:
            return State_38
        else:
            return State_6


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_22]

    def test(self):
        return State_6


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        SetFlagState(flag=71300084, state=1)

    def test(self):
        return State_24


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_20]

    def test(self):
        if GetFlagState(71300085) == 1 and GetFlagState(71300083) == 1:
            return State_34
        if GetFlagState(71300087) == 1:
            return State_99
        if GetFlagState(71300086) == 1:
            return State_98
        if GetFlagState(71300084) == 0 and GetFlagState(1171) == 0:
            return State_23
        else:
            return State_32


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        TalkToPlayer(conversation=18012000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71300085, state=1)

    def test(self):
        return State_97


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        TalkToPlayer(conversation=18012300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71300086, state=1)

    def test(self):
        return State_24


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        TalkToPlayer(conversation=18011700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_39


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_36


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        TalkToPlayer(conversation=18011700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        DebugEvent(message='奇跡を教わる')
        SetFlagState(flag=71300078, state=1)

    def test(self):
        return State_45


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        DebugEvent(message='奇跡を教わらない')
        SetFlagState(flag=71300079, state=1)

    def test(self):
        return State_46


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_15, State_86]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_41
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_43
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_43
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_42


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_42, State_78]

    def enter(self):
        TalkToPlayer(conversation=18011200, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_82
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        TalkToPlayer(conversation=18011300, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        else:
            return State_6


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_51, State_93]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=1)
        SetFlagState(flag=842, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_55
        if GetFlagState(842) == 0:
            return State_136


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        DebugEvent(message='誓約を変更しない')

    def test(self):
        if GetFlagState(71300092) == 0 and GetFlagState(1202) == 1:
            return State_85
        else:
            return State_48


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=1)
        RequestUnlockTrophy(7)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_49
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_51
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_51
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_50


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)
        RequestUnlockTrophy(7)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_55
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_54
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_54


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        if GetFlagState(71300091) == 0:
            return State_83
        if GetFlagState(71300091) == 1:
            return State_20
        else:
            return State_6


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_50, State_53, State_136, State_138]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_20, State_82, State_87]

    def test(self):
        if ComparePlayerStatus(11, 0, 1) == 1:
            return State_53
        else:
            return State_52


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_52, State_53, State_136, State_138]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        else:
            return State_6


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18000410, unk1=-1, unk2=-1)
        SetFlagState(flag=71300056, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        SetFlagState(flag=71300056, state=1)

    def test(self):
        return State_11


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18000420, unk1=-1, unk2=-1)
        SetFlagState(flag=71300057, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        SetFlagState(flag=71300057, state=1)

    def test(self):
        return State_11


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18000430, unk1=-1, unk2=-1)
        SetFlagState(flag=71300058, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=71300058, state=1)

    def test(self):
        return State_11


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18010800, unk1=-1, unk2=-1)
        SetFlagState(flag=71300064, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        SetFlagState(flag=71300064, state=1)

    def test(self):
        return State_11


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18010700, unk1=-1, unk2=-1)
        SetFlagState(flag=71300060, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        SetFlagState(flag=71300060, state=1)

    def test(self):
        return State_11


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18010710, unk1=-1, unk2=-1)
        SetFlagState(flag=71300061, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_68]

    def enter(self):
        SetFlagState(flag=71300061, state=1)

    def test(self):
        return State_11


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18010720, unk1=-1, unk2=-1)
        SetFlagState(flag=71300062, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_71
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        SetFlagState(flag=71300062, state=1)

    def test(self):
        return State_11


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=18010730, unk1=-1, unk2=-1)
        SetFlagState(flag=71300063, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        SetFlagState(flag=71300063, state=1)

    def test(self):
        return State_11


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=18000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=18010900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=18000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        TalkToPlayer(conversation=18010900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71300065) == 0:
            return State_101
        if GetFlagState(71300065) == 1 and GetFlagState(71300066) == 0:
            return State_103
        if GetFlagState(71300083) == 0 and GetFlagState(1171) == 1:
            return State_91
        if GetFlagState(71300078) == 0 and GetFlagState(71300079) == 0 and GetFlagState(71300066) == 1:
            return State_14
        if GetFlagState(71300078) == 0 and GetFlagState(71300079) == 1:
            return State_86
        if GetFlagState(71300090) == 0 and GetFlagState(71300078) == 1:
            return State_45
        if GetFlagState(71300090) == 1 and ComparePlayerStatus(11, 5, 1) == 1 and GetFlagState(71300091) == 0:
            return State_87
        if GetFlagState(71300091) == 0 and ComparePlayerStatus(11, 0, 1) == 1:
            return State_83
        if GetFlagState(71300081) == 1:
            return State_90
        else:
            return State_88


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(1180) == 1 and GetFlagState(71300072) == 1:
            return State_119
        if GetFlagState(1177) == 1 and GetFlagState(71300072) == 1:
            return State_119
        if GetFlagState(71300071) == 0 and GetFlagState(11026107) == 0 and GetFlagState(71300070) == 1:
            return State_113
        if GetFlagState(71300070) == 1 and GetFlagState(1180) == 1 and GetFlagState(71300072) == 0:
            return State_115
        if GetFlagState(71300070) == 1 and GetFlagState(1177) == 1 and GetFlagState(815) == 1 and GetFlagState(71300072) == 0:
            return State_115
        if GetFlagState(71300070) == 1:
            return State_117
        if GetFlagState(71300069) == 1:
            return State_111
        if GetFlagState(71300069) == 0 and GetFlagState(71300065) == 1:
            return State_109
        if GetFlagState(71300065) == 0:
            return State_101


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71300067) == 1 and GetFlagState(11026108) == 0:
            return State_107
        if GetFlagState(71300066) == 1:
            return State_105


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(1175) == 1 and GetFlagState(71300076) == 0:
            return State_125
        if GetFlagState(71300074) == 1 and GetFlagState(71300075) == 0:
            return State_123
        if GetFlagState(71300074) == 0:
            return State_121
        if GetFlagState(71300075) == 1:
            return State_127


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        SetFlagState(flag=71300090, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_6
        else:
            return State_56


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_54, State_78, State_137]

    def enter(self):
        TalkToPlayer(conversation=18011210, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_84
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        SetFlagState(flag=71300091, state=1)

    def test(self):
        return State_27


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=18011300, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_93
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_89
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_88]

    def enter(self):
        SetFlagState(flag=71300081, state=1)

    def test(self):
        return State_27


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_92
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_91]

    def enter(self):
        SetFlagState(flag=71300083, state=1)
        SetFlagState(flag=11020600, state=1)
        SetFlagState(flag=71300078, state=1)
        SetFlagState(flag=71300090, state=1)
        SetFlagState(flag=71300091, state=1)
        SetFlagState(flag=71300081, state=1)

    def test(self):
        return State_6


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_85]

    def enter(self):
        SetFlagState(flag=71300092, state=1)

    def test(self):
        return State_48


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        DebugEvent(message='奇跡を教わる')
        SubtractAcquittalCostFromPlayerSouls(100, 1)
        SetFlagState(flag=71300086, state=1)

    def test(self):
        return State_98


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        DebugEvent(message='奇跡を教わらない')
        SetFlagState(flag=71300079, state=1)
        SetFlagState(flag=71300087, state=1)

    def test(self):
        return State_99


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020050, unk2=3, unk3=4, display_distance=2)
        SetAquittalCostMessageTag(100, 1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_100
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_94
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_96
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_96
        if GetGenericDialogButtonResult() == 1 and ComparePlayerAcquittalPrice(100, 1, 2) == 1 and IsGenericDialogOpen() == 0:
            return State_130
        if GetGenericDialogButtonResult() == 1 and ComparePlayerAcquittalPrice(100, 1, 3) == 1 and IsGenericDialogOpen() == 0:
            return State_95


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_31, State_95]

    def enter(self):
        TalkToPlayer(conversation=18012100, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_31, State_96]

    def enter(self):
        TalkToPlayer(conversation=18012200, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_97, State_130]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_17
        else:
            return State_6


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_78, State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18000000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_102
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_101]

    def enter(self):
        SetFlagState(flag=71300065, state=1)

    def test(self):
        return State_6


class State_103(State):
    """ 103: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18000100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_104
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_3


class State_104(State):
    """ 104: No description. """

    def previous_states(self):
        return [State_103]

    def enter(self):
        SetFlagState(flag=71300066, state=1)
        SetFlagState(flag=11020599, state=1)

    def test(self):
        return State_6


class State_105(State):
    """ 105: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_106
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_106(State):
    """ 106: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        SetFlagState(flag=71300067, state=1)
        SetFlagState(flag=11026108, state=1)

    def test(self):
        return State_6


class State_107(State):
    """ 107: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_108
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_108(State):
    """ 108: No description. """

    def previous_states(self):
        return [State_107]

    def enter(self):
        SetFlagState(flag=71300068, state=1)
        SetFlagState(flag=11020600, state=1)

    def test(self):
        return State_6


class State_109(State):
    """ 109: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_110
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_110(State):
    """ 110: No description. """

    def previous_states(self):
        return [State_109]

    def enter(self):
        SetFlagState(flag=71300069, state=1)

    def test(self):
        return State_6


class State_111(State):
    """ 111: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_112
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_112(State):
    """ 112: No description. """

    def previous_states(self):
        return [State_111]

    def enter(self):
        SetFlagState(flag=71300070, state=1)
        SetFlagState(flag=11026107, state=1)

    def test(self):
        return State_6


class State_113(State):
    """ 113: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_114
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_114(State):
    """ 114: No description. """

    def previous_states(self):
        return [State_113]

    def enter(self):
        SetFlagState(flag=71300071, state=1)

    def test(self):
        return State_6


class State_115(State):
    """ 115: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_116
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_116(State):
    """ 116: No description. """

    def previous_states(self):
        return [State_115]

    def enter(self):
        SetFlagState(flag=71300072, state=1)

    def test(self):
        return State_6


class State_117(State):
    """ 117: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18012410, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_118
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_118(State):
    """ 118: No description. """

    def previous_states(self):
        return [State_117]

    def enter(self):
        SetFlagState(flag=71300073, state=1)

    def test(self):
        return State_27


class State_119(State):
    """ 119: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18012400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_120
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_120(State):
    """ 120: No description. """

    def previous_states(self):
        return [State_119]

    def enter(self):
        SetFlagState(flag=71300073, state=1)

    def test(self):
        return State_27


class State_121(State):
    """ 121: No description. """

    def previous_states(self):
        return [State_81]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_122
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_122(State):
    """ 122: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        SetFlagState(flag=71300074, state=1)

    def test(self):
        return State_27


class State_123(State):
    """ 123: No description. """

    def previous_states(self):
        return [State_81]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_124
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_124(State):
    """ 124: No description. """

    def previous_states(self):
        return [State_123]

    def enter(self):
        SetFlagState(flag=71300075, state=1)

    def test(self):
        return State_27


class State_125(State):
    """ 125: No description. """

    def previous_states(self):
        return [State_81]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18010600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_126
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_126(State):
    """ 126: No description. """

    def previous_states(self):
        return [State_125]

    def enter(self):
        SetFlagState(flag=71300076, state=1)
        SetFlagState(flag=71300075, state=1)
        SetFlagState(flag=71300074, state=1)

    def test(self):
        return State_27


class State_127(State):
    """ 127: No description. """

    def previous_states(self):
        return [State_81]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=18011500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_128
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_128(State):
    """ 128: No description. """

    def previous_states(self):
        return [State_127]

    def test(self):
        return State_27


class State_129(State):
    """ 129: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=18011000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71300093, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_130(State):
    """ 130: No description. """

    def previous_states(self):
        return [State_97]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010752, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_100
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_132
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_131
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_131


class State_131(State):
    """ 131: No description. """

    def previous_states(self):
        return [State_130, State_138]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_24


class State_132(State):
    """ 132: No description. """

    def previous_states(self):
        return [State_130]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_133(State):
    """ 133: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        OpenRegularShop(4000, 4099)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25
        if IsMenuOpen(11) == 0:
            return State_20


class State_134(State):
    """ 134: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9005, 1)
        AcquireGesture(5)
        SetFlagState(flag=280, state=0)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_25
        if IsMenuOpen(63) == 0:
            return State_138


class State_135(State):
    """ 135: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71300093, state=0)

    def test(self):
        return State_6


class State_136(State):
    """ 136: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わしました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_55
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_137
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_137


class State_137(State):
    """ 137: No description. """

    def previous_states(self):
        return [State_136]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        if GetFlagState(71300091) == 0:
            return State_83
        else:
            return State_20


class State_138(State):
    """ 138: No description. """

    def previous_states(self):
        return [State_134]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_55
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_131
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_131
