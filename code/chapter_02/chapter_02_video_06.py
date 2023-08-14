#################################
### Using Boundaries and Sets ###
#################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# To be very specific in the content
# that we are going to match, 
# we can use boundaries and sets. 
# If we are looking for any variant
# of the word "no", we can use the
# boundary \\b and the set [Nn][Oo].
# This will find any of the following:
# no, No, nO, NO.
# It will not find a "no" within
# another word, such as "not".

aliens[aliens['Bio'].str.contains(
  '\\b[Nn][Oo]\\b', 
  regex=True
)]

# Just as an FYI, you can negate a set 
# by using the caret (^) within the set.