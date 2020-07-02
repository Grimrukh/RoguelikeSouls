REGISTER_GOAL(GOAL_KingIzalis523000_Battle, "KingIzalis523000Battle")
REGISTER_GOAL_NO_UPDATE(GOAL_KingIzalis523000_Battle, 1)

-- Now won't use two swipe attacks in a row.

-- 3000: small left swipe
-- 3001: small right swipe
-- 3002: left slam
-- 3003: right slam
-- 3004: long left swipe, then slam
-- 3005: long right swipe, then slam
-- 3006: long left swipe, long right swipe

-- (unused)
-- 3010: short forward left slam
-- 3011: short mid left slam
-- 3012: short far left slam
-- 3013: long forward left slam
-- 3014: long mid left slam
-- 3015: long far left slam
-- 3016: long very far left slam

KingIzalis523000Battle_Activate = function(ai, goal)
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = 0
   local func1_var16 = 0
   local func1_var17 = 0
   local func1_var18 = 0
   local func1_var19 = 0
   local func1_var20 = 0
   local func1_var21 = 0
   local func1_var22 = 0
   local func1_var23 = 0
   local func1_var24 = 0
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412550) then
      func1_var18 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412552) then
      func1_var19 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412554) then
      func1_var20 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412555) then
      func1_var21 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412556) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1412557) then
      func1_var22 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412560) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1412561) then
      func1_var23 = 1
   end
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1412564) then
      func1_var24 = 1
   end
   if func1_var18 == 1 then
      func1_var10 = 100
   end
   if func1_var19 == 1 then
      func1_var11 = 100
   end
   if func1_var20 == 1 then
      func1_var12 = 100
   end
   if func1_var21 == 1 then
      func1_var13 = 100
   end
   if func1_var22 == 1 and ai:IsFinishTimer(0) then
      func1_var14 = 100
   end
   if func1_var23 == 1 and ai:IsFinishTimer(0) then
      func1_var15 = 100
   end
   if func1_var24 == 1 and ai:IsFinishTimer(0) then
      func1_var16 = 100
   end
   local func1_var25 = ai:GetRandam_Int(1, func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17)
   if func1_var25 <= func1_var10 then
      KingIzalis523000_Act01(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 then
      KingIzalis523000_Act02(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 + func1_var12 then
      KingIzalis523000_Act03(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 then
      KingIzalis523000_Act04(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 then
      KingIzalis523000_Act05(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 then
      KingIzalis523000_Act06(ai, goal)
   elseif func1_var25 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 then
      KingIzalis523000_Act07(ai, goal)
   else
      KingIzalis523000_Act40(ai, goal)
   end
end

KingIzalis523000_Act01 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3000, TARGET_ENE_0, DIST_None, 0)
end

KingIzalis523000_Act02 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3001, TARGET_ENE_0, DIST_None, 0)
end

KingIzalis523000_Act03 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3002, TARGET_ENE_0, DIST_None, 0)
end

KingIzalis523000_Act04 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3003, TARGET_ENE_0, DIST_None, 0)
end

KingIzalis523000_Act05 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
   ai:SetTimer(0, 6)
end

KingIzalis523000_Act06 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3005, TARGET_ENE_0, DIST_None, 0)
   ai:SetTimer(0, 6)
end

KingIzalis523000_Act07 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3006, TARGET_ENE_0, DIST_None, 0)
   ai:SetTimer(0, 6)
end

KingIzalis523000_Act40 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(1, 3), TARGET_NONE, 0, 0, 0)
end

KingIzalis523000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

KingIzalis523000Battle_Terminate = function(ai, goal)
end

KingIzalis523000Battle_Interupt = function(ai, goal)
   return false
end


