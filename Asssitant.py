#Importing necessary modules
import uuid 
import socket
import subprocess
import json
from urllib.request import urlopen
import urllib.request
from tabulate import tabulate
import psutil
import GPUtil
import platform
import wmi
import pyautogui
from string import ascii_letters, digits
import string
from pytube import YouTube 
import requests
from pprint import pprint
import speech_recognition as sr
import datetime
import winshell
import pyttsx3
import ctypes
import wikipedia
import shutil
import os
import time
import wolframalpha
from itertools import chain, repeat
from tqdm import tqdm
from playsound import playsound
import validators
import matplotlib.pyplot as plt
from win10toast import ToastNotifier


#Clear function for clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()


#Loading screen
print("Making your Program Ready...")
time.sleep(2)
print("\nThis may take a while...")
time.sleep(2)
print("\n*Please make sure you'r device is connected to an Internet Connection*")
time.sleep(2)
print("\n")
for _ in tqdm(range(100),
        desc = "Loading your Program...",
        ascii = False, ncols =75):
    time.sleep(0.1)

print("\nStarting The Program...")
time.sleep(2)
print("\nHere you GO...")
time.sleep(1)

clear()

#For speech_recognition
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#For playing a sound file
playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\It Pennywise hello.mp3")

#For speaking the commands
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#Starting commands
def Sofia_commands():
    
    time.sleep(2)
    
    speak("I am sorry for that. It was just a prank. I hope it didn't scared you.")
    
    speak("By the way")
    
    commands = ["I am your assistant Sofia", "And I will be your guide for this program.", 
                "Taking you to the Instructions Menu.", "Please wait..."]
    
    for i in chain.from_iterable(repeat(commands, 1)):
        speak(i)
        
Sofia_commands()

#Function for giving a desktop notification
def notification1():
    
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Pennywise"
    message = "Hi Sanyam I am Pennywise the dancing Clown." + u"\U0001F921" + "You leaving so early." + "Don't worry We will play again soon." + "hahaha"
    
    icon = "icon.ico"
    length = 50
    toast.show_toast(title, message,icon_path=icon, duration=length)

#Function for giving another desktop notification
def notification2():
    
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Pennywise"
    message = "Hi Sanyam I am Pennywise the  dancing Clown." + u"\U0001F921" + "hahaha" + "Wrong input ha. hahaha" + "Don't worry we just restart the program and we can play again."
    
    icon = "icon.ico"
    length = 50
    toast.show_toast(title, message,icon_path=icon, duration=length)
    

#User instructions
def instructions():
    
    time.sleep(1)
    clear()
    
    print("\t\t\t*Instructions*", flush=False)
    print("\n")
    speak("This is the instructions Menu. And your instructions are as follows.")
    print("The instructions are as follows:")
    
    lst = ["We have 4 classes in this program.", "In the First class we have 6 operations which I will show you later.", 
            "The Second class is the image scrapping program in which you can download any image from google.",
            "The Third class is the YouTube program in which we have 3 operations which I will show you later.",
            "The Fourth and the last class is the weather scrapping program in which you can get weather data of any city of India.",
            "The Fifth class is the Graph plotting program in which you can plot bar graphs and pie charts."]

    for i in chain.from_iterable(repeat(lst, 1)):
        
        time.sleep(2)
        speak(i)
        print("\n")
        print(i)
    
    speak("Now I will take you to the First class. Please wait...")
    
instructions()

#Class 1 instructions
#System details class 
def class1():
    
    time.sleep(2)
    clear()
    
    print("\t\t\t*CLASS 1*", flush=False)
    print("\n")
    speak("In class one you can do the following 6 operations.")
    
    C1 = ["First. Get the Mac Adress of your device", "Second. Get the IP Address of your device", 
            "Third. Get the passwords of the wifi portals which connected to your device", 
                "Fourth. Get the Network Location", "Fifth. Get your system detils", 
                    "Sixth. Get your CPU information"]
    
    for i in chain.from_iterable(repeat(C1, 1)):
        speak(i)
    
    print("The operations which you can perform are:")
    
    C1P = ["1. Get the Mac Adress of your device", "2. Get the IP Address of your device", 
                "3. Get the passwords of the wifi portals which connected to your device",
                    "4. Get the Network Location", "5. Get your system detils", 
                            "6. Get your CPU information"]
    
    for i in chain.from_iterable(repeat(C1P, 1)):
        time.sleep(2)
        print("\n")
        print(i)
        
    speak("Now I will take you to the Second class. Please wait...")
        
