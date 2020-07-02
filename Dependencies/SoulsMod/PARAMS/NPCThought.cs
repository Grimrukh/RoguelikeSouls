using SoulsFormats;
using System;

namespace SoulsFormatsMod.PARAMS
{
    public class NPCThought : RowWrapper
    {
        public NPCThought() { }
        public NPCThought(PARAM.Row r, GameParamHandler gParam, TextHandler text) : base(r, gParam, text) { }

        // LINK_STRING: <AI:Logic>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// ID of logic (non-battle) Lua script.
        /// </summary>
        public int LogicID
        {
            get => Convert.ToInt32(Row["logicId"].Value);
            set => Row["logicId"].Value = value;
        }

        // LINK_STRING: <AI:Battle>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Battle goal ID used to look up battle Lua script.
        /// </summary>
        public int BattleID
        {
            get => Convert.ToInt32(Row["battleGoalID"].Value);
            set => Row["battleGoalID"].Value = value;
        }

        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance considered to be close range by this NPC (for scripts).
        /// </summary>
        public float NearDistance
        {
            get => Convert.ToSingle(Row["nearDist"].Value);
            set => Row["nearDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance considered to be medium range by this NPC (for scripts).
        /// </summary>
        public float MidDistance
        {
            get => Convert.ToSingle(Row["midDist"].Value);
            set => Row["midDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance considered to be long range by this NPC (for scripts).
        /// </summary>
        public float FarDistance
        {
            get => Convert.ToSingle(Row["farDist"].Value);
            set => Row["farDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance beyond which the NPC will not attempt to fight.
        /// </summary>
        public float OutOfRangeDistance
        {
            get => Convert.ToSingle(Row["outDist"].Value);
            set => Row["outDist"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Retreat goal time when touching an 'enemy wall' that blocks the NPC's
        /// path. (Not clear what an 'enemy wall' means. Almost always set to 5
        /// (rarely 6).
        /// </summary>
        public float RetreatTimeAfterHittingEnemyWall
        {
            get => Convert.ToSingle(Row["BackHomeLife_OnHitEneWal"].Value);
            set => Row["BackHomeLife_OnHitEneWal"].Value = value;
        }
        // LINK_STRING: <AI:Logic>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Lua script to use when NPC's AI enters the 'Caution' state (I think).
        /// Requires a CautionGoalAction value of 4. Used only by Hawkeye Gough
        /// (411000); zero otherwise.
        /// </summary>
        public int CautionGoalID
        {
            get => Convert.ToInt32(Row["goalID_ToCaution"].Value);
            set => Row["goalID_ToCaution"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation to use if the NPC gets stuck on a destructible object.
        /// Usually 3000 (basic attack).
        /// </summary>
        public int StuckAnimationID
        {
            get => Convert.ToInt32(Row["idAttackCannotMove"].Value);
            set => Row["idAttackCannotMove"].Value = value;
        }
        // LINK_STRING: <AI:Logic>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Lua script to use when NPC's AI enters the 'Search' state (I think).
        /// Requires a SearchGoalAction value of 4. Not used by any vanilla NPC
        /// (all zero).
        /// </summary>
        public int SearchGoalID
        {
            get => Convert.ToInt32(Row["goalID_ToFind"].Value);
            set => Row["goalID_ToFind"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation to play when responding to a call for help. Usually set to
        /// -1 for NPCs who can reply to calls for help, which I assume means no
        /// animation is played. Set to 0 for NPCs who ignore calls for help.
        /// </summary>
        public int HelpCallResponseAnimation
        {
            get => Convert.ToInt32(Row["callHelp_ActionAnimId"].Value);
            set => Row["callHelp_ActionAnimId"].Value = value;
        }
        // LINK_STRING: <Animation>
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Animation to play when calling for help. Only used by Female Ghost
        /// (7300) and Male Ghost and summons (-1). I assume -1 means no animation
        /// is played. Set to 0 for all other NPCs.
        /// </summary>
        public int HelpCallSendAnimation
        {
            get => Convert.ToInt32(Row["callHelp_CallActionId"].Value);
            set => Row["callHelp_CallActionId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance of NPC eyesight (in meters).
        /// </summary>
        public ushort SightDistance
        {
            get => Convert.ToUInt16(Row["eye_dist"].Value);
            set => Row["eye_dist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance of NPC hearing (in meters).
        /// </summary>
        public ushort HearingDistance
        {
            get => Convert.ToUInt16(Row["ear_dist"].Value);
            set => Row["ear_dist"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'Distance to reduce the size of the sound
        /// source. Sounds less than this distance will not be heard.' Set to 1
        /// for Bloatheads and Bloathead Sorcerers and 0 for everyone else.
        /// </summary>
        public ushort HearingCutDistance
        {
            get => Convert.ToUInt16(Row["ear_soundcut_dist"].Value);
            set => Row["ear_soundcut_dist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance of NPC smell (auto-detect).
        /// </summary>
        public ushort SmellDistance
        {
            get => Convert.ToUInt16(Row["nose_dist"].Value);
            set => Row["nose_dist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Absolute furthest the NPC can travel from their nest before
        /// retreating, in or out of battle. (Argument of internal GOAL function
        /// 'COMMON_SetBattleActLogic()'.) Usually set to about 50% more than
        /// BattleRetreatDistance.
        /// </summary>
        public ushort MaxRetreatDistance
        {
            get => Convert.ToUInt16(Row["maxBackhomeDist"].Value);
            set => Row["maxBackhomeDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Furthest distance the NPC can travel from their nest before retreating
        /// in battle. (Argument of internal GOAL function
        /// 'COMMON_SetBattleActLogic()'.)
        /// </summary>
        public ushort BattleRetreatDistance
        {
            get => Convert.ToUInt16(Row["backhomeDist"].Value);
            set => Row["backhomeDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Target distance at which battle mode is triggered while the enemy is
        /// retreating. (Argument of internal GOAL function
        /// 'COMMON_SetBattleActLogic()'.)
        /// </summary>
        public ushort RetreatBattleStartDistance
        {
            get => Convert.ToUInt16(Row["backhomeBattleDist"].Value);
            set => Row["backhomeBattleDist"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Lifespan of Acts outside of battle. Set to 10 for Bloatheads and
        /// Bloathead Sorcerers, 0 for Priscilla's Tail and the Bed of Chaos bug,
        /// and 5 for everyone else. (Argument of internal GOAL function
        /// 'COMMON_SetBattleActLogic()'.)
        /// </summary>
        public ushort NonBattleActLife
        {
            get => Convert.ToUInt16(Row["nonBattleActLife"].Value);
            set => Row["nonBattleActLife"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time that NPC will search for a lost target before retreating (I
        /// think). Set to 20 for everyone except the Bounding Demons of Izalith,
        /// who have a value of 0.
        /// </summary>
        public ushort SearchTimeBeforeRetreat
        {
            get => Convert.ToUInt16(Row["BackHome_LookTargetTime"].Value);
            set => Row["BackHome_LookTargetTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Distance that NPC will search for a lost target before retreating (I
        /// think). Set to 20 for everyone except the Bounding Demons of Izaltih,
        /// who have a value of 0.
        /// </summary>
        public ushort SearchDistanceBeforeRetreat
        {
            get => Convert.ToUInt16(Row["BackHome_LookTargetDist"].Value);
            set => Row["BackHome_LookTargetDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time to forget about sighted targets. Usually set to 600.
        /// </summary>
        public ushort SightForgetTime
        {
            get => Convert.ToUInt16(Row["SightTargetForgetTime"].Value);
            set => Row["SightTargetForgetTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time to forget about heard targets. Usually set to 300.
        /// </summary>
        public ushort HearingForgetTime
        {
            get => Convert.ToUInt16(Row["SoundTargetForgetTime"].Value);
            set => Row["SoundTargetForgetTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Target distance at which battle mode is triggered.
        /// </summary>
        public ushort BattleStartDistance
        {
            get => Convert.ToUInt16(Row["BattleStartDist"].Value);
            set => Row["BattleStartDist"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Determines which calls for help this NPC will respond to (must match
        /// caller's HelpCallGroupID). Only 0 (no ID) and 1 are used.
        /// </summary>
        public ushort HelpGroupID
        {
            get => Convert.ToUInt16(Row["callHelp_MyPeerId"].Value);
            set => Row["callHelp_MyPeerId"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// HelpGroupID value of NPCs who should respond to calls for help by this
        /// NPC. Only 0 (no ID) and 1 are used.
        /// </summary>
        public ushort HelpCallGroupID
        {
            get => Convert.ToUInt16(Row["callHelp_CallPeerId"].Value);
            set => Row["callHelp_CallPeerId"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'Get damage rate (%) for target system
        /// evaluation information.' Set to 0 for summons, phantoms, and the
        /// Parasitic Wall Hugger, and 100 for everyone else.
        /// </summary>
        public ushort TargetSysDamageRate
        {
            get => Convert.ToUInt16(Row["targetSys_DmgEffectRate"].Value);
            set => Row["targetSys_DmgEffectRate"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Value from 0 to 100 that determines the number of simultaneous attacks
        /// made by this NPC's team. Higher values mean that less members of this
        /// team can participate in attacks at the same time. (I presume that the
        /// total score of attacking team members cannot exceed 100.) Usually set
        /// to 25 or 100.
        /// </summary>
        public byte TeamAttackEffectivity
        {
            get => Convert.ToByte(Row["TeamAttackEffectivity"].Value);
            set => Row["TeamAttackEffectivity"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angular width of sight field in degrees.
        /// </summary>
        public byte SightRangeHeight
        {
            get => Convert.ToByte(Row["eye_angX"].Value);
            set => Row["eye_angX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angular height of sight field in degrees.
        /// </summary>
        public byte SightRangeWidth
        {
            get => Convert.ToByte(Row["eye_angY"].Value);
            set => Row["eye_angY"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angular width of hearing field in degrees.
        /// </summary>
        public byte HearingRangeHeight
        {
            get => Convert.ToByte(Row["ear_angX"].Value);
            set => Row["ear_angX"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Angular height of hearing field in degrees.
        /// </summary>
        public byte HearingRangeWidth
        {
            get => Convert.ToByte(Row["ear_angY"].Value);
            set => Row["ear_angY"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Minimum distance from AI target for help call to be made. Always zero.
        /// </summary>
        public byte HelpCallTargetMinDistance
        {
            get => Convert.ToByte(Row["callHelp_CallValidMinDistTarget"].Value);
            set => Row["callHelp_CallValidMinDistTarget"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Maximum distance of friend to receive help call from this NPC. Set to
        /// 50 for both Male and Female Ghosts, and 0 for everyone else.
        /// </summary>
        public byte HelpCallFriendMaxDistance
        {
            get => Convert.ToByte(Row["callHelp_CallValidRange"].Value);
            set => Row["callHelp_CallValidRange"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Time until call for help is forgotten by responder.
        /// </summary>
        public byte HelpCallForgetTime
        {
            get => Convert.ToByte(Row["callHelp_ForgetTimeByArrival"].Value);
            set => Row["callHelp_ForgetTimeByArrival"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'Minimum time for response goal at first waiting
        /// goal'. Units are in tenths of a second. Only used for Male Ghosts
        /// (20).
        /// </summary>
        public byte HelpCallMinWaitTime
        {
            get => Convert.ToByte(Row["callHelp_MinWaitTime"].Value);
            set => Row["callHelp_MinWaitTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'Maximum time for response goal at first waiting
        /// goal'. Units are in tenths of a second. Only used for Female Ghosts
        /// (40).
        /// </summary>
        public byte HelpCallMaxWaitTime
        {
            get => Convert.ToByte(Row["callHelp_MaxWaitTime"].Value);
            set => Row["callHelp_MaxWaitTime"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of action taken when AI enters the 'Caution' state.
        /// </summary>
        public byte CautionGoalAction
        {
            get => Convert.ToByte(Row["goalAction_ToCaution"].Value);
            set => Row["goalAction_ToCaution"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Type of action taken when AI enters the 'Search' state.
        /// </summary>
        public byte SearchGoalAction
        {
            get => Convert.ToByte(Row["goalAction_ToFind"].Value);
            set => Row["goalAction_ToFind"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Set to 0 for NPCs who do not reply to calls for help and 1 for NPCs
        /// who do.
        /// </summary>
        public byte HelpCallReplyType
        {
            get => Convert.ToByte(Row["callHelp_ReplyBehaviorType"].Value);
            set => Row["callHelp_ReplyBehaviorType"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If 1, this NPC will ignore navmesh when moving. True for Ghosts and
        /// enemies that don't move at all.
        /// </summary>
        public byte IgnoreNavmesh
        {
            get => Convert.ToByte(Row["disablePathMove"].Value);
            set => Row["disablePathMove"].Value = value;
        }
        // DEFAULT_VISIBLE: False
        /// <summary>
        /// Internal description: 'If enabled, arrival determination is performed
        /// even if the line of sight is not passed.' True only for Hawkeye Gough.
        /// </summary>
        public byte SkipArrivalVisibleCheck
        {
            get => Convert.ToByte(Row["skipArrivalVisibleCheck"].Value);
            set => Row["skipArrivalVisibleCheck"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// Internal description: 'Thought attribute: when enabled, it plays the
        /// role of a wrap.' I don't know exactly what that means, but this is
        /// likely important for something. Enabled for Soulmass and Pursuers,
        /// non-giant Rats, Infested Ghouls, Mushrooms, most Hollows (not
        /// archers), Male Ghosts, normal Skeletons and Skeleton Beasts, Pisaca,
        /// Gardeners, Bloatheads (not Sorcerers), Humanity Phantoms, and the Four
        /// Kings.
        /// </summary>
        public byte AdmirerAttribute
        {
            get => Convert.ToByte(Row["thinkAttr_doAdmirer"].Value);
            set => Row["thinkAttr_doAdmirer"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC will pursue targets off navmesh edges (survivable
        /// falls).
        /// </summary>
        public bool CanFallOffEdges
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_Edge"].Value));
            set => Row["enableNaviFlg_Edge"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC can enter navmesh regions flagged as 'large spaces'.
        /// </summary>
        public bool CanNavigateWideSpaces
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_LargeSpace"].Value));
            set => Row["enableNaviFlg_LargeSpace"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC will use ladders.
        /// </summary>
        public bool CanNavigateLadders
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_Ladder"].Value));
            set => Row["enableNaviFlg_Ladder"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC can fall into navmesh holes.
        /// </summary>
        public bool CanNavigateHoles
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_Hole"].Value));
            set => Row["enableNaviFlg_Hole"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC can go through doors (but not necessarily open
        /// closed doors).
        /// </summary>
        public bool CanNavigateDoors
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_Door"].Value));
            set => Row["enableNaviFlg_Door"].Value = value;
        }
        // DEFAULT_VISIBLE: True
        /// <summary>
        /// If True, this NPC can go through walls (i.e. ignores navmesh walls).
        /// </summary>
        public bool CanNavigateInsideWalls
        {
            get => MiscUtil.AsBoolean(Convert.ToByte(Row["enableNaviFlg_InSideWall"].Value));
            set => Row["enableNaviFlg_InSideWall"].Value = value;
        }
    }
}