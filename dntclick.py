import time
import os

# ASCII art representations for different buttons
BIG_RED_BUTTON = """
   ****   
 *      * 
*  RED   * 
 *      * 
   ****   
"""

SMALL_BUTTON = """
 *  
* S *
 *  
"""

PENGUIN = """
  ___
 (o o) 
  > ^ <
"""

MEDIUM_BUTTON = """
  ***  
 * M * 
  ***  
"""

GREEN_BUTTON = """
  ****  
 *GREEN* 
  ****  
"""

BLUE_BUTTON = """
  **** 
 *BLUE* 
  **** 
"""

WHITE_BUTTON = """
  ****  
 *WHITE* 
  ****  
"""

# Store the sequence of messages (same as the JavaScript speek function)
messages = [
    "DO NOT PRESS",
    "*Ahem*\nDO NOT PRESS",
    "... you pressed it again.\nOkay punk, press it again.",
    "Yeah, that's it.\nCome on, one more time.",
    "Again.",
    "Do it.",
    "Okay, now you've had your fill.\nStop clicking.",
    "You see, this is why\nwe can't be friends.",
    "Grr... now you've asked for it.\nDo NoT pReSs ThE bUtToN!",
    "You seem to be immune to\nmy mind control.",
    "Time for Plan B.\nPress it. You know you want to.",
    "Mwahahaha! Now let's see\nyou press it! LOSER!",  # small button
    "...this displeases me.",  # back to default
    "HA! I have replaced the button\nwith this penguin. Now what are you\ngoing to do?",  # penguin
    "...I hate you.",  # back to default
    "In that \"cut off your head with a\ntoothbrush\" kind of way.",
    "Quick! What's that behind you?!",
    "Which one is it?\nNot so smart now, are ya?",  # three buttons
    "You're a clever one.\nTime for Round 2.",  # back to default
    "You're a clever one.\nTime for Round 2.",  # thirty-two buttons
    "HAHAHAHAHAHA!",  # one-twenty-eight buttons
    "...",  # back to default
    "Okay Okay. You can press the button.\nI don't care.",
    "No really, I don't care anymore.",
    "I'm doing this just to entertain you.",
    "Really.",
    "Do you like cartoons?",
    "...and paint?",
    "Cartoons and Paint?",
    "Well you should.",
    "Pick a colour.",
    "Green. Perfect.",
    "Press the red button.",  # colors_red
    "Press the green button",  # colors_green
    "Press the blue button",
    "See, you just can't trust me.\nOr can you?",  # back to default
    "You know, I'm glad we get\nto spend so much time together.",
    "Doesn't it make you want to stop\nclicking big red buttons?",
    "No seriously.",
    "Look deep inside you.",
    "Deeper.",
    "DEEPER!",
    "What if I told you that that the next\ntime you press the button, the world\nwill explode?",
    "See. You could have been\ndead right there.",
    "And there.",
    "You know, eventually\nI'll stop letting you get away with this.",
    "The world is going to explode\nand all you care about is pressing buttons",
    "Okay, this time the world will\nexplode. I guarantee.",
    "BOOM!\nYou're dead.",
    "That wasn't very smart now was it?",
    "Everyone's dead. Even you.",
    "I'm not. I'm just text.",
    "But you're dead.",
    "Ha! Dead-face!",
    "Stop clicking.",
    "Have I ever told you how much I hate you?",
    "Well I do.",
    "I'm gonna start talking upside down\nif you click one more time.",
    "¿noʎ uɐɔ 'ʍou ǝɯ pɐǝɹ ʇ,uɐɔ ¡ɐɥ",  # upsidedown text
    "¿ʎɐʍʎuɐ ǝɯ pɐǝɹ oʇ ʇuɐʍ ʇ,upıp noʎ ¿ʇɐɥʍ",
    "¡noʎ ʍoɥs ןן,ı 'uǝɥʇ ןןǝʍ",
    "",  # back to default text
    "",  # white button
    "You really are stubborn.",  # back to default
    "Stop clicking. Please.",
    "See look. You've reduced me\nto begging. So please stop.",
    "PLEASE!!!!",
    "I'll give you a nickel",
    "Dime?",
    "Quarter?",
    "Aww come on! Just stop!",
    "That does it! Time to\nunleash my master plan!",
    "BEHOLD!\nThe awesome power of javascript animation!",  # animated
    "H8!",  # back to default
    "Let's get funky!",  # funky (15 buttons)
    "I'll bet you're starting to wonder\nwhy you've been doing this\nfor so long.",  # back to default
    "Like jeez, all you've been doing is\nclicking a red button.",
    "How lame is that?",
    "But there is a bonus to all this",
    "But it's a secret.\nSo I can't tell you.",
    "I got you going didn't I?",
    "You should've seen the look\non your face! HA!",
    "But seriously, there is a secret.\nThere's been one the whole time.",
    "You've been busy clicking away at this big red button...",
    "...when all the while a little white\nbutton has watched your every move",
    "MWAHAHAHAHAHA!",
    "HAHAHA!",
    "BWAHAA!",
    "MWAAAAH!!",
    "HAHA!",
    "hehe!",
    "lol",
    "rofl",
    "roflmao",
    "roflmaoqxz",
    "and so on and so forth",
    "...",
    "*whistles*",
    "Find it yet?",
    "Look harder! It's right under your nose.",
    "I know where it is.\nBut I'll never tell.",
    "Or maybe I will...",
    "But you gotta stop clicking the\nBig Red Button first!",
    "Stop.",
    "Now.",
    "Fine, I won't tell you\nthe secret.",
    "Go ahead. Try to find it yourself.\nYou'll never find it.",
    "Well you might... but the odds\nare against you.",
    "~",
    "What's your favorite letter?",
    "Mine is the squiggly!",
    "~",
    "Find it yet?",
    "No?",
    "Then stop clicking and I'll tell you.",
    "You know what?",
    "POOF! It's gone!",  # small2
    "Has anyone ever slapped you?",  # back to default
    "Cuz I will.",
    "Really I will.",
    "It won't hurt though.",
    "Cuz you're dead.",
    "D-E-D",
    "Remember? You went and blew up\nthe entire planet!",
    "Thought I'd forget about that\ndidn't you?",
    "But an elephant never forgets!",
    "...or something along those lines.",
    "You killed everyone.",
    "Sikko.",
    "What would you're mother say?",
    "That's right... feel bad.",
    "The world is null and you're to blame.",
    "I'd recommend suicide,\nbut you're dead already.",
    "So there's only one thing left that you can do...",
    "Stop clicking the button.",
    "Dude, you're dead.\nWhat are you gaining from this?",
    "Okay, everytime you click, you\nget sent to a lower layer of hell.\n(You're in layer 1: Limbo)",
    "Welcome to layer 2\n(Lust)",
    "3\n(Gluttony)",
    "4\n(Greed)",
    "5\n(Wrath)",
    "6\n(Heresy)",
    "7\n(Violence)",
    "8\n(Fraud)",
    "9\n(Treachery)",
    "BOOM!\nYou've exploded Hell.",
    "I hope you're happy.",
    "Heavens gone too.\nThat's how smooth you are.",
    "No you're dead, and there's\nno heaven or hell.",
    "How does it feel?\nYou've condemned the world to limbo.",
    "I once shot a man for being in limbo.",
    "...or was he doing the limbo?",
    "Meh, Tomato Tomahto",
    "This is getting boring isn't it?",
    "But you can't stop!",
    "You want to end this.\nYou want to leave you're computer.",
    "But you can't!",
    "You need to see if there's a pot of gold\nat the end of the rainbow!",
    "But I've already told you how to\nfind the pot of gold",
    "Follow the white rabbit.",
    "...erm, button.",
    "Remember the hidden button?",
    "Or are you so self-centered you forgot about that too?",
    "I could just keep you here all day\nif I wanted.",
    "You're in my world now.",
    "No matter how much you\nhate it, you have to press the button.",
    "again...",
    "and again...",
    "and again.",
    "You just keep hoping something\ngood will come of this.",
    "Sure I could tell you if I wanted\nto, but I'm not gonna.",
    "You decided to keep clicking.\nSo I'm gonna enjoy it.",
    "I mean, there's nothing else to enjoy",
    "You blew it all up remember?",
    "You're probably wondering who I am",
    "Well let me tell you a tale about myself",
    "One day, I was walking home from\n work and I saw a small little house.",
    "I knocked on the door out of curiousity\nto see if anyone was home.",
    "The door opened.",
    "But no one was there.",
    "I went inside to check it out\nand found nothing...",
    "...nothing but a little metal box.",
    "So I opened it.",
    "Inside the box was a layer of\nfoam protecting it's contents",
    "I removed the foam are there it was...",
    "...",
    "... ...",
    "ZZZzzzzzz",
    "zzzzZZZZzzzz",
    "ZZZZzzzZZZZ",
    "Huh?",
    "Oh! Right! The story!",
    "So there I was, holding this\nlittle metal box in my hands.",
    "The top was open and sitting\ninside was this...",
    "Big Red Button.",
    "And do you know what it said?",
    "Oh I'll tell you what it said.\nIt said..."
]

