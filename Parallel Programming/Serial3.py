#This will show Serial processing
#Ek burner wali shegdi
#Program run vhayla lagnara vel show karel
#Kam vatun ghyaycha code ( Multi burner shegdi)

import time
import multiprocessing

def fun(no):
    sum = 0

    for i in range(100000):
        sum = sum + (no*no)
    return sum

def main():
    print("Demonstration of serial execution using single core")

    starttime = time.time()
    p = multiprocessing.Pool()      # p is a object of class Pool

    Result = []
    Result = p.map(fun,range(10000))
    p.close()
    p.join()

    endtime = time.time()
    print("Time required to execute a application : ",endtime - starttime)
    
if __name__ == "__main__":
    main()