
namespace RoguelikeSouls.Installation
{
    enum GameFlag
    {
        None = -1,

        InvaderUsedBaseFlag = 1500,  // records which invaders have been used in the run
        VengeanceAvailableBaseFlag = 1550,  // TODO: records which invaders can be invaded back with Black Eye Orb
        MerchantStateBaseFlag = 1600,  // records which merchants are hostile/dead

        InDepths = 1800,
        InUndeadBurg = 1801,
        InUndeadParish = 1802,
        InPaintedWorld = 1803,
        InDarkroot = 1804,
        InRoyalWood = 1805,
        InOolacileTownshp = 1806,
        InChasm = 1807,
        InCatacombs = 1808,
        InTomb = 1809,
        InGreatHollow = 1810,
        InAshLake = 1811,
        InBlighttown = 1812,
        InDemonRuins = 1813,
        InLostIzalith = 1814,
        InSensFortress = 1815,
        InAnorLondo = 1816,
        InNewLondoRuins = 1817,
        InDukesArchives = 1818,
        InKiln = 1819,

        LordvesselObtained = 1850,
        ArchivesBossDefeated = 1851,
        TombBossDefeated = 1852,
        NewLondoBossDefeated = 1853,  // does not include normal Abyss battles
        IzalithBossDefeated = 1854,
        ChasmBossDefeated = 1855,
        KilnBossDefeated = 1856,
        KilnAvailable = 1860,  // Common EMEVD event.

        AbyssBattleRequest = 1870,  // Causes mod to generate a thin New Londo map for Abyss battle.
        AbyssBattleRequestComplete = 1871,  // Causes mod to generate a thin New Londo map for Abyss battle.
        AbyssBattleActive = 1872,  // Causes New Londo EMEVD to return you home.
        DisableAbyssPortal = 1873,  // Reset by mod when new map is created.

        LifeCountBaseFlag = 1900,  // run ends if you die while 1901 is enabled (one life)

        BonfireCreationRequest = 1930,  // Triggers mod program.
        BonfireRequestSuccessful = 1931,  // Response from mod program.
        BonfireRequestUnsuccessful = 1932,  // Response from mod program.
        OneBonfireCreated = 1933,
        TwoBonfiresCreated = 1934,

        AbyssBattleVictoryCountBase = 1940,  // if 1941 is enabled, one Abyss boss has been defeated

        MapLevelBaseFlag = 1950,  // records current level of map (if 1951 is enabled, current map is level 1).

        SolaireRingFlag = 1961,
        SiegmeyerRingFlag = 1962,
        LoganRingFlag = 1963,
        QuelanaRingFlag = 1964,
        HavelRingFlag = 1965,
        MornsteinRingFlag = 1966,
        LobosJrRingFlag = 1967,

        SiegmeyerCarePackageReceived = 1970,
        QuelanaCarePackageReceived = 1971,

        StatBoostRequest = 1980,
        StatResetRequest = 1981,
        AttunementClearRequest = 1982,
        SpellRechargeRequest = 1985,

        InvisibleEffect = 11022020,

        BoostVitalityBase = 11022100,  // offset (0 to 9) indicates amount
        BoostAttunementBase = 11022110,
        BoostEnduranceBase = 11022120,
        BoostStrengthBase = 11022130,
        BoostDexterityBase = 11022140,
        BoostResistanceBase = 11022150,
        BoostIntelligenceBase = 11022160,
        BoostFaithBase = 11022170,

        RequestLevelMessageBase = 11022300,

        RunStartedFlag = 11812000,
        DoRunSetupFlag = 11812010,
        RunSetupCompleteFlag = 11812011,
        DoRunCleanupFlag = 11812020,
        RunCleanupCompleteFlag = 11812021,
        HookErrorFlag = 11812098,  // enabled here and impedes game progress
        HookCheckFlag = 11812099,  // continually enabled in common EMEVD and disabled here
        BossCategoryUsedBaseFlag = 11812100,  // +0, +1, etc. for used categories
        AbyssBossCategoryUsedBaseFlag = 11812150,  // +0, +1, etc. for used categories
    }
}
