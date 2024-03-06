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