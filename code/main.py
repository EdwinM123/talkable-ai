from datetime import datetime
import pyttsx3
import speech_recognition as sr 
import webbrowser
import wikipedia  
 
#browser stuff
chrome_path = r"C:\Program Files\Google\Chrome\Application\Chrome.exe" 
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

#speech recognition 
engine = pyttsx3.init();
voices = engine.getProperty("voices");
engine.setProperty('voices', voices[1].id); #0=guy 1=girl
#word to activate 
word = 'karen' 

def speak(text, rate =120):
    engine.setProperty('rate', rate);
    engine.say(text);
    engine.runAndWait();

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

#Wikipedia
def search_wikipedia(query=' ') :
    searchResults = wikipedia.search(query)
    if not searchResults:
        print("No wikipedia result")
        return "No result received"
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0]);
    print(wikiPage.title);
    wikiSummary = str(wikiPage.summary);
    return wikiSummary;

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
            #browser
            if query[0] == 'go' and query[0] == 'to':
                speak('opening');
                query = ' '.join(query[:2]);
                webbrowser.get('chrome').open_new(query);
            #Wiki
            if query[0] =='wikipedia' or query [0]=='search' and query[0]=='up' or query[0]=='search':
                query = ' '.join(query[1:]);
                speak("searching...")
                speak(search_wikipedia(query));
            #wolfram questions
            if query[0] == 'calculate' or query[0] == 'compute' or query[0] == 'computer' or query[0] == 'check':
                query = ' '.join(query[1:]);
                speak("calculating...")
                try: 
                    result = search_wikipedia(query)
                    speak(result) 
                    result = webbrowser.get('chrome').open_new(query)
                    speak(result)
                except:
                    speak('Unable to compute.')
            
            #end of my misery
            if query[0] == 'exit' or query[0]=='goodbye' or query[0]=='bye' or query[0]=='kys':
                speak("goodbye")
                break;
