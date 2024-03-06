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
