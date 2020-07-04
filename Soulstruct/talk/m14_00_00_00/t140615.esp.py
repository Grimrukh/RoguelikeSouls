from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_25


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_23


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_6, State_59, State_61, State_62]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if IsEquipmentIDEquipped(2, 137) == 1:
            return State_15
        else:
            return State_25


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        BreakCovenantPledge()
        DebugEvent(message='誓約を変更する')
        ChangePlayerStats(unk1=11, unk2=5, unk3=9)
        SetFlagState(flag=849, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or IsAttackedBySomeone() == 1:
            return State_9
        if GetFlagState(11400596) == 0 and GetFlagState(849) == 0:
            return State_76
        if GetFlagState(849) == 0:
            return State_207


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

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=25000700, unk1=-1, unk2=-1)
        DebugEvent(message='誓約結ぶ前会話')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_5, State_215]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=9)
        RequestUnlockTrophy(15)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_4
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_3


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_8
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_8


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7, State_207]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_3, State_7, State_207, State_208, State_209]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        TalkToPlayer(conversation=25000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_37


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_10


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_23, State_32]

    def enter(self):
        AddTalkListData(menu_index=2, menu_text=15000265, required_flag=859)
        AddTalkListData(menu_index=4, menu_text=15000230, required_flag=716)
        AddTalkListData(menu_index=3, menu_text=15000200, required_flag=-1)
        AddTalkListData(menu_index=7, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=8, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_29
        if GetTalkListEntryResult() == 0:
            return State_34
        if GetTalkListEntryResult() == 7:
            return State_40
        if GetTalkListEntryResult() == 8:
            return State_34
        if GetTalkListEntryResult() == 3:
            return State_44
        if GetTalkListEntryResult() == 2:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_29
        if GetTalkListEntryResult() == 4:
            return State_87

    def exit(self):
        ClearTalkListData()


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_15, State_28, State_29]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_25


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_2, State_28, State_29]

    def enter(self):
        TalkToPlayer(conversation=25000500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if GetDistanceToPlayer() >= 15:
            return State_14
        if HasTalkEnded() == 1:
            return State_38


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        SetFlagState(flag=71400009, state=1)

    def test(self):
        return State_17


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16, State_18, State_19, State_56]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_25


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_17


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        SetFlagState(flag=71400008, state=1)

    def test(self):
        return State_17


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        TalkToPlayer(conversation=25001000, unk1=-1, unk2=-1)
        SetFlagState(flag=71400008, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=25000150, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        TalkToPlayer(conversation=25001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_1, State_8, State_49, State_51, State_53, State_54, State_63, State_67, State_68, State_85, State_201, State_204, State_212, State_214]

    def test(self):
        return State_13
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 8:
        #     return State_25


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_5, State_10, State_15, State_21, State_22, State_33, State_35, State_37, State_42, State_45, State_46, State_47, State_50, State_52, State_54, State_70, State_211, State_213, State_214, State_215]

    def enter(self):
        ClearTalkProgressData()
        ForceEndTalk(unk1=3)

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_73
        if GetFlagState(1271) == 1:
            return State_18
        if GetFlagState(71400010) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 8 and GetFlagState(71400009) == 1 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_57
        if GetFlagState(71400009) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 8 and GetFlagState(71400008) == 1 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_55
        if GetFlagState(71400008) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 8 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_20
        if GetFlagState(71400010) == 1:
            return State_18
        else:
            return State_18

    def exit(self):
        RemoveMyAggro()


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_0, State_2, State_9, State_10, State_14, State_17, State_23, State_26, State_27, State_28, State_31, State_32, State_34, State_37, State_38, State_43, State_48, State_66, State_69, State_71, State_73, State_74, State_75, State_76, State_77, State_78, State_79, State_80, State_86, State_88, State_202, State_205]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1272) == 0 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_43
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and IsEquipmentIDEquipped(2, 137) == 0:
            return State_213
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(11405020) == 1 and GetFlagState(71400000) == 1:
            return State_42
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71400001) == 1 and GetFlagState(71400002) == 0:
            return State_21
        if GetFlagState(71400001) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71400000) == 1:
            return State_35
        if GetFlagState(71400000) == 0 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1:
            return State_47
        if IsAttackedBySomeone() == 1 and GetFlagState(1272) == 0:
            return State_33
        if GetOneLineHelpStatus() == 0 and GetFlagState(1271) == 0 and GetFlagState(1272) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and RelativeAngleBetweenTwoPlayers_SpecifyAxis(-20) <= 40 and GetDistanceToPlayer() <= 5 and GetRelativeAngleBetweenPlayerAndSelf() <= 40:
            return State_71
        if GetOneLineHelpStatus() == 0 and GetFlagState(1271) == 0 and GetFlagState(1272) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and RelativeAngleBetweenTwoPlayers_SpecifyAxis(20) <= 40 and GetDistanceToPlayer() <= 5 and GetRelativeAngleBetweenPlayerAndSelf() <= 40:
            return State_26
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 80 or GetDistanceToPlayer() > 5):
            return State_27


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)
        ChangeMotionOffsetID(1)
        DebugEvent(message='向かって左')

    def test(self):
        return State_25


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_25


