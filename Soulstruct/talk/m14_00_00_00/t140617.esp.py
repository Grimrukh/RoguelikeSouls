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
        OpenRegularShop(3400, 3499)

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
        return [State_1, State_13, State_22, State_74]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000190, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if GetTalkListEntryResult() == 0:
            return State_24
        if GetTalkListEntryResult() == 3:
            return State_27
        if GetTalkListEntryResult() == 1:
            return State_2
        if GetTalkListEntryResult() == 2:
            return State_74
        if GetTalkListEntryResult() == 4:
            return State_24

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

    def enter(self):
        TalkToPlayer(conversation=27000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if GetDistanceToPlayer() >= 12:
            return State_4
        if HasTalkEnded() == 1:
            return State_25


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71400057, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=27000700, unk1=-1, unk2=-1)
        SetFlagState(flag=71400057, state=1)
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
        return [State_6, State_9, State_10, State_66]

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
        SetFlagState(flag=71400055, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=27000640, unk1=-1, unk2=-1)
        SetFlagState(flag=71400055, state=1)
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
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=27000900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_26, State_61, State_63, State_65, State_75]

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_15


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_5, State_12, State_23, State_29, State_38, State_39, State_44, State_46, State_48, State_50, State_51, State_53, State_55, State_57, State_59, State_60, State_62, State_64, State_68, State_71, State_72, State_75, State_76, State_77]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_31
        if GetFlagState(71400057) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1294) == 1:
            return State_9
        if GetFlagState(71400056) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400055) == 1:
            return State_67
        if GetFlagState(71400055) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_11
        if GetFlagState(71400028) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_0, State_4, State_8, State_13, State_16, State_17, State_18, State_21, State_22, State_24, State_25, State_28, State_31, State_33, State_34, State_40, State_54, State_58, State_68, State_71, State_73, State_76, State_77]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1295) == 0 and GetDistanceToPlayer() <= 5:
            return State_28
        if GetFlagState(1293) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_43
        if GetFlagState(1292) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_49
        if GetFlagState(1291) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_42
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1290) == 0 and GetFlagState(1294) == 0 and GetFlagState(1295) == 0:
            return State_16
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_17
        if IsAttackedBySomeone() == 1 and GetFlagState(1295) == 0:
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
        return [State_1, State_74]

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
        return [State_7, State_11, State_12, State_28, State_29, State_31, State_38, State_39, State_44, State_46, State_48, State_50, State_51, State_53, State_55, State_57, State_59, State_60, State_62, State_64, State_67, State_68, State_71, State_72, State_75, State_76, State_77]

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
        return [State_41, State_45, State_47, State_52, State_56, State_58, State_59]

    def enter(self):
        ClearTalkActionState()
        SetFlagState(flag=365, state=1)
        SetFlagState(flag=366, state=1)

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
        if GetFlagState(722) == 1:
            return State_72
        if DidYouDoSomethingInTheMenu(11) == 1 or DidYouDoSomethingInTheMenu(4) == 1:
            return State_69
        if DidYouDoSomethingInTheMenu(11) == 0 or DidYouDoSomethingInTheMenu(4) == 0:
            return State_70
        else:
            return State_15


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        SetFlagState(flag=11405021, state=1)

    def test(self):
        return State_15


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71400073, state=1)

    def test(self):
        return State_13


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(71400077) == 1:
            return State_75
        if GetFlagState(11406104) == 0 and GetFlagState(71400075) == 1 and GetFlagState(71400077) == 0:
            return State_64
        if GetFlagState(71400074) == 1 and GetFlagState(11406104) == 0 and GetFlagState(71400075) == 0:
            return State_62
        if GetFlagState(71400073) == 1:
            return State_60
        if GetFlagState(71400073) == 0:
            return State_12


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_15, State_32]

    def enter(self):
        TalkToPlayer(conversation=27000800, unk1=-1, unk2=-1)
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
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000000, unk1=-1, unk2=-1)
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
        return [State_29, State_48]

    def enter(self):
        SetFlagState(flag=71400058, state=1)

    def test(self):
        return State_37


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_14, State_18, State_19, State_40]

    def enter(self):
        TalkToPlayer(conversation=27000800, unk1=-1, unk2=-1)
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
        return [State_7, State_11, State_67]

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
        return [State_39]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_15


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_15


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DebugEvent(message='YES')
        SetFlagState(flag=71400059, state=1)

    def test(self):
        return State_38


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DebugEvent(message='NO')
        SetFlagState(flag=71400060, state=1)

    def test(self):
        return State_39


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_36
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_36
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_35


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_35, State_42]

    def enter(self):
        TalkToPlayer(conversation=27000020, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        TalkToPlayer(conversation=27000040, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_31
        else:
            return State_15


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71400061, state=1)

    def test(self):
        return State_22


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(11405021) == 1:
            return State_55
        if GetFlagState(71400059) == 0 and GetFlagState(71400060) == 1:
            return State_48
        if GetFlagState(71400059) == 1 and GetFlagState(71400061) == 0:
            return State_38
        if GetFlagState(71400059) == 0 and GetFlagState(71400060) == 0:
            return State_29
        if GetFlagState(11406100) == 0 and GetFlagState(71400063) == 1:
            return State_51
        if GetFlagState(71400063) == 1 and GetFlagState(71400064) == 1:
            return State_50
        if GetFlagState(71400063) == 1 and GetFlagState(71400064) == 0:
            return State_44
        if GetFlagState(71400063) == 0:
            return State_46


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        if GetFlagState(71400077) == 1:
            return State_59
        if GetFlagState(71400077) == 0:
            return State_57


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000120, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44, State_50]

    def enter(self):
        SetFlagState(flag=71400064, state=1)
        SetFlagState(flag=11406100, state=1)

    def test(self):
        return State_22


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71400063, state=1)
        SetFlagState(flag=11406100, state=1)

    def test(self):
        return State_22


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000060, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_15]

    def test(self):
        return State_53


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000130, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000140, unk1=-1, unk2=-1)
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
        SetFlagState(flag=71400066, state=1)
        SetFlagState(flag=71400063, state=0)
        SetFlagState(flag=71400064, state=0)
        SetFlagState(flag=11406100, state=1)

    def test(self):
        return State_22


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        TalkToPlayer(conversation=27000340, unk1=-1, unk2=-1)
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
        SetFlagState(flag=71400072, state=1)

    def test(self):
        return State_15


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=27000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

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
        SetFlagState(flag=11405021, state=0)

    def test(self):
        return State_22


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        TalkToPlayer(conversation=27001300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_20


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71400077, state=1)
        SetFlagState(flag=11400594, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_15
        if IsMenuOpen(63) == 0:
            return State_22


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        TalkToPlayer(conversation=27000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=27001000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        SetFlagState(flag=71400074, state=1)
        SetFlagState(flag=11406104, state=1)

    def test(self):
        return State_13


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=27001100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_63
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=71400075, state=1)
        SetFlagState(flag=11406104, state=1)

    def test(self):
        return State_13


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=27001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        SetFlagState(flag=71400076, state=1)

    def test(self):
        return State_13


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        SetFlagState(flag=71400056, state=1)

    def test(self):
        return State_8


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=27000660, unk1=-1, unk2=-1)
        SetFlagState(flag=71400056, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_32
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        TalkToPlayer(conversation=27000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        if GetFlagState(71400077) == 1:
            return State_76
        else:
            return State_71


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        if GetFlagState(71400077) == 1:
            return State_77
        else:
            return State_68


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        TalkToPlayer(conversation=27000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        TalkToPlayer(conversation=27000320, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        SetFlagState(flag=71400071, state=1)
        SetFlagState(flag=11400595, state=1)

    def test(self):
        return State_15


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        CollectJustPyromancyFlame()
        CombineMenuFlagAndEventFlag(365, 331)
        CombineMenuFlagAndEventFlag(366, 332)
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_18
        if IsMenuOpen(13) == 0:
            return State_3


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        TalkToPlayer(conversation=27001310, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        TalkToPlayer(conversation=27000350, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        TalkToPlayer(conversation=27000250, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_14
        if HasTalkEnded() == 1:
            return State_15
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_20
