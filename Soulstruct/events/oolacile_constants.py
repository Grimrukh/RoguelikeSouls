from soulstruct.game_types import *


WoodBaseFlag = 11212000
WoodTempBaseFlag = 11215000
WoodBaseEntity = 1210000
WoodBaseNPC = 6200

TownshipBaseFlag = 11212300
TownshipTempBaseFlag = 11215300
TownshipBaseEntity = 1210300
TownshipBaseNPC = 6500

ChasmBaseFlag = 11212600
ChasmTempBaseFlag = 11215600
ChasmBaseEntity = 1210600
ChasmBaseNPC = 6800


class Flags(Flag):
    WoodExit1Disabled = WoodBaseFlag + 0
    WoodExit1Activated = WoodBaseFlag + 1
    WoodExit2Disabled = WoodBaseFlag + 10
    WoodExit2Activated = WoodBaseFlag + 11

    WoodBoss1Dead = WoodBaseFlag + 290
    WoodBoss1IsTwin = WoodBaseFlag + 291
    WoodBoss1AllyAvailable = WoodBaseFlag + 292
    WoodBoss1AllyDone = WoodBaseFlag + 293
    WoodBoss2Dead = WoodBaseFlag + 280
    WoodBoss2IsTwin = WoodBaseFlag + 281
    WoodBoss2AllyAvailable = WoodBaseFlag + 282
    WoodBoss2AllyDone = WoodBaseFlag + 283

    TownshipExit1Disabled = TownshipBaseFlag + 0
    TownshipExit1Activated = TownshipBaseFlag + 1
    TownshipExit2Disabled = TownshipBaseFlag + 10
    TownshipExit2Activated = TownshipBaseFlag + 11

    TownshipBoss1Dead = TownshipBaseFlag + 290
    TownshipBoss1IsTwin = TownshipBaseFlag + 291
    TownshipBoss1AllyAvailable = TownshipBaseFlag + 292
    TownshipBoss1AllyDone = TownshipBaseFlag + 293
    TownshipBoss2Dead = TownshipBaseFlag + 280
    TownshipBoss2IsTwin = TownshipBaseFlag + 281
    TownshipBoss2AllyAvailable = TownshipBaseFlag + 282
    TownshipBoss2AllyDone = TownshipBaseFlag + 283

    # ChasmExit1Disabled = ChasmBaseFlag + 0
    # ChasmExit1Activated = ChasmBaseFlag + 1
    ChasmExit2Disabled = ChasmBaseFlag + 10
    ChasmExit2Activated = ChasmBaseFlag + 11

    ChasmBoss1Dead = ChasmBaseFlag + 290
    ChasmBoss1IsTwin = ChasmBaseFlag + 291
    ChasmBoss1AllyAvailable = ChasmBaseFlag + 292
    ChasmBoss1AllyDone = ChasmBaseFlag + 293

    WoodInvaderSummoned = WoodTempBaseFlag + 40
    WoodInvaderDismissed = WoodTempBaseFlag + 41
    WoodInvaderDead = WoodBaseFlag + 90

    TownshipInvaderSummoned = TownshipTempBaseFlag + 40
    TownshipInvaderDismissed = TownshipTempBaseFlag + 41
    TownshipInvaderDead = TownshipBaseFlag + 90

    ChasmInvaderSummoned = ChasmTempBaseFlag + 40
    ChasmInvaderDismissed = ChasmTempBaseFlag + 41
    ChasmInvaderDead = ChasmBaseFlag + 90


class Chrs(Character):
    WoodAllyBoss1 = WoodBaseNPC + 0
    WoodBoss1 = WoodBaseEntity + 290
    WoodBoss1Twin = WoodBaseEntity + 291

    WoodAllyBoss2 = WoodBaseNPC + 1
    WoodBoss2 = WoodBaseEntity + 280
    WoodBoss2Twin = WoodBaseEntity + 281

    WoodInvader = WoodBaseNPC + 50

    WoodMimic = WoodBaseEntity + 180

    TownshipAllyBoss1 = TownshipBaseNPC + 0
    TownshipBoss1 = TownshipBaseEntity + 290
    TownshipBoss1Twin = TownshipBaseEntity + 291

    TownshipAllyBoss2 = TownshipBaseNPC + 1
    TownshipBoss2 = TownshipBaseEntity + 280
    TownshipBoss2Twin = TownshipBaseEntity + 281

    TownshipInvader = TownshipBaseNPC + 50

    TownshipMimic = TownshipBaseEntity + 180

    ChasmAllyBoss1 = ChasmBaseNPC + 0
    ChasmBoss1 = ChasmBaseEntity + 290
    ChasmBoss1Twin = ChasmBaseEntity + 291
    ChasmInvader = ChasmBaseNPC + 50

    ChasmMimic = ChasmBaseEntity + 180


class Regions(Region):
    WoodInvaderTrigger = WoodBaseEntity + 200
    WoodInvaderSpawnPoint = WoodBaseEntity + 201

    WoodBoss1Trigger = WoodBaseEntity + 292
    WoodBoss2Trigger = WoodBaseEntity + 282

    WoodMimicNest = WoodBaseEntity + 185

    TownshipInvaderTrigger = TownshipBaseEntity + 200
    TownshipInvaderSpawnPoint = TownshipBaseEntity + 201

    TownshipBoss1Trigger = TownshipBaseEntity + 292
    TownshipBoss2Trigger = TownshipBaseEntity + 282

    TownshipMimicNest = TownshipBaseEntity + 185

    ChasmInvaderTrigger = ChasmBaseEntity + 200
    ChasmInvaderSpawnPoint = ChasmBaseEntity + 201

    ChasmBoss1Trigger = ChasmBaseEntity + 292

    ChasmMimicNest = ChasmBaseEntity + 185


class Objects(Object):
    WoodExit1Prompt = WoodBaseEntity + 250  # Sanctuary tunnel.
    WoodExit2Prompt = WoodBaseEntity + 251  # Kalameet fog.

    TownshipExit1Prompt = TownshipBaseEntity + 250  # Gate to Artorias arena.
    TownshipExit2Prompt = TownshipBaseEntity + 251  # Prison entrance hall.

    ChasmExit2Prompt = ChasmBaseEntity + 250  # Bonfire appears after final boss.


class ItemLots(ItemLotParam):
    WoodBoss1Reward = WoodBaseEntity + 290
    WoodBoss2Reward = WoodBaseEntity + 280
    TownshipBoss1Reward = TownshipBaseEntity + 290
    TownshipBoss2Reward = TownshipBaseEntity + 280
    ChasmBoss1Reward = ChasmBaseEntity + 290