class State_28(State):
    """ 28: No description. """

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_73
        if IsPlayerMovingACertainDistance(1) == 1 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_15
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_14
        else:
            return State_25


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_73
        if IsPlayerMovingACertainDistance(1) == 1 and IsEquipmentIDEquipped(2, 137) == 1:
            return State_15
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_14


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_5, State_10, State_20, State_21, State_22, State_35, State_37, State_42, State_43, State_45, State_46, State_47, State_50, State_52, State_54, State_55, State_57, State_70, State_73, State_211, State_213, State_214, State_215]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_31


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_25


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_36, State_39, State_41, State_213]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_13
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 8:
        #     return State_25


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_24


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_13]

    def test(self):
        if IsEquipmentIDEquipped(2, 137) == 1 and ComparePlayerStatus(11, 0, 9) == 1:
            return State_11
        if IsEquipmentIDEquipped(2, 137) == 1:
            return State_12
        else:
            return State_25


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=25000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_36
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        SetFlagState(flag=71400001, state=1)
        SetFlagState(flag=71400002, state=0)

    def test(self):
        return State_32


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        TalkToPlayer(conversation=25000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=11405020, state=1)

    def test(self):
        return State_25


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        SetFlagState(flag=71400002, state=1)
        SetFlagState(flag=71400001, state=0)

    def test(self):
        return State_32


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_13]

    def test(self):
        if IsEquipmentIDEquipped(2, 137) == 0:
            return State_214
        if GetFlagState(11406101) == 0 and GetFlagState(71400004) == 1:
            return State_52
        if GetFlagState(11406101) == 0 and GetFlagState(71400003) == 1:
            return State_50
        if GetFlagState(11406101) == 0 and GetFlagState(71400003) == 0:
            return State_22
        if GetFlagState(11406101) == 1:
            return State_54


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        SetFlagState(flag=11405020, state=0)

    def test(self):
        return State_32


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=25000600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_25, State_74]

    def enter(self):
        TalkToPlayer(conversation=25001200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_25
        if GetDistanceToPlayer() >= 8:
            return State_30


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_13]

    def test(self):
        if ComparePlayerStatus(11, 0, 9) == 1:
            return State_7
        if IsEquipmentIDEquipped(2, 137) == 1:
            return State_5
        else:
            return State_215


