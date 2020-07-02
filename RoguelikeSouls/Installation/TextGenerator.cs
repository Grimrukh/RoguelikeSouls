using SoulsFormatsMod;
using System.Collections.Generic;

namespace RoguelikeSouls.Installation
{
    class TextGenerator
    {
        SoulsMod Mod { get; }

        public static Dictionary<int, string> EventTexts = new Dictionary<int, string>()
        {
            { 79999, "Mod connection error. Please restart mod program." },
            { 80000, "Depart area" },
            { 80001, "Exit is locked" },
            { 80002, "Exit is unavailable" },
            // { 80003, "Sigil required" },
            { 80004, "Return to Firelink Shrine" },
            { 80005, "Begin journey to Lordran" },
            { 80006, "Lord Soul captured. More treasure unlocked." },
            { 80007, "Lord Soul captured. Abyssal treasure unlocked." },
            { 80008, "Abandon journey and return to Firelink Shrine?" },
            { 80009, "The five fingers uncurl..." },
            
            { 80010, "Bell has not sounded" },
            { 80011, "Moonlight magic blocks the path" },
            { 80012, "Cannot capture Lord Soul without Lordvessel" },
            { 80013, "Step into abyssal portal" },
            { 80014, "The fortress gate has opened" },
            { 80015, "Demonic magic blocks the path" },

            // TODO: Different "receive gift" prompt for each ally.

            { 80020, "Receive gift from ally" },
            { 80021, "Two gifts have already been accepted" },
            { 80022, "Prove yourself worthy next time" },
            { 80023, "Lord Souls can now be captured. More treasure unlocked." },
            { 80024, "Departing..." },

            { 80030, "Bonfire created" },
            { 80031, "Bonfire could not be created" },
            { 80032, "Bonfire cannot be created again" },
            { 80033, "Kindle bonfire here?" },
            { 80034, "Increase game difficulty?" },

            { 80041, "Solaire has been rescued" },
            { 80042, "Siegmeyer has been rescued" },
            { 80043, "Logan has been rescued" },
            { 80044, "Quelana has been rescued" },
            { 80045, "Havel has been rescued" },
            { 80046, "King Mornstein has been rescued" },
            { 80047, "Lobos Jr has been rescued" },

            { 80050, "Level 1" },
            { 80051, "Level 2" },
            { 80052, "Level 3" },
            { 80053, "Level 4" },
            { 80054, "Level 5" },
            { 80055, "Level 6" },
            { 80056, "Level 7" },
            { 80057, "Level 8" },
            { 80058, "Level 9" },
            { 80059, "Level 10" },

            { 80060, "Bonus Level" },

            { 90001, "<?gdsparam@2001?> required" },
            { 90002, "<?gdsparam@2002?> required" },
            { 90003, "<?gdsparam@2003?> required" },
            { 90005, "<?gdsparam@2005?> required" },
            { 90006, "<?gdsparam@2006?> required" },
            { 90007, "<?gdsparam@2007?> required" },
            { 90100, "<?gdsparam@2100?> required" },
            
            { 15000185, "Trade souls for motes" },

            { 15000500, "Obtain Warrior's equipment" },
            { 15000501, "Obtain Knight's equipment" },
            { 15000502, "Obtain Wanderer's equipment" },
            { 15000503, "Obtain Thief's equipment" },
            { 15000504, "Obtain Barbarian's equipment" },
            { 15000505, "Obtain Hunter's equipment" },
            { 15000506, "Obtain Witch's equipment" },
            { 15000507, "Obtain Cleric's equipment" },
            
            { 15000510, "Crush four fingers for blessing" },

            { 15000550, "Equipment already chosen" },
            { 15000551, "Fate already sealed" },
        };

        public TextGenerator(SoulsMod mod)
        {
            Mod = mod;
        }

        public void Install()
        {
            AddEventText();
            ChangeConversations();
            Mod.Text.NPCNames[1000] = "Da Boss";  // humorous backup in case EMEVD injection fails for whatever reason
            Mod.Text.NPCNames[1001] = "Boss of Chaos";  // too hard to inject custom names into Bed of Chaos fight
        }

        public void AddEventText()
        {
            foreach (var kv in EventTexts)
            {
                Mod.Text.EventText[kv.Key] = kv.Value;
            }
        }

        public void ChangeConversations()
        {
            Mod.Text.Conversations[23010040] = "Ahh, I cometh too late. Thou has touched the cursed hand.";
            Mod.Text.Conversations[23010041] = "Thine task will be treacherous, but hope is lost not.";
            Mod.Text.Conversations[23010042] = "The fate of thine friends need not be sealed.";
            Mod.Text.Conversations[23010043] = "I beseech thee: take the crow and find thine kin.";

            Mod.Text.Conversations[23010120] = "Thou are resilient and loyal, beyond any doubt.";
            Mod.Text.Conversations[23010121] = "But wilt thou press on, and ascend to the cradle of fire?";
            Mod.Text.Conversations[23010122] = "I hear it's pretty lit.";
            Mod.Text.Conversations[23010123] = "Do not flame me for that bad joke.";

            Mod.Text.Conversations[23010020] = "The wretched hand is pernicious.";
            Mod.Text.Conversations[23010021] = "But if thou weareth my ring, thou shall find it somewhat less so.";
            Mod.Text.Conversations[23010022] = "Well? Onward, hero.";
            Mod.Text.Conversations[23010023] = "There is no need for paws.";
            Mod.Text.Conversations[23010024] = "You are purrfectly capable of journeying forth, are you not?";
        }
    }
}
