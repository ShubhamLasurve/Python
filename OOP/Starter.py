#Starter cha demo
# Module1.py ani Module2.py pn check kara

import Module1
import Module2

def main():
    print("Special variable of starter.py is : ",__name__)

    Module1.DisplayModule1()
    Module2.DisplayModule2()

if __name__ == "__main__":
    main()