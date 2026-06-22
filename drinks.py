class Drink:
    def __init__(self,name,water,milk,coffee,sugar,price):
        self.name= name
        self.water= water  #latte.water = 200, this is how self will work
        self.milk=milk
        self.coffee=coffee
        self.sugar=sugar
        self.price=price

latte= Drink("Latte",200,150,24,1,120)
espresso= Drink("Espresso",50,0,18,0,150)
cappuccino= Drink("Cappuccino",250,100,24,1,180)                       

 