from soulstruct.game_types import *


BaseFlag = 11302000
TempBaseFlag = 11305000
BaseEntity = 1300000
BaseNPC = 6200


class Flags(Flag):
    Exit1Disabled = BaseFlag + 0
    Exit1Activated = BaseFlag + 1
    Exit2Disabled = BaseFlag + 10  # Coffin.
    Exit2Activated = BaseFlag + 11
    Exit3Disabled = BaseFlag + 20
    Exit3Activated = BaseFlag + 21

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

    Boss1Trigger = BaseEntity + 292  # Done
    Boss2Trigger = BaseEntity + 282  # Done

    MimicNest = BaseEntity + 185


class Objects(Object):
    Exit1Prompt = BaseEntity + 250  # Fog to Firelink.
    # Exit2Prompt is manually handled with coffin events.
    Exit3Prompt = BaseEntity + 252  # Ladder after Pinwheel. (Done)


class ItemLots(ItemLot):
    Boss1Reward = BaseEntity + 290
    Boss2Reward = BaseEntity + 280
