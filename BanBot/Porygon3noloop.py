import praw
import time
import HTMLParser
import csv
import os
import urllib2


if __name__ == "__main__":
    main()



def messagereply(message):
            try:
                message.reply("You did something wrong. Or I did. Who knows. " + '\n' + '\n' + "Look, let's just agree that we're both idiots.")
                already_done.add(message.id)
                message.mark_as_read()
            except urllib2.HTTPError, e:
                if e.code in [429, 500, 502, 503, 504]:
                    print "Reddit is down (error %s), sleeping..." % e.code
                    time.sleep(60)
                    pass
                else:
                    raise
            except Exception, e:
                print "couldn't Reddit: %s" % str(e)
                raise

def messagesuccess(message):
            try:
                message.reply("Successfully did whatever it was you asked me to do." + '\n' + '\n' + "Because I am the best bot ever.")
                already_done.add(message.id)
                message.mark_as_read()
            except urllib2.HTTPError, e:
                if e.code in [429, 500, 502, 503, 504]:
                    print "Reddit is down (error %s), sleeping..." % e.code
                    time.sleep(60)
                    pass
                else:
                    raise
            except Exception, e:
                print "couldn't Reddit: %s" % str(e)
                raise
                
def removeuser(redditortest):

    redditname = "/u/" + redditortest
    with open('svdatabase.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        datalist = []
        for row in spamreader:
            data = '\n'.join(row)
        
        datalist = data.split('\n')
        datalist = [x.strip(' ') for x in datalist]
        filtered = [ v for v in datalist if not v.startswith(redditname) ]
        newdatastring = ', '.join(filtered)
        
        temp = open('temporary.csv','w')
        temp.write(newdatastring)
        temp.close()

        csvfile.close()

    os.remove('svdatabase.csv')
    os.rename('temporary.csv', 'svdatabase.csv')



def main():
    try:
        r = praw.Reddit(user_agent='Shiny-Bot')
        r.login('Shiny-Bot', 'password')
    except urllib2.HTTPError, e:
        if e.code in [429, 500, 502, 503, 504]:
            print "Reddit is down (error %s), sleeping..." % e.code
            time.sleep(60)
            pass
        else:
            raise
    except Exception, e:
        print "couldn't Reddit: %s" % str(e)
        raise

    print("Shiny-Bot up and running")


    fcWords = [] #add FCs here - maybe add from wiki page using method below
    fullwiki = """The new TSV Database! Ran by /u/Shiny-Bot


    Username|IGN|Friend Code|TSV|Reference Page|SVExchange Thread|Timezone|Alternative Contact
    --------|--------|--------|---------|-------|------|------|------"""

    
    for message in r.get_unread():
        has_fc = any(string in message for string in fcWords)
        redditortest = str(message.author)
        columns = message.body.count('|')  # Counts columns in message
        mods = r.get_moderators('pokemontrades')
        if message.id not in already_done and message.subject == 'Ban':
            if message.author not in mods:
                message.reply("I can't let you do that Dave")
            else:
                if msg.body.count("[FC]") and msg.body.count("[/FC]"):
		    ban_fc = msg.body[msg.body.find("[FC]")+4:msg.body.find("[/FC]")]
		else:
		    ban_fc = "Error"
		if msg.body.count("[Reason]") and msg.body.count("[/Reason]"):
		    ban_reason = msg.body[msg.body.find("[Reason]")+8:msg.body.find("[/Reason]")]
		else:
		    ban_reason = ""
		if msg.body.count("[Proof]") and msg.body.count("[/Proof]"):
		    ban_proof = msg.body[msg.body.find("[Proof]")+7:msg.body.find("[/Proof]")]
		else:
		    ban_proof = ""
		if (len(ban_fc) == 14) and (ban_fc[4]=="-") and (ban_fc[9]=="-"):
		    try:
			print "Banned FC: " + ban_fc
		    except:
			print "Banned FC: ASCII Error"
		    try:
			if ban_reason:
			    print "Reason: " + ban_reason
			else:
			    print "Reason: None Available"
		    except:
			print "Reason: ASCII Error"
                    if ban_proof:
                        print "Proof: Yes"
                    else:
                        print "Proof: None Available"

                    banfc2 = ban_fc.replace("-", " ")
                    banfc3 = ban_fc.replace("-", "")
                    
		    automod = r.get_wiki_page('pokemontrades','automoderator').content_md
		    auto_update = automod[:automod.find("{/Mjolnir}")-8]+","+ban_fc+","+banfc2+","+banfc3+automod[automod.find("{/Mjolnir}")-8:]
		    r.edit_wiki_page('pokemontrades','automoderator',auto_update)
		    r.send_message('AutoModerator','pokemontrades','update')

		    banlist = r.get_wiki_page('pokemontrades','banlist').content_md
		    r.edit_wiki_page('pokemontrades','banlist',banlist + "\r\n" + ban_fc + " | "+ user + " | " + ban_reason +"|" + ban_proof+" |")

		    msg.reply("The Friend Code Ban request has already been sent. Thank you for your work!")
                
        if message.id not in already_done and message.subject == 'Remove123456':
            redditortest = message.body
            page = r.get_wiki_page('SVExchange', 'shinyids')    #Needs to be down here so that new users data is caught too
            html_parser = HTMLParser.HTMLParser()
            page_content = html_parser.unescape(page.content_md)
            if redditortest in page_content:
                time.sleep(30)
                removeuser(redditortest)
                message.reply("User removed.")
                already_done.add(message.id)
                message.mark_as_read()
                print(redditortest)
        elif columns != 7 and message.id not in already_done:
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
                usercontent = usercontent + ","
                usercontent = usercontent.encode('utf-8') #To remove the crash - maybe not needed
                fd = open('svdatabase.csv','a')
                fd.write(usercontent)
                fd.close()
                messagesuccess(message)
        elif message.id not in already_done and message.subject == 'Remove': #Add remove feature
            page = r.get_wiki_page('SVExchange', 'shinyids')    #Needs to be down here so that new users data is caught too
            html_parser = HTMLParser.HTMLParser()
            page_content = html_parser.unescape(page.content_md)
            if redditortest in page_content: #If this breaks add /u/ to the test - stops it finding the username in other words
                time.sleep(30)
                removeuser(redditortest)
                messagesuccess(message)
                print(redditortest)
            else:
                messagereply(message)
        elif message.id not in already_done:
            messagereply(message)
            
    with open('svdatabase.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',') #Splitting the csv file at space - why spaces are disappeaing
        for row in spamreader:
            newuserstring = '\n'.join(row)
            #newuserstring = newuserstring.replace(",", '\n')
            r.edit_wiki_page('SVExchange', 'shinyids', fullwiki + '\n' + newuserstring, reason="New users added")
            print("UPDATED") 






