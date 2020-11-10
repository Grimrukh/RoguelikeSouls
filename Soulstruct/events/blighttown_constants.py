from soulstruct.game_types import *


BaseFlag = 11402000
TempBaseFlag = 11405000
BaseEntity = 1400000
BaseNPC = 6200


class Flags(Flag):
    Exit1Disabled = BaseFlag + 0
    Exit1Activated = BaseFlag + 1
    Exit2Disabled = BaseFlag + 10
    Exit2Activated = BaseFlag + 11
    Exit3Disabled = BaseFlag + 20
    Exit3Activated = BaseFlag + 21
    Exit4Disabled = BaseFlag + 30
    Exit4Activated = BaseFlag + 31

    Boss1Dead = BaseFlag + 290
    Boss1IsTwin = BaseFlag + 291
    Boss1AllyAvailable = BaseFlag + 292
    Boss1AllyDone = BaseFlag + 293
    Boss2Dead = BaseFlag + 280
    Boss2IsTwin = BaseFlag + 281
    Boss2AllyAvailable = BaseFlag + 282
    Boss2AllyDone = BaseFlag + 283

    InvaderSummoned = TempBaseFlag + 40
    InvaderDismissed = TempBaseFlag + 41
    InvaderDead = BaseFlag + 90


class Chrs(Character):
    AllyBoss1 = BaseNPC + 0
    Boss1 = BaseEntity + 290
    Boss1Twin = BaseEntity + 291
    AllyBoss2 = BaseNPC + 1
    Boss2 = BaseEntity + 280
    Boss2Twin = BaseEntity + 281
    Invader = BaseNPC + 50

    Mimic = BaseEntity + 180

    Havel = 6051


class Regions(Region):
    InvaderTrigger = BaseEntity + 200
    InvaderSpawnPoint = BaseEntity + 201

    Boss1Trigger = BaseEntity + 292
    Boss2Trigger = BaseEntity + 282

    Exit1Prompt = BaseEntity + 250  # Depths door.
    Exit3Prompt = BaseEntity + 252  # Great Hollow entrance.

    MimicNest = BaseEntity + 185


class Objects(Object):
    Exit2Prompt = BaseEntity + 251  # Valley exit.
    Exit4Prompt = BaseEntity + 253  # Quelaag's exit.


class ItemLots(ItemLotParam):
    Boss1Reward = BaseEntity + 290
    Boss2Reward = BaseEntity + 280
