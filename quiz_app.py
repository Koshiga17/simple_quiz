class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option


def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        answer = int(input("Enter your answer (1, 2, 3, etc.): "))

        if answer == question.correct_option:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        print()

    print("Quiz completed!")
    print(f"You scored {score}/{total_questions}.")


# Define your questions here
question_1 = Question("What is the capital of France?",
                      ["London", "Paris", "Berlin", "Rome"],
                      2)

question_2 = Question("Who painted the Mona Lisa?",
                      ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Salvador Dalí"],
                      2)

question_3 = Question("What is the largest planet in our solar system?",
                      ["Mars", "Jupiter", "Earth", "Saturn"],
                      2)

# Add more questions if desired

# Create a list of questions
questions = [question_1, question_2, question_3]

# Run the quiz
run_quiz(questions)
