import pandas as pd

log = pd.read_csv(
    'log.csv', 
    header=None
    )
log.describe(include='all')