######################################
### Chaining pandas String Methods ###
######################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# Nothing you haven't seen here
# before, but we are just going
# to chain the string methods
# together. 

(aliens['Bio'].str.replace('\\bis\\b', 'was', regex=True)
  .str.replace('\\bdoes\\b', 'did', regex=True)
)

(aliens[aliens['Bio']
  .str.contains(
  '\\b[Nn][Oo]\\b', regex=True
)]['Bio']
  .str.replace('No', '', regex=True)
)