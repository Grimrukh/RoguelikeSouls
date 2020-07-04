from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_40


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        SetFlagState(flag=11815020, state=0)

    def test(self):
        return State_28


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        SetFlagState(flag=11815020, state=1)

    def test(self):
        return State_19


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_24, State_25]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_24, State_25, State_42]

    def enter(self):
        TalkToPlayer(conversation=32000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if GetDistanceToPlayer() >= 12:
            return State_4
        if HasTalkEnded() == 1:
            return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71810009, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=32000700, unk1=-1, unk2=-1)
        SetFlagState(flag=71810009, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_26


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_72]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_19


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_11
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_10]

    def enter(self):
        SetFlagState(flag=71810000, state=1)

    def test(self):
        return State_19


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=32001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_22]

    def test(self):
        if GetFlagState(71810014) == 1 and GetFlagState(71810015) == 0:
            return State_15
        if GetFlagState(1110) == 0 and GetFlagState(71810013) == 1 and GetFlagState(71810014) == 0:
            return State_14
        else:
            return State_12


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=32001700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26
        if HasTalkEnded() == 1:
            return State_61


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_13]

    def enter(self):
        TalkToPlayer(conversation=32001800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26
        if HasTalkEnded() == 1:
            return State_62


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71810013, state=1)

    def test(self):
        return State_17


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16, State_61, State_62]

    def test(self):
        return State_22
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 6:
        #     return State_19


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_2, State_5, State_10, State_12, State_14, State_15, State_29, State_33, State_36, State_45, State_47, State_48, State_51, State_53, State_54, State_55, State_57, State_59, State_63]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 6:
            return State_74
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 6 and GetFlagState(71810009) == 0 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1381) == 1:
            return State_9
        if GetFlagState(71810012) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 6:
            return State_73
        if GetFlagState(71810012) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_3, State_4, State_8, State_11, State_17, State_20, State_21, State_24, State_27, State_28, State_31, State_33, State_36, State_37, State_40, State_74, State_76]

    def enter(self):
        DebugEvent(message='待機')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1382) == 0 and GetDistanceToPlayer() <= 6:
            return State_37
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(11815020) == 1:
            return State_2
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71810000) == 0:
            return State_10
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71810000) == 1 and GetFlagState(71810001) == 0:
            return State_55
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 806) == 1:
            return State_45
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 807) == 1:
            return State_51
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 800) == 1 and GetFlagState(71810016) == 0:
            return State_64
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 801) == 1 and GetFlagState(71810017) == 0:
            return State_65
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 802) == 1 and GetFlagState(71810018) == 0:
            return State_66
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 808) == 1 and GetFlagState(71810019) == 0:
            return State_67
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 809) == 1 and GetFlagState(71810020) == 0:
            return State_68
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 810) == 1 and GetFlagState(71810021) == 0:
            return State_69
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 812) == 1 and GetFlagState(71810022) == 0:
            return State_70
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 813) == 1 and GetFlagState(71810023) == 0:
            return State_71
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71810003) == 0 and GetFlagState(71810002) == 1 and GetFlagState(71810001) == 1:
            return State_59
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetOneLineHelpStatus() == 1 and GetFlagState(71810002) == 0 and GetFlagState(71810001) == 1:
            return State_57
        if IsAttackedBySomeone() == 1 and GetFlagState(1382) == 0:
            return State_29
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 4 and GetFlagState(1381) == 0 and GetFlagState(1382) == 0:
            return State_20
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 4):
            return State_21


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_19


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_19


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_17, State_23, State_28, State_32, State_38, State_39, State_78]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000190, required_flag=-1)
        AddTalkListData(menu_index=2, menu_text=15000111, required_flag=-1)
        AddTalkListData(menu_index=3, menu_text=15000112, required_flag=-1)
        AddTalkListData(menu_index=4, menu_text=15000120, required_flag=-1)
        AddTalkListData(menu_index=7, menu_text=15000010, required_flag=-1)
        AddTalkListData(menu_index=5, menu_text=15000000, required_flag=-1)
        AddTalkListData(menu_index=6, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if GetTalkListEntryResult() == 6:
            return State_30
        if GetTalkListEntryResult() == 4:
            return State_23
        if GetTalkListEntryResult() == 2:
            DebugEvent(message='強化ショップが呼ばれる')
            return State_38
        if GetTalkListEntryResult() == 0:
            return State_30
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_25
        if GetTalkListEntryResult() == 5:
            return State_13
        if GetTalkListEntryResult() == 1:
            return State_32
        if GetTalkListEntryResult() == 3:
            return State_39
        if GetTalkListEntryResult() == 7:
            return State_77

    def exit(self):
        ClearTalkListData()


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        OpenRepairShop()

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_24
        if IsMenuOpen(12) == 0:
            return State_22


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23, State_32, State_38, State_39, State_78]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 6:
            return State_74
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4
        else:
            return State_19


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 6:
            return State_74
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_2, State_7, State_10, State_12, State_14, State_15, State_33, State_36, State_37, State_45, State_47, State_48, State_51, State_53, State_54, State_55, State_57, State_59, State_63, State_73, State_74]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_27


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_19


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_1, State_41, State_56, State_58, State_60]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_22
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 6:
        #     return State_19


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_18


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_22]

    def test(self):
        if DidYouDoSomethingInTheMenu(12) == 1 or DidYouDoSomethingInTheMenu(2) == 1 or DidYouDoSomethingInTheMenu(3) == 1 or DidYouDoSomethingInTheMenu(4) == 1:
            return State_34
        if DidYouDoSomethingInTheMenu(12) == 0 or DidYouDoSomethingInTheMenu(2) == 0 or DidYouDoSomethingInTheMenu(3) == 0 or DidYouDoSomethingInTheMenu(4) == 0:
            return State_35
        else:
            return State_31


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_19


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        CombineMenuFlagAndEventFlag(355, 336)
        CombineMenuFlagAndEventFlag(356, 337)
        CombineMenuFlagAndEventFlag(357, 338)
        CombineMenuFlagAndEventFlag(367, 346)
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_24
        if IsMenuOpen(13) == 0:
            return State_22


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_35]

    def enter(self):
        TalkToPlayer(conversation=32000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_36


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_33


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        TalkToPlayer(conversation=32000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_19
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_19, State_75]

    def enter(self):
        TalkToPlayer(conversation=32000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 6:
            return State_26


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        OpenEnhanceShop(category=0)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_24
        if IsMenuOpen(13) == 0:
            return State_22


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        OpenEnhanceShop(category=10)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_24
        if IsMenuOpen(13) == 0:
            return State_22


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=355, state=1)
        SetFlagState(flag=367, state=1)

    def test(self):
        return State_19


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_47, State_48, State_53, State_54, State_63]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_28


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_46, State_52]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_5


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DebugEvent(message='アイテムを渡す1')
        SetFlagState(flag=356, state=1)

    def test(self):
        return State_47


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        DebugEvent(message='アイテムを渡さない1')

    def test(self):
        return State_48


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000900, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_46
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020016, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_76
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_43
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_44
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_42


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        TalkToPlayer(conversation=32001100, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_44]

    def enter(self):
        TalkToPlayer(conversation=32001000, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        DebugEvent(message='アイテムを渡す2')
        SetFlagState(flag=357, state=1)

    def test(self):
        return State_53


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        DebugEvent(message='アイテムを渡さない2')

    def test(self):
        return State_54


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32001200, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話2')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_52
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_51]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020017, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_76
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_49
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_50
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_42


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        TalkToPlayer(conversation=32001400, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        TalkToPlayer(conversation=32001300, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000020, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_56
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        SetFlagState(flag=71810001, state=1)

    def test(self):
        return State_28


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_57]

    def enter(self):
        SetFlagState(flag=71810002, state=1)
        SetFlagState(flag=71810003, state=0)

    def test(self):
        return State_28


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=32000150, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_60
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71810003, state=1)
        SetFlagState(flag=71810002, state=0)

    def test(self):
        return State_28


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        SetFlagState(flag=71810014, state=1)

    def test(self):
        return State_17


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71810015, state=1)

    def test(self):
        return State_17


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_64, State_65, State_66, State_67, State_68, State_69, State_70, State_71]

    def enter(self):
        TalkToPlayer(conversation=32001500, unk1=-1, unk2=-1)
        DebugEvent(message='だれかの転職アイテム持ってた会話')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_18
        if HasTalkEnded() == 1:
            return State_41
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_26


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810016, state=1)

    def test(self):
        return State_63


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810017, state=1)

    def test(self):
        return State_63


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810018, state=1)

    def test(self):
        return State_63


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810019, state=1)

    def test(self):
        return State_63


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810020, state=1)

    def test(self):
        return State_63


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810021, state=1)

    def test(self):
        return State_63


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810022, state=1)

    def test(self):
        return State_63


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71810023, state=1)

    def test(self):
        return State_63


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_73]

    def enter(self):
        SetFlagState(flag=71810012, state=1)

    def test(self):
        return State_8


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=32000660, unk1=-1, unk2=-1)
        SetFlagState(flag=71810012, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_75
        if HasTalkEnded() == 1:
            return State_72
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 8:
            return State_26


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_18, State_24, State_25, State_76]

    def enter(self):
        TalkToPlayer(conversation=32000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_19
        if GetDistanceToPlayer() >= 6:
            return State_26


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_7, State_73]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 6:
            return State_37

    def exit(self):
        RemoveMyAggro()


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_46, State_52]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_74
        else:
            return State_19


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_22]

    def test(self):
        return State_78


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_77]

    def enter(self):
        OpenRegularShop(2100, 2199)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_24
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 6:
            return State_24
        if IsMenuOpen(11) == 0:
            return State_22
