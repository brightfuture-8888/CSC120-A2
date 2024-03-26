from computer import *
class ResaleShop:

# What attributes will it need?
    inventory:list
# How will you set up your constructor?
# Remember: in python, all constructors have the same name (__init__)
    def __init__(self): 
        self.inventory=[]

    # What methods will you need?

    # define buy method
    def buy(self,computer:Computer): 
        self.inventory.append(computer) 
        print("Computer added successfully")

    # define sell method
    def sell(self,computer:Computer): 
        if computer in self.inventory:
            self.inventory.remove(computer) 
            print("Computer removed successfully")       
        else:
            print("Computer doesn't exist.")

    # define print__inventory method
    def print_inventory(self):
        if  self.inventory:
            for comp in self.inventory: 
                print("comp details") 
        else: print("No inventory to display.") 

    # define reefurbish method
    def refurbish(self,computer:Computer,new_os: Optional[str] = None):
        if computer in self.inventory:
                
            if computer.year_made < 2000:
                computer.price = 0 # too old to sell, donation only 
            elif computer.year_made < 2012: 
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif computer.year_made < 2018:
                    computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff 

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
            else:
                    print("not found. Please select another item to refurbish.")  
        else: print("Computer doesn't exist in inventory.")

# define main method that include all of the attributes that we defined        
def main():

    mycomputer=Computer("MacBookcomputer","Retina",200,130,"Apple",2018,2000)
    myshop=ResaleShop()
    myshop.buy(mycomputer)
    mycomputer.update_price(2000)
    myshop.sell(mycomputer)
    myshop.print_inventory()
    myshop.refurbish(mycomputer,new_os="A")
    print(mycomputer.price)

main()

