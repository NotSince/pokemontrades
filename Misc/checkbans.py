import praw
import time
import re
import sys
import HTMLParser

r = praw.Reddit(user_agent='Porygon-Bot')
subreddit = r.get_subreddit('pokemontrades')
svhatching = r.get_subreddit('TSVhatching')
searchwords = ['MustardFTW']


def log_in():
        print '\nLogging in...'
        try:
                r.login('Porygon-Bot', 'password')
                print 'Logged in succesfully\n'
        except:
                print 'Invalid username or password\n'
                sys.exit()


def check_bans():


        banned = subreddit.get_banned(limit=500)
        banned = [x for x in banned]
        
        for submission in svhatching.get_new(limit=200):
                if submission.author in banned:
                        print('Author: ' + str(submission.author))


    
##    bans = r.get_wiki_page('pokemontrades','banlist')
##    html_parser = HTMLParser.HTMLParser()
##    page_content = html_parser.unescape(bans.content_md)
##    banlist = page_content.encode('utf-8')
##    for submission in svhatching.get_new(limit=1000):
##        time.sleep(0.2)
##        if str(submission.author) in banlist:
##            print('Author: ' + str(submission.author))

        


def main():
        log_in()
        while True:
                print '\nSearching for request...'
                check_bans()
                print 'Finished searching...\n'
                #time.sleep(3000)
                sys.exit()
 
 
 
if __name__ == '__main__':
        main()

