import pyttsx3
import os
#This project is suitable to full screen cmd (font 24)
pyttsx3.speak("Heyyy, Elliot this side. Your assistant  ")
print()
print()
print("===================================================WELCOME TO MY PYTHON PROJECT======================================================")
print("           Hey, Elliot this side. Tell me your query I'll try to solve it very quickly")
while True:     #to run code recursively
	print()
	print()
	pyttsx3.speak("Sir Please Enter your queries ")
	print(">chat with me with your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	#TO OPEN CHROME BROWSER
	if (("run" in p) or ("start" in p) or ("execute" in p )or ("browse" in p ) or ("open" in p ))  and ("chrome" in p):
	  pyttsx3.speak("Opening google chrome")
	  os.system("chrome")
	  print()
	  print()	
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE------------------------------------------------------------")

	#TO OPEN MICROSOFT EDGE
	elif (("run" in p) or ("start" in p) or ("execute" in p )or ("browse" in p ) or ("open" in p ))  and ("edge" in p):
	  pyttsx3.speak("Opening microsoft edge")
	  os.system("msedge") 
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")

	#TO OPEN NOTEPAD
	elif (("run" in p) or ("start" in p) or ("execute" in p) or ("open" in p )) and (("notepad" in p ) or ("editor" in p)):
	  pyttsx3.speak("Opening notepad")
	  os.system("notepad")
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")

	#TO OPEN WINDOWS MEDIA PLAYER
	elif (("run" in p) or ("start" in p) or ("execute" in p ) or ("open" in p ))  and (("windows" in p) or ("media" in p) or ("wmplayer" in p) or ("player" in p)):
	  pyttsx3.speak("Opening windows media player")
	  os.system("wmplayer")
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")

#TO OPEN CALCULATOR
	elif (("run" in p) or ("start" in p) or ("execute" in p ) or ("open" in p ))  and (("calc" in p) or ("calculator" in p )):
	  pyttsx3.speak("Opening calculator")
	  os.system("calc") 
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")

	#TO OPEN HELP SECTION
	elif ("help" in p):
	  pyttsx3.speak("hope you found it helpfull")
	  print("		-This project is just for testing purpose")
	  print("		-This tool is still is in developement phase")
	  print("		-In case you cant terminate previous command try ctrl+c")
	  print("		-We will add some more features soon!!!")
	  print("		-To exit this try 'exit'/ 'quit'/ 'end'/ 'esc' ")
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")

        
	 
	#TO EXIT OF TOOL
	elif  ("exit" in p)   or ("quit" in p) or ("end" in p) or ("esc" in p):
	  pyttsx3.speak("We are closing this program  Thank You Sir HOPE YOU GOT GOOD EXPERIENCE")
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------")
	  break

	#TO SHOW ERROR
	else:
	  pyttsx3.speak(" Error Please enter proper query or command")
	  print("     -Command Not supported!!!!")
	  print("     -Try more familiar command")
	  print("     -Use help command for more information")
	  print()
	  print()
	  print("-----------------------------------------------HOPE YOU GOT GOOD EXPERIENCE-----------------------------------------------------------") 
