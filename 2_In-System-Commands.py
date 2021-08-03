
print("""
                        ##############################
                     ############   God AI   ############
                        ##############################

                *    Copyright Of Captain Murlidhar Singh & ASAI Inc, 2021                 *

                *    Suggestion, Feedback & Contact E-mail; captainms.asaiinc@gmail.com    *

""")

#username
username = "Captain Skywalker"


#modules_required
import pyttsx3 
import datetime  
import speech_recognition as source1
import os
import datetime


# voice_engine
voice_engine = pyttsx3.init('sapi5')   # object creation, voice_engine
# voice_engine.say('Hello World')

# voice_engine_voice
voice_engine_voice = voice_engine.getProperty('voices')
# print(voice_engine_voice[1].id)
voice_engine.setProperty('voice', voice_engine_voice[1].id)

# voice_engine_rate
voice_engine_rate = voice_engine.getProperty('rate')
# print(voice_engine_rate)
voice_engine.setProperty('rate', 210)


def speak(audio):   # A speak function(), which takes audio as it's parameter
    voice_engine.say(audio)
    voice_engine.runAndWait()
    

# Greeting message
def greeting():
    time1 = datetime.datetime.now()
    # print(time1)
    time_in_hour = int(datetime.datetime.now().hour)
    # print(time_in_hour)
    if time_in_hour>0 and time_in_hour<12:
        print(f'Hello {username}, Good Morning !\n')
    elif time_in_hour>12 and time_in_hour<16:
        print(f'Hello {username}, Good Afternoon !\n')
    else:
        print(f'Hello {username}, Good Evening !\n')

    print("I'm here to help you :)")   # Ultimate statements
    speak("I'm here to help you ... ")   


def processCommand():
    """
    It processes voice command from microphone & returns result of the command !        
    """
    command = source1.Recognizer()
    with source1.Microphone() as source:
        print("Listening...")
        command.pause_threshold=1.5      
        audio = command.listen(source)

    #Executing Query
    try:
        print('Recognizing...')
        query = command.recognize_google(audio, language='en-us')
        print(f"You said; {query}\n")

    except Exception as error:
        return 'None'

    return query


