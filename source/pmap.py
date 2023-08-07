#██████  ███    ███  █████  ██████  
#██   ██ ████  ████ ██   ██ ██   ██ 
#██████  ██ ████ ██ ███████ ██████  
#██      ██  ██  ██ ██   ██ ██      
#██      ██      ██ ██   ██ ██            
                                                  
# Welcome! This is PMAP, the open source Python Port scanner!
# Github: https://github.com/users/nikkeisadev
# Made by: nikkeisadev, with love!

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⠠⡖⠲⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⡠⠶⣴⣶⣄⠀⠀⠀⢀⣴⣞⣼⣴⣖⣶⣾⡷⣶⣿⣿⣷⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢸⠀⠀⠀⠙⢟⠛⠴⣶⣿⣿⠟⠙⣍⠑⢌⠙⢵⣝⢿⣽⡮⣎⢿⡦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢱⡶⣋⠿⣽⣸⡀⠘⣎⢢⡰⣷⢿⣣⠹⣿⢸⣿⢿⠿⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⢧⡿⣇⡅⣿⣇⠗⢤⣸⣿⢳⣹⡀⠳⣷⣻⣼⢿⣯⡷⣿⣁⠒⠠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⣼⣿⣧⡏⣿⣿⢾⣯⡠⣾⣸⣿⡿⣦⣙⣿⢹⡇⣿⣷⣝⠿⣅⣂⡀⠀⠡⢂⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⣿⡟⣿⡇⡏⣿⣽⣿⣧⢻⡗⡇⣇⣤⣿⣿⣿⣧⣿⣿⡲⣭⣀⡭⠛⠁⠀⠀⠈⠀⠉⢂⢄⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⢻⣿⣇⣥⣏⣘⣿⣏⠛⠻⣷⠿⡻⡛⠷⡽⡿⣿⣿⣿⣷⠟⠓⠉⠢⢄⡀⠀⠀⠀⠀⠀⠁⠫⢢⠀⠀⠀  
#⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⢸⣾⣿⣽⣿⣏⣻⠻⠁⢠⠁⠀⠀⠀⠘⣰⣿⣿⢟⢹⢻⠀⠀⠀⠀⠀⠈⠒⢄⡀⠀⠀⠀⠀⠀⠀⠑⢄    (Anime girl says: pmap is sooo kawaiii - UwU)
#⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⢸⣯⣿⣿⣿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠛⣩⣿⣿⢿⣾⣸⠀⠀⠀⠀⠀⠀⢀⡠⠚⠉⠉⠁⠀⠀⠀⢀⠌                    (also, no skid, right?)
#⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠀⢟⣿⣯⡟⠿⡟⢇⡀⠀⠀⠐⠁⢀⢴⠋⡼⢣⣿⣻⡏⠀⠀⠀⣀⠄⠂⠁⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠈⠊⢻⣿⣜⡹⡀⠈⠱⠂⠤⠔⠡⢶⣽⡷⢟⡿⠕⠒⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⡠⠐⠁⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⢿⠿⠿⢿⠾⣽⡀⠀⠀⠀⠈⠻⣥⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⠁⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣖⠂⠠⠐⠋⠀⠙⠳⣤⣠⠀⠀⠀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠵⡐⠄⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⡀⠀⠠⡀⠀⠈⠙⠶⣖⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡥⠈⠂⠀⠀⠀⠀⠀⠀⠀⣼⠉⠙⠲⣄⠈⠣⡀⠀⠀⠈⢻⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀ ⠈⣷⡄⠈⠄⠀⠀⠀⢧⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⡀⠀⢠⣿⣤⣤⣶⣶⣾⣿⣿⡄⢸⠀⠀⠀⢸⣄⣤⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠇⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⠀⠀⠀⣼⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠁⠀⠈⠉⠙⠛⠿⠿⠽⠿⠟⠛⡉⠛⠲⣿⣿⠿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⢠⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⠀⠀⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⡠⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢫⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⣰⡿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣼⠏⣸⣿⣷⢷⠙⣻⢶⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠉⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠰⣏⠀⣿⣿⡘⣼⡇⠀⠁⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠁⠀⠀⣽⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢙⠓⠛⠘⣧⠾⢷⣄⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⣿⢟⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠸⠀⠀⠀⢸⣧⠀⠹⣆⠀⠀⠀⠀⠈⢻⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⢂⠙⢿⡷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢃⠀⠀⠈⠙⠀⠀⠻⡄⠀⠀⠀⠀⠸⡀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠐⠠⠀⠻⠬⠄⡒⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀

#===================================CODE======================================
#Importing packages, such as socket for making pings.
import colorama
from colorama import Fore, Back
import socket, errno, sys, os, platform, requests, time, datetime
from datetime import datetime

#Def. values, strings-ints, and also the url for testing the internet connection.
startTime  = time.time()
CONNECTION_TEST = "https://github.com"
TIMEOUT = 5
PMAP_PREFIX = '[PMAP]> '

#The sleeping def...
def sleep(sec):
    time.sleep(sec)

#Printing the main logo, and other inforamtion.
print('')
print(Fore.BLUE + "█▀█ █▀▄▀█ █▀█ █▀█" + Fore.YELLOW + "       0.2 ALPHA REMASTER")
print(Fore.BLUE + "█▀▀ █░▀░█ █▀█ █▀▀" + Fore.RED + " Made with love by, Nikke")
print(Fore.BLUE + "=====================" + Fore.WHITE + "WELCOME" + Fore.BLUE + "=====================")
print(Fore.BLUE + "Welcome to port map! The opensource port scanner writen in Python!")
print(Fore.BLUE + "Found any bug? Contact me here: https://github.com/nikkeisadev")
print(Fore.BLUE + "======================" + Fore.WHITE + "PMAP" + Fore.BLUE + "=======================")

