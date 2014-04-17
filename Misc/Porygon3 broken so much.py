import praw
import time
import HTMLParser
import csv
import os

try:
    r = praw.Reddit(user_agent='Shiny-Bot')
    r.login('Shiny-Bot', 'password')
except HTTPError, e:
    if e.code in [429, 500, 502, 503, 504]:
        print "Reddit is down (error %s), sleeping..." % e.code
        time.sleep(60)
        pass
    else:
        raise

print("Shiny-Bot up and running")

already_done = set() #Messages already checked.
fcWords = [] #add FCs here - maybe add from wiki page using method below
fullwiki = """The new TSV Database! Ran by /u/Shiny-Bot


Username|IGN|Friend Code|TSV|Reference Page|SVExchange Thread|Timezone|Alternative Contact
--------|--------|--------|---------|-------|------|------|------"""

def messagereply(message):
            try:
                message.reply("You did something wrong. Or I did. Who knows. " + '\n' + '\n' + "Look, let's just agree that we're both idiots.")
                already_done.add(message.id)
                message.mark_as_read()
            except HTTPError, e:
                if e.code in [429, 500, 502, 503, 504]:
                    print "Reddit is down (error %s), sleeping..." % e.code
                    time.sleep(60)
                    pass
                else:
                    raise

def messagesuccess(message):
            try:
                message.reply("Successfully added." + '\n' + '\n' + "Because I am the best bot ever.")
                already_done.add(message.id)
                message.mark_as_read()
            except HTTPError, e:
                if e.code in [429, 500, 502, 503, 504]:
                    print "Reddit is down (error %s), sleeping..." % e.code
                    time.sleep(60)
                    pass
                else:
                    raise
                
def removeuser(redditortest):
    
    #with open('svdatabase.csv', 'rb') as csvfile:
    #    for col in csvfile:
    #        if redditortest not in col:
    #            csv.writer(open('temporary.csv', 'a+')).write(col)
    with open('svdatabase.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',') #Splitting the csv file at space - why spaces are disappeaing
        for row in spamreader:
            csv.writer(open('temporary.csv', 'a+')).writerow(row)
            
           # newuserstring = ''.join(row)
           # newuserstring = newuserstring.replace(",", '\n')
           # r.edit_wiki_page('SVExchange', 'shinyids', fullwiki + '\n' + newuserstring, reason="New users added")
           # print("UPDATED") 



#try:
while True:
        #with open('svdatabase.csv', 'rb') as csvfile:
        #    spamreader = csv.reader(csvfile, delimiter=',') #Splitting the csv file at space - why spaces are disappeaing
        #    for row in spamreader:
        #        newuserstring = '\n'.join(row)
        #        #newuserstring = newuserstring.replace(",", '\n')
        #        r.edit_wiki_page('SVExchange', 'shinyids', fullwiki + '\n' + newuserstring, reason="New users added")
        #        print("UPDATED") 
        for message in r.get_unread():
            has_fc = any(string in message for string in fcWords)
            redditortest = str(message.author)
            columns = message.body.count('|')  # Counts columns in message
            if columns != 7 and message.id not in already_done:
                messagereply(message)
            elif message.id not in already_done and has_fc:
                messagereply(message)
            elif message.id not in already_done and '\r' in message.body: #Checks that there is only one line
                messagereply(message)
            elif message.id not in already_done and '\n' in message.body: #Checks that there is only one line
                messagereply(message)
            elif message.id not in already_done and message.subject == 'Add': # Needs to check that the user is new
                usercontent = "/u/" + redditortest + message.body
                page = r.get_wiki_page('SVExchange', 'shinyids')    #Needs to be down here so that new users data is caught too
                html_parser = HTMLParser.HTMLParser()
                page_content = html_parser.unescape(page.content_md)
                if redditortest in page_content: 
                    message.reply("User already exists")
                    already_done.add(message.id)
                    message.mark_as_read()
                else:
                    print(usercontent)
                    usercontent = usercontent.replace(",", "")
                    #usercontent = usercontent + ","
                    usercontent = usercontent.encode('utf-8') #To remove the crash - maybe not needed
                    fd = csv.writer(open('svdatabase.csv','a+'))
                    fd.writerow(usercontent)
                    #fd.close()
                    messagesuccess(message)
            elif message.id not in already_done and message.subject == 'Remove': #Add remove feature
                page = r.get_wiki_page('SVExchange', 'shinyids')    #Needs to be down here so that new users data is caught too
                html_parser = HTMLParser.HTMLParser()
                page_content = html_parser.unescape(page.content_md)
                if redditortest in page_content: #If this breaks add /u/ to the test - stops it finding the username in other words
                    #index = page_content.find(redditortest)
                    #part1 = page_content[0:index+1]
                    #part2 = page_content[index+1:len(page_content)]
                    #Part1 = part1[:-5]
                    #groups = part2.split('|')
                    #Part2 = '|'.join(groups[7:])
                    #r.edit_wiki_page('SVExchange', 'shinyids', Part1 + Part2, reason="User Removed")
                    time.sleep(30)

                    removeuser(redditortest)

                    #os.remove('svdatabase.csv')
                    #os.rename('temporary.csv', 'svdatabase.csv')
                    
                    #messagereply(message)
                    print(redditortest)
                else:
                    messagereply(message)
            elif message.id not in already_done:
                messagereply(message)
        time.sleep(60)
#except HTTPError:
 #   print("reddit might be down")
#    time.sleep(60)






