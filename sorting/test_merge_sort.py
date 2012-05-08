import unittest
import random

class TestMergeSort(unittest.TestCase):
  def test_sort(self):
    a = []
    for x in range(100):
      a.append(random.randint(0,100))
    b = list(a)
    control_array = sorted(b)
    
    self.assertEqual(control_array, QuickSort.sort(a))

class Callable:
  def __init__(self, anycallable):
    self.__call__ = anycallable

class QuickSort:
  def sort(array):
    if len(array) <=1:
      return array
    pivot = array.pop()
    less = []
    greater = []
    for x in array:
      if x <= pivot:
        less.append(x)
      else:
        greater.append(x)
    return QuickSort.sort(less) + [pivot] + QuickSort.sort(greater)
    
  sort = Callable(sort)
     
if __name__ == '__main__':  
  unittest.main()
