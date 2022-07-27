import requests
import json
import random

def getQuestion():
    r = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = json.loads(r.text)
    
    questionString = ""
    correctAnswer = ""
    difficulty = ""
    answerList = []

    for item in data['results']:

        for element in item['difficulty']:
            difficulty += element

        for element in item['incorrect_answers']:
            
            answerList.append(element)

        for element in item['correct_answer']:
            correctAnswer += element

        for element in item['question']:
    
            questionString += element


    answerList.append(correctAnswer)
    random.shuffle(answerList)

    return questionString, correctAnswer, answerList
           
getQuestion()


