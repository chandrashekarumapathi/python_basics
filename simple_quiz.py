import random


class Quiz:
    def __init__(self):
        self.ask_question()

    @staticmethod
    def generate_random(upper):
        r = random.randint(0, upper)
        return r

    def get_answer(self):
        num1 = self.generate_random(10)
        num2 = self.generate_random(10)
        answer = num1 * num2
        return num1, num2, answer

    def ask_question(self):
        var = True
        while var:
            num1, num2, answer = self.get_answer()
            question = input(f'What is {num1} * {num2} ?\n')
            if question.isdigit():
                if int(question) == answer:
                    print("Correct answer!!!")
                    choice = input("Do you want to continue? Y/N")
                    if choice == 'Y':
                        var = True
                    else:
                        var = False
                else:
                    print("Wrong answer. Please try again!!")
            else:
                print('Please enter a number, not anything else!!!')


quiz = Quiz()