class State_45(State):
    """ 45: No description. """

    def enter(self):
        TalkToPlayer(conversation=-1, unk1=-1, unk2=-1)
        DebugEvent(message='誓約したあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_46(State):
    """ 46: No description. """

    def enter(self):
        TalkToPlayer(conversation=-1, unk1=-1, unk2=-1)
        DebugEvent(message='誓約しなかったあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=25000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71400012, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_48
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        SetFlagState(flag=71400000, state=1)

    def test(self):
        return State_25


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        SetFlagState(flag=71400003, state=1)
        SetFlagState(flag=11406101, state=1)

    def test(self):
        return State_23


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        TalkToPlayer(conversation=25001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=71400004, state=1)
        SetFlagState(flag=11406101, state=1)

    def test(self):
        return State_23


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        TalkToPlayer(conversation=25001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_53
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=71400005, state=1)
        SetFlagState(flag=11406101, state=1)

    def test(self):
        return State_23


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        TalkToPlayer(conversation=25001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        TalkToPlayer(conversation=25001020, unk1=-1, unk2=-1)
        SetFlagState(flag=71400009, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71400010, state=1)

    def test(self):
        return State_17


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        TalkToPlayer(conversation=25001040, unk1=-1, unk2=-1)
        SetFlagState(flag=71400010, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_74
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_13]

    def test(self):
        if GetStatus(10) <= 1:
            return State_65
        else:
            return State_59


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020205, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_61
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_60


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59, State_61]

    def enter(self):
        DebugEvent(message='人間性を捧げない')

    def test(self):
        return State_63


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        DebugEvent(message='DECIDE_NUMBER')
        OpenGenericDialog(unk1=3, text_id=10020205, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_2
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_62
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_60


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        DebugEvent(message='人間性を捧げた')
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)
        ChangePlayerStats(unk1=15, unk2=0, unk3=1)
        AddIzalithRankingPoints()
        SetFlagState(flag=849, state=1)

    def test(self):
        if DoesSelfHaveSpEffect(23, 30) == 1 and GetFlagState(11400598) == 0 and GetFlagState(849) == 0:
            return State_78
        if DoesSelfHaveSpEffect(23, 80) == 1 and GetFlagState(849) == 0:
            return State_216
        if DoesSelfHaveSpEffect(23, 100) == 1 and GetFlagState(71400011) == 0 and IsEquipmentIDEquipped(2, 137) == 1 and GetFlagState(849) == 0:
            return State_211
        if DoesSelfHaveSpEffect(23, 30) == 1 and GetFlagState(849) == 0:
            return State_216
        if DoesSelfHaveSpEffect(23, 10) == 1 and GetFlagState(849) == 0:
            return State_216
        if GetFlagState(849) == 0:
            return State_208
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_2


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_59, State_60, State_61, State_208, State_210]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000リストへ')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_23


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_206]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010795, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='これ以上捧げられない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8 or IsAttackedBySomeone() == 1:
            return State_69
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_68
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_68


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010785, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性がない\u3000リストから')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8 or IsAttackedBySomeone() == 1:
            return State_66
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_67
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_67


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_23


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_23


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_216]

    def enter(self):
        DebugEvent(message='人間性を捧げた会話')
        TalkToPlayer(conversation=25001700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30
        if HasTalkEnded() == 1:
            return State_209


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)
        ChangeMotionOffsetID(0)
        DebugEvent(message='向かって右')

    def test(self):
        return State_25


class State_72(State):
    """ 72: No description. """

    def enter(self):
        DisplayOneLineHelp(text_id=-1)


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_24, State_28, State_29, State_75, State_88]

    def enter(self):
        TalkToPlayer(conversation=25001200, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_25
        if GetDistanceToPlayer() >= 8:
            return State_30


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_20, State_55, State_57]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_43
        else:
            return State_25

    def exit(self):
        RemoveMyAggro()


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_6, State_7, State_59, State_61, State_64, State_65, State_207, State_208, State_209]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_73
        else:
            return State_25


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        SetFlagState(flag=11400596, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_25
        if IsMenuOpen(63) == 0:
            return State_207


class State_77(State):
    """ 77: No description. """

    def enter(self):
        SetFlagState(flag=11400597, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_25


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        SetFlagState(flag=11400598, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_25
        if IsMenuOpen(63) == 0:
            return State_216


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_82]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_25


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_103


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        DebugEvent(message='強化しない')

    def test(self):
        return State_79


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010890, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_80
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_82
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_82
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 390) == 1 and IsGenericDialogOpen() == 0:
            return State_89
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 391) == 1 and IsGenericDialogOpen() == 0:
            return State_105
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 392) == 1 and IsGenericDialogOpen() == 0:
            return State_121
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 393) == 1 and IsGenericDialogOpen() == 0:
            return State_137
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 394) == 1 and IsGenericDialogOpen() == 0:
            return State_153
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 395) == 1 and IsGenericDialogOpen() == 0:
            return State_169
        if GetGenericDialogButtonResult() == 1 and IsEquipmentIDObtained(3, 396) == 1 and IsGenericDialogOpen() == 0:
            return State_185


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010760, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_86
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_85
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_85


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_84]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_13]

    def test(self):
        if IsEquipmentIDObtained(3, 215) == 1 or IsEquipmentIDObtained(3, 214) == 1:
            return State_200
        if IsEquipmentIDObtained(3, 390) == 0 and IsEquipmentIDObtained(3, 391) == 0 and IsEquipmentIDObtained(3, 392) == 0 and IsEquipmentIDObtained(3, 393) == 0 and IsEquipmentIDObtained(3, 394) == 0 and IsEquipmentIDObtained(3, 395) == 0 and IsEquipmentIDObtained(3, 396) == 0:
            return State_84
        if IsEquipmentIDObtained(3, 390) == 1 or IsEquipmentIDObtained(3, 391) == 1 or IsEquipmentIDObtained(3, 392) == 1 or IsEquipmentIDObtained(3, 393) == 1 or IsEquipmentIDObtained(3, 394) == 1 or IsEquipmentIDObtained(3, 395) == 1 or IsEquipmentIDObtained(3, 396) == 1:
            return State_83


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_83, State_84, State_200, State_203]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and IsEquipmentIDEquipped(2, 137) == 1 and GetDistanceToPlayer() <= 8:
            return State_73
        else:
            return State_25


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 390, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_81
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_90
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_91
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_92
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_93
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_94
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_95
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_96
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_97
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_98
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_99
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_100
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_101
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_102


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_103


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_103


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_103


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_103


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_103


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_103


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_103


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_103


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_103


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_103


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_103


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_103


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_103