class1()

#Class 2 instructions
#Image scrapping class
def Class2():
    
    time.sleep(2)
    clear()
    
    print("\t\t\t*CLASS 2*", flush=False)
    print("\n")
    
    C2 = ["This is an Image scrapping class. Using this class you can download any image from google.",
            "You will just have to give the url of the image and a name for it.", 
                "And then the image will get saved in file where your python projects or programs are located.",
                    "Or I can say that when the image get downloaded it will show in the IDE which you are using."]
    
    for i in chain.from_iterable(repeat(C2, 1)):
        speak(i)
        print("\n")
        print(i)
        
    speak("Now I will take you to the third class. Please wait...")
    
Class2()

#Class 3 instructions
#Youtube video downloading class
def Class3():
    
    time.sleep(3)
    clear()
    
    print("\t\t\t*CLASS 3*", flush=False)
    print("\n")
    
    speak("In this class you can perform the following three operations.")
    
    C3 = ["First. Download any video from Youtube to your Device", 
            "You will just have to provide the url of the video, a name for the video and the location path where you want to save the video",
                "Second. Get the details of any youtube video.", 
                    "In this you will just have to provide the url of the video for which you want to get the details.",
                        "Third. Extract the audio from a youtube video.",
                            "In this you will just have to provide the url of the video for which you want to extract the audio and the path where you want to save that audio."]

    for i in chain.from_iterable(repeat(C3, 1)):
        speak(i)
        
    print("The operations which you can use are:")
    
    C3P = ["1. Download any video from Youtube to your Device.", 
            "You will just have to provide the url of the video, a name for the video and the location path where you want to save the video.",
                "2. Get the details of any youtube video.", 
                    "In this you will just have to provide the url of the video for which you want to get the details.",
                        "3. Extract the audio from a youtube video.",
                                "In this you will just have to provide the url of the video for which you want to extract the audio and the path where you want to save the audio."]
    
    for i in chain.from_iterable(repeat(C3P, 1)):
        
        time.sleep(2)
        print("\n")
        print(i)
        
    speak("Now I will take you to the fourth class. Please wait...")
    
Class3()

#Class 4 instructions
#Weather scrapping class
def Class4():
    
    time.sleep(3)
    clear()
    
    print("\t\t\t*CLASS 4*", flush=False)
    print("\n")
    
    C4 = ["This is a Weather Scrapping class.", "Using this class you will be able to get the Weather of any city of the World.", 
            "You will just have to give the name of the city and the  current weather details of that city will get printed."]

    for i in chain.from_iterable(repeat(C4, 1)):
        speak(i)
        print("\n")
        print(i)
    
    speak("Now I will take you to the fifth class. Please wait...")
Class4()

#Class 5 instructions
#Graphs making class
def Class5():
    
    time.sleep(3)
    clear()
    
    print("\t\t\t*CLASS 5*", flush=False)
    print("\n")
    
    C5 = ["The is a graph plotting class.", "Using this class you will be able to plot bar graphs and pie charts"]
    
    for i in chain.from_iterable(repeat(C5, 1)):
        speak(i)
        print("\n")
        print(i)
        
Class5()

