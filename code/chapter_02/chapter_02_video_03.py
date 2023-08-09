###########################
### Reordering Strings  ###
### With Backreferences ###
###########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens['Bio'].str.replace(
  '([a-z])([A-Z])', 
  '\\1 \\2', 
  regex = True
)

aliens['Favorite Earth Book'].str.replace(
  '(.*) by (.*)', 
  '\\1: \\2', 
  regex = True
)