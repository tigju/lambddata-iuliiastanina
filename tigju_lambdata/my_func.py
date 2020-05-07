import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import seaborn as sns
import matplotlib.pyplot as plt

# enlarge number
def enlarge(n):
    return n * 100

# check for nulls
def check_null(df):
    X = df.copy()
    null_list = X.isnull().sum()
    serie = pd.Series(null_list)
    new_df = pd.DataFrame({'column_name': serie.index, 'num_of_nulls': serie})
    new_df = new_df.reset_index(drop=True)
    return new_df

# split on train/val/test
def train_val_test_split(df):
    X = df.copy()
    train1, test = train_test_split(X, test_size=0.2, random_state=42, shuffle=True)
    train, val = train_test_split(train1, test_size=0.2, random_state=42, shuffle=True)
    return (train, val, test)

# confusion matrix
def cm(x, y):
    cm = confusion_matrix(x, y)
    cols = unique_labels(x)
    df_cm = pd.DataFrame(cm, columns=cols, index=cols)
    plt.figure(figsize=(10, 7))
    return sns.heatmap(df_cm, annot=True, cmap='Blues', fmt='.0f')

# separate day, month, year from date colunm 
def date_split(df, date_column):
    X = df.copy()

    X['day'] = pd.to_datetime(X[date_column]).dt.day
    X['month'] = pd.to_datetime(X[date_column]).dt.month
    X['year'] = pd.to_datetime(X[date_column]).dt.year

    return X

if __name__ == "__main__":
    # only run the code below if executing this file
    print(enlarge(5))

