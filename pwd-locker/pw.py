#! python3
# A password manager haha

PASSWORDS={ "test1":"lolol" , 
	    "test2":"lolol2" 
	   };
import sys,pyperclip;

if len(sys.argv) < 2 :
	print("Usage python pw.py [account] " );
	sys.exit();

account=sys.argv[1];
if account in PASSWORDS:
	try:
		pyperclip.copy(PASSWORDS[account]);
		print("Password for " + account + " copied to clipboard.");
	except:
		print("Cannot copy even if account exists");
else:
	print("No such account");

