from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_44


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        SetFlagState(flag=11515020, state=0)

    def test(self):
        return State_23


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(conversation=31000500, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        SetFlagState(flag=11515020, state=1)

    def test(self):
        return State_23


class State_4(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_28, State_29]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_23


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_28, State_29, State_46]

    def enter(self):
        TalkToPlayer(conversation=31000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if GetDistanceToPlayer() >= 20:
            return State_4
        if HasTalkEnded() == 1:
            return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71510009, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        TalkToPlayer(conversation=31000700, unk1=-1, unk2=-1)
        SetFlagState(flag=71510009, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_61
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_30


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_10, State_58]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_23


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        SetFlagState(flag=71510008, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        TalkToPlayer(conversation=31000600, unk1=-1, unk2=-1)
        SetFlagState(flag=71510008, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_61
        if HasTalkEnded() == 1:
            return State_10
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(conversation=31000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(conversation=31000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_32
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71510000, state=1)

    def test(self):
        return State_32


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=31001200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_26]

    def test(self):
        if GetFlagState(10) == 1 and GetFlagState(71510005) == 0:
            return State_56
        if GetFlagState(12) == 1 and GetFlagState(71510004) == 0:
            return State_19
        if GetFlagState(71510002) == 1:
            return State_18
        if GetFlagState(71510002) == 0 and GetFlagState(71510001) == 1:
            return State_17
        if GetFlagState(71510001) == 0:
            return State_15


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=31001300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30
        if HasTalkEnded() == 1:
            return State_53


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=31001400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30
        if HasTalkEnded() == 1:
            return State_54


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=31001500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30
        if HasTalkEnded() == 1:
            return State_55


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71510001, state=1)

    def test(self):
        return State_21


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_20, State_53, State_54, State_55, State_57]

    def test(self):
        return State_26
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 7:
        #     return State_23


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_2, State_5, State_12, State_13, State_15, State_17, State_18, State_19, State_33, State_37, State_40, State_49, State_51, State_52, State_56]

    def enter(self):
        ClearTalkProgressData()
        ForceEndTalk(unk1=3)

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_60
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 10 and GetFlagState(71510009) == 0 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1361) == 1:
            return State_9
        if GetFlagState(71510010) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 10 and GetFlagState(71510008) == 1:
            return State_59
        if GetFlagState(71510008) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 10:
            return State_11
        if GetFlagState(71510010) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_1, State_3, State_4, State_8, State_21, State_24, State_25, State_28, State_31, State_32, State_35, State_37, State_40, State_41, State_44, State_60, State_62, State_63]

    def enter(self):
        DebugEvent(message='待機')
        SetUpdateDistance(distance=25)

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1362) == 0 and GetDistanceToPlayer() <= 7:
            return State_41
        if GetFlagState(1361) == 1 and IsPlayerDead() == 1 and GetDistanceToPlayer() <= 15 and GetFlagState(71510011) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 15:
            return State_63
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(11515020) == 1:
            return State_2
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71510000) == 0:
            return State_12
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and IsEquipmentIDObtained(3, 802) == 1:
            return State_49
        if IsAttackedBySomeone() == 1 and GetFlagState(1362) == 0:
            return State_33
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetFlagState(1361) == 0 and GetFlagState(1362) == 0:
            return State_24
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 5):
            return State_25
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 5 and GetOneLineHelpStatus() == 1 and GetFlagState(71510000) == 1:
            return State_13


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_23


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_23


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_21, State_27, State_32, State_36, State_42, State_43, State_64]

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
            return State_29
        if GetTalkListEntryResult() == 6:
            return State_34
        if GetTalkListEntryResult() == 4:
            return State_27
        if GetTalkListEntryResult() == 2:
            DebugEvent(message='強化ショップが呼ばれる')
            return State_42
        if GetTalkListEntryResult() == 0:
            return State_34
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_29
        if GetTalkListEntryResult() == 5:
            return State_16
        if GetTalkListEntryResult() == 1:
            return State_36
        if GetTalkListEntryResult() == 3:
            return State_43
        if GetTalkListEntryResult() == 7:
            return State_64

    def exit(self):
        ClearTalkListData()


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        OpenRepairShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_28
        if IsMenuOpen(12) == 0:
            return State_26


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_27, State_36, State_42, State_43, State_64]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_60
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4
        else:
            return State_23


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_60
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_4


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_2, State_7, State_11, State_12, State_13, State_15, State_17, State_18, State_19, State_37, State_40, State_41, State_49, State_51, State_52, State_56, State_59, State_60]

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
        return State_23


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_13, State_14, State_45]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_26
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 7:
        #     return State_23


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_22


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_26]

    def test(self):
        if DidYouDoSomethingInTheMenu(12) == 1 or DidYouDoSomethingInTheMenu(2) == 1 or DidYouDoSomethingInTheMenu(3) == 1 or DidYouDoSomethingInTheMenu(4) == 1:
            return State_38
        if DidYouDoSomethingInTheMenu(12) == 0 or DidYouDoSomethingInTheMenu(2) == 0 or DidYouDoSomethingInTheMenu(3) == 0 or DidYouDoSomethingInTheMenu(4) == 0:
            return State_39
        else:
            return State_35


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_23


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        CombineMenuFlagAndEventFlag(352, 333)
        CombineMenuFlagAndEventFlag(353, 334)
        CombineMenuFlagAndEventFlag(364, 345)
        CombineMenuFlagAndEventFlag(367, 346)
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_28
        if IsMenuOpen(13) == 0:
            return State_26


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_39]

    def enter(self):
        TalkToPlayer(conversation=31000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_40


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_37


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        TalkToPlayer(conversation=31000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_23, State_61]

    def enter(self):
        TalkToPlayer(conversation=31000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_23
        if GetDistanceToPlayer() >= 7:
            return State_30


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        OpenEnhanceShop(category=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_28
        if IsMenuOpen(13) == 0:
            return State_26


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        OpenEnhanceShop(category=10)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_28
        if IsMenuOpen(13) == 0:
            return State_26


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=353, state=1)
        SetFlagState(flag=364, state=1)
        SetFlagState(flag=71510011, state=0)
        SetFlagState(flag=367, state=1)

    def test(self):
        return State_23


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_51, State_52]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_32


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_5


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        DebugEvent(message='アイテムを渡す1')
        SetFlagState(flag=352, state=1)

    def test(self):
        return State_51


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        DebugEvent(message='アイテムを渡さない1')

    def test(self):
        return State_52


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(conversation=31000900, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_50
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020012, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_46
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_48
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_48
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_47


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        TalkToPlayer(conversation=31001100, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        TalkToPlayer(conversation=31001000, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_45
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        SetFlagState(flag=71510002, state=1)

    def test(self):
        return State_21


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        SetFlagState(flag=71510003, state=1)

    def test(self):
        return State_21


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71510004, state=1)

    def test(self):
        return State_21


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=31001600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_22
        if HasTalkEnded() == 1:
            return State_57
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=71510005, state=1)

    def test(self):
        return State_21


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        SetFlagState(flag=71510010, state=1)

    def test(self):
        return State_8


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_22]

    def enter(self):
        TalkToPlayer(conversation=31000650, unk1=-1, unk2=-1)
        SetFlagState(flag=71510010, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_61
        if HasTalkEnded() == 1:
            return State_58
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_30


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_22, State_28, State_29, State_62]

    def enter(self):
        TalkToPlayer(conversation=31000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_23
        if GetDistanceToPlayer() >= 7:
            return State_30


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_7, State_11, State_59]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_41

    def exit(self):
        RemoveMyAggro()


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 7:
            return State_60
        else:
            return State_23


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_23]

    def enter(self):
        TalkToPlayer(conversation=31001700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71510011, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_23


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        OpenRegularShop(6200, 6299)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_28
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 7:
            return State_28
        if IsMenuOpen(11) == 0:
            return State_26
