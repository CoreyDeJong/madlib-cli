from textwrap import dedent

# items = dict.fromkeys(menu_list,values)
# f = open('./madlib-cli')

def welcome():
    message = """
        **************************************
        **       Welcome to Madlibs!        **
        **    Please provide a response     **
        **        to each question          **
        **                                  **  
        ** To quit at any time, type "quit" **
        **************************************
        """
    print(dedent(message))


def getKeys():

    with open("../assets/madlib-template.txt") as template:
        content = template.read()
      
    keyList = []
    last=0

    numOfKeys = content.count('{')
    

    for i in range(numOfKeys):
        begin = content.find('{', last)+1
        last = content.find('}', begin)
        key = content[begin : last]
        keyList.append(key)

    return keyList
        

def user_input(keyList):
     
    numQuestions = len(keyList)
    user_answers = []
    for i in range(numQuestions):
        print(f"Please enter a {keyList[i]}")
        user_answers.append(input())
    
    return user_answers


def main():
    welcome()
    keyList=getKeys()
    user_input(keyList)


if __name__ =="__main__":
    main()
   