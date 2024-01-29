import time

def offensive_mode(word_list_file):
    with open(word_list_file, 'r') as file:
        for word in file:
            word = word.strip()  # Remove leading/trailing whitespaces
            time.sleep(1)  # Add a delay of 1 second between words
            print(word)

def defensive_mode(user_input, word_list_file):
    with open(word_list_file, 'r') as file:
        word_list = [line.strip() for line in file]
        if user_input in word_list:
            print(f'The password "{user_input}" is recognized.')
        else:
            print(f'The password "{user_input}" is NOT recognized.')

def main():
    print("Select mode:")
    print("1: Offensive; Dictionary Iterator")
    print("2: Defensive; Password Recognized")

    mode = input("Enter mode (1 or 2): ")

    if mode == '1':
        word_list_file = input("Enter word list file path: ")
        offensive_mode(word_list_file)

    elif mode == '2':
        user_input = input("Enter a string: ")
        word_list_file = input("Enter word list file path: ")
        defensive_mode(user_input, word_list_file)

    else:
        print("Invalid mode. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
