# chalu processes chi list dictonary format madhe display krt
import psutil       #running processes chi mahiti handle karayla
from sys import *
import os
import time

def ProcessDisplay(log_dir = "Marvellous"):
    listprocess = []
    
    if not os.path.exists(log_dir):     #jr folder nasel tr folder banva 
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator = "-" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))     #folder cha path join karun current time chya navane log file create keli
    f = open(log_path,'w')  #file write mode madhe create karun open keli
    f.write(seperator + "\n")       #file madhe seperator write kela
    f.write("Marvellous Process Logger : "+time.ctime() + "\n")
    f.write(seperator + "\n")

    for proc in psutil.process_iter():      #process_iter method process chi mahiti anun dete
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])     #as_dict he type casting ahe 
            #mhanje yenara data as a dictonay mhanun ghya
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            #1024*1024 = 1 kb
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor with memory and log file")

    print("Application name : ",argv[0])

    if(len(argv)!= 2):
        print("Error : Invalid number of argumnets")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This script is uses log record of running process")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()
    
    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid Datatype of input")

    except Exception:
        print("Error : Invalid Input")
    
if __name__=="__main__":
    main()
