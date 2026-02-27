colors = ["red","green","yellow","blue"]

for col in colors:
    print(col)


for i in range(10):
    print(i)


#example of break
print("-----------------------")
for i in range(5):
    if i == 3:
        break
    print(i)

#example of continue
print("-----------------------")
for i in range(5):
    if i == 3:
        continue
    print(i)