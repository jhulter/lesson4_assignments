# Task 1

import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

times = ["Morning", "Afternoon", "Evening"]

for day in days:
    for time in times:
        print(f"On {day} {time} I felt {random.choice(moods)} ")
