from config import db


def delete_card_by_uid(card_id: str) -> bool:
    try:
        cards_ref = db.collection('cards')
        docs = cards_ref.stream()
        for doc in docs:
            if str(doc.id) == card_id:
                doc.reference.delete()
                return True
        return False
    except Exception as e:
        print(e.code)
        return False
        