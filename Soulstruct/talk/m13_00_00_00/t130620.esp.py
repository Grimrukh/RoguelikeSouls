from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_26


class State_1(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_2]

    def enter(self):
        SetFlagState(flag=11015020, state=0)

    def test(self):
        return State_PrepareForTalkMenu


class State_2(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29000800, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_1
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_3(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_5]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_26


class State_EndOfInteraction(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_5, State_InterruptOpenMenu, InterruptTalkMenu]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_26


class State_5(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_InterruptOpenMenu, InterruptTalkMenu, State_45]

    def enter(self):
        # TalkToPlayer(conversation=29000700, unk1=-1, unk2=-1)
        ForceEndTalk(unk1=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if GetDistanceToPlayer() >= 12:
            return State_EndOfInteraction
        if HasTalkEnded() == 1:
            return State_3


class State_6(State):
    """ 6: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        SetFlagState(flag=71010010, state=1)

    def test(self):
        return State_8


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=29001000, unk1=-1, unk2=-1)
        SetFlagState(flag=71010010, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_94
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_34


class State_8(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_6, State_9, State_10, State_86]

    def enter(self):
        ClearTalkDisabledState()
        RemoveMyAggro()

    def test(self):
        return State_26


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        ForceEndTalk(unk1=3)

    def test(self):
        return State_8


class State_10(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_11]

    def enter(self):
        SetFlagState(flag=71010009, state=1)

    def test(self):
        return State_8


class State_11(State):
    """ 11: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=29000900, unk1=-1, unk2=-1)
        SetFlagState(flag=71010009, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_94
        if HasTalkEnded() == 1:
            return State_10
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_12(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29000000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_14
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29000100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_PrepareForTalkMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71010000, state=1)

    def test(self):
        return State_PrepareForTalkMenu


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29000200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def test(self):
        if GetFlagState(71010006) == 1 and GetFlagState(710) == 1:
            return State_96
        if GetFlagState(71010005) == 1 and GetFlagState(11016102) == 0:
            return State_78
        if GetFlagState(71010004) == 1 and GetFlagState(11016102) == 0:
            return State_76
        if GetFlagState(71010003) == 1 and GetFlagState(11016102) == 0:
            return State_19
        if GetFlagState(71010002) == 1:
            return State_18
        if GetFlagState(71010001) == 1 and GetFlagState(71010002) == 0:
            return State_17
        if GetFlagState(71010001) == 0:
            return State_15


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29000300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_21
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29000400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_22
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29000500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_15]

    def enter(self):
        SetFlagState(flag=71010001, state=1)

    def test(self):
        return State_24


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_17]

    def enter(self):
        SetFlagState(flag=71010002, state=1)

    def test(self):
        return State_24


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        SetFlagState(flag=71010003, state=1)
        SetFlagState(flag=11016102, state=1)

    def test(self):
        return State_24


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        SetFlagState(flag=71010004, state=1)

    def test(self):
        return State_24


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_20, State_21, State_22, State_23, State_77, State_79, State_97, State_99, State_101]

    def test(self):
        return State_DisplayTalkMenu
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_26


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_2, State_5, State_12, State_13, State_15, State_17, State_18, State_19, State_37, State_48, State_50, State_51, State_54, State_56, State_57, State_60, State_62, State_63, State_66, State_68, State_69, State_72, State_74, State_75, State_76, State_78, State_80, State_88, State_91, State_96]

    def enter(self):
        ClearTalkProgressData()
        ForceEndTalk(unk1=3)

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_93
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010010) == 0 and GetSelfHP() <= 90:
            return State_7
        if GetFlagState(1321) == 1:
            return State_9
        if GetFlagState(71010011) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71010009) == 1:
            return State_87
        if GetFlagState(71010009) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5:
            return State_11
        if GetFlagState(71010011) == 1:
            return State_9
        else:
            return State_9

    def exit(self):
        RemoveMyAggro()


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_0, State_3, State_EndOfInteraction, State_8, State_24, State_27, State_28, State_InterruptOpenMenu, State_35, State_PrepareForTalkMenu, State_40, State_88, State_91, State_92, State_93, State_95]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1322) == 0 and GetDistanceToPlayer() <= 5:
            return State_40
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_PrepareForTalkMenu


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_26


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_26


