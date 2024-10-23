print("Hello, Welcome!")
name = input("Let me have your name please!: ")
serv = input(f"{name} How may we help you today?: ")
date = int(input("When do you want to do the exam: "))
qa = input("Are you enrolled in this university?: ")
age = int(input("How old are you?: "))


if age >= 18 or age <= 65:
        print("Great your age is eligible")

        if date >=10 or date <=25:
            print("There is still available seat on that date")

        if qa == "yes":
            print("We can make that happen")
        else:
            print("But, You need to fulfill certain conditions")

else:
    print("You need to be between 18 and 65 years old to partake in the exam and \n and enrolled in the university for the program of your choice  ")



