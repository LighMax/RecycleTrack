from config import db

import firebase_admin.exceptions as exp


def get_card_by_uid(card_id: str) -> bool:
    try:
        cards_ref = db.collection('cards')
        docs = cards_ref.stream()
        for doc in docs:
            if str(doc.id) == card_id:
                # print(f'{doc.id}->{doc.to_dict()}')
                #return True
                return doc.to_dict()
        return False
    except exp.NotFoundError as e:
        print(e.code)
        return False

def get_all_card() -> list:
    uid_list = []
    try:
        cards_ref = db.collection('cards')
        docs = cards_ref.stream()
        for doc in docs:
            uid_list.append(str(doc.id))
        return uid_list
    except exp.NotFoundError as e:
        print(e.code)
        
        