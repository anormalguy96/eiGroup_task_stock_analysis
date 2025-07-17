from pathlib import Path
import pandas as pd

from .loader import Dataloader
from .indicators import Indicator


class StockAnalysis:

    def __init__(self,
                 ticker: str,
                 csv_folder: str = '.',
                 date_col: str = 'Date',
                 index_col: str = 'Date'):

        self.ticker = ticker
        self.csv_folder = Path(csv_folder)
        self.filename_raw = self.csv_folder / f'{self.ticker}_raw.csv'
        self.df: pd.DataFrame = pd.DataFrame()
        self.date_col = date_col
        self.index_col = index_col

    def load_data(self) -> pd.DataFrame:

        loader = Dataloader(
            filepath=str(self.filename_raw),
            index_col=self.index_col,
            parse_dates=True
        )
        self.df = loader.load()
        return self.df

    def compute_all_indicators(self,
                               ma_window: int = 30,
                               ema_span: int = 14,
                               rsi_window: int = 14,
                               macd_fast: int = 12,
                               macd_slow: int = 26,
                               macd_signal: int = 9,
                               atr_window: int = 14,
                               bb_window: int = 20,
                               bb_std: int = 2) -> pd.DataFrame:

        df = self.df.copy()


        df[f'MA_{ma_window}'] = Indicator.moving_average(df, window=ma_window)
        df[f'EMA_{ema_span}'] = Indicator.exponential_moving_average(df, span=ema_span)


        df[f'RSI_{rsi_window}'] = Indicator.rsi(df, window=rsi_window)


        macd_df = Indicator.macd(df,
                                           fast_span=macd_fast,
                                           slow_span=macd_slow,
                                           signal_span=macd_signal)
        df = pd.concat([df, macd_df], axis=1)


        df[f'ATR_{atr_window}'] = Indicator.atr(df, window=atr_window)


        bb_df = Indicator.bollinger_bands(df,
                                                    window=bb_window,
                                                    num_std=bb_std)
        df = pd.concat([df, bb_df], axis=1)

        self.df = df
        return self.df

    def export(self,
               outpath: str = None,
               include_index: bool = True) -> None:

        if outpath is None:
            outpath = str(self.csv_folder / f'{self.ticker}_processed.csv')
        loader = Dataloader(filepath=outpath,
                            index_col=None,
                            parse_dates=False)
        loader.save(self.df, outpath=outpath, include_index=include_index)