class State_103(State):
    """ 103: No description. """

    def previous_states(self):
        return [State_81, State_90, State_91, State_92, State_93, State_94, State_95, State_96, State_97, State_98, State_99, State_100, State_101, State_102]

    def test(self):
        return State_203


class State_104(State):
    """ 104: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_119


class State_105(State):
    """ 105: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 391, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_104
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_106
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_107
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_108
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_109
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_110
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_111
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_112
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_113
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_114
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_115
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_116
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_117
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_118


class State_106(State):
    """ 106: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_119


class State_107(State):
    """ 107: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_119


class State_108(State):
    """ 108: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_119


class State_109(State):
    """ 109: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_119


class State_110(State):
    """ 110: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_119


class State_111(State):
    """ 111: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_119


class State_112(State):
    """ 112: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_119


class State_113(State):
    """ 113: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_119


class State_114(State):
    """ 114: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_119


class State_115(State):
    """ 115: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_119


class State_116(State):
    """ 116: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_119


class State_117(State):
    """ 117: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_119


class State_118(State):
    """ 118: No description. """

    def previous_states(self):
        return [State_105]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_119


class State_119(State):
    """ 119: No description. """

    def previous_states(self):
        return [State_104, State_106, State_107, State_108, State_109, State_110, State_111, State_112, State_113, State_114, State_115, State_116, State_117, State_118]

    def test(self):
        return State_203


class State_120(State):
    """ 120: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_135


class State_121(State):
    """ 121: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 392, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_120
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_122
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_123
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_124
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_125
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_126
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_127
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_128
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_129
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_130
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_131
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_132
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_133
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_134


class State_122(State):
    """ 122: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_135


class State_123(State):
    """ 123: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_135


class State_124(State):
    """ 124: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_135


class State_125(State):
    """ 125: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_135


class State_126(State):
    """ 126: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_135


class State_127(State):
    """ 127: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_135


class State_128(State):
    """ 128: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_135


class State_129(State):
    """ 129: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_135


class State_130(State):
    """ 130: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_135


class State_131(State):
    """ 131: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_135


class State_132(State):
    """ 132: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_135


class State_133(State):
    """ 133: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_135


class State_134(State):
    """ 134: No description. """

    def previous_states(self):
        return [State_121]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_135


class State_135(State):
    """ 135: No description. """

    def previous_states(self):
        return [State_120, State_122, State_123, State_124, State_125, State_126, State_127, State_128, State_129, State_130, State_131, State_132, State_133, State_134]

    def test(self):
        return State_203


class State_136(State):
    """ 136: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_151


class State_137(State):
    """ 137: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 393, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_136
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_138
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_139
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_140
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_141
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_142
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_143
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_144
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_145
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_146
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_147
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_148
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_149
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_150


class State_138(State):
    """ 138: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_151


class State_139(State):
    """ 139: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_151


class State_140(State):
    """ 140: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_151


class State_141(State):
    """ 141: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_151


class State_142(State):
    """ 142: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_151


class State_143(State):
    """ 143: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_151


