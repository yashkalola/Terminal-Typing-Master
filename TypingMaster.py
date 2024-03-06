import time
import json
import os
import random
from pynput import keyboard

class TypingMaster:
    def __init__(self):
        self.words = [
            "programming", "challenge", "keyboard", "python", "coding", "terminal",
            "developer", "leaderboard", "practice", "speed", "accuracy", "typing",
            "creative", "challenge", "language", "exercise", "inspiration", "innovation",
            "experience", "learning"
        ]
        self.leaderboard_file = "leaderboard.json"
        self.current_user = None
        self.results = []
        self.exit_flag = False

    def get_username(self):
        user_name = input("Enter your name: ")
        self.current_user = user_name

    def start_typing_test(self):
        input("Press Enter to start typing test...")
        print("\nTyping test starts now. Type the following words:\n")

        random_words = random.sample(self.words, len(self.words))
        words_to_type = " ".join(random_words)
        print(words_to_type)

        start_time = time.time()

        typed_words = input("\nType the words: ")

        while " ".join(typed_words.split()) != words_to_type:
            print("Incorrect! Please retype the words.")
            start_time = time.time()  # Reset the timer
            typed_words = input("Type the words again: ")

        end_time = time.time()
        self.calculate_wpm(start_time, end_time, words_to_type, typed_words)

    def calculate_wpm(self, start_time, end_time, words_to_type, typed_words):
        total_time = end_time - start_time
        total_words = len(words_to_type.split())  # Counting words in the given string
        correct_count = sum(1 for tw, ww in zip(typed_words, words_to_type) if tw == ww)

        wpm = (correct_count / 5) / (total_time / 60)  # Adjusted for 5 characters per word

        print("\nTyping test completed!\n")
        print(f"Your typing speed: {wpm:.2f} WPM")
        print(f"Total time taken: {total_time:.2f} seconds\n")

        if correct_count == total_words * 5:
            print("Congratulations! You typed all words correctly.")

        self.results.append({"name": self.current_user, "wpm": wpm, "time": total_time})
        self.save_results()

    def show_leaderboard(self):
        print("\nLeaderboard:")
        if os.path.exists(self.leaderboard_file):
            with open(self.leaderboard_file, 'r') as file:
                leaderboard = json.load(file)
                for entry in leaderboard:
                    print(f"{entry['name']}: {entry['wpm']} WPM - Time: {entry['time']:.2f} seconds")
        else:
            print("Leaderboard is empty.")

    def save_results(self):
        with open(self.leaderboard_file, 'w') as file:
            json.dump(self.results, file, indent=2)
    def on_press(self, key):
        try:
            if key.char == 'q' and (key.ctrl or key.meta):
                self.exit_flag = True
                return False
        except AttributeError:
            pass

    def run(self):
        self.get_username()

        while not self.exit_flag:
            print("\nChoose an option:")
            print("1. Start typing test")
            print("2. Show leaderboard")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.start_typing_test()
            elif choice == '2':
                self.show_leaderboard()
            elif choice == '3':
                self.exit_flag = True
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    typing_master = TypingMaster()

    with keyboard.Listener(on_press=typing_master.on_press) as listener:
        typing_master.run()

    print("Program ended.")

