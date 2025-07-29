# 2)
nums = [10, 20, 30, 40, 50, 60]
print("პირველი ელემენტი:", nums[0])       # 10
print("ბოლო ელემენტი:", nums[-1])         # 60
print("რიცხვები 30 და 40:", nums[2:4])    # [30, 40]

# 3)
word = "Programming"
print("პირველი ასო:", word[0])           # 'P'
print("ბოლო ასო:", word[-1])             # 'g'
print('"gram" slicing-ით:', word[4:8])    # 'gram'
print("სიტყვა შებრუნებულად:", word[::-1])  # 'gnimmargorP'

# 4)
sentence = input("შეიყვანეთ წინადადება: ")
first_last = sentence[0] + sentence[-1]
print("პირველი და ბოლო ასოების ნაერთი:", first_last)
print("უკუღმა წინადადება:", sentence[::-1])

# 5)
lst = [1, 2, 3, 4, 5]
print("სიის თავდაპირველი სახე:", lst)
index = int(input("რომელ ინდექსზე გინდათ ჩანაცვლება? (0-4): "))
value = input("რა მნიშვნელობით უნდა შეიცვალოს? ")
lst[index] = value
print("შეცვლილი სია:", lst)
print("სიის ბოლო სახე:", lst)

# 6)
lst = [1, 2, 3, 2, 1]
if lst == lst[::-1]:
    print("Symmetric")
else:
    print("Not symmetric")

# 7)
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
mean = sum(numbers) / len(numbers)
total_sum = sum(numbers)
print(f"The arithmetic mean of this list is: {mean}")
print(f"The sum of all numbers in this list is: {total_sum}")