class State_144(State):
    """ 144: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_151


class State_145(State):
    """ 145: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_151


class State_146(State):
    """ 146: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_151


class State_147(State):
    """ 147: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_151


class State_148(State):
    """ 148: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_151


class State_149(State):
    """ 149: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_151


class State_150(State):
    """ 150: No description. """

    def previous_states(self):
        return [State_137]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_151


class State_151(State):
    """ 151: No description. """

    def previous_states(self):
        return [State_136, State_138, State_139, State_140, State_141, State_142, State_143, State_144, State_145, State_146, State_147, State_148, State_149, State_150]

    def test(self):
        return State_203


class State_152(State):
    """ 152: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_167


class State_153(State):
    """ 153: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 394, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_152
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_154
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_155
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_156
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_157
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_158
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_159
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_160
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_161
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_162
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_163
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_164
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_165
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_166


class State_154(State):
    """ 154: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_167


class State_155(State):
    """ 155: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_167


class State_156(State):
    """ 156: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_167


class State_157(State):
    """ 157: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_167


class State_158(State):
    """ 158: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_167


class State_159(State):
    """ 159: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_167


class State_160(State):
    """ 160: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_167


class State_161(State):
    """ 161: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_167


class State_162(State):
    """ 162: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_167


class State_163(State):
    """ 163: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_167


class State_164(State):
    """ 164: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_167


class State_165(State):
    """ 165: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_167


class State_166(State):
    """ 166: No description. """

    def previous_states(self):
        return [State_153]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_167


class State_167(State):
    """ 167: No description. """

    def previous_states(self):
        return [State_152, State_154, State_155, State_156, State_157, State_158, State_159, State_160, State_161, State_162, State_163, State_164, State_165, State_166]

    def test(self):
        return State_203


class State_168(State):
    """ 168: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_183


class State_169(State):
    """ 169: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 395, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_168
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_170
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_171
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_172
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_173
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_174
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_175
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_176
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_177
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_178
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_179
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_180
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_181
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_182


class State_170(State):
    """ 170: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_183


class State_171(State):
    """ 171: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_183


class State_172(State):
    """ 172: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_183


class State_173(State):
    """ 173: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_183


class State_174(State):
    """ 174: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_183


class State_175(State):
    """ 175: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_183


class State_176(State):
    """ 176: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_183


class State_177(State):
    """ 177: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_183


class State_178(State):
    """ 178: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_183


class State_179(State):
    """ 179: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_183


class State_180(State):
    """ 180: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_183


class State_181(State):
    """ 181: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_183


class State_182(State):
    """ 182: No description. """

    def previous_states(self):
        return [State_169]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_183


class State_183(State):
    """ 183: No description. """

    def previous_states(self):
        return [State_168, State_170, State_171, State_172, State_173, State_174, State_175, State_176, State_177, State_178, State_179, State_180, State_181, State_182]

    def test(self):
        return State_203


class State_184(State):
    """ 184: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(200, 202, 1)

    def test(self):
        return State_199


class State_185(State):
    """ 185: No description. """

    def previous_states(self):
        return [State_83]

    def enter(self):
        PlayerEquipmentQuantityChange(3, 396, -1)

    def test(self):
        if IsEquipmentIDObtained(3, 200) == 1:
            return State_184
        if IsEquipmentIDObtained(3, 201) == 1:
            return State_186
        if IsEquipmentIDObtained(3, 202) == 1:
            return State_187
        if IsEquipmentIDObtained(3, 203) == 1:
            return State_188
        if IsEquipmentIDObtained(3, 204) == 1:
            return State_189
        if IsEquipmentIDObtained(3, 205) == 1:
            return State_190
        if IsEquipmentIDObtained(3, 206) == 1:
            return State_191
        if IsEquipmentIDObtained(3, 207) == 1:
            return State_192
        if IsEquipmentIDObtained(3, 208) == 1:
            return State_193
        if IsEquipmentIDObtained(3, 209) == 1:
            return State_194
        if IsEquipmentIDObtained(3, 210) == 1:
            return State_195
        if IsEquipmentIDObtained(3, 211) == 1:
            return State_196
        if IsEquipmentIDObtained(3, 212) == 1:
            return State_197
        if IsEquipmentIDObtained(3, 213) == 1:
            return State_198


class State_186(State):
    """ 186: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(201, 203, 1)

    def test(self):
        return State_199


