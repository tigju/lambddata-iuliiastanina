import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

class ConfusionMatrix:
    def __init__(self, x_axis, y_axis, title, size=(10, 7)):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.title = title
        self.size = size

    def cm(self):
        return confusion_matrix(self.x_axis, self.y_axis)

    def labels(self):
        return unique_labels(self.x_axis)


if __name__ == "__main__":
    
    y_true = pd.DataFrame({"column": ['cat', 'dog', 'cat', 'cat', 'dog', 'cat']})
    y_pred = pd.DataFrame({"column": ['cat', 'dog', 'dog', 'cat', 'cat', 'cat']})

    cm1 = ConfusionMatrix(y_true, y_pred, "Example", (6,4))
    
    print(cm1.labels())