class State_DisplayTalkMenu(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_24, State_OpenRepair, State_31, State_PrepareForTalkMenu, State_OpenModify, State_OpenShopReal, State_OpenReinforceArmor]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000190, required_flag=-1)  # Modify
        AddTalkListData(menu_index=2, menu_text=15000112, required_flag=-1)  # Reinforce armor
        AddTalkListData(menu_index=3, menu_text=15000120, required_flag=-1)  # Repair
        AddTalkListData(menu_index=4, menu_text=15000010, required_flag=-1)  # Shop
        AddTalkListData(menu_index=5, menu_text=15000005, required_flag=-1)
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return InterruptTalkMenu
        if GetTalkListEntryResult() == 5:
            return ExitTalkMenu
        if GetTalkListEntryResult() == 3:
            return State_OpenRepair
        if GetTalkListEntryResult() == 0:
            return ExitTalkMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return InterruptTalkMenu
        if GetTalkListEntryResult() == 1:
            return State_OpenModify
        if GetTalkListEntryResult() == 4:
            return State_OpenShop
        if GetTalkListEntryResult() == 2:
            return State_OpenReinforceArmor

    def exit(self):
        ClearTalkListData()


class State_OpenRepair(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        OpenRepairShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(12) == 0:
            return State_DisplayTalkMenu


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        OpenEnhanceShop(category=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(13) == 0:
            return State_DisplayTalkMenu


class State_InterruptOpenMenu(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_OpenRepair, State_31, State_OpenModify, State_OpenShopReal, State_OpenReinforceArmor, State_100]

    def enter(self):
        CloseMenu()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_93
        if IsPlayerMovingACertainDistance(1) == 1:
            return State_5
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_EndOfInteraction
        else:
            return State_26


class InterruptTalkMenu(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_93
        if IsPlayerMovingACertainDistance(1) == 0:
            return State_EndOfInteraction


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_2, State_7, State_11, State_12, State_13, State_15, State_17, State_18, State_19, State_40, State_48, State_50, State_51, State_54, State_56, State_57, State_60, State_62, State_63, State_66, State_68, State_69, State_72, State_74, State_75, State_76, State_78, State_80, State_87, State_88, State_91, State_93, State_96]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        return State_35


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_26


class State_PrepareForTalkMenu(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_1, State_13, State_14, State_44]

    def enter(self):
        ClearTalkActionState()
        SetFlagState(flag=367, state=1)

    def test(self):
        return State_DisplayTalkMenu
        # UNREACHABLE:
        # if GetDistanceToPlayer() >= 3:
        #     return State_26


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_25


class ExitTalkMenu(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def test(self):
        if DidYouDoSomethingInTheMenu(11) == 1 or DidYouDoSomethingInTheMenu(12) == 1 or DidYouDoSomethingInTheMenu(2) == 1 or DidYouDoSomethingInTheMenu(3) == 1 or DidYouDoSomethingInTheMenu(4) == 1:
            return State_89
        if DidYouDoSomethingInTheMenu(11) == 0 or DidYouDoSomethingInTheMenu(12) == 0 or DidYouDoSomethingInTheMenu(2) == 0 or DidYouDoSomethingInTheMenu(3) == 0 or DidYouDoSomethingInTheMenu(4) == 0:
            return State_90
        else:
            return State_92


class State_OpenModify(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        CombineMenuFlagAndEventFlag(11812000, 333)  # Crystal
        CombineMenuFlagAndEventFlag(11812000, 334)  # Lightning
        CombineMenuFlagAndEventFlag(11812000, 335)  # Refined
        CombineMenuFlagAndEventFlag(11812000, 336)  # Magic
        CombineMenuFlagAndEventFlag(11812000, 338)  # Enchanted
        CombineMenuFlagAndEventFlag(11812000, 339)  # Divine
        CombineMenuFlagAndEventFlag(11812000, 341)  # Dire
        CombineMenuFlagAndEventFlag(11812000, 342)  # Fire
        CombineMenuFlagAndEventFlag(11812000, 344)  # Draconic
        CombineMenuFlagAndEventFlag(11812000, 346)  # Undo ascension
        OpenEquipmentChangeOfPurposeShop()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(13) == 0:
            return State_DisplayTalkMenu


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_26, State_94]

    def enter(self):
        # TalkToPlayer(conversation=29001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_26
        if GetDistanceToPlayer() >= 5:
            return State_34


class State_OpenShop(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def test(self):
        return State_OpenShopReal


class State_OpenShopReal(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_OpenShop]

    def enter(self):
        OpenRegularShop(2000, 2099)  # Vamos's range.

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(11) == 0:
            return State_DisplayTalkMenu


class State_OpenReinforceArmor(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        OpenEnhanceShop(category=10)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(13) == 0:
            return State_DisplayTalkMenu


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_50, State_51, State_56, State_57, State_62, State_63, State_68, State_69, State_74, State_75, State_80]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_PrepareForTalkMenu


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_49, State_55, State_61, State_67, State_73, State_98, State_102]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_5


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        DebugEvent(message='アイテムを渡す1')
        SetFlagState(flag=350, state=1)

    def test(self):
        return State_50


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        DebugEvent(message='アイテムを渡さない1')

    def test(self):
        return State_51


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29001200, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話1')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_49
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_48]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020010, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_47
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_47
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_46


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_46]

    def enter(self):
        TalkToPlayer(conversation=29001400, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_47]

    def enter(self):
        TalkToPlayer(conversation=29001300, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと1')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        DebugEvent(message='アイテムを渡す2')
        SetFlagState(flag=351, state=1)

    def test(self):
        return State_56


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_55]

    def enter(self):
        DebugEvent(message='アイテムを渡さない2')

    def test(self):
        return State_57


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29001450, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話2')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_55
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_54]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020011, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_53
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_53
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_52


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        TalkToPlayer(conversation=29001470, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_53]

    def enter(self):
        TalkToPlayer(conversation=29001460, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと2')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        DebugEvent(message='アイテムを渡す3')
        SetFlagState(flag=358, state=1)

    def test(self):
        return State_62


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_61]

    def enter(self):
        DebugEvent(message='アイテムを渡さない3')

    def test(self):
        return State_63


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29001500, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話2')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020018, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_59
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_59
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_58


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=29001700, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと3')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_59]

    def enter(self):
        TalkToPlayer(conversation=29001600, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと3')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        DebugEvent(message='アイテムを渡す4')
        SetFlagState(flag=359, state=1)

    def test(self):
        return State_68


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        DebugEvent(message='アイテムを渡さない4')

    def test(self):
        return State_69


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29001800, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話4')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020019, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_65
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_65
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_64


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        TalkToPlayer(conversation=29002000, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと4')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_65]

    def enter(self):
        TalkToPlayer(conversation=29001900, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと4')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_73]

    def enter(self):
        DebugEvent(message='アイテムを渡す5')
        SetFlagState(flag=360, state=1)

    def test(self):
        return State_74


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_73]

    def enter(self):
        DebugEvent(message='アイテムを渡さない5')

    def test(self):
        return State_75


class State_72(State):
    """ 72: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        TalkToPlayer(conversation=29002100, unk1=-1, unk2=-1)
        DebugEvent(message='転職アイテム持ってた会話5')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_73
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_73(State):
    """ 73: No description. """

    def previous_states(self):
        return [State_72]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020020, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_71
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_71
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_70


class State_74(State):
    """ 74: No description. """

    def previous_states(self):
        return [State_70]

    def enter(self):
        TalkToPlayer(conversation=29002300, unk1=-1, unk2=-1)
        DebugEvent(message='渡したあと5')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_75(State):
    """ 75: No description. """

    def previous_states(self):
        return [State_71]

    def enter(self):
        TalkToPlayer(conversation=29002200, unk1=-1, unk2=-1)
        DebugEvent(message='渡さなかったあと5')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_76(State):
    """ 76: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29000600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_77
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_77(State):
    """ 77: No description. """

    def previous_states(self):
        return [State_76]

    def enter(self):
        SetFlagState(flag=71010005, state=1)

    def test(self):
        return State_24


class State_78(State):
    """ 78: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29002700, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_79
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_79(State):
    """ 79: No description. """

    def previous_states(self):
        return [State_78]

    def enter(self):
        SetFlagState(flag=71010006, state=1)

    def test(self):
        return State_24


class State_80(State):
    """ 80: No description. """

    def previous_states(self):
        return [State_81, State_82, State_83, State_84, State_85]

    def enter(self):
        TalkToPlayer(conversation=29002400, unk1=-1, unk2=-1)
        DebugEvent(message='だれかの転職アイテム持ってた会話')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_44
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_81(State):
    """ 81: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71010012, state=1)

    def test(self):
        return State_80


class State_82(State):
    """ 82: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71010013, state=1)

    def test(self):
        return State_80


class State_83(State):
    """ 83: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71010014, state=1)

    def test(self):
        return State_80


