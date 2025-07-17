# eiGroup Stock Analysis Task

The goal of this task is to write a Python script which:
- Reads a raw `.csv` file for a selected company,
- Calculates the 30 day MA + 14 day EMA for stock closing prices,
- Writes the processed data to a new `.csv` file.

Three companies are considered:
- Palantir (`PLTR_raw.csv`)
- Nvidia (`NVDA_raw.csv`)
- PayPal (`PYPL_raw.csv`)

## Essential Files

### `task.py` — Core Script

This Python script performs the following for each company:

1. Loads the raw stock data from `/data/*.csv`,
2. Computes:
   - `MA_30`: 30-day **Moving Average** of `Close` price,
   - `EMA_14`: 14-day **Exponential Moving Average** of `Close` price,
3. Saves the resulting DataFrame to `/data/processed/*.csv`.

### `data_processing.ipynb` — Jupyter Notebook (Optional Demo)

This notebook provides a step-by-step breakdown of how the script works using only **Palantir** data as an example. It visually demonstrates how the `MA_30` and `EMA_14` columns are computed and stored.


### `__init__.py`

This file is intentionally left blank to indicate that the `eiGroup_task_stock_analysis/` directory is a Python package.

### `task.txt`

This file contains a textual copy of the original task instructions for future reference.


## What is going to happen:

Upon successful execution, the [Optional](Optional/) folder will contain:
- `PLTR_processed.csv`
- `NVDA_processed.csv`
- `PYPL_processed.csv`

Each of these files contains:
- Original data,
- `MA_30` column (30-day Moving Average),
- `EMA_14` column (14-day Exponential Moving Average).
