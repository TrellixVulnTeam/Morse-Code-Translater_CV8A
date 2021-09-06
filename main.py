from morse_code import text_to_morse, morse_to_text


def text_to_morse_translate():
    text_input = input("\nWrite the text to be translated into morsecode:\n").upper()
    letter_list = [i for i in text_input]
    try:
        code_list = [text_to_morse[i] for i in letter_list]
    except KeyError:
        print("Sorry, can only translate letters and numbers. Try again")
        text_to_morse_translate()
    else:
        print(" ".join(code_list))
        user_input = input("\nWant to translate something else? (y/n): ").lower()
        if user_input == "y":
            console_translator()
        else:
            print("Goodbye!")


def morse_to_text_translate():
    code_input = input("\ndah = . ¦ dit = - ¦ short gap = space ¦ medium gap = 2* space\n"
                       "Example: ... --- ...  ... --- ... = SOS SOS\nType: ")
    code_list = code_input.split(" ")
    try:
        letter_list = [morse_to_text[i] for i in code_list]
    except KeyError:
        print("Wrong Input. Try again.")
        morse_to_text_translate()

    else:
        print("".join(letter_list))
        user_input = input("\nWant to translate something else? (y/n): ").lower()
        if user_input == "y":
            console_translator()
        else:
            print("Shutting down...")


def console_translator():
    user_input = input("\n1. Text to Morsecode or 2. Morsecode to Text? Type 1 or 2: ")
    if user_input == "1":
        text_to_morse_translate()
    elif user_input == "2":
        morse_to_text_translate()
    else:
        print("Input is whether 1 or 2. Let's try this again:")
        console_translator()


def main_program():
    print("\nWelcome to the Morsecode Translater")
    console_translator()


main_program()
