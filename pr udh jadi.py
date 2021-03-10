#tugas pengulangan (for and while)

print("for")
print("-------------------------------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print("\n")
print("while")
print("--------------------------------")
i = 0
while i < 6:
  i += 1
  if i == 0:
    continue
  print(i)
  if i == 0:
    break
  i += 0
