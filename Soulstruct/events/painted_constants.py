from soulstruct.game_types import *


BaseFlag = 11102000
TempBaseFlag = 11105000
BaseEntity = 1100000
BaseNPC = 6200


class Flags(Flag):
    Exit2Disabled = BaseFlag + 0
    Exit2Activated = BaseFlag + 1

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


class Regions(Region):
    InvaderTrigger = BaseEntity + 200
    InvaderSpawnPoint = BaseEntity + 201

    Exit2Prompt = BaseEntity + 251  # Arena dropoff.

    Boss1Trigger = BaseEntity + 292  # Done

    MimicNest = BaseEntity + 185


class ItemLots(ItemLot):
    Boss1Reward = BaseEntity + 290
