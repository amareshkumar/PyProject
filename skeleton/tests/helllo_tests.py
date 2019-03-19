from nose.tools import *
from NAME.hello import Arithmetic

# def test_avg():
# 	ar = Arithmetic()
#     arr = [1, 4, 10, 15, 20]

#     assert_equal (ar.average(arr), 10)

# def test_max():
# 	ar = Arithmetic()
    
#     assert_equal(ar.max(3, 5), 5)

def test_square ():
	ar = Arithmetic()

	assert_equal(ar.square(5), 25)

def test_sum ():
	ar = Arithmetic()	

	assert_equal (ar.sum(4, 3), 7)