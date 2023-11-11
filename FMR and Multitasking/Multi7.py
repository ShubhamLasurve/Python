#Multithreading
import os
import threading        #Multithreading cha module

def Task1(Value):
    print("PID of Task 1 is : ",os.getpid())

def Task2(Value):
    print("PID of Task 2 is : ",os.getpid())

def main():
    print("PID of parent process is : ",os.getpid())
    No = 5

    t1 = threading.Thread(target= Task1, args = (No,))  #Creation of thread
    t2 = threading.Thread(target= Task2, args = (No,))

    t1.start()          #Starting the execution of thread
    t2.start()

    t1.join()           #Wait for the execution of threads
    t2.join()
    

if __name__ == "__main__":
    main()