from flask import Flask
import json
from Recommender import getRecommendedItems
import databaseCon

app = Flask(__name__)

@app.route('/predictions/<int:uid>',strict_slashes=False)
def prediction(uid):
    return json.dumps(getRecommendedItems(uid),indent=2)

@app.route("/createUser/<string:uid>",strict_slashes=False)
def createUser(uid):
    con = databaseCon.Database()
    return con.insertUser(uid)

@app.route("/getUser/<string:uid>",strict_slashes=False)
def getUser(uid):
    print("Came here")
    con = databaseCon.Database()
    return json.dumps(con.getUser(uid),indent=2)

if __name__ == '__main__':
    app.run(debug=True)




