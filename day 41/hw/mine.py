
words = input("შეიყვანეთ რამდენიმე სიტყვა, რომლებიც ერთმანეთისგან განაწილებულია სივრცით: ").split()
print("სიის სიგრძე:", len(words))


my_list = []
for i in range(3):
    data = input(f"შეიყვანეთ მონაცემი №{i+1}: ")
    my_list.append(data)
print("სია:", my_list)


fruits = ["apple", "banana", "cherry", "date"]
new_fruit = input("შეიყვანეთ ახალი ხილი: ")
fruits.insert(2, new_fruit)
print("განახლებული სია:", fruits)


vehicles = ["car", "bike", "bus", "train", "plane"]
vehicles.pop(4)
vehicles.pop()   
print("დაბეჭდილი სია:", vehicles)
