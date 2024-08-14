from redis_connection import RedisConnection
# load restaurants db

redis = RedisConnection.get_client()

# syntax geoadd('key', (longitude, latitude, name))
key_name = 'chicago_restaurants'

pipe = redis.pipeline(transaction=False)
pipe.geoadd(key_name, (-87.628662, 41.879341, 'The Berghoff Restaurant'))
pipe.geoadd(key_name, (-87.64109, 41.8799, 'Dylans Tavern & Grill'))
pipe.geoadd(key_name, (-87.64228, 41.88402, 'Sepia'))
pipe.geoadd(key_name, (-87.64054, 41.88186, 'Soul & Smoke'))
pipe.geoadd(key_name, (-87.64338, 41.88443, 'avec Restaurant'))
pipe.geoadd(key_name, (-87.6397, 41.88379, 'Station Restaurant & Bar'))
pipe.geoadd(key_name, (-87.626282, 41.880390, 'Millers Pub'))
pipe.geoadd(key_name, (-87.64054, 41.88186, 'Madison Tavern'))
pipe.geoadd(key_name, (-87.64229, 41.88444, 'Alla Vita'))
pipe.geoadd(key_name, (-87.632820, 41.879169, 'The Florentine'))

pipe.execute()