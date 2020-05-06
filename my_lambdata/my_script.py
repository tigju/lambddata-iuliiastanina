import pandas as pd
#from my_func import enlarge
from my_lambdata import my_func
# print('Hello')

# df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
# print(df)

# y = int(input("Please enter number : "))

# print(enlarge(y))

df = pd.DataFrame({'a': [2, 4, None, None], 'b': [4, None, 4, 5], 'c': ['Cat', 'Dog', 'bird', 'fish'], 'd': [3,4,5,6], 'e':[10,56,89,67]})

# print(check_null(df))

train, val, test = my_func.train_val_test_split(df)
print(train.shape)
print(val.shape)
print(test.shape)
