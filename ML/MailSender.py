import os
from sys import *
import smtplib,ssl
import urllib.error
import urllib.request

def is_connected():
    try:
        urllib.request.urlopen('http://www.gmail.com')
        return True
    except urllib.error.URLError as err:
        return False

def MailSender(mailid):
    try:
        fromadd = "shubhamlasurve77@gmail.com"      #sender
        toadd = mailid                              #receiver
        #Body of mail
        Message = """                   
        Hello %s,
        This is auto generated mail.
        From : - Marvellous Infosystems
        """%(toadd)

        s = smtplib.SMTP('smtp.gmail.com',587)          #587 portnumber ahe

        s.starttls()                             #hi method smtp protocol use karun secure connection establish krte

        s.login(fromadd,"xsrf kyku qssq ywcu")      #hi method login krte

        s.sendmail(fromadd,toadd,Message)           #yane mail send hoil

        s.quit()                                    #Secure connection band karel 
        
        print("Mail Successfully Send")

    except Exception as E:
        print("Unable to send mail.",E)       

def main():

    if(len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to send mail")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName")
            exit()

    try:
        MailSender("svlasurve@gmail.com")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()    