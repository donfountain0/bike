# Create a new class called Bike with the following properties/attributes:
# price
# max_speed
# miles
class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    
# Create 3 instances of the Bike class.
# mongoose = Bike(10, "25 mph", 33)
# schwinn = Bike(10.00, "20 mph", 33)
# tonyHawk = Bike(10.00, "35 mph", 33)

# Use the __init__() method to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); 
# In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.


# Add the following methods to this class:

    
# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self
    
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10

    def ride(self):
        self.miles = self.miles + 10
        print("Riding")
        return self

# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
    def reverse(self):
        self.miles = self.miles - 5
        print("Reversing")
        return self

# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, 
# reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
mongoose = Bike(10, "25 mph", 33)
mongoose.ride().ride().ride().displayInfo()

schwinn = Bike(20, "20 mph", 35)
schwinn.reverse().reverse().displayInfo()