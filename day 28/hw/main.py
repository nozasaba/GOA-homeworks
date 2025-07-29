# # 2) კომენტარი: 
# # Slicing Python-ში გამოიყენება სტრინგების, სიების და სხვა სქემების ნაწილი ამოსაღებად. 
# # ეს საშუალებას გვაძლევს გამოვიღოთ კონკრეტული ელემენტების სეგმენტი (ქვეპროდუქტი) ერთი მონაცემისგან მარტივად.

# # 3) რიცხვების სია და პირველი 5 რიცხვის ამოღება slicing-ით
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# first_five = numbers[0:5]  # ან უბრალოდ numbers[:5]
# print("პირველი 5 რიცხვი:", first_five)

# # 4) სიტყვიდან "Goal-Oriented Academy" გამოყვანა "Academy" გამოყენებით slicing
# text = "Goal-Oriented Academy"
# academy = text[14:]  # სიტყვა იწყება 14 ინდექსიდან
# print("Academy:", academy)

# # 5) სიტყვიდან "Goal-Oriented Academy" გამოყვანა "Oriented" გამოყენებით slicing
# oriented = text[5:13]  # "Oriented" არის ინდექსებზე 5-დან 12-მდე
# print("Oriented:", oriented)

# # 6) შენი გვარის პირველი, შუა და ბოლო ასოების გამოღება ინდექსირებით
# surname = "Nozadze"  # აქ ჩაწერე შენი გვარი
# first_letter = surname[0]
# last_letter = surname[-1]
# middle_letter = surname[len(surname)//2]  # შუა ასო
# print("გვარის პირველი ასო:", first_letter)
# print("გვარის შუა ასო:", middle_letter)
# print("გვარის ბოლო ასო:", last_letter)

# # 7) სია colors და Yellow-სა და Black-ის გამოღება
# colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
# selected_colors = [colors[1], colors[0]]  # Yellow და Black
# print("Yellow და Black:", selected_colors)

# # 8) სტრინგიდან "Hello" და "World!" გამოღება slicing-ით
# greeting = "Hello, World!"
# hello = greeting[0:5]  # "Hello"
# world = greeting[7:]   # "World!"
# print("Hello:", hello)
# print("World:", world)






numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_five = numbers[:5]  
print("პირველი 5 რიცხვი:", first_five)

text = "Goal-Oriented Academy"
academy = text[14:] 
print("Academy:", academy)


oriented = text[5:13]  
print("Oriented:", oriented)


surname = "Nozadze"  
first_letter = surname[0]
last_letter = surname[-1]
middle_letter = surname[len(surname)//2] 
print("გვარის პირველი ასო:", first_letter)
print("გვარის შუა ასო:", middle_letter)
print("გვარის ბოლო ასო:", last_letter)


colors = ["Black", "Yellow", "Blue", "Purple", "Orange"]
selected_colors = [colors[1], colors[0]] 
print("Yellow და Black:", selected_colors)


greeting = "Hello, World!"
hello = greeting[:5]  
world = greeting[7:]  
print("Hello:", hello)
print("World:", world)
