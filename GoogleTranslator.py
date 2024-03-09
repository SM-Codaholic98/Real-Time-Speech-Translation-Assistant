import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

language_mapping = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "chinese": "zh",
    "japanese": "ja",
    "korean": "ko",
    "arabic": "ar",
    "russian": "ru",
    "portuguese": "pt",
    "italian": "it",
    "dutch": "nl",
    "swedish": "sv",
    "norwegian": "no",
    "danish": "da",
    "finnish": "fi",
    "greek": "el",
    "polish": "pl",
    "turkish": "tr",
    "hindi": "hi",
    "bengali": "bn",
    "punjabi": "pa",
    "urdu": "ur",
    "thai": "th",
    "vietnamese": "vi",
    "indonesian": "id",
    "malay": "ms",
    "filipino": "fil",
    "swahili": "sw",
    "slovak": "sk",
    "czech": "cs",
    "hungarian": "hu",
    "romanian": "ro",
    "bulgarian": "bg",
    "serbian": "sr",
    "croatian": "hr",
    "ukrainian": "uk",
    "lithuanian": "lt",
    "latvian": "lv",
    "estonian": "et",
    "albanian": "sq",
    "macedonian": "mk",
    "slovenian": "sl",
    "icelandic": "is",
    "maltese": "mt",
    "irish": "ga",
    "welsh": "cy",
    "gujarati": "gu",
    "tamil": "ta",
    "telugu": "te",
    "kannada": "kn",
    "marathi": "mr",
    "oriya": "or",
    "assamese": "as",
    "maithili": "mai",
    "bhojpuri": "bh",
    "nepali": "ne",
    "sinhala": "si",
    "burmese": "my",
    "khmer": "km",
    "lao": "lo",
    "tibetan": "bo",
    "uzbek": "uz",
    "tajik": "tg",
    "pashto": "ps",
    "kurdish": "ku",
    "kazakh": "kk",
    "kyrgyz": "ky",
    "turkmen": "tk",
    "mongolian": "mn",
    "azerbaijani": "az",
    "georgian": "ka",
    "armenian": "hy",
    "samoan": "sm",
    "tongan": "to",
    "fijian": "fj",
    "hawaiian": "haw",
    "maori": "mi",
    "chamorro": "ch",
    "marshallese": "mh",
    "palauan": "pw",
    "tahitian": "ty",
    "kiribati": "ki",
    "nauruan": "na",
    "cook islands maori": "mi",
    "sesotho": "st",
    "setswana": "tn",
    "siswati": "ss",
    "tswana": "tn",
    "venda": "ve",
    "xhosa": "xh",
    "zulu": "zu",
    "yoruba": "yo",
    "hausa": "ha",
    "igbo": "ig",
    "kinyarwanda": "rw",
    "lingala": "ln",
    "somali": "so",
    "tigrinya": "ti",
    "wolof": "wo",
    "amharic": "am",
    "oromo": "om",
    "fulah": "ff",
    "kikuyu": "ki",
    "kirundi": "rn",
    "sango": "sg",
    "shona": "sn",
    "twi": "tw",
    "zulu": "zu"
}


def get_input_language():
    return language_mapping.get(input("Enter the input language (default is Hindi) : ").lower(), 'hi')


def get_output_language():
    return language_mapping.get(input("Enter the output language (default is English) : ").lower(), 'en')


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print("You said : ", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio !!")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None
    

def translate_text(text, input_lang, output_lang):
    translated_text = Translator().translate(text, src = input_lang, dest = output_lang)
    return translated_text.text


def speak_text(text, lang):
    tts = gTTS(text = text, lang = lang)
    tts.save('output.mp3')
    os.system('start output.mp3')
    
    
ans = 'y'
while ans.lower() == 'y':
    input_lang = get_input_language()
    output_lang = get_output_language()
    
    input_text = recognize_speech()
    if input_text:
        translated_text = Translator().translate(input_text, src = input_lang, dest = output_lang)
        print("Translated text : ", translated_text.text)
        speak_text(translated_text.text, output_lang)
    else:
        print("## YOU HAVE NOT SPOKEN ANYTHING ##")
    
    print()
    ans = input("Press 'y/Y' to speak again : ")
    print()