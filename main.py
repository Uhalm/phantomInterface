import os;
import time;
import platform;


#Global Constants
VER = "0.0.0";

#Global Change
clear = 'nul';
opsys = 'nul';
con = 'nul';

#check the operating system and configure acordingly
def osCheck():
	#call the globals this function will change
	global clear;
	global opsys;
	global con;

	#get the operating system
	opsys = platform.system();

	#check what os user is running
	if opsys.lower() == 'linux':
		clear = 'clear';
		con = 'linux';
		os.system(clear);

	elif opsys.lower() == 'windows' or opsys.lower == 'win':
		clear = 'cls';
		con = 'windows';
		os.system('TITLE Minecraft Bedrock Phantom Server Interface')
		os.system(clear);

	else:
		print('The operating system you are using is not supported by this software.');
		print('Please use Windows or Linux or you may alter the code to add suport for your device.');
		time.sleep(15);
		exit();


#Splashscreen to show credits
def intro():
	print("Minecraft Bedrock Phantom Server Interface");
	print("Phantom LAN Server Software by jhead");
	print("https://github.com/jhead/phantom");
	print("Interface by Uhalm");
	time.sleep(5);
	main();

#main screen to find what user wants to do
def mainMenu():
	while True:
		os.system(clear);
		print("Minecraft Bedrock Phantom Server Interface");
		print(" ");
		print("1.) Connect");
		print("2.) Help");
		print("3.) Setup (Linux)");
		print("4.) Exit");
		print(" ");
		userIn = input('>>>');

		#check what user inputed
		if userIn == '1':
			connect();

		elif userIn == '2':
			help();

		elif userIn == '3':
			setupL();

		elif userIn == '4':
			exit();

		else:
			print('Please select option 1, 2, or 3 by typing the number then pressing enter');
			time.sleep(4);


#run the command to setup the phantom server
def setupL():
	os.system('chmod u+x ./phantom-linux');


#main logic of the connect step
def connect():
	os.system(clear);
	ipport = getInfo();
	runLAN(ipport);

#get the info for the server to connect to
def getInfo():
	os.system(clear);
	print('Type the IP and Port for the server it should look like one of these two examples');
	print('play.example.org:12345');
	print('127.0.0.1:67890');
	ipport = input('>>>')
	return ipport;

#run the command
def runLAN(ip):
	os.system(clear);
	print('Press Ctrl+C to goto main menu.');
	cmd = './phantom-' + con + ' -server ' + ip;
	os.system(cmd);

#print the help screen
def help():
	os.system(clear);
	print('Minecraft Bedrock Phantom Server Interface');
	print('Phantom LAN Server Software by jhead');
	print('https://github.com/jhead/phantom');
	print('Interface by Uhalm');
	print(' ');
	print('Select "Connect" and follow the on screen instructions.');
	print('Then go on your console and select the server from the friends tab.');
	print(' ');
	input('Press Enter to continue.');



#run the program
osCheck();
mainMenu();
