import json
from json import JSONDecodeError
def main():
    try:
        f = open("data.txt", 'r')
        try:
            data = json.load(f)
        except JSONDecodeError as err:
            print("erroer in json file")
            print(err.msg)
    except FileExistsError as err:
        print("Opss!! something gone wrong")
        print(err.msg)

    #     f = []

    # f += [1, 3, 4]
    # print(f)

    # data = json.load(f)
    # f.close()
    # for i in data:
    #     jokes_dic = i
    #     print(jokes_dic["setup"])
if __name__ == "__main__":
    main()
