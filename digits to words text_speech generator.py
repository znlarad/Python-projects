#This program is for converting digits into words AND then it turns the numbers into voice
#This code is written by znl_arad

#using gtts
from gtts import gTTS
import os


#define the function
def convert_to_words(number):
    numbers = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }

    output = ""

    for char in number:
        if char.isdigit():
            output += numbers[char] + " "
        else:
            output += char + " not a digit "

    return output.strip()
#using tect to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    #saving the file
    tts.save("output.mp3")
    os.system("start output.mp3")  # Opens the new voice in computer's default mp3 player 

def main():
    try:
        number = input("Enter your phone number: ")
        result = convert_to_words(number)
        print("Number in words:", result)
        text_to_speech(result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
