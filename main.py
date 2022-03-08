handle = open("copperfield.txt", "r")

text = ""
for n in handle:
  n = n.replace("\n", "")
  text = text + n
  print(n)

f.close()