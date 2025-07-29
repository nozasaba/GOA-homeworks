# 2) ჩამოწერეთ პირობითი განცხადებების შემადგენელი ყველა Keyword-ი, თითოეულს თან დაურთეთ განმარტება და თქვენი სიტყვებით ახსენით თუ რატომ/რა შემთხვევებში არის elif keyword-ი საჭირო.

# 3) ცვლადში შეინახეთ თქვენი ასაკი. შემდეგ მომხმარებელს შემოატანინეთ თავისი ასაკი. თუ თქვენი გვარები დაემთხვევა გამოიტანეთ "We are the same age", სხვა შემთხვევაში - "We are not the same age".

# 4) დააკვირდით მოცემულ flowchart-ს, ახსენით მისი მუშაობის პრინციპი. მისი მიხედვით Vscode-ში დაწერეთ პროგრამა და აღწერეთ რა შედეგს გამოიტანს კოდი იმ შემთხვევაში, როდესაც მომხმარებელი არის 14 წლის და არ არის სტუდენტი.

# if	ამოწმებს პირობას. თუ პირობა მართალია (True), შესრულდება შესაბამისი კოდი.
# elif	"else if"-ის შემოკლებაა. გამოიყენება მაშინ, როცა if პირობა არ შესრულდა, მაგრამ გვსურს სხვა პირობის შემოწმება.
# else	საბოლოო ალტერნატივაა. შესრულდება მაშინ, როცა არც if და არც elif პირობა არ არის მართალი.


# if პირობა1:
#     # შესრულდება თუ პირობა1 მართალია
# elif პირობა2:
#     # შესრულდება მხოლოდ თუ პირობა1 არ არის მართალი და პირობა2 არის მართალი
# elif პირობა3:
#     # შემოწმდება შემდეგი პირობა
# else:
#     # ყველაფერი დანარჩენი


    # ჩემი ასაკი
my_age = 20

# მომხმარებლის ასაკის შეყვანა
user_age = int(input("Enter your age: "))

# შედარება
if my_age == user_age:
    print("We are the same age")
else:
    print("We are not the same age")

# მომხმარებლის ასაკი
age = int(input("Enter your age: "))

# სტუდენტობა
is_student = input("Are you a student? (yes/no): ")

if age >= 18:
    print("Adult")
else:
    if is_student.lower() == "yes":
        print("Student minor")
    else:
        print("Minor")


number = int(input("Please enter a positive number: "))

while number <= 0:
    print("The number must be positive!")
    number = int(input("Try again. Enter a positive number: "))

print("Thank you! You entered:", number)
