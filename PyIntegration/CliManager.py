import array
import sys
# import os
# os.system("python hello.py")
import hello

class CliManager:
    def take_input():
        print ("enter input: ")
        input = input()
        if (isinstance(input, int)):
            #process the integer input
            #ar = Arithmetic()
            #ar.square (input)
            print ("Todo")
        elif (isinstance(input, str)):
            print ("File read module")
        else:
            #process other inputs
            print ("ToDo")

    def read_File_print(self):
        print ("input file with complete path: ")
        input = str(input());

        with open (input) as f:
            #lineList = f.readlines();
            lineList = [line.rstrip('\n') for line in open(input)]

            print ("print list")
