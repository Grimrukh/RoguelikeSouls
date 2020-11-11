using System;
using System.Collections.Generic;
using System.Text;
using PropertyHook;
using GameHook;
using System.Threading;
using System.Numerics;
using System.Text.RegularExpressions;
using RoguelikeSouls.Installation;

namespace RoguelikeSouls
{
    class MapPointGenerator
    {
        const int DebugCollisionAddress = 0x04454964;  // dynamic, can't be bothered tracking pointers
        static IntPtr DebugCollisionPtr { get; } = new IntPtr(DebugCollisionAddress);
        PHPointer DebugCollisionPointer { get; }
        DSHook DarkSoulsHook { get; }

        const int MappingInterval = 50;  // milliseconds between mapping checks
        const float MinPointDistanceHorizontalSquared = 1.0f;  // 1.0
        const float MinPointDistanceVerticalSquared = 0.25f;  // 0.5

        public MapPointGenerator()
        {
            DarkSoulsHook = new DSHook(5000, 5000);
            DebugCollisionPointer = DarkSoulsHook.CreateBasePointer(DebugCollisionPtr);
        }

        public void StartHook()
        {
            DarkSoulsHook.Start();
        }
        public void StopHook()
        {
            DarkSoulsHook.Stop();
        }

        public void StartMapping(string mapName)
        {
            // Opens a text file and starts streaming "{x} {y} {z} {angle} {collisionName}" entries into it, 
            // depending on distance from existing values.
            
            string timestamp = DateTime.Now.ToString("yyyyMMdd_hhmm");
            List<GamePoint> allPositions = new List<GamePoint>();
            using (System.IO.StreamWriter file = new System.IO.StreamWriter($"{mapName}_{timestamp}.txt"))
            {
                Console.WriteLine("Press ESC to stop");
                do
                {
                    while (!Console.KeyAvailable)
                    {
                        GamePoint point = GetPositionInfo();
                        if (point != null && CheckDistance(point, allPositions))
                        {
                            if (!point.CollisionName.StartsWith("unknown"))
                            {
                                allPositions.Add(point);
                                Console.WriteLine(point);
                                file.WriteLine(point.ToString());
                            }
                            else
                            {
                                Console.WriteLine("UNKNOWN (not written) " + point.ToString());
                            }
                            
                        }
                        Thread.Sleep(MappingInterval);
                    }
                } while (Console.ReadKey(true).Key != ConsoleKey.Escape);
            }
        }

        GamePoint GetPositionInfo()
        {
            if (DarkSoulsHook.Hooked && DarkSoulsHook.Loaded)
            {
                DarkSoulsHook.GetStablePosition(out float x, out float y, out float z, out float angle);
                string debugCollisionName = DebugCollisionPointer.ReadString(0, Encoding.Unicode, 0xA0, true);
                int collisionNameStart = debugCollisionName.IndexOf("[h");
                if (collisionNameStart == -1)
                {
                    debugCollisionName = $"unknown ({debugCollisionName})";
                }
                else
                {
                    debugCollisionName = debugCollisionName.Substring(collisionNameStart + 1);
                    string[] nameParts = debugCollisionName.Split(']');
                    debugCollisionName = (nameParts.Length != 0) ? nameParts[0] : "unknown";
                }
                return new GamePoint(x, y, z, 180.0 * angle / Math.PI, debugCollisionName);
            }
            return null;
        }

        bool CheckDistance(GamePoint newPoint, List<GamePoint> allPoints)
        {
            // Returns true if newPosition is sufficiently far away from other positions in the map.
            if (allPoints.Count == 0) 
                return true;
            foreach (GamePoint point in allPoints)
            {
                Vector3 delta = point.Position - newPoint.Position;
                float horizontalDistanceSq = delta.X * delta.X + delta.Z * delta.Z;
                float verticalDistanceSq = delta.Y * delta.Y;
                if (horizontalDistanceSq < MinPointDistanceHorizontalSquared && verticalDistanceSq < MinPointDistanceVerticalSquared)
                    return false;  // too close to an existing point
            }
            return true;
        }       
    }

    class GamePoint
    {
        const string LinePattern = @"^x = ([\d-.]+), y = ([\d-.]+), z = ([\d-.]+), angle = ([\d-.]+), collision = ([\d\w]+)$";

        public Vector3 Position { get; }
        public float Angle { get; }
        public string CollisionName { get; }
        public string RegionLabel { get; }
        public ArenaSize ArenaSize { get; }
        public int NearbyCount { get; set; }
        public string OccupantLabel { get; set; } = "";

        public GamePoint(float x, float y, float z, double angle, string collisionName, string regionLabel = "Default", ArenaSize arenaSize = ArenaSize.Any)
        {
            Position = new Vector3(x, y, z);
            Angle = (float)angle;
            CollisionName = collisionName;
            RegionLabel = regionLabel;
            ArenaSize = arenaSize;
            NearbyCount = -1;
        }

        public GamePoint(string line, string regionLabel = "Default")
        {
            Regex rg = new Regex(LinePattern);
            Match match = rg.Match(line);
            if (!match.Success)
                throw new ArgumentException($"Could not parse line into GamePosition: {line}");
            Position = new Vector3(
                float.Parse(match.Groups[1].ToString()),
                float.Parse(match.Groups[2].ToString()),
                float.Parse(match.Groups[3].ToString())
                );
            Angle = float.Parse(match.Groups[4].ToString());
            CollisionName = match.Groups[5].ToString();
            RegionLabel = regionLabel;
            ArenaSize = ArenaSize.Any;  // Not read.
        }

        public override string ToString()
        {
            return $"x = {Position.X}, y = {Position.Y}, z = {Position.Z}, angle = {Angle}, collision = {CollisionName}, region = {RegionLabel}";
        }

        public float SquaredDistanceFromPoint(GamePoint otherPoint)
        {
            return SquaredDistanceFromPoint(otherPoint.Position);
        }

        public float SquaredDistanceFromPoint(Vector3 otherPoint)
        {
            Vector3 delta = Position - otherPoint;
            delta *= delta;
            return delta.X + delta.Y + delta.Z;
        }
    }
}