#Ultimate-Function
attempt = 1
if __name__ == "__main__":
    greeting()
    #logic
    while True:
        query = processCommand().lower()


        #base-commands
        #attempt-limit
        if attempt == 6:
            print("Looking Forward To Help You ...")
            speak("Looking Forward To Help You ...")
            exit()


        #intro 
        elif 'who are you' in query:
            print("Hey! I'm GOD AI & I'm here to do cool tasks for you !")
            speak("I'm here to do cool tasks for you !")

        elif 'tell me about yourself' in query:
            speak(" Here's some informations about me; ")
            print("""
                        ##############################
                     ############   God AI   ############
                        ##############################

                *    Copyright Of Captain Murlidhar Singh & ASAI Inc, 2021                 *

                *    Suggestion, Feedback & Contact E-mail; captainms.asaiinc@gmail.com    *


                ######   ASAI Inc.   ######

                    *   Founder & CEO; Captain Murlidhar Singh  *

                    *   Founded On; Day 5th Of November 2020   *

                    *   ASAI Inc Stands For; an Automation System with Artificial Intelligence Incorporated    *

                    *   Origin; Earth   *


                ######   Developer & Development Details   ######

                    *   Developed Under; ASAI Inc.   *

                    *   Developed By; Captain Murlidhar Singh  (Known As; Captain Skywalker)   *

                    *   Programming Language Used; Python3 & Windows Batchfile   *

                    
                
            """)


        #feedback | work required !
        elif 'you need to improve' in query:
            print("Sure, I'll definitely improve !")
            speak("Sure...")
            exit()
     

        #date | work required !
        elif "the date" in query:
            speak("The Current Date is; ")
            today_date = str(os.system("date"))
            print(today_date)


        #time
        elif 'the time' in query:
            nowTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f'The time is; {nowTime}')
            speak(f'The time is; {nowTime}')


        #wishing
        elif 'good morning' in query:
            print(f'Good Morning {username}, Have a nice day !')
            speak(f'Good Morning {username}, Have a nice day !')

        elif 'good afternoon' in query:
            print(f'Good Afternoon {username}, Hope you doing a great work !')
            speak(f'Good Afternoon {username}, Hope you doing a great work !')

        elif 'good evening' in query:
            print(f'Good Evening {username}, It\'s time to refresh and relax for some time !')
            speak(f'Good Evening {username}, It\'s time to refresh and relax for some time !')

        elif 'good night' in query:
            print(f'Good Night {username}, Have a nice dream !')
            speak(f'Good Night {username}, Have a nice dream !')


        #web-commands
        #



        #system-commands
        #explorer
        elif "open explorer" in query:
            os.system("explorer")
            print("Opening File Explorer...")
            speak("Opening File Explorer...")
            exit()

        #files
        elif "open files" in query:
            os.system("explorer")
            print("Opening Files...")
            speak("Opening File Explorer...")
            exit()


        #bash shell
        elif "open bash shell" in query:
            print("Opening Bash Shell (Linux Terminal, WSL)...")
            speak("Opening Bash Shell...")
            os.system("bash")
            exit()


        #bash
        elif "open bash" in query:
            print("Opening Bash Shell (Linux Terminal, WSL)...")
            speak("Opening Bash Shell...")
            os.system("bash")
            exit()


        #kali 
        elif "open kali" in query:
            print("Opening Kali Linux (Linux Terminal, WSL)...")
            speak("Opening Kali Linux...")
            os.system("kali")
            exit()


        #kali linux
        elif "open kali linux" in query:
            print("Opening Kali Linux (Linux Terminal, WSL)...")
            speak("Opening Kali Linux...")
            os.system("kali")
            exit()


        #ubuntu
        elif "open ubuntu" in query:
            print("Opening Ubuntu (Linux Terminal, WSL)...")
            speak("Opening Ubuntu...")
            os.system("ubuntu")
            exit()


        #python
        elif "open python" in query:
            print("Opening Python Shell...")
            speak("Opening Python...")
            os.system("python") 
            exit()


        #vscode
        elif 'open code' in query:
            os.system("code")
            print('Opening Visual Studio Code...')
            speak('Opening VS Code...')
            exit()

        elif 'open vs code' in query:
            vscodePath = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
            print('Opening Visual Studio Code...')
            speak('Opening VS Code...')
            exit()


        elif "open virtualbox" in query:
            virtualbox_path = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(virtualbox_path)
            print("Opening Virtualbox...")
            speak("Opening Virtualbox...")
            exit()


        #firefox
        elif 'open firefox' in query:
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox_path)
            print('Opening Firefox Browser...')
            speak('Opening Firefox...')
            exit()


        #chrome
        elif "open chrome" in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)
            print("Opening Chrome Browser...")
            speak("Opening Chrome...")
            exit()


        #microsoft browser
        elif "open microsoft browser" in query:
            microsoft_browser_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(microsoft_browser_path)
            print('Opening Microsoft Edge Browser...')
            speak("Opening Microsoft Edge...")
            exit()


        #control panel
        elif "open control panel" in query:
            os.system("%windir%\System32\Control.exe")
            print("Opening Control Panel...")
            speak("Opening Control Panel...")
            exit()


        #poweroff
        elif 'poweroff the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you!')
            exit()

        elif 'power of the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you...')
            exit()

        elif "stop poweroff" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        elif "stop power of" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")


        #shutdown
        elif 'shutdown the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you!')
            exit()

        elif 'shut down the system' in query:
            print('Shutting Down The System In Less Than A Minute...')
            speak('Shutting Down The System In Less Than A Minute...')
            os.system('shutdown -s')
            speak('Looking forward to help you...')
            exit()

        elif "stop shutdown" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")

        elif "stop shut down" in query:
            print('Stoping System From Shutdown...')
            speak('Stoping System From Shutdown...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")


        #reboot
        elif 'reboot the system' in query:
            print('Rebooting The System In Less Than A Minute...')
            speak('Rebooting The System In Less Than A Minute...')
            os.system('shutdown /r')
            speak('Looking forward to help you...')
            exit()
       
        elif "stop reboot" in query:
            print('Stoping System From Reboot...')
            speak('Stoping System From Reboot...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")


        #restart
        elif 'restart the system' in query:
            print('Restarting The System In Less Than A Minute...')
            speak('Restarting The System In Less Than A Minute...')
            os.system('shutdown /r')
            speak('Looking forward to help you...')
            exit()

        elif "stop restart" in query:
            print('Stoping System From Restart...')
            speak('Stoping System From Restart...')
            os.system('shutdown -a')
            speak("Welcome Back, I'm here to help you... ")


        #base-commands
        #exit
        elif "quit" in query:
            print("Okay !")
            speak("Okay !")
            quit()

        elif "exit" in query:
            print("Okay !")
            speak("Okay !")
            exit()

        #ok
        elif "ok" in query:
            print("Alright !")
            speak("Alright !")
            exit()

        #error-message
        else:
            print("Please! Say Again ...\n")
            speak("Say Again ...\n")
            attempt = attempt + 1























