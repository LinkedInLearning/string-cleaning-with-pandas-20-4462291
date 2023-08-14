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

# We can come in with a lower score
# by using the \d metacharacter --
# it is the same as [0-9].
aliens['Earth Birthdate'].str.contains(
    '\d{2}\/\d{2}\/\d{4}', 
    regex=True
    )

# We've already seen some other metachaaracters,
# but here is a list of them:
# \d : any digit
# \D : any non-digit
# \w : any alphanumeric character
# \W : any non-alphanumeric character
# \s : any whitespace character
# \S : any non-whitespace character
# \b : any word boundary
# \B : any non-word boundary
