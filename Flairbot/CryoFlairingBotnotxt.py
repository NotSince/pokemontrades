import praw
import urllib2
import time
import re
import sys

#subreddit.get_flair_list(limit=none) will get all flair. If we want to set 2 for each. 

r = praw.Reddit(user_agent='Porygon2-Bot')
COM_AMOUNT = 15
subreddit = r.get_subreddit('pokemontrades')
fcformat = re.compile('[0-9]{4}\-[0-9]{4}\-[0-9]{4}\\s\|\|\\s')
pikachu = """quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \
        :##.       ==             .###.       `.      `.    `\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                    """

def log_in():
    print '\nLogging in...'
    try:
        r.login('Porygon2-Bot', 'password')
        print 'Logged in succesfully\n '
        print pikachu
    except:
        print 'Invalid username or password\n'
        sys.exit() # Will this break shit?


def check_messages():
    for message in r.get_unread(limit=COM_AMOUNT):
        reddituser = str(message.author)
        message.mark_as_read()
        if  '\r' in message.body:
            messagefailure(message, "Extra line found")    
        elif  '\n' in message.body: #Checks that there is only one line
            messagefailure(message, "Extra line found")           
        elif message.subject == 'Flair': #and not check_if_done(message.id):
            cssflair = r.get_flair(subreddit,reddituser)
            flairball = str(cssflair['flair_css_class'])
            if flairball == 'None':
                flairball = 'default'
            if flairball == '':
                flairball = 'default'
            flair = message.body.encode('utf-8')
            flair = str(flair)
            fcflair = flair[:18]
            if len(flair) > 30:
                messagefailure(message, "Flair is too long")
            elif len(flair) < 18:
                messagefailure(message, "No IGN found")
            elif fcformat.match(fcflair):
                r.set_flair(subreddit,reddituser,flair,flairball)
                print("User: "+str(reddituser)+"\n"+"Flair: "+flair+", "+flairball+"\n")
                messagesuccess(message)
                
            else:
                messagefailure(message, "Friend Code format changed")

        else:
            messagefailure(message, "I can't let you do that Dave")


def add_to_done(message_id):
    with open('done.txt', 'a') as done:
        done.write(message_id + '\n')
                

def check_if_done(message_id):
    with open('done.txt', 'r') as done:
        id_list = done.readlines()
    raw_message_id = message_id + '\n'
    if raw_message_id in id_list:
        return True
    else:
        return False

def cut_file():
    with open('done.txt', 'r') as done:
        file_lines = done.readlines()
    if file_lines > COM_AMOUNT:    
        with open('done.txt', 'w') as done:
            done.writelines(file_lines[-COM_AMOUNT:])

def main():
    log_in()
    
    print '\nSearching for request...'
    check_messages()
    #cut_file()
    print 'Sleeping...\n'
    sys.exit


def messagefailure(message, reason):
    try:
        message.reply("Flair not updated. Reason: \n \n" + reason)
        #add_to_done(message.id)
        
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
        message.reply("Flair updated.")
        #add_to_done(message.id)
        
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
                


if __name__ == "__main__":
    main()





