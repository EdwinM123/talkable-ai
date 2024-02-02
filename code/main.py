from datetime import datetime
import pyttsx3
import speech_recognition as sr 
import webbrowser
import wikipedia 
import wolframalpha

#speech recognition 
software = pyttsx3.init();
voices = software.getProperty("voices");
software.setProperty('voices', voices[0].id); #0=guy 1=girl
#word to activate 
word = 'computer' 
def speak(text, rate =120):
    software.setProperty('rate', rate);
    software.say(text);
    software.runAndWait();

def parseCommand():
    listening=sr.Recognizer();
    print("listening for a command");

    with sr.Microphone() as source:
        listening.pause_threshold = 2;
        input_speech = listening.listen(source);

    try:
        print('recognizing speech...')
        query = listening.recognize_google(input_speech, language='en_gb')
        print(f"the input speech was: {query}");
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

#main loop
if __name__ == '__main__':
    speak('all systems nominal.')

    while True:
        query = parseCommand().lower().split()

        if query[0] == word:
            query.pop(0);
            if query[0] == 'say':
                if 'hello' in query:
                    speak('greetings');
                else:
                    query.pop(0)
                    speech=" ".join(query);
                    speak(speech)