#Instructions help class to get the brief of the instructions
def instructions_help():
    
    speak("If you want me to show you the instructions. please enter 'instructions' below: ")
    time.sleep(1)
    speak("Else If you want me to show you the the information of any class then just enter the number of the class whose information you want me to display.")
    time.sleep(1)
    
    C = input("Please enter what you want me to do: ")
    
    if C == "1" or C == "Class 1" or C == "ONE" or C == "one" or C == "One" or C == "class 1":
        
        print("The operations which you can perform in First class are:")
    
        HC1 = ["1. Get the Mac Adress of your device", "2. Get the IP Address of your device", 
                    "3. Get the passwords of the wifi portals which connected to your device",
                        "4. Get the Network Location", "5. Get your system detils", 
                            "6. Get your CPU information"]
    
        for i in chain.from_iterable(repeat(HC1, 1)):
            time.sleep(2)
            print("\n")
            print(i)
            
    if C == "2" or C == "Class 2" or C == "TWO" or C == "two" or C == "Two" or C == "class 2":
        
        HC2 = ["This is an Image scrapping class. Using this class you can download any image from google.",
                    "You will just have to give the url of the image and a name for it.", 
                        "And then the image will get saved in file where your python projects or programs are located.",
                            "Or I can say that when the image get downloaded it will show in the IDE which you are using."]
    
        for i in chain.from_iterable(repeat(HC2, 1)):
            speak(i)
            print("\n")
            print(i)
            
    if C == "3" or C == "Class 3" or C == "THREE" or C == "three" or C == "Three" or C == "class 3":
        
        print("The operations which you can use are:")
    
        C3P = ["1. Download any video from Youtube to your Device.", 
                    "You will just have to provide the url of the video, a name for the video and the location path where you want to save the video.",
                        "2. Get the details of any youtube video.", 
                            "In this you will just have to provide the url of the video for which you want to get the details.",
                                "3. Extract the audio from a youtube video.",
                                        "In this you will just have to provide the url of the video for which you want to extract the audio and the path where you want to save the audio."]
        
        for i in chain.from_iterable(repeat(C3P, 1)):
            
            time.sleep(2)
            print("\n")
            print(i)
            
    if C == "4" or C == "Class 4" or C == "FOUR" or C == "four" or C == "Four" or C == "class 4":
        
        C4 = ["This is a Weather Scrapping class.", "Using this class you will be able to get the Weather of any city of the World.", 
            "You will just have to give the name of the city and the  current weather details of that city will get printed."]

        for i in chain.from_iterable(repeat(C4, 1)):
            speak(i)
            print("\n")
            print(i)
            
    if C == "5" or C == "Class 5" or C == "FIVE" or C == "five" or C == "Five" or C == "class 5":
        
        C5 = ["The is a graph plotting class.", "Using this class you will be able to plot bar graphs( enter '1') and pie charts('enter '2')"]
    
        for i in chain.from_iterable(repeat(C5, 1)):
            speak(i)
            print("\n")
            print(i)
            
    else:
        speak("It is an invalid input. The program will end for now.")
        time.sleep(1)
        speak("Please restart the program.")
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
        

#Image scrapping class help for getting help related to image scrapping class
def image_downloader_help():
    
    speak("In the image downloader I can help you in the following ways")
    
    image_help = ["1. How to get the url/adress of an image in google", "2. To help you with where your image got downloaded"]
    
    H = int(input("Enter your choice('1' or '2'): "))
    
    if H == 1:
        
        lst1 = ["To get the url/adress of an image in google just enter the name of the image which you want to download", 
                    "Then click on the image which you want to download from the multiple choices",
                        "Then right click on the image and select copy image adress", "By this the image adress of that image will get copied",
                            "Then paste that url where you will be asked for the url and then the image will be downloaded."]
        
        for i in chain.from_iterable(repeat(lst1, 1)):
            speak(i)
            print("\n")
            print(i)

    if H == 2:
        
        lst2 = ["When your image is downloaded. Just open your files section in your IDE", "There you will see the download image with your given name", 
                    "You can then access the image from the IDE or just open the folder which is linked to your IDE and you will be able to access the image."]
        
        for i in chain.from_iterable(repeat(lst2, 1)):
            speak(i)
            print("\n")
            print(i)
    
    else:
        
        speak("It is an invalid input. The program will end for now.")
        time.sleep(1)
        speak("Please restart the program.")
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
        

#Inputting path help to get help related to how to get the url of path 
def input_path_help():
    
    lst1 = ["To get the path of any file.", "Just open the folder in which you want to save the data.",
                "Then above the folder you will be able to see the location of that folder.", 
                    "Just double click on that and fule path of that folder will appear.",
                        "Select that path link and paste that in the program.",
                            "The path link would be like this: 'C:\\Users\\HP\\OneDrive\\Desktop\\New folder'.",
                                "Just paste that link in the program and your data will get saved."]
    
    for i in chain.from_iterable(repeat(lst1, 1)):
            speak(i)
            print("\n")
            print(i)
    
    speak("I hope you understood it...")


