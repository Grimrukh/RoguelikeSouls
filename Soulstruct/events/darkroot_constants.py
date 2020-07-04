from soulstruct.game_types import *


BaseFlag = 11202000
TempBaseFlag = 11205000
BaseEntity = 1200000
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

    ButterflyDead = 11200900

    Boss1Dead = BaseFlag + 290
    Boss1IsTwin = BaseFlag + 291
    Boss1AllyAvailable = BaseFlag + 292
    Boss1AllyDone = BaseFlag + 293

    InvaderSummoned = TempBaseFlag + 40
    InvaderDismissed = TempBaseFlag + 41
    InvaderDead = BaseFlag + 90


class Chrs(Character):
    Logan = 6031

    MoonlightButterfly = 1200801
    Hydra = 1200810
    # Seven Hydra heads are 1200811 to 1200817.

    AllyBoss1 = BaseNPC + 0
    Boss1 = BaseEntity + 290
    Boss1Twin = BaseEntity + 291
    Invader = BaseNPC + 50

    Mimic = BaseEntity + 180


class Regions(Region):
    InvaderTrigger = BaseEntity + 200
    InvaderSpawnPoint = BaseEntity + 201

    Exit3Prompt = BaseEntity + 252  # Valley elevator. (Done)
    Exit4Prompt = BaseEntity + 253  # Near Grave of Artorias sword. (Done)

    Boss1Trigger = BaseEntity + 292  # Done

    MimicNest = BaseEntity + 185


class Objects(Object):
    Exit1Prompt = BaseEntity + 250  # Watchtower door. (Done)
    Exit2Prompt = BaseEntity + 251  # Titanite Demon room. (Done)


class ItemLots(ItemLot):
    Boss1Reward = BaseEntity + 290
