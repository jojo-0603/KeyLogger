Introduction : 
Keylogger  is a type of surveillance technology used to monitor and record each keystroke on a specific device, such as a computer or smartphone. It can be either hardware- or software-based. The latter type is also known as system monitoring software or keyboard capture software.Keyloggers are often used as a spyware tool by cybercriminals to steal personally identifiable information, login credentials and sensitive enterprise data.
That said, some uses of keyloggers could be considered ethical or appropriate in varying degrees. For instance, keyloggers can also be used for the following reasons:
By employers to observe employees' computer activities.
By parents to supervise their children's internet usage.
By device owners to track possible unauthorized activity on their devices.
By law enforcement agencies to analyze incidents involving computer use.

Brief Overview of the Code :
The code covers various functionalities like 
Keylogging : The script captures keystrokes pressed by the user and stores them in a text file (log.txt), allowing the monitoring of user input.
Email Reporting : It periodically sends email reports containing the captured keystrokes as a text file attachment (log.txt), providing a stealthy means of monitoring user activity.
System Information Retrieval : The script gathers information about the user's system, including the IP address, processor, operating system, and machine type. This information is included in an email sent during startup for system reconnaissance.
Audio Recording : The script records audio from the system's microphone and sends it as an email attachment (sound.wav), enabling remote auditory surveillance.
Screenshot Capture : It takes screenshots of the user's screen and sends them as email attachments, facilitating visual monitoring of the user's activities.
Stealth Mode : The script operates in stealth mode by hiding the console window associated with its execution, ensuring that the monitoring activities remain discreet.
Startup Persistence : It adds itself to the Windows startup folder (Startup) to ensure that it runs automatically whenever the user logs into their Windows account, maintaining persistent monitoring.

Libraries Used : 
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







Environment Setup : 

1. Python Environment :
Ensure Python is installed on the system. The script is written in Python and requires a Python interpreter to execute.

2. Required Libraries :
Install the necessary Python libraries using pip, the Python package installer. These libraries include:
     - `email`: For handling email functionality.
     - `os`: For interacting with the operating system.
     - `platform`: For accessing information about the underlying platform.
     - `smtplib`: For sending email using the SMTP protocol.
     - `socket`: For working with network sockets.
     - `time`: For working with time-related functions.
     - `wave`: For reading and writing WAV audio files.
     - `pyscreenshot`: For capturing screenshots.
     - `win32console`: For accessing the Windows console API.
     - `win32gui`: For accessing the Windows GUI API.
     - `pyautogui`: For automating mouse and keyboard actions.
     - `pynput`: For monitoring and controlling input devices.
     - `sounddevice`: For recording audio from the microphone.
     - `getpass`: For securely reading passwords and sensitive information.
     - `dotenv`: For loading environment variables from a `.env` file.
       CMD :
   “pip install email pyscreenshot pynput sounddevice pyautogui python-dotenv”
   

3. Environment Variables :
Create a `.env` file in the same directory as the script to store sensitive information like email credentials.
Define the following environment variables in the `.env` file:
     - `fromaddr`: Email address of the sender (e.g., `from@example.com`).
     - `toaddr`: Email address of the recipient (e.g., `to@example.com`).
     - `password`: Password for the sender's email account.

   Example `.env` file:
   fromaddr=your_email@example.com
   toaddr=recipient_email@example.com
   password=your_email_password
   


4. Windows Startup Configuration :
Modify the script's `add_to_startup()` function to specify the desired file path for adding the script to the Windows startup folder.
By default, the script adds itself to the startup folder located at:
“C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup”
Ensure proper permissions and considerations for adding scripts to the startup folder.


Functions :
1.  add_to_startup : This function is used to add the ‘.bat’ file to the startup folder so that whenever the laptop reboots the function auto executes.

2. on_press : This function is used to store the keystrokes into a list objective and sends that list to the write_file.

3. write_file : This function is used to write the keystrokes to a ‘log.txt’ file.

4. stealth : This function is used so that it can hide the console .

5. screenshot : This function is used to take the screenshot of the entire window screen.

6. send_email : This function is used to send mail. 

7. get_system_info : This function is used to get the information of the system.

8. record_audio :  This function is used to record the audio of the victim from his microphone.


Error Handling : 
Errors are detected through various means, including:
Exception Handling: The script utilizes try-except blocks to catch and handle exceptions that may occur during execution. This allows the script to continue running even if an error occurs in a specific section of the code.
Conditional Statements: Certain sections of the code may include conditional statements to check for specific conditions or states. If a condition is not met, an error may be raised or specific error-handling logic may be triggered.






Usage : 
How to Use the Script
1. Environment Setup  :
   - Ensure Python is installed on the system.
   - Install the required Python libraries using pip, as specified in the "Environment Setup" section of the documentation.

2. Configuration :
Create a `.env` file in the same directory as the script and define the necessary environment variables (`fromaddr`, `toaddr`, `password`) as described in the "Environment Setup" section.

3. Run the Script :
  Execute the script by running the Python file (`python script_name.py`).

Follow the steps outlined above to set up and run the script for monitoring user activity on the system. Ensure proper configuration of environment variables and permissions for effective execution.


Conclusion : 
The provided script offers a powerful tool for monitoring user activity on a system, with features including keylogging, audio recording, and screenshot capture. It operates in stealth mode, allowing discreet monitoring, and sends periodic email reports for remote surveillance.It's important to note that while such scripts can have legitimate use cases such as parental control or employee monitoring, they also raise significant privacy and security concerns. Therefore, it's essential to use such tools responsibly and in compliance with applicable laws and regulations.
Proper documentation and understanding of the script's functionalities are crucial for ensuring effective and ethical use. Users should be aware of the potential risks and implications associated with deploying such monitoring tools. Additionally, regular updates and security measures should be implemented to mitigate potential vulnerabilities and protect against unauthorized access.Overall, this document aims to provide clear guidance on the setup, usage, and implications of the keylogger and system monitoring script, facilitating informed decision-making and responsible use of such tools.











Implementation

https://drive.google.com/drive/folders/1tpUoBVPSuOAbI3TfwJPX7jNz_YnHTeRb


