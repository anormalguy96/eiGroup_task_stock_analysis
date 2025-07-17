import pandas as pd; from pathlib import Path; from typing import Optional

class Dataloader:


    def __init__(self,
                 filepath: str,
                 index_col: Optional[str] = None,
                 parse_dates: bool = True):  # whether to parse index_col as datetime
        self.filepath = Path(filepath)
        self.index_col = index_col
        self.parse_dates = parse_dates

    
    def load(self) -> pd.DataFrame:

        df = pd.read_csv(
            self.filepath,
            index_col=self.index_col,
            parse_dates=[self.index_col] if (self.index_col and self.parse_dates) else False
        )
        return df

    def save(self,
             df: pd.DataFrame,
             outpath: str,
             include_index: bool = True) -> None:
        
        df.to_csv(outpath, index=include_index)