#########################
### Matching Patterns ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# The pattern that we are going to match is
# pretty simple -- we are just looking for
# the phrase "world domination" in the Bio column.
# We could also use any regular expression pattern
# within contains.

aliens[aliens['Bio'].str.contains(
  'world domination', 
  regex=True
)]
