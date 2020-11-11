namespace RoguelikeSouls.ModProgram
{
    public static class Settings
    {
        public static int MinBasicEnemyTypeCount { get; } = 6;
        public static int MaxBasicEnemyTypeCount { get; } = 12;
        public static int LobosJrLabelCount { get; } = 5;
        public static int MaxCommonEnemyTypeCount { get; } = 15;
        public static int MaxUncommonEnemyTypeCount { get; } = 10;
        public static int MaxRareEnemyTypeCount { get; } = 10;
                
        public static double EnemyPatrolOdds { get; } = 0.5;
        public static int MinEnemyPatrolPointCount { get; } = 2;
        public static int MaxEnemyPatrolPointCount { get; } = 4;
        public static double MinPatrolPointGap { get; } = 5.0;
        public static double MaxPatrolPointGap { get; } = 15.0;
               
        public static double VagrantOdds { get; } = 0.5;
        public static double EvilVagrantOdds { get; } = 0.5;  // otherwise Good Vagrant
        public static double VagrantRedPhantomOdds { get; } = 0.1;
        public static double MornsteinVagrantRedPhantomOdds { get; } = 0.2;

        public static double PaintingOdds { get; } = 0.15;
        public static double VeryRareEnemyOdds { get; } = 0.3;
        public static double MornsteinVeryRareEnemyOdds { get; } = 0.6;
        public static double MimicOdds { get; } = 0.4;
        public static double MerchantOdds { get; } = 0.2;
        public static double ChesterOdds { get; } = 0.1;
        public static double InvaderOdds { get; } = 0.6;
        public static double AbyssPortalOdds { get; } = 0.33;
        public static double UncommonEnemyOdds { get; } = 0.25;  // otherwise common
        public static double LobosJrUncommonEnemyOdds { get; } = 0.33;  // otherwise common
        public static double TwinBossOdds { get; } = 0.5;  // odds only apply if twin boss is possible

        public static double MinEnemyDistanceFromSpawnPoint { get; } = 10.0;

        public static double MinInvaderDistanceFromTrigger { get; } = 10.0;
        public static double MaxInvaderDistanceFromTrigger { get; } = 20.0;

        // Map-specific odds.
        public static double BlighttownSwampOdds { get; } = 0.25;
    }
}
