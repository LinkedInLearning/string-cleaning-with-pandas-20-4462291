######################################
### Chaining pandas String Methods ###
######################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

(aliens['Bio'].str.replace('\\bis\\b', 'was', regex=True)
  .str.replace('\\bdoes\\b', 'did', regex=True)
)

(aliens[aliens['Bio']
  .str.contains(
  '\\b[Nn][Oo]\\b', regex=True
)]['Bio']
  .str.replace('No', '', regex=True)
)