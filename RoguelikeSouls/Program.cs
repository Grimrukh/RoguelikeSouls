using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Threading;
using GameHook;
using SoulsFormatsMod;
using RoguelikeSouls.ModProgram;
using RoguelikeSouls.Extensions;
using RoguelikeSouls.Installation;
using System.Windows.Forms;

namespace RoguelikeSouls
{
    class Program
    {
        static string MOD_PATH = null;

        static List<string> SoyPuns { get; } = new List<string>()
        {
            "When I destroyed that crystal, man, was he ever Seath-ing with rage.",
            "I joined the Bank of Lordran so my souls could collect Gwyn-terest.",
            "My friend's not happy about those hostile crab enemies that spawn every now and again - he goes on vague-rants about them all the time.",
            "This mod is pretty tough. In fact, a snake told me it really framped up the difficulty.",
            "That forest behind the Artorias crest is kind of spooky - I start to Shiva just thinking about it.",
            "Lautrec's not so bad a guy, he actually made me a souffle as a peace offering! It was very Carim-y.",
            "You're going to need some weapons for this! Don't forget to estoc up before you go.",
            "Artorias was trying to figure out how to ring up a song request in the chat, so I said, \"Arty, SR!\"",
            "Patches was trying to steal my favorite greatsword, but I wasn't having any of it. Zwei hander over now when we've been through so much?",
        };

        static string HelpText { get; } = @"

COMMANDS:

    install {seed}
    
        Runs the INSTALLER for Roguelike Souls, which will randomize the game
        parameters. You should run this ONCE before playing the game, then
        re-run it whenever you want a fresh set of equipment, spells, enemy
        animation speeds, and 'lore'. Your progress in the mod will not be
        lost if you re-install.

        Note that the installer no longer randomizes enemy attack speeds
        by default. Use the separate ""randomize-enemy-attack-speeds"" command
        to randomize (or re-randomize) animation speeds as you prefer.

        The ""seed"" argument is optional, and will run the installer with a
        specific seed string. Seed strings can contain spaces, except at the
        start and end of the string, where they will be ignored.

    manager {seed}
    (or press Enter without typing anything)

        Run the MANAGER program for Roguelike Souls, which should always run in
        the background while you are playing the mod. The game will display an
        error message if connection is lost with this program. If you close it
        accidentally or it closes for any other reason, you should be able to
        run the manager again without needing to quit the game.

        If an error message is printed in this window, copy it or take a screenshot
        for Grimrukh.

        You can also set a seed string for the manager instance. (To do so, you
        must use ""manager {seed}"" explicitly.)

    manager-restart {seed}

        Run the MANAGER program for Roguelike Souls AND automatically abort
        your current run and return to Firelink Shrine the first time the game
        loads. Exit and restart the mod manager program in this mode if you get
        input-locked during a run and are unable to use the Hand of Cessation
        (e.g. the infinite falling loop that currently occurs if you quit out
        of an Abyss battle). Sorry in advance if this happens!

    randomize-enemy-attack-speeds {seed}

        Randomize all enemy attack animation speeds. The randomizer attempts to
        prevent attacks from activating their hitboxes too quickly, and also
        prefers to slow down wind-ups. The idea is to make parry and dodge
        timings less predictable, but it does sometimes get a little intense,
        especially if you get very unlucky with a particular foe.

        You can re-run this randomizer any time you want without affecting
        your game progress or any other part of the most recent installation
        (weapons, spells, and so on).

        The ""seed"" argument is optional, and will run the randomizer with a
        specific seed string. Seed strings can contain spaces, except at the
        start and end of the string, where they will be ignored.

    uninstall

        Uninstall all modded files by restoring the "".rsbak"" files that were
        created at installation time. This won't work if these files were
        already deleted.

    exit

        Quit this console without doing anything.
";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            if (File.Exists("ROGUELIKE_SOULS.cfg"))
            {
                MOD_PATH = File.ReadAllText("ROGUELIKE_SOULS.cfg");
            }

