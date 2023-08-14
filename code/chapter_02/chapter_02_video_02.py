#########################
### Using Quantifiers ###
#########################

import pandas as pd

# Since we are dealing with extract, 
# we can't use pyarrow data types.

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
)

# The pattern below is a pretty fun one!
# We need to find a lot of different phrases,
# like:
# art of painting
# art of stone-throwing
# art of anti-gravity fun

# To capture those, we need to be flexible
# with our pattern. We can use the actual
# words "art of", but what follows is cool.
# We are using a word character (\w) followed
# by a plus sign (*) -- effectively giving
# us a word character zero or more times. 
# Next we have a space (\s), followed by a
# question mark (?) -- meaning there
# can be zero or one spaces. We'll
# repeat that pattern for a another
# word character zero or more times (\w*),
# followed by a space (\s), followed by
#  another word character zero or more times.

aliens['art_talent'] = aliens['Bio'].str.extract(
    '(art of \w*\s?-?\w*\s?\w*)', 
    expand=False
)

aliens['art_talent'].unique()

# Since str.extract() extracts a capture group,
# instead of just the pattern, you can't really
# use a group within the extract group. The
# pattern above could be condensed 
# to something like the following:
# 'art of (\w+\s?-?)+'