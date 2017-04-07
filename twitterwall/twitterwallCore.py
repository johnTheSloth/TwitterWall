import secret
import session as Session
import click
import base64
import requests
from time import sleep
from flask import Flask, url_for, render_template

def twitter_session(api_key, api_secret):
    session = requests.Session()
    secret = '{}:{}'.format(api_key, api_secret)
    secret64 = base64.b64encode(secret.encode('ascii')).decode('ascii')

    headers = {
        'Authorization': 'Basic {}'.format(secret64),
        'Host': 'api.twitter.com',
    }

    r = session.post('https://api.twitter.com/oauth2/token',
                    headers=headers,
                    data={'grant_type': 'client_credentials'})

    bearer_token = r.json()['access_token']

def bearer_auth(req):
    req.headers['Authorization'] = 'Bearer ' + bearer_token
    return req

    session.auth = bearer_auth
    return session

@click.command()
@click.option('--path', '-p', default=1, help='Path to secret user account config.')
@click.option('--expression', '-e', default='python', help='Search expression.')
@click.option('--onload', '-o', default=10, help='Number of tweets on load.')
@click.option('--time', '-t', default=100, help='Time between tweet searches.')
@click.option('--retweet', '-r', default=True, help='Show retweets?')
def run(path, expression, onload, time, retweet):
    """Simple twittewall application."""
    session = Session.twitter_session(secret.api_key, secret.api_secret)
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

def get_first(expression, onload):
    r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+expression, 'count' : onload})
    return r

def get_second(expression, onload, last_id):
    r = session.get('https://api.twitter.com/1.1/search/tweets.json',params={'q': '#'+expression, 'count' : onload, 'since_id' : last_id})
    return r

#def main():
#    run()
if __name__ == "__main__":
    run()