            Console.WriteLine(@"
 ______    _______  _______  __   __  _______  ___      ___   ___   _  _______ 
|    _ |  |       ||       ||  | |  ||       ||   |    |   | |   | | ||       |
|   | ||  |   _   ||    ___||  | |  ||    ___||   |    |   | |   |_| ||    ___|
|   |_||_ |  | |  ||   | __ |  |_|  ||   |___ |   |    |   | |      _||   |___ 
|    __  ||  |_|  ||   ||  ||       ||    ___||   |___ |   | |     |_ |    ___|
|   |  | ||       ||   |_| ||       ||   |___ |       ||   | |    _  ||   |___ 
|___|  |_||_______||_______||_______||_______||_______||___| |___| |_||_______|
                 _______  _______  __   __  ___      _______                   
                |       ||       ||  | |  ||   |    |       |                  
                |  _____||   _   ||  | |  ||   |    |  _____|                  
                | |_____ |  | |  ||  |_|  ||   |    | |_____                   
                |_____  ||  |_|  ||       ||   |___ |_____  |                  
                 _____| ||       ||       ||       | _____| |                  
                |_______||_______||_______||_______||_______|   

                        ~~ The Binding of Lordran ~~~
                                   v1.6.1
                               
                                 by Grimrukh
");
            Thread.Sleep(1000);
            Console.WriteLine(@"  
  BASIC INSTRUCTIONS:

     - Run the ""install"" command to generate a fresh set of parameters.
     - Optionally, run the ""randomize-enemy-attack-speeds"" command to
       make enemy attacks less predictable.
     - Run the ""manager"" command before launching the game, then open
       Dark Souls Remastered alongside it (each time you play). You can also
       start the manager quickly by pressing Enter below without a command.
     - Run the ""manager-restart"" command if you get soft-locked in a run.
     - Re-run ""install"" or ""randomize-enemy-attack-speeds"" whenever you
       want a fresh set of game parameters. This won't affect game progress.

  Use the ""help"" command for more information about each option.

  You will be prompted once to specify your Dark Souls Remastered installation
  directory, which will then be stored in 'ROGUELIKE_SOULS.cfg' next to this
  executable for automatic future use. Delete that file and restart this mod
  program to be prompted again.

  ~ All puns and cat voices are courtesy of Soycrates (@Soycrates). ~
");

#if DEBUG
            Console.WriteLine($@"
    DEBUG MODE ACTIVE:
        - More detailed installation progress.
        - Character stats will start at max.
        - Debug map chosen: {RunManager.DEBUG_MAP}
        - Possibly other side-effects.
");
#endif

            string command;
            string inputSeed = "";
            while (true)
            {
                Console.Write(">>> ");
                string input = Console.ReadLine().Trim();
                if (input != "")
                {
                    if (input.Contains(" "))
                    {
                        command = input.Split(' ')[0];
                        inputSeed = input.Substring(input.IndexOf(' ') + 1).Trim();
                    }
                    else
                    {
                        command = input;  // No seed.
                    }
                }
                else
                {
                    command = "manager";
                    inputSeed = "";
                }

                switch (command)
                {
                    case "help":
                        Console.WriteLine(HelpText);
                        break;
                    case "install":
                        INSTALL(inputSeed);
                        break;
                    case "randomize-enemy-attack-speeds":
                        RANDOMIZE_ENEMY_ATTACK_SPEEDS(inputSeed);
                        break;
                    case "manager":
                        MANAGE_RUN(inputSeed, immediateRestart: false);
                        break;
                    case "manager-restart":
                        MANAGE_RUN(inputSeed, immediateRestart: true);
                        break;
                    case "uninstall":
                        UNINSTALL();
                        break;
                    case "exit":
                        return;
                    default:
                        Console.WriteLine($"Invalid command: {command}.");
                        break;
                }
            }
        }

        static string GetGameDir()
        {
            if (MOD_PATH != null)
            {
                //Console.WriteLine("\nUse previously-specified game directory? (Y/N)");
                //if (ReadKey(ConsoleKey.Y, ConsoleKey.N) == ConsoleKey.Y)
                //    return MOD_PATH;
                return MOD_PATH;
            }

            Console.WriteLine("\nPress ENTER to select your Dark Souls Remastered executable.");
            Console.ReadLine();
            OpenFileDialog ofd = new OpenFileDialog { Filter = "EXE Files|*.exe" };

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                MOD_PATH = Path.GetDirectoryName(ofd.FileName) + "\\";
                File.WriteAllText("ROGUELIKE_SOULS.cfg", MOD_PATH);
                return MOD_PATH;
            }
            else
            {
                return null;
            }
        }

        static ConsoleKey ReadKey(params ConsoleKey[] accepted)
        {
            ConsoleKey key = Console.ReadKey(true).Key;
            while (!accepted.Contains(key))
                key = Console.ReadKey(true).Key;
            return key;
        }

        static void INSTALL(string inputSeed)
        {
            Random random;
            random = inputSeed == "" ? new Random() : new Random(inputSeed.GetHashCode());

            MOD_PATH = GetGameDir();
            if (MOD_PATH == null) {
                Console.WriteLine("No EXE selected. Cancelling installation.");
                return;
            }

            DateTime startTime = DateTime.Now;
            Console.WriteLine("\nBeginning installation... This will take about one minute.");
            Console.WriteLine("\n" + SoyPuns.PopRandomElement(random) + "\n");

            SoulsMod mod = new SoulsMod(
                MOD_PATH, ".rsbak",
                Resources.GameData.GameParam_parambnd,
                Resources.GameData.paramdef_paramdefbnd,
                Resources.GameData.item_msgbnd,
                Resources.GameData.menu_msgbnd);
            mod.LoadPlayerCharacter();
            mod.LoadNonPlayerCharacters();
            InstallInterrootFolder("event", mod);
            InstallInterrootFolder("map", mod);
            InstallInterrootFolder("script", mod);
            InstallInterrootFolder("sfx", mod);
            InstallInterrootFolder("sound", mod);

            TextGenerator textSetup = new TextGenerator(mod);
#if DEBUG
            Console.WriteLine("Running text setup...");
#else
            Console.WriteLine("Studying the ancient texts...");
#endif
            textSetup.Install();
            Thread.CurrentThread.Join(0);

            PlayerGenerator playerSetup = new PlayerGenerator(mod);
#if DEBUG
            Console.WriteLine("Running player setup...");
#else
            Console.WriteLine("Putting the party together...");
#endif
            playerSetup.Install();
            Thread.CurrentThread.Join(0);

            SpEffectGenerator spEffectSetup = new SpEffectGenerator(mod);
#if DEBUG
            Console.WriteLine("Running SpEffect setup...");
#else
            Console.WriteLine("Channeling the powers that be...");
#endif
            spEffectSetup.Install();
            Thread.CurrentThread.Join(0);

            GoodsGenerator goodsSetup = new GoodsGenerator(mod);
#if DEBUG
            Console.WriteLine("Running goods setup...");
#else
            Console.WriteLine("Documenting the artifacts...");
#endif
            goodsSetup.Install();
            Thread.CurrentThread.Join(0);

            SpellGenerator spellSetup = new SpellGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running spell setup...");
#else
            Console.WriteLine("Messing with forces beyond our control...");
#endif
            spellSetup.Install();
            Thread.CurrentThread.Join(0);

            WeaponGenerator weaponSetup = new WeaponGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running weapon setup...");
#else
            Console.WriteLine("Spinning up the whetstone...");
#endif
#if SKIP_BEHAVIORS
            Console.WriteLine("WARNING: Skipping weapon behaviors/attacks!");
            weaponSetup.SkipBehaviors = true;
#endif
            weaponSetup.Install();
            Thread.CurrentThread.Join(0);

            ArmorGenerator armorSetup = new ArmorGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running armor setup...");
#else
            Console.WriteLine("Polishing the armor...");
#endif
            armorSetup.Install();
            Thread.CurrentThread.Join(0);

            EnemyGenerator enemySetup = new EnemyGenerator(mod, random, weaponSetup, armorSetup);
#if DEBUG
            Console.WriteLine("Running enemy setup...");
#else
            Console.WriteLine("Opening the bestiary...");
#endif
            enemySetup.Install();
            Thread.CurrentThread.Join(0);
            
            EnemyAnimationGenerator animSetup = new EnemyAnimationGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Modifying enemy animations...");
#else
            Console.WriteLine("Rousing the rabble...");
#endif
            animSetup.Install();
            Thread.CurrentThread.Join(0);

            MapItemLotsGenerator itemLotsSetup = new MapItemLotsGenerator(mod, weaponSetup, armorSetup, random);
#if DEBUG
            Console.WriteLine("Running item lot setup...");
#else
            Console.WriteLine("Burying the treasures...");
#endif
            itemLotsSetup.Install();
            Thread.CurrentThread.Join(0);

            // Must be run AFTER weapon/armor setup.
            CharacterGenerator chrSetup = new CharacterGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running character setup...");
#else
            Console.WriteLine("Assembling the party...");
#endif
            chrSetup.Install();
            Thread.CurrentThread.Join(0);

#if DEBUG
            Console.WriteLine("Installing mod...");
#else
            Console.WriteLine("Heading forth...");
#endif
            mod.Install();
            Thread.CurrentThread.Join(0);

            Console.WriteLine("\nInstallation successful! Press ENTER to return to the prompt.");
#if DEBUG
            Console.WriteLine($"Installation time: {(DateTime.Now - startTime).TotalSeconds} seconds");
#endif
            Console.ReadLine();
        }

        static void RANDOMIZE_ENEMY_ATTACK_SPEEDS(string inputSeed)
        {
            MOD_PATH = GetGameDir();
            if (MOD_PATH == null)
            {
                Console.WriteLine("No EXE selected. Cancelling attack speed randomization.");
                return;
            }

            Random random;
            random = inputSeed == "" ? new Random() : new Random(inputSeed.GetHashCode());
            SoulsMod mod = new SoulsMod(MOD_PATH, ".rsbak");
            mod.LoadNonPlayerCharacters();
            EnemyAnimationGenerator animSetup = new EnemyAnimationGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running animation setup...");
#else
            Console.WriteLine("Stepping into time vortex...");
#endif
            animSetup.AddSpeedEffects(noParamEdit: true);  // just registers effect IDs in setup
            animSetup.AddAttackDamageEffects(noParamEdit: true);  // just registers effect IDs in setup
            animSetup.RandomizeAllEnemySpeeds();
            mod.InstallAnimations(skipPlayer: true);
            Thread.CurrentThread.Join(0);

            Console.WriteLine("\nEnemy attack speeds randomized successfully! Press ENTER to return to the prompt.");
            Console.ReadLine();
        }

        static void InstallInterrootFolder(string dir, SoulsMod game)
        {
            foreach (string newFile in Directory.GetFiles($@"Package\{dir}"))
            {
                string originalFile = $@"{game.GameDir}{dir}\{Path.GetFileName(newFile)}";
                if (File.Exists(originalFile))
                    game.Backup(originalFile);
                File.Copy(newFile, originalFile, true);
            }
            foreach (string subfolder in Directory.GetDirectories($@"Package\{dir}"))
            {
                string subfolderName = subfolder.Split('\\').Last();
                InstallInterrootFolder($@"{dir}\{subfolderName}", game);
            }
        }

        static void MANAGE_RUN(string inputSeed, bool immediateRestart = false)
        {
            MOD_PATH = GetGameDir();
            if (MOD_PATH == null)
            {
                Console.WriteLine("No EXE selected. Aborting run manager.");
                return;
            }

            SoulsMod mod = new SoulsMod(MOD_PATH, ".rsbak");
            DSRHook hook = new DSRHook(5000, 5000);
            hook.Start();

            Console.WriteLine("Waiting for game application to start...");
            while (!hook.Hooked)
                Thread.Sleep(100);

            Console.WriteLine("Waiting for game to be loaded...");
            while (!hook.Loaded)
                Thread.Sleep(100);

            Console.WriteLine("Hooked.");
            Console.WriteLine("Roguelike Souls manager starting...");
            RunManager runManager = new RunManager(mod, hook, inputSeed);
            runManager.RunMainLoop(immediateRestart);
        }

        static void UNINSTALL()
        {
            MOD_PATH = GetGameDir();
            if (MOD_PATH == null)
            {
                Console.WriteLine("No EXE selected. Cancelling uninstallation.");
                return;
            }

            Console.Write("Restoring backup files...");
            int restoreCount = RestoreDir(MOD_PATH, ".rsbak");
            Console.WriteLine($"{restoreCount} files restored.");
        }

        static int RestoreDir(string dir, string backupExtension)
        {
            string[] directories = Directory.GetDirectories(dir, "*", SearchOption.AllDirectories);
            int restoreCount = 0;
            foreach (string directory in directories)
            {
                if (directory.Contains("_utilities")) continue;

                IEnumerable<string> files = Directory.GetFiles(directory).Where(f => !f.EndsWith(backupExtension));
                foreach (string file in files)
                    if (File.Exists(file + backupExtension))
                    {
                        File.Copy(file + backupExtension, file, true);
                        restoreCount += 1;
                    }

                IEnumerable<string> dirs = Directory.GetDirectories(directory, "*", SearchOption.AllDirectories);
                foreach (string dct in dirs)
                    restoreCount += RestoreDir(dct, backupExtension);
            }
            return restoreCount;
        }
    }
}
