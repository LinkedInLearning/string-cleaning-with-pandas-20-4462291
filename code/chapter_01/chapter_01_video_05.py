###########################
### Extracting Patterns ###
###########################

import pandas as pd

# Sadly, extract is not supported by the pyarrow backend yet!

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow'
    )

aliens['degree_type'] = aliens['Bio'].str.extract(
  '(doctorate|masters)'
)

aliens[aliens['degree_type'].isna() == False].head(2)
