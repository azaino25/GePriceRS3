#The Link to graphs per item
#https://secure.runescape.com/m=itemdb_rs/api/graph/X.json
#https://secure.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=X&alpha=Y&page=Z
#X=Category of item, Y=first letter of item, Z=Page Number
#12142 = summing pot 3
import datetime


def formatEpoch(EpochDataGrabbed):
    stringLen = 13


#since all data is in Epoch/Unix time, convert to datetime
epoch_time = 1644451200000
epoch_time_formatted = epoch_time / 1000
date_time = datetime.datetime.fromtimestamp(epoch_time_formatted)
print("Epoch Time:", epoch_time)
print("real time: ", date_time)

