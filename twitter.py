#!/usr/bin/env python2

import sys
from config import config
from twython import Twython
from generateHtmlPage import generate_html_page

# Function to exit program with printing error
def pexit(str):
    print("Error: " + str)
    exit()

# Main function
def main():

    keyword1 = ""
    keyword2 = ""

    # VALIDATING ARGUMENTS

    # if no args passed take input from stdin
    if(len(sys.argv) == 1):
        keyword1 = raw_input("Enter first keyword: ")
        keyword2 = raw_input("Enter second keyword: ")

    # if args are passed use those
    elif(len(sys.argv) == 3):
        keyword1 = sys.argv[1]
        keyword2 = sys.argv[2]

    # print error
    else:
        pexit("Invalid arguments!")

    print("First keyword: {}\nSecond keyword: {}".format(keyword1, keyword2))


    # CREATING CONNECTION

    print("[+] Initiating Connection")

    twitter = Twython(config['APP_KEY'], config['APP_SECRET'], oauth_version=2)
    config['ACCESS_TOKEN'] = twitter.obtain_access_token()

    twitter = Twython(config['APP_KEY'], access_token=config['ACCESS_TOKEN'])

    print("[+] Connection established")


    # SEARCHING KEYWORDS

    # searching keyword 1
    print("[+] Searching {}".format(keyword1))
    
    profile1 = []
    tweets_key1 = twitter.cursor(twitter.search, q=keyword1)
    
    # Populating the list of profile images of keyword 1 users
    try:
        for tweet in tweets_key1:
            profile1.append(tweet['user']['profile_image_url_https'])
    except StopIteration:
        pass

    
    count_key1 = len(profile1)
    print("Count of tweets containing {}: {}".format(keyword1, count_key1))


    # searching keyword 2

    print("[+] Searching {}".format(keyword2))
    
    profile2 = []
    tweets_key2 = twitter.cursor(twitter.search, q=keyword2)
    
    # Populating the list of profile images of keyword 1 users
    try:
        for tweet in tweets_key2:
            profile2.append(tweet['user']['profile_image_url_https'])
    except StopIteration:
        pass

    
    count_key2 = len(profile2)
    print("Count of tweets containing {}: {}".format(keyword2, count_key2))
    

    # SUMMERIZING RESULTS

    total = count_key1 + count_key2
    percent1 = (count_key1 / float(total))
    percent2 = (count_key2 / float(total))

    print("{} - percent {:.2%}".format(keyword1, percent1))
    print("{} - percent {:.2%}".format(keyword2, percent2))

    data = {
        'key1': keyword1,
        'percent1': "{:.2%}".format(percent1),
        'profile1': profile1,
        'key2': keyword2,
        'percent2': "{:.2%}".format(percent2),
        'profile2': profile2,
    }
    
    generate_html_page(data)

if __name__ == "__main__":
    main()
