###########################
### Reordering Strings  ###
### With Backreferences ###
###########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# Backreferences are a way to reference
# a capture group within a pattern.
# You can reference a capture group
# by using two backslashes (\\) followed
# by the capture group number. The 
# capture group number is the order
# in which the capture group appears
# in the pattern. The first capture
# group -- any letter in the set of
# [a-z] -- is denoted by \\1. The
# second capture group -- any letter
# in the set of [A-Z] -- is denoted
# by \\2. We will take those backreferences
# and put a space between them.
aliens['Bio'].str.replace(
  '([a-z])([A-Z])', 
  '\\1 \\2', 
  regex=True
)

# You can also use backreferences
# to reorder strings. Let's say
# that you want to change the order
# of the author and title in the
# 'Favorite Earth Book' column.
# We can create a capture group
# for everything that comes before
# the word "by" and another capture
# group for everything that comes
# after the word "by".
aliens['Favorite Earth Book'].str.replace(
  '(.*) \\bby (.*)', 
  '\\2: \\1', 
  regex=True
)