class State_84(State):
    """ 84: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71010015, state=1)

    def test(self):
        return State_80


class State_85(State):
    """ 85: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71010016, state=1)

    def test(self):
        return State_80


class State_86(State):
    """ 86: No description. """

    def previous_states(self):
        return [State_87]

    def enter(self):
        SetFlagState(flag=71010011, state=1)

    def test(self):
        return State_8


class State_87(State):
    """ 87: No description. """

    def previous_states(self):
        return [State_25]

    def enter(self):
        TalkToPlayer(conversation=29000950, unk1=-1, unk2=-1)
        SetFlagState(flag=71010011, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_94
        if HasTalkEnded() == 1:
            return State_86
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_88(State):
    """ 88: No description. """

    def previous_states(self):
        return [State_90]

    def enter(self):
        TalkToPlayer(conversation=29002500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_89(State):
    """ 89: No description. """

    def previous_states(self):
        return [ExitTalkMenu]

    def enter(self):
        DebugEvent(message='買って立ち去る')

    def test(self):
        return State_91


class State_90(State):
    """ 90: No description. """

    def previous_states(self):
        return [ExitTalkMenu]

    def enter(self):
        DebugEvent(message='買わず立ち去る')

    def test(self):
        return State_88


class State_91(State):
    """ 91: No description. """

    def previous_states(self):
        return [State_89]

    def enter(self):
        TalkToPlayer(conversation=29002600, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_26
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_92(State):
    """ 92: No description. """

    def previous_states(self):
        return [ExitTalkMenu]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_26


class State_93(State):
    """ 93: No description. """

    def previous_states(self):
        return [State_25, State_InterruptOpenMenu, InterruptTalkMenu, State_95]

    def enter(self):
        # TalkToPlayer(conversation=29001100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_26
        if GetDistanceToPlayer() >= 5:
            return State_34


class State_94(State):
    """ 94: No description. """

    def previous_states(self):
        return [State_7, State_11, State_87]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_40

    def exit(self):
        RemoveMyAggro()


class State_95(State):
    """ 95: No description. """

    def previous_states(self):
        return [State_49, State_55, State_61, State_67, State_73, State_98, State_102]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_93
        else:
            return State_26


class State_96(State):
    """ 96: No description. """

    def previous_states(self):
        return [State_16]

    def enter(self):
        TalkToPlayer(conversation=29002800, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_25
        if HasTalkEnded() == 1:
            return State_97
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_34


class State_97(State):
    """ 97: No description. """

    def previous_states(self):
        return [State_96]

    def enter(self):
        SetFlagState(flag=71010020, state=1)

    def test(self):
        return State_24


class State_98(State):
    """ 98: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        OpenGenericDialog(unk1=1, text_id=10010750, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='種火持ってない')

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_99
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_99


class State_99(State):
    """ 99: No description. """

    def previous_states(self):
        return [State_98]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_24


class State_100(State):
    """ 100: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        OpenItemAcquisitionMenu(3, 9002, 1)
        AcquireGesture(2)
        SetFlagState(flag=282, state=0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(63) == 0:
            return State_102


class State_101(State):
    """ 101: No description. """

    def previous_states(self):
        return [State_102]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000誓約同じ')

    def test(self):
        return State_24


class State_102(State):
    """ 102: No description. """

    def previous_states(self):
        return [State_100]

    def enter(self):
        OpenGenericDialog(unk1=7, text_id=10010755, unk2=1, unk3=0, display_distance=2)
        DebugEvent(message='ジェスチャーを学んだ')
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        if CheckSelfDeath() == 1:
            return State_95
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsAttackedBySomeone() == 1:
            return State_45
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_101
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_101
