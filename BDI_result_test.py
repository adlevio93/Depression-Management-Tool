# The purpose of this application is the part of my M.A.R.C.H.E.S concept (Military and Responder Comprehensive Health Evaluation Service), designed to
#create a mental health platform for Military And Responders.

#This portion uses the Beck Depression Index, a globally recognized tool
#to determine indication of an  depression diagnosis. This is in honor of Uncle Steve Cortez,
#and my late, dear friend, Patrick Charles Berg, who suffered from schizophrenia and died from suicide in 2015.





# Portion below asks the # QUESTIONS:

#QUESTION 1:
question_1 = """
Question 1: Sadness:
0: I do not feel sad.
1: I feel sad.
2: I am sad all the time and I can't snap out of it.
3: I am so sad and unhappy that I can't stand it.
"""
print(question_1)

#inputs the answer
ans_1 = int(input(" "))

print("You answered: ", ans_1)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_1 = ans_1

#Question 2

#prints the question
question_2 = """
Question 2: Pessimism:
0: I am not discouraged about my future.
1: I feel more discouraged about my future than I used to.
2: I do not expect things to work out for me.
3: I feel my future is hopeless and will only get worse.
"""
print(question_2)


#inputs the answer
ans_2 = int(input(" "))

print("You answered: ", ans_2)
#selects which answer to print based on user's input using if, elif, while conditions.

#saves the answer from the imput above for the end result
result_2 = ans_2

#QUESTION 3:
question_3 = """
Question 3: Past Failure:
0: I do not feel like a failure.
1: I have failed more than I should have.
2: As I look back, I see a lot of failures.
3: I feel I am a total failure as a person.
"""
print(question_3)


#inputs the answer
ans_3 = int(input(" "))

print("You answered: ", ans_3)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_3 = ans_3


question_4 = """
Question 4: Loss of Pleasure:
0: I get as much pleasure as I ever did from the things I enjoy.
1: I don't enjoy things as much as I used to.
2: I get very little pleasure from the things I used to enjoy.
3: I can't get any pleasure from the things I used to enjoy.
"""
print(question_4)

#inputs the answer
ans_4 = int(input(" "))

print("You answered: ", ans_4)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_4 = ans_4

#Question 5
question_5 = """
Question 5: Gulity Feelings:
0: I don't feel particularly guilty.
1: I feel guilty over many things I have done.
2: I feel quite guilty most of the time.
3: I feel guilty all of the time.
"""
print(question_5)

#inputs the answer
ans_5 = int(input(" "))

print("You answered: ", ans_5)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_5 = ans_5

#Question 6
question_6 = """
Question 6: Punishment Feelings:
0: I don't feel I am being punihed.
1: I I feel I may be punished.
2: I expect to be punished.
3: I feel I am being punished.
"""
print(question_6)

#inputs the answer
ans_6 = int(input(" "))

print("You answered: ", ans_6)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_6 = ans_6

#Question 7
question_7 = """
Question 7: Self-Dislike:
0: I feel the saame about myself as ever.
1: I have lost confidence in myself.
2: I am disappointed in myself.
3: I dislike myself.
"""
print(question_7)

#inputs the answer
ans_7 = int(input(" "))

print("You answered: ", ans_7)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_7 = ans_7

#Question 8
question_8 = """
Question 8: Self Criticalness:
0: I don't criticize or blame myself more than usual.
1: I am more critical of myself than I used to be.
2: I criticize myself for all my faults.
3: I blame myself for everything bad that happens.
"""
print(question_8)

#inputs the answer
ans_8 = int(input(" "))

print("You answered: ", ans_8)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_8 = ans_8


#Question 9
question_9 = """
Question 9: Suicidal Thoughts or Wishes:
0: I don't have any thoughts of killing myself.
1: I have thoughts of killing myself, but I would not cary them out.
2: I would like to kill myself.
3: I would kill myself if I had the chance.
"""
print(question_9)

#inputs the answer
ans_9 = int(input(" "))

print("You answered: ", ans_9)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_9 = ans_9


#Question 10
question_10 = """
Question 10: Crying:
0: I don't cry anymore than I used to.
1: I cry over every little thing.
2: Icry over every little thing.
3: I feel like crying, but I can't.
"""
print(question_10)

#inputs the answer
ans_10 = int(input(" "))

print("You answered: ", ans_10)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_10 = ans_10

#Question 11
question_11 = """
Question 11: Agitation:
0: I am no more restless or wound up than usual.
1: I feel more restless or wound up than usual.
2: I am so restless or agitated, it's hard to stay still.
3: I am so restless or agitated that I have to keep moving or doing something.
"""
print(question_11)

#inputs the answer
ans_11 = int(input(" "))

print("You answered: ", ans_11)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_11 = ans_11

