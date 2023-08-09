#################################
### Using Boundaries and Sets ###
#################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens[aliens['Bio'].str.contains(
  '\\b[Nn][Oo]\\b', regex=True
)]