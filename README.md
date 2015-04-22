# python-cleanup-of-dropbox
This program removes files from a Dropbox app which are older than 10 days.

Before running this program I make sure that the server time (on which the script is run) is correct, because the program compares the Dropbox modified time and the loca server time to determine 10 days old!

NOTE: This program is for use when you are trying to clear out older files from Dropbox automatically, please take caution as running this program will delete your files.
