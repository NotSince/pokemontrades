import socket
import praw
import re
import sys

def modmail_search(username):

   r = praw.Reddit(user_agent='Rash_Bot')
   subreddit = r.get_subreddit('pokemontrades') 

   searchlist = []
   
   try:
      r.login('Porygon-Bot', 'password')
      print 'Logged in succesfully\n'
   except:
      print 'Invalid username or password\n'

   for message in subreddit.get_mod_mail(limit=10000):
      if str(message.author) == username:
         listitem = 'http://en.reddit.com/message/messages/' + message.id
         print(listitem)
         searchlist.append(listitem)

   searchresults = ', '.join(searchlist)
   
   return searchresults

network = 'irc.synirc.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK MMS_Bot\r\n' )
irc.send ( 'USER MMS_Bot MMS_Bot MMS_Bot :Python IRC\r\n' )
irc.send ( 'JOIN #pkmntrades4mods\r\n' )
irc.send ( 'PRIVMSG #pkmntrades4mods :Hello World.\r\n' )
while True:
   data = irc.recv ( 4096 )
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '!MMS_Bot quit' ) != -1:
      irc.send ( 'PRIVMSG #pkmntrades4mods :Fine, if you dont want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'hi MMS_Bot' ) != -1:
      irc.send ( 'PRIVMSG #pkmntrades4mods :I already said hi...\r\n' )
   if data.find ( 'hello MMS_Bot' ) != -1:
      irc.send ( 'PRIVMSG #pkmntrades4mods :I already said hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #pkmntrades4mods\r\n' )
   if data.find ( 'Modmail:' ) != -1:
      results = modmail_search(username)
      irc.send ( 'PRIVMSG #pkmntrades4mods :' + results + '\r\n' )
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #pkmntrades4mods :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps MMS_Bot' ) != -1:
      irc.send ( 'PRIVMSG #pkmntrades4mods :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data

