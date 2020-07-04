from soulstruct.game_types import *


HollowBaseFlag = 11322000
LakeBaseFlag = 11322300
HollowTempBaseFlag = 11325000
LakeTempBaseFlag = 11325300
HollowBaseEntity = 1320000
LakeBaseEntity = 1320300
HollowBaseNPC = 6200
LakeBaseNPC = 6500


class Flags(Flag):
    HollowExit1Disabled = HollowBaseFlag + 0
    HollowExit1Activated = HollowBaseFlag + 1
    HollowExit2Disabled = HollowBaseFlag + 10
    HollowExit2Activated = HollowBaseFlag + 11

    HollowInvaderSummoned = HollowTempBaseFlag + 40
    HollowInvaderDismissed = HollowTempBaseFlag + 41
    HollowInvaderDead = HollowBaseFlag + 290

    LakeExit1Disabled = LakeBaseFlag + 0
    LakeExit1Activated = LakeBaseFlag + 1
    LakeExit2Disabled = LakeBaseFlag + 10
    LakeExit2Activated = LakeBaseFlag + 11

    LakeInvaderSummoned = LakeTempBaseFlag + 40
    LakeInvaderDismissed = LakeTempBaseFlag + 41
    LakeInvaderDead = LakeBaseFlag + 290


class Chrs(Character):
    HollowInvader = HollowBaseNPC + 50
    LakeInvader = LakeBaseNPC + 50

    StoneDragon = 1320800

    HollowMimic = HollowBaseEntity + 180
    LakeMimic = LakeBaseEntity + 180

    Siegmeyer = 6021
    SiegmeyerGolem = 1320710


class Regions(Region):
    HollowInvaderTrigger = HollowBaseEntity + 200
    HollowInvaderSpawnPoint = HollowBaseEntity + 201

    HollowMimicNest = HollowBaseEntity + 185

    LakeInvaderTrigger = LakeBaseEntity + 200
    LakeInvaderSpawnPoint = LakeBaseEntity + 201
    LakeExit2Prompt = LakeBaseEntity + 251  # Dragon

    LakeMimicNest = LakeBaseEntity + 185


class Objects(Object):
    HollowExit1Prompt = HollowBaseEntity + 250  # Top
    HollowExit2Prompt = HollowBaseEntity + 251  # Bottom
    LakeExit1Prompt = LakeBaseEntity + 250  # Hollow
