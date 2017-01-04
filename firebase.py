import pyrebase
import datetime
import json

'''
    Firebase authentication, for saving hyper params.
'''

config = {
    "apiKey": "AIzaSyB08LCdlCdj4uCqXqhpmbYtqC97OgtGo_8",
    "authDomain": "kheiron-9df3a.firebaseapp.com",
    "databaseURL": "https://kheiron-9df3a.firebaseio.com",
    "storageBucket": "kheiron-9df3a.appspot.com",
    "messagingSenderId": "869585286373"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# load personal config file
user_data = json.load(open("user/config.json"))
# Log the user in
user = auth.sign_in_with_email_and_password(user_data["email"], user_data["password"])
# Get a reference to the database service
db = firebase.database()

#Create global vars file.
save_config = lambda MODEL_NAME, mdl: db.child("test").child(MODEL_NAME).child(datetime.date.today()).child(datetime.datetime.today().strftime('%H:%M:%S')).set(mdl, user['idToken'])