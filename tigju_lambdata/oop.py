import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import seaborn as sns
import matplotlib.pyplot as plt

class ConfusionMatrix:

    '''
    This class creates and object of confusion matrix for classification predictions

    Params: 
            x_axis (series, true values)
            y_axis (series, predicted values) 
            title (string, name of the confusion matrix)
            size (tuple, containing 2 integers of width and height of plot. Default (10, 7))
            color (str 'coolwarm', 'YlGnBu', 'BuPu', 'Greens', 'Blues'. Default='Blues')
            format (str how mady decimals to show. Dafault '.0f')

    Returns: 
            Object (confusion matrix)

    Dependencies: 
                pandas,
                confusion_matrix from sklearn.metrics,
                unique_labels from sklearn.utils.multiclass,
                matplotlib.pyplot,
                seaborn
    '''

    def __init__(self, x_axis, y_axis, title, size=(10, 7), color='Blues', format_cm='.0f'):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.size = size
        self.color = color
        self.format_cm = format_cm

    def cm(self):
        return confusion_matrix(self.x_axis, self.y_axis)

    def labels(self):
        return unique_labels(self.x_axis)

    def make_df(self):
        cm = self.cm()
        cols = self.labels()
        df = pd.DataFrame(cm, columns=cols, index=cols)
        return df

    def plot_cm(self):
        plt.figure(figsize=self.size)
        return sns.heatmap(self.make_df(), annot=True, cmap=self.color, fmt=self.format_cm)




if __name__ == "__main__":
    
    y_true = pd.DataFrame({"column": ['cat', 'dog', 'cat', 'cat', 'dog', 'cat']})
    y_pred = pd.DataFrame({"column": ['cat', 'dog', 'dog', 'cat', 'cat', 'cat']})

    cm1 = ConfusionMatrix(y_true, y_pred, "Dogs and Cats", (6, 4))
    
    print(cm1.x_axis)
    print(cm1.y_axis) 
    print(cm1.title)
    print(cm1.size) 
    print(cm1.color) 
    print(cm1.format_cm)
    print(cm1.cm())
    print(cm1.labels())
    print(cm1.make_df())
    print(cm1.plot_cm())
