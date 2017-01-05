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

#For Database - constant
DATE_RAN = datetime.date.today()
# Retrieve Last known run.
try:
    returned_list = [db.child("test").child(MODEL_NAME).child(DATE_RAN).shallow().get(user['idToken']).val())]
    LAST_RUN = sorted([i.split(":")[1].split("_")[0] for i in returned_list])[-1]
except TypeError:
    LAST_RUN = 1
#Create global vars file.
save_config = lambda MODEL_NAME, mdl: db.child("test").child(MODEL_NAME) \
										.child(DATE_RAN) \
										.child(str(LAST_RUN+1)+'_'+user_data["username"]) \
										.set(mdl, user['idToken']) 

save_output = lambda logs: db.child("test").child(MODEL_NAME) \
										.child(DATE_RAN) \
										.child(str(LAST_RUN+1)+'_'+user_data["username"]) \
										.update(logs ,user['idToken'])
