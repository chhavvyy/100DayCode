
def add(n1, n2):
           return n1 + n2


def subtract(n1, n2):
            return n1 - n2


def multiply(n1, n2):
             return n1 * n2


def divide(n1, n2):
             return n1 / n2


dict ={
    "+": add ,
    "-": subtract ,
    "*": multiply ,
    "/": divide }
def calculator():
    hah = True
    a = int(input("whats the first value"))
    while hah:

        for symbol in dict:
            print(symbol)
        operation_symbol = input("pick an operation symbol")
        b = int(input("whats the second value"))
        answer = dict[operation_symbol](a,b)
        print(f"{a} {operation_symbol} {b}= {answer} ")

        choice = input("select 'y' to continue or 'n' to exit")
        if choice == "y":
             a = answer
        else:
            hah = False
            print("calc closed")
            print( "\n" * 20)
            
            calculator()
calculator()