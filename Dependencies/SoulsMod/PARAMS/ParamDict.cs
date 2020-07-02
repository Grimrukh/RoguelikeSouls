using SoulsFormats;
using System;
using System.Collections.Generic;
using System.Linq;

namespace SoulsFormatsMod.PARAMS
{
    public class ParamDict<T> : Dictionary<long, T> where T : RowWrapper, new()
    {
        private string ParamName { get; }
        private GameParamHandler AllParams { get; }
        private TextHandler Text { get; }
        private PARAM Param => AllParams[ParamName];
        
        public ParamDict(string name, GameParamHandler gParam, TextHandler text) : base()
        {
            ParamName = name;
            AllParams = gParam;
            Text = text;
            foreach (PARAM.Row row in Param.Rows)
            {
                // Add existing Row instances to ParamDict. Writes warnings if the same ID is encountered twice.
                if (ContainsKey(row.ID))
                    Console.WriteLine($"WARNING: Key {row.ID} occurred multiple times in Param {ParamName}. Only first entry kept.");
                else
                    base[row.ID] = (T)Activator.CreateInstance(typeof(T), row, AllParams, Text);
            }
        }

        private T AddRow(PARAM.Row row)
        {
            // Add Row instance to this Param AND add its RowWrapper to this ParamDict.
            Param.Rows.Add(row);
            base[row.ID] = (T)Activator.CreateInstance(typeof(T), row, AllParams, Text);
            return this[row.ID];
        }

        public T AddRow(long newId, params dynamic[] args)
        {
            // Add a row with all default values, plus any additional (field, value) pairs passed in.
            // If `newId == -1`, it will use the highest-numbered ID plus one.
            if (ContainsKey(newId))
                throw new ArgumentException($"ParamDict {ParamName} already contains entry with ID {newId}. Delete it first or just modify it.");

            if (newId == -1)
                newId = Param.Rows.Max(p => p.ID) + 1;

            PARAM.Row row = new PARAM.Row(newId, ParamName, Param.AppliedParamdef);
            ApplyArgsToRow(row, args);
            row.Name = row.Name ?? $"Row {newId}";
            return AddRow(row);
        }

        public T CopyRow(long sourceId, long newId, params dynamic[] args)
        {
            T newRow = AddRow(newId);
            PARAM.Row sourceRow = Param.Rows.First(row => row.ID == sourceId);
            // Copy all values from source row (except name).
            foreach (var cell in newRow.Row.Cells)
                cell.Value = sourceRow[cell.Def.InternalName].Value;
            // Override with any arguments passed in.
            ApplyArgsToRow(newRow, args);
            return newRow;
        }

        public T CopyRow(T otherRow, long newId, params dynamic[] args)
        {
            T newRow = AddRow(newId);
            // Copy all values from source row (except name).
            foreach (var cell in newRow.Row.Cells)
                cell.Value = otherRow.Row[cell.Def.InternalName].Value;
            // Override with any arguments passed in.
            ApplyArgsToRow(newRow, args);
            return newRow;
        }

        public void SortRows()
        {
            // Sort all rows in GameParam.
            Param.Rows.Sort((x, y) => x.ID.CompareTo(y.ID));
        }

        private static void ApplyArgsToRow(PARAM.Row row, dynamic[] args)
        {
            for (int i = 0; i < args.Length; i += 2)
            {
                dynamic field = args[i];
                dynamic val = args[i + 1];
                if (field.ToLower() == "name")
                    row.Name = val;
                else 
                    row[field].Value = val;
            }
        }

        private static void ApplyArgsToRow(RowWrapper row, dynamic[] args)
        {
            ApplyArgsToRow(row.Row, args);
        }
        
        public void ChangeRowID(long oldId, long newId)
        {
            if (!ContainsKey(oldId))
                throw new ArgumentException($"No ID {oldId} in {ParamName} to change.");
            if (ContainsKey(newId))
                throw new ArgumentException($"Cannot change ID {oldId} in {ParamName} to existing ID {newId}.");
            T row = this[oldId];
            row.Row.ID = newId;
            this[newId] = row;
            Remove(oldId);
        }

        public void DeleteRow(long id)
        {
            Param.Rows.RemoveAll(r => r.ID == id);
            Remove(id);
        }

        public void DeleteRowRange(long firstId, long lastId)
        {
            Param.Rows.RemoveAll(row => firstId <= row.ID && row.ID < lastId);
            for (long i = firstId; i < lastId; i++)
                Remove(i);
        }

        public void DeleteRowWhereID(Func<long, bool> condition)
        {
            // Remove all Param rows whose ID evalutes to true in the given condition.
            Param.Rows.RemoveAll(row => condition(row.ID));
            foreach (long key in Keys.Where(id => condition(id)).ToList())
                Remove(key);
        }
    }
}
