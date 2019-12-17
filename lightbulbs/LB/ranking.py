def getRating(upvotes,downvotes,timestamp):
    from datetime import datetime, timedelta
    from math import log

    
    def time_difference(timestamp):
        startingtime=datetime(2000,1,1)
        return timestamp-datetime.timestamp(startingtime)
   
    def getScore(upvotes,downvotes):
        return upvotes - downvotes

    score = getScore(upvotes, downvotes)
    order = log(max ( abs (score), 1), 10)
    if score > 0:
        sign = 1
    elif score < 0:
        sign = -1
    else:
        sign = 0     

    timepassed=time_difference(timestamp)
    rating=round(sign*order+timepassed/45000,7)        

    return rating



