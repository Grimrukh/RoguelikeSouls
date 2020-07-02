using System;
using System.Collections.Generic;
using System.Linq;
using SoulsFormats;
using SoulsFormatsMod;
using SoulsFormatsMod.PARAMS;
using static SoulsFormatsMod.Extensions.AnimExtensions;

namespace RoguelikeSouls.Installation
{
    class EnemyAnimationGenerator
    {
        const float FrameDuration = 1.0f / 30.0f;
        const float QuantizedSpeed = 0.1f;
        const float MaxSpeedChangePerFrame = 0.1f;
        const float MaxSpeedMultiplier = 3.0f;
        const bool UseWeightedRory = true;
        const bool UseRemovalRory = false;
        const float MinAttackBehaviorHitboxScalar = 1.0f;
        const float MinMaxAttackBehaviorDelay = 0.5f;
        const float MaxMaxAttackBehaviorDelay = 0.8f;  // took down from 1.0 to prevent SUPER slow speeds a bit more
        const float MinAttackScale = 0.8f;
        const float MaxAttackScale = 1.2f;
        int MaxDifference { get; }
        int MaxSpeedPoints { get; }

        Dictionary<float, int> SpeedEffects { get; } = new Dictionary<float, int>();
        Dictionary<float, int> AttackDamageEffects { get; } = new Dictionary<float, int>();

        SoulsMod Mod { get; }
        Random Rand { get; }
        
        bool DEBUG { get; } = false;

        public EnemyAnimationGenerator(SoulsMod mod, Random random)
        {
            if (MaxSpeedChangePerFrame < QuantizedSpeed)
            {
                throw new ArithmeticException("maxSpeedChangePerFrame cannot be less than quantizedSpeed.");
            }
            Mod = mod;
            Rand = random;
            MaxDifference = (int)(MaxSpeedChangePerFrame / QuantizedSpeed);
            MaxSpeedPoints = (int)(MaxSpeedMultiplier / QuantizedSpeed);
        }

        public void Install(bool skipAnimRandomizer = false)
        {
            AddSpeedEffects();
            AddAttackDamageEffects();
            if (!skipAnimRandomizer)
                RandomizeAllEnemySpeeds();
            AddFadingAnimations();
            ResetSpeedInDeathAnimations();
        }

        void ResetSpeedInDeathAnimations()
        {
            foreach (int chrID in Mod.Characters.Keys)
            {
                if (chrID != 0)
                {
                    TAE enemyTAE = Mod[chrID].GetTAE(chrID);
                    foreach (TAE.Animation deathAnim in enemyTAE.Animations.Where(anim => 2200 >= anim.ID && anim.ID < 2210))
                        deathAnim.ApplyEffect(SpeedEffects[1.0f], 0.0f, 1.0f);
                }
            }
        }

        void RandomizeAllEnemySpeeds()
        {
            foreach (int chrID in Mod.Characters.Keys)
            {
                if (chrID != 0)
                    RandomizeEnemySpeed(chrID);
            }
        }

        void AddFadingAnimations()
        {
            foreach (int chrID in Mod.Characters.Keys)
            {
                if (chrID == 0)
                    continue;

                TAE enemyTAE = Mod[chrID].GetTAE(chrID);
                TAE.Animation standing = enemyTAE.Animations[0];

                TAE.Animation fadeIn = new TAE.Animation(10, standing.MiniHeader, standing.AnimFileName);
                fadeIn.CloneReference(standing, 0, true);
                TAE.Event fadeInEvent = new TAE.Event(0.0f, 2.0f, 193, 0, false, DS1[0][193]);
                fadeInEvent.Parameters["GhostVal1"] = 0.0f;
                fadeInEvent.Parameters["GhostVal2"] = 1.0f;
                fadeIn.Events.Add(fadeInEvent);
                enemyTAE.Animations.Add(fadeIn);

                TAE.Animation fadeOut = new TAE.Animation(11, standing.MiniHeader, standing.AnimFileName);
                fadeOut.CloneReference(standing, 0, true);
                TAE.Event fadeOutEvent = new TAE.Event(0.0f, 2.0f, 193, 0, false, DS1[0][193]);
                fadeOutEvent.Parameters["GhostVal1"] = 1.0f;
                fadeOutEvent.Parameters["GhostVal2"] = 0.0f;
                TAE.Event invisibleEvent = new TAE.Event(2.0f, 10.0f, 193, 0, false, DS1[0][193]);
                invisibleEvent.Parameters["GhostVal1"] = 0.0f;
                invisibleEvent.Parameters["GhostVal2"] = 0.0f;
                fadeOut.Events.Add(fadeOutEvent);
                fadeOut.Events.Add(invisibleEvent);
                enemyTAE.Animations.Add(fadeOut);
            }
        }

