import tweepy
import datetime
import sys
import xlsxwriter

auth = tweepy.OAuthHandler("key1", "key2")
auth.set_access_token("key3", "key4")

api = tweepy.API(auth)

username = input ("What's the username of the person you would like to Stalk?\n")
Startyear = int(input ("what year would you like to start? (four digits)" ))
Startmonth = int(input ("what Month would you like to start (two digits)"))
StartDay = int(input ("What day would you like to start? (two digits)"))
Endyear = int(input ("what year would you like to end? (four digits)" ))
Endmonth = int(input ("what Month would you like to end? (two digits)"))
EndDay =  int(input ("What day would you like to end? (two digits)"))

startDate = datetime.datetime(Startyear, Startmonth, StartDay, 0, 0, 0)
endDate =   datetime.datetime(Endyear, Endmonth, EndDay, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)

for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    print("Getting Tweet @", tmpTweets[-1].created_at, " - Getting some more")
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

workbook = xlsxwriter.Workbook(username + ".xlsx")
worksheet = workbook.add_worksheet()
row = 0
for tweet in tweets:
    worksheet.write_string(row, 0, str(tweet.id))
    worksheet.write_string(row, 1, str(tweet.created_at))
    worksheet.write(row, 2, tweet.text)
    worksheet.write_string(row, 3, str(tweet.in_reply_to_status_id))
    row += 1

workbook.close()
print("Excel file ready")