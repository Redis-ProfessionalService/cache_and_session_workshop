import random
import sys
import redis

from redis_connection import RedisConnection
from redis.commands.json.path import Path

FIRST_NAME = ['Aiden','Dinah','Chryses','Zamir','Bolormaa','Mahmud','Raegan','Marko','Eva','Edvin','Toni','Adalfarus','Ņina','Pitter','Taina','Gall','Rhys','Imke','Minoo','Modeste','Nereus','Hestia','Lígia','Mnason','Noureddin','Satu','Opeyemi','Finnian','Jayashri','Maira']
LAST_NAME = ['Garrett','Johns','Chandler','Kent','Rollins','Mathews','Carter','Patel','Larsen','Lozano','Wilson','Kidd','Phillips','Wall','Soto','Sims','Cole','Obrien','Bishop','Stuart','Richmond','Roach','Benson','Chambers','Walton','Terrell','Nicholson','Crane','Sexton','Cunningham']
VISITED = ['www.megashop.com','www.whatever.org','redis.io','mail.example.com','duckduckgo.com','www.example.shop','redis.io','google.com','www.example.com','www.something.com','portal.example.com']
LONLAT = ['-87.675662,41.87314','-87.634227,41.875473','-87.616911,41.865694','-87.613907,41.867452','-87.607126,41.866173','-87.6403,41.8787','-87.6051,41.8919','-87.6359,41.8789','-87.6229,41.8988','-87.64228,41.88402','-87.64338,41.88443','-87.64054,41.88186','-87.64229,41.88186','-87.64229,41.88444','-87.64054,41.88186','-87.64109,41.8799']
ITEM_LIST = [
    {"itemId":"bigaxe","itemCost":918.99,"quantity":1},
    {"itemId":"roncowidget","itemCost":69.99,"quantity":1},
    {"itemId":"superwidget","itemCost":87.99,"quantity":4},
    {"itemId":"okwidget","itemCost":39.99,"quantity":2},
    {"itemId":"shamblah","itemCost":12.98,"quantity":2},
    {"itemId":"pfffft","itemCost":14.57,"quantity":3},
    {"itemId":"coolstuff","itemCost":99.99,"quantity":1},
    {"itemId":"qwerty","itemCost":49.99,"quantity":2},
    {"itemId":"abc456","itemCost":123.45,"quantity":1},
    {"itemId":"roundtuit","itemCost":57.88,"quantity":1},
    {"itemId":"squaretuit","itemCost":47.76,"quantity":2},
    {"itemId":"squaredeal","itemCost":25.00,"quantity":5},
    {"itemId":"4square","itemCost":16.00,"quantity":4}
]


class LoadSessions():

    redis = RedisConnection.get_client()

    def load_premade():
        redis = RedisConnection.get_client()

        # a few predefined sessions so that everyone can get at least some of the same answers.
        # These all have single-digit session IDs so they're obvious.
        redis.json().set('session:1', Path.root_path(), '{"lastAccessed":1723573333,"creation":1723565555,"user": {"firstname":"Jane","lastname":"Appleseed"},"visited":["redis.io","www.example.com"], "location": "-87.6403,41.8787", "cart":[{"itemId":"invictajolly","itemCost":68.99,"quantity":1}, {"itemId":"MacBook","itemCost":2990.99,"quantity":1}]}')
        redis.json().set('session:2', Path.root_path(), '{"lastAccessed":1723572020,"creation":1723561234,"user": {"firstname":"Jonny","lastname":"Appleseed"},"visited":["www.redis.io","www.example.com"], "location": "-87.6229,41.8988", "cart":[{"itemId":"roncowidget","itemCost":88.88,"quantity":1}, {"itemId":"blahblah","itemCost":45.67,"quantity":4}]}' )
        redis.json().set('session:3', Path.root_path(), '{"lastAccessed":1723574040,"creation":1723572000,"user": {"firstname":"Paul","lastname":"Bunion"},"visited":["www.megashop.com","www.whatever.org","www.bobsburgers.com"], "location": "-87.6359,41.8788", "cart":[{"itemId":"bigaxe","itemCost":918.99,"quantity":2}]}' )
        redis.json().set('session:4', Path.root_path(), '{"lastAccessed":1723572101,"creation":1723568404,"user": {"firstname":"Carl","lastname":"Llama"},"visited":["redis.io","login.example.com"], "location": "-87.605,41.892"}' )

        return

    def load_session(how_many):

        def get_key():
            return('session:' + format(random.getrandbits(32), 'x'))

        def get_create_time():
            # returns a random time between 2:00:00 pm, Aug 13, 2024 and 2:00:00 pm, Aug 14, 2024
            return (random.randint(1723575600,1723576000))

        def get_last_active(start):
            # add random seconds to the creation time
            return (start + random.randint(0,3600))

        def get_fname():
            return (FIRST_NAME[random.randint(0, len(FIRST_NAME) - 1)])

        def get_lname():
            return (LAST_NAME[random.randint(0, len(LAST_NAME) - 1)])

        def get_location():
            return(LONLAT[random.randint(0, len(LONLAT) - 1)])

        def get_visited():
            end = random.randint(1,4)
            visited = []
            for n in range(0,end):
                visited.append(VISITED[random.randint(0, len(VISITED) - 1)])

            return (visited)

        def get_cart():
            size = random.randint(1,3)
            return(random.sample(ITEM_LIST, size))
            
        redis = RedisConnection.get_client()

        for n in range(how_many):
            key = get_key()
            created_time = get_create_time()

            session = {
                'creation': created_time,
                'lastAccessed': get_last_active(created_time),
                'user': {
                    'firstname': get_fname(),
                    'lastname': get_lname()
                },
                "location": get_location(),
                "visited": get_visited(),
                "cart": get_cart()
            }

            redis.json().set(key, Path.root_path(), session)
