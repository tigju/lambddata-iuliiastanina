# lambddata-iuliiastanina

## Installation

TODO

## Usage

```py
from my_lambdata.my_func import enlarge, check_null, train_val_test_split

x = 5

print(enlarge(x))

df = pd.DataFrame({'a': [2, 4, None, None], 
                   'b': [4, None, 4, 5], 
                   'c': ['Cat', 'Dog', 'bird', 'fish'], 
                   'd': [3,4,5,6], 
                   'e':[10,56,89,67]})

# check the null values in dataframe
print(check_null(df))

# train/val/test split
train, val, test = train_val_test_split(df)
```