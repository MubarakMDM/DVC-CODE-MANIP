import numpy as np
import pandas as pd
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
df =df.iloc[:,3:]
df=df['Avg. Session Length'].sample(200)
df.to_csv(os.path.join('data','customer.csv'))