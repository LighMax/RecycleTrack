from config import db

import firebase_admin.exceptions as exp


def set_new_card(card_id: str, scores: int) -> bool:
    record = {
        'card_id': card_id,
        'phone': '',
        'scores': scores,
        'uid': '',
    }
    try:
        doc_ref = db.collection('cards').document(card_id)
        doc_ref.set(record)
        return True
    except exp.AlreadyExistsError as e:
        print(e.code)
        return False
        