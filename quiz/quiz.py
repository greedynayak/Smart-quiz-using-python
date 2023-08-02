import tkinter as tk


def create_question(question, options, correct_option):
    return {
        "question": question,
        "options": options,
        "correct_option": correct_option,
    }


def display_question(question):
    feedback_label.config(text="", fg="black")  # Clear the feedback label
    question_label.config(text=question["question"], bg="#e0f2f1", fg="#37474f")
    for i, option in enumerate(question["options"], start=1):
        option_buttons[i - 1].config(text=f"{i}. {option}", bg="#b2dfdb", fg="#37474f")
        option_buttons[i - 1].config(state=tk.NORMAL)  # Enable the buttons


def is_correct_answer(question, answer):
    return question["correct_option"] == answer


def check_answer(answer, questions):
    global current_question, score
    if is_correct_answer(questions[current_question], answer):
        feedback_label.config(text="Correct!", fg="green")
        score += 1
    else:
        correct_option = questions[current_question]["correct_option"]
        feedback_label.config(
            text=f"Wrong! The correct answer was: {questions[current_question]['options'][correct_option]}", fg="red")

    current_question += 1
    if current_question < len(questions):
        root.after(2000, display_question, questions[current_question])
    else:
        display_score()


def display_score():
    question_label.config(text=f"Your score: {score}/{len(questions)}", bg="#e0f2f1", fg="#37474f")
    for button in option_buttons:
        button.config(state=tk.DISABLED)  # Disable the buttons


if __name__ == "__main__":
    questions = [
        create_question("What is the Capital of India?", ["Paris", "Berlin", "Delhi", "Madrid"], 2),
        create_question("Which Planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Mercury"], 1),
        create_question("What Movement did Srila Prabhupada start?", ["Iskcon", "Isha", "Brahmakumaris", "Beerbiceps"],
                        0),
    ]

    score = 0
    current_question = 0

    root = tk.Tk()
    root.title("Quiz Application")

    root.config(bg="#e0f2f1")

    question_label = tk.Label(root, text="", font=("Arial", 14))
    question_label.pack(pady=20)

    option_buttons = []
    button_color = "#b2dfdb"

    for i in range(4):
        button = tk.Button(root, text="", font=("Arial", 12), bg=button_color, fg="#37474f",
                           command=lambda i=i: check_answer(i, questions))
        option_buttons.append(button)
        button.pack(pady=5)

    feedback_label = tk.Label(root, text="", font=("Arial", 12))
    feedback_label.pack(pady=10)

    display_question(questions[current_question])

    root.mainloop()