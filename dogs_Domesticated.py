import random
from dogs import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained):
         super().__init__(name, age, weight)
         self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *other_dogs):
        for one_dog in other_dogs:
            print('the dogs: ' + self.name + ' and '+ one_dog.name + ' play together')
            one_dog.trained = False

    def do_a_trick(self):
        if (self.trained):
            dog_name = self.name
            sentences = (
                'does a barrel roll',
                'stands on their back legs',
                'hakes your hand',
                'plays dead'
            )
        num = random.randrange(0,4)
        print( dog_name + ' ' +  sentences[num])
        self.trained = False
    
if __name__ == '__main__':
    my_dog = PetDog('bobe', 11, 22,False)
    my_dog1 = PetDog('max', 4, 1, True)
    my_dog2 = PetDog('meka', 1, 13, False)
    my_dog.play(my_dog1, my_dog2)

