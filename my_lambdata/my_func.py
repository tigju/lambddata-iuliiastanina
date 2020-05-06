import pandas as pd
from sklearn.model_selection import train_test_split
def enlarge(n):
    return n * 100

def check_null(df):
    X = df.copy()
    null_list = X.isnull().sum()
    serie = pd.Series(null_list)
    new_df = pd.DataFrame({'column_name': serie.index, 'num_of_nulls': serie})
    new_df = new_df.reset_index(drop=True)
    return new_df

def train_val_test_split(df):
    X = df.copy()
    train1, test = train_test_split(X, test_size=0.2, random_state=42, shuffle=True)
    train, val = train_test_split(train1, test_size=0.2, random_state=42, shuffle=True)
    return (train, val, test)

if __name__ == "__main__":
    # only run the code below if executing this file
    print(enlarge(5))

