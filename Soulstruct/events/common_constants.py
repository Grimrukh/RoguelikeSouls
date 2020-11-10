from soulstruct.game_types import *


# Map flag offset (+300 for second level, etc.):
#   2000-2049: Exit flags (disabled/activated).
#   2050-2059: Boss battle events (not flags).
#   2100-2199: Label flags.
#   2200-2249: Exit prompt events (not flags).
#   2250-2259: Ally assistance events.
#   2260-2269: Invader death events.


class CommonFlags(Flag):
    NeverEnabled = 1400  # Dummy flag for boss battles.
    InvaderUsedBaseFlag = 1500  # Mod use only.

    AndreHostile = 1600
    AndreDead = 1601
    VamosHostile = 1610
    VamosDead = 1611
    UndeadMerchantHostile = 1620
    UndeadMerchantDead = 1621
    ChesterHostile = 1640
    ChesterDead = 1641

    InDepths = 1800
    InUndeadBurg = 1801
    InUndeadParish = 1802
    InPaintedWorld = 1803  # Source area flag is also left on.
    InDarkroot = 1804
    InRoyalWood = 1805
    InOolacileTownship = 1806
    InChasm = 1807
    InCatacombs = 1808
    InTomb = 1809
    InGreatHollow = 1810
    InAshLake = 1811
    InBlighttown = 1812
    InDemonRuins = 1813
    InLostIzalith = 1814
    InSensFortress = 1815
    InAnorLondo = 1816
    InNewLondoRuins = 1817
    InDukesArchives = 1818
    InKiln = 1819

    # Flags that mark when end bosses have been defeated. These unlock larger treasure ranges.
    LordvesselObtained = 1850
    ArchivesBossDefeated = 1851
    TombBossDefeated = 1852
    NewLondoBossDefeated = 1853  # does not include normal Abyss battles
    IzalithBossDefeated = 1854
    ChasmBossDefeated = 1855
    KilnBossDefeated = 1856
    KilnAvailable = 1860  # Common EMEVD event.

    AbyssBattleRequest = 1870  # Causes mod to generate a thin New Londo map for Abyss battle.
    AbyssBattleRequestComplete = 1871  # Causes mod to generate a thin New Londo map for Abyss battle.
    AbyssBattleActive = 1872  # Causes New Londo EMEVD to return you home.
    DisableAbyssPortal = 1873  # Reset by mod when new map is created.

    LifeCount9 = 1900
    LifeCount8 = 1901
    LifeCount7 = 1902
    LifeCount6 = 1903
    LifeCount5 = 1904  # You start here if you haven't got Alvina's Ring.
    LifeCount4 = 1905
    LifeCount3 = 1906
    LifeCount2 = 1907
    LifeCount1 = 1908  # The run is over if you die at this point.
    Permadeath = 1909  # Game will keep trying to send you back to Firelink.

    InBossBattle = 1920  # If this is enabled when the map loads, you will be killed (and it will be disabled).

    BonfireCreationRequest = 1930  # Triggers mod program.
    BonfireRequestSuccessful = 1931  # Response from mod program.
    BonfireRequestUnsuccessful = 1932  # Response from mod program.
    OneBonfireCreated = 1933
    TwoBonfiresCreated = 1934  # Permitted with Solaire's Ring.

    AbyssBattleVictoryCountBase = 1940  # Don't use these ten flags.

    MapLevelBase = 1950  # Don't use these ten flags. Records current map level (1951 == level 1).

    # Flags enabled as soon as you start a run with the given ring in your inventory.
    # NO flag for Alvina Ring (flag 1960 represents map level 10).
    SolaireRingFlag = 1961
    SiegmeyerRingFlag = 1962
    LoganRingFlag = 1963
    QuelanaRingFlag = 1964
    HavelRingFlag = 1965
    MornsteinRingFlag = 1966
    LobosJrRingFlag = 1967

    SiegmeyerCarePackageReceived = 1970
    QuelanaCarePackageReceived = 1971

    StatBoostRequest = 1980  # Enabled in combination with a stat boost flag below.
    StatResetRequest = 1981
    AttunementClearRequest = 1982

    SpellRechargeRequest = 1985

    ShowUncurlMessage = 11020251

    OneAllyGiftReceived = 11022000
    TwoAllyGiftsReceived = 11022001
    AllyGiftUnavailable = 11022002  # Must beat at least one level on previous run to receive gift.
    RequestWarpToFirelink = 11022005
    SolaireRescued = 11022011
    SiegmeyerRescued = 11022012
    LoganRescued = 11022013
    QuelanaRescued = 11022014
    HavelRescued = 11022015
    MornsteinRescued = 11022016
    LobosJrRescued = 11022017

    InvisibleEffect = 11022020

    GetAlvinaRing = 11022030

    BoostVitalityBase = 11022100  # offset (0 to 9) indicates amount
    BoostAttunementBase = 11022110  # offset (0 to 9) indicates amount
    BoostEnduranceBase = 11022120  # offset (0 to 9) indicates amount
    BoostStrengthBase = 11022130
    BoostDexterityBase = 11022140
    BoostResistanceBase = 11022150
    BoostIntelligenceBase = 11022160
    BoostFaithBase = 11022170

    RequestLevelBannerBase = 11022300
    RequestCursedLevelBannerBase = 11022310
    RequestBonusLevelBanner = 11022320

    StartingEquipmentReceived = 11022450

    RunHasStarted = 11812000
    DoRunSetupFlag = 11812010
    RunSetupCompleteFlag = 11812011
    DoRunCleanupFlag = 11812020
    RunCleanupCompleteFlag = 11812021
    RequestFirelinkSpawnReset = 11812022
    HookErrorFlag = 11812098
    HookCheckFlag = 11812099
    BossCategoryUsedBaseFlag = 11812100
    AbyssBossCategoryUsedBaseFlag = 11812200

    # Key item lots.
    RustedKeyObtained = 50050010
    TarnishedKeyObtained = 50050020
    PolishedKeyObtained = 50050030
    GiantKeyObtained = 50050050
    HolySigilObtained = 50050060
    PiercingEyeObtained = 50050070
    SkeletonKeyObtained = 50050100


