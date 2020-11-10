using RoguelikeSouls.Extensions;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

namespace RoguelikeSouls.ModProgram
{
    class MapPointManager
    {
        Random Rand { get; }
        List<GamePoint> MapPoints { get; } = new List<GamePoint>();
        const double NearbyRadiusSq = 8.0 * 8.0;
        HashSet<GamePoint> OccupiedPoints { get; } = new HashSet<GamePoint>();

        List<GamePoint> AvailablePoints
        {
            get => new List<GamePoint>(MapPoints.Where(point => !OccupiedPoints.Contains(point)));
        }

        public MapPointManager(string mapPointFileName, Random random)
        {
            Rand = random;
            using (StringReader file = new StringReader(Resources.MapPoints.ResourceManager.GetString(mapPointFileName)))
            {
                string line;
                string regionLabel = "Default";
                while ((line = file.ReadLine()) != null)
                {
                    if (line == "")
                        continue;
                    else if (line.StartsWith("# "))
                        regionLabel = line.Substring(1).Trim(' ');
                    else
                        MapPoints.Add(new GamePoint(line, regionLabel));
                }
            }
            foreach (GamePoint point in MapPoints)
            {
                int count = 0;
                foreach (GamePoint otherPoint in MapPoints)
                {
                    if (point.SquaredDistanceFromPoint(otherPoint) <= NearbyRadiusSq)
                        count++;
                }
                point.NearbyCount = count;
            }
        }

        public GamePoint CheckOutPoint(GamePoint point, string occupantLabel)
        {
            OccupiedPoints.Add(point);
            point.OccupantLabel = occupantLabel;
            return point;
        }

        public GamePoint CheckOutRandomPoint(string occupantLabel, int minNearbyCount = 0, string regionLabel = "")
        {
            // Returns a random unoccupied point with at least the given `minNearbyCount` and checks it out (marks it as occupied).
            List<GamePoint> available = new List<GamePoint>(MapPoints.Where(
                point => !OccupiedPoints.Contains(point) && point.NearbyCount >= minNearbyCount && (regionLabel == "" || point.RegionLabel == regionLabel)));
            GamePoint chosen = available.GetRandomElement(Rand);
            return CheckOutPoint(chosen, occupantLabel);
        }

        public GamePoint CheckOutRandomPointWeightedInverseNearby(string occupantLabel, int minNearbyCount = 0, string regionLabel = "")
        {
            // Returns a random unoccupied point, weighted by the inverse of NearbyCount (subtraction from max + 1).
            List<GamePoint> available = new List<GamePoint>(MapPoints.Where(
                point => !OccupiedPoints.Contains(point) && point.NearbyCount >= minNearbyCount && (regionLabel == "" || point.RegionLabel == regionLabel)));
            int maxNearbyCount = available.Max(p => p.NearbyCount) + 1;
            Dictionary<GamePoint, int> weightedOptions = available.ToDictionary(p => p, p => maxNearbyCount - p.NearbyCount);
            GamePoint chosen = weightedOptions.GetWeightedRandomElement(Rand);
            return CheckOutPoint(chosen, occupantLabel);
        }

        public GamePoint CheckOutRandomPointCustomNearbyRadius(string occupantLabel, double nearbyRadius, int minNearbyCount, string regionLabel = "")
        {
            // Returns a random unoccupied point with at least the given `minNearbyCount` and checks it out (marks it as occupied).
            List<GamePoint> available = new List<GamePoint>(MapPoints.Where(
                point => !OccupiedPoints.Contains(point) && GetNearbyCount(point, nearbyRadius) >= minNearbyCount && (regionLabel == "" || point.RegionLabel == regionLabel)));
            GamePoint chosen = available.GetRandomElement(Rand);
            return CheckOutPoint(chosen, occupantLabel);
        }

        public GamePoint CheckOutRandomPointWithinDistance(string occupantLabel, GamePoint originPoint, double minDistanceSq = -1.0, double maxDistanceSq = -1.0)
        {
            // Returns a random unoccupied point between `minDistance` (if not -1) and `maxDistance` (if not -1) of `originPoint`.
            List<GamePoint> available = new List<GamePoint>(MapPoints.Where(
                point => !OccupiedPoints.Contains(point) && ValidPointDistance(originPoint, point, minDistanceSq, maxDistanceSq)));
            GamePoint chosen = available.GetRandomElement(Rand);
            return CheckOutPoint(chosen, occupantLabel);
        }

        public float GetAngleFacingNearestPoint(GamePoint point)
        {
            List<GamePoint> available = AvailablePoints;
            GamePoint nearestPoint = available[available.IndexOfMinBy(p => p.SquaredDistanceFromPoint(point))];
            return GetFacingPoint(point, nearestPoint);
        }

        static public float GetFacingPoint(GamePoint origin, GamePoint target)
        {
            Vector3 delta = target.Position - origin.Position;
            return (float)Math.Atan2(-delta.Z, -delta.X);  // note reversal and negation
        }

        public int GetNearbyCount(GamePoint point, double radius)
        {
            double radiusSq = radius * radius;
            int count = 0;
            foreach (GamePoint otherPoint in MapPoints)
            {
                if (point.SquaredDistanceFromPoint(otherPoint) <= radiusSq)
                    count++;
            }
            return count;
        }

        public GamePoint GetClosestPoint(float x, float y, float z, double maxDistance = 3.0, bool excludeEqual = false)
        {
            Vector3 target = new Vector3(x, y, z);
            double sqMaxDistance = maxDistance * maxDistance;
            float sqShortestDistance = -1.0f;
            GamePoint closestPoint = null;
            foreach (GamePoint point in MapPoints)
            {
                if (excludeEqual && point.Position == target)
                    continue;
                Vector3 delta = point.Position - target;
                delta *= delta;
                float sqDistance = delta.X + delta.Y + delta.Z; 
                if (sqDistance < sqMaxDistance)
                {
                    if (sqShortestDistance == -1.0f || sqDistance < sqShortestDistance)
                    {
                        closestPoint = point;
                        sqShortestDistance = sqDistance;
                    }
                }
            }
            return closestPoint;  // could be null
        }

        public GamePoint GetClosestPoint(Vector3 position, double maxDistance = 3.0, bool excludeEqual = false)
        {
            return GetClosestPoint(position.X, position.Y, position.Z, maxDistance, excludeEqual);
        }

        bool ValidPointDistance(GamePoint point1, GamePoint point2, double minDistanceSq = -1.0, double maxDistanceSq = -1.0)
        {
            if (minDistanceSq == -1.0 && maxDistanceSq == -1.0)
                return true;
            float sqDistance = point1.SquaredDistanceFromPoint(point2);
            return (minDistanceSq == -1.0 || minDistanceSq <= sqDistance) && (maxDistanceSq == -1.0 || sqDistance < maxDistanceSq);
        }
    }
}
