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
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "To Do"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)