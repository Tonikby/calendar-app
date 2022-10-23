from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

#import calendar
#y = int(input("Y: "))
#m = int(input("M: "))
#print(calendar.month(y,m))