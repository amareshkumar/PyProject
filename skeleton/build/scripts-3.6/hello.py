import math
import array
from sys import argv


class Arithmetic:
    def sum (self, a, b):
        return a+b

    def max (self, a, b):
        return (a > b) and a or b

    def square (self, n):
        return n * n;

    def average (self, arr):
        return sum (arr) / len(arr)


def Main():
    print("Hello Python")
    #number = int (input ("Enter Number:"))

    #create an object
    ar = Arithmetic();
    #print("Square: ", ar.square(number))
    #print ("Sum: ", ar.sum(number, 4))
    #assert ((2*number)%2 ==0), "should be even"

    #print ("Max: ", max(input("number1: "), input("number2: ")))

    #create an array
    arr = [2, 4, 6, 7, 8]
    print ("Avg of ele in array arr: ", ar.average(arr))

    #print ("Lets play with command line input")

    #script, first, second = argv;
    #print ("first: ", first, "Second", second)
    #print ("sum of args:", ar.sum(int(first), int (second)))

    # print("Reading from a file")
    # script, filename = argv

    # txt = open(filename)
    # print(f'filename is "{filename}":')
    # print(txt.read())

    # print ("enter another file name to read: ")
    # prompt = input ("> ")

    # txt2 = open (prompt)
    # print (f'you entered: "{prompt}"') 
    # print(txt2.read())   

if __name__== "__main__":
    Main()