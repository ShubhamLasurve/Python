#Demonstration of multi tasking
#Serial code
#vegveglya processes create kelya ahet

import multiprocessing
import os

def Task1(Value):       #Child Process1
    print("Executing the first task...")
    print("PID of running process for Taks 1 is : ",os.getpid())

def Task2(Value):       # Child Process2
    print("Executing the second task...")
    print("PID of running process for Task 2 is : ",os.getpid())

def main():         #Parent process
    print("Demonstration of Multiprocessing")

    print("PID of running process is : ",os.getpid())

    No = 5
    p1 = multiprocessing.Process(target= Task1, args = (No,))  #This function creates the process
    p2 = multiprocessing.Process(target= Task2, args = (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()