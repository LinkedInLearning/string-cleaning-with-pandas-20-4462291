###################################
### Removing Special Characters ###
###################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

aliens['Salary (USD)'].loc[130]

aliens['Salary (USD)'].replace(
  '\$|,',
  '', 
  regex=True
).loc[130]