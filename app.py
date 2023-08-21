def index() :

    firstNumber = int(input("please send firstNumber:")) 
    secoundNumber =int(input("please send secoundNumber:"))
    type = input("please send your resuly , forexample(Total,Subtraction,Multiplication,Division):")


   
    if type  == "Total" :
        print(f"your answer is :{firstNumber+secoundNumber}")
    elif type == "Subtraction" :
        print(f"your answer is :{firstNumber-secoundNumber}")
    elif type == "Multiplication" :
        print(f"your answer is :{firstNumber*secoundNumber}")
    elif type == "Division" :
        print(f"your answer is :{firstNumber/secoundNumber}")
    else :
        pass





index()