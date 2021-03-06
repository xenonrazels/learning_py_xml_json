import json

try:
    f = open("data.txt", 'r')
    data = json.load(f)
except:  #JSONDecodeError as err:print("erroer in json file")  print(err.msg)
    data = [] # except FileExistsError as err:print("Opss!! something gone wrong")     print(err.msg)
def input_int():
    number = int(input("Jokes number to view :"))
    for k, v in enumerate(data):
        if k==number-1:
            print(f"   {v['setup']}")
            print(f"    {v['punchline']}")
            if v['laugh'] == 0 and v['groans'] == 0:
                print("joke is not rated  ")
            else:
                print(f"{v['laugh']} {v['groans']}")
        else:
            print("joke number is  out of bound")
            break
def del_jokes():
    del_num = int(input("joke number to delete:"))
    for k,v in enumerate(data):
        if k == del_num - 1:
            data.__delitem__(del_num - 1)
            sav_data(data)
    
def input_sth():
    search = ((input("Enter the word:")).strip()).lower()
    if search == '':
        input_sth()
    for index,value in enumerate(data):
        if search in (value["setup"]).lower():
            print("Found in setup")
            print(f" {index}) {value['setup']}")
        elif search in (value["punchline"]).lower():
            print("Found in punchline")
            print (f"{index}) {value['punchline']}")           

def input_something():
    setup = (input("Enter the setup :")).strip()
    punchline = (input("Enter the punchline :")).strip()
    if setup == "" or punchline == '':
        print("please don't use whitespcae cauz they are a part of joke")
        input_something()
    data_dic = {"setup": setup, "punchline": punchline, "laugh": 0, "groans": 0}
    data.append(data_dic)
    sav_data(data)


  
def sav_data(data_list):
    f = open("data.txt", 'w')
    json_str = json.dumps(data_list)
    f.write(json_str)
    f.close()
        

def main():
    print('Welcome to the Joke Catalogue Admin Program.')

    while True:
        print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        choice = input('> ')
            
        if choice == 'a':
            input_something()
 
        elif choice == 'l':
            if data == []:
                print("NO joke message is saved")
            else:
                print("List of jokes")
                for index,value in enumerate(data):
                    print(f" {index}) {value['setup']}")
        elif choice == 's':
            input_sth()
        elif choice == 'v':
            input_int()
        elif choice == 'd':
            del_jokes()
        elif choice == 'q':
            print("Goodbye!!")
            break
        else:
            print("You idiot user it's invalid choice")

if __name__ == "__main__":
    main()