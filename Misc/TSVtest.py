import praw
import time
import re
import sys

r = praw.Reddit(user_agent='Shiny-Bot')
COM_AMOUNT = 15
tidformat = re.compile('([0-9]{1,5})\/([0-9]{1,5})')
hexformat = re.compile('(0x[0-9A-Fa-f]{8})')
subreddit = r.get_subreddit('SVExchange')

def log_in():
        print '\nLogging in...'
        try:
                r.login('Shiny-Bot', 'password')
                print 'Logged in succesfully\n'
        except:
                print 'Invalid username or password\n'
                sys.exit()


def check_comments():
    for comment in subreddit.get_comments(limit=COM_AMOUNT):
        time.sleep(0.2)
        if '@Shiny-Bot' in comment.body and comment.author != 'Shiny-Bot' and not check_if_done(comment.id):
            tid_sid = tidformat.findall(comment.body)
            for match in tid_sid:
                tid = int(match[0])
                sid = int(match[1])
                tsv = (tid ^ sid) >> 4
                print('the tsv is %d' % tsv)
                comment.reply('For the TID/SID combination %d/%d, the TSV is %d' % (tid, sid, tsv))
                add_to_done(comment.id)
            pid = hexformat.findall(comment.body)
            for match in pid:
                pidno = int(match, 16)
                pidhigh = (pidno & 0xffff0000) >> 16
                pidlow = pidno & 0xffff
                esv = (pidlow ^ pidhigh) >> 4
                comment.reply('For the PID %s, the ESV is %d' % (match, esv))
                print esv
                add_to_done(comment.id)
        else:
            print 'No requests...'


def add_to_done(comment_id):
        with open('done.txt', 'a') as done:
                done.write(comment_id + '\n')
                

def check_if_done(comment_id):
        with open('done.txt', 'r') as done:
                id_list = done.readlines()
        raw_comment_id = comment_id + '\n'
        if raw_comment_id in id_list:
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
        while True:
                print '\nSearching for request...'
                check_comments()
                cut_file()
                print 'Sleeping...\n'
                time.sleep(30)
 
 
 
if __name__ == '__main__':
        main()