#Checking internet connection with requests.
print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Checking internet connection...")
try:
    request = requests.get(CONNECTION_TEST, timeout=TIMEOUT)
    sleep(1)
    print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Connection is successfully to the internet!" + Fore.BLUE + "[" + Fore.GREEN + "OK" + Fore.BLUE + "]")
    sleep(1)
    print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Starting Port Map... " + Fore.BLUE + "[" + Fore.GREEN + "OK" + Fore.BLUE + "]")
    sleep(1)
except (requests.ConnectionError, requests.Timeout) as exception:
    print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Connection timeouted!" + Fore.WHITE +"[" + Fore.RED + "ERR" + Fore.WHITE + "] !")
    quit()

#Gathering information about the target.
#Input field to store the IP address of the target.
print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Entering to pmap>" + Fore.RED + "ipsetup" + Fore.BLUE + "..!" + Fore.BLUE)
ip = input(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "ipsetup>" + Fore.RED + "ip" + Fore.WHITE + "> Add the target's IP address: ")
print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "Validating the IP address...")

#Validating the IP address.
try:
    socket.inet_aton(ip)
    print(Fore.BLUE + f"{PMAP_PREFIX}" + Fore.WHITE + "The IP is valid! [" + Fore.GREEN + "OK" + Fore.BLUE + "]")
except socket.error:
    print(Fore.RED + f"{PMAP_PREFIX}" + Fore.WHITE + "The IP address is not valid! " + Fore.WHITE + "[" + Fore.RED + "ERR" + Fore.WHITE + "]")
    quit()
print(Fore.BLUE + f"{PMAP_PREFIX}ipsetup>" + Fore.RED + "ip " + Fore.BLUE + "Setup completed! [" + Fore.GREEN + "OK" + Fore.BLUE + "]")
print(Fore.BLUE + f"{PMAP_PREFIX}portsetup>" + Fore.RED + "port" + Fore.BLUE + "> Collecting info about the ports.")
sleep(1)
#Def. the IP address into a variable.
remote_server = ip
remote_server_ip = socket.gethostbyname(remote_server)

#Input field to store the PORT number of the target.
print(Fore.YELLOW + f"{PMAP_PREFIX}Enter the range of ports! [min/max]")
startPort = input(Fore.BLUE + f"{PMAP_PREFIX}Enter the first port: ")
endPort = input(f"{PMAP_PREFIX}Enter the last port: ")

#Validating the first and last port number.
if int(startPort) > 65535 or int(startPort) <= 0:
    print(Fore.BLUE + f"{PMAP_PREFIX}Invalid value for the first port number!" + Fore.WHITE +"[" + Fore.RED + "ERR" + Fore.WHITE + "]")
    quit()
if int(endPort) > 65535 or int(endPort) <= 0:
    print(Fore.BLUE + f"{PMAP_PREFIX}Invalid value for the last port number!" + Fore.WHITE +"[" + Fore.RED + "ERR" + Fore.WHITE + "]")
    quit()

#Starting the scan... it's just the print thingy-
print(Fore.BLUE + f"{PMAP_PREFIX}Initializing scanning at [", remote_server_ip,']')
print('')
time_init = datetime.now()
print(Fore.BLUE + "======================PMAP=======================")
print(Fore.BLUE + f"{PMAP_PREFIX}The scan starts in 5 secounds, you still can hit CTRL-C...")
print(Fore.RED + f"{PMAP_PREFIX}It's possible to track your ping requests!")
sleep(5)
print('')

#A for loop for each port; checking them one by one.
hits = 0
fails = 0

try:
  for port in range(int(startPort), int(endPort)+1):
      print(Fore.BLUE + "Checking port {} ...".format(port))
      server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      server_sock.settimeout(5)
      result = server_sock.connect_ex((remote_server_ip, port))
      #If the result exit value is equals 0 it's means that it's a hit (an openport)
      if result == 0:
          hits += 1
          print(Fore.GREEN + "======================OPEN=======================" + Fore.BLUE + "")
          print(Fore.GREEN + "", ip, Fore.GREEN + "PORT ==> " + Fore.GREEN + "OPEN".format(port))
      #And, ofc, if it's a bigger value, like 1 bit, it's a nope. So it's a closed port.
      else:
          fails += 1
          print(Fore.RED + "", ip, Fore.RED + "PORT ==> " + Fore.RED + "CLOSED".format(port))
          print(Fore.YELLOW + "Info:" + Fore.YELLOW, errno.errorcode[result])
      server_sock.close()
except socket.error:
    #There is a possibility that the server went down while scanning, so ya can detect it.
    print(Fore.RED + f"{PMAP_PREFIX}The host seems to be down!" + Fore.WHITE +"[" + Fore.RED + "ERR" + Fore.WHITE + "]")
    sys.exit()

#The end of the code, when the scan finnishes, (finaly XD)-
time_finish = datetime.now()
total_time = time_finish - time_init
print(Fore.GREEN + "====================FINISHED=====================")
print(Fore.WHITE + f"{PMAP_PREFIX}Finished in" + Fore.GREEN + "", total_time)
print(Fore.WHITE + f"{PMAP_PREFIX}The scan is completed!")
print(Fore.WHITE + f"{PMAP_PREFIX}Informations: All Hit[{hits}] - All Fail[{fails}].")
#Just a question: ya liked the anime character, right?