import random

class Pou:
  # inciciar
  def __init__(self, name):
    self.name = name
    self.age = random.randint(1, 10)
    self.hunger = random.randint(1, 10)
    self.energy = 0
    self.happiness = 0
    self.health = 0
    self.alive = True

  def status(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Hunger:", self.hunger)
    print("Energy:", self.energy)
    print("Happiness:", self.happiness)
    print("Health:", self.health)

  def __str__(self): #__str__ seria la alternativa (lo mismo) a __repr__
    return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}"

  def play(self):
    self.hunger += 1
    self.energy += 1
    self.happiness += 1
    self.health += 1

    # Add code
    if(self.energy <= 0):
      self.happiness -= 1
    else:
      self.happiness += 1

def eat(self):
    self.hunger -= 1
    self.happiness += 1
    #pass #to indicate that the body of the class 'eat' was intentionally left blank.

  # add more methods
def sleep(self):
  self.energy += 5
  self.happiness += 1
  self.hunger += 3

toto = Pou("Toto")

while True:
  option = input("What do you want to do? (play, eat, sleep, exit): ")

  if option == "play":
    toto.play()
    toto.status()
# add more methods
  elif option == "eat":
    toto.eat()
    toto.status()
  elif option == "sleep":
    toto.sleep()
    toto.status()
  else:
    break
   