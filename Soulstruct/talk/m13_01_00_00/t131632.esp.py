from soulstruct.esd import State
from soulstruct.esd.functions import *


class State_0(State):
    """ 0: No description. """

    def test(self):
        return State_70


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
        return [State_8, State_12, State_21, State_22, State_24, State_26, State_28, State_30, State_32, State_34, State_36, State_38, State_40, State_41, State_44, State_45, State_46, State_47, State_48, State_49, State_50, State_52, State_53, State_54, State_55, State_56, State_60]

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
        return [State_2, State_4, State_5, State_11, State_16, State_17, State_23, State_40, State_41, State_44, State_51, State_54, State_57, State_59, State_62, State_63, State_67, State_68, State_69, State_70, State_71]

    def enter(self):
        DebugEvent(message='unknow')

    def test(self):
        if CheckSelfDeath() == 1 and GetFlagState(1628) == 0 and GetDistanceToPlayer() <= 5:
            return State_14
        if IsPlayerDead() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310079) == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 180 and GetDistanceToPlayer() <= 5 and (GetFlagState(1625) == 1 or GetFlagState(1627) == 1):
            return State_58
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1624) == 1:
            return State_43
        if IsPlayerTalkingToMe() == 1 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetOneLineHelpStatus() == 1 and GetFlagState(1623) == 1:
            return State_42
        if GetOneLineHelpStatus() == 0 and HasDisableTalkPeriodElapsed() == 1 and IsTalkingToSomeoneElse() == 0 and CheckSelfDeath() == 0 and IsCharacterDisabled() == 0 and IsClientPlayer() == 0 and GetRelativeAngleBetweenPlayerAndSelf() <= 45 and GetDistanceToPlayer() <= 2 and GetFlagState(1628) == 0 and GetFlagState(1627) == 0 and GetFlagState(1625) == 0:
            return State_5
        if GetOneLineHelpStatus() == 1 and (IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 45 or GetDistanceToPlayer() > 2):
            return State_4
        if IsAttackedBySomeone() == 1 and GetFlagState(1628) == 0:
            return State_1


