"""
linked:


strings:

"""
from soulstruct.darksouls1r.events import *
from common_constants import *
from oolacile_constants import *


def Constructor():
    """ 0: Event 0 """
    # Sanctuary Guardian arena
    BossBattle(
        0,
        Chrs.WoodBoss1, Chrs.WoodBoss1Twin, Flags.WoodBoss1IsTwin,
        Regions.WoodBoss1Trigger, Flags.WoodBoss1Dead, 1213800,
        ItemLots.WoodBoss1Reward,
        1211792, 1211793, 0, 0,  # Tunnel-side fog is permanent (prompt).
        1000, 1000,
    )

    # Ravine arena
    BossBattle(
        1,
        Chrs.WoodBoss2, Chrs.WoodBoss2Twin, Flags.WoodBoss2IsTwin,
        Regions.WoodBoss2Trigger, Flags.WoodBoss2Dead, 1213803,
        ItemLots.WoodBoss2Reward,
        1211692, 1211693, 0, 0,  # Old Kalameet fog is permanent (prompt).
        1000, 1000,
    )

    # Artorias arena
    BossBattle(
        2,
        Chrs.TownshipBoss1, Chrs.TownshipBoss1Twin, Flags.TownshipBoss1IsTwin,
        Regions.TownshipBoss1Trigger, Flags.TownshipBoss1Dead, 1213801,
        ItemLots.TownshipBoss1Reward,
        1211892, 1211893, 0, 0,  # Exit fog (890/891) is permanent (prompt).
        1000, 1000,
    )

    # Chasm hall arena
    BossBattle(
        3,
        Chrs.TownshipBoss2, Chrs.TownshipBoss2Twin, Flags.TownshipBoss2IsTwin,
        Regions.TownshipBoss2Trigger, Flags.TownshipBoss2Dead, 1213804,
        ItemLots.TownshipBoss2Reward,
        1211694, 1211695, 0, 0,  # Exit fog is permanent (prompt).
        1000, 1000,
    )

    # Manus arena
    BossBattle(
        4,
        Chrs.ChasmBoss1, Chrs.ChasmBoss1Twin, Flags.ChasmBoss1IsTwin,
        Regions.ChasmBoss1Trigger, Flags.ChasmBoss1Dead, 1213801,
        ItemLots.ChasmBoss1Reward,
        1211990, 1211991, 0, 0,
        1000, 1000,
    )

    SkipLinesIfClient(10)
    DisableObject(1211988)
    DeleteVFX(1211989, erase_root_only=False)
    DisableObject(1211994)
    DeleteVFX(1211995, erase_root_only=False)
    DisableObject(1211996)
    DeleteVFX(1211997, erase_root_only=False)
    DisableObject(1211998)
    DeleteVFX(1211999, erase_root_only=False)
    DisableObject(1211986)
    DeleteVFX(1211987, erase_root_only=False)
    DisableCollision(1213061)

    SkipLinesIfFlagOff(2, 11210539)
    EnableCollision(1213061)
    DisableCollision(1213060)

    # NOTE: collision 1213001 (h7400) used to "hem in" Kalameet and Artorias arenas. Probably only needed for Kalameet.

    InvincibleChasmFall()

    RegisterBonfire(11210992, obj=1211960, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210984, obj=1211970, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(11210976, obj=1211980, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterLadder(start_climbing_flag=11210210, stop_climbing_flag=11210211, obj=1211110)
    RegisterLadder(start_climbing_flag=11210212, stop_climbing_flag=11210213, obj=1211111)
    RegisterLadder(start_climbing_flag=11210214, stop_climbing_flag=11210215, obj=1211112)

    BreakIllusoryWall()
    IllusoryWallInvincible()

    # TODO: May want to inspect these Sif combat events.
    RunEvent(11215040)
    RunEvent(11215041)
    RunEvent(11210020)
    RunEvent(11215043)
    RunEvent(11215044)

    # Five chests per level.
    OpenChest(0, 1211650, 11210600)
    OpenChest(1, 1211651, 11210601)
    OpenChest(2, 1211652, 11210602)
    OpenChest(3, 1211653, 11210603)
    OpenChest(4, 1211654, 11210604)

    OpenChest(10, 1211660, 11210610)
    OpenChest(11, 1211661, 11210611)
    OpenChest(12, 1211662, 11210612)
    OpenChest(13, 1211663, 11210613)
    OpenChest(14, 1211664, 11210614)

    OpenChest(20, 1211670, 11210620)
    OpenChest(21, 1211671, 11210621)
    OpenChest(22, 1211672, 11210622)
    OpenChest(23, 1211673, 11210623)
    OpenChest(24, 1211674, 11210624)

    # TODO: Keep corpse on rope.
    CutCorpseOnRope(0, 1211700, 1211701, 125, 126)

    # Elevators.
    RunEvent(11210100)  # Township shortcut.
    TownshipElevatorFirstActivation()  # First activation (depends on start point).
    RunEvent(11210110)
    RunEvent(11210120)  # Royal Wood shortcut.
    WoodShortcutElevatorFirstActivation()  # First activation (depends on start point).
    # RunEvent(11210130)  # Chasm-Wood elevator disabled.
    # RunEvent(11210133)
    # RunEvent(11210140)  # Chasm-Township elevator disabled.
    RunEvent(11219100, slot=0, args=(11218102, 1211000, 0, 1, 1211001), arg_types='iiiBi')
    RunEvent(11219100, slot=1, args=(11218103, 1211000, 10, 0, 1211002), arg_types='iiiBi')
    RunEvent(11210170, slot=0, args=(11215220, 1213050, 1212105))
    RunEvent(11210170, slot=1, args=(11215221, 1213051, 1212115))
    RunEvent(11210170, slot=2, args=(11215222, 1213052, 1212125))
    RunEvent(11210170, slot=3, args=(11215223, 1213053, 1212135))
    RunEvent(11210170, slot=4, args=(11215224, 1213054, 1212145))

    # Light-based illusory walls.
    DisableSoundEvent(1213810)
    DisableSoundEvent(1213811)
    RunEvent(11210200, slot=0, args=(1211200, 1212200))
    RunEvent(11210200, slot=1, args=(1211201, 1212201))
    RunEvent(11210205, slot=0, args=(1211200, 1212200, 11210200))
    RunEvent(11210205, slot=1, args=(1211201, 1212201, 11210201))

    # Objects in Manus's arena.
    RunEvent(11215250, slot=0, args=(1211300, 1213160))
    RunEvent(11215250, slot=1, args=(1211301, 1213161))
    RunEvent(11215250, slot=2, args=(1211302, 1213162))
    RunEvent(11215250, slot=3, args=(1211303, 1213163))
    RunEvent(11215250, slot=4, args=(1211304, 1213164))
    RunEvent(11215250, slot=5, args=(1211305, 1213165))
    RunEvent(11215250, slot=6, args=(1211306, 1213166))
    RunEvent(11215250, slot=7, args=(1211307, 1213167))
    RunEvent(11215250, slot=8, args=(1211308, 1213168))
    RunEvent(11215250, slot=9, args=(1211309, 1213169))
    RunEvent(11215250, slot=10, args=(1211310, 1213170))
    RunEvent(11215250, slot=11, args=(1211311, 1213171))
    RunEvent(11215250, slot=12, args=(1211312, 1213172))
    RunEvent(11215250, slot=13, args=(1211313, 1213173))
    RunEvent(11215250, slot=14, args=(1211314, 1213174))
    RunEvent(11215250, slot=15, args=(1211315, 1213175))
    RunEvent(11215250, slot=16, args=(1211316, 1213176))
    RunEvent(11215250, slot=17, args=(1211317, 1213177))
    RunEvent(11215250, slot=18, args=(1211318, 1213178))
    RunEvent(11215250, slot=19, args=(1211319, 1213179))
    RunEvent(11215250, slot=20, args=(1211320, 1213180))
    RunEvent(11215250, slot=21, args=(1211321, 1213181))
    RunEvent(11215250, slot=22, args=(1211322, 1213182))
    RunEvent(11215250, slot=23, args=(1211323, 1213183))

    # Mimic.
    OpenMimic(0, Chrs.WoodMimic)
    ControlMimicState(0, Chrs.WoodMimic)
    HitMimicWithTalisman(0, Chrs.WoodMimic)
    TalismanWearsOffMimic(0, Chrs.WoodMimic)
    MimicReturnsToChest(0, Chrs.WoodMimic, Regions.WoodMimicNest)
    ReplanMimicAIOnLoad(0, Chrs.WoodMimic)

    OpenMimic(1, Chrs.TownshipMimic)
    ControlMimicState(1, Chrs.TownshipMimic)
    HitMimicWithTalisman(1, Chrs.TownshipMimic)
    TalismanWearsOffMimic(1, Chrs.TownshipMimic)
    MimicReturnsToChest(1, Chrs.TownshipMimic, Regions.TownshipMimicNest)
    ReplanMimicAIOnLoad(1, Chrs.TownshipMimic)

    OpenMimic(2, Chrs.ChasmMimic)
    ControlMimicState(2, Chrs.ChasmMimic)
    HitMimicWithTalisman(2, Chrs.ChasmMimic)
    TalismanWearsOffMimic(2, Chrs.ChasmMimic)
    MimicReturnsToChest(2, Chrs.ChasmMimic, Regions.ChasmMimicNest)
    ReplanMimicAIOnLoad(2, Chrs.ChasmMimic)

    for enemy in range(100):
        DespawnEnemy(enemy, 1210100 + enemy)
    for enemy in range(100):
        DespawnEnemy(100 + enemy, 1210400 + enemy)
    for enemy in range(100):
        DespawnEnemy(200 + enemy, 1210700 + enemy)

    # Holy Sigil isn't needed in this map, but just for fun.
    GetReward(0, 1210130, CommonItemLots.HolySigilLot, CommonFlags.HolySigilObtained)

    DepartLevelIfFlag(
        0, Objects.WoodExit1Prompt, CommonTexts.DepartLevel, Flags.WoodExit1Disabled, Flags.WoodBoss1Dead,
        Flags.WoodExit1Activated, CommonFlags.InRoyalWood)
    DepartLevelIfFlag(
        1, Objects.WoodExit2Prompt, CommonTexts.DepartLevel, Flags.WoodExit2Disabled, Flags.WoodBoss2Dead,
        Flags.WoodExit2Activated, CommonFlags.InRoyalWood)

    DepartLevelIfFlag(
        2, Objects.TownshipExit1Prompt, CommonTexts.DepartLevel, Flags.TownshipExit1Disabled, Flags.TownshipBoss1Dead,
        Flags.TownshipExit1Activated, CommonFlags.InOolacileTownship)
    DepartLevelIfFlag(
        3, Objects.TownshipExit2Prompt, CommonTexts.DepartLevel, Flags.TownshipExit2Disabled, Flags.TownshipBoss2Dead,
        Flags.TownshipExit2Activated, CommonFlags.InOolacileTownship)

    ActivateExitBonfire()

    ActivateAbyssPortal(0, 1210997, 1210998)


def Preconstructor():
    """ 50: Event 50 """
    InvaderTrigger(0, 6990, 6991, Chrs.WoodInvader, Regions.WoodInvaderTrigger, Flags.WoodInvaderDead)
    InvaderTrigger(1, 6990, 6991, Chrs.TownshipInvader, Regions.TownshipInvaderTrigger, Flags.TownshipInvaderDead)
    InvaderTrigger(2, 6990, 6991, Chrs.ChasmInvader, Regions.ChasmInvaderTrigger, Flags.ChasmInvaderDead)

    DisableObject(1211220)  # Artorias's gravestone.

    # Secret illusory floor.
    EnableObjectInvulnerability(1211250)
    RunEvent(11210346)
    RunEvent(11210347)
    EndOfAnimation(1211606, 0)
    EndOfAnimation(1211607, 0)

    AggravateMerchant(0, CommonChrs.Andre, CommonFlags.AndreHostile, 9000)
    AggravateMerchant(1, CommonChrs.Vamos, CommonFlags.VamosHostile, 9003)
    AggravateMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantHostile, 9000)
    AggravateMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterHostile, 0)

    KillMerchant(0, CommonChrs.Andre, CommonFlags.AndreDead)
    KillMerchant(1, CommonChrs.Vamos, CommonFlags.VamosDead)
    KillMerchant(2, CommonChrs.UndeadMerchant, CommonFlags.UndeadMerchantDead)
    KillMerchant(3, CommonChrs.MarvelousChester, CommonFlags.ChesterDead)


