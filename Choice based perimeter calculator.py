print("====Welcome to Perimeter calculator====")

while True:
    print("\n ==Select your choice==")
    print("[1.] Perimeter of Rectangle")
    print("[2.] Perimeter of square")
    print("[3.] area of cricle ")  
    choice = int(input("Enter your choice = ")) 
    
    if choice == 1:
        l = float(input(" Enter your length = "))
        b = float(input("Enter your breadth = "))   
        rect = 2 * (l + b)
        print(f"Ok thanks! your Perimeter of Rectangle is {rect}.")
        
    elif choice == 2:
        side = float(input("Enter your length of side = "))
        sqr = 4 * side
        print(f"Ok thanks! your Perimeter of Square is {sqr}.")
        
    elif choice == 3:
        print("3.14*(Radius**2)")
        break  
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

    else:
        p