class State_187(State):
    """ 187: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(202, 204, 1)

    def test(self):
        return State_199


class State_188(State):
    """ 188: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(203, 205, 1)

    def test(self):
        return State_199


class State_189(State):
    """ 189: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(204, 206, 1)

    def test(self):
        return State_199


class State_190(State):
    """ 190: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(205, 207, 1)

    def test(self):
        return State_199


class State_191(State):
    """ 191: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(206, 208, 1)

    def test(self):
        return State_199


class State_192(State):
    """ 192: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(207, 209, 1)

    def test(self):
        return State_199


class State_193(State):
    """ 193: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(208, 210, 1)

    def test(self):
        return State_199


class State_194(State):
    """ 194: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(209, 211, 1)

    def test(self):
        return State_199


class State_195(State):
    """ 195: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(210, 212, 1)

    def test(self):
        return State_199


class State_196(State):
    """ 196: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(211, 213, 1)

    def test(self):
        return State_199


class State_197(State):
    """ 197: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(212, 214, 1)

    def test(self):
        return State_199


class State_198(State):
    """ 198: No description. """

    def previous_states(self):
        return [State_185]

    def enter(self):
        DebugEvent(message='強化する')
        ReplaceTool(213, 215, 1)

    def test(self):
        return State_199


class State_199(State):
    """ 199: No description. """

    def previous_states(self):
        return [State_184, State_186, State_187, State_188, State_189, State_190, State_191, State_192, State_193, State_194, State_195, State_196, State_197, State_198]

    def test(self):
        return State_203


class State_200(State):
    """ 200: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010762, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_202
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_201
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_201


class State_201(State):
    """ 201: No description. """

    def previous_states(self):
        return [State_200]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_202(State):
    """ 202: No description. """

    def previous_states(self):
        return [State_200]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_203(State):
    """ 203: No description. """

    def previous_states(self):
        return [State_103, State_119, State_135, State_151, State_167, State_183, State_199]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010891, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='エスト瓶強化しました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_88
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_205
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_204
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_204


class State_204(State):
    """ 204: No description. """

    def previous_states(self):
        return [State_203]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_23


class State_205(State):
    """ 205: No description. """

    def previous_states(self):
        return [State_203]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_25


class State_206(State):
    """ 206: No description. """

    def test(self):
        if ComparePlayerStatus(23, 0, 100) == 1:
            return State_64


class State_207(State):
    """ 207: No description. """

    def previous_states(self):
        return [State_3, State_76]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約を交わした')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_8
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_8


class State_208(State):
    """ 208: No description. """

    def previous_states(self):
        return [State_62]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010796, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ポイントアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_63
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_63


class State_209(State):
    """ 209: No description. """

    def previous_states(self):
        return [State_70, State_216]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010797, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ランクアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_9
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_210
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_210


class State_210(State):
    """ 210: No description. """

    def previous_states(self):
        return [State_209]

    def test(self):
        if DoesSelfHaveSpEffect(23, 100) == 1 and GetFlagState(71400011) == 0 and IsEquipmentIDEquipped(2, 137) == 1 and GetFlagState(849) == 0:
            return State_211
        else:
            return State_63


class State_211(State):
    """ 211: No description. """

    def previous_states(self):
        return [State_62, State_210]

    def enter(self):
        DebugEvent(message='人間性を捧げた最後')
        TalkToPlayer(conversation=25001800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_212
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_212(State):
    """ 212: No description. """

    def previous_states(self):
        return [State_211]

    def enter(self):
        SetFlagState(flag=71400011, state=1)

    def test(self):
        return State_23


class State_213(State):
    """ 213: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=25001900, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71400012, state=1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_214(State):
    """ 214: No description. """

    def previous_states(self):
        return [State_40]

    def enter(self):
        TalkToPlayer(conversation=25001900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_215(State):
    """ 215: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=25001900, unk1=-1, unk2=-1)
        DebugEvent(message='誓約結ぶ前会話')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_24
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_30


class State_216(State):
    """ 216: No description. """

    def previous_states(self):
        return [State_62, State_78]

    def test(self):
        if IsEquipmentIDEquipped(2, 137) == 1:
            return State_70
        else:
            return State_209
