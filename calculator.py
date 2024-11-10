a = int(input("enter any number:"))
b = int(input("enter any number:"))
choice = input("enter any operator from (+,-,*,/): ")
match choice:
    case "+":
        print("the value of",a,"+",b, "is:",a+b)
    case "-":
        print("the value of", a, "-", b, "is:",a-b)
    case "*":
        print("the value of", a, "*", b, "is:",a*b)
    case "/":
        print("the value of", a, "/", b, "is:",a/b)


    