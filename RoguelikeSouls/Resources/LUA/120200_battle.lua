REGISTER_GOAL(GOAL_BigInunezumi120200_Battle, "BigInunezumi120200Battle")
REGISTER_GOAL_NO_UPDATE(GOAL_BigInunezumi120200_Battle, 1)

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 2.1
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 1.6
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 1.7
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 1.6
local localScriptConfigVar8 = 2
local localScriptConfigVar9 = 3.5
local localScriptConfigVar10 = 2
local localScriptConfigVar11 = 3.5
local localScriptConfigVar12 = 5
local localScriptConfigVar13 = 7.3
BigInunezumi120200Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENEMY)
   local func1_var3 = ai:GetRandam_Int(1, 100)
   local func1_var4 = ai:GetRandam_Int(1, 100)
   local func1_var5 = ai:GetRandam_Int(1, 100)
   local func1_var6 = 0
   local func1_var7 = 0
   local func1_var8 = 0
   local func1_var9 = 0
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = ai:GetDistAtoB(POINT_EVENT, TARGET_SELF)
   func1_var11 = 100
   local func1_var16 = ai:GetExcelParam(AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer)
   local func1_var17 = ai:GetTeamOrder(ORDER_TYPE_Role)
   local func1_var18 = 0
   if func1_var16 == 1 and func1_var17 == ROLE_TYPE_Torimaki then
      Torimaki_Act(ai, goal, func1_var18)
   elseif func1_var16 == 1 and func1_var17 == ROLE_TYPE_Kankyaku then
      Kankyaku_Act(ai, goal, func1_var18)
   else
      local func1_var19 = ai:GetRandam_Int(1, func1_var7 + func1_var8 + func1_var9 + func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14)
      if func1_var19 <= func1_var7 then
         local enemyDistance0 = localScriptConfigVar1
         local enemyDistance1 = localScriptConfigVar1 + 2
         local enemyDistance2 = 0
         Approach_Act(ai, goal, enemyDistance0, enemyDistance1, enemyDistance2)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3000, TARGET_ENEMY, DIST_Middle, -1, 32)
         func1_var6 = 100
      elseif func1_var19 <= func1_var7 + func1_var8 then
         local enemyDistance0 = localScriptConfigVar3
         local enemyDistance1 = localScriptConfigVar3 + 2
         local enemyDistance2 = 0
         Approach_Act(ai, goal, enemyDistance0, enemyDistance1, enemyDistance2)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3001, TARGET_ENEMY, DIST_Middle, -1, 32)
         func1_var6 = 100
      elseif func1_var19 <= func1_var7 + func1_var8 + func1_var9 then
         local enemyDistance0 = localScriptConfigVar5
         local enemyDistance1 = localScriptConfigVar5 + 2
         local enemyDistance2 = 0
         Approach_Act(ai, goal, enemyDistance0, enemyDistance1, enemyDistance2)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3002, TARGET_ENEMY, DIST_Middle, -1, 32)
         func1_var6 = 100
      elseif func1_var19 <= func1_var7 + func1_var8 + func1_var9 + func1_var10 then
         local enemyDistance0 = localScriptConfigVar7
         local enemyDistance1 = localScriptConfigVar7 + 2
         local enemyDistance2 = 0
         Approach_Act(ai, goal, enemyDistance0, enemyDistance1, enemyDistance2)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3003, TARGET_ENEMY, DIST_Middle, -1, 32)
         func1_var6 = 100
      elseif func1_var19 <= func1_var7 + func1_var8 + func1_var9 + func1_var10 + func1_var11 then
         if func1_var19 <= func1_var7 + func1_var8 + func1_var9 + func1_var10 + func1_var11 + func1_var12 then
            local enemyDistance0 = 0
            goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 5, 3004, TARGET_ENEMY, DIST_Middle, 0)
            func1_var6 = 100
         elseif func1_var19 <= func1_var7 + func1_var8 + func1_var9 + func1_var10 + func1_var11 + func1_var12 + func1_var13 then
            local enemyDistance0 = 0
            goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 5, 3005, TARGET_ENEMY, DIST_Middle, 0)
            func1_var6 = 100
         else
            local enemyDistance0 = localScriptConfigVar13
            local enemyDistance1 = localScriptConfigVar13 + 1.5
            local enemyDistance2 = 0
            Approach_Act(ai, goal, enemyDistance0, enemyDistance1, enemyDistance2)
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3006, TARGET_ENEMY, DIST_Middle, -1, 32)
            func1_var6 = 100
         end
      end
   end
   local func1_var19 = ai:GetRandam_Int(1, 100)
   if func1_var19 <= func1_var6 then
      if func1_var4 <= 70 then
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENEMY, 0, AI_DIR_TYPE_B, 5)
      end
   end
end

BigInunezumi120200Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

BigInunezumi120200Battle_Terminate = function(ai, goal)
end

BigInunezumi120200Battle_Interupt = function(ai, goal)
   if ai:IsInterupt(INTERUPT_Inside_ObserveArea) and ai:IsFinishTimer(0) == true then
      ai:SetTimer(0, 2)
      ai:Replaning()
      return true
   end
   return false
end


