# RedditWiper
Replaces your all of your reddit comments with a random string and then deletes them.

To use it adapt the config.json to your reddit api credentials and simply run it from console.
Then sit back, relax and wait a few minutes until it's done.
The script needs 4 seconds for one comment because only 30 api calls per minute are allowed and for each comment it does 2 api calls
(the replacing and the deleting).

If it didn't delete everything (which should never be the case) simply run the script again.
It might be the case that the comments you are trying to delete are archived and not editable or deletable. (AFAIK
archiving is only for posts not comments)
