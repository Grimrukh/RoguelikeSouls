from soulstruct.game_types import *


RuinsBaseFlag = 11412000
IzalithBaseFlag = 11412300
RuinsTempBaseFlag = 11415000
IzalithTempBaseFlag = 11415300
RuinsBaseEntity = 1410000
IzalithBaseEntity = 1410300
RuinsBaseNPC = 6200
IzalithBaseNPC = 6500


class Flags(Flag):
    RuinsExit1Disabled = RuinsBaseFlag + 0
    RuinsExit1Activated = RuinsBaseFlag + 1
    RuinsExit2Disabled = RuinsBaseFlag + 10
    RuinsExit2Activated = RuinsBaseFlag + 11
    RuinsExit3Disabled = RuinsBaseFlag + 20
    RuinsExit3Activated = RuinsBaseFlag + 21
    RuinsExit4Disabled = RuinsBaseFlag + 30
    RuinsExit4Activated = RuinsBaseFlag + 31

    RuinsBoss1Dead = RuinsBaseFlag + 290
    RuinsBoss1IsTwin = RuinsBaseFlag + 291
    RuinsBoss1AllyAvailable = RuinsBaseFlag + 292
    RuinsBoss1AllyDone = RuinsBaseFlag + 293

    RuinsBoss2Dead = RuinsBaseFlag + 280
    RuinsBoss2IsTwin = RuinsBaseFlag + 281
    RuinsBoss2AllyAvailable = RuinsBaseFlag + 282
    RuinsBoss2AllyDone = RuinsBaseFlag + 283

    RuinsInvaderSummoned = RuinsTempBaseFlag + 40
    RuinsInvaderDismissed = RuinsTempBaseFlag + 41
    RuinsInvaderDead = RuinsBaseFlag + 290

    IzalithExit1Disabled = IzalithBaseFlag + 0
    IzalithExit1Activated = IzalithBaseFlag + 1
    IzalithExit2Disabled = IzalithBaseFlag + 10
    IzalithExit2Activated = IzalithBaseFlag + 11
    IzalithExit3Disabled = IzalithBaseFlag + 20
    IzalithExit3Activated = IzalithBaseFlag + 21

    IzalithBoss1Dead = IzalithBaseFlag + 290
    IzalithBoss1IsTwin = IzalithBaseFlag + 291
    IzalithBoss1AllyAvailable = IzalithBaseFlag + 292
    IzalithBoss1AllyDone = IzalithBaseFlag + 293

    IzalithInvaderSummoned = IzalithTempBaseFlag + 40
    IzalithInvaderDismissed = IzalithTempBaseFlag + 41
    IzalithInvaderDead = IzalithBaseFlag + 290


class Chrs(Character):
    RuinsAllyBoss1 = RuinsBaseNPC + 0
    RuinsBoss1 = RuinsBaseEntity + 290
    RuinsBoss1Twin = RuinsBaseEntity + 291

    RuinsAllyBoss2 = RuinsBaseNPC + 1
    RuinsBoss2 = RuinsBaseEntity + 280
    RuinsBoss2Twin = RuinsBaseEntity + 281

    RuinsInvader = RuinsBaseNPC + 50

    IzalithAllyBoss1 = IzalithBaseNPC + 0
    IzalithBoss1 = IzalithBaseEntity + 290
    IzalithBoss1Twin = IzalithBaseEntity + 291
    IzalithInvader = IzalithBaseNPC + 50

    RuinsMimic = RuinsBaseEntity + 180
    IzalithMimic = IzalithBaseEntity + 180

    Quelana = 6041
    QuelanaBonewheel1 = 1410810
    QuelanaBonewheel2 = 1410811


class Regions(Region):
    RuinsBoss1Trigger = RuinsBaseEntity + 292
    RuinsBoss2Trigger = RuinsBaseEntity + 282

    RuinsInvaderTrigger = RuinsBaseEntity + 200
    RuinsInvaderSpawnPoint = RuinsBaseEntity + 201

    RuinsExit2Prompt = RuinsBaseEntity + 251  # Fair Lady elevator
    RuinsExit4Prompt = RuinsBaseEntity + 253  # Izalith shortcut door

    RuinsMimicNest = RuinsBaseEntity + 185

    IzalithBoss1Trigger = IzalithBaseEntity + 292
    IzalithInvaderTrigger = IzalithBaseEntity + 200
    IzalithInvaderSpawnPoint = IzalithBaseEntity + 201

    IzalithMimicNest = IzalithBaseEntity + 185


class Objects(Object):
    RuinsExit1Prompt = RuinsBaseEntity + 250  # Fair Lady tunnel
    RuinsExit3Prompt = RuinsBaseEntity + 252  # Centipede tunnel
    IzalithExit1Prompt = IzalithBaseEntity + 250  # Demon Ruins shortcut door
    IzalithExit2Prompt = IzalithBaseEntity + 251  # Lava dome exit
    IzalithExit3Prompt = IzalithBaseEntity + 252  # Bed of Chaos (bonfire)


class ItemLots(ItemLotParam):
    RuinsBoss1Reward = RuinsBaseEntity + 290
    RuinsBoss2Reward = RuinsBaseEntity + 280
    IzalithBoss1Reward = IzalithBaseEntity + 290
