#!/usr/bin/env python
#https://github.com/nicholasserra/reddit-simple-media-scrape/blob/master/reddit_scrape.py
#https://crypto.stackexchange.com/questions/26336/sha-512-faster-than-sha-256 

from   argparse import ArgumentParser 
import requests
import hashlib
import sys
import os
import re


class RedditScrape(object):
    PROFILE_URL = 'https://www.reddit.com/user/{}/submitted.json'


    def __init__(self, username, directory):
        assert os.path.isdir(directory), RuntimeError('Invalid directory')
        self.username  = username
        self.directory = directory


    def scrape(self):
        directory  = self.directory + os.sep + self.username
        if not os.path.exists(directory):
            os.mkdir(directory)
        count      = 0
        user_url   = self.PROFILE_URL.format(self.username)
        user_agent = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0'}
        while True:
            response = requests.get(user_url, headers=user_agent).text
            hash_rsp = hashlib.sha512(str.encode(response)).hexdigest() # <-- long story to explain why i did this silly thing and why i first thought that would be a clever thing to do, lol.
            if not os.path.exists(directory + os.sep + hash_rsp + '.json'):
                file = open(f'{directory}{os.sep}{hash_rsp}.json', 'w+')
                file .write(response)
                file .close()
            after_id = re.search('(?<="after": ").*?(?=")', response)
            if after_id : user_url = self.PROFILE_URL.format(self.username) + '?after={}'.format(after_id.group(0))
            else        : break
            count += 1
            sys.stdout.write('.')
            sys.stdout.flush()
        print('\n{} files saved.'.format(count))



def main():
    parser  = ArgumentParser   (description="Reddit simple media scraper.")
    parser.add_argument        ('username' , nargs='?', type=str , help='Username of the user you want to get the data')
    parser.add_argument        ('directory', nargs='?', default=os.path.dirname(os.path.realpath(__file__)))
    args    = parser.parse_args()
    scraper = RedditScrape     (args.username, args.directory)
    scraper.scrape             ()


if __name__ == '__main__':
    main()

#python reddit_scrapper.py username