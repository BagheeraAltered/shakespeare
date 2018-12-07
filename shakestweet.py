import random
import os
import tweepy
import sys
import subprocess

quote_file = 'shakespeare1.txt'
f = open(quote_file, 'r')
txt = f.read()
lines = txt.split('\n.\n')
param_1 = random.choice(lines)
print param_1


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

  api = get_api(cfg)
  tweet = param_1
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

