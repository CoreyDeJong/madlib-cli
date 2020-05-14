from textwrap import dedent

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

def returnKeys(user_answers, keyList):

    with open("../assets/madlib-template.txt", 'r') as template:
        content = template.read()

    for i in range(len(user_answers)):
        content=content.replace(keyList[i], user_answers[i],1)

    with open("../assets/madlib-response.txt","a") as xtemplate:
        xtemplate.write(content)

def main():
    welcome()
    keyList=getKeys()
    user_answers=user_input(keyList)
    returnKeys(user_answers, keyList)


if __name__ =="__main__":
    main()
   