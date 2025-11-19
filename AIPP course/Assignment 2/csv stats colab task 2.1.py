# csv_stats_colab.py
# Colab-ready function to read a CSV and compute mean/min/max for numeric columns.
# This file can be run locally or its function can be imported into a Colab notebook.

import io
import sys
import subprocess
from typing import List, Optional, Dict, Any, Union

# Ensure pandas is available (Colab already has it, but this is safe for local runs)
try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
    import pandas as pd


def read_csv_compute_stats(
    file: Union[str, io.BytesIO],
    columns: Optional[List[Any]] = None,
    delimiter: str = ",",
    na_values: Optional[List[str]] = None,
    skiprows: int = 0,
    return_dataframe: bool = True,
) -> Union[pd.DataFrame, Dict[str, Dict[str, float]]]:
    """
    Read a CSV and compute mean, min, max for numeric columns.

    Args:
      file: Path to CSV (str) or file-like object (e.g., uploaded file or BytesIO).
      columns: Optional list of column names or 0-based indices to include. If None, all columns considered.
      delimiter: CSV delimiter (default ',').
      na_values: Additional strings to treat as NaN.
      skiprows: Number of rows to skip before the header.
      return_dataframe: If True returns a pandas DataFrame (rows: mean,min,max). If False returns a dict.

    Returns:
      pandas.DataFrame or dict mapping column -> {'mean','min','max'}.

    Raises:
      FileNotFoundError if file path doesn't exist.
      ValueError if no numeric data found in the selected columns.
    """
    # Read csv into DataFrame robustly
    try:
        df = pd.read_csv(file, delimiter=delimiter, na_values=na_values, skiprows=skiprows)
    except FileNotFoundError:
        raise
    except Exception:
        # Fallback: read bytes/text then parse
        if hasattr(file, "read"):
            content = file.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8", errors="replace")
            df = pd.read_csv(io.StringIO(content), delimiter=delimiter, na_values=na_values)
        else:
            with open(file, "r", encoding="utf-8", errors="replace") as f:
                df = pd.read_csv(io.StringIO(f.read()), delimiter=delimiter, na_values=na_values)

    # If columns are indices, map to names
    if columns is not None and all(isinstance(c, int) for c in columns):
        max_idx = len(df.columns) - 1
        cols_by_index = []
        for idx in columns:
            if idx < 0 or idx > max_idx:
                raise ValueError(f"Column index {idx} out of range (0..{max_idx})")
            cols_by_index.append(df.columns[idx])
        columns = cols_by_index

    # Select given columns if provided
    if columns is not None:
        missing = [c for c in columns if c not in df.columns]
        if missing:
            raise ValueError(f"Specified columns missing from CSV: {missing}")
        df = df[columns]

    # Try coercing every column to numeric (non-convertible -> NaN)
    numeric_df = df.apply(pd.to_numeric, errors="coerce")

    # Drop columns that are completely NaN after coercion
    numeric_df = numeric_df.dropna(axis=1, how="all")
    if numeric_df.shape[1] == 0:
        raise ValueError("No numeric data found in the selected columns or file.")

    # Compute stats
    stats = numeric_df.agg(["mean", "min", "max"])

    if return_dataframe:
        return stats
    else:
        out: Dict[str, Dict[str, float]] = {}
        for col in stats.columns:
            out[col] = {
                "mean": float(stats.loc["mean", col]) if pd.notna(stats.loc["mean", col]) else float("nan"),
                "min": float(stats.loc["min", col]) if pd.notna(stats.loc["min", col]) else float("nan"),
                "max": float(stats.loc["max", col]) if pd.notna(stats.loc["max", col]) else float("nan"),
            }
        return out


if __name__ == "__main__":
    # Small demo: create sample CSV and run stats
    sample_csv = """id,value_a,value_b,notes
1,10,100,ok
2,20,200,ok
3,30,300,ok
4,,400,missing a
5,50,invalid,invalid b
"""
    with open("sample.csv", "w", encoding="utf-8") as f:
        f.write(sample_csv)

    print("Wrote sample.csv. Running read_csv_compute_stats on it...\n")
    df_stats = read_csv_compute_stats("sample.csv")
    print(df_stats)

    print("\nAs JSON-friendly dict:\n")
    print(read_csv_compute_stats("sample.csv", return_dataframe=False))
