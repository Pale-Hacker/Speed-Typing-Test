import os
import time
import random

# --- #

Texts = [
    "Like a bridge over troubled water, I will lay me down."
    "I don't want a lot for Christmas, there is just one thing I need",
    "Every little thing gonna be all right.",
    "I know I'm not perfect, but at least I'm not fake.",
    "In the end, the love you take is equal to the love you make",
    "Yesterday, all my troubles seemed so far away. Now it looks as though they're here to stay. Oh, I believe in yesterday.",
    "I'm trying to hold my breath, let it stay this way, can't let this moment end. You set off a dream with me, getting louder now, can you hear it echoing?",
    "We found love in a hopeless place.",
    "Don't stop believin', hold on to that feelin'.",
    "I came in like a wrecking ball.",
    "I'm on the highway to hell.",
    "I'm just a small town girl, living in a lonely world.",
    "All the single ladies, now put your hands up.",
    "Cause baby you're a firework, come on show 'em what you're worth.",
    "I don't want to miss a thing.",
    "I will always love you.",
]  # You Can Add More ..

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print("""  _____                     _              _______          _                          _______        _   
 / ____|                   | |            |__   __|        (_)                        |__   __|      | |  
| (___  _ __   ___  ___  __| |   ______      | |_   _ _ __  _ _ __   __ _    ______      | | ___  ___| |_ 
 \___ \| '_ \ / _ \/ _ \/ _` |  |______|     | | | | | '_ \| | '_ \ / _` |  |______|     | |/ _ \/ __| __|
 ____) | |_) |  __/  __/ (_| |               | | |_| | |_) | | | | | (_| |               | |  __/\__ \ |_ 
|_____/| .__/ \___|\___|\__,_|               |_|\__, | .__/|_|_| |_|\__, |               |_|\___||___/\__|
       | |                                       __/ | |             __/ |                                
       |_|                                      |___/|_|            |___/                                 \n\nCreated By : Pale-Hacker\n""")


def Typing_Test():
    Text = random.choice(Texts)
    print(f"Type This Text : \n\n{Text}\n")
    Start_Time = time.time()
    User_Input = input()
    End_Time = time.time()
    Time_Taken = End_Time - Start_Time
    Correct_Characters = 0
    for i in range(min(len(Text), len(User_Input))):
        if Text[i] == User_Input[i]:
            Correct_Characters += 1
    Accuracy = (Correct_Characters / len(Text)) * 100
    Banner()
    print(f"Time Taken : {Time_Taken:.2f} Seconds")
    print(f"Accuracy : {Accuracy:.2f}%")
    input("\nPress \"Enter\" To Exit ! ")

# --- #


Banner()
Typing_Test()

# --- #
