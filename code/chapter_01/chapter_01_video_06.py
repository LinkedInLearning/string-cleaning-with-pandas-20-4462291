########################
### Counting Strings ###
########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# Again, a pretty simple pattern -- 
# we are just looking for the word "art"
# within the Bio column. You'll notice that
# we are using the count function to make
# a new column called art_count.

aliens['art_count'] = aliens['Bio'].str.count(
  'art'
)