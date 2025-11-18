class Interrogator():
    def __init__(self,questions):
        self.questions=questions

    def __iter__(self):
        return self.questions.__iter__()
    
questions=['Q1 ?','Q2 ?','Q3 ?','Q4 ?']
onePerson=Interrogator(questions)

for question in onePerson:
    print(question)
