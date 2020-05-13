from textwrap import dedent

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
















# def user_input():
#     print(dedent("""
#     ***********************************
#     ** What would you like to order? **
#     ***********************************
#     """))
#         while True:
#         order=input()
#         if order == 'quit':
#             break
        
#         # update items
#         # items[order] += 1

#         ## when user places an order           
#         if order in items:
#                 amount = items[order]
#                 if amount ==0:
#                     print(f"\n** {amount + 1} order of {order} have been added to your meal **\n")
#                     items[order]+=1
#                 if amount >=1:
#                     print(f"\n** {amount + 1} orders of {order} have been added to your meal **\n")
#                     items[order]+=1



def main():
    welcome()
    # show_menu()
    # take_order()

if __name__ =="__main__":
    main()