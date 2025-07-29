
print("კენტ რიცხვები 10-დან 45-ის ჩათვლით:")
for num in range(10, 46):
    if num % 2 != 0:
        print(num, end=' ')
print('\n')

print("ლუწ რიცხვები 20-დან 50-მდე:")
num = 20
while num <= 50:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
print()
