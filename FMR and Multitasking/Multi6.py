#Demonstration of multi tasking
#Serial code
#vegveglya processes create kelya ahet
#Multiprocessing cha code pn execution serially karaych asel tr

import multiprocessing
import os

def Task1(Value):       #Child Process1
    print("Executing the first task...")
    for i in range(Value):
        print("Task1 : ",i)

def Task2(Value):       # Child Process2
    print("Executing the second task...")
    for i in range(Value):
        print("Task2 : ",i)

def main():         #Parent process
    print("Demonstration of Multiprocessing")

    print("PID of running process is : ",os.getpid())

    No1 = 500
    No2 = 800

    p1 = multiprocessing.Process(target= Task1, args = (No1,))  #This function creates the process
    p2 = multiprocessing.Process(target= Task2, args = (No2,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()

if __name__ == "__main__":
    main()