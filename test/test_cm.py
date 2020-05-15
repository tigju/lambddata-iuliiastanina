import unittest

from tigju_lambdata.oop import ConfusionMatrix

class TestConfusionMatrix(unittest.TestCase):

    def test_values_type(self):

        list1 = ['cat']
        list2 = ['cat']
        
        cm = ConfusionMatrix(list1, list2)
        self.assertEqual(type(cm.x_axis), list)
        self.assertEqual(type(cm.y_axis), list)



if __name__ == '__main__':
    unittest.main()


