from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_80


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
        return [State_8, State_12, State_14, State_16, State_22, State_31, State_44, State_46, State_48, State_50, State_52, State_54, State_55, State_56, State_58, State_59, State_65, State_67, State_69]

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
        return [State_2, State_4, State_5, State_11, State_16, State_20, State_23, State_24, State_26, State_28, State_31, State_35, State_41, State_43, State_52, State_55, State_58, State_61, State_64, State_71, State_74, State_77, State_78, State_80]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1702) == 0 and GetDistanceToPlayer() <= 5:
            return State_52
        if GetFlagState(1701) == 1 and IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800067) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5:
            return State_71
        if IsEquipmentIDObtained(3, 373) == 0 and GetFlagState(71800065) == 1:
            return State_78
        if IsEquipmentIDObtained(3, 373) == 1 and GetFlagState(71800065) == 0:
            return State_77
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1700) == 1:
            return State_53
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1701) == 0 and GetFlagState(1702) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1702) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_14, State_22, State_31, State_54, State_55, State_56, State_58, State_59, State_65, State_67, State_69]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800055) == 0 and GetSelfHP() <= 90:
            return State_12
        if GetFlagState(1701) == 1:
            return State_10
        if GetFlagState(71800054) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800053) == 1:
            return State_50
        if GetFlagState(71800053) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800052) == 1:
            return State_48
        if GetFlagState(71800052) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800051) == 1:
            return State_46
        if GetFlagState(71800051) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71800050) == 1:
            return State_44
        if GetFlagState(71800050) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_8
        if GetFlagState(71300058) == 1:
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
        TalkToPlayer(conversation=47000900, unk1=-1, unk2=-1)
        SetFlagState(flag=71800050, state=1)
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
        SetFlagState(flag=71800050, state=1)

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
        return [State_9, State_10, State_13, State_45, State_47, State_49, State_51]

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
        TalkToPlayer(conversation=47001000, unk1=-1, unk2=-1)
        SetFlagState(flag=71800055, state=1)
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
        SetFlagState(flag=71800055, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000100, unk1=-1, unk2=-1)

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
        SetFlagState(flag=71800058, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_7, State_24, State_25, State_43, State_64]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47001100, unk1=-1, unk2=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_8, State_12, State_44, State_46, State_48, State_50]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_52

    def exit(self):
        RemoveMyAggro()


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        return State_75


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_23, State_26, State_75]

    def enter(self):
        AddTalkListData(menu_index=2, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=5, menu_text=15000210, required_flag=-1)
        AddTalkListData(menu_index=6, menu_text=15000165, required_flag=-1)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=1, menu_text=15000350, required_flag=283)
        AddTalkListData(menu_index=3, menu_text=15000000, required_flag=71300069)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_27
        if GetTalkListEntryResult() == 3:
            return State_30
        if GetTalkListEntryResult() == 2:
            return State_18
        if GetTalkListEntryResult() == 4:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_25
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if GetTalkListEntryResult() == 5:
            return State_42
        if GetTalkListEntryResult() == 6:
            return State_84
        if GetTalkListEntryResult() == 1:
            return State_79

    def exit(self):
        ClearTalkListData()


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_21, State_24, State_25]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_6


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_24, State_25]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_20
        else:
            return State_28


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        TalkToPlayer(conversation=47001700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_29, State_34, State_40, State_62, State_73]

    def test(self):
        return State_19
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_75, State_79]

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


