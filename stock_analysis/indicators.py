import pandas as pd


class Indicator:

    @staticmethod
    def moving_average(df: pd.DataFrame,
                       column: str = 'Close',
                       window: int = 30) -> pd.Series:
        return df[column].rolling(window).mean()

    @staticmethod
    def exponential_moving_average(df: pd.DataFrame,
                                   column: str = 'Close',
                                   span: int = 14,
                                   adjust: bool = False) -> pd.Series:
        return df[column].ewm(span=span, adjust=adjust).mean()

    @staticmethod
    def rsi(df: pd.DataFrame,
            column: str = 'Close',
            window: int = 14) -> pd.Series:
        delta = df[column].diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)
        avg_gain = gain.rolling(window).mean()
        avg_loss = loss.rolling(window).mean()
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def macd(df: pd.DataFrame,
             column: str = 'Close',
             fast_span: int = 12,
             slow_span: int = 26,
             signal_span: int = 9) -> pd.DataFrame:
        ema_fast = df[column].ewm(span=fast_span, adjust=False).mean()
        ema_slow = df[column].ewm(span=slow_span, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal_span, adjust=False).mean()
        return pd.DataFrame({
            'MACD': macd_line,
            'MACD_Signal': signal_line
        }, index=df.index)

    @staticmethod
    def atr(df: pd.DataFrame,
            high: str = 'High',
            low: str = 'Low',
            close: str = 'Close',
            window: int = 14) -> pd.Series:
        high_low = df[high] - df[low]
        high_close = (df[high] - df[close].shift()).abs()
        low_close = (df[low] - df[close].shift()).abs()
        true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        return true_range.rolling(window).mean()

    @staticmethod
    def bollinger_bands(df: pd.DataFrame,
                        column: str = 'Close',
                        window: int = 20,
                        num_std: int = 2) -> pd.DataFrame:
        sma = df[column].rolling(window).mean()
        std = df[column].rolling(window).std()
        upper = sma + (std * num_std)
        lower = sma - (std * num_std)
        return pd.DataFrame({
            'BB_Middle': sma,
            'BB_Upper': upper,
            'BB_Lower': lower
        }, index=df.index)
