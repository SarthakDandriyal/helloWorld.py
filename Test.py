#! /usr/bin/python3

import unitest

from prog1 import summation

class TestSum(unitest.TestCase):
  def test_list_int(self):
    """
    test case to add 2 numbers
    """
    data=[20,30]
    result=summation(data)
    self.assertEqual(result,50)
    
if __name__=='__main__':
  unitest.main()
