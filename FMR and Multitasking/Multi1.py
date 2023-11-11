#Demonstration of multi tasking
#Serial code
#There is no multiprocessing

import multiprocessing
import os

def Task1():
    print("Executing the first task...")
    print("PID of running process for Taks 1 is : ",os.getpid())

def Task2():
    print("Executing the second task...")
    print("PID of running process for Task 2 is : ",os.getpid())

def main():
    print("Demonstration of Multiprocessing")

    print("PID of running process is : ",os.getpid())

    Task1()
    Task2()

if __name__ == "__main__":
    main()