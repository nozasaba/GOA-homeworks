# 2) მომხმარებელს შემოატანინეთ მისი ქალაქის, უბნის, კორპუსის და სართულის შესახებ ინფორმაცია (რომლებიც უნდა შეინახოთ ცალ-ცალკე ცვლადებში). მაგ. city = "Tbilisi", District = "Gldani" და ა.შ. საბოლოოდ print() ბრძანების საშუალებით ტერმინალში გამოიტანეთ მომხმარებლის სრული მისამართი.

# 3) მომხმარებელს შემოატანინეთ ასაკი და f სტრინგის გამოყენებით დაუბეჭდეთ მსგავსი ფორმატის წინადადება: 
# "You are ასაკი years old".

# 4) შექმენით ორი ცვლადი: Num1 და Num2. ორივე ცვლადში შინახეთ input-ი, სადაც მომხმარებელმა სასურველი რიცხვები უნდა შემოიტანოს. ამ ოპერაციის დასრულების შემდეგ სცადეთ რომ Num1-სა და Num2-ს შორის განახორციელოთ მათემატიკური ოპერაცია და დააკვირდით ტერმინალში შედეგს. ახსენით თქვენი აზრით რატომ მივიღეთ ასეთი შედეგი.

# 5) მეოთხე დავალების ანალოგიურად - სცადეთ მომხმარებლის მიერ შემოტანილ ორ რიცხვს შორის შეასრულოთ ყველა მათემატიკური ოპერაცია, რომელიც აქამდე ვისწავლეთ. ამ შემთხვევაშიც დააკვირდით შედეგს და ეცადეთ თქვენი სიტყვებით ახსნათ მიღებული რესულტატი.

# 6) Paint-ის საშუალებით შექმენით წრიული დიაგრამა, სადაც გექნებათ სამი კატეგორია: Input, Output და საერთო. Input-ში ჩასვით ყველა ის მოწყობილობა, რომლებიც Input-ის მაგალითია, Output-ში ის მოწყობილობები ჩასვით, რომლებიც Output-ის მაგალითებია, ხოლო საერთო კატეგორიაში ჩაწერეთ მოწყობილობები, რომლებიც როგორც Input-ს ასევე Output-საც ეკუთვნის. (Paint-ში დახატული დიაგრამა დასქრინეთ და გადაიტანეთ Day 08 homework ფოლდერში.)

# 7) გადახედეთ ჩანაწერს თავიდან - განსაკუთრებით მიაქციეთ ყურადღება იმ მომენტებს, სადაც ავხსენი Input/Output და f სტრინგის ფორმატი.


town = input ("Enter your town: ")
corps = input ("Enter your corps: ")
district = input ("Enter your district: ")
floor = input ("Enter your floor: ")

print (f"user town is {town} user corps is {corps} user district is {district} and user floor is {floor}")

num1 = input ("Enter your number: ")
num2 = input ("Enter your number: ")

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2)

user_age = input("enter your age: ")
print(f"the user's age is {user_age}.")

