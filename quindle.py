import pandas as pd
import quandl as q

q.ApiConfig.api_key = "B-7xYsZDVqAfue83x_Fm"
msft_data = q.get("XNSE/BAJAJ_AUTO",authtoken="B-7xYsZDVqAfue83x_Fm")
msft_data.head()
print(msft_data)