@RestartOnRest
def Event11215020():
    """ 11215020: Event 11215020 """
    IfFlagOff(1, 11210002)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1212998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1211990,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212997)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215021():
    """ 11215021: Event 11215021 """
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1212998, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1211990)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212997)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215022():
    """ 11215022: Event 11215022 """
    SkipLinesIfThisEventOn(3)
    IfFlagOff(1, 11210002)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210840, UpdateAuthority.Forced)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    SkipLinesIfConditionFalse(1, 2)
    IfFlagOn(0, 703)
    ActivateMultiplayerBuffs(1210840)


def Event11215027():
    """ 11215027: Event 11215027 """
    IfFlagOn(1, 11215020)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(120140, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=1212022, move_to_map=OOLACILE)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(120140, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=1212022,
                 move_to_map=OOLACILE)
    SkipLines(1)
    PlayCutscene(120140, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EnableFlag(11210031)


@RestartOnRest
def Event11215026():
    """ 11215026: Event 11215026 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableInvincibility(PLAYER)
    Wait(2.0)
    DisableInvincibility(PLAYER)


@RestartOnRest
def Event11215023():
    """ 11215023: Event 11215023 """
    EndIfFlagOn(17)
    SkipLinesIfThisEventOn(3)
    DisableAI(1210840)
    IfCharacterInsideRegion(0, PLAYER, region=1212021)
    EnableAI(1210840)
    EnableBossHealthBar(1210840, name=4500, slot=0)


def Event11215024():
    """ 11215024: Event 11215024 """
    DisableNetworkSync()
    IfFlagOff(1, 11210002)
    IfFlagOn(1, 11215023)
    SkipLinesIfHost(3)
    IfFlagOn(1, 11215021)
    IfCharacterInsideRegion(1, PLAYER, region=1212996)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212990)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213802)


def Event11215025():
    """ 11215025: Event 11215025 """
    DisableNetworkSync()
    IfFlagOn(1, 11215024)
    IfFlagOn(1, 11210002)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213802)


def Event11210002():
    """ 11210002: Event 11210002 """
    DisableObject(1211950)
    DisableObject(1211950)
    SkipLinesIfThisEventOff(4)
    DisableCharacter(1210840)
    Kill(1210840, award_souls=False)
    EnableObject(1211950)
    End()
    IfHealthLessThanOrEqual(0, 1210840, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210840, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210840)
    EnableFlag(11210002)
    EnableFlag(17)
    KillBoss(1210840)
    DisableObject(1211990)
    DeleteVFX(1211991, erase_root_only=True)
    DeleteVFX(1213100, erase_root_only=True)
    CreateTemporaryVFX(90014, anchor_entity=1211950, anchor_type=CoordEntityType.Object, model_point=-1)
    Wait(2.0)
    EnableObject(1211950)
    RegisterBonfire(11210992, obj=1211950, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0)


def Event11215250(_, arg_0_3: int, arg_4_7: int):
    """ 11215250: Event 11215250 """
    DeleteVFX(arg_4_7, erase_root_only=False)
    SkipLinesIfFlagOff(2, 11210002)
    DisableObject(arg_0_3)
    End()
    IfObjectDestroyed(-1, arg_0_3)
    IfCharacterDead(-1, 1210840)
    IfConditionTrue(0, input_condition=-1)
    DestroyObject(arg_0_3, slot=1)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    DisableObject(arg_0_3)


@RestartOnRest
def Event11215060():
    """ 11215060: Event 11215060 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, line_intersects=1211690,
                   boss_version=True)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212907)
    ForceAnimation(PLAYER, 7410, wait_for_completion=True)
    Restart()


