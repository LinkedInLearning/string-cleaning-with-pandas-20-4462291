######################################
### Finding and Replacing Patterns ###
######################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# The replace function is pretty simple --
# we are just looking for a pattern that
# is a word boundary -- \\b -- followed 
# by the word "by" and then anything else
# that follows. We are replacing that with
# an empty string, which will remove it.
aliens['Favorite Earth Book'].str.replace(
  '\\bby.*',
  '', 
  regex=True
)

# Sometimes, you'll find yourself needing
# to replace a pattern with something from
# another column on the same row. You can
# do this by using a replace() within a
# list comprehension. With the amount
# of data we are working with, this can
# take a few seconds to run!
aliens['redacted_bio'] = [
    aliens['Bio'][x].replace(
        aliens['Name'][x], 'REDACTED'
        ) for x in range(0, len(aliens))
    ]
