import unittest
import pandas as pd
import matplotlib
from tigju_lambdata.oop import ConfusionMatrix

class TestConfusionMatrix(unittest.TestCase):


    def test_values_type(self):
        list1 = ['cat']
        list2 = ['cat']
        cm = ConfusionMatrix(list1, list2)
        self.assertEqual(type(cm.x_axis), list)
        self.assertEqual(type(cm.y_axis), list)

    def test_labels(self):
        list1 = ['cat', 'dog', 'dog']
        list2 = ['cat', 'cat', 'dog']
        cm = ConfusionMatrix(list1, list2)
        df = cm.make_df()
        self.assertEqual(list(df.columns), list(df.index))

    def test_plot(self):
        list1 = ['cat', 'dog', 'dog']
        list2 = ['cat', 'cat', 'dog']
        cm = ConfusionMatrix(list1, list2)
        plot = cm.plot_cm()
        self.assertTrue(hasattr(plot, 'figure'))

if __name__ == '__main__':
    unittest.main()


