import random

JOE_WORDS = ["right", "awesome", "interesting", "cool","cool"]
def generate(lim:int=4):
  word = ""
  for i in range(lim):
    rand_word = random.choice(JOE_WORDS)
    word += rand_word.title()
  return word
print(generate(random.randint(2,11)))
