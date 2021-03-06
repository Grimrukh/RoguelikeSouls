from soulstruct.game_types import *


BaseFlag = 11512000
TempBaseFlag = 11515000
BaseEntity = 1510000
BaseNPC = 6200


class Flags(Flag):
    Exit1Disabled = BaseFlag + 0
    Exit1Activated = BaseFlag + 1
    Exit2Disabled = BaseFlag + 10
    Exit2Activated = BaseFlag + 11
    Exit3Disabled = BaseFlag + 20
    Exit3Activated = BaseFlag + 21

    Boss1Dead = BaseFlag + 290
    Boss1IsTwin = BaseFlag + 291
    Boss1AllyAvailable = BaseFlag + 292
    Boss1AllyDone = BaseFlag + 293

    InvaderSummoned = TempBaseFlag + 40
    InvaderDismissed = TempBaseFlag + 41
    InvaderDead = BaseFlag + 90


class Chrs(Character):
    AllyBoss1 = BaseNPC + 0
    Boss1 = BaseEntity + 290
    Boss1Twin = BaseEntity + 291
    Invader = BaseNPC + 50

    Mimic = BaseEntity + 180

    Solaire = 6011

    Gwynevere = 1510600


class Regions(Region):
    InvaderTrigger = BaseEntity + 200
    InvaderSpawnPoint = BaseEntity + 201

    Exit1Prompt = BaseEntity + 250  # Sen's demons. (Unused)

    Boss1Trigger = BaseEntity + 292  # Done

    MimicNest = BaseEntity + 185


class Objects(Object):
    Exit2Prompt = BaseEntity + 251  # Archives golden fog. (Done)
    Exit3Prompt = BaseEntity + 252  # Bonfire in Gwynevere's room. (Done)


class ItemLots(ItemLotParam):
    Boss1Reward = BaseEntity + 290
