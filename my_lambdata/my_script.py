import pandas as pd
#from my_func import enlarge
from my_lambdata.my_func import enlarge
print('Hello')

df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
print(df)

y = int(input("Please enter number : "))

print(enlarge(y))