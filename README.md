# List of User Agents /L

Comprehensive List of historical web + mobile browser `user-agent` strings.

And some scripts.


## Objective

To feed my own web tools with reliable data. I think it may be useful to others.

Instead of restarting from scratch, I choose to update something that I was already used to, and so this fork.


## Source

The current lists of `user-agent`s  were updated from real-life data from the domains I have control. You will find some gems around here, since I have a very diverse audience, from retro-computer enthusiasts to die hard UNIX hackers - and some hardcore gamers. 😁

Some bits were scrapped from:

* https://www.browsers.fyi/
* https://jnrbsn.github.io/user-agents/

And there's also these nice webpages to toy a bit with:

* https://jnrbsn.github.io/user-agents/user-agents.json
* https://github.com/microlinkhq/top-user-agents


## Data

* `Android+Webkit+Browser.txt`
	+ List of every Android Browser using WebKit I ever had contact with.
	+ Really every one, including Android 2.2 times.
		- I really miss my Nexus One. Still the best overall experience I ever had with Android.
	+ I didn't understood the need for this specialised list but, since it was already there, I'm keeping it.
* `Chrome.txt`
	+ Ditto for Google's Chrome.
* `Edge.txt`
	+ Ditto for Microsoft Edge.
	+ Very short list, essentially no one use this thing...
* `Firefox.txt`
	+ Ditto for Mozilla's Firefox.
		- Another journey into the past awaits you here!
* `Internet+Explorer.txt`
	+ Ditto for Microsoft Internet Explorer.
	+ So you can troll the poor bastards still using it!! 🤣
* `Opera.txt`
	+ Ditto for Opera.
		- Another journey into the past awaits you here, you will find even the MIDP versions!
		- Yeah, I maintain some sites for a very long time already...
* `Safari.txt`
	+ Ditto for Apple's Safari.
* `attic.txt`
	+ Here you will find some really, really old beasts.
		- Like Netscape running on AmigaOS!!
		- Boy, I'm proud of my servers, you know?
* `misc.txt`
	+ Whatever I found that is not **that** old yet.
* `newest.txt`
	+ The `user-agent`s for the newest releases of the the mainstream browsers.
	+ It's updated scarcely, don't trust it too much.
* `recent.txt`
	+ The `user-agent`s that hit my servers in the last month.
	+ It's updated now and then, using data from
		- https://report.lisias.net/
* `unsorted.txt`
	+ Whatever I didn't recognised, it's from a bot or it's just trash.
		- **DO NOT** use these ones, they are here so you can have a grasp on how a potential undesired request looks like.

## Scripts

* `fetch_newest.py`
	+ Fetch the newest data available from the mainstream browser's newest data.
		- It was used to build `newest.txt`
	+ Check the source for instructions.
* `user-agent.py`
	+ something I inherited when I forked the project. Don't have a clue about how it works yet. 😅
