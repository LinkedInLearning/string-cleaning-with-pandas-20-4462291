###########################
### Extracting Patterns ###
###########################

import pandas as pd

# Sadly, extract is not supported by the 
# pyarrow backend yet! Keep an eye out 
# for it, though, because it will be
# very helpful when it is ready!
# For now, we will use the pandas backend.

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow'
)

# The following pattern will extract the words
# doctorate or masters from the Bio column. 
# The parentheses are used to group the words
# for extraction.

aliens['degree_type'] = aliens['Bio'].str.extract(
  '(doctorate|masters)'
)

# Let's see who we found!

aliens[aliens['degree_type'].isna() == False].head(2)
