# 2) მოიყვანეთ მაგალითები და ახსენით თუ რატომ არის სტრინგი - Immutable და სია - Mutable.
# ამასთანავე ახსენით ტუ რას ეწოდება Mutable და Immutable.

# 3) მომხმარებელს შემოატანინეთ თავისი სახელი, გვარი, ID ნომერი და ეროვნება. ეს ყოველივე შეინახეთ User_info ცვლადში. ჯერ მთლიანი სია დაბეჭდეთ, შემდეგ კი ინდექსინგის საშუალებით გამოიტანეთ სიის თითოეული ელემენტი ტერმინალში.

# 4) შექმენით Vending Machine პროგრამა.

# შექმენით Vending Machine სია სადაც მინიმუმ 10 ცალ პროდუქტს დაამატებთ. მომხმარებელი უნდა ირჩევდეს პროდუქტის ინდექსს და შემდეგ თქვენ პროდუქტის 
# დასახელება უნდა გამოუტანოთ ტერმინალში. (პირობაში დეტალები არ მიწერია, ასერომ ეცადეთ რაც შეიძლება დახვეწილი და მომხმარებლისთვის მოსახერხებელი 
# პროგრამა შექმნათ)

# 5) შექმენით Fruits სია: 
# Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
# სიის მეოთხე ელემეტი ჩაანაცვლეთ "Watermelon"-ით, მეორე ელემენტი კი "Pear"-ით. ტერმინალში დაბეჭდეთ სიის თავდაპირველი და საბოლოო სახე.

# 6) რამდენიმე ცვლადში შინახეთ სხვადასხვა სიტყვა. ამ სიტყვების გამოყენებით ააწყვეთ ერთი მთლიანი სიტყვა. მაგ.
# ("Moon", "light" -- "Moonlight")

name = "Giorgi"
name[0] = "B"   # ეს შეცდომას გამოიტანს

name = "Giorgi"
name = "B" + name[1:] 

names = ["Giorgi", "Nino", "Luka"]
names[0] = "Beka"
print(names)  # ['Beka', 'Nino', 'Luka']

name = input("Enter your name: ")
surname = input("Enter your surname: ")
user_id = input("Enter your ID number: ")
nationality = input("Enter your nationality: ")

User_info = [name, surname, user_id, nationality]

print("\nFull User Info List:")
print(User_info)

print("\nEach item individually:")
print("Name:", User_info[0])
print("Surname:", User_info[1])
print("ID:", User_info[2])
print("Nationality:", User_info[3])


Fruits = ["Strawberry", "Mango", "Melon", "Cherry"]
print("Original list:", Fruits)

Fruits[3] = "Watermelon"
Fruits[1] = "Pear"

print("Updated list:", Fruits)


part1 = "Moon"
part2 = "light"
part3 = "shine"

final_word = part1 + part2 + part3
print(final_word)  # Moonlightshine

