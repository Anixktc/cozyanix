import tkinter as tk
from tkinter import messagebox

class MysteryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🕵️ Mystery of the Haunted Mansion")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a1a")

        self.story_text = tk.Text(root, wrap=tk.WORD, height=18, width=90, bg="#111", fg="white", font=("Consolas", 12), state=tk.DISABLED)
        self.story_text.pack(pady=10)

        self.input_frame = tk.Frame(root, bg="#1a1a1a")
        self.input_frame.pack()

        self.input_label = tk.Label(self.input_frame, text="Your answer:", fg="white", bg="#1a1a1a", font=("Consolas", 11))
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_field = tk.Entry(self.input_frame, width=40, font=("Consolas", 11))
        self.input_field.pack(side=tk.LEFT)

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.handle_input, font=("Consolas", 11))
        self.submit_button.pack(side=tk.LEFT, padx=5)

        self.inventory_label = tk.Label(root, text="Inventory: ", fg="lime", bg="#1a1a1a", font=("Consolas", 11))
        self.inventory_label.pack(pady=5)

        self.reset_game()

    def reset_game(self):
        self.player_name = ""
        self.current_level = 0
        self.max_levels = 5
        self.inventory = []
        self.solved_puzzles = 0
        self.stage = "get_name"
        self.update_story("🕵️ Welcome to the Mystery of the Haunted Mansion!\nEnter your detective name to begin:")

    def update_story(self, text):
        self.story_text.config(state=tk.NORMAL)
        self.story_text.insert(tk.END, f"\n{text}\n")
        self.story_text.config(state=tk.DISABLED)
        self.story_text.see(tk.END)

    def update_inventory(self):
        items = ', '.join(self.inventory) if self.inventory else "Empty"
        self.inventory_label.config(text=f"Inventory: {items}")

    def handle_input(self):
        user_input = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)

        if self.stage == "get_name":
            self.player_name = user_input if user_input else "Detective"
            self.update_story(f"🔍 Welcome, {self.player_name}! Let's begin your investigation...")
            self.stage = "level_1"
            self.level_one()

        elif self.stage == "level_1":
            if user_input == "1847":
                self.update_story("✅ The door unlocks! You enter the mansion.")
                self.solved_puzzles += 1
                self.stage = "level_2"
                self.level_two()
            else:
                self.update_story("❌ Incorrect code. Try again.\nClue: The mansion was built in 1847.")

        elif self.stage == "level_2":
            if user_input.lower() == "echo":
                self.update_story("✅ Correct! The chest opens and reveals a key.")
                self.inventory.append("Mansion Key")
                self.update_inventory()
                self.solved_puzzles += 1
                self.stage = "level_3"
                self.level_three()
            else:
                self.update_story("❌ Wrong. Hint: It's a sound without a body.")

        elif self.stage == "level_3":
            expected = ["night", "is", "when", "most", "dangerous"]
            words = user_input.lower().split()
            if words == expected:
                self.update_story("✅ 'Night is when most dangerous.' A hidden compartment opens with a map.")
                self.inventory.append("Mansion Map")
                self.update_inventory()
                self.solved_puzzles += 1
                self.stage = "level_4"
                self.level_four()
            else:
                self.update_story("❌ Incorrect sentence. Try again.\nUse these words: NIGHT, IS, WHEN, MOST, DANGEROUS")

        elif self.stage == "level_4":
            if user_input == "3":
                self.update_story("✅ You chose ⚧ Ankh - the symbol of life. The door opens.")
                self.solved_puzzles += 1
                self.stage = "level_5"
                self.level_five()
            else:
                self.update_story("❌ Wrong door. Hint: Symbol of life is ⚧. Enter 3.")

        elif self.stage == "level_5":
            if user_input.lower() == "thursday":
                self.update_story("✅ Correct! Thursday is 3 days after Monday.")
                self.solved_puzzles += 1
                self.stage = "end"
                self.end_game()
            else:
                self.update_story("❌ Incorrect. 3 days after Monday? Try again.")

    def level_one(self):
        self.update_story("\n📍 Level 1: The mansion is locked. A keypad reads: 'The year this mansion was built holds the key.'\nClue: 1847")

    def level_two(self):
        self.update_story("\n📍 Level 2: A riddle on a chest reads:\n'I speak without a mouth and hear without ears. I have no body, but come alive with wind. What am I?'")

    def level_three(self):
        self.update_story("\n📍 Level 3: Rearrange these words into a sentence:\nNIGHT, IS, WHEN, MOST, DANGEROUS")

    def level_four(self):
        self.update_story("\n📍 Level 4: You see 3 doors with symbols:\n1. ⚡ Lightning (Energy)\n2. ☠ Skull (Death)\n3. ⚧ Ankh (Life)\n\nChoose the correct door number (1/2/3):")

    def level_five(self):
        self.update_story("\n📍 Final Level: A puzzle box asks:\nIf today is Monday, and the ghost appears every 3 days, on what day will it appear again?")

    def end_game(self):
        result = f"\n🎉 CASE SOLVED, {self.player_name}!\nYou solved {self.solved_puzzles} out of {self.max_levels} puzzles."
        if self.solved_puzzles == 5:
            result += "\n🏆 Perfect score! You're a master detective!"
        elif self.solved_puzzles >= 4:
            result += "\n🥇 Great work! You're almost perfect."
        elif self.solved_puzzles >= 3:
            result += "\n🥈 Good effort!"
        else:
            result += "\n🥉 Keep practicing to improve."

        self.update_story(result)
        self.update_inventory()

        self.input_frame.pack_forget()
        tk.Button(self.root, text="Play Again", command=self.restart, font=("Consolas", 11)).pack(pady=10)

    def restart(self):
        for widget in self.root.pack_slaves():
            widget.destroy()
        self.__init__(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    game = MysteryGame(root)
    root.mainloop()
