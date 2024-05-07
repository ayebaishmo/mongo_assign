import pymongo
from sqlite_connection import connect_to_db, execute_q
import queies as q


# This format os the data from sqlite database 

# [(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)]

# Credentials 
DBNAME = 'test'
PASSWORD = 'Lord'

# define connectgion to mongo

def mongo_connect(password = PASSWORD, dbname = DBNAME, collection_name= 'test'):
    client = pymongo.MongoClient(f'mongodb+srv://ishmo:{password}@cluster0.egh1tqc.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Cluster0')
    db = client[dbname]
    collection = db[collection_name]
    return collection

if __name__=='__main__':
    # collection = mongo_connect(collection_name= 'charactercreator_character')
    # collection = mongo_connect(collection_name= 'charactercreator_character_inventory')
    # collection = mongo_connect(collection_name= 'armory_item')
    collection = mongo_connect(collection_name= 'armory_weapon')
    # for document in collection.find():
    #     print(document)

    sl_conn =connect_to_db()
    # sl_characters =execute_q(sl_conn, q.GET_CHARACTERS)
    # sl_characters =execute_q(sl_conn, q.GET_CHARACTERS_INVETORY)
    # sl_characters =execute_q(sl_conn, q.GET_ARMORY_ITEM)
    sl_characters =execute_q(sl_conn, q.GET_ARMORY_WEAPON)

    # for character in sl_characters:
    #     doc = {
    #     'character_id' : character[0],
    #     'name': character[1],
    #     'level': character[2],
    #     'exp': character[3],
    #     'hp': character[4],
    #     'strength': character[5],
    #     'intelligence': character[6],
    #     'dexterity': character[7],
    #     'wisdom':  character[8],
    #     }

    #     collection.insert_one(doc)

    # for invet in sl_characters:
    #     doc2 = {
    #         'id': invet[0],
    #         'character_id': invet[1],
    #         'item_id': invet[2],
    #     }
    #     collection.insert_one(doc2)

    # for arm in sl_characters:
    #     doc3 = {
    #         'item_id': arm[0],
    #         'name': arm[1],
    #         'value': arm[2],
    #         'weight': arm[3],
    #     }
    #     collection.insert_one(doc3)

    for arm_wep in sl_characters:
        doc4 = {
            'item_ptr_id': arm_wep[0],
            'power' : arm_wep[1]
        }
        collection.insert_one(doc4)
