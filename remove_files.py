#imports
import dropbox
import datetime

def getPresent():
    #obtain and convert the server time to year, month, date
        current_time = datetime.datetime.now()
        current_year = current_time .year
        current_month = current_time .month
        current_day = current_time .day
        present = datetime.datetime(current_year, current_month, current_day)
        return present

def getTimeDifferenceInSeconds(present, past):
    d = present - past
    return d.total_seconds()

def getDeletionApproval(timeDifferenceInSeconds):
    # 1, 209, 600 seconds in 10 days
    if timeDifferenceInSeconds > 864000:
        return True

def deleteTheFile(pathToFile):
        client.file_delete(pathToFile)

#get the current date
present = getPresent()

#access the drop box account
client = dropbox.client.DropboxClient("_GSRrTwYHmEAAAAAAAAAB1zpOghn4aJz2E04vC-lmC-oENW1pv0O3DUccAkoV43h")

#get a dict of all files in the specific dropbox api folder
folder_metadata = client.metadata('/')

#load the contents dict (actual list of files within the app folder) into a list variable
md = folder_metadata["contents"]
#check that we don't delete files in the even that the files have stopped being placed in Dropbox by the back up script (want at least 5 files on hand)
#TODO perhaps find the difference in seconds for all files and delete from oldest to newest until either all old ones are gone or there are only 5 of the newest remaining
if len(md) > 5:
        #loop through the contents
        for item in md:
                #reset deletion approval to false
                deletionApproval = False
                #obtain and convert dropbox date to year, month, date
                t1 = datetime.datetime.strptime(item["modified"],'%a, %d %b %Y %H:%M:%S +0000')
                year = t1.year
                month = t1.month
                day = t1.day
                past = datetime.datetime(year, month, day)
                #get the time difference in seconds
                timeDifferenceInSeconds = getTimeDifferenceInSeconds(present, past)
                #get approval to delete (default file must be 14 days or older)
                deletionApproval = getDeletionApproval(timeDifferenceInSeconds)
                if deletionApproval == True:
                    deleteTheFile(item["path"])
