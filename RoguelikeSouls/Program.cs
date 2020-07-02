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

namespace RoguelikeSouls
{
    class Program
    {
        //const string MOD_PATH = @"G:\Steam\steamapps\common\DARK SOULS REMASTERED\";
        const string MOD_PATH = @"..\";

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

        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            Console.WriteLine(
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" +
                "\n~~~    ROGUE-LIKE SOULS    ~~~" +
                "\n~~~                        ~~~" +
                "\n~~~ The Binding of Lordran ~~~" +
                "\n~~~                        ~~~" +
                "\n~~~          v1.0          ~~~" +
                "\n~~~                        ~~~" +
                "\n~~~       by Grimrukh      ~~~" +
                "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

            Console.WriteLine(
                "\n--- BASIC USAGE INSTRUCTIONS ---" +
                "\n  1. Make sure everything was unzipped into a subfolder inside your " +
                "\n     \"DARK SOULS REMASTERED\" folder. (This executable looks for the game " +
                "\n     executable in the folder above itself. More flexible one later.)" +
                "\n  2. If a patch zip is available with a higher version number, make sure " +
                "\n     to copy its contents into the original mod folder and override " +
                "\n     everything when asked. You only need the latest patch zip." +
                "\n  3. Copy-paste the contents of \"Package\" into your game directory. " +
                "\n     Back your existing files up first for easy uninstallation later." +
                "\n  4. Run the \"install\" command to generate a fresh set of parameters." +
                "\n  5. Run the \"manager\" command before launching the game, then open " +
                "\n     Dark Souls Remastered alongside it (each time you play). You can also " +
                "\n     start the manager quickly by pressing Enter below without a command." +
                "\n  6. Use the \"manager-restart\" command if you get soft-locked in a run." +
                "\n" +
                "\nCOMMANDS:" +
                "\n" +
                "\ninstall {seed} " +
                "\n" +
                "\n    Runs the INSTALLER for Roguelike Souls, which will randomize the game " +
                "\n    parameters. You should run this ONCE before playing the game, then " +
                "\n    re-run it whenever you want a fresh set of equipment, spells, enemy " +
                "\n    animation speeds, and 'lore'." +
                "\n" +
                "\n    Don't forget to copy and paste the contents of the \"Package\" folder " +
                "\n    into your game directory before playing as well! These files are not " +
                "\n    automatically backed up by any installer and you should back them up " +
                "\n    yourself if you want to easily uninstall the mod later. (I may make " +
                "\n    this easier in a future update.)" +
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
                "\n    Run the MANAGER program for Roguelike Souls AND automatically abort " +
                "\n    your current run and return to Firelink Shrine the first time the game " +
                "\n    loads. Exit and restart the mod manager program in this mode if you get " +
                "\n    input-locked during a run and are unable to use the Hand of Cessation " +
                "\n    (e.g. the infinite falling loop that currently occurs if you quit out " +
                "\n    of an Abyss battle)." +
                "\n" +
                "\nuninstall" +
                "\n    Uninstall most modded files by restoring the \".smbak\" files that were " +
                "\n    created at installation time. This won't work if these files were " +
                "\n    already deleted! Files replaced by the contents of \"Package\" also won't " +
                "\n    be restored by this command, sorry!" +
                "\n" +
                "\nexit" +
                "\n    Quit this console without doing anything." +
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

                if (command == "install")
                    INSTALL(inputSeed);
                else if (command == "install-noanim")
                    INSTALL(inputSeed, skipAnimRandomizer: true);
                else if (command == "manager")
                    MANAGE_RUN(inputSeed, immediateRestart: false);
                else if (command == "manager-restart")
                    MANAGE_RUN(inputSeed, immediateRestart: true);
                else if (command == "uninstall")
                    UNINSTALL();
                else if (command == "exit")
                    return;
                else
                {
                    Console.WriteLine($"Invalid command: {command}.");
                }
            }
        }

        static void INSTALL(string inputSeed, bool skipAnimRandomizer = false)
        {
            DateTime startTime = DateTime.Now;

            Random random;
            if (inputSeed == "")
                random = new Random();
            else
                random = new Random(inputSeed.GetHashCode());

            Console.WriteLine("\nBeginning installation... This will take about one minute.");
            Console.WriteLine("\n" + SoyPuns.PopRandomElement(random) + "\n");

            SoulsMod mod = new SoulsMod(MOD_PATH, ".smbak", 
                Resources.GameData.GameParam_parambnd, Resources.GameData.paramdef_paramdefbnd,
                Resources.GameData.item_msgbnd, Resources.GameData.menu_msgbnd);
            mod.LoadPlayerCharacter();
            mod.LoadNonPlayerCharacters();            

            PlayerGenerator playerSetup = new PlayerGenerator(mod);
#if DEBUG
            Console.WriteLine("Running player setup...");
#endif
            playerSetup.Install();

            TextGenerator textSetup = new TextGenerator(mod);
#if DEBUG
            Console.WriteLine("Running text setup...");
#endif
            textSetup.Install();

            SpEffectGenerator spEffectSetup = new SpEffectGenerator(mod);
#if DEBUG
            Console.WriteLine("Running SpEffect setup...");
#endif
            spEffectSetup.Install();

            GoodsGenerator goodsSetup = new GoodsGenerator(mod);
#if DEBUG
            Console.WriteLine("Running goods setup...");
#endif
            goodsSetup.Install();

            SpellGenerator spellSetup = new SpellGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running spell setup...");
#endif
            spellSetup.Install();

            WeaponGenerator weaponSetup = new WeaponGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running weapon setup...");
#endif
            weaponSetup.Install();

            ArmorGenerator armorSetup = new ArmorGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running armor setup...");
#endif
            armorSetup.Install();

            EnemyGenerator enemySetup = new EnemyGenerator(mod, random, weaponSetup, armorSetup);
#if DEBUG
            Console.WriteLine("Running enemy setup...");
#endif
            enemySetup.Install();

            MapItemLotsGenerator itemLotsSetup = new MapItemLotsGenerator(mod, weaponSetup, armorSetup, random);
#if DEBUG
            Console.WriteLine("Running item lot setup...");
#endif
            itemLotsSetup.Install();

            EnemyAnimationGenerator animSetup = new EnemyAnimationGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running animation setup...");
#endif
            animSetup.Install(skipAnimRandomizer);

            // Must be run AFTER weapon/armor setup.
            CharacterGenerator chrSetup = new CharacterGenerator(mod, random);
#if DEBUG
            Console.WriteLine("Running chr setup...");
#endif
            chrSetup.Install();

            Console.WriteLine(SoyPuns.PopRandomElement(random) + "\n");

#if DEBUG
            Console.WriteLine("Installing mod...");
#endif
            mod.Install();

#if DEBUG
            Console.WriteLine($"Installation time: {(DateTime.Now - startTime).TotalSeconds}");
#endif
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
