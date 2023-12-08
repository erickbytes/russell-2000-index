import pandas as pd

url = "https://bullishbears.com/russell-2000-stocks-list/"
russell_index = pd.read_html(url)[0]
print(russell_index.shape)
