#!/usr/bin/python2.7
import sys
import requests
import json

# Get last comment posted
# Get Auth and Group#
# Pull new comments as json individuals
# Post comments to directory/file

#GLOBALS
FILE = "infofile.txt"
AUTH = "" # personal auth token of user
GROUPID = "" # group ID
LASTCOM = "" # last comment grabbed
COMMENTSFILE = "newComs.txt"

def getInfo():
    global FILE
    global AUTH
    global GROUPID
    global LASTCOM

    with open(FILE) as f:
        content = f.readlines()
    # remove whitespace characters
    content = [x.strip() for x in content]
    AUTH = content[0]
    GROUPID = content[1]
    LASTCOM = content[2]

    #print stuff
    print "AUTH TOKEN: " + AUTH
    print "GROUPID: " + GROUPID
    print "LAST COMMENT ID: " + LASTCOM

if __name__ == '__main__':

    print "GETTING COMMENTS"
    getInfo()

    if FILE is None or FILE == "" or \
        AUTH is None or AUTH == "" or \
        GROUPID is None or GROUPID == "":
        print "ERROR! Add information into infofile.txt"
        print "Ending Process"
        sys.exit(1)

    # go through pull data
    flag = True
    beforeID = "" # allows us to download a lot if behind
    firstID = ''
    jsondump = open(COMMENTSFILE,"w")
    newComsNum = 0

    print "Downloading New Comments"
    while flag:
        output = requests.get("https://api.groupme.com/v3/groups/" \
                              + GROUPID + "/messages?token="+AUTH+"&limit=100&before_id="\
                              +beforeID)
        try:
            output = output.json()
        except:
            flag = False
            break
        for x in output['response']['messages']:
            if firstID == '':
                firstID = x['id']
            # iterate through json objects of messages
            if x['id'] != LASTCOM:
                newComsNum+=1
                # if it is a new comment!
                beforeID = x['id']
                json.dump(x,jsondump)
                jsondump.write("\n")
            elif x['id'] == LASTCOM:
                # last comment reached!
                # Stop the Presses!
                flag = False
                break;

    # jsondump file now has updated comments
    print "Downloading Stoped! " + str(newComsNum) + " New Comments Downloaded"
    # update LASTCOM
    LASTCOM = firstID

    # update FILE
    with open(FILE,'w') as f:
        f.write(AUTH +"\n")
        f.write(GROUPID +"\n")
        f.write(LASTCOM +"\n")

    print "Infofile.txt Updated, Ending Process!"


