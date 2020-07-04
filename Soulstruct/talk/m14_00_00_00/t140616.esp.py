from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_16


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        OpenRegularShop(3200, 3209)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if IsMenuOpen(11) == 0:
            return State_3


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(1286) == 1:
            return State_93
        if GetFlagState(1286) == 0:
            return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1, State_14, State_23, State_93, State_96]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000190, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_20
        if GetTalkListEntryResult() == 0:
            return State_25
        if GetTalkListEntryResult() == 3:
            return State_29
        if GetTalkListEntryResult() == 1:
            return State_2
        if GetTalkListEntryResult() == 2:
            return State_96
        if GetTalkListEntryResult() == 4:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_20

    def exit(self):
        ClearTalkListData()


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_19, State_20]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_16


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_19, State_20]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_4
        else:
            return State_27


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7, State_92]

    def enter(self):
        SetFlagState(flag=71400024, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001600, unk1=-1, unk2=-1)
        SetFlagState(flag=71400024, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_21


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_10, State_86, State_88, State_90]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_16


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        SetFlagState(flag=71400020, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001500, unk1=-1, unk2=-1)
        SetFlagState(flag=71400020, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_10
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=26000200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_28, State_44, State_49, State_73, State_75, State_77, State_79, State_81]

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_16


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_12, State_13, State_24, State_26, State_31, State_40, State_41, State_49, State_50, State_53, State_55, State_57, State_59, State_61, State_64, State_66, State_68, State_70, State_72, State_74, State_76, State_78, State_80, State_82, State_84, State_95, State_97]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_94
        if GetFlagState(71400024) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400038) == 1 and GetSelfHP() <= 90 and GetFlagState(71400050) == 0:
            return State_92
        if GetFlagState(71400024) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400038) == 0 and GetSelfHP() <= 90 and GetFlagState(71400050) == 0:
            return State_7
        if GetFlagState(1282) == 1:
            return State_9
        if GetFlagState(1283) == 1:
            return State_9
        if GetFlagState(1287) == 1:
            return State_9
        if GetFlagState(71400023) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400022) == 1:
            return State_91
        if GetFlagState(71400022) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400021) == 1:
            return State_89
        if GetFlagState(71400021) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400020) == 1:
            return State_87
        if GetFlagState(71400020) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_11
        if GetFlagState(71400023) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_0, State_4, State_8, State_12, State_14, State_17, State_18, State_19, State_22, State_23, State_25, State_26, State_27, State_30, State_33, State_35, State_36, State_42, State_43, State_45, State_46, State_63, State_65, State_67, State_94]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1284) == 0 and GetFlagState(1272) == 0 and GetDistanceToPlayer() <= 5:
            return State_30
        if GetFlagState(1272) == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71400050) == 0 and GetFlagState(1284) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_63
        if GetFlagState(1286) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_52
        if GetFlagState(1281) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_58
        if GetFlagState(1280) == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_51
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1282) == 0 and GetFlagState(1283) == 0 and GetFlagState(1284) == 0 and GetFlagState(1287) == 0 and GetFlagState(11405001) == 0:
            return State_17
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_18
        if IsAttackedBySomeone() == 1 and GetFlagState(1284) == 0:
            return State_24


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_16


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_16


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_1, State_93, State_96]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_94
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4
        else:
            return State_16


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_94
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_7, State_11, State_12, State_13, State_26, State_30, State_31, State_33, State_40, State_41, State_49, State_50, State_53, State_55, State_57, State_59, State_61, State_63, State_64, State_66, State_68, State_70, State_72, State_74, State_76, State_78, State_80, State_82, State_84, State_87, State_89, State_91, State_92, State_95, State_97]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_22


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_16


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_54, State_56, State_60, State_62, State_69, State_71]

    def enter(self):
        ClearTalkActionState()
        SetFlagState(flag=365, state=1)

    def test(self):
        return State_3
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_16


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_15


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        return State_16


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=26000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_5]

    def test(self):
        return State_16


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        SetFlagState(flag=71400036, state=1)

    def test(self):
        return State_14


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_3]

    def test(self):
        if GetFlagState(71400049) == 1 and GetFlagState(71400048) == 0 and GetFlagState(11406103) == 0:
            return State_84
        if GetFlagState(71400048) == 0 and GetFlagState(71400049) == 0 and ComparePlayerStatus(5, 2, 10) == 1 and GetFlagState(1286) == 1 and GetFlagState(11406103) == 0:
            return State_82
        if GetFlagState(71400042) == 0 and GetFlagState(1286) == 1 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_74
        if GetFlagState(71400036) == 1 and GetFlagState(1286) == 0:
            return State_72
        if GetFlagState(71400036) == 0 and GetFlagState(1286) == 0:
            return State_13
        if GetFlagState(11406103) == 0 and GetFlagState(71400044) == 1:
            return State_80
        if GetFlagState(11406103) == 0 and GetFlagState(71400043) == 1:
            return State_78
        if GetFlagState(1286) == 1:
            return State_76


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_16, State_34]

    def enter(self):
        TalkToPlayer(conversation=26001700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 5:
            return State_21


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=26000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_31, State_57]

    def enter(self):
        SetFlagState(flag=71400027, state=1)

    def test(self):
        return State_39


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_94]

    def enter(self):
        TalkToPlayer(conversation=26001700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 5:
            return State_21


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_7, State_11, State_87, State_89, State_91, State_92]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_30

    def exit(self):
        RemoveMyAggro()


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_16


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_16


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        DebugEvent(message='YES')
        SetFlagState(flag=71400028, state=1)

    def test(self):
        if GetFlagState(753) == 1:
            return State_95
        else:
            return State_40


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        DebugEvent(message='NO')
        SetFlagState(flag=71400029, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_41


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_36
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_37


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_37, State_51]

    def enter(self):
        TalkToPlayer(conversation=26000020, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        TalkToPlayer(conversation=26000040, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_39, State_48]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_94
        else:
            return State_16


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_40, State_95]

    def enter(self):
        SetFlagState(flag=11400593, state=1)
        SetFlagState(flag=71400030, state=1)

    def test(self):
        return State_16


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_14


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_16


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        DebugEvent(message='教わる')
        SetFlagState(flag=71400048, state=1)
        SetFlagState(flag=11400592, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_16
        if IsMenuOpen(63) == 0:
            return State_49


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        DebugEvent(message='教わらない')
        SetFlagState(flag=71400049, state=1)

    def test(self):
        return State_50


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_83, State_85]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020040, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_47
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_47
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_46


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        TalkToPlayer(conversation=26002200, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        TalkToPlayer(conversation=26002300, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if GetFlagState(71400028) == 0 and GetFlagState(71400029) == 0 and GetFlagState(11406102) == 0:
            return State_31
        if GetFlagState(71400029) == 1 and GetFlagState(11406102) == 1 and GetFlagState(71400028) == 0:
            return State_12
        if GetFlagState(71400028) == 1 and GetFlagState(11400593) == 0 and GetFlagState(753) == 1:
            return State_95
        if GetFlagState(71400028) == 1 and GetFlagState(11400593) == 0:
            return State_40
        if GetFlagState(71400028) == 0 and GetFlagState(71400029) == 1 and GetFlagState(11406102) == 0:
            return State_57


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if GetFlagState(753) == 1 and GetFlagState(11400591) == 0 and GetFlagState(71400038) == 1:
            return State_66
        if GetFlagState(753) == 1 and GetFlagState(71400038) == 0 and GetFlagState(71400051) == 1:
            return State_97
        if GetFlagState(753) == 1 and GetFlagState(71400038) == 0:
            return State_64
        if GetFlagState(71400038) == 1 and GetFlagState(11406102) == 0 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_70
        else:
            return State_68


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=26000400, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_54
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        SetFlagState(flag=71400033, state=1)

    def test(self):
        return State_23


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=26000300, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        SetFlagState(flag=71400032, state=1)

    def test(self):
        return State_23


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        TalkToPlayer(conversation=26000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_16]

    def test(self):
        if GetFlagState(71400030) == 1 and GetFlagState(71400012) == 0:
            return State_26
        if IsEquipmentIDEquipped(2, 137) == 1 and GetFlagState(71400000) == 1:
            return State_55
        if GetFlagState(71400034) == 1:
            return State_61
        if GetFlagState(71400033) == 1:
            return State_59
        else:
            return State_53


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=26000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71400034, state=1)

    def test(self):
        return State_23


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=26000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        SetFlagState(flag=71400035, state=1)
        SetFlagState(flag=71400034, state=0)
        SetFlagState(flag=71400033, state=0)

    def test(self):
        return State_23


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=26001800, unk1=-1, unk2=-1)
        SetFlagState(flag=71400050, state=1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_16
        if GetDistanceToPlayer() >= 10:
            return State_21


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=26000900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_21


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_64, State_97]

    def enter(self):
        SetFlagState(flag=71400038, state=1)
        SetFlagState(flag=11400591, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_16


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=26001000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_21


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        SetFlagState(flag=71400039, state=1)
        SetFlagState(flag=11400591, state=1)

    def test(self):
        return State_16


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=26001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_68]

    def enter(self):
        SetFlagState(flag=71400040, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_23


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=26001200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_71
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        SetFlagState(flag=71400041, state=1)
        SetFlagState(flag=11406102, state=1)

    def test(self):
        return State_23


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        SetFlagState(flag=71400037, state=1)

    def test(self):
        return State_14


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_74]

    def enter(self):
        SetFlagState(flag=71400042, state=1)

    def test(self):
        return State_14


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        SetFlagState(flag=71400043, state=1)
        SetFlagState(flag=11406103, state=1)

    def test(self):
        return State_14


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26001900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_79
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        SetFlagState(flag=71400044, state=1)
        SetFlagState(flag=11406103, state=1)

    def test(self):
        return State_14


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26002000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_81
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_80]

    def enter(self):
        SetFlagState(flag=71400045, state=1)

    def test(self):
        return State_14


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26002100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_83
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_82]

    def enter(self):
        SetFlagState(flag=71400046, state=1)
        SetFlagState(flag=11406103, state=1)

    def test(self):
        return State_48


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_29]

    def enter(self):
        TalkToPlayer(conversation=26002110, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_85
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        SetFlagState(flag=71400047, state=1)
        SetFlagState(flag=11406103, state=1)

    def test(self):
        return State_48


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        SetFlagState(flag=71400021, state=1)

    def test(self):
        return State_8


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001510, unk1=-1, unk2=-1)
        SetFlagState(flag=71400021, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        SetFlagState(flag=71400022, state=1)

    def test(self):
        return State_8


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001520, unk1=-1, unk2=-1)
        SetFlagState(flag=71400022, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_91]

    def enter(self):
        SetFlagState(flag=71400023, state=1)

    def test(self):
        return State_8


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001530, unk1=-1, unk2=-1)
        SetFlagState(flag=71400023, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_90
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        TalkToPlayer(conversation=26001650, unk1=-1, unk2=-1)
        SetFlagState(flag=71400024, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_34
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_21


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        OpenRegularShop(3200, 3299)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if IsMenuOpen(11) == 0:
            return State_3


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_15, State_19, State_20, State_42]

    def test(self):
        if GetFlagState(1272) == 0:
            return State_33
        else:
            return State_16


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_37, State_51]

    def enter(self):
        TalkToPlayer(conversation=26000021, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')
        SetFlagState(flag=71400051, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_21


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        CollectJustPyromancyFlame()
        CombineMenuFlagAndEventFlag(365, 331)
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_19
        if IsMenuOpen(13) == 0:
            return State_3


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=26000903, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_65
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_21
