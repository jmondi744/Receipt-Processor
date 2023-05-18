import json
import random
import string
import os
import math

def score_receipt(ID):
    ##Search dictionary for ID
    try:
        target = open("./receipts/" + ID + "/points.json", 'r')
        data = json.load(target)
        print(data)
         
    except:
        print("An exception occured (hint: ID was most likely non existent)")

def process_file(inputFile):
    jsonFile = json.load(inputFile)
    ##Generate ID
    ID = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    print("This receipt will have ID " + ID)
    newIDdir = "./receipts/" + ID
    os.mkdir(newIDdir)
    
    processJson = '{"id": "' + ID + '"}'
    processFile = "./receipts/process/" + ID + ".json"

    with open(processFile, 'w') as working:
        working.write(processJson)
        
    print("JSON object created for this receipt: " + processJson)

    ##Get score
    score = 0
    dumps = json.dumps(jsonFile)
    workable = json.loads(dumps)
    
    
    #1. length
    for ch in workable['retailer']:
        if ch.isalnum():
            score += 1
            
    #2. round dollar
    if ".00" in workable['total']:
        score += 50
        
    #3. 0.25 multiple
    if ".00" in workable['total'] or ".25" in workable['total'] or ".50" in workable['total'] or ".75" in workable['total']:
        score += 25
       
    #4. every 2 items
    numItems = len(workable['items'])
    score += int(5 * (numItems / 2))
        
    #5. if desc length is multiple of 3, multiply price*0.2 rounded up FOR EACH ITEM
    for item in workable['items']:
        if len(item['shortDescription']) % 3 == 0:
            score += int(math.ceil(float(item['price']) * 0.2))
    
    #6. odd day
    day = workable['purchaseDate'][8:]
    if int(day) % 2 == 1:
        score += 6
    
    #7. purchase between 14 and 16 oclock
    hour = workable['purchaseTime'][0:2]
    if int(hour) >= 14 and int(hour) < 16:
        score += 10

    ##Save receipt as ID name + score
    scoreJson = '{"points": "' + str(score) + '"}'
    scoreFile = newIDdir + "/points.json"
    with open(scoreFile, 'w') as working:
        working.write(scoreJson)
    
if __name__ == "__main__":
    if not os.path.exists("./receipts"):
        os.mkdir("./receipts")
    if not os.path.exists("./receipts/process"):
        os.mkdir("./receipts/process")
    print("Welcome! Type in 'read' to enter a receipt, 'score' to go into score mode, 'quit' to leave, or 'help' to repeat this message.")
    while True:
        inVal = input("Prompt: ")
        if inVal == "quit":
            break
            
        elif inVal == "help":
            print("Welcome! Type in 'read' to enter a receipt, quit to leave, or help to repeat this message")
            
        ##File processing check
        elif inVal == "read":
            read = input("Please type in the file path relative to this file location: ")
            
            f = open(read, 'r')
            process_file(f)

            
        ##Score checking
        elif inVal == "score":
            code = input("Please type in the ID of the receipt you'd like to score: ")
            score = score_receipt(code)
        ##else
        else:
            print("Unknown command, type help for information")
            