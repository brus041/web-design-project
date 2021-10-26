import pandas as pd 

data = pd.read_csv('Resources/cities.csv')
df = pd.DataFrame(data).to_html("Resources/table.html")

