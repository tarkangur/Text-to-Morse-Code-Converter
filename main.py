alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z", "Ç", "Ğ", "İ", "Ö", "Ş", "Ü", "0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", ".", ",", "?", "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", '"', "$", "@",
            "¿", "¡", " "]

morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                  "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
                  "-.-..", "--.-.", ".-..-", "---.", ".--..", "..--", "-----", ".----", "..---", "...--", "....-",
                  ".....", "-....", "--...", "---..", "----.", ".-.-.-", "--..--", "..--..", ".----.", "-.-.--",
                  "-..-.", "-.--.", "-.--.-", ".-...", "---...", "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-",
                  ".-..-.", "...-..-", ".--.-.", "..-.-", "--...-", "/"]


def to_morse(input_text):
    morse_text = ""
    for char in input_text:
        if char in alphabet:
            morse_text += morse_alphabet[alphabet.index(char)] + " "
        else:
            morse_text += "#"
    print(morse_text)


def to_text(morse_text):
    message = ""
    for char in morse_text.split():
        if char in morse_alphabet:
            message += alphabet[morse_alphabet.index(char)]
    print(message)


def translator():
    run = "y"
    while run == "y":
        text_type = input("what is your message type? Please write 'morse' or 'text':").lower()
        if text_type == 'text':
            text = input("Type your message:\n").upper()
            to_morse(text)
            break
        elif text_type == 'morse':
            text = input("Type your message:\n").upper()
            to_text(text)
            break
        else:
            print("Please write correctly")
            break
    run = input("Do you want to translate another message? Type 'y' or 'n': ").lower()
    if run == 'y':
        translator()
    else:
        print('Have a good day')
        exit()

if __name__ == "__main__":
    translator()
