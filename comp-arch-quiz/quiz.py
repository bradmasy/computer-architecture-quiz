import json
import random


AMOUNT_OF_QUESTIONS = 27
AMOUNT_OF_QUESTIONS_CHAPTER_4_AND_5 = 38
BEGINNING_OF_QUESTIONS = 1


def get_json_file(chapter_number):
    """
    Chooses which JSON File to read based on the users input.

    :param chapter_number: the chapter number the user provides
    :return: the corresponding JSON file
    """

    json_file = None
    if chapter_number == 1:
        json_file = "chapter_1.json"
    elif chapter_number == 2 or chapter_number == 3:
        json_file = "chapter_2_and_3_questions.json"
    elif chapter_number == 4 or chapter_number == 5:
        json_file = "chapter_4_and_5_questions.json"
    elif chapter_number == 6:
        json_file = "chapter_6_questions.json"
    elif chapter_number == 7 or chapter_number == 8:
        json_file = "chapter_7_and_8_questions.json"
    elif chapter_number == 9 or chapter_number == 10:
        json_file = "chapter_9_and_10_question.json"
    elif chapter_number == 11 or chapter_number == 13:
        json_file = "chapter_11_and_13_questions.json"
    elif chapter_number == 16:
        json_file = "chapter_16_questions.json"
    return json_file


def throw_exception(number):
    if number != number.is_integer():
        raise ValueError("Invalid type")


def parseJSON(filename):
    """
    Parses the json file to a string.

    :param filename: a string representing the name of a JSON file that we wish to parse
    :return: json file converted to a string
    """
    f = open(filename)
    json_string = json.load(f)

    return json_string


def create_question_number_list(json_file):
    """
    Generates a list of numbers to choose the question from.
    :return: a list of numbers ranging
    """
    question_num_list = []
    amount = len(json_file)

    for i in range(BEGINNING_OF_QUESTIONS, amount):
        question_num_list.append(i)
    return question_num_list


def shuffle_question_list(question_number_list):
    """
    Creates a new list of the question numbers in random order.
    :param question_number_list:
    :return:
    """
    new_list = []

    for i in range(len(question_number_list)):
        random_index = random.choice(question_number_list)
        question_number_list.remove(random_index)
        new_list.append(random_index)
    return new_list


def get_question(json_string, question_number):
    question = json_string[str(question_number)]["question"]
    print(question)
    print()
    return question_number


def get_options(question_number, json_string):
    options = dict(json_string[str(question_number)]["choices"])

    for key, answer in options.items():
        print(f"{key}: {answer}")

    print("--------------------------------")


def get_answer(json_string, question_number):
    question_number_string = str(question_number)
    answer_key = json_string["answer_key"][question_number_string]
    return answer_key


def compare_results(program_answer, user_answer, user_score):
    if program_answer == user_answer:
        print()
        print("correct answer")
        user_score += 1
    else:
        print()
        print("incorrect response")
        user_score += 0
    return user_score


def continue_quiz():
    continue_game = False
    next_question = str(input("would you like to continue? \"y\" for yes and \"n\" for no: "))
    print("---------------------------------------------")
    if next_question == "y":
        continue_game = True
    else:
        pass
    return continue_game


def ask_what_chapter():
    correct_value = True
    while correct_value:
        try:
            chapter_number = int(input("which chapter would you like to study? "))
            correct_value = False
        except ValueError:
            print("\nIncorrect Value: Must be an Integer\n")
    return chapter_number


def loop_through_questions(shuffled_list, user_score, json_string, quiz_question_count):
    i = 0
    while i < len(shuffled_list):
        q_num = get_question(json_string, shuffled_list[i])
        get_options(q_num, json_string)
        answer = get_answer(json_string, q_num)
        user_answer = str(input("what is your answer? "))
        user_score = compare_results(answer, user_answer, user_score)
        quiz_question_count += 1
        i += 1
        if continue_quiz():
            continue
        else:
            break
    return [user_score,quiz_question_count]


def ask_question(user_score, quiz_question_count):
    continue_match = False
    chapter_number = ask_what_chapter()
    print()
    json_file = get_json_file(chapter_number)
    json_string = parseJSON(json_file)
    question_number_list = create_question_number_list(json_string)
    shuffled_list = shuffle_question_list(question_number_list)
    user_score = loop_through_questions(shuffled_list, user_score, json_string, quiz_question_count)
    user_score_digits = user_score[0]
    quiz_question_count = user_score[1]

    return [continue_match, user_score_digits, quiz_question_count]


def main():
    print("running program")
    print("---------------------------------------------")

    user_score = 0
    quiz_question_count = 0
    take_quiz = True
    game = True

    while game:  # will continue to prompt for another chapter unless you exit

        while take_quiz:  # runs each chapter

            question_results = ask_question(user_score, quiz_question_count)
            user_score = question_results[1]
            take_quiz = question_results[0]
            quiz_question_count = question_results[2]
            print()
        next_decision = str(input("would you like to pick another chapter? type \"y\" to continue and \"n\" to exit "))
        print()
        if next_decision == "y":
            game = True
            take_quiz = True
        else:
            game = False

    print(f"your score is: {user_score} out of {quiz_question_count}")
    percentage = ((user_score/quiz_question_count) * 100)
    print(f"your percentage is {percentage:.2f}% ")


if __name__ == "__main__":
    main()