def Event11215061():
    """ 11215061: Event 11215061 """
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1211690)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 1212907)
    ForceAnimation(PLAYER, 7410)
    Restart()


def Event11215062():
    """ 11215062: Event 11215062 """
    SkipLinesIfThisEventOn(4)
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfCharacterInsideRegion(1, PLAYER, region=1212909)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(2)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(1210401, UpdateAuthority.Forced)
    ActivateMultiplayerBuffs(1210401)


@RestartOnRest
def Event11215063():
    """ 11215063: Event 11215063 """
    EnableInvincibility(1210401)
    SkipLinesIfThisEventOn(9)
    DisableAI(1210401)
    IfFlagOn(1, 11215062)
    IfCharacterInsideRegion(1, PLAYER, region=1212906)
    IfStandingOnCollision(-1, 1213003)
    IfStandingOnCollision(-1, 1213004)
    IfStandingOnCollision(-1, 1213009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(1210401)
    DisableInvincibility(1210401)
    EnableBossHealthBar(1210401, name=4510, slot=0)
    EnableCollision(1213001)


def Event11215064():
    """ 11215064: Event 11215064 """
    DisableNetworkSync()
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215063)
    SkipLinesIfHost(2)
    IfFlagOn(1, 11215061)
    IfFlagOn(1, 11215067)
    IfCharacterInsideRegion(1, PLAYER, region=1212900)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(1213803)


def Event11215065():
    """ 11215065: Event 11215065 """
    DisableNetworkSync()
    IfFlagOn(1, 11215064)
    IfFlagOn(1, 11210004)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(1213803)


def Event11215066():
    """ 11215066: Event 11215066 """
    DisableNetworkSync()
    IfFlagOn(1, 11210592)
    IfFlagOff(1, 11210004)
    IfFlagOn(1, 11215062)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButton(1, prompt_text=10010403, anchor_entity=1212908, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, trigger_attribute=TriggerAttribute.All, line_intersects=1211690)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(75)
    EnableFlag(11215067)


def Event11210005():
    """ 11210005: Event 11210005 """
    EndIfThisEventOn()
    IfHealthLessThanOrEqual(0, 1210401, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=1210401, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 1210401)
    EnableFlag(11210004)
    EnableFlag(11210005)
    EnableFlag(121)
    KillBoss(1210401)
    DisableObject(1211690)
    DeleteVFX(1211691, erase_root_only=True)
    DisableCollision(1213001)


