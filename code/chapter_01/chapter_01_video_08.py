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

aliens['moving_split'] = aliens['Means of Ambulation'].str.split(
  ','
)

aliens['primary_ambulation'] = [x[0] for x in aliens['moving_split']]
aliens['secondary_ambulation'] = [x[1] if len(x) == 2 else "" for x in aliens['moving_split']]
