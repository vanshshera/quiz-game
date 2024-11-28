questions = ("What is the Current Age Of Pranjay?",
             "Who Is The real father Of Saksham?",
             "What is Tanya's Favorite food ?",
             "In Which Subject Pranjay Got his Back?",
             "What is the name Of Kabir's GF?")

options = (("A.12","B.16","C.20","D.30"),
           ("A.God","B.Weeknd","C.no one knows","D.saksham"),
           ("A.Rajma Chawal","B.Chicken","C.White Sauce Pasta","D.Golgappe"),
           ("A.Maths","B.English","C.EVS","D.Hindi"),
           ("A.SAKSHI","B.PRIYA","C.KHUSHI","D.YASHI"))

answers = ("C","B","C","A","D")

guesses = []

score = 0

question_num = 0
print("------------------")
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct Biyach")
    else:
        print("Incorrect")
        print(f"The correct Answer is ->{answers[question_num]}")

    question_num += 1
print("------------------")


print("---------YOUR SCORE---------")
score = score/len(questions)*100
print(score )