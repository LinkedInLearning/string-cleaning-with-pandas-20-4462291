###############################
###     Extracting Strings  ###
###     With Lookarounds    ###
###############################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow'
)

# Without doubt the look arounds 
# are what I use the most! They
# do, however, take some time to
# commit to memory.

# The look ahead is noted as:
# (?=pattern). We are going to 
# find the word "by and look
# ahead to see a pattern that 
# matches anything (.*).
aliens['book_only'] = aliens['Favorite Earth Book'].str.extract(
  '(.*(?=\\bby))'
)

# The look behind syntax is:
# (?<=pattern). We are going to
# find the word "by" and look
# behind to see a pattern that
# matches anything (.*).
aliens['book_only'] = aliens['Favorite Earth Book'].str.extract(
  '((?<=\\bby ).*)'
)