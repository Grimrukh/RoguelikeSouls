REGISTER_GOAL(GOAL_ArmoredTask_BackGuard346100_Battle, "ArmoredTask_BackGuard346100Battle")
REGISTER_GOAL_NO_UPDATE(GOAL_ArmoredTask_BackGuard346100_Battle, 1)

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 2
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 10
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 1.4
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 1.6
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 1.6
local localScriptConfigVar10 = 0
local localScriptConfigVar11 = 1.1
local localScriptConfigVar12 = 0
local localScriptConfigVar13 = 3.5
local localScriptConfigVar14 = 0
local localScriptConfigVar15 = 8
local localScriptConfigVar16 = 2.5
local localScriptConfigVar17 = 4
ArmoredTask_BackGuard346100Battle_Activate = function(ai, goal)
   local distanceToEnemy = ai:GetDist(TARGET_ENE_0)
   local func1_var3 = ai:GetRandam_Int(120, 180)
   local func1_var4 = ai:GetEventRequest(0)
   local func1_var5 = ai:GetRandam_Int(1, 100)
   local func1_var6 = ai:GetRandam_Int(1, 100)
   local func1_var7 = ai:GetRandam_Int(1, 100)
   local func1_var8 = ai:GetRandam_Int(1, 100)
   local chargeRequest = ai:GetEventRequest(0)
   local func1_var9 = 0
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = 0
   local func1_var16 = 0
   local func1_var17 = 0
   local fadeChargeOdds = 0

   if chargeRequest == 1 then
      fadeChargeOdds = 100
   elseif ai:IsFinishTimer(0) == true and distanceToEnemy >= 12 then
      ai:SetTimer(0, func1_var3)
      func1_var13 = 100
   elseif distanceToEnemy <= 1.1 and func1_var5 <= 80 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 45) then
      func1_var16 = 100
   elseif distanceToEnemy <= 2 and func1_var5 <= 80 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 90) then
      func1_var14 = 100
   elseif distanceToEnemy <= 2 and func1_var5 <= 80 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 90) then
      func1_var15 = 100
   elseif distanceToEnemy >= 12 then
      func1_var10 = 25
      func1_var11 = 55
      func1_var12 = 20
      func1_var17 = 0
   elseif distanceToEnemy >= 4 then
      func1_var10 = 40
      func1_var11 = 35
      func1_var12 = 20
      func1_var17 = 5
   else
      func1_var10 = 35
      func1_var11 = 10
      func1_var12 = 35
      func1_var17 = 20
   end
   local func1_var20 = ai:GetRandam_Int(1, func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 +
           func1_var15 + func1_var16 + func1_var17 + fadeChargeOdds)
   if func1_var20 <= func1_var10 then
      if distanceToEnemy >= 6 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, localScriptConfigVar17, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3009, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      elseif distanceToEnemy >= 4.5 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, localScriptConfigVar16, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3009, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, true, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, -1)
      end
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 100
   elseif func1_var20 <= func1_var10 + func1_var11 then
      if distanceToEnemy >= 10 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, localScriptConfigVar15, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, true, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3001, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      end
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 0
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 then
      local func1_var21 = localScriptConfigVar5
      local func1_var22 = localScriptConfigVar5 + 2
      local func1_var23 = 0
      BusyApproach_Act(ai, goal, func1_var21, func1_var22, func1_var23)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Middle, 1, 20)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 100
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3003, TARGET_ENE_0, DIST_None)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, localScriptConfigVar15, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 0
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      func1_var9 = 100
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      func1_var9 = 100
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
      func1_var9 = 0
   elseif func1_var20 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16 + func1_var17 then
      local func1_var21 = localScriptConfigVar13
      local func1_var22 = localScriptConfigVar13 + 2
      local func1_var23 = 0
      BusyApproach_Act(ai, goal, func1_var21, func1_var22, func1_var23)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 1.5, 10)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 100
   else
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3103, TARGET_ENE_0, DIST_None)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, localScriptConfigVar15, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 1.5, 30)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_NONE, 0, 0, 0)
      func1_var9 = 0
   end
   goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_SELF)
   goal:AddSubGoal(GOAL_COMMON_Turn, 2, TARGET_ENE_0, 0, 0, 0)
   local func1_var21 = ai:GetRandam_Int(1, 100)
   if func1_var21 <= func1_var9 then
      ArmoredTask_BackGuard346100_ActAfter_AdjustSpace(ai, goal)
   end
end

ArmoredTask_BackGuard346100_ActAfter_AdjustSpace = function(ai, goal)
   local func2_var2 = ai:GetRandam_Int(1, 100)
   if func2_var2 <= 80 then
   else
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 3)
   end
end

ArmoredTask_BackGuard346100Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

ArmoredTask_BackGuard346100Battle_Terminate = function(ai, goal)
end

ArmoredTask_BackGuard346100Battle_Interupt = function(ai, goal)
   return false
end


