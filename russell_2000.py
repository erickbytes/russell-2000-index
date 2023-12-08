import pandas as pd

url = "https://www.marketbeat.com/types-of-stock/russell-2000-stocks/"
russell_index = pd.read_html(url)[0]
print(russell_index.shape)