class State_25(State):
    """ 25: No description. """

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


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_15, State_57, State_60, State_66, State_68, State_70, State_76]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_19
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_6


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        if GetFlagState(71800064) == 1:
            return State_58
        if DidYouDoSomethingInTheMenu(11) == 1 and IsEquipmentIDObtained(3, 373) == 1 and GetFlagState(71800065) == 0:
            return State_32
        else:
            return State_33
        # UNREACHABLE:
        # if 1:
        #     return State_34


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_21]

    def test(self):
        return State_6


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        SetFlagState(flag=71800066, state=1)

    def test(self):
        return State_23


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        return State_22


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        TalkToPlayer(conversation=47000800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_55


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_31


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_27, State_37]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_23


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=0)
        SetFlagState(flag=840, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_41
        if GetFlagState(840) == 0:
            return State_81


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        DebugEvent(message='誓約を変更しない')

    def test(self):
        return State_34


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010746, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_35
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_37
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_37
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_36


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010727, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_41
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_40
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_40


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_39, State_81]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_36, State_39, State_81, State_85]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        if ComparePlayerStatus(11, 0, 0) == 1:
            return State_39
        else:
            return State_38


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_38, State_39, State_81]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        else:
            return State_6


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=47000910, unk1=-1, unk2=-1)
        SetFlagState(flag=71800051, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        SetFlagState(flag=71800051, state=1)

    def test(self):
        return State_11


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=47000920, unk1=-1, unk2=-1)
        SetFlagState(flag=71800052, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        SetFlagState(flag=71800052, state=1)

    def test(self):
        return State_11


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=47000930, unk1=-1, unk2=-1)
        SetFlagState(flag=71800053, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        SetFlagState(flag=71800053, state=1)

    def test(self):
        return State_11


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=47000940, unk1=-1, unk2=-1)
        SetFlagState(flag=71800054, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_17
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=71800054, state=1)

    def test(self):
        return State_11


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_6, State_17]

    def enter(self):
        TalkToPlayer(conversation=47001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71800056) == 0 and GetFlagState(71800057) == 0 and ComparePlayerStatus(11, 5, 1) == 1:
            return State_59
        if GetFlagState(71800056) == 0 and ComparePlayerStatus(11, 0, 1) == 1 and GetFlagState(71800057) == 0:
            return State_56
        if GetFlagState(71800061) == 1 and GetFlagState(11016111) == 0 and GetPlayerChrType() == 8:
            return State_67
        if GetFlagState(71800058) == 1 and GetPlayerChrType() == 8:
            return State_69
        if GetFlagState(11016111) == 0 and GetFlagState(71800059) == 1:
            return State_65
        if GetFlagState(71800058) == 1 and GetFlagState(11016111) == 0:
            return State_54
        else:
            return State_14


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        TalkToPlayer(conversation=47001600, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3
        if HasTalkEnded() == 1:
            return State_76


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71800056, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_27]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000600, unk1=-1, unk2=-1)
        SetFlagState(flag=71800064, state=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71800057, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        DebugEvent(message='免罪しない')
        SetFlagState(flag=71300079, state=1)
        SetFlagState(flag=71300087, state=1)

    def test(self):
        return State_23


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020052, unk2=3, unk3=4, display_distance=2)
        SetAquittalCostMessageTag(500, 1)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_61
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_62
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_62
        if GetGenericDialogButtonResult() == 1 and ComparePlayerAcquittalPrice(500, 1, 2) == 1 and IsGenericDialogOpen() == 0:
            return State_72
        if GetGenericDialogButtonResult() == 1 and ComparePlayerAcquittalPrice(500, 1, 3) == 1 and IsGenericDialogOpen() == 0:
            return State_85


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_63, State_72, State_82, State_83, State_87]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_16
        else:
            return State_6


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        SetFlagState(flag=71800060, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_68
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        SetFlagState(flag=71800062, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=47000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_70
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_69]

    def enter(self):
        SetFlagState(flag=71800061, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        TalkToPlayer(conversation=47001200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71800067, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010754, unk2=1, unk3=0, display_distance=1)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_74
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_73
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_73


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72, State_82, State_83, State_87]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_72, State_82, State_83, State_87]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        OpenRegularShop(4400, 4499)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_24
        if IsMenuOpen(11) == 0:
            return State_19


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        SetFlagState(flag=71800059, state=1)
        SetFlagState(flag=11016111, state=1)

    def test(self):
        return State_26


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        SetFlagState(flag=71800065, state=1)

    def test(self):
        return State_6


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        SetFlagState(flag=71800065, state=0)

    def test(self):
        return State_6


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9011, 1)
        AcquireGesture(11)
        SetFlagState(flag=283, state=0)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15:
            return State_24
        if IsMenuOpen(63) == 0:
            return State_87


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71800067, state=0)

    def test(self):
        return State_6


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010728, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を破棄した')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_41
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_40
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_40


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_85]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010735, unk2=1, unk3=0, display_distance=1)
        DebugEvent(message='免罪する')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_74
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_73
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_73


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010734, unk2=1, unk3=0, display_distance=1)
        DebugEvent(message='罪を犯していない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 15 or IsAttackedBySomeone() == 1:
            return State_74
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_73
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_73


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_19]

    def test(self):
        if GetFlagState(742) == 0 and GetFlagState(744) == 0:
            return State_83
        if GetFlagState(742) == 1 or GetFlagState(744) == 1:
            return State_63


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_63]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        DebugEvent(message='免罪する')
        SubtractAcquittalCostFromPlayerSouls(500, 1)
        SetFlagState(flag=755, state=1)
        SetFlagState(flag=71800064, state=1)
        SetFlagState(flag=840, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_41
        if GetFlagState(840) == 0:
            return State_82


class State_86(State):
    """ 86: No description. """

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010735, unk2=1, unk3=0, display_distance=1)
        DebugEvent(message='免罪する')
        DisplayOneLineHelp(text_id=-1)
        SubtractAcquittalCostFromPlayerSouls(500, 1)
        SetFlagState(flag=755, state=1)
        SetFlagState(flag=71800064, state=1)


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_79]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_64
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_74
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_73
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_73