        void AddSpeedEffects()
        {
            // Adds speed modifier SpEffects (9000 range) to GPARAM and registers in dictionary for easy lookup here.
            int speedEffectCount = (int)(MaxSpeedMultiplier / QuantizedSpeed);
            for (int i = 1; i <= speedEffectCount; i++)
            {
                float speed = (float)Math.Round(i * QuantizedSpeed, 2);
                SpEffect effect = Mod.GPARAM.SpEffects.CopyRow(81001, 9000 + i);
                effect.Name = $"SpeedMultiplier ({speed:0.00}x)";
                effect.EffectDuration = 0;
                effect.SpecialState = 0;
                effect.SpecialEffectCategory = 0;
                effect.AnimationSpeedMultiplier = speed;
                effect.CanAffectAll = true;
                SpeedEffects[speed] = Convert.ToInt32(effect);
            }
        }
        void AddAttackDamageEffects()
        {
            // Adds blanket attack damage modifier SpEffects (9100 range) to GPARAM and registers in dictionary for easy lookup here.
            int attackEffectCount = (int)(2.0f / 0.05f);
            for (int i = 1; i <= attackEffectCount; i++)
            {
                float attackMultiplier = (float)Math.Round(i * 0.05, 2);
                SpEffect effect = Mod.GPARAM.SpEffects.CopyRow(81001, 9100 + i);
                effect.Name = $"AttackDamageMultiplier ({attackMultiplier:0.00}x)";
                effect.EffectDuration = 0;
                effect.OutgoingPhysicalDamageMultiplier = attackMultiplier;
                effect.OutgoingMagicDamageMultiplier = attackMultiplier;
                effect.OutgoingFireDamageMultiplier = attackMultiplier;
                effect.OutgoingLightningDamageMultiplier = attackMultiplier;
                effect.OutgoingStaminaDamageMultiplier = attackMultiplier;
                effect.CanAffectAll = true;
                AttackDamageEffects[attackMultiplier] = Convert.ToInt32(effect);
            }
        }
        void RandomizeEnemySpeed(int enemyID)
        {
            // Randomizes speeds of relevant animations in enemy TAE. Also adjusts attack damage based on new speed (excludes Bullets).
            if (enemyID == 0) throw new ArgumentException("`RandomizeEnemySpeed` is not for the player.");
            TAE tae = Mod[enemyID].GetTAE(enemyID);
            foreach (var animation in tae.Animations)
            {
                var info = new NPCAnimationInfo(animation, enemyID, Mod);
                if (info.HasInvokeBehaviorEvent && 3000 <= animation.ID && animation.ID <= 3999)
                {
                    RandomizeBehaviorAnimationSpeed(animation, info);
                }
            }
        }
        void RandomizeBehaviorAnimationSpeed(TAE.Animation behaviorAnim, NPCAnimationInfo info, bool isPlayer = false)
        {
            /* Apply random speed modifiers throughout given attack animation (includes behaviors that trigger Bullets and SpEffects).
             *  - The earliest possible time for the hitbox behavior to start is Min(oldStartTime, Max(0.5, 0.5 * oldStartTime, hitboxRadius)).
             *  - The latest possible time for the hitbox is 0.5 * (oldStart - minStart), clamped between [minMax] and [maxMax].
             *  - RoryAlgorithm is more likely to add speed to valid frames that already have more speed, which leads to less noisy functions.
             *  - Hitbox radius of bullets is estimated, but does not take projectile speed into account. Fast, small bullets may see large speed boosts.
             *  - Non-Bullet attack damage is scaled by [minAttackScale] (if earliest possible time) to [maxAttackScale] (if latest possible time), rounded to the nearest 0.1.
             *  - Bullets themselves are unchanged here and randomized separately.
             */
            float hitboxRadius = 1.0f;  // default
            float behaviorStartTime = -1.0f;
            float behaviorEndTime = -1.0f;
            if (info.InvokeAttackEvent != null)
            {
                Behavior attackBehavior = info.GetAttackBehavior();
                if (attackBehavior == null) return;  // Missing Behavior param, which means it is most likely unused. No randomization.
                Attack attack = info.GetAttack();
                if (attack == null) return;  // Missing Attack param, which means it is most likely unused. No randomization.
                hitboxRadius = attack.Hitbox0Radius;
                behaviorStartTime = info.InvokeAttackEvent.StartTime;
                behaviorEndTime = info.InvokeAttackEvent.EndTime;
            }
            else if (info.InvokeBulletEvent != null)
            {
                Behavior bulletBehavior = info.GetBulletBehavior();
                if (bulletBehavior == null) return;  // Missing Behavior param, which means it is most likely unused. No randomization.
                if (bulletBehavior.ReferenceType == 1)
                {
                    Bullet bullet = info.GetBullet();
                    if (bullet == null) return;  // Missing Bullet param.
                    hitboxRadius = Tools.GuessBulletRadius(bullet, Mod);
                    // Console.WriteLine($"    Final bullet ({bullet.ID}) radius of animation {behaviorAnim.ID}: {hitboxRadius:0.00}");
                    if (hitboxRadius == -1.0f) hitboxRadius = 1.0f;  // default for bullets with no final radius
                }
                else if (bulletBehavior.ReferenceType == 2)
                {
                    SpEffect spEffect = info.GetSpEffect();
                    if (spEffect == null) return;  // Missing SpEffect param.
                    hitboxRadius = 1.0f;  // leave as default for SpEffect
                }
                behaviorStartTime = info.InvokeBulletEvent.StartTime;
                behaviorEndTime = info.InvokeBulletEvent.EndTime;
            }
            if (behaviorStartTime == -1.0f || behaviorEndTime == -1.0f) throw new ArgumentException($"Behavior start/end times were not set.");
            
            float minBehaviorStartTime = Math.Min(behaviorStartTime, Math.Max(0.5f, Math.Max(0.5f * behaviorStartTime, MinAttackBehaviorHitboxScalar * hitboxRadius)));
            float maxBehaviorStartTime = behaviorStartTime + Math.Max(MinMaxAttackBehaviorDelay, Math.Min(0.5f * (behaviorStartTime - minBehaviorStartTime), MaxMaxAttackBehaviorDelay));
            float newBehaviorStartTime = minBehaviorStartTime + (float)Rand.NextDouble() * (maxBehaviorStartTime - minBehaviorStartTime);
            List<int> preAttackSpeedFunction = GetRandomSpeedFunction(0.0f, behaviorStartTime, newBehaviorStartTime);
            ApplySpeedFunction(behaviorAnim, preAttackSpeedFunction);
            if (DEBUG)
            {
                Console.WriteLine($"\nANIMATION {behaviorAnim.ID}");
                Console.WriteLine($"    Attack start time: {behaviorStartTime} => {newBehaviorStartTime}");
                Console.WriteLine($"    Random min/max: {minBehaviorStartTime}, {maxBehaviorStartTime}");
                Tools.DrawSpeedFunction(preAttackSpeedFunction, MaxSpeedMultiplier, QuantizedSpeed);
            }
            if (info.InvokeAttackEvent != null)
            {
                float attackPowerFactor = (newBehaviorStartTime - minBehaviorStartTime) / (maxBehaviorStartTime - minBehaviorStartTime);
                float attackDamageMultiplier = MinAttackScale + attackPowerFactor * (MaxAttackScale - MinAttackScale);
                ApplySpeedAttackDamageMultiplier(behaviorAnim, attackDamageMultiplier, behaviorStartTime - FrameDuration, behaviorEndTime + FrameDuration);
            }
            // Mild random speed change during InvokeBehaviorEvent itself (multiplier of 1.0, 1.1, or 1.2).
            int duringSpeedOptionCount = (int)(0.2f / QuantizedSpeed) + 1;
            float duringAttackSpeed = 1.0f + (Rand.Next(duringSpeedOptionCount) * QuantizedSpeed);
            int duringSpEffectID = SpeedEffects[(float)Math.Round(duringAttackSpeed, 2)];
            behaviorAnim.ApplyEffect(duringSpEffectID, behaviorStartTime, behaviorEndTime);

            // Post-attack speed function (if cancel event is present to approximate end of animation).
            if (info.AnimationCancelEventEnd != -1.0f)
            {
                float animationEndTime = info.AnimationCancelEventEnd;
                float minEndRealTime = behaviorEndTime + (0.5f * (animationEndTime - behaviorEndTime));
                float maxEndRealTime = behaviorEndTime + (1.3f * (animationEndTime - behaviorEndTime));
                float newAnimationEndTime = minEndRealTime + (float)Rand.NextDouble() * (maxEndRealTime - minEndRealTime);
                if (DEBUG)
                {
                    Console.WriteLine($"    Attack end time: {behaviorEndTime} (before pre-attack speed change)");
                    Console.WriteLine($"    Animation end time: {animationEndTime} => {newAnimationEndTime}");
                    Console.WriteLine($"    Random min/max: {minEndRealTime}, {maxEndRealTime}");
                }
                List<int> postAttackSpeedFunction = GetRandomSpeedFunction(behaviorEndTime, animationEndTime, newAnimationEndTime);
                ApplySpeedFunction(behaviorAnim, postAttackSpeedFunction);
            }
        }
        List<int> GetRandomSpeedFunction(float startTime, float endTime, float newEndTime)
        {
            int frameCount = (int)(30 * (endTime - startTime));
            float meanSpeed = endTime / newEndTime;
            int speedPointTotal = (int)(meanSpeed / QuantizedSpeed) * frameCount;
            return RoryAlgorithm(frameCount, speedPointTotal);
        }
        void ApplySpeedFunction(TAE.Animation animation, List<int> speedFunction)
        { 
            for (int i = 0; i < speedFunction.Count; i++)
            {
                int speedPoints = speedFunction[i];
                float speedMultiplier = (float)Math.Round(speedPoints * QuantizedSpeed, 2);
                if (!SpeedEffects.ContainsKey(speedMultiplier))
                {
                    throw new KeyNotFoundException($"No speed effect with multiplier {speedMultiplier}");
                }
                float startTime = Tools.SnapTimeTo30FPS(i * FrameDuration);
                float endTime = startTime + FrameDuration;  // effect lasts only one frame
                animation.ApplyEffect(SpeedEffects[speedMultiplier], startTime, endTime);
            }
        }
        void ApplySpeedAttackDamageMultiplier(TAE.Animation animation, float attackPowerScale, float startTime, float endTime)
        {
            // Rounds attackPowerScale to nearest multiple of 0.05.
            attackPowerScale = (int)Math.Round(20 * attackPowerScale) / 20.0f;
            if (!AttackDamageEffects.ContainsKey(attackPowerScale)) throw new KeyNotFoundException($"No speed effect with multiplier {attackPowerScale}");
            animation.ApplyEffect(AttackDamageEffects[attackPowerScale], startTime, endTime);
        }
        List<int> RoryAlgorithm(int frameCount, int speedPointTotal)
        {
            // Each speed point adds `quantizedSpeed` to the speed modifier for that frame.
            if (speedPointTotal < frameCount)
            {
                throw new ArgumentException("Cannot use RoryAlgorithm with less speed points than frame count.");
            }
            List<int> function = Enumerable.Repeat(UseRemovalRory ? speedPointTotal / frameCount : 1, frameCount).ToList();
            for (int i = 0; i < speedPointTotal - frameCount; i++)
            {
                if (UseRemovalRory)
                {
                    int frameRemovalIndex = GetRandomValidRoryFrameIndex(function, MaxDifference, MaxSpeedPoints, UseWeightedRory, forRemoval: true, ignoreEndpoints: true);
                    function[frameRemovalIndex] -= 1;
                }
                int frameAdditionIndex = GetRandomValidRoryFrameIndex(function, MaxDifference, MaxSpeedPoints, UseWeightedRory, forRemoval: false, ignoreEndpoints: UseRemovalRory);
                function[frameAdditionIndex] += 1;
            }
            return function;
        }
        int GetRandomValidRoryFrameIndex(List<int> function, int maxDifference, int maxSpeedPoints, bool weighted = false, bool forRemoval = false, bool ignoreEndpoints = false)
        {
            // Return a random valid frame index, where "valid" means adding one won't push its
            // difference to its neighbors above `maxDifference`.
            List<int> validIndices = new List<int>();
            if (!ignoreEndpoints)
            {
                if (forRemoval && function[0] < maxSpeedPoints && (function[1] - function[0]) < maxDifference)
                {
                    validIndices.Add(0);  // valid for removal
                }
                else if (function[0] < maxSpeedPoints && (function[0] - function[1]) < maxDifference)
                {
                    validIndices.Add(0);  // valid for addition
                }
            }
            
            for (int i = 1; i < function.Count - 1; i++)
            {
                if (forRemoval && function[i] > 1 && function[i - 1] - function[i] < maxDifference && function[i + 1] - function[i] < maxDifference)
                {
                    validIndices.Add(i);  // valid for removal
                }
                else if (function[i] < maxSpeedPoints && function[i] - function[i - 1] < maxDifference && function[i] - function[i + 1] < maxDifference)
                {
                    validIndices.Add(i);  // valid for addition
                }
            }
            if (!ignoreEndpoints)
            {
                if (forRemoval && function[function.Count - 1] < maxSpeedPoints && function[function.Count - 2] - function[function.Count - 1] < maxDifference)
                {
                    validIndices.Add(function.Count - 1);  // valid for removal
                }
                else if (function[function.Count - 1] < maxSpeedPoints && function[function.Count - 1] - function[function.Count - 2] < maxDifference)
                {
                    validIndices.Add(function.Count - 1);  // valid for addition
                }
            }
            if (validIndices.Count == 0)
            {
                foreach (int i in function)
                {
                    Console.Write($"{i} ");
                }
                Console.Write("\n");
                throw new ArithmeticException($"No valid indices. Max speed points = {maxSpeedPoints}, max difference = {maxDifference}.");
            }
            int randomIndex = weighted ? GetRandomWeightedIndex(function, validIndices) : validIndices[Rand.Next(validIndices.Count)];
            return randomIndex;
        }
        int GetRandomWeightedIndex(List<int> weights, List<int> validIndices)
        {
            // Return a random index in the valid subset of the given list, weighted by the value at that index.
            int weightSum = 0;
            foreach (int i in validIndices)
            {
                weightSum += weights[i];
            }
            int roll = Rand.Next(weightSum);
            int cumSum = 0;
            foreach (int i in validIndices)
            {
                cumSum += weights[i];
                if (roll < cumSum)
                {
                    return i;
                }
            }
            Console.WriteLine($"Weight index error: roll={roll}, weightSum={weightSum}");
            throw new IndexOutOfRangeException($"Error while getting weighted random index (roll = {roll}, weight sum = {weightSum})");
        }
    }

