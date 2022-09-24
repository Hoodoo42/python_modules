import antigravity
# one way to locally import the log.py into app.py is specifying the specific function(s) you want to use
from helpers.log import logging_logs


# and then call imported functions
logging_logs('Day One')
logging_logs('Day Two')
logging_logs('Day Three')