def Event11210340():
    """ 11210340: Event 11210340 """
    SkipLinesIfThisEventOff(3)
    EndIfFlagOn(11210341)
    Move(6760, destination=1212331, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=6760)
    End()
    IfHost(1)
    IfEntityWithinDistance(-1, 6760, PLAYER, radius=7.0)
    IfAttacked(-1, 6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(entity=6760, animation=7003, loop=False, wait_for_completion=True,
                                      skip_transition=False, arg1=5.0)
    DisableCharacter(6760)
    Move(6760, destination=1212331, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=6760)
    EnableCharacter(6760)


def Event11210341():
    """ 11210341: Event 11210341 """
    SkipLinesIfThisEventSlotOff(2)
    Move(6760, destination=1212332, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=6760)
    End()
    IfHost(1)
    IfFlagOn(1, 11210340)
    IfEntityWithinDistance(-1, 6760, PLAYER, radius=12.0)
    IfAttacked(-1, 6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(entity=6760, animation=7003, loop=False, wait_for_completion=True,
                                      skip_transition=False, arg1=5.0)
    DisableCharacter(6760)
    Move(6760, destination=1212332, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_parent=6760)
    EnableCharacter(6760)


def Event11210345():
    """ 11210345: Event 11210345 """
    SkipLinesIfThisEventOff(3)
    DisableCharacter(6760)
    DeleteVFX(1213125, erase_root_only=False)
    End()
    IfHost(1)
    IfFlagOn(1, 11210341)
    IfEntityWithinDistance(-1, 6760, PLAYER, radius=12.0)
    IfAttacked(-1, 6760, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation_WithUnknownEffect2(entity=6760, animation=7003, loop=False, wait_for_completion=True,
                                      skip_transition=False, arg1=5.0)
    DisableCharacter(6760)
    DeleteVFX(1213125, erase_root_only=True)


def Event11210346():
    """ 11210346: Event 11210346 """
    DisableNetworkSync()
    IfFlagOff(1, 11210345)
    IfCharacterInsideRegion(1, PLAYER, region=1212335)
    IfFlagOn(2, 11210345)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    AddSpecialEffect(PLAYER, 4161)
    Restart()


def Event11210347():
    """ 11210347: Event 11210347 """
    SkipLinesIfFlagOn(1, 11215045)
    SkipLinesIfFlagOff(2, 11210345)
    DisableObject(1211250)
    End()
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=1212336)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11215045)
    EndIfObjectDestroyed(1211250)
    DisableObjectInvulnerability(1211250)
    DestroyObject(1211250, slot=1)
    ForceAnimation(1211250, 0)
    PlaySoundEffect(anchor_entity=1211250, sound_type=SoundType.o_Object, sound_id=262000000)


def BreakIllusoryWall():
    """ 11210025: Event 11210025 """
    SkipLinesIfThisEventOff(2)
    DisableObject(1211240)
    End()
    IfObjectDestroyed(0, 1211240)
    End()


def IllusoryWallInvincible():
    """ 11210026: Blah. """
    if FlagEnabled(11210025):
        return
    EnableObjectInvulnerability(1211240)
    Await(HasGood(CommonGoods.PiercingEye))
    DisableObjectInvulnerability(1211240)
    Await(not HasGood(CommonGoods.PiercingEye))
    return RESTART


@RestartOnRest
def Event11215040():
    """ 11215040: Event 11215040 """
    DisableAI(1210500)
    DisableCharacter(1210500)
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfActionButton(1, prompt_text=50000000, anchor_entity=1212300, anchor_type=CoordEntityType.Region,
                   facing_angle=0.0, max_distance=0.0, model_point=0)
    IfConditionTrue(0, input_condition=1)
    DisplayBattlefieldMessage(140010, display_location_index=0)
    SkipLinesIfClient(1)
    ForceAnimation(1210501, 7008)
    WaitFrames(30)
    DisableCharacter(1210501)
    EnableFlag(11215042)
    DeleteVFX(1213100, erase_root_only=True)
    Wait(10.0)
    EnableCharacter(1210500)
    EnableAI(1210500)
    SetTeamType(1210500, TeamType.WhitePhantom)
    ForceAnimation(1210500, 7004)
    SkipLinesIfClient(2)
    DisplayBattlefieldMessage(20001110, display_location_index=0)
    SkipLines(1)
    DisplayBattlefieldMessage(20001111, display_location_index=0)
    WaitFrames(140)


@RestartOnRest
def Event11215041():
    """ 11215041: Event 11215041 """
    DisableCharacter(1210501)
    DisableAI(1210501)
    DisableAnimations(1210501)
    EndIfClient()
    IfFlagOn(1, 11210021)
    IfFlagOff(1, 17)
    IfCharacterInsideRegion(1, PLAYER, region=1212300)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(11215042)
    EnableCharacter(1210501)
    ForceAnimation(1210501, 7006, wait_for_completion=True)
    ForceAnimation(1210501, 7007, loop=True)
    IfCharacterOutsideRegion(2, PLAYER, region=1212300)
    IfFlagOn(2, 11215020)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(1210501, 7008, wait_for_completion=True)
    DisableCharacter(1210501)
    Restart()


@RestartOnRest
def Event11215044():
    """ 11215044: Event 11215044 """
    DeleteVFX(1213100, erase_root_only=True)
    EndIfClient()
    IfFlagOff(1, 17)
    IfFlagOn(1, 11210021)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(1213100)
    IfFlagOff(2, 17)
    IfFlagOn(2, 11210021)
    IfCharacterHuman(2, PLAYER)
    IfConditionFalse(0, input_condition=2)
    Restart()


def Event11210020():
    """ 11210020: Event 11210020 """
    EndIfFlagOn(17)
    IfCharacterDead(1, 1210840)
    IfCharacterAlive(1, 1210500)
    IfFlagOn(1, 11215040)
    IfCharacterDead(2, 1210500)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    DisableAI(1210500)
    WaitFrames(120)
    ForceAnimation(1210500, 7005, wait_for_completion=True)
    DisableCharacter(1210500)
    End()
    DisplayBattlefieldMessage(20001115, display_location_index=0)


# TODO: Sif limping. Add to every map? (No.)
@RestartOnRest
def Event11215043():
    """ 11215043: Event 11215043 """
    SkipLinesIfThisEventOn(1)
    IfHealthLessThanOrEqual(0, 1210500, 0.30000001192092896)
    AddSpecialEffect(1210500, 5401)


def OpenChest(_, arg_0_3: int, arg_4_7: int):
    """ 11210600: Open chest. """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    DisableTreasure(arg_0_3)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event11210100():
    """ 11210100: Event 11210100 """
    SkipLinesIfFlagOff(1, 11210101)
    EndOfAnimation(1211000, 0)
    SkipLinesIfFlagOn(1, 11210101)
    EndOfAnimation(1211000, 10)
    IfFlagOn(0, 11210103)
    IfFlagOff(0, 11215220)
    IfFlagOff(1, 11210101)
    IfCharacterInsideRegion(1, PLAYER, region=1212101)
    IfFlagOn(2, 11210102)
    IfFlagOn(2, 11210101)
    IfCharacterInsideRegion(2, PLAYER, region=1212100)
    IfFlagOn(3, 11210102)
    IfFlagOff(3, 11210101)
    IfCharacterInsideRegion(3, PLAYER, region=1212102)
    IfFlagOn(4, 11210101)
    IfCharacterInsideRegion(4, PLAYER, region=1212103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215220)
    SkipLinesIfFinishedConditionTrue(26, 2)
    SkipLinesIfFinishedConditionTrue(25, 4)
    EnableFlag(11210102)
    EnableFlag(11218102)
    SkipLinesIfFinishedConditionTrue(11, 1)
    IfAllPlayersOutsideRegion(-2, region=1212102)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagOff(7, 11218102)
    IfFlagOff(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212100)
    IfCharacterInsideRegion(5, PLAYER, region=1212103)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfFlagOff(7, 11218102)
    IfFlagOff(7, 11218103)
    IfConditionTrue(7, input_condition=-2)
    IfConditionTrue(0, input_condition=7)
    DisableFlag(11215220)
    Restart()
    EnableFlag(11218103)
    SkipLinesIfFinishedConditionTrue(11, 2)
    IfAllPlayersOutsideRegion(-3, region=1212103)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagOff(8, 11218102)
    IfFlagOff(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212101)
    IfCharacterInsideRegion(6, PLAYER, region=1212102)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfFlagOff(8, 11218102)
    IfFlagOff(8, 11218103)
    IfConditionTrue(8, input_condition=-3)
    IfConditionTrue(0, input_condition=8)
    DisableFlag(11215220)
    Restart()


def Event11219100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_12: uchar, arg_16_19: int):
    """ 11219100: Event 11219100 """
    IfFlagOn(0, arg_0_3)
    CreateTemporaryVFX(120030, anchor_entity=arg_16_19, anchor_type=CoordEntityType.Object, model_point=101)
    SetFlagState(11210101, state=arg_12_12)
    CreateObjectVFX(120029, obj=arg_4_7, model_point=191)
    ForceAnimation(arg_4_7, arg_8_11)
    WaitFrames(180)
    DeleteObjectVFX(arg_4_7, erase_root=False)
    DisableFlag(arg_0_3)
    Restart()