# Simulate button states
current_button = "default"
num = 0

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_button():
    global current_button
    if current_button == "small":
        print(SMALL_BUTTON)
    elif current_button == "penguin":
        print(PENGUIN)
    elif current_button == "three":
        print("1. " + BIG_RED_BUTTON)
        print("2. " + BIG_RED_BUTTON)
        print("3. " + BIG_RED_BUTTON)
    elif current_button == "thirtytwo":
        for i in range(1, 33):
            print(f"{i}. " + MEDIUM_BUTTON)
    elif current_button == "onetwentyeight":
        for i in range(1, 129):
            print(f"{i}. " + SMALL_BUTTON)
    elif current_button == "colors_red":
        print("1. " + BIG_RED_BUTTON)
        print("2. " + GREEN_BUTTON)
        print("3. " + BLUE_BUTTON)
    elif current_button == "colors_green":
        print("1. " + GREEN_BUTTON)
        print("2. " + BIG_RED_BUTTON)
    elif current_button == "animated":
        print(BIG_RED_BUTTON + " (Moving!)")
    elif current_button == "funky":
        for i in range(1, 16):
            print(f"{i}. " + BIG_RED_BUTTON)
    elif current_button == "small2":
        print(SMALL_BUTTON)
    elif current_button == "w":
        print(WHITE_BUTTON)
    else:
        print(BIG_RED_BUTTON)

