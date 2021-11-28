
from multi_choice_question_class import Question


question_prompt = [
    "What color are apples?\n (a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n (a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n (a) Green\n(b) Purple\n(c) Red\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c")
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question)
        print (answer)
        if answer == question_prompt:
            score += 1
    print ("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(question_prompt)


