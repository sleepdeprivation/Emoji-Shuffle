# Emoji-Shuffle

If you're like I was about a week ago you've noticed all the most successful github users have something that you don't.

That's right! Emojis all over their repo descriptions!

'That's ridiculous', you say, 'I can't possibly spend the time to put the perfect emoji on each and every repo'.

Now you don't need to. Thanks to [advanced science](https://en.wikipedia.org/wiki/Confirmation_bias)
you're probably going to notice that a few of those emojis are spot-on!

## Instructions

Just fill in your creds and run (DISCLAIMER: READ THE CODE, I AM NOT RESPONSIBLE FOR ANYTHING THAT YOU DO WITH THIS)

These functions are currently called from main

    g = Github("sleepdeprivation", "?????????");
    saveFix(g); #saves a fix for when you mess up
    addRandomEmojisToAll(g)

## What's included right in the box?

### removeBeginningEmoji(s):
	"""
		Remove an emoji matching the regex from the first 31 chars
		expects there is a space afterward
	"""

### placeRandomBeginningEmoji(s):
	"""
		Pick a random emoji from the emoji list
		and put it on the string
	"""
### testEmojis():
	"""
		Test for above functions
	"""

### def addRandomEmojisToAll(git):
	"""
		go through all the repos and edit them to have a random emoji at the beginning
	"""
		
### def saveFix(git):
	"""
		If not exists, save name : descriptions dict
	"""
	
### def plzFix(git):
	"""
		For when you mess up
	"""

### def listNamesDict(git):
	"""
		For when you really mess up badly
		If you have made it to this you will be rewriting all your descriptions
		You shouldn't need this
	"""



