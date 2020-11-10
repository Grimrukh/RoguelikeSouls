from soulstruct.game_types import *


BaseFlag = 11502000
TempBaseFlag = 11505000
BaseEntity = 1500000
BaseNPC = 6200


class Flags(Flag):
    Exit1Disabled = BaseFlag + 0
    Exit1Activated = BaseFlag + 1
    Exit2Disabled = BaseFlag + 10
    Exit2Activated = BaseFlag + 11

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


class Regions(Region):
    InvaderTrigger = BaseEntity + 200
    InvaderSpawnPoint = BaseEntity + 201

    Exit2Prompt = BaseEntity + 251  # Warp to Anor Londo (unused, existing one used).

    Boss1Trigger = BaseEntity + 292  # Done
    Boss2Trigger = BaseEntity + 282  # Done

    MimicNest = BaseEntity + 185


class Objects(Object):
    Exit1Prompt = BaseEntity + 250  # Bridge to Parish.
    # Exit 2 is handled with original ring activation event.


class ItemLots(ItemLotParam):
    Boss1Reward = BaseEntity + 290
    Boss2Reward = BaseEntity + 280
