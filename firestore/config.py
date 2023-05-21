from firebase_admin import credentials
from firebase_admin import firestore

import firebase_admin


cred = credentials.Certificate("phoneauthflutter-203b6-137a22d9360b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
