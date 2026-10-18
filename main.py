quiz = {"4-2 = ":"2",
        "9/3 = ":"3"}
count = 0
for question, answer in quiz.items():
    print(f"1 - suraq = {question}")

    user_answer = input("Zhauap engiz: ")

    if answer.lower() == user_answer.lower():
        print("Zauap durys!!!")
        count+=1
    else:print("Qate!")
print(f"\nSiz {count} suraqqa durys zhauap berdiniz")