#Help function for showing all the above help functions
def help():
    
    speak("I can help you with the following problems: ")
    
    HELP = ["1. To show the instructions of any class.", "2. To help you with image downloader.",
                "3. To help you with inputting path."]
    
    for i in chain.from_iterable(repeat(HELP, 1)):
        print("\n")
        time.sleep(1)
        print(i)
        
    Help = int(input("Enter your choice: "))
    
    if Help == 1:
        
        instructions_help()
        
    elif Help == 2:
        
        image_downloader_help()
        
    elif Help == 3:
        
        input_path_help()
        
    else:
        
        speak("It is an invalid input. The program will end for now.")
        time.sleep(1)
        speak("Please restart the program.")
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
        

#Function for getting the MAC address of your device
def MacAdress():
    
    print ("Your  device's MAC address is: ",hex(uuid.getnode())) 
    

#Function for getting the IP address of your device
def IPAdress():
    
    hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(hostname) 
    print("Your Device Name is:" + hostname) 
    print("Your Device's IP Address is:" + IPAddr) 
    

#Function for getting the passwords of the networks which connected to this device
def WifiPassword():

    speak("The Wifi portals names and their associated passwords are as follows:")
    
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            time.sleep(1.5)
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            time.sleep(1.5)
            print ("{:<30}|  {:<}".format(i, ""))


#Function for getting the Network Location of your network
def NetworkLocation():
    
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)

    table = [["Server:", data["org"]], ["City:", data["city"]], ["country:", data["country"]], ["region:", data["region"]]]

    print(tabulate(table))


#Function for getting the system details
def System_Details():
    
    c = wmi.WMI() 
    my_system = c.Win32_ComputerSystem()[0]
    
    lst = [(f"Manufacturer: {my_system.Manufacturer}"), (f"Model Name: {my_system.Name}"), 
                (f"Number Of Processors: {my_system.NumberOfProcessors}"), (f"System Type: {my_system.SystemType}"), 
                        (f"System Family: {my_system.SystemFamily}")]

    for i in lst:
        print(i)
        
    my_system = platform.uname()

    lst1 = [(f"System: {my_system.system}"), (f"Release: {my_system.release}"), (f"Version: {my_system.version}"), 
            (f"Machine: {my_system.machine}"), (f"Processor: {my_system.processor}")]

    for i in lst1:
        print(i)


#Function for getting the CPU information
def CPU_INFO():
    
    print("Physical Cores:", psutil.cpu_count(logical=False))
    print("Total Cores:", psutil.cpu_count(logical=True))
    
    cpufreq = psutil.cpu_freq()
    print("Max Frequency: {cpufreq.max: 0.2f}Mhz")
    print("Min Frequency: {cpufreq.min: 0.2f}Mhz")
    print("Current Frequency: {cpufreq.current: 0.2f}Mhz")
    
    print("Cpu Usage Per Core:")
    
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")

    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


#Function for downloading image from google
def image():
    
    speak("Please enter the url of the image which you want to download.")
    image_url = input("Enter the url of the image: ")
    
    valid=validators.url(image_url)
    
    if valid==True:
        pass
    
    else:
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
    
    speak("Please enter a name by which you want to save the image.")
    name = input("Enter name: ")
    
    filename = name + ".jpg"

    req = urllib.request.build_opener()
    req.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64)')]
    urllib.request.install_opener(req)

    urllib.request.urlretrieve(image_url, filename)
    speak("Image has been successfully downloaded.")
    speak("Please check your files in IDE. The image will be there.")

#image()


#Function for downloading youtube video
def youtube():
    
    speak("Enter the url of the youtube video which you want to download.")
    url = input("Enter url: ")
    
    valid=validators.url(url)
    
    if valid==True:
        pass
    
    else:
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()

    speak("Enter the path of the location where you want to save the video file.")
    path = input("Enter path: ")
    
    isExist = os.path.exists(path)
    
    if isExist == True:
        pass
    
    else:
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()

    speak("Enter a name for the file.")
    filename = input("Enter filename: ")

    try:
        yt_obj = YouTube(url)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        # download the highest quality video
        filters.get_highest_resolution().download(path, filename)
        speak('Video Downloaded Successfully')
        speak("Please check the location where you have saved the video file.")
        pass
    
    except Exception as e:
        print(e)
        

