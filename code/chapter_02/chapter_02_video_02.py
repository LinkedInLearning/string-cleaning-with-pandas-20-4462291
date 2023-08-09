#########################
### Using Quantifiers ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    )

aliens['art_talent'] = aliens['Bio'].str.extract(
    '(art of \w+\s?-?\w+\s\w+)', 
    expand=False
)

# Since str.extract() extracts a capture group,
# instead of just the pattern, you can't really
# use a group within the extract group. The
# pattern above could be condensed to the following:
# 'art of (\w+\s?-?)+'

aliens['art_talent'].value_counts()

