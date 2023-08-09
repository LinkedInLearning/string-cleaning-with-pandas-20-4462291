#########################
### Matching Patterns ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens[aliens['Bio'].str.contains(
  'world domination', regex=True
)]
