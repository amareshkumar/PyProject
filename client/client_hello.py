#import from hello.py

import sys
sys.path.append('D:/PyCode/PyProject/PyIntegration')

import hello

def test_Ctor ():
	ar = Arithmetic(4)
	print (ar.classname())
    #print (ar.return_nearest_even())