    class Tools
    {
        public static float GetRealTAETime(TAE.Animation animation, float time, Dictionary<int, float> speedEffects)
        {
            // Looks for TAE events that apply speed-affecting SpEffect IDs in the given dictionary
            // and returns the real "wall time" of the given TAE animation time, relative to animation start.
            List<TAE.Event> speedEvents = new List<TAE.Event>(animation.Events.Where(
                e => e.Type == 66 && speedEffects.ContainsKey(Convert.ToInt32(e.Parameters["SpEffectID"]))));
            int frame = 0;
            float frameTime = frame / 30.0f;
            float realTime = 0;
            while (frameTime < time)
            {
                float actualSpeed = 1;
                foreach (TAE.Event speedEvent in speedEvents)
                {
                    if (speedEvent.StartTime <= frameTime && frameTime < speedEvent.EndTime)
                    {
                        if (actualSpeed != 1)
                        {
                            throw new ArgumentException($"Animation contains multiple overlapping speed effects at time {frameTime}.");
                        }
                        int spEffectID = Convert.ToInt32(speedEvent.Parameters["SpEffectID"]);
                        actualSpeed *= speedEffects[spEffectID];
                    }
                }
                realTime += (1 / 30.0f) / actualSpeed;
                frame += 1;
                frameTime = frame / 30.0f;
            }
            return realTime;
        }
        public static float GetRealEventStartTime(TAE.Animation animation, TAE.Event taeEvent, Dictionary<int, float> speedEffects)
        {
            return GetRealTAETime(animation, taeEvent.StartTime, speedEffects);
        }
        public static float GetRealEventEndTime(TAE.Animation animation, TAE.Event taeEvent, Dictionary<int, float> speedEffects)
        {
            return GetRealTAETime(animation, taeEvent.EndTime, speedEffects);
        }
        public static float SnapTimeTo30FPS(float time)
        {
            // Snaps given time value to 30 FPS.
            int frames = (int)Math.Round(30 * time);
            return frames / 30.0f;
        }
        public static float GuessBulletRadius(Bullet bullet, SoulsMod sm)
        {
            // Looks for the deepest possible hit radius (preferring "Final" over "Initial") in recursive bullet hierarchy.
            int childBulletID = bullet.BulletOnHit;
            if (childBulletID != -1)
            {
                return GuessBulletRadius(sm.GPARAM.Bullets[childBulletID], sm);
            }
            else
            {
                if (bullet.FinalHitRadius > 0.0f) return bullet.FinalHitRadius;
                return bullet.InitialHitRadius;
            }

        }
        public static void DrawAnimation(TAE.Animation animation, int framesPerSpace = 1, bool showArgNames = true, bool showTimes = true)
        {
            // Draw an animation's events on a timeline in ASCII. Increase `framesPerSpace` to compress the time axis.
            Console.WriteLine($"Animation {animation.ID}");
            foreach (var e in animation.Events)
            {
                int startSpaces = (int)Math.Round(e.StartTime * 30 / framesPerSpace, 0);
                float durationSeconds = (e.EndTime - e.StartTime);
                int durationSpaces = (int)Math.Round(durationSeconds * 30 / framesPerSpace, 0);
                List<string> eventArgs = new List<string>();
                if (e.Parameters != null)
                {
                    foreach (var arg in e.Parameters.Values)
                    {
                        eventArgs.Add(showArgNames ? $"{arg.Key}={arg.Value}" : $"{arg.Value}");
                    }
                }
                string eventArgString = (e.Parameters != null) ? "(" + string.Join<string>(", ", eventArgs) + ")" : "";
                string eventLabel = new string(' ', startSpaces) + $"{e.Type} {e.TypeName}{eventArgString}";
                if (showTimes)
                {
                    eventLabel += $" [{e.StartTime:0.00} -> {e.EndTime:0.00}]";
                }
                string eventTimeline = new string(' ', startSpaces) + "|" + new string('>', durationSpaces);
                Console.WriteLine(eventLabel);
                Console.WriteLine(eventTimeline);
            }
        }
        public static void DrawSpeedFunction(List<int> speedFunction, float maxSpeed, float quantizedSpeed)
        {
            int speedEffectCount = (int)(maxSpeed / quantizedSpeed);
            for (int row = speedEffectCount; row > 0; row--)
            {
                
                float speedMultiplier = (float)Math.Round(row * quantizedSpeed, 2); ;
                Console.Write($"{speedMultiplier:0.00} | ");
                foreach (int speedPoints in speedFunction)
                {
                    if (speedMultiplier == 1.00f)
                    {
                        Console.Write("-");
                    }
                    else
                    {
                        Console.Write((speedPoints >= row) ? "o" : " ");
                    }
                }
                Console.Write("\n");
            }
            Console.WriteLine("   Frames -->");
        }
    }
    class NPCAnimationInfo
    {
        // Holds basic information (mostly boolean) about given NPC animation and provides methods
        // for retrieving Behavior, Attack, Bullet, and SpEffect entries for animations that invoke
        // behaviors (with TAE event 1 or 4).
        public static readonly long[] DashIds = { 680, 700, 701, 702, 703 };

