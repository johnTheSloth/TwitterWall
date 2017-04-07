# Twitterwall
 Domácí úloha k předmětu ke kurzu [Python a jeho knihovny](http://naucse.python.cz/2017/pyknihovny-brno/) inspirovaný předmětem [MI-PYT (Pokročilý Python)](http://bk.fit.cvut.cz/cz/predmety/00/00/00/00/00/00/04/87/12/p4871206.html) na [FIT ČVUT](http://fit.cvut.cz/).

	Usage:
    python3 twitterwall/twitterwallCore.py console [OPTIONS]
    or
    python3 twitterwall/twitterwallCore.py web

| Options: 	|          	| Meaning:                             	|
|-------	|--------------	|-------------------------------------	|
| -p    	| --path       	| Path to secret user account config. 	|
| -e    	| --expression 	| Search expression.                  	|
| -o    	| --onload     	| Number of tweets on load.           	|
| -t    	| --time        	| Time between tweet searches.        	|
| -r    	| --retweet     	| Show retweets?                      	|
|       	| --help       	| Show this message and exit.         	|

It's needed to add file secret.py with your own Twitter API keys in format:
    api_key = '<insert key here>'
    api_secret = '<insert super secret key here>'