def TownshipElevatorFirstActivation():
    """ 11210103: Event 11210103 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(2, PLAYER, region=1212104)
    IfFlagOn(2, Flags.TownshipExit1Disabled)  # Start at top -> activate from bottom.
    IfCharacterInsideRegion(3, PLAYER, region=1212106)
    IfFlagOn(3, Flags.TownshipExit2Disabled)  # Start at bottom -> activate from top.
    IfConditionTrue(-1, 2)
    IfConditionTrue(-1, 3)
    IfConditionTrue(1, -1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210103)
    EnableFlag(11210102)  # Skips need to use summon button first.


def Event11210110():
    """ 11210110: Event 11210110 """
    SkipLinesIfFlagOff(1, 11210111)
    EndOfAnimation(1211010, 11)
    SkipLinesIfFlagOn(1, 11210111)
    EndOfAnimation(1211010, 1)
    IfFlagOff(0, 11215221)
    IfFlagOn(1, 11210111)
    IfCharacterInsideRegion(1, PLAYER, region=1212111)
    IfFlagOff(2, 11210111)
    IfCharacterInsideRegion(2, PLAYER, region=1212110)
    IfFlagOn(3, 11210111)
    IfCharacterInsideRegion(3, PLAYER, region=1212112)
    IfFlagOff(4, 11210111)
    IfCharacterInsideRegion(4, PLAYER, region=1212113)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215221)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryVFX(120030, anchor_entity=1211011, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210111)
    CreateObjectVFX(120029, obj=1211010, model_point=191)
    ForceAnimation(1211010, 1)
    WaitFrames(140)
    DeleteObjectVFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212112)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212110)
    IfCharacterInsideRegion(5, PLAYER, region=1212113)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215221)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=1211012, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210111)
    CreateObjectVFX(120029, obj=1211010, model_point=191)
    ForceAnimation(1211010, 11)
    WaitFrames(140)
    DeleteObjectVFX(1211010, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212113)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212111)
    IfCharacterInsideRegion(6, PLAYER, region=1212112)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215221)
    Restart()


def Event11210120():
    """ 11210120: Event 11210120 """
    SkipLinesIfFlagOff(1, 11210121)
    EndOfAnimation(1211020, 2)
    SkipLinesIfFlagOn(1, 11210121)
    EndOfAnimation(1211020, 12)
    IfFlagOn(0, 11210123)
    IfFlagOff(0, 11215222)
    IfFlagOff(1, 11210121)
    IfCharacterInsideRegion(1, PLAYER, region=1212121)
    IfFlagOn(2, 11210122)
    IfFlagOn(2, 11210121)
    IfCharacterInsideRegion(2, PLAYER, region=1212120)
    IfFlagOn(3, 11210122)
    IfFlagOff(3, 11210121)
    IfCharacterInsideRegion(3, PLAYER, region=1212122)
    IfFlagOn(4, 11210121)
    IfCharacterInsideRegion(4, PLAYER, region=1212123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215222)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryVFX(120030, anchor_entity=1211021, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210121)
    EnableFlag(11210122)
    CreateObjectVFX(120029, obj=1211020, model_point=191)
    ForceAnimation(1211020, 2)
    WaitFrames(140)
    DeleteObjectVFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212122)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212120)
    IfCharacterInsideRegion(5, PLAYER, region=1212123)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215222)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=1211022, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210121)
    CreateObjectVFX(120029, obj=1211020, model_point=191)
    ForceAnimation(1211020, 12)
    WaitFrames(140)
    DeleteObjectVFX(1211020, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212123)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212121)
    IfCharacterInsideRegion(6, PLAYER, region=1212122)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215222)
    Restart()


def WoodShortcutElevatorFirstActivation():
    """ 11210123: Event 11210123 """
    IfCharacterType(7, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=7)
    IfCharacterInsideRegion(2, PLAYER, region=1212124)
    IfFlagOn(2, Flags.WoodExit1Disabled)  # Start at top -> activate from bottom.
    IfCharacterInsideRegion(3, PLAYER, region=1212120)
    IfFlagOn(3, Flags.WoodExit2Disabled)  # Start at bottom -> activate from top.
    IfConditionTrue(-1, 2)
    IfConditionTrue(-1, 3)
    IfConditionTrue(1, -1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(11210123)
    EnableFlag(11210122)  # Skips need to use summon button first.


def Event11210130():
    """ 11210130: Event 11210130 """
    SkipLinesIfFlagOff(1, 11210131)
    EndOfAnimation(1211030, 3)
    SkipLinesIfFlagOn(1, 11210131)
    EndOfAnimation(1211030, 13)
    IfFlagOn(0, 11210133)
    IfFlagOff(0, 11215223)
    IfFlagOff(1, 11210131)
    IfCharacterInsideRegion(1, PLAYER, region=1212131)
    IfFlagOn(2, 11210132)
    IfFlagOn(2, 11210131)
    IfCharacterInsideRegion(2, PLAYER, region=1212130)
    IfFlagOn(3, 11210132)
    IfFlagOff(3, 11210131)
    IfCharacterInsideRegion(3, PLAYER, region=1212132)
    IfFlagOn(4, 11210131)
    IfCharacterInsideRegion(4, PLAYER, region=1212133)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215223)
    SkipLinesIfFinishedConditionTrue(25, 2)
    SkipLinesIfFinishedConditionTrue(24, 4)
    CreateTemporaryVFX(120030, anchor_entity=1211031, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210131)
    EnableFlag(11210132)
    CreateObjectVFX(120029, obj=1211030, model_point=191)
    ForceAnimation(1211030, 3)
    WaitFrames(240)
    DeleteObjectVFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212132)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212130)
    IfCharacterInsideRegion(5, PLAYER, region=1212133)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215223)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=1211032, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210131)
    CreateObjectVFX(120029, obj=1211030, model_point=191)
    ForceAnimation(1211030, 13)
    WaitFrames(240)
    DeleteObjectVFX(1211030, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212133)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212131)
    IfCharacterInsideRegion(6, PLAYER, region=1212132)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215223)
    Restart()


def Event11210133():
    """ 11210133: Event 11210133 """
    IfCharacterInsideRegion(0, PLAYER, region=1212134)
    EnableFlag(11210133)


def Event11210140():
    """ 11210140: Event 11210140 """
    SkipLinesIfFlagOff(1, 11210141)
    EndOfAnimation(1211040, 4)
    SkipLinesIfFlagOn(1, 11210141)
    EndOfAnimation(1211040, 14)
    IfFlagOff(0, 11215224)
    IfFlagOff(1, 11210141)
    IfCharacterInsideRegion(1, PLAYER, region=1212141)
    IfFlagOn(2, 11210141)
    IfCharacterInsideRegion(2, PLAYER, region=1212140)
    IfFlagOff(3, 11210141)
    IfCharacterInsideRegion(3, PLAYER, region=1212142)
    IfFlagOn(4, 11210141)
    IfCharacterInsideRegion(4, PLAYER, region=1212143)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    WaitForNetworkApproval(max_seconds=3.0)
    EnableFlag(11215224)
    EnableFlag(11210160)
    SkipLinesIfFinishedConditionTrue(24, 2)
    SkipLinesIfFinishedConditionTrue(23, 4)
    CreateTemporaryVFX(120030, anchor_entity=1211041, anchor_type=CoordEntityType.Object, model_point=101)
    EnableFlag(11210141)
    CreateObjectVFX(120029, obj=1211040, model_point=191)
    ForceAnimation(1211040, 4)
    WaitFrames(180)
    DeleteObjectVFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 1)
    IfAllPlayersOutsideRegion(-2, region=1212142)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-2, region=1212140)
    IfCharacterInsideRegion(5, PLAYER, region=1212143)
    IfHost(5)
    IfTimeElapsed(5, 1.0)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(11215224)
    Restart()
    CreateTemporaryVFX(120030, anchor_entity=1211042, anchor_type=CoordEntityType.Object, model_point=101)
    DisableFlag(11210141)
    CreateObjectVFX(120029, obj=1211040, model_point=191)
    ForceAnimation(1211040, 14)
    WaitFrames(180)
    DeleteObjectVFX(1211040, erase_root=False)
    SkipLinesIfFinishedConditionTrue(8, 2)
    IfAllPlayersOutsideRegion(-3, region=1212143)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()
    IfAllPlayersOutsideRegion(-3, region=1212141)
    IfCharacterInsideRegion(6, PLAYER, region=1212142)
    IfHost(6)
    IfTimeElapsed(6, 1.0)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    DisableFlag(11215224)
    Restart()


def Event11210170(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210170: Event 11210170 """
    DisableCollision(arg_4_7)
    SkipLinesIfNotEqual(1, left=arg_0_3, right=11215220)
    IfAllPlayersOutsideRegion(1, region=1212100)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagOn(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableCollision(arg_4_7)
    SkipLinesIfNotEqual(3, left=arg_0_3, right=11215220)
    IfCharacterInsideRegion(7, PLAYER, region=1212100)
    IfTimeElapsed(7, 2.0)
    IfConditionTrue(-1, input_condition=7)
    IfAllPlayersOutsideRegion(-1, region=arg_8_11)
    IfFlagOff(-1, arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    Wait(5.0)
    Restart()


@RestartOnRest
def OpenMimic(_, mimic: Character):
    """ 11215810: Mimic is activated by the player. """
    IfHealthGreaterThan(1, mimic, 0.0)
    IfCharacterBackreadEnabled(1, mimic)
    IfCharacterHasSpecialEffect(1, mimic, 5421)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    IfConditionFalse(1, input_condition=2)
    IfActionButton(1, prompt_text=10010400, anchor_entity=mimic, anchor_type=CoordEntityType.Character,
                   facing_angle=45.0, max_distance=1.2000000476837158, model_point=7,
                   trigger_attribute=TriggerAttribute.All)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=mimic, destination_type=CoordEntityType.Character, model_point=100,
         copy_draw_parent=mimic)
    ForceAnimation(PLAYER, 7521)
    AICommand(mimic, command_id=10, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def ControlMimicState(_, mimic: Character):
    """ 11215820: Mimic state control. """
    IfCharacterDoesNotHaveSpecialEffect(1, mimic, 5420)
    IfAttacked(1, mimic, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    IfCharacterBackreadDisabled(7, mimic)
    RestartIfConditionTrue(7)
    IfCharacterHasSpecialEffect(2, mimic, 5421)
    SkipLinesIfConditionFalse(1, 2)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(3, mimic, 5422)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(4, mimic, 5423)
    SkipLinesIfConditionFalse(1, 4)
    ForceAnimation(mimic, 3001, wait_for_completion=True)
    IfCharacterHasSpecialEffect(5, mimic, 5424)
    SkipLinesIfConditionFalse(1, 5)
    ForceAnimation(mimic, 3006, wait_for_completion=True)
    ReplanAI(mimic)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    Restart()


@RestartOnRest
def HitMimicWithTalisman(_, mimic: Character):
    """ 11215830: Mimic goes to sleep. """
    IfCharacterHasSpecialEffect(1, mimic, 5421)
    IfCharacterHasSpecialEffect(1, mimic, 3150)
    IfCharacterHasSpecialEffect(2, mimic, 5420)
    IfCharacterHasSpecialEffect(2, mimic, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(mimic, command_id=200, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(mimic, command_id=210, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, mimic, 5420)
    IfCharacterHasSpecialEffect(-2, mimic, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def TalismanWearsOffMimic(_, mimic: Character):
    """ 11215840: Mimic wakes up again. """
    IfCharacterHasSpecialEffect(1, mimic, 5422)
    IfCharacterDoesNotHaveSpecialEffect(1, mimic, 3150)
    IfCharacterHasSpecialEffect(2, mimic, 5423)
    IfCharacterDoesNotHaveSpecialEffect(2, mimic, 3150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(mimic, 3150)
    CancelSpecialEffect(mimic, 3151)
    SkipLinesIfFinishedConditionTrue(5, 2)
    AICommand(mimic, command_id=201, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    SkipLines(4)
    AICommand(mimic, command_id=211, slot=0)
    ReplanAI(mimic)
    Wait(0.10000000149011612)
    AICommand(mimic, command_id=-1, slot=0)
    IfCharacterHasSpecialEffect(-2, mimic, 5420)
    IfCharacterHasSpecialEffect(-2, mimic, 5421)
    IfConditionTrue(0, input_condition=-2)
    Restart()


@RestartOnRest
def MimicReturnsToChest(_, mimic: Character, mimic_nest: Region):
    """ 11215850: Mimic enters chest form. """
    IfSingleplayer(1)
    IfCharacterInsideRegion(1, mimic, region=mimic_nest)
    IfCharacterBackreadDisabled(1, mimic)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(mimic, 5421)
    ClearTargetList(mimic)
    ReplanAI(mimic)
    Move(mimic, destination=mimic_nest, destination_type=CoordEntityType.Region, short_move=True)
    IfCharacterBackreadEnabled(0, mimic)
    Restart()


@RestartOnRest
def ReplanMimicAIOnLoad(_, mimic: int):
    """ 11215860: Force Mimic to play animation 0 and replan its AI if it's in backread on map load. """
    EndIfHost()
    IfCharacterBackreadDisabled(1, mimic)
    EndIfConditionTrue(1)
    ResetAnimation(mimic, disable_interpolation=True)
    ForceAnimation(mimic, 0)
    ReplanAI(mimic)


def Event11210200(_, arg_0_3: int, arg_4_7: int):
    """ 11210200: Event 11210200 """
    SkipLinesIfThisEventSlotOff(2)
    DisableObject(arg_0_3)
    End()
    IfCharacterHasSpecialEffect(-1, PLAYER, 620)
    IfCharacterHasSpecialEffect(-1, PLAYER, 6950)
    IfSkullLanternActive(-1)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=262000000)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    DisableObject(arg_0_3)


def Event11210205(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 11210205: Event 11210205 """
    DisableNetworkSync()
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EndIfFlagOn(arg_8_11)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=120199999)
    Wait(2.0)
    Restart()


def CutCorpseOnRope(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 11210230: Event 11210230 """
    if not THIS_SLOT_FLAG:
        EndOfAnimation(arg_4_7, arg_12_15)
        PostDestruction(arg_0_3, slot=1)
        # EnableTreasure(arg_4_7)
        return
    DisableTreasure(arg_4_7)
    SkipLinesIfClient(1)
    CreateObjectVFX(99005, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, arg_8_11, loop=True)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, arg_12_15, wait_for_completion=True)
    SkipLinesIfClient(1)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    # EnableTreasure(arg_4_7)


@RestartOnRest
def BossBattle(_, boss: Character, boss_twin: Character, twin_enabled: Flag,
               trigger_region: Region, dead_flag: Flag, music_id: int, reward_item_lot: ItemLotParam,
               fog_1_object: int, fog_1_sfx: int,
               fog_2_object: int, fog_2_sfx: int,
               boss_name: short, boss_twin_name: short):
    """ 11212080: All-in-one boss event for simplicity. """
    DisableSoundEvent(music_id)
    DisableObject(fog_1_object)
    DeleteVFX(fog_1_sfx, erase_root_only=False)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteVFX(fog_2_sfx, erase_root_only=False)

    if dead_flag:
        DisableCharacter(boss)
        if twin_enabled:
            DisableCharacter(boss_twin)
        return

    DisableCharacter(boss)
    if twin_enabled:
        DisableCharacter(boss_twin)

    Await(trigger_region)
    EnableFlag(CommonFlags.InBossBattle)

    EnableObject(fog_1_object)
    CreateVFX(fog_1_sfx)
    if fog_2_object != 0:
        EnableObject(fog_2_object)
        CreateVFX(fog_2_sfx)

    if twin_enabled:
        EnableCharacter(boss_twin)
        EnableInvincibility(boss_twin)
        ForceAnimation(boss_twin, 10)
    EnableCharacter(boss)
    EnableInvincibility(boss)
    ForceAnimation(boss, 10)
    if twin_enabled:
        SetTeamType(boss, TeamType.Enemy)
        SetTeamType(boss_twin, TeamType.Enemy)
    Wait(2.0)
    ResetAnimation(boss)
    ReplanAI(boss)
    if twin_enabled:
        ResetAnimation(boss_twin)
        ReplanAI(boss_twin)
    DisableInvincibility(boss)
    if twin_enabled:
        DisableInvincibility(boss_twin)

    EnableSoundEvent(music_id)
    EnableBossHealthBar(boss, boss_name, slot=0)
    if twin_enabled:
        EnableBossHealthBar(boss_twin, boss_twin_name, slot=1)

    Await(IsDead(boss) and (not twin_enabled or IsDead(boss_twin)))
    DisableFlag(CommonFlags.InBossBattle)

    EnableFlag(dead_flag)
    DisableBossHealthBar(boss, boss_name, slot=0)  # Will disable twin's bar automatically.
    DisableObject(fog_1_object)
    DeleteVFX(fog_1_sfx, erase_root_only=True)
    if fog_2_object != 0:
        DisableObject(fog_2_object)
        DeleteVFX(fog_2_sfx, erase_root_only=True)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(2.0)
    DisplayBanner(BannerType.VictoryAchieved)
    DisableSoundEvent(music_id)
    AwardItemLot(reward_item_lot, True)


def InvaderTrigger(_, invasion_message: int, dead_message: int, invader: Character, trigger: Region, dead_flag: Flag):
    """ 11212260: Invasion is triggered. Human not needed. """
    DisableCharacter(invader)
    if THIS_SLOT_FLAG:
        return
    IfHost(1)
    IfFlagOff(1, dead_flag)
    IfCharacterInsideRegion(1, PLAYER, region=trigger)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableCharacter(invader)
    ForceAnimation(invader, PlayerAnimations.SummonSpawn, wait_for_completion=True)
    ReplanAI(invader)
    SetTeamType(invader, TeamType.BlackPhantom)
    DisplayBattlefieldMessage(invasion_message, 0)

    # TODO: If player dies while invader is active (two possible outcomes here), give them a Black Eye Orb and register
    #  future possible vengeance invasion by checking that flag in the run manager.
    Await(IsDead(invader))

    DisplayBattlefieldMessage(dead_message, 0)
    EnableFlag(dead_flag)


@RestartOnRest
def DespawnEnemy(_, enemy: int):
    """ 11213000: Despawn enemy. """
    if THIS_SLOT_FLAG:
        DisableCharacter(enemy)
        Kill(enemy, False)
        return
    Await(IsDead(enemy))
    return


def DepartLevelUnconditional(_, prompt_region: Region, prompt_text: Text, disabled_flag: Flag,
                             end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11212200: Depart level by interacting with prompt. No conditions. """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and ActionButton(
        prompt_text, prompt_region, anchor_type=CoordEntityType.Object))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def DepartLevelIfFlag(_, prompt_object: Object, prompt_text: Text, disabled_flag: Flag, required_flag: Flag,
                      end_trigger_flag: Flag, in_map_flag: Flag):
    """ 11212210: Depart level by interacting with prompt after boss is defeated. """
    if not FlagEnabled(in_map_flag):
        return
    Await(FlagDisabled(disabled_flag) and FlagEnabled(required_flag) and ActionButton(
        prompt_text, prompt_object, anchor_type=CoordEntityType.Object))
    EnableFlag(end_trigger_flag)
    DisplayBattlefieldMessage(CommonTexts.DepartingArea, 0)


def ActivateExitBonfire():
    """ 11212230: Defeat boss to make bonfire appear and finish level. Always goes back to Firelink. """
    if not Flags.ChasmBoss1Dead:
        DisableObject(Objects.ChasmExit2Prompt)
        Await(Flags.ChasmBoss1Dead)
        CreateTemporaryVFX(90014, anchor_entity=Objects.ChasmExit2Prompt, anchor_type=CoordEntityType.Object,
                          model_point=-1)
        Wait(2.0)
        EnableObject(Objects.ChasmExit2Prompt)
        if not CommonFlags.ChasmBossDefeated:
            if CommonFlags.LordvesselObtained:
                DisplayStatus(CommonTexts.MoreTreasureUnlocked)
                EnableFlag(CommonFlags.ChasmBossDefeated)
            else:
                DisplayStatus(CommonTexts.LordvesselNotObtained)

    # Wait for player to touch bonfire.
    Await(not Flags.ChasmExit2Disabled and ActionButton(
        CommonTexts.ReturnToFirelink, Objects.ChasmExit2Prompt, max_distance=2.0))
    AddSpecialEffect(PLAYER, CommonEffects.QuitRun)


def InvincibleChasmFall():
    """ 11210300: Fall safely into Chasm."""
    Await(Regions.ChasmBoss1Trigger)
    EnableInvincibility(PLAYER)
    Wait(3.0)
    DisableInvincibility(PLAYER)
    return RESTART


def GetReward(_, enemy: int, item_lot: ItemLotParam, item_lot_flag: Flag):
    """ 11212270: Enemy awards a given item lot when killed. """
    if THIS_SLOT_FLAG:
        return
    if item_lot_flag:
        return
    Await(IsDead(enemy))
    AwardItemLot(item_lot)
    EnableFlag(item_lot_flag)


def ActivateAbyssPortal(_, portal: int, fx_id: int):
    """ 11212999: Activate Abyss portal. """
    if CommonFlags.DisableAbyssPortal:
        DeleteVFX(fx_id, erase_root_only=False)
        return
    Await(ActionButton(
        CommonTexts.DelveIntoAbyss, portal, facing_angle=180.0, max_distance=2.0,
        anchor_type=CoordEntityType.Character))

    DisableFlag(CommonFlags.AbyssBattleRequestComplete)
    EnableFlag(CommonFlags.AbyssBattleRequest)
    # Wait for mod to generate Abyss map.
    Await(CommonFlags.AbyssBattleRequestComplete)
    EnableFlag(CommonFlags.DisableAbyssPortal)
    EnableFlag(CommonFlags.AbyssBattleActive)
    WarpToMap(NEW_LONDO_RUINS, 1600243)


@RestartOnRest
def AggravateMerchant(_, merchant: int, hostile_flag: int, standby_animation: int):
    """ 11212950: Merchant becomes aggravated when you attack them to below 90% HP. """
    SetTeamType(merchant, TeamType.Ally)
    SetStandbyAnimationSettings(merchant, standby_animation=standby_animation)
    Await(FlagEnabled(hostile_flag) or IsAttacked(merchant, PLAYER) and HealthRatio(merchant) <= 0.9)
    SetTeamTypeAndExitStandbyAnimation(merchant, TeamType.HostileAlly)
    ReplanAI(merchant)
    EnableFlag(hostile_flag)


@RestartOnRest
def KillMerchant(_, merchant: int, dead_flag: int):
    """ 11212960: Merchant dies for the duration of the run. """
    if FlagEnabled(dead_flag):
        DisableCharacter(merchant)
        return
    Await(IsDead(merchant))
    EnableFlag(dead_flag)
