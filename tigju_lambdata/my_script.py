import pandas as pd
#from my_func import enlarge
from tigju_lambdata import my_func
# print('Hello')

# df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
# print(df)

# y = int(input("Please enter number : "))

# print(enlarge(y))

#df = pd.DataFrame({'a': [2, 4, None, None], 'b': [4, None, 4, 5], 'c': ['Cat', 'Dog', 'bird', 'fish'], 'd': [3,4,5,6], 'e':[10,56,89,67]})

# print(check_null(df))

# train, val, test = my_func.train_val_test_split(df)
# print(train.shape)
# print(val.shape)
# print(test.shape)
# y_true = pd.DataFrame({"column": ['cat', 'dog', 'cat', 'cat', 'dog', 'cat']})
# y_pred = pd.DataFrame({"column": ['cat', 'dog', 'dog', 'cat', 'cat', 'cat']})
# print(my_func.cm(y_true, y_pred))

df = pd.DataFrame({'firsname': ['Anna', 'Peter'], 'lastname':['Smith', 'Peterson'], 'DOB': ['10-12-1988', '01-03-2000']})
print(my_func.date_split(df, 'DOB'))