from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_25


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2, State_3, State_25, State_38, State_41, State_48, State_54, State_56]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=10)

    def test(self):
        if CompareBonfireLevel(0, 0) == 1:
            return State_25
        if CompareBonfireState(0) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and GetOneLineHelpStatus() == 1:
            return State_3
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 3.4):
            return State_3
        if GetPlayerYDistance() > 1 and GetOneLineHelpStatus() == 1:
            return State_48
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and CompareBonfireState(1) == 1 and GetPlayerYDistance() < 1:
            return State_2
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 3.4 and GetOneLineHelpStatus() == 1 and CompareBonfireState(1) == 1:
            return State_46


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=10010183)

    def test(self):
        return State_1


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_1


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_19, State_20, State_RepairEquipment, State_30, State_31, State_AttuneMagic, State_37, State_38, State_42, State_43, State_44, State_45, State_46, State_ReinforceArmor, State_50, State_55, State_56, State_59, State_60, State_61, State_62]

    def enter(self):
        ShowShopMessage(0, 0, 0)
        DebugEvent(message='篝火リスト')
        RequestSave(0)
        AddTalkListData(menu_index=1, menu_text=15000270, required_flag=-1)  # Reverse Hollowing
        AddTalkListData(menu_index=2, menu_text=15000170, required_flag=-1)  # Kindle
        AddTalkListData(menu_index=3, menu_text=15000130, required_flag=-1)  # Attune Magic
        AddTalkListData(menu_index=4, menu_text=15000190, required_flag=-1)  # Modify
        AddTalkListData(menu_index=5, menu_text=15000112, required_flag=-1)  # Reinforce Armor
        AddTalkListData(menu_index=6, menu_text=15000120, required_flag=-1)  # Repair Equipment
        AddTalkListData(menu_index=7, menu_text=15000185, required_flag=-1)  # Shop
        AddTalkListData(menu_index=8, menu_text=15000005, required_flag=-1)  # Leave

    def test(self):
        if CompareBonfireState(0) == 1 or IsPlayerDead() == 1:
            return State_InterruptTalkMenu
        if HasPlayerBeenAttacked() == 1:
            return State_InterruptTalkMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if GetTalkListEntryResult() == 0:
            return State_LeaveBonfire
        if GetTalkListEntryResult() == 1:
            return State_ReverseHollowing
        if GetTalkListEntryResult() == 2:
            return State_Kindle
        if GetTalkListEntryResult() == 3:
            return State_AttuneMagic
        if GetTalkListEntryResult() == 5:
            return State_ReinforceArmor
        if GetTalkListEntryResult() == 6:
            return State_RepairEquipment
        if GetTalkListEntryResult() == 7:
            return State_OpenShop
        if GetTalkListEntryResult() == 8:
            return State_LeaveBonfire

    def exit(self):
        ClearTalkListData()


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        Command_talk_1_72()
        DebugEvent(message='Open_covenant_menu')

    def test(self):
        if CheckActionButtonArea() == 1:
            return State_6
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(180) == 0:
            return State_4


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        ForceCloseMenu()

    def test(self):
        if GetFlagState(4084) == 1:
            return State_7


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_6]

    def enter(self):
        Command_talk_1_75()

    def test(self):
        if CheckSpecificPersonMenuIsOpen() == 0:
            return State_8


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_7]

    def test(self):
        if ComparePlayerStatus(11, 0, 8) == 1 and (GetFlagState(11510596) == 0 or GetFlagState(11510580) == 0):
            return State_9
        if ComparePlayerStatus(11, 0, 9) == 1 and GetFlagState(11400596) == 0:
            return State_10
        if ComparePlayerStatus(11, 0, 4) == 1 and GetFlagState(11600594) == 0:
            return State_11
        if ComparePlayerStatus(11, 0, 7) == 1 and GetFlagState(11200592) == 0:
            return State_12
        if ComparePlayerStatus(11, 0, 6) == 1 and (GetFlagState(11310592) == 0 or GetFlagState(11310580) == 0):
            return State_13
        if ComparePlayerStatus(11, 0, 5) == 1 and GetFlagState(11320581) == 0:
            return State_14
        if ComparePlayerStatus(11, 0, 2) == 1:
            return State_15
        if ComparePlayerStatus(11, 0, 3) == 1 and GetFlagState(11010594) == 0:
            return State_16
        else:
            return State_18


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11510596, state=1)
        SetFlagState(flag=11510580, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11400596, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11600594, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71200047, state=1)
        SetFlagState(flag=11200592, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11310592, state=1)
        SetFlagState(flag=11310580, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11320592, state=1)
        SetFlagState(flag=11320581, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11510595, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=11010594, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_17(State):
    """ 17: No description. """

    def enter(self):
        SetFlagState(flag=11010594, state=1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if IsMenuOpen(63) == 0:
            return State_18


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_8, State_9, State_10, State_11, State_12, State_13, State_14, State_15, State_16, State_17]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_InterruptTalkMenu
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_19


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()
        SetFlagState(flag=760, state=0)

    def test(self):
        return State_4


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenSoul()
        DebugEvent(message='ソウルショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(23) == 0:
            return State_4


class State_InterruptTalkMenu(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_4, State_9, State_10, State_11, State_12, State_13, State_14, State_15, State_16, State_17, State_18, State_LeaveBonfire, State_46, State_49]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_41


class State_LeaveBonfire(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_InterruptTalkMenu


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000最初')

    def test(self):
        return State_25


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DebugEvent(message='人間性を捧げた')
        OfferHumanity()
        RequestUnlockTrophy(26)

    def test(self):
        return State_23


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_0, State_1, State_23, State_27, State_28]

    def enter(self):
        DebugEvent(message='最初')

    def test(self):
        if GetOneLineHelpStatus() == 1 and CompareBonfireState(0) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2:
            return State_27
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_27
        if CompareBonfireLevel(2, 0) == 1 and CompareBonfireState(1) == 1:
            return State_1
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and CompareBonfireState(1) == 1:
            return State_28
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and CompareBonfireState(1) == 1:
            return State_26


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_24


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

    def previous_states(self):
        return [State_25]

    def enter(self):
        DisplayOneLineHelp(text_id=10010182)

    def test(self):
        return State_25


class State_RepairEquipment(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenRepairShop()
        DebugEvent(message='修理ショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(12) == 0:
            return State_4


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenEnhanceShop(category=0)
        DebugEvent(message='武器強化')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(13) == 0:
            return State_4


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        StartWarpMenuInit()
        DebugEvent(message='ワープメニューを開く')

    def test(self):
        if WasWarpMenuDestinationSelected() == 1:
            return State_63
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(36) == 0:
            return State_4


class State_Kindle(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if GetPlayerChrType() == 8:
            return State_65
        if GetStatus(10) <= 1:
            return State_40
        if CompareBonfireLevel(0, 4) == 1:
            return State_39
        if CompareBonfireLevel(0, 2) == 1 and GetFlagState(257) == 0:
            return State_64
        else:
            return State_34


class State_AttuneMagic(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenMagicEquip(first_id=10000, last_id=10499)
        DebugEvent(message='魔法装備ショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(25) == 0:
            return State_4


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_Kindle]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010741, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_37
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_36
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_35


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='人間性を捧げない')

    def test(self):
        return State_38


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='人間性を捧げた')
        SetFlagState(flag=760, state=1)
        OfferHumanity()

    def test(self):
        return State_38


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_34, State_35, State_36]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000リストへ')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        if GetFlagState(760) == 0:
            return State_4
        if GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_1


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_Kindle]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010723, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='これ以上捧げられない\u3000解放後')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_45
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_44
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_44


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_Kindle]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010722, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性がない\u3000リストから')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_42
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_43
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_43


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_InterruptTalkMenu, State_63]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマーをクリア\u3000待機へ')

    def test(self):
        return State_1


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_40, State_65]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_40, State_65]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_39, State_64]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_39, State_64]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        StartBonfireAnimLoop()
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()
        SetFlagState(flag=760, state=0)

    def test(self):
        if CompareBonfireState(0) == 1:
            return State_InterruptTalkMenu
        if GetDistanceToPlayer() >= 8 or GetPlayerYDistance() > 1:
            return State_InterruptTalkMenu
        if CompareBonfireState(1) == 1:
            return State_4


