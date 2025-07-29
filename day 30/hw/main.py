# 2) მოცემულია სტრინგი: "Programming"

#     დაბეჭდეთ მხოლოდ პირველი 5 სიმბოლო.

#     • დაბეჭდეთ ბოლო 3 სიმბოლო.

#     • დაბეჭდეთ სტრინგი შებრუნებულად.

# 3) მოცემულია სია: fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
#   ჯერ სიიდან ამოიღეთ შუა სამი ელემენტი, შემდეგ დაბეჭდეთ სიის ყოველი მეორე ელემენტი.

# 4)  ცვლადში შეინახეთ სტრინგი, სადაც Alphabet-ის ყველა ასოს ჩაწერთ. 

#     • ამოიღეთ სტრინდიდან ყველა მესამე სიმბოლო Slicing-ის გამოყენებით.

#    • შებრუნებული სტრინგიდან ამოღეთ მხოლოდ ყოველი მეორე სიმბოლო.

# 5) მოცემულია სტრინგი: text = "IndexingAndSlicingIsPowerful"

# ამოიღეთ text ცვლადიდან სიტყვა "Slicing". შემდეგ შეაბრუნეთ და გამოიტანეთ შედეგის სახით ეკრანზე.

# 6) მოცემულია სტრინგი: word = "Programming"

#    • დაბეჭდეთ სტრინგი უკუღმა ისე, რომ გამოტოვებული იყოს ყოველი მეორე ასო.

#    • ამოჭერით სტრინგი შუა სამი ასო.

#    • შეაერთეთ მხოლოდ ლუწ ინდექსებზე მყოფი ასოები.

# 7) შექმენით ცვლადი alphabet = "abcdefghijklmnopqrstuvwxyz"

#  შექმენი სიტყვა "python" ამ სტრინგიდან ინდექსების კომბინაციით.

# 8) მოცემულია სია: nums = [0, 10, 20, 30, 40, 50, 60, 70]

#    • ამოჭერით სიიდან ბოლო სამი ელემენტი.

#    • ამოიღეთ ელემენტები 20-დან 50-ის ჩათვლით.

# 9) Level 29-ზე დაწყებული Html პროექტისთვის შეადგინეთ (მხოლოდ) Products სექციის კოდი, ჩემი მინიშნების გარეშე მოიფიქრეთ, თუ რა კომპონენტები უნდა დაამატოთ წიგნების გასაყიდ გვერდს. თქვენს მიერ აწყობილი გვერდი გასტილეთ CSS-ის გამოყენებით ცისფერ/ლურჯ თემაში, ფერების ასარჩევად გადადით რესურსებში ჩაგდებული საიტის ლინკზე. რომლის გვერდიც ყველაზე მეტად მომეწონება, იმაზე დაყრდნობით ავაგებ ჩვენი წიგნების საიტისთვის სტილსა და სტრუქტურას შემდეგ Html-ს გაკვეთილზე.

# წარმატებები:)


text = "Programming"

# პირველი 5 სიმბოლო
print(text[:5])  # 'Progr'

# ბოლო 3 სიმბოლო
print(text[-3:])  # 'ing'

# შებრუნებული სტრინგი
print(text[::-1])  # 'gnimmargorP'



fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# შუა სამი ელემენტის ამოღება (ინდექსებით 2,3,4)
middle_three = fruits[2:5]
print("შუა სამი:", middle_three)  # ['cherry', 'date', 'fig']

# სიის ყოველი მეორე ელემენტი (ინდექსები 0,2,4...)
every_second = fruits[::2]
print("ყოველი მეორე:", every_second)  # ['apple', 'cherry', 'fig']



alphabet = "abcdefghijklmnopqrstuvwxyz"

# ყველა მესამე სიმბოლო (0,3,6,9...)
every_third = alphabet[0::3]
print("ყველა მესამე სიმბოლო:", every_third)  # 'adgjmpsvy'

# შებრუნებული სტრინგიდან (reverse) ყოველ მეორე სიმბოლო
reversed_alphabet = alphabet[::-1]
every_second_from_reversed = reversed_alphabet[::2]
print("შებრუნებული, ყოველი მეორე:", every_second_from_reversed)  # 'zxvtrpnljhfdb'


text = "IndexingAndSlicingIsPowerful"

# "Slicing" ინდექსები 11-18 (18 - არ შედის)
slicing = text[11:18]

# შებრუნება
reversed_slicing = slicing[::-1]

print("Slicing:", slicing)  # Slicing
print("შებრუნებული:", reversed_slicing)  # gnicilS



word = "Programming"

# უკუღმა, გამოტოვებული ყოველი მეორე ასო
reverse_skip = word[::-2]
print("უკუღმა ყოველი მეორე:", reverse_skip)  # 'gnmro'

# შუა სამი ასო - 3 ინდექსი შუაში (len=11, შუა=5)
middle_three = word[4:7]
print("შუა სამი ასო:", middle_three)  # 'ram'

# ლუწ ინდექსებზე მყოფი ასოების შეერთება
even_index_letters = word[0::2]
print("ლუწ ინდექსები:", even_index_letters)  # 'Pormig'



alphabet = "abcdefghijklmnopqrstuvwxyz"

python_word = alphabet[15] + alphabet[24] + alphabet[19] + alphabet[7] + alphabet[14] + alphabet[13]
print("სიტყვა:", python_word)  # 'python'



nums = [0, 10, 20, 30, 40, 50, 60, 70]

# ბოლო სამი ელემენტი
last_three = nums[-3:]
print("ბოლო სამი ელემენტი:", last_three)  # [50, 60, 70]

# 20-დან 50-ის ჩათვლით ელემენტები (ინდექსები 2-5)
subset = nums[2:6]
print("20-დან 50 ჩათვლით:", subset)  # [20, 30, 40, 50]



