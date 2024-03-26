from typing import Optional


class Computer:

    # What attributes will it need? 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int 

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.description=description
        self.processor_type=processor_type
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price
    def update_price(self,new_price: int):
        self.price=new_price

    def refurbish(self,computer: str,new_os: Optional[str] = None):
           if self.year_made < 2000:
               self.price = 0 # too old to sell, donation only 
           elif self.year_made < 2012:
               self.price = 250 # heavily-discounted price on machines 10+ years old
           elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
           else:
               self.price = 1000 # recent stuff

           if new_os is not None:
               computer.operating_system = new_os # update details after installing new OS
           else:
                print("not found. Please select another item to refurbish.")

    # What methods will you need?
def main():
    mycomputer=Computer("MacBookcomputer","Retina",200,130,"Apple",2018,2000)

if __name__ == "__main__": main()
