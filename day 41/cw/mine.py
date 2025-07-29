# 1) კომენტარის სახით ახსენით რას აკეთებს len(), append(), insert() და pop() ფუნქციები

# 2) შექმენით სია და შეინახეთ  5 სახელი. მომხმარებელს შემოატანინეთ სახელი და დაამატეთ ამ სიაში. ბოლოს, დაბეჭდეთ ამ სიის სიგრძე და სიის განახლებული ვერსია.

# 3) შექმენით სია: fruits = ["Melon", "Orange", "Cantaloupe", "Watermelon", "Kiwi"]
# ამოაგდეთ სიიდან ბოლო ელემენტი და მესამე ინდექსზე ჩასვით "Pomegranate".

#len funqcia abrunebs siis sigrdzes
#append amatebs sityvas  siiis boloshi
#insert inserti amatebs sityvas mititebul chamonatvalze
#pop shis elements siidan

names = ["ana" , "luka" , "barbare", "data", "gio"]
new_name= input (" type name: ")
names.append(new_name)
print ("ordered list:", names)
print(len(names))

fruits = ["melon", "orange", "cantaloupe", "watermelon", "kiwi"]
fruits.pop()
print(fruits)