        public readonly TAE.Event InvokeAttackEvent;
        public readonly List<TAE.Event> AllInvokeAttackEvents = new List<TAE.Event>();
        public readonly TAE.Event InvokeBulletEvent;
        public readonly List<TAE.Event> AllInvokeBulletEvents = new List<TAE.Event>();
        public readonly TAE.Event PushEvent;
        public readonly long AttackBehaviorParamId = -1;
        public readonly List<long> AllAttackBehaviorParamIds = new List<long>();
        public readonly long BulletBehaviorParamId = -1;
        public readonly List<long> AllBulletBehaviorParamIds = new List<long>();
        public readonly long BulletDummyPolyId = -1;
        public readonly List<long> AllBulletDummyPolyIds = new List<long>();
        public readonly float AnimationCancelEventEnd = -1.0f;  // best guess at end of animation, if available
        
        SoulsMod Mod { get; }
        TAE.Animation CurrentAnim { get; }  // for exception messages

        public bool IsDeath { get; }
        public bool IsMove { get; }
        public bool IsDash { get; }
        public bool IsThrow { get; }
        public bool HasInvokeBehaviorEvent { get; }  // either attack or bullet
        public bool IsInjury { get; }
        public bool IsGeneric { get; }

        public NPCAnimationInfo(TAE.Animation anim, int characterID, SoulsMod mod)
        {
            ChrHandler chrHandler = mod[characterID];
            if (chrHandler.ID == 0)
            {
                throw new ArgumentException("`NPCAnimationInfo` must receive a non-player `chrHandler`.");
            }
            InvokeAttackEvent = anim.FindEvent(1);
            AllInvokeAttackEvents = new List<TAE.Event>(anim.Events.Where(e => e.Type == 1));
            InvokeBulletEvent = anim.FindEvent(2);
            AllInvokeBulletEvents = new List<TAE.Event>(anim.Events.Where(e => e.Type == 2));
            PushEvent = anim.FindEvent(307);

            CurrentAnim = anim;
            Mod = mod;

            IsDeath = anim.FindJumpTable(12) != null;
            IsMove = anim.InRange(200, 599);
            IsDash = DashIds.Contains(anim.ID);
            IsThrow = chrHandler.ThrowAnimIds.Contains((int)anim.ID);
            HasInvokeBehaviorEvent = InvokeAttackEvent != null || InvokeBulletEvent != null || PushEvent != null;
            IsInjury = anim.InRange(2000, 2299);

            TAE.Event animationCancelEvent = anim.FindJumpTable(86);
            if (animationCancelEvent != null)
            {
                AnimationCancelEventEnd = animationCancelEvent.EndTime;
            }

            if (AllInvokeAttackEvents.Count != 0)
            {
                foreach (var invokeAttackEvent in AllInvokeAttackEvents)
                {
                    int behaviorSubId = Convert.ToInt32(invokeAttackEvent.Parameters["BehaviorSubID"]);
                    long behaviorParamId = 200000000 + 10000 * chrHandler.ID + behaviorSubId;
                    AllAttackBehaviorParamIds.Add(behaviorParamId);
                }
                AttackBehaviorParamId = AllAttackBehaviorParamIds[0];
            }

            if (AllInvokeBulletEvents.Count != 0)
            {
                foreach (var invokeBulletEvent in AllInvokeBulletEvents)
                {
                    int behaviorSubId = Convert.ToInt32(invokeBulletEvent.Parameters["BehaviorSubID"]);
                    long behaviorParamId = 200000000 + 10000 * chrHandler.ID + behaviorSubId;
                    AllBulletBehaviorParamIds.Add(behaviorParamId);
                    int behaviorDummyPolyId = Convert.ToInt32(invokeBulletEvent.Parameters["DummyPolyID"]);
                    AllBulletDummyPolyIds.Add(behaviorDummyPolyId);
                }
                BulletBehaviorParamId = AllBulletBehaviorParamIds[0];
                BulletDummyPolyId = AllBulletDummyPolyIds[0];
            }
        }
        public Behavior GetAttackBehavior(int invokeAttackEventIndex = 0)
        {
            long behaviorParamId = AllAttackBehaviorParamIds[invokeAttackEventIndex];
            if (behaviorParamId == -1)
            {
                throw new MissingFieldException($"Animation {CurrentAnim.ID} has no InvokeAttackBehavior event with index {invokeAttackEventIndex}.");
            }
            if (!Mod.GPARAM.BehaviorsNPC.Keys.Contains(behaviorParamId))
                return null;
            return Mod.GPARAM.BehaviorsNPC[behaviorParamId];  // returns null if ID is missing
        }
        public Behavior GetBulletBehavior(int invokeBulletEventIndex = 0)
        {
            long behaviorParamId = AllBulletBehaviorParamIds[invokeBulletEventIndex];
            if (behaviorParamId == -1)
            {
                throw new MissingFieldException($"Animation {CurrentAnim.ID} has no InvokeBulletBehavior event with index {invokeBulletEventIndex}.");
            }
            if (!Mod.GPARAM.BehaviorsNPC.Keys.Contains(behaviorParamId))
                return null;
            return Mod.GPARAM.BehaviorsNPC[behaviorParamId];  // returns null if ID is missing
        }
        public Attack GetAttack(int invokeAttackEventIndex = 0)
        {
            Behavior behavior = GetAttackBehavior(invokeAttackEventIndex);
            if (behavior == null) return null;
            if (behavior.ReferenceType != 0)
            {
                throw new MissingFieldException($"Behavior {AllAttackBehaviorParamIds[invokeAttackEventIndex]} has reference type {behavior.ReferenceType}, not 0.");
            }
            if (!Mod.GPARAM.AttacksNPC.Keys.Contains(behavior.RefID))
                return null;
            return Mod.GPARAM.AttacksNPC[behavior.RefID];
        }
        public Bullet GetBullet(int invokeBulletEventIndex = 0)
        {
            Behavior behavior = GetBulletBehavior(invokeBulletEventIndex);
            if (behavior == null) return null;
            if (behavior.ReferenceType != 1)
            {
                throw new MissingFieldException($"Behavior {AllBulletBehaviorParamIds[invokeBulletEventIndex]} has reference type {behavior.ReferenceType}, not 1.");
            }
            if (!Mod.GPARAM.Bullets.Keys.Contains(behavior.RefID))
                return null;
            return Mod.GPARAM.Bullets[behavior.RefID];
        }
        public SpEffect GetSpEffect(int invokeBulletEventIndex = 0)
        {
            // Uses InvokeBulletBehavior TAE event.
            Behavior behavior = GetBulletBehavior(invokeBulletEventIndex);
            if (behavior == null) return null;
            if (behavior.ReferenceType != 2)
            {
                throw new MissingFieldException($"Behavior {AllBulletBehaviorParamIds[invokeBulletEventIndex]} has reference type {behavior.ReferenceType}, not 2.");
            }
            if (!Mod.GPARAM.SpEffects.Keys.Contains(behavior.RefID))
                return null;
            return Mod.GPARAM.SpEffects[behavior.RefID];
        }
    }
}