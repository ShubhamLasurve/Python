# chalu processes chi list dictonary format madhe display krt
import psutil       #running processes chi mahiti handle karayla

def ProcessDisplay():
    listprocess = []
    
    for proc in psutil.process_iter():      #process_iter method process chi mahiti anun dete
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])     #as_dict he type casting ahe 
            #mhanje yenara data as a dictonay mhanun ghya
            pinfo['vms'] = proc.memory_info().vms/(1024 * 1024)
            #1024*1024 = 1 kb
            
            listprocess.append(pinfo);
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation & Machine Learning")

    print("Process Monitor")
    
    listprocess = ProcessDisplay()

    iCnt = 0
    for elem in listprocess:
        iCnt+=1
        print(elem)
    
    print("Number of running processes are : ",iCnt)

if __name__=="__main__":
    main()
