def getRating(upvotes,downvotes,timestamp):
    from datetime import datetime, timedelta
    from math import log

    
    def getTimePassed(timestamp):
        current_time=datetime.now()
        time_seconds=datetime.timestamp(current_time)
        return time_seconds-timestamp

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

    timepassed=getTimePassed(timestamp)
    rating=round(sign*order+timepassed/45000,7)        

    return rating

