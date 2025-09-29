# 1) დაწერეთ ფუნქცია, რომელსაც გადასცემთ ინტეჯერების სიას არგუმენტად. პასუხად დააბრუნეთ სიაში არსებული რიცხვების საშუალო არითმეტიკული.

# 2) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს სტრინგს.
# ფუნქციამ უნდა დაითვალოს მოცემულ სტრინგში ხმოვნების რაოდენობა.

# 3) დაწერეთ ფუნქცია და გადაეცით არგუმენტად სია.
# ფუნქციამ სიის თითოეული ელემენტი უნდა დააბრუნოს კვადრატში



def average(lst):
    if len(lst) == 0:
        return 0   
    return sum(lst) / len(lst)



def count_vowels(s):
    vowels = "aeiouAEIOUაეიოუ"  
    return sum(1 for ch in s if ch in vowels)



def square_elements(lst):
    return [x ** 2 for x in lst]



print(average([2, 4, 6, 8]))        
print(count_vowels("Programming"))  
print(count_vowels("გამარჯობა"))   
print(square_elements([1, 2, 3, 4]))