#Function for getting the details of any youtube video
def Youtube_video_details():
    
    try:
        speak("Enter the url of the youtube video for which you want to get video details.")
        yt_obj = YouTube(input("Enter url: "))
    
        lst = [(f'Video Title is {yt_obj.title}'), (f'Video Length is {yt_obj.length} seconds'),
                        (f'Video Rating is {yt_obj.rating}'), (f'Video Views Count is {yt_obj.views}'), 
                                (f'Video Author is {yt_obj.author}')]
    
        for i in lst:
            print(i)

    except Exception as e:
        print(e)
        exit()
        
        
#Function for downloading only the audio of any youtube video
def youtube_audio():
    
    speak("Enter the url of the video for which you want to extract the audio of.")
    youtube_video_url = input("Enter url: ")
    
    valid=validators.url(youtube_video_url)
    
    if valid==True:
        pass
    
    else:
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
    
    speak("Enter the path where you want to save the audio file.")
    path = input("Enter path: ")        
    
    isExist = os.path.exists(path)
    
    if isExist == True:
        pass
    
    else:
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
        
    name = input("Enter name: ")
    
    try:
        yt_obj = YouTube(youtube_video_url)

        yt_obj.streams.get_audio_only().download(output_path=path, filename=name)
        speak('The audio file has been downloaded successfully')
        speak("Please check the location where you have saved the audio file.")
        pass
    
    except Exception as e:
        print(e)


#Functions for getting the weather information of any city of the world
#This function connects the program to the openweathermap service API to get the weather information
def weather_data(query):
    
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');

	return res.json();


#This function prints the weather information
def print_weather(result,city):
    
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))


#This function is used to get the name of the city for which the weather information is to be displayed
#It also checks whether the city name is correct or not
#And if the city name is valid then it displays that city's weather information
def main():
    
	city=input('Enter the city:')

	print()

	try:
    
	    query='q='+city;
	    w_data=weather_data(query);
	    print_weather(w_data, city)
	    print()
    
	except:
    
	    print('City name not found...')


#Function for making bar graph
def bar_graph():
    
    title = input('Enter title for the plot: ')
    x = input("Enter name of x axis: ")
    y = input("Enter the name of y axis: ")
    
    X = []

    n = int(input("Enter the number of elements: "))

    for i in range(0, n):
        ele = float(input("Enter element %d: " % (i + 1)))

        X.append(ele)

    Y = []

    for i in range(0, n):
        ele = float(input("Enter the corresponding value for element %d: " % (i + 1)))

        Y.append(ele)


    plt.plot(X, Y, color=(255/255, 100/255, 100/255))     

    plt.ylabel(y)

    plt.xlabel(x)

    plt.title(title)

    plt.grid(True)
    
    time.sleep(1)
    
    speak('Your graph has been created.')
    
    time.sleep(1)
    
    plt.show()
    

#Function for making pie chart
def pie_chart():

    title = input("Enter the title for the plot: ")
    
    labels = []

    n = int(input("Enter the number of elements: "))

    for i in range(0, n):
        ele = input("Enter name of element %d: " % (i + 1))

        labels.append(ele)

    sizes = []

    for i in range(0, n):
        ele = float(input("Enter the corresponding value for element %d: " % (i + 1)))

        sizes.append(ele)

    plt.pie(sizes,labels=labels, autopct="%1.1f%%")     

    plt.title(title, bbox={'facecolor':'0.8', 'pad':5})
    
    plt.axis("equal")

    time.sleep(1)
    
    speak('Your plot has been created')
    
    time.sleep(1)
    
    plt.show()

clear()


