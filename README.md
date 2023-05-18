# Receipt-Processor
This repository contains a receipt processing program written in Python.

# Setup
To run this program, install the most recent version of Python from https://www.python.org/downloads/ for your OS. 
Upon installing through those instructions, place fetchReceiptProcessor.py in a file location of your choice, and navigate to a terminal window.
Through terminal, change over to the directory that contains fetchReceiptProcessor.py, and run the command 'python fetchReceiptProcessor.py'. 
NOTE: Sometimes if ran on a Windows OS, the 'python' and 'python3' commands will be automatically directed to the Windows store. To prevent this, 
go into 'App Execution Aliases' and turn any related to Python into the 'off' state. This should allow for the run command to work.

# How it works
When run, you will be prompted to enter a command from a list of working commands. 'quit' will exit the program, and 'help' will restate instructions.
If you first type 'read', it will enter receipt entering mode, and you will then be prompted to enter the path to the receipt JSON file RELATIVE TO 
YOUR CURRENT FILE LOCATION. This will then create a 16 character alphanumeric ID for this receipt, save it under ./receipts/process/{ID}.json. 
It will also create a file in directory ./receipts/{ID}/points.json that contains the points received for that receipt.

If you then type 'score', you will then be prompted to enter the ID of the receipt you wish to score, the score will be printed to the terminal in JSON form. 
The true JSON of the score can always be accessed through ./receipts/{ID}/points.json.
