import random

def minmax(value):
    # min(0, max(value, 100))
    if value < 0:
        return 0
    elif value > 100:
        return 100
    else:
        return value

state = {
    "name": "Toto",
    "age": 0,
    "hunger": random.randint(50, 100),
    "energy": random.randint(50, 100),
    "happiness": random.randint(50, 100),
    "health": random.randint(50, 100),
    "alive": True
}

def status():
    print("Name:", state["name"])
    print("Age:", state["age"])
    print("Hunger:", state["hunger"])
    print("Energy:", state["energy"])
    print("Happiness:", state["happiness"])
    print("Health:", state["health"])

def play(state):
    new_state = dict(state) # copy or clone
    new_state["hunger"] = minmax(state['hunger'] + 5)
    new_state["energy"] = state["energy"] - 10
    new_state["happiness"] = state["happiness"] + 10
    new_state["health"] = state["health"] + 5
    return new_state

def eat(state):
    new_state = dict(state)
    new_state["hunger"] = state['hunger'] - 5
    new_state["energy"] = state["energy"] + 10
    new_state["happiness"] = state["happiness"] + 10
    new_state["health"] = state["health"] + 5
    return new_state

def sleep(state):
    pass


while True:
  status()
  option = input("What do you want to do? (1) play, (2) eat, (3) sleep, (any) exit): ")

  if option == "1":
    state = play(state)
  elif option == "2":
    state = eat(state)
  # add more methods
  else:
    break
