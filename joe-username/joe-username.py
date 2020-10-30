import random

JOE_WORDS = ["right", "awesome", "interesting", "cool","cool"]
def generate(lim:int=4):
  word = ""
  for i in range(lim):
    rand_word = random.choice(JOE_WORDS)
    word += rand_word.title()
  return word

with open("README.md") as f:
  fl = f.readlines()
  i1 = f.index('<!--username:START-->\n')
  i2 = f.index('<!--username:END-->\n')
  
  user_name = generate(random.randint(3,11)) + '\n'
  fl = f[:i1+1] + [user_name] + f[i2:]
  print(fl)
# open("README.md",'w').write(out)
