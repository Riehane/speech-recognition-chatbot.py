
import speech_recognition as sr
import pyttsx3
import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone()

conversation = ""
user_name = "Reihane"
bot_name = "Reiahn assistant"

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("no longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        engine="davinci",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
