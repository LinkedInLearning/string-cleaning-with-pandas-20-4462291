###################################
### Naming Backreference Groups ###
###################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# We can use the capture groups and
# backreferences, but name them to 
# make them easier to read; it
# might seem more daunting to
# to type, but it will definitely
# be easier to communicate what
# you are trying to do.
# Capture groups are named by
# using the following syntax:
# (?P<name>pattern).
# Whatever is within the tags will
# be the name of the capture group.
# To reference those named groups, 
# you can use \g flag, followed by
# the name of the capture group in 
# tags/angle brackets.

aliens['Favorite Earth Book'].str.replace(
  '(?P<book_title>.*) by (?P<book_author>.*)', 
  '\g<book_author>: \g<book_title>', 
  regex = True
)
