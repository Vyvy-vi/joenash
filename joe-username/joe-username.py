import random

JOES_CONSTANTS = ["right", "awesome", "interesting", "cool","cool"]
def generate(max_limit=4):
  max_limit = int(max_limit)
  word = ""
  for i in range(max_limit):
    rand_word = random.choice(JOES_CONSTANTS)
    word += rand_word[0].upper() + rand_word[1:]
  return word
print(generate(random.randint(3,11)))
