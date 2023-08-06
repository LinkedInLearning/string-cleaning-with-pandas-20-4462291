import pandas as pd
import pyarrow as pa
import re
import timeit

small_aliens_numpy = pd.read_csv('small_cosmic.csv')

small_aliens = pd.read_csv('small_cosmic.csv', engine='pyarrow', dtype_backend="pyarrow")

aliens_numpy = pd.read_csv("cosmic_data.csv")

aliens = pd.read_csv("cosmic_data.csv", engine='pyarrow', dtype_backend="pyarrow")
