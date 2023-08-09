###############################
### Regular Expression Golf ###
###############################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

aliens['Earth Birthdate'].str.contains(
    '[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]', 
    regex=True
    )

aliens['Earth Birthdate'].str.contains(
    '[0-9]{2}\/[0-9]{2}\/[0-9]{4}', 
    regex=True
    )

aliens['Earth Birthdate'].str.contains(
    '\d{2}\/\d{2}\/\d{4}', 
    regex=True
    )