#While loop so that the operations can be done again and again until user inputs end
while True:
    
    #For choosing which class the user want to use
    choice = input('Enter The class which you want to use: ')

    
    #If user enters 1 then it will open 1st class for usage
    if choice == "1":
        speak("Please enter the operation do you want to perform")
        
        #For choosing an operation from class 1
        try:
            op1 = int(input('Enter the operation you want to perform: '))
            
        except ValueError:
            speak("It is an invalid input. Please try again.")
            #print("It is an invalid input. Please try again.")
            continue
        
        #And after choosing the class the user has to choose which operation he/she wants to perform in the 1st class
        if op1 == 1:
            MacAdress()
            
        elif op1 == 2:
            IPAdress()
            
        elif op1 == 3:
            WifiPassword()
            
        elif op1 == 4:
            NetworkLocation()
            
        elif op1 == 5:
            System_Details()
            
        elif op1 == 6:
            CPU_INFO()
            
        else:
            print("Invalid Input. Please try again.")
            exit()
    
    #If user enters 2 then it will open the second class for usage
    if choice == "2":
        
        image()
    
    
    #If user enters 3 then it will open the third class for usage
    if choice == "3":
        
        #After choosing the 3rd class the user has to select which operation he/she wants to perfrom in the 3rd class
        speak("Please enter the operation do you want to perform.")
        op3 = int(input("Enter the operation which you want to perform: "))
        
        
        #If user enters 1 then it will open the youtube video downloader
        if op3 == 1:
            youtube()
        
        
        #If user enters 2 then it will open the get youtube video details function
        elif op3 == 2:
            Youtube_video_details()

        
        #If user enters 3 then it will open the get the audio from youtube video function
        elif op3 == 3:
            youtube_audio()
            
        
        else:
            speak("It is an invalid input. The program will end now.")
            speak("Please restart the program again.")
            time.sleep(1)
            playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
            time.sleep(1)
            notification2()
            exit()
            
            
    #If user enters 4 then it will open the weather scrapping class
    if choice == "4":
        main()
        
        
    #And if user enters 5 then...
    if choice == "5":
        
        speak("To make a bar graph please enter one in input and to make a pie chart please enter two in input.")
        speak("Please enter the operation do you want to perform")
        
        
        #User has to select which type of graph he/she wants to make
        op5 = int(input("Enter the operation which you want to perform: "))
        
        
        #If user enters 1 then it will open the bar graph making function
        if op5 == 1:
            bar_graph()
            
            
        #If user enters 2 then it will open the pie chart making function
        if op5 == 2:
            pie_chart()
            
        else:
            speak("It is an invalid input. The program will end now.")
            speak("Please restart the program again.")
            time.sleep(1)
            playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
            time.sleep(1)
            notification2()
            exit()

    
    #If user enters 'end' as input then the program will end
    if choice == "End" or choice == "end" or choice == "END":
        speak("Thank You for your time.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\smile_on_the_face.mp3")
        time.sleep(1)
        print("Thank You.")
        time.sleep(1)
        exit()
    
    
    #Else if the user enters 'exit' then also the program will end
    elif choice == "EXIT" or choice == "exit" or choice == "Exit":
        
        speak("Thank You for your time.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\smile_on_the_face.mp3")
        time.sleep(1)
        print("Thank You.")
        time.sleep(1)
        exit()
    
    
    #If user enters 'help' as input then the help function will be opened
    if choice == "Help" or choice == "help" or choice == "HELP":
        
        help()
        
    else:
        
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
        
    
    #If user wants to perform again then he/she enters 'y' else 'n'
    choice1 = input("Do you want to perfrom again? (y/n): ").lower()
    
    if choice1 == "y":
        
        continue
    
    elif choice1 == "n":
        
        speak("OK...sure...")
        time.sleep(1)
        speak("Thank you for your time.")
        time.sleep(1)
        print("Thank you.")
        notification1()
        
        
    #Also if the user enters 'exit' or 'end' here also then the program will also end
    elif choice1 == "EXIT" or choice1 == "exit" or choice1 == "Exit":
        
        speak("Thank You for your time.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\smile_on_the_face.mp3")
        time.sleep(1)
        print("Thank You.")
        time.sleep(1)
        notification1()
        exit()
        
    elif choice1 == "End" or choice1 == "end" or choice1 == "END":
        speak("Thank You for your time.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\smile_on_the_face.mp3")
        time.sleep(1)
        print("Thank You.")
        time.sleep(1)
        notification1()
        exit()
        
    else:
        
        speak("It is an invalid input. The program will end now.")
        speak("Please restart the program again.")
        time.sleep(1)
        playsound("C:\\Users\\HP\\Downloads\\Telegram Desktop\\Python\\Audio\\IT - Pennywise laugh.mp3")
        time.sleep(1)
        notification2()
        exit()
