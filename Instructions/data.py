import pandas as pd 

#read the csv file in 
df = pd.read_csv("Resources/cities.csv")

#save to file
df.to_html('data.html', index = False)

#assign to string
table = df.to_html()
print(table)