import pandas as pd

aliens = pd.read_csv('cosmic_data.csv', engine='pyarrow', dtype_backend='pyarrow')