class State_7(State):
    """ 7: No description. """

    def previous_states(self):
        return [State_1, State_21, State_22, State_44, State_45, State_46, State_47, State_48, State_49, State_50, State_52, State_53, State_54, State_55, State_56]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310090) == 0 and GetSelfHP() <= 90 and GetFlagState(1623) == 1:
            return State_60
        if GetFlagState(71310088) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1638) == 1 and ComparePlayerStatus(12, 0, 0) == 1 and GetSelfHP() <= 90 and GetFlagState(1624) == 1:
            return State_38
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310086) == 0 and GetSelfHP() <= 90 and GetFlagState(1638) == 1 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1624) == 1:
            return State_12
        if GetFlagState(71310089) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1638) == 0 and ComparePlayerStatus(12, 0, 0) == 1 and GetSelfHP() <= 90 and GetFlagState(1624) == 1:
            return State_30
        if IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(71310087) == 0 and GetSelfHP() <= 90 and GetFlagState(1638) == 0 and ComparePlayerStatus(12, 0, 1) == 1 and GetFlagState(1624) == 1:
            return State_36
        if GetFlagState(1625) == 1 or GetFlagState(1627) == 1:
            return State_10
        if GetFlagState(71310085) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1623) == 1 and GetFlagState(71310084) == 1:
            return State_34
        if GetFlagState(71310084) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1623) == 1 and GetFlagState(71310083) == 1:
            return State_32
        if GetFlagState(71310083) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1623) == 1:
            return State_28
        if GetFlagState(71310082) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1624) == 1 and GetFlagState(71310081) == 1:
            return State_26
        if GetFlagState(71310081) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1624) == 1 and GetFlagState(71310080) == 1:
            return State_24
        if GetFlagState(71310080) == 0 and IsPlayerAttacking() == 1 and GetDistanceToPlayer() <= 5 and GetFlagState(1624) == 1:
            return State_8
        if GetFlagState(71310082) == 1:
            return State_10
        if GetFlagState(71310085) == 1:
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
        TalkToPlayer(conversation=42011440, unk1=-1, unk2=-1)
        SetFlagState(flag=71310080, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_9
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_9(State):
    """ 9: No description. """

    def previous_states(self):
        return [State_8]

    def enter(self):
        SetFlagState(flag=71310080, state=1)

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
        return [State_9, State_10, State_13, State_25, State_27, State_29, State_31, State_33, State_35, State_37, State_39, State_61]

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
        TalkToPlayer(conversation=42011500, unk1=-1, unk2=-1)
        SetFlagState(flag=71310086, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_13
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_13(State):
    """ 13: No description. """

    def previous_states(self):
        return [State_12]

    def enter(self):
        SetFlagState(flag=71310086, state=1)

    def test(self):
        return State_11


class State_14(State):
    """ 14: No description. """

    def previous_states(self):
        return [State_6, State_7, State_15, State_23]

    def test(self):
        if GetFlagState(1624) == 1:
            return State_41
        if GetFlagState(1623) == 1:
            return State_40


class State_15(State):
    """ 15: No description. """

    def previous_states(self):
        return [State_8, State_12, State_24, State_26, State_28, State_30, State_32, State_34, State_36, State_38, State_60]

    def enter(self):
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14

    def exit(self):
        RemoveMyAggro()


class State_16(State):
    """ 16: No description. """

    def previous_states(self):
        return [State_21, State_22]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_17(State):
    """ 17: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_18(State):
    """ 18: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        DebugEvent(message='はい')
        SetFlagState(flag=71310091, state=1)
        SetFlagState(flag=1638, state=1)
        SetFlagState(flag=1637, state=1)
        SetFlagState(flag=71310098, state=1)

    def test(self):
        return State_21


class State_19(State):
    """ 19: No description. """

    def previous_states(self):
        return [State_20]

    def enter(self):
        DebugEvent(message='いいえ')
        SetFlagState(flag=71310092, state=1)
        SetFlagState(flag=1637, state=1)
        SetFlagState(flag=71310098, state=1)

    def test(self):
        return State_22


class State_20(State):
    """ 20: No description. """

    def previous_states(self):
        return [State_45]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_17
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_19
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_18


class State_21(State):
    """ 21: No description. """

    def previous_states(self):
        return [State_18]

    def enter(self):
        TalkToPlayer(conversation=42010100, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_22(State):
    """ 22: No description. """

    def previous_states(self):
        return [State_19]

    def enter(self):
        TalkToPlayer(conversation=42010200, unk1=-1, unk2=-1)
        DebugEvent(message='ノーを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_16
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_23(State):
    """ 23: No description. """

    def previous_states(self):
        return [State_20, State_66]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        if CheckSelfDeath() == 1 and GetDistanceToPlayer() <= 5:
            return State_14
        else:
            return State_6


class State_24(State):
    """ 24: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011450, unk1=-1, unk2=-1)
        SetFlagState(flag=71310081, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_25
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_25(State):
    """ 25: No description. """

    def previous_states(self):
        return [State_24]

    def enter(self):
        SetFlagState(flag=71310081, state=1)

    def test(self):
        return State_11


class State_26(State):
    """ 26: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011460, unk1=-1, unk2=-1)
        SetFlagState(flag=71310082, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_27
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_27(State):
    """ 27: No description. """

    def previous_states(self):
        return [State_26]

    def enter(self):
        SetFlagState(flag=71310083, state=1)

    def test(self):
        return State_11


class State_28(State):
    """ 28: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011840, unk1=-1, unk2=-1)
        SetFlagState(flag=71310083, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_29
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_29(State):
    """ 29: No description. """

    def previous_states(self):
        return [State_28]

    def enter(self):
        SetFlagState(flag=71310083, state=1)

    def test(self):
        return State_11


class State_30(State):
    """ 30: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011570, unk1=-1, unk2=-1)
        SetFlagState(flag=71310089, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_31
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_31(State):
    """ 31: No description. """

    def previous_states(self):
        return [State_30]

    def enter(self):
        SetFlagState(flag=71310089, state=1)

    def test(self):
        return State_11


class State_32(State):
    """ 32: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011850, unk1=-1, unk2=-1)
        SetFlagState(flag=71310084, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_33
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_33(State):
    """ 33: No description. """

    def previous_states(self):
        return [State_32]

    def enter(self):
        SetFlagState(flag=71310084, state=1)

    def test(self):
        return State_11


class State_34(State):
    """ 34: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011860, unk1=-1, unk2=-1)
        SetFlagState(flag=71310085, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_35
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_35(State):
    """ 35: No description. """

    def previous_states(self):
        return [State_34]

    def enter(self):
        SetFlagState(flag=71310085, state=1)

    def test(self):
        return State_11


class State_36(State):
    """ 36: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011520, unk1=-1, unk2=-1)
        SetFlagState(flag=71310087, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_37
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_37(State):
    """ 37: No description. """

    def previous_states(self):
        return [State_36]

    def enter(self):
        SetFlagState(flag=71310087, state=1)

    def test(self):
        return State_11


class State_38(State):
    """ 38: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011550, unk1=-1, unk2=-1)
        SetFlagState(flag=71310088, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_39
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_39(State):
    """ 39: No description. """

    def previous_states(self):
        return [State_38]

    def enter(self):
        SetFlagState(flag=71310088, state=1)

    def test(self):
        return State_11


class State_40(State):
    """ 40: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=42012000, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_41(State):
    """ 41: No description. """

    def previous_states(self):
        return [State_14]

    def enter(self):
        TalkToPlayer(conversation=42011600, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        ForceCloseMenu()

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
        if GetDistanceToPlayer() >= 5:
            return State_3


class State_42(State):
    """ 42: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71310094) == 1:
            return State_44
        if GetFlagState(71310094) == 0 and GetFlagState(71310098) == 1:
            return State_49
        if GetFlagState(71310091) == 0 and GetFlagState(71310092) == 0 and GetFlagState(1637) == 0:
            return State_45
        if GetFlagState(71310098) == 0 and GetFlagState(1638) == 1 and GetFlagState(1637) == 1:
            return State_46
        if GetFlagState(71310098) == 0 and GetFlagState(1638) == 0 and GetFlagState(1637) == 1 and ComparePlayerStatus(12, 0, 1) == 1:
            return State_48
        if GetFlagState(71310098) == 0 and GetFlagState(1638) == 0 and GetFlagState(1637) == 1 and ComparePlayerStatus(12, 0, 0) == 1:
            return State_47


class State_43(State):
    """ 43: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(71310096) == 1 and GetFlagState(11310594) == 0:
            return State_56
        if GetFlagState(1638) == 1:
            return State_50
        if GetFlagState(71310099) == 1:
            return State_54
        if GetFlagState(71310095) == 0 and GetFlagState(71310096) == 0 and GetFlagState(1638) == 0:
            return State_52


class State_44(State):
    """ 44: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        TalkToPlayer(conversation=42010600, unk1=-1, unk2=-1)
        DebugEvent(message='イエスを選んだあと')

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_45(State):
    """ 45: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_20
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_46(State):
    """ 46: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_47(State):
    """ 47: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010450, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_48(State):
    """ 48: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010400, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_69
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_49(State):
    """ 49: No description. """

    def previous_states(self):
        return [State_42]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010500, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_68
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_50(State):
    """ 50: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42011200, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_51
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_51(State):
    """ 51: No description. """

    def previous_states(self):
        return [State_50]

    def enter(self):
        SetFlagState(flag=11310595, state=1)
        SetFlagState(flag=71310088, state=1)
        SetFlagState(flag=71310086, state=1)

    def test(self):
        return State_6


class State_52(State):
    """ 52: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42010900, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_66
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_53(State):
    """ 53: No description. """

    def previous_states(self):
        return [State_67]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42011110, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        else:
            return State_62
        # UNREACHABLE:
        # if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
        #     return State_3


class State_54(State):
    """ 54: No description. """

    def previous_states(self):
        return [State_43]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42011300, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_6
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_55(State):
    """ 55: No description. """

    def previous_states(self):
        return [State_64]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42011000, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_62
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_3


class State_56(State):
    """ 56: No description. """

    def previous_states(self):
        return [State_43, State_65]

    def enter(self):
        DisplayOneLineHelp(text_id=-1)
        TalkToPlayer(conversation=42011100, unk1=-1, unk2=-1)

    def test(self):
        if IsAttackedBySomeone() == 1 or CheckSelfDeath() == 1:
            return State_7
        if HasTalkEnded() == 1:
            return State_67
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5 or IsPlayerDead() == 1:
            return State_3


class State_57(State):
    """ 57: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=42011700, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310079, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_58(State):
    """ 58: No description. """

    def previous_states(self):
        return [State_6]

    def test(self):
        if GetFlagState(1623) == 1:
            return State_71
        if ComparePlayerStatus(12, 0, 0) == 1:
            return State_59
        if ComparePlayerStatus(12, 0, 1) == 1:
            return State_57


class State_59(State):
    """ 59: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=42011750, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310079, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6


class State_60(State):
    """ 60: No description. """

    def previous_states(self):
        return [State_7]

    def enter(self):
        TalkToPlayer(conversation=42011900, unk1=-1, unk2=-1)
        SetFlagState(flag=71310090, state=1)
        ForceCloseMenu()

    def test(self):
        if CheckSelfDeath() == 1:
            return State_15
        if HasTalkEnded() == 1:
            return State_61
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 10:
            return State_3


class State_61(State):
    """ 61: No description. """

    def previous_states(self):
        return [State_60]

    def enter(self):
        SetFlagState(flag=71310090, state=1)

    def test(self):
        return State_11


class State_62(State):
    """ 62: No description. """

    def previous_states(self):
        return [State_53, State_55]

    def enter(self):
        ClearTalkDisabledState()
        DebugEvent(message='会話タイマークリア\u3000選択肢')

    def test(self):
        return State_6


class State_63(State):
    """ 63: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        ForceCloseGenericDialog()
        ForceEndTalk(unk1=0)
        ClearTalkProgressData()

    def test(self):
        return State_6


class State_64(State):
    """ 64: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        DebugEvent(message='はい')
        SetFlagState(flag=71310095, state=1)
        SetFlagState(flag=71310099, state=1)

    def test(self):
        return State_55


class State_65(State):
    """ 65: No description. """

    def previous_states(self):
        return [State_66]

    def enter(self):
        DebugEvent(message='奇跡を教わらない')
        SetFlagState(flag=71310096, state=1)
        SetFlagState(flag=71310099, state=1)

    def test(self):
        return State_56


class State_66(State):
    """ 66: No description. """

    def previous_states(self):
        return [State_52]

    def enter(self):
        OpenGenericDialog(unk1=8, text_id=10020041, unk2=3, unk3=4, display_distance=2)

    def test(self):
        if CheckSelfDeath() == 1 or IsAttackedBySomeone() == 1:
            return State_23
        if IsTalkingToSomeoneElse() or CheckSelfDeath() or IsCharacterDisabled() or IsClientPlayer() == 1 or GetRelativeAngleBetweenPlayerAndSelf() > 120 or GetDistanceToPlayer() > 5:
            return State_63
        if GetGenericDialogButtonResult() == 0 and IsGenericDialogOpen() == 0:
            return State_65
        if GetGenericDialogButtonResult() == 2 and IsGenericDialogOpen() == 0:
            return State_65
        if GetGenericDialogButtonResult() == 1 and IsGenericDialogOpen() == 0:
            return State_64


class State_67(State):
    """ 67: No description. """

    def previous_states(self):
        return [State_56]

    def enter(self):
        SetFlagState(flag=11310594, state=1)

    def test(self):
        if GetDistanceToPlayer() >= 5:
            return State_6
        if IsMenuOpen(63) == 0:
            return State_53


class State_68(State):
    """ 68: No description. """

    def previous_states(self):
        return [State_49]

    def enter(self):
        SetFlagState(flag=71310094, state=1)

    def test(self):
        return State_6


class State_69(State):
    """ 69: No description. """

    def previous_states(self):
        return [State_46, State_47, State_48]

    def enter(self):
        SetFlagState(flag=71310098, state=1)

    def test(self):
        return State_6


class State_70(State):
    """ 70: No description. """

    def previous_states(self):
        return [State_0]

    def enter(self):
        SetFlagState(flag=71310079, state=0)

    def test(self):
        return State_6


class State_71(State):
    """ 71: No description. """

    def previous_states(self):
        return [State_58]

    def enter(self):
        TalkToPlayer(conversation=42012100, unk1=-1, unk2=-1)
        DisplayOneLineHelp(text_id=-1)
        SetFlagState(flag=71310079, state=1)

    def test(self):
        if HasTalkEnded() == 1:
            return State_6
