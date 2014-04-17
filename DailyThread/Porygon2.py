
import time
import praw
import datetime


now = datetime.datetime.now()
date = now.strftime("%d %B %Y")

r = praw.Reddit(user_agent='Porygon-Bot')
r.login('Porygon-Bot', 'password')

#date = raw_input("Enter date: ")

title = "Daily Standard Trade Thread for " + date

title2 = "Daily TSV/ESV/Battle Checking Thread " + date

body = """[m]

* Please read the [rules](http://www.reddit.com/r/pokemontrades/wiki/rules) before posting.
* Do not beg for karma.
* Please state your generation if you are not trading on X and Y.

*****

* **No shinies or events are to be traded on this thread**, with the exception of shiny trades directly involving:
     * A shiny Ditto,
     * A regular Ditto,
     * Or Megastones.

*****

* [Message the Mods](http://www.reddit.com/message/compose?to=%2Fr%2Fpokemontrades) if you have a question or something to report."""

body2 = """[m]

Good Morning everyone. 

Battle checking can also be requested in this thread! [More information can be found here.](http://www.reddit.com/r/SVExchange/comments/20k4hg/xy_keybv_battle_video_data_viewer/)

* Please read the [rules](http://www.reddit.com/r/SVExchange/wiki/rules/) before posting.
* This thread is to either volunteer to check other people's shiny values (egg or trainer) or to request your own to be checked.
* Please make sure your Friend Code and IGN are in your flair.

*****

* Any Pokemon with your OT can be used to check your TSV. 
* Remember that checking eggs requires a trade and a tradeback, be reasonable with your requests. 


*****

* For further advice, or just a friendly chat, visit the [IRC](https://kiwiirc.com/client/irc.synirc.net/?channels=#svexchange).
* [Message the Mods](http://www.reddit.com/message/compose?to=%2Fr%2Fsvexchange) if you have a question or something to report."""


#submission = r.submit('pkmntrades4mods', title, text=body)

#submission = r.submit('pokemontrades', title, text=body)

#submission.distinguish()

#Comment = submission.add_comment("All off topic discussion must be as a reply to this comment.")

#Comment.distinguish()

#submission.sticky()

submission2 = r.submit('SVExchange', title2, text=body2)

submission2.distinguish()

submission2.sticky()

submission2.approve()
