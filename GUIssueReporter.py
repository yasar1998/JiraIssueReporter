from tkinter import *
from tkinter import scrolledtext
import requests
import json
from base64 import b64encode

member_name = "Yashar Mustafayev"
member_ncode = "ERV6M2"
member_token = ""
member_email = "yasarmustafayev1998@gmail.com"

def successfull(full_name, neptun_code):
	name = full_name
	n_code = neptun_code

	if member_name==name and member_ncode==n_code:
		return True	
	return False

def connect(full_name, neptun_code):
	name = full_name
	n_code = neptun_code

	if member_name==name and member_ncode==n_code:
		user = "yasarmustafayev1998@gmail.com"
		auth_token = member_token.encode()
		
	print("----------------------------Reporter for Issues------------------------------");
	user_name = user.encode()
	BASE_URL = "https://atillaseyid87.atlassian.net/rest"

	session = requests.session()

	s = user_name + b":" + auth_token
	s = b64encode(s).decode('ascii')
	header = {"Authorization": "Basic " + s}

	resp = session.get(BASE_URL + '/api/latest/search?jql=project="TS"', headers=header)

	string = resp.text
	dct = json.loads(string)

	result = ""
	for i in range(dct["total"]):

		key = dct["issues"][i]["key"]
		print("Issue key: ", key)
		created = dct["issues"][i]["fields"]["created"]
		print("Issue Created: ", created)
		type_of_issue=dct["issues"][i]["fields"]["issuetype"]["name"]
		print("Issue Type: ", type_of_issue)
		Issue_descr = dct["issues"][i]["fields"]["summary"]
		print("Issue Description: ", Issue_descr)
		Issue_progress = dct["issues"][i]["fields"]["status"]["name"]
		print("Issue Progress: ", Issue_progress)

		if(dct["issues"][i]["fields"]["assignee"] is None):
			print("Assignee: Not Available")
			result = result + "Issue key: " + key + "\n" + "Issue Created: " + created + "\n" + "Issue Type: " + type_of_issue + "\n" + "Issue Description: " + Issue_descr+"\n" + "Issue Progress: " + Issue_progress + "\nAssigned: Not assigned"
		else:
			print("Assignee: ", dct["issues"][i]["fields"]["assignee"]["displayName"])
			result = result + "Issue key: " + key + "\n" + "Issue Created: " + created + "\n" + "Issue Type: " + type_of_issue + "\n" + "Issue Description: " + Issue_descr+"\n" + "Issue Progress: " + Issue_progress + "\nAssigned: " + dct["issues"][i]["fields"]["assignee"]["displayName"] + "\n"
		Time_spent = dct["issues"][i]["fields"]["timespent"]				
		if(Time_spent is None):
			print("Time Spent: Not Available")
			result = result + "Time Spent: Not Available"
		else:
			print("Time spent: ", Time_spent, " sec.")
			result = result + "Time Spent: "+ str(Time_spent) + " seconds"		
		
		result = result + "\n-------------------------------\n\n"
		

		print("\n")
	return result	
		
root = Tk()
root.title("Issue Reporter")
root.geometry("500x500")

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

e1 = Entry(root, width = 50)
myLabel1 = Label(root, text="Your Full Name:")
myLabel1.pack()
e1.pack()
e1.insert(0, "")


e2 = Entry(root, width = 50)
myLabel2 = Label(root, text="Your Neptun Code:")
myLabel2.pack()
e2.pack()
e2.insert(0, "")

def myClick():

	full_name = e1.get()
	neptun_code = e2.get()
	
	
	if successfull(full_name, neptun_code)==True:
		srcText = scrolledtext.ScrolledText(root, wrap=WORD)
		srcText.pack()
		srcText.insert('insert', "\n----------Issues for the Project--------------\n\n"+connect(full_name, neptun_code))
		srcText.config(state=DISABLED)
	
		
	else:
		srcText = scrolledtext.ScrolledText(root, wrap=WORD)
		srcText.pack()
		srcText.insert('insert', "Wrong Information! Access Denied to the Project Site!")
		srcText.config(state=DISABLED)
		

myButton = Button(root, text="Access", command = myClick)
myButton.pack()

root.mainloop()
