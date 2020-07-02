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

        static string helpText = "\n|----------------------------|\n|----------COMMANDS----------|\n|----------------------------|\n" +
                "\n" +
                "\ninstall {seed} " +
                "\n" +
                "\n    Runs the INSTALLER for Roguelike Souls, which will randomize the game " +
                "\n    parameters. You should run this ONCE before playing the game, then " +
                "\n    re-run it whenever you want a fresh set of equipment, spells, enemy " +
                "\n    animation speeds, and 'lore'." +
                "\n" +
                "\n    The \"seed\" argument is option, and will run the INSTALLER with a " +
                "\n    specific seed string. Seed strings can contain spaces, except at the " +
                "\n    start/end of the string where they will be ignored." +
                "\n" +
                "\ninstall-noanim {seed} " +
                "\n" +
                "\n    Run the INSTALLER but don't touch enemy animation speeds." +
                "\n" +
                "\nmanager {seed}" +
                "\n(or press Enter without typing anything)" +
                "\n" +
                "\n    Run the MANAGER program for Roguelike Souls, which should always run in " +
                "\n    the background while you are playing the mod. The game will display an " +
                "\n    error message if connection is lost with this program." +
                "\n" +
                "\n    If an error message is printed in this window, take a screenshot for " +
                "\n    Grimrukh. You can also set a seed string for the manager instance, but " +
                "\n    then you must use \"/manager {seed}\" explicitly." +
                "\n" +
                "\nmanager-restart {seed}" +
                "\n" +
                "\n    Run the MANAGER program for Roguelike Souls AND automatically abort " +
                "\n    your current run and return to Firelink Shrine the first time the game " +
                "\n    loads. Exit and restart the mod manager program in this mode if you get " +
                "\n    input-locked during a run and are unable to use the Hand of Cessation " +
                "\n    (e.g. the infinite falling loop that currently occurs if you quit out " +
                "\n    of an Abyss battle)." +
                "\n" +
                "\nuninstall" +
                "\n" +
                "\n    Uninstall all modded files by restoring the \".smbak\" files that were " +
                "\n    created at installation time. This won't work if these files were " +
                "\n    already deleted" +
                "\n" +
                "\nexit" +
                "\n" +
                "\n    Quit this console without doing anything." +
                "\n";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            if (File.Exists("ROGUE-LIKE_SOULS.cfg"))
            {
                MOD_PATH = File.ReadAllText("ROGUE-LIKE_SOULS.cfg");
            }

            Console.WriteLine(
                "\n                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
                "\n                   ~~~    ROGUE-LIKE SOULS    ~~~" +
                "\n                   ~~~                        ~~~" +
                "\n                   ~~~ The Binding of Lordran ~~~" +
                "\n                   ~~~                        ~~~" +
                "\n                   ~~~          v1.0          ~~~" +
                "\n                   ~~~                        ~~~" +
                "\n                   ~~~       by Grimrukh      ~~~" +
                "\n                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

            Console.WriteLine(
                "\n--- BASIC USAGE INSTRUCTIONS ---" +
                "\n  " +
                "\n  IMPORTANT: If a patch zip is available with a higher version number, make " +
                "\n  sure to copy its contents into the original mod folder (overwriting any" +
                "\n  existing files) before continuing." +
                "\n  " +
                "\n  1. Run the \"install\" command to generate a fresh set of parameters." +
                "\n  2. Run the \"manager\" command before launching the game, then open " +
                "\n     Dark Souls Remastered alongside it (each time you play). You can also " +
                "\n     start the manager quickly by pressing Enter below without a command." +
                "\n  3. Use the \"manager-restart\" command if you get soft-locked in a run." +
                "\n  " +
                "\n  Run the \"help\" command for more information about the various commands." +
                "\n");


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
                        Console.WriteLine(helpText);
                        break;
                    case "install":
                        INSTALL(inputSeed);
                        break;
                    case "install-no-anim":
                        INSTALL(inputSeed, skipAnimRandomizer: true);
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

        static string AskForDir()
        {
            Console.WriteLine("\nPress ENTER to select your Dark Souls Remastered executable.");
            Console.ReadLine();
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "EXE Files|*.exe";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                string name = Path.GetDirectoryName(ofd.FileName) + "\\";
                File.WriteAllText("ROGUE-LIKE_SOULS.cfg", name);
                return name;
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

        static void INSTALL(string inputSeed, bool skipAnimRandomizer = false)
        {
            Random random;
            if (inputSeed == "")
                random = new Random();
            else
                random = new Random(inputSeed.GetHashCode());

            if (MOD_PATH == null)
            {
                MOD_PATH = AskForDir();
            }
            else
            {
                Console.WriteLine("\nUse previously-specified game directory? (Y/N)");
                bool yes = ReadKey(ConsoleKey.Y, ConsoleKey.N) == ConsoleKey.Y;
                if (!yes)
                    MOD_PATH = AskForDir();
            }

            if (MOD_PATH == null) {
                Console.WriteLine("No EXE selected. Cancelling installation.");
                return;
            }

            DateTime startTime = DateTime.Now;
            Console.WriteLine("\nBeginning installation... This will take about one minute.");
            Console.WriteLine("\n" + SoyPuns.PopRandomElement(random) + "\n");

            SoulsMod mod = new SoulsMod(
                MOD_PATH, ".smbak",
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


            PlayerGenerator playerSetup = new PlayerGenerator(mod);
#if DEBUG
            Console.WriteLine("Running player setup...");
#endif
            playerSetup.Install();
            Thread.CurrentThread.Join(0);

            TextGenerator textSetup = new TextGenerator(mod);
#if DEBUG
            Console.WriteLine("Running text setup...");
#endif
            textSetup.Install();
            Thread.CurrentThread.Join(0);

            SpEffectGenerator spEffectSetup = new SpEffectGenerator(mod);
#if DEBUG
            Console.WriteLine("Running SpEffect setup...");
#endif
            spEffectSetup.Install();
            Thread.CurrentThread.Join(0);

            GoodsGenerator goodsSetup = new GoodsGenerator(mod);
#if DEBUG
            Console.WriteLine("Running goods setup...");
#endif
            goodsSetup.Install();
            Thread.CurrentThread.Join(0);

            SpellGenerator spellSetup = new SpellGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running spell setup...");
#endif
            spellSetup.Install();
            Thread.CurrentThread.Join(0);

            WeaponGenerator weaponSetup = new WeaponGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running weapon setup...");
#endif
            weaponSetup.Install();
            Thread.CurrentThread.Join(0);

            ArmorGenerator armorSetup = new ArmorGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running armor setup...");
#endif
            armorSetup.Install();
            Thread.CurrentThread.Join(0);

            EnemyGenerator enemySetup = new EnemyGenerator(mod, random, weaponSetup, armorSetup);
#if DEBUG
            Console.WriteLine("Running enemy setup...");
#endif
            enemySetup.Install();
            Thread.CurrentThread.Join(0);

            MapItemLotsGenerator itemLotsSetup = new MapItemLotsGenerator(mod, weaponSetup, armorSetup, random);
#if DEBUG
            Console.WriteLine("Running item lot setup...");
#endif
            itemLotsSetup.Install();
            Thread.CurrentThread.Join(0);

            EnemyAnimationGenerator animSetup = new EnemyAnimationGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running animation setup...");
#endif
            animSetup.Install(skipAnimRandomizer);
            Thread.CurrentThread.Join(0);

            // Must be run AFTER weapon/armor setup.
            CharacterGenerator chrSetup = new CharacterGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running chr setup...");
#endif
            chrSetup.Install();
            Thread.CurrentThread.Join(0);

            Console.WriteLine(SoyPuns.PopRandomElement(random) + "\n");

#if DEBUG
            Console.WriteLine("Installing mod...");
#endif
            mod.Install();
            Thread.CurrentThread.Join(0);

#if DEBUG
            Console.WriteLine($"Installation time: {(DateTime.Now - startTime).TotalSeconds}");
#endif
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
            SoulsMod mod = new SoulsMod(MOD_PATH, ".smbak");
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
            if (!File.Exists("ROGUE-LIKE_SOULS.cfg"))
            {
                MOD_PATH = AskForDir();
            }
            else
            {
                Console.WriteLine("\nUninstall previously-specified game directory? (Y/N)");
                bool yes = ReadKey(ConsoleKey.Y, ConsoleKey.N) == ConsoleKey.Y;
                if (yes)
                    MOD_PATH = File.ReadAllText("ROGUE-LIKE_SOULS.cfg");
                else
                    MOD_PATH = AskForDir();
            }

            if (MOD_PATH == null)
            {
                Console.WriteLine("No EXE selected. Cancelling uninstallation.");
                return;
            }

            Console.Write("Restoring backup files...");
            int restoreCount = RestoreDir(MOD_PATH, ".smbak");
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
