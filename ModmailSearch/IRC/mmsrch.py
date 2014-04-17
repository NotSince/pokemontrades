#Base coding by NotSinceYesterday
#Additions and prompts by Rash_Octillery
#Version 1.1
#Date: 4/8/2014
#Readme.txt coming soon!!!

import praw
import time
import re
import sys
import getpass

r = praw.Reddit(user_agent='Rash_Bot')
subreddit = r.get_subreddit('pokemontrades') # Remember to set subreddit!


def log_in():
        uname = raw_input('Enter your Moderator Username: ')
        pwd = getpass.getpass('Enter your password: ') #IDLE will still show password characters on screen...regular CMD won't   
        try:
                r.login(uname, pwd)
                print 'Logged in succesfully\n'
        except:
                print 'Invalid username or password\n'
                sys.exit()  

def check_comments(srch):
        for message in subreddit.get_mod_mail(limit=10000):
               if str(message.author) == srch: #this username is who it searches for...
                   print('Author: ' + str(message.author) + "  ")
                   print('http://en.reddit.com/message/messages/' + message.id + "  ")

def main():
        log_in()
        while True:
                srch = raw_input('Enter the reddit username to search for: ')
                print '\nSearching for request...'
                check_comments(srch)
                print '\n Finished searching...\n'
                sys.exit()
 
 
if __name__ == '__main__':
        main()
