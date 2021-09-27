import pandas as pd
import numpy as np 

fp = np.random.randn(100)

# assume df has 100 rows
df.loc[:, 'new_col'] = pd.Series(fp, index=df.index)
