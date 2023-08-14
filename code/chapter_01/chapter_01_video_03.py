###################################
### Removing Special Characters ###
###################################

import pandas as pd

aliens = pd.read_csv(
    'data/cosmic_data.csv', 
    engine='pyarrow', 
    dtype_backend='pyarrow'
)

# Any reserved/special regex character needs to
# be escaped with a backslash to be taken literally. 
# The following are the reserved/special regex characters:
# . : is a wildcard character 
# ^ : matches the beginning of a string
# $ : matches the end of a string
# * : matches zero or more repetitions
# + : matches one or more repetitions
# ? : matches zero or one repetitions
# { } : matches an explicitly specified number of repetitions
# [ ] : matches any characters inside the brackets
# \ : escapes special characters
# | : is an OR operator
# ( ) : groups characters together

# You could take them all out with a set, 
# but it's better to explore your data
# and only remove what you need.

aliens['Salary (USD)'].replace(
  '\$|,',
  '', 
  regex=True
)

