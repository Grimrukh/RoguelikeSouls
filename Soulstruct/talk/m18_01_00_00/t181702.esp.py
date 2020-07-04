from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_Zero(State):
    """ 0: No description. """

    def test(self):
        return State_InteractionStart


class State_EndOfInteraction(State):
    """ 1: No description. """

    def previous_states(self):
        return [State_InterruptOpenMenu, InterruptTalkMenu]

    def enter(self):
        ForceEndTalk(unk1=0)

    def test(self):
        return State_InteractionStart


class State_InteractionStart(State):
    """ 2: No description. """

    def previous_states(self):
        return [State_Zero, State_EndOfInteraction, State_DisableTalkPrompt, State_InterruptOpenMenu, State_PrepareForTalkMenu, State_ClearTalkDisabled]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1:
            return State_PrepareForTalkMenu
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_DisableTalkPrompt
        if GetFlagState(1620) == 0 and GetFlagState(1621) == 0 and GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2:
            return State_EnableTalkPrompt


class State_EnableTalkPrompt(State):
    """ 3: No description. """

    def previous_states(self):
        return [State_InteractionStart]

    def enter(self):
        DisplayOneLineHelp(text_id=10010200)

    def test(self):
        return State_InteractionStart


class State_DisableTalkPrompt(State):
    """ 4: No description. """

    def previous_states(self):
        return [State_InteractionStart]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)

    def test(self):
        return State_InteractionStart


class State_DisplayTalkMenu(State):
    """ 5: No description. """

    def previous_states(self):
        return [State_OpenRepair, State_PrepareForTalkMenu, State_OpenModify, State_OpenShopReal, State_OpenReinforceArmor]

    def enter(self):
        AddTalkListData(menu_index=1, menu_text=15000010, required_flag=-1)  # Shop
        AddTalkListData(menu_index=2, menu_text=15000005, required_flag=-1)  # Leave
        ShowShopMessage(0, 0, 0)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return InterruptTalkMenu
        if GetTalkListEntryResult() == 2:
            return ExitTalkMenu
        if GetTalkListEntryResult() == 0:
            return ExitTalkMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return InterruptTalkMenu
        if GetTalkListEntryResult() == 1:
            return State_OpenShop

    def exit(self):
        ClearTalkListData()


class State_OpenRepair(State):
    """ 6: No description. """

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


class State_InterruptOpenMenu(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_OpenRepair, State_OpenModify, State_OpenShopReal, State_OpenReinforceArmor]

    def enter(self):
        CloseMenu()

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1 or IsPlayerMovingACertainDistance(1) == 1 or IsPlayerMovingACertainDistance(1) == 0:
            return State_EndOfInteraction
        else:
            return State_InteractionStart


class InterruptTalkMenu(State):
    """ 8: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def enter(self):
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()
        CloseShopMessage()

    def test(self):
        return State_EndOfInteraction


class State_PrepareForTalkMenu(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_InteractionStart]

    def enter(self):
        ClearTalkActionState()

    def test(self):
        return State_DisplayTalkMenu


class ExitTalkMenu(State):
    """ 10: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def test(self):
        return State_ClearTalkDisabled


class State_OpenModify(State):
    """ 11: No description. """

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


class State_OpenShop(State):
    """ 12: No description. """

    def previous_states(self):
        return [State_DisplayTalkMenu]

    def test(self):
        return State_OpenShopReal


class State_OpenShopReal(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_OpenShop]

    def enter(self):
        OpenRegularShop(3000, 3099)  # Undead Merchant's range.

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_InterruptOpenMenu
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 3:
            return State_InterruptOpenMenu
        if IsMenuOpen(11) == 0:
            return State_DisplayTalkMenu


class State_OpenReinforceArmor(State):
    """ 14: No description. """

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


class State_ClearTalkDisabled(State):
    """ 15: No description. """

    def previous_states(self):
        return [ExitTalkMenu]

    def enter(self):
        ClearTalkDisabledState()

    def test(self):
        return State_InteractionStart
