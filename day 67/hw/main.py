# 1) დაწერეთ ფუნქცია reverse_lst, რომელიც მიიღებს სიას და დააბრუნებს მის შებრუნებულ ვერსიას.

# 2) დაწერეთ პირველი დავალების ანალოგი ფუნქცია სტრინგებზე, სახელად reverse_str.

# 3) შექმენით ფუნქცია double, რომელიც მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც ყველა რიცხვი გაორმაგებულია.

# 4) დაწერე ფუნქცია sum_of_digits, რომელიც მიიღებს რიცხვს და დააბრუნებს მის ციფრთა ჯამს (მაგ. 123 → 6).

# 5) დაწერე ფუნქცია divisors, რომელიც მიიღებს რიცხვს და დააბრუნებს მის ყველა გამყოფს.
#    მაგ. მოცემულია რიცხვი 4. 4-ის გამყოფებია: 1, 2, 4. შესაბამისად ამ რიცხვის გამყოფებს აბრუნებთ სიის სახით --> [1, 2, 4]
#    12 -> [1, 2, 3, 4, 6, 12]
#    45 -> [1, 3, 5, 9, 15, 45]

# 6) შექმენით ფუნქცია max, რომელსაც არგუმენტად გადასცემთ რიცხვების სიას და პასუხად დააბრუნებს ამ რიცხვებიდან მაქსიმალურს.

# 7) შექმენით ფუნქცია min, რომელსაც არგუმენტად გადასცემთ რიცხვების სიას და პასუხად დააბრუნებს ამ რიცხვებიდან მინიმალურს.



def reverse_lst(lst):
    return lst[::-1]


def reverse_str(s):
    return s[::-1]

def double(lst):
    return [x * 2 for x in lst]


def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))


def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def max_num(lst):
    maximum = lst[0]
    for x in lst:
        if x > maximum:
            maximum = x
    return maximum

def min_num(lst):
    minimum = lst[0]
    for x in lst:
        if x < minimum:
            minimum = x
    return minimum



print(reverse_lst([1, 2, 3, 4]))    
print(reverse_str("python"))         
print(double([1, 2, 3]))              
print(sum_of_digits(123))            
print(divisors(12))                   
print(max_num([3, 8, 1, 9, 2]))       
print(min_num([3, 8, 1, 9, 2]))       
