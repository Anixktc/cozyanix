import tkinter as tk
from tkinter import messagebox

class MysteryGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🕵️ Mystery of the Haunted Mansion")
        self.root.geometry("700x500")
        self.root.configure(bg="black")

        self.story_text = tk.Text(root, wrap=tk.WORD, height=20, width=80, bg="black", fg="lime", font=("Consolas", 12))
        self.story_text.pack(padx=10, pady=10)

        self.input_field = tk.Entry(root, width=50, font=("Consolas", 12))
        self.input_field.pack(pady=5)
        self.input_field.bind("<Return>", lambda event: self.handle_input())

        self.submit_button = tk.Button(root, text="Submit", command=self.handle_input, bg="gray20", fg="white", font=("Consolas", 11))
        self.submit_button.pack()

        self.story_text.insert(tk.END, "🕵️ Welcome to the Mystery of the Haunted Mansion!\nType your detective name to begin...\n")
        self.player_name = ""
        self.stage = "get_name"

    def handle_input(self):
        user_input = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)

        if not user_input:
            self.story_text.insert(tk.END, "\n⚠️ Please enter something.\n")
            return

        if self.stage == "get_name":
            self.player_name = user_input
            self.story_text.insert(tk.END, f"\n🔍 Detective {self.player_name}, you've been called to solve the mystery!\n")
            self.story_text.insert(tk.END, "\nYou arrive at the mansion. The front door is locked. A keypad beside it reads:\n")
            self.story_text.insert(tk.END, "'The year this mansion was built holds the key.'\n")
            self.story_text.insert(tk.END, "Clue: The mansion was built in 1847.\n")
            self.stage = "puzzle_1"

        elif self.stage == "puzzle_1":
            if user_input == "1847":
                self.story_text.insert(tk.END, "\n✅ The door unlocks! You step inside the dark foyer...\n")
                self.story_text.insert(tk.END, "\nTo be continued... Add more stages in the code 🧩\n")
                self.stage = "done"
            else:
                self.story_text.insert(tk.END, "\n❌ Wrong code. Try again.\n")

        elif self.stage == "done":
            self.story_text.insert(tk.END, f"\n🎉 Well done, {self.player_name}! You've completed the prototype.\n")
        else:
            self.story_text.insert(tk.END, "\n🤖 No further stages yet. Add more in code!\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = MysteryGameGUI(root)
    root.mainloop()
