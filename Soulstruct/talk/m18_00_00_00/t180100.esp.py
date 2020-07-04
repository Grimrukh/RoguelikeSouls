from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_15


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2, State_3, State_15, State_24, State_26, State_31, State_39, State_41]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=10)

    def test(self):
        if CompareBonfireState(0) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4:
            return State_3
        if CompareBonfireLevel(0, 0) == 1:
            return State_15
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 4):
            return State_3
        if GetPlayerYDistance() > 2 and GetOneLineHelpStatus() == 1:
            return State_31
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and CompareBonfireState(1) == 1 and GetPlayerYDistance() < 2:
            return State_2
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and CompareBonfireState(1) == 1:
            return State_29


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=10010106)

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
        return [State_5, State_9, State_10, State_19, State_20, State_21, State_22, State_24, State_27, State_28, State_29, State_30, State_33, State_40, State_41, State_44, State_45, State_46, State_47]

    def enter(self):
        ShowShopMessage(0, 0, 0)
        DebugEvent(message='篝火リスト')
        RequestSave(0)
        AddTalkListData(menu_index=9, menu_text=15000005, required_flag=-1)
        AddTalkListData(menu_index=6, menu_text=15000175, required_flag=702)
        AddTalkListData(menu_index=1, menu_text=15000100, required_flag=11810000)
        AddTalkListData(menu_index=2, menu_text=15000111, required_flag=250)
        AddTalkListData(menu_index=3, menu_text=15000112, required_flag=251)
        AddTalkListData(menu_index=4, menu_text=15000120, required_flag=252)
        AddTalkListData(menu_index=5, menu_text=15000130, required_flag=719)
        AddTalkListData(menu_index=10, menu_text=15000220, required_flag=258)
        AddTalkListData(menu_index=7, menu_text=15000150, required_flag=710)
        AddTalkListData(menu_index=8, menu_text=10010744, required_flag=69696969)
        AddTalkListData(menu_index=11, menu_text=15000270, required_flag=11810000)

    def test(self):
        if CompareBonfireState(0) == 1 or IsPlayerDead() == 1:
            return State_11
        if HasPlayerBeenAttacked() == 1:
            return State_11
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_11
        if GetTalkListEntryResult() == 0:
            return State_12
        if GetTalkListEntryResult() == 1:
            return State_10
        if GetTalkListEntryResult() == 2:
            return State_20
        if GetTalkListEntryResult() == 4:
            return State_19
        if GetTalkListEntryResult() == 7:
            return State_21
        if GetTalkListEntryResult() == 10:
            return State_33
        if GetTalkListEntryResult() == 5:
            return State_22
        if GetTalkListEntryResult() == 3:
            return State_30
        if GetTalkListEntryResult() == 9:
            return State_12
        if GetTalkListEntryResult() == 6:
            return State_35
        if GetTalkListEntryResult() == 11:
            return State_36
        if GetTalkListEntryResult() == 8:
            return State_5

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
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
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

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010729, unk2=1, unk3=0, display_distance=2)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 180 or GetDistanceToPlayer() > 8:
            return State_11
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_9
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_9


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()
        SetFlagState(flag=760, state=0)

    def test(self):
        return State_4


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenSoul()
        DebugEvent(message='ソウルショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(23) == 0:
            return State_4


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_4, State_8, State_12, State_29, State_32]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_26


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_4, State_24]

    def enter(self):
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_11


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_14, State_34]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000最初')

    def test(self):
        return State_15


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        DebugEvent(message='人間性を捧げた')
        OfferHumanity()

    def test(self):
        if GetFlagState(270) == 0:
            return State_34
        else:
            return State_13


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_0, State_1, State_13, State_17, State_18]

    def enter(self):
        DebugEvent(message='最初')

    def test(self):
        if GetOneLineHelpStatus() == 1 and CompareBonfireState(0) == 1 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2:
            return State_17
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_17
        if CompareBonfireLevel(2, 0) == 1 and CompareBonfireState(1) == 1:
            return State_1
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and CompareBonfireState(1) == 1:
            return State_18
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and CompareBonfireState(1) == 1:
            return State_16


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_14


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
        return [State_15]

    def enter(self):
        DisplayOneLineHelp(text_id=10010106)

    def test(self):
        return State_15


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenRepairShop()
        DebugEvent(message='修理ショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(12) == 0:
            return State_4


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenEnhanceShop(category=0)
        DebugEvent(message='武器強化')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(13) == 0:
            return State_4


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        StartWarpMenuInit()
        DebugEvent(message='ワープメニューを開く')

    def test(self):
        if WasWarpMenuDestinationSelected() == 1:
            return State_48
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(36) == 0:
            return State_4


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenMagicEquip(first_id=10000, last_id=10499)
        DebugEvent(message='魔法装備ショップ')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(25) == 0:
            return State_4


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        DebugEvent(message='王のソウルを捧げた')
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        SetFlagState(flag=756, state=1)

    def test(self):
        return State_24


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000リストへ')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        if GetFlagState(756) == 0 and GetFlagState(11800211) == 0:
            return State_4
        if GetFlagState(11800211) == 1:
            return State_12
        if GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1 or IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_1


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        OpenGenericDialog(unk1=1, text_id=10010171, unk2=1, unk3=0, display_distance=1)
        DebugEvent(message='王のソウルがない\u3000リストから')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_27
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_28
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_28


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_11, State_48]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマーをクリア\u3000待機へ')

    def test(self):
        return State_1


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        StartBonfireAnimLoop()
        ClearTalkActionState()
        DisplayOneLineHelp(text_id=-1)
        ClearPlayerDamageInfo()

    def test(self):
        if CompareBonfireState(0) == 1:
            return State_11
        if GetDistanceToPlayer() >= 8 or GetPlayerYDistance() > 2:
            return State_11
        if CompareBonfireState(1) == 1:
            return State_4


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        OpenEnhanceShop(category=10)
        DebugEvent(message='防具強化')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(13) == 0:
            return State_4


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_1]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_1


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_5, State_10, State_19, State_20, State_21, State_22, State_30, State_33, State_35, State_36]

    def enter(self):
        CloseMenu()
        DebugEvent(message='メッセージボックス閉じる')
        EndBonfireKindleAnimLoop()

    def test(self):
        return State_11


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        DebugEvent(message='倉庫')
        OpenRepository()

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetDistanceToPlayer() >= 8 and GetPlayerYDistance() > 2:
            return State_32
        if IsMenuOpen(26) == 0:
            return State_4


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=270, state=1)
        RequestUnlockTrophy(26)

    def test(self):
        return State_13


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_4]

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if IsEquipmentIDObtained(3, 2500) == 0 and IsEquipmentIDObtained(3, 2501) == 0 and IsEquipmentIDObtained(3, 2502) == 0 and IsEquipmentIDObtained(3, 2503) == 0:
            return State_25
        if GetFlagState(4084) == 1:
            return State_23


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_4]

    def enter(self):
        DebugEvent(message='亡者から復活する')

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1:
            return State_32
        if GetFlagState(751) == 1:
            return State_50
        if GetPlayerChrType() == 0:
            return State_42
        if GetStatus(10) <= 1:
            return State_43
        else:
            return State_37


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10010732, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_40
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_38
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_49
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_38


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        DebugEvent(message='人間性を捧げない')

    def test(self):
        return State_41


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        DebugEvent(message='人間性を捧げた')
        PlayerRespawn()
        DisplayBanner(banner_type=3)
        GiveSpEffectToPlayer(speffect=25)
        ChangePlayerStats(unk1=10, unk2=1, unk3=1)

    def test(self):
        if IsPlayerDead() == 1:
            return State_40
        if GetDistanceToPlayer() >= 8 or HasPlayerBeenAttacked() == 1:
            return State_1
        if IsMenuOpen(53) == 0 and GetFlagState(764) == 0:
            return State_41


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_37, State_39, State_49]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_38, State_39]

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


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010730, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='亡者ではない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_47
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_47
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_46
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_46


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010731, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='人間性がない')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_44
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_45


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_43, State_50]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_43, State_50]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア')
        ClearTalkActionState()
        ForceCloseGenericDialog()

    def test(self):
        return State_4


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_4


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_21]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()
        DebugEvent(message='リスト強制開放')

    def test(self):
        return State_26


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_37]

    def enter(self):
        SetFlagState(flag=762, state=1)
        SetFlagState(flag=764, state=1)

    def test(self):
        if IsPlayerDead() == 1:
            return State_40
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_40
        if GetFlagState(762) == 0:
            return State_39


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010736, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='呪われている')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CompareBonfireState(0) == 1 or HasPlayerBeenAttacked() == 1 or IsPlayerDead() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_44
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_45
