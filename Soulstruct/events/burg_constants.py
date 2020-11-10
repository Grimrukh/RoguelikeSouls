from soulstruct.game_types import *


BurgBaseFlag = 11012000
ParishBaseFlag = 11012300
BurgTempBaseFlag = 11015000
ParishTempBaseFlag = 11015300
BurgBaseEntity = 1010000
ParishBaseEntity = 1010300
BurgBaseNPC = 6200
ParishBaseNPC = 6500


class Flags(Flag):
    BurgExit1Disabled = BurgBaseFlag + 0
    BurgExit1Activated = BurgBaseFlag + 1
    BurgExit2Disabled = BurgBaseFlag + 10
    BurgExit2Activated = BurgBaseFlag + 11
    BurgExit3Disabled = BurgBaseFlag + 20
    BurgExit3Activated = BurgBaseFlag + 21
    BurgExit4Disabled = BurgBaseFlag + 30
    BurgExit4Activated = BurgBaseFlag + 31
    BurgExit5Disabled = BurgBaseFlag + 40
    BurgExit5Activated = BurgBaseFlag + 41
    BurgExit6Disabled = BurgBaseFlag + 50
    BurgExit6Activated = BurgBaseFlag + 51

    BurgBoss1Dead = BurgBaseFlag + 290
    BurgBoss1IsTwin = BurgBaseFlag + 291
    BurgBoss1AllyAvailable = BurgBaseFlag + 292
    BurgBoss1AllyDone = BurgBaseFlag + 293
    BurgBoss2Dead = BurgBaseFlag + 280
    BurgBoss2IsTwin = BurgBaseFlag + 281
    BurgBoss2AllyAvailable = BurgBaseFlag + 282
    BurgBoss2AllyDone = BurgBaseFlag + 283

    BurgInvaderSummoned = BurgTempBaseFlag + 40
    BurgInvaderDismissed = BurgTempBaseFlag + 41
    BurgInvaderDead = BurgBaseFlag + 290

    ParishExit1Disabled = ParishBaseFlag + 0
    ParishExit1Activated = ParishBaseFlag + 1
    ParishExit2Disabled = ParishBaseFlag + 10
    ParishExit2Activated = ParishBaseFlag + 11
    ParishExit3Disabled = ParishBaseFlag + 20
    ParishExit3Activated = ParishBaseFlag + 21
    ParishExit4Disabled = ParishBaseFlag + 30
    ParishExit4Activated = ParishBaseFlag + 31

    ParishBoss1Dead = ParishBaseFlag + 290
    ParishBoss1IsTwin = ParishBaseFlag + 291
    ParishBoss1AllyAvailable = ParishBaseFlag + 292
    ParishBoss1AllyDone = ParishBaseFlag + 293
    ParishBoss2Dead = ParishBaseFlag + 280
    ParishBoss2IsTwin = ParishBaseFlag + 281
    ParishBoss2AllyAvailable = ParishBaseFlag + 282
    ParishBoss2AllyDone = ParishBaseFlag + 283

    ParishInvaderSummoned = ParishTempBaseFlag + 40
    ParishInvaderDismissed = ParishTempBaseFlag + 41
    ParishInvaderDead = ParishBaseFlag + 290


class Chrs(Character):
    BurgAllyBoss1 = BurgBaseNPC + 0
    BurgBoss1 = BurgBaseEntity + 290
    BurgBoss1Twin = BurgBaseEntity + 291
    BurgAllyBoss2 = BurgBaseNPC + 1
    BurgBoss2 = BurgBaseEntity + 280
    BurgBoss2Twin = BurgBaseEntity + 281
    BurgInvader = BurgBaseNPC + 50

    ParishAllyBoss1 = ParishBaseNPC + 0
    ParishBoss1 = ParishBaseEntity + 290
    ParishBoss1Twin = ParishBaseEntity + 291
    ParishAllyBoss2 = ParishBaseNPC + 1
    ParishBoss2 = ParishBaseEntity + 280
    ParishBoss2Twin = ParishBaseEntity + 281
    ParishInvader = ParishBaseNPC + 50

    BurgMimic = BurgBaseEntity + 180
    ParishMimic = ParishBaseEntity + 180

    LobosJr = 6071


class Regions(Region):
    BurgBoss1Trigger = BurgBaseEntity + 292  # Done
    BurgBoss2Trigger = BurgBaseEntity + 282  # Done
    BurgInvaderTrigger = BurgBaseEntity + 200
    BurgInvaderSpawnPoint = BurgBaseEntity + 201

    BurgMimicNest = BurgBaseEntity + 185

    ParishBoss1Trigger = ParishBaseEntity + 292  # Done
    ParishBoss2Trigger = ParishBaseEntity + 282  # Done
    ParishInvaderTrigger = ParishBaseEntity + 200
    ParishInvaderSpawnPoint = ParishBaseEntity + 201

    ParishExit3Prompt = ParishBaseEntity + 252  # Parish elevator. (Done)
    # No exit at Sunlight Portcullis.

    ParishMimicNest = ParishBaseEntity + 185


class Objects(Object):
    BurgExit1Prompt = BurgBaseEntity + 250  # Parish bridge (portcullis lever). (Done)
    BurgExit2Prompt = BurgBaseEntity + 251  # Parish bridge (door below). (Done)
    BurgExit3Prompt = BurgBaseEntity + 252  # Firelink aqueduct (near end). (Done)
    BurgExit4Prompt = BurgBaseEntity + 253  # Firelink aqueduct (far end). (Done)
    BurgExit5Prompt = BurgBaseEntity + 254  # Watchtower basement. (Done)
    BurgExit6Prompt = BurgBaseEntity + 255  # Depths door. (Done)

    ParishExit1Prompt = ParishBaseEntity + 250  # Sen's Fortress fog (bell required). (Done)
    ParishExit2Prompt = ParishBaseEntity + 251  # Titanite Demon room. (Done)
    ParishExit4Prompt = ParishBaseEntity + 253  # Rat room. (Done)


class ItemLots(ItemLotParam):
    BurgBoss1Reward = BurgBaseEntity + 290
    BurgBoss2Reward = BurgBaseEntity + 280
    ParishBoss1Reward = ParishBaseEntity + 290
    ParishBoss2Reward = ParishBaseEntity + 280
