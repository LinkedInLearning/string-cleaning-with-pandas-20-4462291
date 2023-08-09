#########################
### Splitting Strings ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens['moving_split'] = aliens['Means of Ambulation'].str.split(
  ','
)

aliens['moving_split'].dtype
