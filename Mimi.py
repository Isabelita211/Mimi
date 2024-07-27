import speech_recognition as sr #reconocimiento de voz
import pyttsx3 #voz de la ia
from pyttsx3.voice import Voice
import pywhatkit #busqueda en internet
import datetime #hora
import wikipedia
import pyjokes #bromas

name = 'Mimi'

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice_path = 'C:\\Users\\ISABELA\\Music\\'

#cargar el archivo de voz
engine.save_to_file('', voice_path)
engine.runAndWait()

#Cargar la voz
voice = pyttsx3.voice.Voice(
    name = 'custom_voice',
    id = 'custom_voice',
    languages = 'es',
)

voices.append(voice) #Agregar voz personalizada a la lista

engine.setProperty('voice','custom_voice')

def talk(text): #Permite a Mimi hablar al usuario
    engine.say(text)
    engine.runAndWait()

def listen(): #Captura la voz del usuario
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-US")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        talk("Vuelve a intentar") #Si no entiende o no reconoce la voz
    return rec

def run(): #Opciones
    rec = listen()
    if 'estas ahi' in rec: #Saber si Mimi está activa
        talk('Si, estoy aqui')
    elif 'reproduce' in rec: #Reproducir en youtube
        if 'youtube':
            music = rec.replace('reproduce', '')
            talk(f'Reproduciendo {music}')
            pywhatkit.playonyt(music)
    elif 'hora' in rec: #Dar la hora actual
        hora = datetime.datetime.now().strftime('%H:%M %p')
        talk('son las ' + hora)
    elif 'busca' in rec: #Buscar la información en wikipedia
        busqueda = rec.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(busqueda, 1)
        talk(info)
    elif 'chiste' in rec: #Te cuenta un chiste
        jokes = pyjokes.get_joke("es")
        talk(jokes)
    else:
        talk(f'Vuelve a intentar: {rec}') #No reconoce el comando

while True:
    run() #Correr el codigo en bucle