"""Reddit extractor"""
import requests
import praw
from praw.models import MoreComments
import re
from nltk import tokenize


url = "" # e.g."https://www.reddit.com/r/TrueFilm/comments/6cgomc/what_have_you_been_watching_week_of_may_21_2017/" reddit post url

pattern = r'https://www\.reddit\.com/r/\w*/comments/(?P<post_id>\d*\w*)/\w*/' # pattern for capturing post ids
submission_id = re.search(pattern, url).group('post_id') # gets the post id of the reddit post in the url above

## your reddit info for the reddit module "praw" - please look up reddit api for more info on wha tyour need 
reddit = praw.Reddit(client_id='INSERT CLIENT ID HERE',client_secret='INSERT CLIENT SECRET HERE'/
	,password='INSERT YOUR REDDIT PW',user_agent='python commenter v1.0 by /u/insert_your_username',/
	username='INSERT YOUR REDDIT USERNAME')


# using reddit api to get all comments in list 
reddit_list = []
submission = reddit.submission(id=submission_id)
for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			reddit_list.extend(tokenize.sent_tokenize(top_level_comment.body))

#### sent_tokenize everyhing ###
self_text_sent_toke = [tokenize.sent_tokenize(self_text) for self_text in reddit_list]

### clean up (might need to do more clean up)###
self_text = [ [word for word in sentence if not word.startswith("http") and not word.startswith("*") \
			and not word.startswith("(") and not word.startswith(")") and not word.startswith("\"")] \
			for sentence in self_text_sent_toke]

sentence2 = ""
for sentence in self_text:
	for word in sentence:
		if word not in ".,;?!'":
			sentence2 += " " + word
		elif word in ['t', 's', 'nt', 've']:
			sentence2 += word + " "
		else:
			sentence2 += word + " "
self_text_join = [ sentence for sentence in sentence2.split('.')]

print("Example: ", self_text_join[0:2]) # an example of the corpus 

with open("reddit.txt", 'w') as f:
	[f.write(line+"\n") for line in self_text_join]