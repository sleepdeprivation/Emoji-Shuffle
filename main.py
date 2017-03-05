from github import Github
from emojipile import EMOJIS #ZOMG
import re
import random
import pickle
import os

def removeBeginningEmoji(s):
	"""
		Remove an emoji matching the regex from the first 31 chars
		expects there is a space afterward
	"""
	return re.sub(r":[a-z_]*: ", "", s[0:32]) + s[32:];

def placeRandomBeginningEmoji(s):
	"""
		Pick a random emoji from the emoji list
		and put it on the string
	"""
	emoji = EMOJIS[random.randint(0, len(EMOJIS))]
	return ":" + emoji + ": " + s;

def testEmojis():
	"""
		Test for above functions
	"""
	testcase = ":smiley_face: this is a repoasdfjaslkjfalskfjdaskldjasdfjklasdfljksdajkladfsj     ";
	print("test result:");
	print(removeBeginningEmoji(testcase));
	print(placeRandomBeginningEmoji(removeBeginningEmoji(testcase)))

### BE CAREFUL!
def addRandomEmojisToAll(git):
	"""
		go through all the repos and edit them to have a random emoji at the beginning
	"""
	for i in git.get_user().get_repos():
		desc = i.description;
		desc = "" if (type(desc) is None ) else desc;
		desc = placeRandomBeginningEmoji(removeBeginningEmoji(desc))
		#print desc;
		i.edit(description=desc);
		
def saveFix(git):
	"""
		If not exists, save name : descriptions dict
	"""
	filename = "uh-oh.p";
	if(not os.path.exists(filename)):
		print("backup doesn't exist, creating :")
		fix = { i.name : i.description for i in git.get_user().get_repos() };
		print(fix);
		pickle.dump( fix , open( "uh-oh.p", "wb" ) )
	else:
		print("Backup already exists!")
	
def plzFix(git):
	"""
		For when you mess up
	"""
	fix = pickle.load(open( "uh-oh.p", "rb" ));
	print("loaded fix, fixing ", fix);
	for i in git.get_user().get_repos():
		i.edit(description=fix[i.name]);
		

def listNamesDict(git):
	"""
		For when you really mess up badly
		If you have made it to this you will be rewriting all your descriptions
		You shouldn't need this
	"""
	print("{");
	for i in git.get_user().get_repos():
		print("\"" + i.name + "\":" + "\"\",");
	print("}")

if __name__ == '__main__':
	g = Github("sleepdeprivation", "?????????");
	saveFix(g);
	addRandomEmojisToAll(g)
	
	
	
	
	
	
	
	
	
	
	
	
