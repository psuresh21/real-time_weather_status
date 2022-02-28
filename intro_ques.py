import re
import datetime
from weather_report import copyright_intro


print(copyright_intro())
myline = "___________________________________"
status_name = " enter your country name\n for weather status"


print(myline)
print(" ")
print(status_name)
print(myline)
print(" ")


ask_weather = str(input('=> '))
mycountry = re.sub(' ','+',ask_weather)
print(" ")
