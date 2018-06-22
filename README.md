# GroupMe-Download-JSON-Comments

Download all comments from a GroupMe in individual JSON format. Requires you to have access to your AUTH token and Group ID. Also allows users to only download new comments since last time they ran the file.

## Requirements

Requires these modules:
json
requests
python2.7

## Operation

Input your information into infofile.txt
remove 'LAST COMMENT' from infofile.txt
A simple run of pullbot (python2.7) will download all your comments into JSON format.
This data is stored in newComs.txt

## Infofile.txt Format Below:

~~~~~~~~~~~
[Personal Auth Token]
[GroupID]
[ID of last comment, optional]
~~~~~~~~~~~

The ID of the last comment allows the user to input the id of a comment that they wish pullbot 2000 to stop downloading on. This space will be filled automatically when Pullbot is ran. This allows the user to run this script again, and only download new comments. See arguments to make sure new comments do not overwrite old ones

## Arguments

-h : Pull up help menu, doesn't run process

-a : Ignore Last Comment information in infofile.txt, meaning PullBot 2000 will pull all comments associated with selected GroupMe

-x : Appends new Comments to newComs.txt file, instead of overwriting previous Comments


## SPLUNK USE

Add a monitor or a batch on newComs.txt in this directory
Add a 'chron' job for Pullbot 2000, run at in interval you see fit.
Pullbot 2000 will periodically populate your Splunk with data, and thanks to the 'created_at' field, the timestampes will be mostly right. 
