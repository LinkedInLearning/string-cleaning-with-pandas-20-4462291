#################################
### Using the pyarrow backend ###
#################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# For the following chapters, we are going
# to be using the following functions:
# replace()
# contains()
# extract()
# split()
# count()