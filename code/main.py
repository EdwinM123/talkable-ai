from datetime import datetime
import pyttsx3
import speech_recognition as sr 
import webbrowser
import wikipedia 
import wolframalpha

#speech recognition 
software = pyttsx3.init();
voices = software.getProperty("voices");
software.setProperty('voices', voices[0]);