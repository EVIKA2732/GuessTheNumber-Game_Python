print("Pick a number from 1 to 100.")
print("I Will make a guess")
print ("If I'am right, type 'Y'.")
print ("If the number is heigher than my guess, type 'h'.")
print("If it's lower, type 'I.")

import random, time
time.sleep(2)

ans = True
tries = 0
guess  = random.randnit(1.100)
low = 1
hight = 100
def ans(h):
  low = guess + 1
while ans !="y":
  write = "Is it" + str(guess) +"?"
  ans = input(write)
  if ans not in ("y", "I", "h"):
    print("Huh ?")
    continue
    tries += 1
    if ans == "y":
      print("I got it in", tries, "attempts.")
      elif ans == "h":
        low = guess + 1
        guess = random.randnit(low, high)
        elif ans == "I":
          high = guess - 1
          guess = random.randnit(low, high)
