

class Animal:
    noise = "Rrr"   # A variable attached to Animal class is called properties
    color = "Red"

    def make_noise(self):
        print(f"{self.noise}")

    # def set_noise(self, new_noise):
    #     self.noise = new_noise
        

    def get_noise(self):
        return self.noise
    
    def set_noise(self, new_noise):
        self.noise = new_noise
        return self.noise
    

    def set_color(self, new_color):
        self.color = new_color
        return self.color
    
    def get_color(self):
        return self.color
         

class wolf(Animal):             # This class inherit Animal class 
    noise = "grr"


class BabyWolf(wolf):
    color = "Yellow"


# BabyWolf → wolf → Animal   # This is multilevel inheritance , as there is a chain of inheritance from Animal to wolf and then to BabyWolf.

    
    # def rando(self):
    #     print("this")



# obj = Animal()
# print(obj)

# obj.make_noise()
# print(obj.noise)


