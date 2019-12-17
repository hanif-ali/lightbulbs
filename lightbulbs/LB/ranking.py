def getRating(upvotes,downvotes,timestamp):
    from datetime import datetime, timedelta
    from math import log

    
    def time_difference(timestamp):
        startingtime=datetime(2000,1,1)
        return timestamp-datetime.timestamp(startingtime)
   
    score = upvotes-downvotes

    order = log(max(abs(score), 1), 10)

    timepassed = time_difference(timestamp)

    rating = round(abs(order)+timepassed/45000,7)        

    return rating



