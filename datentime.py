from datetime import datetime
dateNtime = datetime.now()
time = dateNtime.strftime("%I:%M %p")
date = dateNtime.strftime("%B %d, %Y")
print(time + date)