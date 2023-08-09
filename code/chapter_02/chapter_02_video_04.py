###################################
### Naming Backreference Groups ###
###################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
    )


aliens['Favorite Earth Book'].str.replace(
  '(?P<book_title>.*) by (?P<book_author>.*)', 
  '\g<book_author>: \g<book_title>', 
  regex = True
)
