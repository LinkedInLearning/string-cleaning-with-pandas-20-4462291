######################################
### Finding and Replacing Patterns ###
######################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens['Favorite Earth Book'].str.replace(
  '\\bby.*',
  '', 
  regex=True
)

aliens['redacted_bio'] = [aliens['Bio'][x].replace(aliens['Name'][x], 'REDACTED') for x in range(0, len(aliens))]