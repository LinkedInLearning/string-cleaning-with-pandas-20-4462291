#########################
### Using Quantifiers ###
#########################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    )

aliens['art_talent'] = aliens['Bio'].str.extract(
    '(art of (\\w+\\s?-?){1,3})', 
    expand=False
)

aliens['art_talent'].value_counts()

