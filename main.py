import praw
import json
import random
import time
config = json.load(open('config.json'))
charstring = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz><.-,+!@#$%^&*();:[]~"


def get_comments():
    reddit = praw.Reddit(client_id=config["reddit"]["clientid"],
                         client_secret=config["reddit"]["clientsecret"],
                         user_agent=config["reddit"]["useragent"],
                         username=config["reddit"]["username"],
                         password=config["reddit"]["password"])
    return reddit.user.me().comments.new(limit=None)


def replace_delete_comments(comments):
    for cur_comment in comments:
        commentsize = random.randint(50, 300)
        replacementstring = ""
        for k in range(0, commentsize):
            replacementstring += charstring[random.randint(0, len(charstring)-1)]
        cur_comment_fullname = cur_comment.fullname
        cur_comment.edit(replacementstring)
        # request limit of 30 per min
        time.sleep(2)
        cur_comment.delete()
        time.sleep(2)
        print("Replaced & deleted: " + str(cur_comment_fullname))


if __name__ == "__main__":
    mycomments = get_comments()
    print("Retrieved comments from your Account!")
    replace_delete_comments(mycomments)
    print("Finished wiping your reddit comments!")


