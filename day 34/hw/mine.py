
words = []
n = int(input("რამდენი სიტყვა გინდა შეიტანო? "))
for _ in range(n):
    word = input("შეიყვანეთ სიტყვა: ")
    words.append(word)

print("შენი სიტყვები:")
for w in words:
    print(w)

num = int(input("შეიყვანეთ მთელი რიცხვი: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


days = []
count = int(input("რამდენი დღის სახელი გინდა შეიტანო? "))
for _ in range(count):
    day = input("შეიყვანეთ კვირის დღის სახელი: ")
    days.append(day)

print("ლუწი ინდექსის მქონე ელემენტები:")
for i in range(len(days)):
    if i % 2 == 0:
        print(days[i])