#Question 12
question_12 = """
Question 12: Loss of Interest:
0: I have not lost interest in other people or activities.
1: I am less interessted in other people or things than before.
2: I have lost most of my interest in other people or things.
3: It's hard to get interested in anything.
"""
print(question_12)

#inputs the answer
ans_12 = int(input(" "))

print("You answered: ", ans_12)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_12 = ans_12

#Question 13
question_13 = """
Question 13: Indecisiveness:
0: I make decisions about as well as ever.
1: I find it more difficult to make decisions than usual.
2: I have much greater difficulty in making decisions than I used to.
3: I have trouble making any decisions.
"""
print(question_13)

#inputs the answer
ans_13 = int(input(" "))

print("You answered: ", ans_13)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_13 = ans_13

#Question 14
question_14 = """
Question 14: Worthlessness:
0: I do not feel worthless.
1: I don't consider myself as worthwhile and useful as I used to.
2: I feel more worthless as compared to others.
3: I feel utterly worthless.
"""
print(question_14)

#inputs the answer
ans_14 = int(input(" "))

print("You answered: ", ans_14)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_14 = ans_14

#Question 15
question_15 = """
Question 15: Loss of energy:
0: I have as much energy as ever.
1: I have less energy than I used to have.
2: I don't have enough energy to do very much.
3: I don't have enough enrgy to do anything.
"""
print(question_15)

#inputs the answer
ans_15 = int(input(" "))

print("You answered: ", ans_15)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_15 = ans_15

#Question 16
question_16 = """
Question 16: Sleeping Pattern:
0: I have not experienced any change in my sleep.
1: I sleep somewhat more than usual.
2: I sleep somewhat less than usual.
1.5: I sleep a lot more than usual.
2.5: I sleep a lot less than usual.
3: I sleep most of the day.
4: I wake up 1-2 hours early and can't get enough sleep.
"""
print(question_16)

#inputs the answer
ans_16 = int(input(" "))

print("You answered: ", ans_12)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_16 = ans_16

#Question 17
question_17 = """
Question 17: Irritability:
0: I am not more restless or wound up than usual.
1: I feel more restless or wound up than usual.
2: I am so restless or agitated, it's hard to stay still.
3: I am so restless or agitated that I have to keep moving or doing something.
"""
print(question_17)

#inputs the answer
ans_17 = int(input(" "))

print("You answered: ", ans_17)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_17 = ans_17

#Question 18
question_18 = """
Question 18: Changes in Appetite:
0: I have not experienced any change in my appetite.
1: My appetite is somewhat less than usual.
2: My appetite is much less than before.
2.5: My appetite is much greater than usual.
1.5: I have no appetite at all.
3: I crave food all the time.
"""
print(question_18)

#inputs the answer
ans_18 = int(input(" "))

print("You answered: ", ans_18)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_18 = ans_18

#Question 19
question_19 = """
Question 19: Concentration Difficulty:
0: I can concentrate as well as ever.
1: I can't concentrate as well as usual.
2: It's hard to keep my mind on anything for very long.
3: I find I can't concentrate on anything.
"""
print(question_19)

#inputs the answer
ans_19 = int(input(" "))

print("You answered: ", ans_19)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_19 = ans_19

#Question 20
question_20 = """
Question 20: Tiredness or Fatigue:
0: I am no more tired or fatigued than usual.
1: I get more tired or fatigued more easily than usual.
2: I am too tired or fatigued to do a lot of the things I used to do.
3: I am too tired or fstigued to do most of the things I used to do.
"""
print(question_20)

#inputs the answer
ans_20 = int(input(" "))

print("You answered: ", ans_20)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_20 = ans_20


#Question 21
question_21 = """
Question 21: Agitation:
0: I have not noticed any recent change in my interest in sex.
1: I am less interested in sex than I used to be.
2: I am much less interested in sex now.
3: I have lost interest in sex completely.
"""
print(question_21)

#inputs the answer
ans_21 = int(input(" "))

print("You answered: ", ans_21)

#this variable  belowstores the answer as a result which will be added
# at the end of the questionairre
result_21 = ans_21


#final depression score

final_depression_score = (result_1 + result_2 + result_3 + result_4 +
result_5 + result_6 + result_7 + result_8 + result_9 + result_10 + result_11 + result_12
+ result_13 + result_14 + result_15 +result_16 +result_17 + result_18 + result_19 +
result_20 +result_21)

print("You scored ", final_depression_score)

if final_depression_score <= 9:
    print("You are not depressed");
elif final_depression_score <= 18:
    print("You are experiencing mild to moderate depression symptoms. It might help to talk to a therapist.");
elif final_depression_score <= 29:
    print("You have moderate to severe symptoms of depression. You may want to seek professional guidance.");
elif final_depression_score < 30:
    print("You have severe depression and should seek professional help. Please contact your primary care physician for further instruction.");

    start()
