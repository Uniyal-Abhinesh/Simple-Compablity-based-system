import matplotlib.pyplot as plt


def calculate_compatibility(person1, person2):
    """
    Calculate compatibility percentage between two people based on their answers.

    Args:
        person1 (list): A list of answers for person 1.
        person2 (list): A list of answers for person 2.

    Returns:
        float: Compatibility percentage.
    """
    if len(person1) != len(person2):
        raise ValueError("Both individuals must answer the same number of questions.")

    matches = 0
    for answer1, answer2 in zip(person1, person2):
        if answer1 == answer2:
            matches += 1

    compatibility = (matches / len(person1)) * 100
    return compatibility


def get_person_answers(name, questions):
    """
    Collect answers from a person.

    Args:
        name (str): The person's name.
        questions (list): A list of questions.

    Returns:
        list: The person's answers.
    """
    print(f"\n{name}, please answer the following questions:")
    answers = []
    for question in questions:
        answer = input(f"{question} ")
        answers.append(answer.lower())  # Convert answers to lowercase for consistency
    return answers


def show_compatibility_graph(person1_name, person2_name, compatibility_score):
    """
    Display a bar graph representing compatibility between two people.

    Args:
        person1_name (str): The name of the first person.
        person2_name (str): The name of the second person.
        compatibility_score (float): Compatibility score as a percentage.
    """
    names = [person1_name, person2_name]
    values = [compatibility_score, 100 - compatibility_score]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, values, color=['#4CAF50', '#F44336'])
    plt.ylim(0, 100)
    plt.title("Compatibility Score", fontsize=16)
    plt.ylabel("Percentage (%)", fontsize=12)

    # Add percentage labels on bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f'{value:.2f}%', 
                 ha='center', va='bottom', fontsize=12, color='white')

    plt.show()


# Define questions for the compatibility test
questions = [
    "What is your favorite color? (e.g., red, blue, green)",
    "Do you prefer cats or dogs?",
    "What is your favorite season? (e.g., summer, winter)",
    "Do you enjoy outdoor activities? (yes/no)",
    "What is your favorite type of music? (e.g., pop, rock, classical)",
    "Would you prefer a movie date or a candlelight dinner? (movie/candlelight)",
    "What characteristic do you value most in a partner? (e.g., kind, tall, good looking)",
    "What is your preferred skin color for a partner? (e.g., fair, dark, tan, no preference)"
]

# Get answers from two people
person1_name = input("Enter the name of the first person: ")
person2_name = input("Enter the name of the second person: ")

person1_answers = get_person_answers(person1_name, questions)
person2_answers = get_person_answers(person2_name, questions)

# Calculate compatibility
try:
    compatibility_score = calculate_compatibility(person1_answers, person2_answers)
    print(f"\n{person1_name} and {person2_name}'s compatibility score is: {compatibility_score:.2f}%")

    # Show compatibility graph
    show_compatibility_graph(person1_name, person2_name, compatibility_score)

except ValueError as e:
    print(f"Error: {e}")