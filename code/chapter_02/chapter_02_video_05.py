###############################
###     Extracting Strings  ###
###     With Lookarounds    ###
###############################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )

# Look ahead
aliens['book_only'] = aliens['Favorite Earth Book'].str.extract(
  '(.*(?=by))'
)

# Look behind
aliens['book_only'] = aliens['Favorite Earth Book'].str.extract(
  '((?<=by ).*)'
)