class State_ReinforceArmor(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenEnhanceShop(category=10)
        DebugEvent(message='防具強化')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(13) == 0:
            return State_4


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_1


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_5, State_20, State_RepairEquipment, State_30, State_31, State_Kindle, State_AttuneMagic, State_ReinforceArmor, State_50, State_ReverseHollowing, State_67]

    def enter(self):
        CloseMenu()
        DebugEvent(message='メッセージボックス閉じる')
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_InterruptTalkMenu


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        DebugEvent(message='倉庫')
        OpenRepository()

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(26) == 0:
            return State_4


class State_ReverseHollowing(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        DebugEvent(message='亡者から復活する')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if GetFlagState(751) == 1:
            return State_68
        if GetPlayerChrType() == 0:
            return State_57
        if GetStatus(10) <= 1:
            return State_58
        else:
            return State_52


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_ReverseHollowing]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010732, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_55
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_53
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_66
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_53


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        DebugEvent(message='人間性を捧げない')

    def test(self):
        return State_56


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        DebugEvent(message='人間性を捧げた')
        PlayerRespawn()
        DisplayBanner(banner_type=3)
        GiveSpEffectToPlayer(speffect=25)
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)

    def test(self):
        if IsPlayerDead() == 1:
            return State_55
        if GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_1
        if IsMenuOpen(53) == 0 and GetFlagState(764) == 0:
            return State_56


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_52, State_54, State_66]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_53, State_54]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000リストへ')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
        #     return State_1


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_ReverseHollowing]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010730, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='亡者ではない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_62
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_61
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_61


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_ReverseHollowing]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010731, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性がない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_59
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_60
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_60


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58, State_67, State_68]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_58, State_67, State_68]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_31]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')

    def test(self):
        return State_41


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_Kindle]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010724, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='これ以上捧げられない\u3000解放前')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_45
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_44
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_44


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_Kindle]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010725, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='亡者のときは注ぎ火できない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_42
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_42
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_43
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_43


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        SetFlagState(flag=762, state=1)
        SetFlagState(flag=764, state=1)

    def test(self):
        if IsPlayerDead() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_55
        if GetFlagState(762) == 0:
            return State_54


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010712, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ワープできない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_59
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_60
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_60


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_ReverseHollowing]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010736, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='呪われている')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_59
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_59
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_60
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_60


class State_OpenShop(State):
    """ 69: No description. """

    def test(self):
        return State_OpenShopReal


class State_OpenShopReal(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_OpenShop]

    def enter(self):
        OpenRegularShop(9000, 9099)  # Bonfire range.

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8 or GetPlayerYDistance() > 1:
            return State_49
        if IsMenuOpen(11) == 0:
            return State_4
