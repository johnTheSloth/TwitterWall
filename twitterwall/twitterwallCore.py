import click
import twitterwall.session as Session
import twitterwall.secret
import base64
from datetime import date
import requests
from time import sleep
from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)

@click.group()
def tw():
    pass

@tw.command()
@click.option('--path', '-p', default=1, help='Path to secret user account config.')
@click.option('--expression', '-e', default='python', help='Search expression.')
@click.option('--onload', '-o', default=10, help='Number of tweets on load.')
@click.option('--time', '-t', default=100, help='Time between tweet searches.')
@click.option('--retweet', '-r', default=True, help='Show retweets?')
def console(path, expression, onload, time, retweet):
    """Simple twitterwall application."""
    session = Session.twitter_session(twitterwall.secret.api_key, twitterwall.secret.api_secret)
    last_id = 0

    while True:
        r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+expression, 'count' : onload, 'since_id' : last_id})
        for tweet in reversed(r.json()['statuses']):
            if retweet or 'retweeted_status' not in tweet:
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print("┃ Tweet ID:  {}".format(tweet['id']))
                print("┃ DateTime:  {}".format(tweet['created_at']))
                print("┃ Posted by: {}".format(tweet['user']['name']))
                print("┃")
                print("┃ {} ".format(tweet['text']))
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".format(tweet['id']))
            last_id = tweet['id']
        print("-----------------------------")
        sleep(time);
        #onload = 100

#def main():
#    run()

@app.route('/twitterwall/e/<expression>')
@app.route('/twitterwall/e/<expression>/<int:onload>')
@app.route('/twitterwall/<int:onload>')
def renderPage(expression='python',onload = 10):
    last_id = 0
    session = Session.twitter_session(twitterwall.secret.api_key, twitterwall.secret.api_secret)
    r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+expression, 'count' : onload, 'since_id' : last_id})
    return render_template('twitterwall.html', tweets = r.json()['statuses'])

@tw.command()
def web():
    """Run the web app"""
    click.echo('Running the web app')
    app.run(debug=True)

@app.template_filter('tweetDiv')
def tweetDiv(tweet):
    """View text of tweet"""
    res = '<div class="panel"><div class="header"><img src="'
    res = res + tweet['user']['profile_image_url']
    res = res + '" ><div class="text">'
    res = res + tweet['user']['name']
    res = res + '</div></div><p><small><small>'
    res = res + tweet['created_at'][4:19] + '</small></small><br />'+ tweet['text']
    res = res + '</p></div><br />'

    return Markup(res)

#if __name__ == "__main__":
def main():
    tw()
