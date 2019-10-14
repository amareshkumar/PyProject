import math
import array
from sys import argv

class Arithmetic:
    #data members
    number = 0
    classname = "Arithmetic"

    #member function
    def sum (self, a, b):
        return a+b

    def max (self, a, b):
        return (a > b) and a or b

    def square (self, n):
        return n * n;

    def average (self, *arr):
        sum = 0
        for a in arr:
            sum = sum + a;
        return sum / len(arr)
    #writing a c-tor
    def __init__(self):
        print (self.classname)
    #ctor with one argument
    def __init__(self, random):
        self.number = random

    def return_nearest_even (self):
        if (self.number % 2 == 0):
            return self.number
        else:
            return self.number+1

def Main():
    print("Hello Python")
    #number = int (input ("Enter Number:"))

    #create an object
    #ar = Arithmetic();
    #print("Square: ", ar.square(number))
    #print ("Sum: ", ar.sum(number, 4))
    #assert ((2*number)%2 ==0), "should be even"

    #print ("Max: ", max(input("number1: "), input("number2: ")))

    #create an array
    #arr = array.array('i', [2, 4, 6, 7, 8])
    #print ("Avg of ele in array arr: ", ar.average(arr))

    #print ("Lets play with command line input")

    #script, first, second = argv;
    #print ("first: ", first, "Second", second)
    #print ("sum of args:", ar.sum(int(first), int (second)))

    print("Reading from a file")
    script, filename = argv

    txt = open(filename)
    print(f'filename is "{filename}":')
    print(txt.read())

    #stored read input into a list

if __name__== "__main__":
    Main()