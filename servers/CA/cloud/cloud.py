import firebase_admin
from firebase_admin import credentials, db, auth

# Firebase initilization
cred = credentials.Certificate("firebase-adminsdk.json")
firebase_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://smart-data-protocol.firebaseio.com'})

firebase_logs = db.reference('notifications', firebase_app)
firebase_images = db.reference('images', firebase_app)

def get_resource(resource_id):
    return firebase_images.child(resource_id).get()

def get_resource_url(resource_id):
    resource = get_resource(resource_id)
    return resource['url']

def mark_resource_accessed(resource_id):
    resource = get_resource(resource_id)
    resource['accessed'] = True
    firebase_images.child(resource_id).update(resource)

def insert_resource_certificate_request(uid, resource_id):
    user = next(x for x in auth.list_users().users if x.uid == uid)
    image = firebase_images.child(resource_id).get()
    requestsRef = firebase_images.child(resource_id).child('requests')
    requests = requestsRef.get()
    requests = requests if requests else list()
    requests.append({'userId': uid, 'userName': user.display_name, 'resourceId': resource_id, 'resourceName': image['fileName']})
    requestsRef.set(requests)

def delete_resource_certificate_request(uid, resource_id):
    requestsRef = firebase_images.child(resource_id).child('requests')
    requests = requestsRef.get()
    requests = requests if requests else list()
    unmet_requests = [x for x in requests if x['userId'] != uid]
    #if(len(unmet_requests)):
    requestsRef.set(unmet_requests)

def fire_message(action, message):
    messages = firebase_logs.get()
    messages = list() if messages == None else messages
    messages.append({'Action': action, 'Message': message})
    firebase_logs.set(messages)
