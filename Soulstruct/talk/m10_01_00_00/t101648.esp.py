from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_3


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_3


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        DisplayOneLineHelp(text_id=10010220)

    def test(self):
        return State_3


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_0, State_1, State_2, State_47]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3 and (GetFlagState(853) == 1 or GetStatus(6) + GetStatus(13) + GetStatus(13) + GetStatus(13) + GetStatus(13) + GetStatus(13) > 25):
            return State_2
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3):
            return State_1
        if GetOneLineHelpStatus() == 1 and IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3:
            return State_10


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_7, State_10]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000360, required_flag=715)
        AddTalkListData(menu_index=3, menu_text=15000260, required_flag=853)
        AddTalkListData(menu_index=2, menu_text=15000200, required_flag=-1)
        AddTalkListData(menu_index=5, menu_text=15000350, required_flag=286)
        ShowShopMessage(0, 0, 0)
        AddTalkListData(menu_index=4, menu_text=15000005, required_flag=-1)
        SetFlagState(flag=71100095, state=1)

    def test(self):
        if GetTalkListEntryResult() == 0:
            return State_11
        if GetTalkListEntryResult() == 4:
            return State_11
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_9
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_9
        if GetTalkListEntryResult() == 2:
            return State_21
        if GetTalkListEntryResult() == 3:
            return State_30
        if GetTalkListEntryResult() == 1:
            return State_36
        if GetTalkListEntryResult() == 5:
            return State_37

    def exit(self):
        ClearTalkListData()


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_6, State_8, State_9]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_11


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_8, State_9]

    def test(self):
        if GetDistanceToPlayer() >= 12:
            return State_5
        else:
            return State_12


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_13, State_19, State_24, State_28, State_34, State_40, State_48]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_4
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 5:
        #     return State_11


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        CloseMenu()

    def test(self):
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_6
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_5
        else:
            return State_11


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_6
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_5


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_3]

    def enter(self):
        ForceCloseMenu()
        SetTalkTime(2.5)
        ClearTalkActionState()
        SetFlagState(flag=11015030, state=1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_4
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 5:
        #     return State_11


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_4, State_5, State_7, State_8, State_10, State_12, State_14, State_20, State_22, State_29, State_31, State_32, State_35, State_38]

    def enter(self):
        SetFlagState(flag=11015030, state=0)

    def test(self):
        return State_47


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        return State_11


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_7


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_15, State_17]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        DebugEvent(message='誓約を変更する')
        BreakCovenantPledge()
        ChangePlayerStats(unk1=11, unk2=5, unk3=3)
        SetFlagState(flag=844, state=1)

    def test(self):
        if GetFlagState(11010594) == 0 and GetFlagState(844) == 0:
            return State_31
        if GetFlagState(844) == 0:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_14


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        DebugEvent(message='誓約を変更しない')

    def test(self):
        return State_13


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010745, unk2=3, unk3=4, display_distance=2)
        ChangePlayerStats(unk1=31, unk2=5, unk3=3)
        RequestUnlockTrophy(10)

    def test(self):
        if IsMultiplayerInProgress() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_14
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_16
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_16
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_15


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010726, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が同じ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_20
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_19


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_18, State_42, State_45]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_7


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_18, State_42, State_45]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        if ComparePlayerStatus(11, 0, 3) == 1:
            return State_18
        if IsMultiplayerInProgress() == 1:
            return State_45
        else:
            return State_17


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_23, State_25, State_26]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DebugEvent(message='捧げる')
        ChangePlayerStats(unk1=15, unk2=0, unk3=1)
        PlayerEquipmentQuantityChange(3, 375, -1)
        SetFlagState(flag=844, state=1)

    def test(self):
        if DoesSelfHaveSpEffect(17, 10) == 1 and GetFlagState(11010595) == 0 and GetFlagState(844) == 0:
            return State_32
        if DoesSelfHaveSpEffect(17, 80) == 1 and GetFlagState(844) == 0:
            return State_44
        if DoesSelfHaveSpEffect(17, 30) == 1 and GetFlagState(844) == 0:
            return State_44
        if DoesSelfHaveSpEffect(17, 10) == 1 and GetFlagState(844) == 0:
            return State_44
        if GetFlagState(844) == 0:
            return State_43
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_22


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_25, State_26]

    def enter(self):
        DebugEvent(message='捧げない')

    def test(self):
        return State_7


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020200, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_22
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_24
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_26


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        OpenGenericDialog(unk1=3, text_id=10020200, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_22
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_24
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_24
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_23


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010780, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_29
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_27, State_43, State_44, State_46]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_7


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_27, State_43, State_44, State_46]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        if ComparePlayerStatus(17, 0, 100) == 1:
            return State_33
        if IsEquipmentIDObtained(3, 375) == 0:
            return State_27
        else:
            return State_25


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=11010594, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_11
        if IsMenuOpen(63) == 0:
            return State_42


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        SetFlagState(flag=11010595, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_11
        if IsMenuOpen(63) == 0:
            return State_44


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010790, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_35
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_34
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_34


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_7


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_33]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        return State_41


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9007, 1)
        AcquireGesture(7)
        SetFlagState(flag=286, state=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_8
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_8
        if IsMenuOpen(63) == 0:
            return State_46


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_39, State_41, State_48]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_11


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        DebugEvent(message='捧げる')
        PlayerEquipmentQuantityChange(3, 702, -1)
        SetFlagState(flag=844, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_38
        if GetFlagState(844) == 0:
            return State_48


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_41]

    def enter(self):
        DebugEvent(message='捧げない')

    def test(self):
        return State_7


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020300, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_38
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_40
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_40
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_39


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_15, State_31]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='誓約が変更されました')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_20
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_19


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010796, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ポイントアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_29
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_23, State_32]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010797, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ランクアップ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_29
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_17, State_21]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010747, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='マルチプレイ中')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_20
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_19


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_29
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_3


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        SetFlagState(flag=11010598, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_38
        if IsMenuOpen(63) == 0:
            return State_7
