overall_score = 0

# title of quiz
print("sport trivia")

print()
# question 1
print("which of these sports are not currently in the olympics? ")
print("a. fencing")
print("b. archery")
print("c. surfing")
print("d. cricket")
answer_one = input("answer: ")

if answer_one.lower() == "d":
    print("correct!")
    overall_score += 1
    print("overall score:", overall_score)
else:
    print("incorrect.")
    print("correct answer: cricket")
    print("overall score:", overall_score)

print()
# question 2
print("running is the oldest sport in the world ")
print("a. true")
print("b. false")
answer_two = input("answer: ")

if answer_two.lower() == "a":
    print("correct!")
    overall_score += 1
    print("overall score:", overall_score)
else:
    print("incorrect.")
    print("correct answer: true")
    print("overall score:", overall_score)

print()
# question 3
print("how many players per team are allowed on the field in soccer? ")
answer_three = input("answer: ")

if answer_three == "11":
    print("correct!")
    overall_score += 1
    print("overall score:", overall_score)
else:
    print("incorrect.")
    print("correct answer: 11")
    print("overall score:", overall_score)

print()
# question 4
print("what is the most viewed sport in usa? ")
print("a. soccer")
print("b. baseball")
print("c. american football")
print("d. basketball")
answer_four = input("answer: ")

if answer_four == "c":
    print("correct!")
    overall_score += 1
    print("overall score:", overall_score)
else:
    print("incorrect.")
    print("correct answer: c")
    print("overall_score:", overall_score)

print()
# question 5
print("golf is canada's national sport")
print("a. true")
print("b. false")
answer_five = input("answer: ")

if answer_five == "b":
    print("correct!")
    overall_score += 1
    print("overall score:", overall_score)
else:
    print("incorrect.")
    print("correct answer: b")
    print("overall_score:", overall_score)

# final score and closing
print("final score:", overall_score)
print("thanks for playing!")
