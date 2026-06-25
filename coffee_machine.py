class Coffeemachine():
    def __init__(self, water_left, milk_left,coffee_left,sugar_left,balance):
        self.water_left= water_left
        self.max_water=water_left
        self.milk_left=milk_left
        self.max_milk=milk_left
        self.coffee_left=coffee_left
        self.max_coffee_=coffee_left
        self.sugar_left= sugar_left
        self.max_sugar= sugar_left
        self.balance=balance

    def report(self):
      print("""
 ══════════════════════════════════════
          📊 MACHINE REPORT 📊         
 ══════════════════════════════════════
""")

      print(f"💧 Water   : {self.water_left:>4} ml")
      print(f"🥛 Milk    : {self.milk_left:>4} ml")
      print(f"🫘 Coffee  : {self.coffee_left:>4} gm")
      print(f"🍬 Sugar   : {self.sugar_left:>4} gm")

      print("──────────────────────────────────────")

      print(f"💰 Balance : ₹{self.balance}")

      print("══════════════════════════════════════")


    def check_resources(self,selected):
        if self.water_left < selected.water:
            return False, "Water"
        if self.milk_left< selected.milk:
            return False,"Milk"
        if self.coffee_left< selected.coffee:
            return False,"Coffee"  
        if self.sugar_left< selected.sugar:
            return False,"Sugar"
        return True,None

    def deduct_resources(self,drink):
        self.water_left -= drink.water
        self.milk_left -= drink.milk
        self.coffee_left -= drink.coffee
        self.sugar_left -= drink.sugar
        self.balance += drink.price 
    
    def refill(self):
        self.water_left=self.max_water
        self.milk_left=self.max_milk
        self.coffee_left=self.max_coffee_
        self.sugar_left=self.max_sugar
 