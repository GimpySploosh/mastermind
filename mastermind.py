import random

repeating = True

SLOTNUM = 3
COLORS = ["1", "2", "3", "4"]

#  all possible code combinations
allComb = [[]]

count = 0


#  generate all possible code combinations
def generateComb(comb, slotsLeft):
  #  get rid of the original from allComb
  allComb.remove(comb)
  #  make new variations of the given combination with each variation
  #having a different color added to the end
  for color in COLORS:
    #  skips adding the color already in the combination,
    #if repeating is false
    if color in comb and repeating is False:
      continue
    else:
      newComb = comb + [color]
      allComb.append(newComb)
      #  recursion. As long as there are still slots to fill,
      #this function will continue to add variations unto itself
      if slotsLeft != 0:
        generateComb(newComb, slotsLeft - 1)


generateComb([], SLOTNUM - 1)

while True:
  count += 1

  #  forming guess
  guess = []

  # determining guess
  for i in range(len(allComb)):
    guess = allComb[random.randint(0, len(allComb) - 1)]
    #guess = allComb[0]

  print(allComb)

  print("")
  print(guess)

  print("")
  key = list(input("Enter key for the code: ").upper())
  key.sort()

  #  win condition
  if key.count("R") == SLOTNUM:
    break

  #  find the key for every code combination
  nextComb = []
  for code in allComb:
    tempKey = []
    #  count the number of times each color appears in the code
    colorCount = []
    if repeating:
      for color in guess:
        colorCount.append(code.count(color))

    for i in range(len(code)):
      #  red
      if guess[i] == code[i]:
        #  if repeating and the maximum amount of marked
        #colors are not yet reached, then add "R" into the
        #tempKey
        if repeating:
          if colorCount[i] > 0:
            tempKey += ["R"]
            colorCount[i] -= 1
          else:
            continue
        else:
          tempKey += ["R"]

      #  white
      elif guess[i] in code:
        if repeating:
          if colorCount[i] > 0:
            tempKey += ["W"]
            colorCount[i] -= 1
          else:
            continue
        else:
          tempKey += ["W"]

    tempKey.sort()
    print(code, tempKey, key)
    if tempKey == key:
      nextComb.append(code)
  allComb = nextComb

print("computer won in " + str(count) + " tries!")
