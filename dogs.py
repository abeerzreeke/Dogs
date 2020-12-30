class Dog:
    def __init__(self, name, age, weight):
      self.name = name
      self.age = age
      self.weight = weight

    def bark(self):            
        return 'barks'

    def run_speed(self):
        speed = self.weight / self.age * 10 
        return f'the dogs running speed  {speed} ' 
        
    def fight(self, other_dog):
        self.other_dog = other_dog
        speed_other_dog = other_dog.run_speed()
        speed_dog = self.run_speed()

        if speed_dog > speed_other_dog:
            return '{} it the won !' .format(self.name)
        return '{} it the won !' .format(other_dog.name)
        

if __name__ == '__main__':
    my_dog = Dog('bobe', 11, 22)
    my_dog1 = Dog('max', 4, 1)
    my_dog2 = Dog('meka', 1, 13)
    print(my_dog.run_speed())
    print(my_dog.fight(my_dog1))


    
