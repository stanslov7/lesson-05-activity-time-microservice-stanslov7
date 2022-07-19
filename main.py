"""
===============================================================
Time Microservice - lesson 05 Activity
===============================================================
Created in custom repository on 'stanslov7' Github account
in same style as previously via Github Classroom, except all
work will be committed to main branch to then be submitted
as Link to the repository for the activity itself.
===============================================================
"""
import os
import time

from flask import Flask

# Usage: when running server via Bash command: 'python main.py' ,
# then going to link provided at: "http://localhost:6787/time" ,
# Resulting page displays --> "1658244420.5917065" or similar, 
# as the current time in Epoch Timestamp in seconds.

app = Flask(__name__)

# with open('zipcodes.txt') as f:
#     zipcodes = {}
#     for line in f.readlines():
#         # print(line)
#         # print(line.strip())
#         data = line.strip().split(',')
#         zipcodes[data[0].strip()] = data[1:]


@app.route('/time')
def get_coordinates():
    # Returns the current time in seconds in Epoch Timestamp form
    return str(time.time())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)