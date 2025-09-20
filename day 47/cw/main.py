# 1) შექმენით ფუნქცია სახელად - filter_positives, რომელიც არგუმენტად მიიღებს სიას, თქვენი მიზანი იქნება არგუმენტად გადაცემული სიიდან მხოლოდ დადებითი რიცხვები დააბრუნოთ.

# 2) შექმენით ფუნქცია, სახელად - filter_negatives. ფუნქციას არგუმენტად სია უნდა გადასცეთ. მან კი პასუხად მხოლოდ უარყოფითი რიცხვები უნდა დააბრუნოს.

# 3) დაწერეთ ფუნქცია, რომელსაც გადაეცემა პარამეტრი - სახელი. ფუნქციის მიზანი იქნება ნებისმიერი სახელი გადაიყვანოს Uppercase ასოებად.

def filter_positives(numbers):
result = []
for num  in numbers:
if num > 0:
result.append(num)
return result
print(filter_positives([1, -2, 3, 0, -5, 7]))



def fillter_positives(numbers):
result = []
for num in numbers:
if num < 0:
result.append(num)
return result 
print(fillter_positives([1, -2, 3, 0, -5, 7]))

def uppercase(name):
return name.upper()
print (uppercase())