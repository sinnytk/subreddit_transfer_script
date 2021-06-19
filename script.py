import os
import praw
import prawcore
import argparse
from tqdm import tqdm
from configparser import NoSectionError


DIRNAME = os.path.dirname(__file__)

def get_subreddits(praw_instance: praw.Reddit):
    subscriptions = praw_instance.user.subreddits(limit=None)
    for sub in subscriptions:
        yield sub

def exit_with_msg(msg: str):
    print(msg)
    exit(1)

def get_arguments():
    parser = argparse.ArgumentParser(description='Transfer Reddit subscriptions')
    parser.add_argument('bot_name1', type=str, 
                        help="Name of your source bot in \'praw.ini\'")
    parser.add_argument('bot_name2', type=str, 
                         help="Name of your destination bot in \'praw.ini\'")

    args = parser.parse_args()
    return args.bot_name1, args.bot_name2

def validate(praw_instance : praw.Reddit):
    try:
        print(f'{praw_instance.user.me()} logged in')
    except prawcore.exceptions.OAuthException:
        exit_with_msg(f'Invalid config for {praw_instance.config.username}, verify your praw.ini')

def main():
    bot_name1, bot_name2 = get_arguments()

    try:
        assert os.path.isfile(os.path.join(DIRNAME, 'praw.ini'))
    except AssertionError:
        print('')

    try:
        reddit1 = praw.Reddit(bot_name1, config_interpolation='basic')
    except NoSectionError:
        exit_with_msg(f'The name of your source bot \'{bot_name1}\' does not match your \'praw.ini\'')

    try:
        reddit2 = praw.Reddit(bot_name2, config_interpolation='basic')
    except NoSectionError:
        exit_with_msg(f'The name of your destination bot \'{bot_name2}\' does not match your \'praw.ini\'')

    validate(reddit1)
    validate(reddit2)


    for sub in get_subreddits(reddit1):
        s = reddit2.subreddit(sub.display_name)
        print(f'Subscribing: {s.display_name}', end=".... ")
        try:
            s.subscribe()
            print('success')
        except prawcore.exceptions.Forbidden:
            print(f'...failed. Forbidden subreddit')
        

if __name__ == '__main__':
    main()
