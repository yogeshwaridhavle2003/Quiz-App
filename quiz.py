import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

        self.label = tk.Label(master, text="")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.check_button = tk.Button(master, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            self.label.config(text=self.questions[self.current_question_index].prompt)
        else:
            messagebox.showinfo("Quiz Finished", f"You got {self.score} out of {len(self.questions)} questions correct.")

    def check_answer(self):
        user_answer = self.entry.get()
        correct_answer = self.questions[self.current_question_index].answer

        if user_answer.lower() == correct_answer.lower():
            self.score += 1

        self.current_question_index += 1
        self.entry.delete(0, tk.END)
        self.display_question()

question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) Madrid\n(c) Rome\n\n",
    "What is 2 + 2?\n(a) 3\n(b) 4\n(c) 5\n\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Saturn\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b")
]

root = tk.Tk()
root.title("Quiz Application")

quiz_app = QuizApp(root, questions)

root.mainloop()
