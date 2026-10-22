day = 3
match day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
        
        
Grade = 90
match Grade:
    case 90 | 95 | 100:
        print("Excellent")
    case 80 | 85:
        print("Good")
    case 70 | 75:
        print("Average")
    case _:
        print("Below Average")
        
        
        
        
Signal = "Green"
match Signal:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Prepare to stop")
    case "Green":
        print("Go")
    case _:
        print("Invalid signal")
        
        
month = 4
match month:
    case 1 | 2 | 3:
        print("Winter")
    case 4 | 5 | 6:
        print("Spring")
    case 7 | 8 | 9:
        print("Summer")
    case 10 | 11 | 12:
        print("Autumn")
    case _:
        print("Invalid month")        
        
        
op = "+"
match op:
    case "+":
        print("Addition")
    case "-":
        print("Subtraction")
    case "*":
        print("Multiplication")
    case "/":
        print("Division")
    case _:
        print("Invalid operator")   
        
        
            
drink = "Coffee"
match drink:       
    case "Coffee":
        print("You chose Coffee")
    case "Tea":
        print("You chose Tea")
    case "Juice":
        print("You chose Juice")
    case _:
        print("Invalid drink")
        
        
choice= 3
match choice:
    case 1:
        print("check balance")
    case 2:
        print("withdraw money")
    case 3:
        print("deposit money")
    case 4:
        print("exit")
    case _:
        print("Invalid choice")     
        
        
        
subject = 2
match subject:
    case 1 : 
        print("python")
    case 2:
        print("java")
    case 3:
        print("c++")
    case 4:
        print("data science")
    case _:
        print("Invalid subject")
        
        

choice = 3
match choice:
    case 1:
        print("Add ")
    case 2:
        print("Delete")
    case 3:
        print("Update")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")
        
        
friut = "Mango"
match friut:
    case "Apple":
        print("Apple is a good source of fiber")
    case "Banana":
        print("Banana is a good source of potassium")
    case "Mango":
        print("Mango is a good source of vitamin C")
    case "Orange":
        print("Orange is a good source of vitamin C")
    case _:
        print("Invalid fruit")        