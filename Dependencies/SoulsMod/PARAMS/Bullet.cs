using SoulsFormats;
using System;
using System.Linq;

namespace SoulsFormatsMod.PARAMS
{
    public class Bullet : RowWrapper
    {
        public Bullet() { }
        public Bullet(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        public Attack GetAttackPC => GPARAM.AttacksPC[BulletAttack];
        public Attack GetAttackNPC => GPARAM.AttacksNPC[BulletAttack];

        public Attack NewAttackPC(long? id = null)
        {
            Attack attack;
            if (!id.HasValue) id = GPARAM.AttacksPC.Values.Where(b => b.ID < 100000).Max(b => b.ID) + 1;

            if (GPARAM.AttacksPC.Values.Any(atk => atk.ID == BulletAttack))
                attack = GPARAM.AttacksPC.CopyRow(BulletAttack, id.Value);
            else
                attack = GPARAM.AttacksPC.AddRow(id.Value);

            BulletAttack = attack;
            return attack;
        }


        // LINK_STRING: <Params:Attacks>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Attack parameters for bullet impact. Only certain fields in the attack
        /// parameter are used. Could be directed to either PlayerAttacks table or
        /// NonPlayerAttacks table, depending on the bullet's owner. Set to 0 if
        /// bullet has no attack data (no damage).
        /// </summary>
        public int BulletAttack
        {
            get => Convert.ToInt32(Row["atkId_Bullet"].Value);
            set => Row["atkId_Bullet"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect ID for bullet projectile.
        /// </summary>
        public int ProjectileFX
        {
            get => Convert.ToInt32(Row["sfxId_Bullet"].Value);
            set => Row["sfxId_Bullet"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect ID for bullet impact.
        /// </summary>
        public int ImpactFX
        {
            get => Convert.ToInt32(Row["sfxId_Hit"].Value);
            set => Row["sfxId_Hit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Visual effect ID for when bullet is blocked (I think). Used
        /// predominantly for arrows and throwing knives.
        /// </summary>
        public int FlickFX
        {
            get => Convert.ToInt32(Row["sfxId_Flick"].Value);
            set => Row["sfxId_Flick"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum time before bullet will disappear on its own. -1 means it will
        /// last indefinitely.
        /// </summary>
        public float LifeTime
        {
            get => Convert.ToSingle(Row["life"].Value);
            set => Row["life"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance at which attenuation of the projectile begins.
        /// </summary>
        public float AttenuationDistance
        {
            get => Convert.ToSingle(Row["dist"].Value);
            set => Row["dist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time between emitted bullets. Does nothing for bullets that only shoot
        /// once and is generally left at zero for those bullets.
        /// </summary>
        public float LaunchInterval
        {
            get => Convert.ToSingle(Row["shootInterval"].Value);
            set => Row["shootInterval"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Downward acceleration of bullet. Rarely used.
        /// </summary>
        public float GravityBeforeAttenuation
        {
            get => Convert.ToSingle(Row["gravityInRange"].Value);
            set => Row["gravityInRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Downward acceleration of bullet after it passes the attenuation
        /// distance.
        /// </summary>
        public float GravityAfterAttenuation
        {
            get => Convert.ToSingle(Row["gravityOutRange"].Value);
            set => Row["gravityOutRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet will stop homing if it is within this distance of its homing
        /// target. Use this to prevent homing bullets from being too oppressive.
        /// </summary>
        public float ClosestHomingDistance
        {
            get => Convert.ToSingle(Row["hormingStopRange"].Value);
            set => Row["hormingStopRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Initial speed of bullet.
        /// </summary>
        public float InitialSpeed
        {
            get => Convert.ToSingle(Row["initVellocity"].Value);
            set => Row["initVellocity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Forward acceleration acting on bullet before it reaches the
        /// attenuation distance. Negative values will slow the bullet down.
        /// </summary>
        public float AccelerationBeforeAttenuation
        {
            get => Convert.ToSingle(Row["accelInRange"].Value);
            set => Row["accelInRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Forward acceleration acting on bullet after it passes the attenuation
        /// distance. Negative values will slow the bullet down.
        /// </summary>
        public float AccelerationAfterAttenuation
        {
            get => Convert.ToSingle(Row["accelOutRange"].Value);
            set => Row["accelOutRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum speed of bullet, regardless of acceleration.
        /// </summary>
        public float MaxSpeed
        {
            get => Convert.ToSingle(Row["maxVellocity"].Value);
            set => Row["maxVellocity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Minimum speed of bullet, regardless of acceleration.
        /// </summary>
        public float MinSpeed
        {
            get => Convert.ToSingle(Row["minVellocity"].Value);
            set => Row["minVellocity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time that acceleration is active after bullet creation.
        /// </summary>
        public float AccelerationTime
        {
            get => Convert.ToSingle(Row["accelTime"].Value);
            set => Row["accelTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance from owner at which the bullet starts homing in on targets.
        /// </summary>
        public float HomingStartDistance
        {
            get => Convert.ToSingle(Row["homingBeginDist"].Value);
            set => Row["homingBeginDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Initial hit radius of bullet projectile.
        /// </summary>
        public float InitialHitRadius
        {
            get => Convert.ToSingle(Row["hitRadius"].Value);
            set => Row["hitRadius"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Final hit radius of bullet projectile. Set to -1 if radius does not
        /// change, which is always coupled with a value of 0 for
        /// RadiusIncreaseDuration.
        /// </summary>
        public float FinalHitRadius
        {
            get => Convert.ToSingle(Row["hitRadiusMax"].Value);
            set => Row["hitRadiusMax"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time taken by bullet to transition from initial to final hit radius.
        /// Value of 0 are always coupled with values of -1 for
        /// RadiusIncreaseDuration. I'm not sure if this can actually decrease the
        /// hit radius if the final value is less than the initial value.
        /// </summary>
        public float RadiusIncreaseTime
        {
            get => Convert.ToSingle(Row["spreadTime"].Value);
            set => Row["spreadTime"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Delay between impact and 'explosion' (not sure if that refers to the
        /// visual effect and/or hitbox). Never used (always zero).
        /// </summary>
        public float ExpDelay
        {
            get => Convert.ToSingle(Row["expDelay"].Value);
            set => Row["expDelay"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'When shooting, aim to shift each component of
        /// XYZ by this amount.' Nonzero only for Hydra blasts and Vagrant
        /// attacks.
        /// </summary>
        public float HomingOffsetRange
        {
            get => Convert.ToSingle(Row["hormingOffsetRange"].Value);
            set => Row["hormingOffsetRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Duration of bullet impact hitbox. A value of zero means it is disabled
        /// immediately after first impact.
        /// </summary>
        public float HitboxLifeTime
        {
            get => Convert.ToSingle(Row["dmgHitRecordLifeTime"].Value);
            set => Row["dmgHitRecordLifeTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unknown. Used only for Gargoyle fire breath and Undead Dragon poison
        /// breath.
        /// </summary>
        public float ExternalForce
        {
            get => Convert.ToSingle(Row["externalForce"].Value);
            set => Row["externalForce"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to owner when bullet is created. (Unclear if it
        /// is applied repeatedly by repeating bullets.)
        /// </summary>
        public int OwnerSpecialEffect
        {
            get => Convert.ToInt32(Row["spEffectIDForShooter"].Value);
            set => Row["spEffectIDForShooter"].Value = value;
        }
        // LINK_STRING: <Params:AI>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// AI parameter ID for triggered floating bullets. Only used by Homing
        /// [Crystal] Soulmass (10000) and Pursuers (10001) in the vanilla game.
        /// </summary>
        public int BulletAI
        {
            get => Convert.ToInt32(Row["autoSearchNPCThinkID"].Value);
            set => Row["autoSearchNPCThinkID"].Value = value;
        }
        // LINK_STRING: <Params:Bullets>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet emitted on impact of this bullet. Used often for
        /// 'throw'/'landing' or 'parent'/'child' combinations, like a thrown
        /// Firebomb (bullet 110) triggering a fiery explosion (bullet 111). These
        /// can be chained together indefinitely (see White Dragon Breath, bullet
        /// 11500).
        /// </summary>
        public int BulletOnHit
        {
            get => Convert.ToInt32(Row["HitBulletID"].Value);
            set => Row["HitBulletID"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target hit by bullet. (Slot 0)
        /// </summary>
        public int HitSpecialEffect0
        {
            get => Convert.ToInt32(Row["spEffectId0"].Value);
            set => Row["spEffectId0"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target hit by bullet. (Slot 1)
        /// </summary>
        public int HitSpecialEffect1
        {
            get => Convert.ToInt32(Row["spEffectId1"].Value);
            set => Row["spEffectId1"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target hit by bullet. (Slot 2)
        /// </summary>
        public int HitSpecialEffect2
        {
            get => Convert.ToInt32(Row["spEffectId2"].Value);
            set => Row["spEffectId2"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target hit by bullet. (Slot 3)
        /// </summary>
        public int HitSpecialEffect3
        {
            get => Convert.ToInt32(Row["spEffectId3"].Value);
            set => Row["spEffectId3"].Value = value;
        }
        // LINK_STRING: <Params:SpecialEffects>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Special effect applied to target hit by bullet. (Slot 4)
        /// </summary>
        public int HitSpecialEffect4
        {
            get => Convert.ToInt32(Row["spEffectId4"].Value);
            set => Row["spEffectId4"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Number of bullets emitted at once.
        /// </summary>
        public ushort BulletCount
        {
            get => Convert.ToUInt16(Row["numShoot"].Value);
            set => Row["numShoot"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Turning angle of homing bullet per second. Higher values are better
        /// for homing.
        /// </summary>
        public short HomingAnglePerSecond
        {
            get => Convert.ToInt16(Row["homingAngle"].Value);
            set => Row["homingAngle"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angle of first bullet in degrees around the vertical axis, relative to
        /// the forward direction.
        /// </summary>
        public short AzimuthAngleStart
        {
            get => Convert.ToInt16(Row["shootAngle"].Value);
            set => Row["shootAngle"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angle from one bullet to the next around the vertical axis, beginning
        /// at the azimuth angle start.
        /// </summary>
        public short AzimuthAngleInterval
        {
            get => Convert.ToInt16(Row["shootAngleInterval"].Value);
            set => Row["shootAngleInterval"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angle between bullets in elevation.
        /// </summary>
        public short ElevationAngleInterval
        {
            get => Convert.ToInt16(Row["shootAngleXInterval"].Value);
            set => Row["shootAngleXInterval"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in physical damage per second.
        /// </summary>
        public sbyte PhysicalDamageDamp
        {
            get => Convert.ToSByte(Row["damageDamp"].Value);
            set => Row["damageDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in magic damage per second.
        /// </summary>
        public sbyte MagicDamageDamp
        {
            get => Convert.ToSByte(Row["spelDamageDamp"].Value);
            set => Row["spelDamageDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in fire damage per second.
        /// </summary>
        public sbyte FireDamageDamp
        {
            get => Convert.ToSByte(Row["fireDamageDamp"].Value);
            set => Row["fireDamageDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Percentage reduction in lightning damage per second.
        /// </summary>
        public sbyte LightningDamageDamp
        {
            get => Convert.ToSByte(Row["thunderDamageDamp"].Value);
            set => Row["thunderDamageDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Percentage reduction in stamina damage per second.
        /// </summary>
        public sbyte StaminaDamp
        {
            get => Convert.ToSByte(Row["staminaDamp"].Value);
            set => Row["staminaDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Percentage reduction in knockback power per second.
        /// </summary>
        public sbyte KnockbackDamp
        {
            get => Convert.ToSByte(Row["knockbackDamp"].Value);
            set => Row["knockbackDamp"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angle of elevation of first bullet. Positive values will angle the
        /// bullets up (e.g. Quelaag's fireballs) and negative values will angle
        /// the bullets down (e.g. most breath attacks).
        /// </summary>
        public sbyte FirstBulletElevationAngle
        {
            get => Convert.ToSByte(Row["shootAngleXZ"].Value);
            set => Row["shootAngleXZ"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unknown, but likely important. Set to 30 for most basic projectile
        /// magic.
        /// </summary>
        public byte LockShootLimitAngle
        {
            get => Convert.ToByte(Row["lockShootLimitAng"].Value);
            set => Row["lockShootLimitAng"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet will go through objects, players, and NPCs.
        /// </summary>
        public byte PiercesTargets
        {
            get => Convert.ToByte(Row["isPenetrate"].Value);
            set => Row["isPenetrate"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'Ratio of adding the previous moving direction
        /// to the current direction when a sliding bullet hits the wall.' Like
        /// ExternalForce, this is used only for Gargoyle and Undead Dragon breath
        /// (100) and is zero for everything else.
        /// </summary>
        public byte PreviousDirectionRatio
        {
            get => Convert.ToByte(Row["prevVelocityDirRate"].Value);
            set => Row["prevVelocityDirRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Attack type. Almost always 4 ('other'), but sometimes 3
        /// (knives/arrows/bolts).
        /// </summary>
        public byte AttackAttribute
        {
            get => Convert.ToByte(Row["atkAttribute"].Value);
            set => Row["atkAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Element attached to bullet hit.
        /// </summary>
        public byte ElementAttribute
        {
            get => Convert.ToByte(Row["spAttribute"].Value);
            set => Row["spAttribute"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines visual effects of bullet hit.
        /// </summary>
        public byte MaterialAttackType
        {
            get => Convert.ToByte(Row["Material_AttackType"].Value);
            set => Row["Material_AttackType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Sound and visual effects on hit.
        /// </summary>
        public byte EffectsOnHit
        {
            get => Convert.ToByte(Row["Material_AttackMaterial"].Value);
            set => Row["Material_AttackMaterial"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// 'Size' of attack. Never used.'
        /// </summary>
        public byte MaterialSize
        {
            get => Convert.ToByte(Row["Material_Size"].Value);
            set => Row["Material_Size"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Condition for determing if a new bullet will be generated when this
        /// bullet lands or expires.
        /// </summary>
        public byte LaunchConditionType
        {
            get => Convert.ToByte(Row["launchConditionType"].Value);
            set => Row["launchConditionType"].Value = value;
        }
        public byte FollowType
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Follow type.
        /// </summary>
        {

            get => Convert.ToByte(Row["FollowType"].Value);
            set => Row["FollowType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Origin type of bullet. Usually comes from model points ('damipoly').
        /// </summary>
        public byte OriginType
        {
            get => Convert.ToByte(Row["EmittePosType"].Value);
            set => Row["EmittePosType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Set whether bullets (e.g. arrows) stay stuck upon impact.
        /// </summary>
        public bool RemainAttachedToTarget
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isAttackSFX"].Value));
            set => Row["isAttackSFX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet hitbox is continuous (I think). Only used for corrosion cloud
        /// in vanilla.
        /// </summary>
        public bool IsEndlessHit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isEndlessHit"].Value));
            set => Row["isEndlessHit"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet will pierce the map (e.g. Stray Demon blast).
        /// </summary>
        public bool IsMapPiercing
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isPenetrateMap"].Value));
            set => Row["isPenetrateMap"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Bullet can hit any character.
        /// </summary>
        public bool HitsBothTeams
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isHitBothTeam"].Value));
            set => Row["isHitBothTeam"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Repeating bullets share the amount of times they have hit a target
        /// (usually so the target is only hit once by any of those repeating
        /// bullets).
        /// </summary>
        public bool SharedHitCheck
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isUseSharedHitList"].Value));
            set => Row["isUseSharedHitList"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Set to True if the same model point ('damipoly') is used multiple
        /// times when spawning the bullet.
        /// </summary>
        public bool UsesMultipleModelPoints
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isUseMultiDmyPolyIfPlace"].Value));
            set => Row["isUseMultiDmyPolyIfPlace"].Value = value;
        }
        public byte AttachEffectType
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Mostly 0, but sometimes 1 (Dragon Head breath, Grant AoE, Force
        /// miracles).
        /// </summary>
        {

            get => Convert.ToByte(Row["attachEffectType"].Value);
            set => Row["attachEffectType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this bullet will impact appropriate Force-type magic (e.g.
        /// arrows, bolts, knives).
        /// </summary>
        public bool CanBeDeflectedByMagic
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isHitForceMagic"].Value));
            set => Row["isHitForceMagic"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, hit FX are not produced if the bullet impacts water.
        /// </summary>
        public bool IgnoreFXOnWaterHit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isIgnoreSfxIfHitWater"].Value));
            set => Row["isIgnoreSfxIfHitWater"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Unclear effect, but True for knives/arrows/bolts and False otherwise.
        /// </summary>
        public bool IgnoreStateTransitionOnWaterHit
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isIgnoreMoveStateIfHitWater"].Value));
            set => Row["isIgnoreMoveStateIfHitWater"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this bullet will impact the Silver Pendant shield effect.
        /// True only for dark sorceries.
        /// </summary>
        public bool CanBeDeflectedBySilverPendant
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["isHitDarkForceMagic"].Value));
            set => Row["isHitDarkForceMagic"].Value = value;
        }
    }
}
