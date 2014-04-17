import praw

r = praw.Reddit(user_agent='Porygon-Bot')
r.login('Porygon-Bot', 'password')
subreddit = r.get_subreddit('pokemontrades')

Flairedusers = subreddit.get_flair_list(limit=None)

print Flairedusers

for user in Flairedusers:
    flairball = str(user['flair_css_class'])
    if flairball == 'gsball':
        print str(user['user'])
