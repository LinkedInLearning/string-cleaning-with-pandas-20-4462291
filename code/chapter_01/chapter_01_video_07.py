#########################
### Splitting Strings ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# The split function is a little different, 
# because it returns a list of strings. By
# default, it splits on whitespace, but we
# want to specify that it is splitting on 
# a comma instead. 

aliens['moving_split'] = aliens['Means of Ambulation'].str.split(
  ','
)

aliens['moving_split'].dtype
