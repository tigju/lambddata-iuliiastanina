import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

class ConfusionMatrix:

    '''
    This class creates and object of confusion matrix 
    for classification predictions

    Params: x_axis (series, true values)
            y_axis (series, predicted values) 
            title (string, name of the confusion matrix)
            size (tuple, containing 2 integers of width and height of plot)

    Returns: Object (confusion matrix)
    '''
    def __init__(self, x_axis, y_axis, title, size=(10, 7)):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.size = size

    def cm(self):
        return confusion_matrix(self.x_axis, self.y_axis)

    def labels(self):
        return unique_labels(self.x_axis)

    def create_df(self):
        cm = self.cm()
        cols = self.labels()
        df = pd.DataFrame(cm, columns=cols, index=cols)
        return df
    # def plot_cm(self):



if __name__ == "__main__":
    
    y_true = pd.DataFrame({"column": ['cat', 'dog', 'cat', 'cat', 'dog', 'cat']})
    y_pred = pd.DataFrame({"column": ['cat', 'dog', 'dog', 'cat', 'cat', 'cat']})

    cm1 = ConfusionMatrix(y_true, y_pred, "Example", (6,4))
    
    print(cm1.create_df())