class CommonTexts(EventText):
    HookConnectionError = 79999
    DepartLevel = 80000
    ExitLocked = 80001
    ExitUnavailable = 80002
    # 80003 unused.
    ReturnToFirelink = 80004  # Run completed.
    StartRun = 80005
    MoreTreasureUnlocked = 80006
    MoreAbyssalTreasureUnlocked = 80007
    AbandonJourney = 80008
    FingersUncurl = 80009

    BellMustBeRung = 80010
    ButterflyMustBeDefeated = 80011
    LordvesselNotObtained = 80012
    DelveIntoAbyss = 80013
    FortressGateOpened = 80014
    DemonicMagicBlocks = 80015

    # Gift prompts now start at 80080.
    TwoGiftsAlreadyReceived = 80021
    GiftUnavailable = 80022
    LordvesselObtained = 80023
    DepartingArea = 80024

    BonfireCreationSuccess = 80030
    BonfireCreationFailed = 80031
    MaxBonfiresCreated = 80032
    UseUndeadFlame = 80033
    UseHeart = 80034

    SolaireRescued = 80041
    SiegmeyerRescued = 80042
    LoganRescued = 80043
    QuelanaRescued = 80044
    HavelRescued = 80045
    MornsteinRescued = 80046
    LobosJrRescued = 80047

    LevelMessageBase = 80050
    CursedLevelMessageBase = 80060
    BonusLevel = 80070

    ReceiveGiftAlvina = 80080
    ReceiveGiftSolaire = 80081
    ReceiveGiftSiegmeyer = 80082
    ReceiveGiftLogan = 80083
    ReceiveGiftQuelana = 80084
    ReceiveGiftHavel = 80085
    ReceiveGiftMornstein = 80086
    ReceiveGiftLobosJr = 80087

    RustedKeyRequired = 90001
    TarnishedKeyRequired = 90002
    PolishedKeyRequired = 90003
    GiantKeyRequired = 90005
    HolySigilRequired = 90006
    PiercingEyeRequired = 90007
    SkeletonKeysRequired = 90100

    # Don't need to change these in setup.
    UnlockedWithRustedKey = 10010860
    UnlockedWithTarnishedKey = 10010861
    UnlockedWithSkeletonKeys = 10010883


class CommonGoods(GoodParam):
    HandOfCessation = 600
    UndeadFlame = 601
    HeartOfStJude = 602
    MarkOfDeath = 603

    RustedKey = 2001
    TarnishedKey = 2002
    PolishedKey = 2003
    # MechanismKey = 2004  # Removed.
    GiantKey = 2005
    HolySigil = 2006
    PiercingEye = 2007
    # PalaceKey = 2008  # Removed.
    # 2009 unused at the moment.
    PeculiarDoll = 2010
    SkeletonKeys = 2100
    Lordvessel = 2510


class CommonEffects(IntEnum):
    DireEquipped = 8000
    DireDamageWayDown = 8001
    DireDamageDown = 8002
    DireDamageNoChange = 8003
    DireDamageUp = 8004
    DireDamageWayUp = 8005

    EnchantedHitTrigger = 8015

    ShieldHitTrigger = 8084
    # Too lazy to enumerate different shield hit triggers/effects.

    InvisibleEffect = 8190  # For mod flag.

    RollingDamageTrigger = 8490
    RollingDamageActive = 8491
    RollingDamageEffect = 8492

    AlvinaRing = 8800
    SolaireRing = 8801
    SiegmeyerRing = 8802
    LoganRing = 8803
    QuelanaRing = 8804
    HavelRing = 8805
    MornsteinRing = 8806
    LobosJrRing = 8807

    # Item effects.
    NewGamePlus = 8897
    QuitRun = 8898
    CreateBonfire = 8899


class CommonChrs(Character):
    Andre = 6100
    Vamos = 6110
    UndeadMerchant = 6120
    # CrestfallenMerchant = 6130
    MarvelousChester = 6140


class CommonItemLots(ItemLotParam):
    RustedKeyLot = 50010
    TarnishedKeyLot = 50020
    PolishedKeyLot = 50030
    GiantKeyLot = 50050
    HolySigilLot = 50060
    PiercingEyeLot = 50070
    SkeletonKeysLot = 50100

    MarkOfDeathLot = 50200

    HeartLot = 1020010

    SiegmeyerGiftLot = 1020020
    QuelanaGiftLot = 1020030


class Rings(RingParam):
    AlvinaRing = 100
    SolaireRing = 101
    SiegmeyerRing = 102
    LoganRing = 103
    QuelanaRing = 104
    HavelRing = 105
    MornsteinRing = 106
    LobosJrRing = 107


class PlayerAnimations(PlayerAnimation):
    StandingFadeIn = 10
    StandingFadeOut = 11
    SummonSpawn = 6951
