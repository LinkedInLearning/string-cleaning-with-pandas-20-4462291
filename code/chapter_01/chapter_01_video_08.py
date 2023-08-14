#################################
###     Creating New Columns  ###
###        From Text          ###
#################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# Just to remind you of how we created the 
# moving_split column in the last video!

aliens['moving_split'] = aliens['Means of Ambulation'].str.split(
  ','
)

# Now, we can use list comprehension to create 
# new variables from the moving_split column.

# Since every alien has a primary means of
# ambulation, we can just take the first item
# from the moving_split list.
aliens['primary_ambulation'] = [
    x[0] for x in aliens['moving_split']
]

# However, not every alien has a secondary
# means of ambulation, so we need to check
# the length of the list before we take the
# second item.
aliens['secondary_ambulation'] = [
    x[1] if len(x) == 2 else "" for x in aliens['moving_split']
]
