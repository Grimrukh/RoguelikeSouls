from soulstruct.game_types import *


class Flags(Flag):
    GetWarriorEquipment = 11022400
    GetKnightEquipment = 11022401
    GetWandererEquipment = 11022402
    GetThiefEquipment = 11022403
    GetBarbarianEquipment = 11022404
    GetHunterEquipment = 11022405
    GetSorcererEquipment = 11022406
    GetClericEquipment = 11022407
    ActivateOneLifeMode = 11022410


class Chrs(Character):
    Alvina = 6000
    Solaire = 6010
    Siegmeyer = 6020
    Logan = 6030
    Quelana = 6040
    Havel = 6050
    Mornstein = 6060
    LobosJr = 6070

    Crow = 1020100


class FXEvents(int):
    SolairePortal = 1020851
    SiegmeyerPortal = 1020852
    LoganPortal = 1020853
    QuelanaPortal = 1020854
    HavelPortal = 1020855
    MornsteinPortal = 1020856
    LobosJrPortal = 1020857


class ItemLots(ItemLot):
    AlvinaGift = 51000
    SolaireGift = 51010
    SiegmeyerGift = 51020
    LoganGift = 51030
    QuelanaGift = 51040
    HavelGift = 51050
    MornsteinGift = 51060
    LobosJrGift = 51070

    WarriorEquipment = 1020100
    KnightEquipment = 1020110
    WandererEquipment = 1020120
    ThiefEquipment = 1020130
    BarbarianEquipment = 1020140
    HunterEquipment = 1020150
    SorcererEquipment = 1020160
    ClericEquipment = 1020170
    OneLifeModeGift = 1020200
