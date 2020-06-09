# import json


def main():

#     jsonStr='''[
#     {
#     "setup": "What do you call a group of 8 hobbits?",
#     "punchline": "A hobbyte.",
#     "laughs": 0,
#     "groans": 0
#     },
#     {
#     "setup": "Why do ducks make great detectives?",
#     "punchline": "They always quack the case.",
#     "laughs": 0,
#     "groans": 0
#     }
#     ]'''
#     data = json.loads(jsonStr)
#     for i in data:
#         print(data["setup"])
    lic = [{'setup':'i dont know','punchline':'hey baby'},{"setup":"Hey darling"}]
    for item in lic:
        if 'hey' in item['setup'].lower():
            print(item['setup'])
             
    
    
    
    

        
    
if __name__ == "__main__":
    main()