def change_button(to):
    global current_button
    current_button = to
    clear_screen()
    print(messages[num])
    display_button()
    if to in ["three", "thirtytwo", "onetwentyeight", "colors_red", "colors_green", "funky"]:
        print("Enter '!press #' where # is the number of the correct button (e.g., !press 1)")
    else:
        print("Enter '!press' to continue")

def main():
    global num
    clear_screen()
    print(messages[0])
    display_button()
    print("Enter '!press' to continue")

    while True:
        user_input = input("> ").strip()
        
        if user_input == "!press" and current_button not in ["three", "thirtytwo", "onetwentyeight", "colors_red", "colors_green", "funky"]:
            num += 1
            if num >= len(messages):
                num = 0
            clear_screen()
            print(messages[num])
            display_button()
            print("Enter '!press' to continue")
        elif user_input.startswith("!press ") and current_button in ["three", "thirtytwo", "onetwentyeight", "colors_red", "colors_green", "funky"]:
            try:
                choice = int(user_input.split()[1])
                if current_button == "three" and choice in [1, 2, 3]:
                    num += 1
                    change_button("")  # Back to default after three
                elif current_button == "thirtytwo" and choice in range(1, 33):
                    num += 1
                    change_button("onetwentyeight")  # Progress to onetwentyeight
                elif current_button == "onetwentyeight" and choice in range(1, 129):
                    num += 1
                    change_button("")  # Back to default
                elif current_button == "colors_red" and choice in [1, 2, 3]:
                    num += 1
                    if choice == 1:
                        change_button("colors_green")
                    else:
                        change_button("")  # Wrong choice, back to default
                elif current_button == "colors_green" and choice in [1, 2]:
                    num += 1
                    if choice == 1:
                        change_button("")  # Correct choice, back to default
                    else:
                        change_button("")  # Wrong choice, back to default
                elif current_button == "funky" and choice == 10:
                    num = 75  # Hard-coded jump as in original
                    change_button("")  # Back to default
                else:
                    print("Invalid choice. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Use '!press #' with a valid number.")
        elif user_input == "!press" and current_button == "w":
            print("eek! You found me!")
            num += 1
            change_button("")  # Back to default
        else:
            print("Invalid input. Use '!press' or '!press #' for multiple-choice.")

        # Handle button changes based on num
        if num == 11:
            change_button("small")
        elif num == 12:
            change_button("")
        elif num == 13:
            change_button("penguin")
        elif num == 14:
            change_button("")
        elif num == 17:
            change_button("three")
        elif num == 18:
            change_button("")
        elif num == 19:
            change_button("thirtytwo")
        elif num == 20:
            change_button("onetwentyeight")
        elif num == 21:
            change_button("")
        elif num == 32:
            change_button("colors_red")
        elif num == 33:
            change_button("colors_green")
        elif num == 34:
            change_button("")
        elif num == 62:
            change_button("w")
        elif num == 63:
            change_button("")
        elif num == 72:
            change_button("animated")
        elif num == 73:
            change_button("")
        elif num == 74:
            change_button("funky")
        elif num == 75:
            change_button("")
        elif num == 116:
            change_button("small2")
        elif num == 117:
            change_button("")

if __name__ == "__main__":
    main()