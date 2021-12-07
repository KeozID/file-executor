import os
import time
import getpass

__currentscript__ = os.path.basename(__file__)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__user_info__ = os.path.join(getpass.getuser())

print(f"file-executor       User: {__user_info__}  /  type 'help' to view command")
print("──────────────────────────────────────────────────────────────────────────")

def main(shutdown_timer):
    loop = True
    while loop == True:
        file = input("file-name: ").lower()
        if file == "ls" or file == "list" or file =="dir":
            os.system("cd " + __location__)
            print("────────DIRECTORY────────")
            for i in os.listdir(__location__):
                if i == __currentscript__:
                    continue
                print(i)
            print("─────────────────────────")
        else:
            os.system(os.path.join(__location__, file))
        if file == "help":
            print("─────────────────────────")
            print("write 'quit' to quit, write 'list' to get content")
        if file == "quit" or file == "exit":
            loop = False
            print("Quitting Script..")
            time.sleep(shutdown_timer)

if __name__ == "__main__":
    main(1)
else:
    print("Invalid")