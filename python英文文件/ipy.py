#import pandas as pd
#from matplotlib import pyplot as plt
#from sklearn import linear_model
#from sklearn.metrics import mean_squared_error
#raw_data= pd.read_csv('data.txt')
import requests
url= 'http://www.dataivy.cn/blog/dbscan/'
res= requests.get(url)
html= res.text
print(html)