from config import db

def update_card_by_uid(card_id: str, record: dict) -> bool:
    try:
        cards_ref = db.collection('cards')
        docs = cards_ref.stream()
        for doc in docs:
            if str(doc.id) == card_id:
                res = doc.to_dict()
                if res['uid'] == '':
                    doc_ref = db.collection('cards').document(card_id)
                    doc_ref.update(record)
                else:
                    doc_ref = db.collection('cards').document(card_id)
                    doc_ref.update(record)

                    users_ref = db.collection('users')
                    docs = users_ref.stream()
                    for doc in docs:
                        if str(doc.id) == res['uid']:
                            user_res = doc.to_dict()
                            user_res['scores'] = record['scores']
                            doc_ref = db.collection('users').document(res['uid'])
                            doc_ref.update(user_res)
        return True
    except Exception as  e:
        print(e.code)
        return False