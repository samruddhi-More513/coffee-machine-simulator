import time
import os
from drinks import Drink,latte,espresso,cappuccino
from coffee_machine import Coffeemachine

initial_resources= Coffeemachine(1000,500,200,100,500)

drinks_menu ={
        "latte":latte,
        "lat":latte,
        "espresso":espresso,
        "esp":espresso,
        "cappuccino":cappuccino,
        "cap":cappuccino
}

commands_menu={

    "menu":"Main_menu",
    "rep": "Report",
    "can" : "Cancel"
 }

def user_choice():
 while True:
    print(""" 
          
====================================
          
         COFFEE MACHINE
          
====================================
          
          
Welcome! Let's grab some coffee:
════════════════════════════
          MENU
════════════════════════════
☕ Latte(lat)      - ₹120
☕ Espresso(esp)   - ₹150
☕ Cappuccino(cap) - ₹180
════════════════════════════
🏠 Main Menu         [menu]       
📊 Report            [rep] 
❌ Cancel            [can] 
════════════════════════════
          """)
          

    user_choice= input("What would you like? \n").lower() 
    if user_choice in drinks_menu: 
       selected= drinks_menu[user_choice]
       print(f"You ordered {drinks_menu[user_choice].name},  Price: ₹{selected.price} \n")
       
       return selected
    elif user_choice== "rep":
        initial_resources.report()
        input("Press Enter to continue")
        clear_screen()

    elif user_choice== "can":
        print("Order Cancelled")
        print("Returning to Main Menu", end="", flush=True)

        for i in range(3):
          time.sleep(1)
          print(".", end="", flush=True)

        time.sleep(1.5)
        clear_screen()
    elif user_choice == "menu":
      clear_screen()
      continue
       

    else: 
       print("Invalid Choice")
       print("Please enter the right choice")
       continue
      
    
 


def payment(selected):   
  total_payment = 0   
  while True:
   payment_input = (input("Please insert the money ""\n")).lower()
   if payment_input.isdigit():
     user_payment= int(payment_input)
     break  
   
   elif payment_input== "can":
     print("You cancelled the payment")
     print("Returning to Main Menu", end="", flush=True)
     for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
     time.sleep(1.5)
     clear_screen()
     return False
   else:
     print("Invalid input! Please enter a number or 'can'")
     
  
  total_payment += user_payment
    
  while total_payment< selected.price: 
        needed_money = selected.price - total_payment
        print("Oops! looks like you havent inserted enough amount") 

        extra_input = input(f"Please pay ₹{needed_money} more to get the coffee (or type 'can' to cancel)\n").lower()

        if extra_input == "can":
            print("You cancelled the payment")
            print(f"Here is your refund: ₹{total_payment}")
            print("Returning to Main Menu", end="", flush=True)

            for i in range(3):
             time.sleep(1)
             print(".", end="", flush=True)
            time.sleep(1.5)
            clear_screen()
   
            return False
            
        elif extra_input.isdigit():
            extra = int(extra_input)
            total_payment += extra

        else:
            print("Invalid input! Please enter a valid amount or 'can'.")
       
        
  
  if total_payment > selected.price:
        change = total_payment - selected.price 
        print(f"Your Change: {change}") 
       
       
  
  return True

def clear_screen():
    os.system("cls")




while True:

    selected = user_choice()

    if not selected:
        continue

    result, missing = initial_resources.check_resources(selected)
    if not result:
        print(f"Sorry, Not Enough {missing}\nPlease Refill")
        while True:
           
         choice =input("Refill machine? (yes/no): ").lower()
         if choice== "yes":
           initial_resources.refill()
           print("Machine refilled successfully!")
           input("Press Enter to continue")
           clear_screen()
           break
         elif choice== "no":
           input("Press Enter to continue")
           clear_screen()
           break
         else:
            print("Please enter only 'yes' or 'no'")
        continue
        
        
        
    
    
    payment_done = payment(selected)
    if not payment_done:
      continue
    initial_resources.deduct_resources(selected)

    print(f"\n☕ Preparing your {selected.name}...\n")

    steps = [
    "🫘 Grinding coffee beans...",
    "💧 Heating water...",
    "🥛 Steaming milk...",
    "☕ Brewing coffee...",
    "✨ Pouring into cup..."
      ]

    bars = [
    "[■□□□□]",
    "[■■□□□]",
    "[■■■□□]",
    "[■■■■□]",
    "[■■■■■]"
    ]

    for step, bar in zip(steps, bars):
     print(f"{step}")
     print(f"\r{bar}", end="", flush=True)
     time.sleep(1)
     print("\n")

    print("✅ Coffee Ready!\n")
 
    print(r"""
   ( (
    ) )
  ........
  |      |]
  \      /    
   `----' """)
    print("\n")
    print(f"Here is your {selected.name}")

       
    print("Thank you, Have a Beautiful Day!")
    print("Returning to Main Menu", end="", flush=True)

    for i in range(3):
     time.sleep(1)
     print(".", end="", flush=True)
   
    time.sleep(1.7)
    clear_screen()
