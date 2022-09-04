"""Assigment 2

1) Create a list of names and use a for loop to output the length of each name (len() ).
2) Add an if  check inside the loop to only output names longer than 5 characters.
3) Add another if  check to see whether a name includes a “n”  or “N”  character.
4) Use a while  loop to empty the list of names (via pop() )
  """

names = [
    "Yasmin",
    "Safa",
    "Ashraf",
    "Mercy",
    "Lydia",
    "Suzanna",
    "Divine",
    "Myah",
    "Davey",
    "Alexa",
    "Alex",
]

for name in names:
    if len(name) > 5:
        print(name + " has " + str(len(name)) + " characters")
    if "n" in name or "N" in name:
        print(name + " has an 'N' character")

while len(names) > 0:
    name = names.pop()
    print(name)

print("NO MORE NAMES")
