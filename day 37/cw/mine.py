# # 1) მომხმარებელს შემოატანინეთ მთელი რიცხვი და დაწერეთ პროგრამა, რომელიც ამოწმებს:

# • თუ რიცხვი დადებითია, დაბეჭდოს: "the number is positive"
# • თუ უარყოფითია, დაბეჭდოს: "the number is negative"
# • თუ ნულია, დაბეჭდოს: "the number is zero"

# 2) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი. იქამდე გამოუტანეთ "incorrect password" სანამ მომხმარებელი სწორად არ შემოიტანს პაროლს. სწორად შემოტანის შემთხვევაში გამოიტანეთ "correct password" (გამოიყენეთ while loop)


num = int(input("Enter your number : "))

if num > 0:
    print("the number is possitive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

correct_password = "2008"

user_input = input("enter password : ")

while user_input != correct_password:
    print("inorrect password")
    user_input = input("enter password: ")
    print("correct password")