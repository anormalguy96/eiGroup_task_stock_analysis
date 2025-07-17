import pandas as pd

# User inputs
name = "Palantir"
export_to_file = True


tickers = {
    "Palantir": "PLTR",
    "Nvidia": "NVDA",
    "Paypal": "PYPL"
}
df = pd.read_csv(f'./{tickers[name]}_raw.csv')

# MA (30)
df['MA_30'] = df['Close'].rolling(30).mean()

# EMA (14)
df['EMA_14'] = df['Close'].ewm(span=14, adjust=False).mean()

# RSI (14)
delta = df['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
df['RSI_14'] = 100 - (100 / (1 + gain.rolling(14).mean() / loss.rolling(14).mean()))

# MACD (12, 26, 9)
df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
df['EMA_26'] = df['Close'].ewm(span=26, adjust=False).mean()
df['MACD'] = df['EMA_12'] - df['EMA_26']
df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

# ATR (14)
df['High-Low'] = df['High'] - df['Low']
df['High-Close'] = (df['High'] - df['Close'].shift()).abs()
df['Low-Close'] = (df['Low'] - df['Close'].shift()).abs()
df['True Range'] = df[['High-Low', 'High-Close', 'Low-Close']].max(axis=1)
df['ATR_14'] = df['True Range'].rolling(14).mean()

# Bollinger bands (20, 2)
df['SMA_20'] = df['Close'].rolling(20).mean()
df['STD_20'] = df['Close'].rolling(20).std()
df['Upper_BB'] = df['SMA_20'] + (df['STD_20'] * 2)
df['Lower_BB'] = df['SMA_20'] - (df['STD_20'] * 2)

df.drop(columns=['High-Low', 'High-Close', 'Low-Close', 'True Range'], inplace=True)

if export_to_file:
    df.to_csv(f"{tickers[name]}_processed.csv", index=True)