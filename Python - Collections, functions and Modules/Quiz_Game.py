from quiz_operations import QuizOperations

# Function to display the menu
def display_menu():
    print("\n===== Quiz Game Menu =====")
    print("1. Add Question")
    print("2. View Questions")
    print("3. Delete Question")
    print("4. Play Quiz")
    print("5. Exit")

# Function to get user input with validation
def get_user_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

# Validation function for integer input
def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Validation function for Y/N input
def is_valid_confirmation(value):
    return value.lower() in ['y', 'n']

# Function to handle Quiz Master operations
def quiz_master_operations(quiz):
    question_id = get_user_input("Enter question ID: ", is_valid_integer)
    question = input("Enter the question: ")
    options = input("Enter options separated by commas: ").split(',')
    correct_option = get_user_input("Enter correct option: ", lambda x: x in options)

    quiz.add_question(question_id, question, options, correct_option)
    print("Question added successfully!")

    # Save questions to a text file
    with open("quiz_questions.txt", "a") as file:
        file.write(f"{question_id},{question},{','.join(options)},{correct_option}\n")

# Function to handle Quiz Cracker operations
def quiz_cracker_operations(quiz):
    quiz.view_questions()

# Function to play quiz
def play_quiz(quiz):
    # Load questions from the text file
    with open("quiz_questions.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            question_id, question, options, correct_option = map(str.strip, line.split(','))
            options = options.split(',')
            print(f"\nID: {question_id}, Question: {question}")
            print("Options:", ', '.join(options))

# Main program
if __name__ == "__main__":
    print("======   WELCOME TO TOPS QUIZ GAMING CHALLENGE   ======")
    print('''Select your role : 
                 -> Quiz Master  (Press 1)
                 -> Quiz Cracker (Press 2)
                 -> Exit (Press 0)''')

    role = get_user_input("Enter your role: ", lambda x: x in ['0', '1', '2'])

    quiz = QuizOperations()

    if role == '1':
        while True:
            display_menu()
            choice = get_user_input("Enter your choice: ", is_valid_integer)

            if choice == '1':
                quiz_master_operations(quiz)

            elif choice == '2':
                quiz_cracker_operations(quiz)

            elif choice == '3':
                question_id = get_user_input("Enter question ID to delete: ", is_valid_integer)
                confirmation = get_user_input("Are you sure you want to delete this question? (Y/N): ", is_valid_confirmation)

                if confirmation == 'y':
                    if quiz.delete_question(question_id):
                        print("Question deleted successfully!")
                    else:
                        print("Question ID not found.")

            elif choice == '4':
                play_quiz(quiz)

            elif choice == '5':
                print("Exiting the Quiz Game. Thank you!")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    elif role == '0':
        print("Exiting the Quiz Game. Thank you!")

    else:
        print("Invalid input. Please enter 0, 1, or 2 for your role.")
