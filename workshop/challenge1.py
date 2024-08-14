#the completed coding challenge 1.

from redis.commands.search.field import GeoField, NumericField, TextField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query, NumericFilter

# The presumes that "from redis_connection import RedisConnection" and "redis = RedisConnection.get_client()" have previously been run

# >>> START CODING CHALLENGE <<<
index_name = 'session:index' # give your index a name

redis.ft(index_name).create_index(
    (
        NumericField("$.lastAccessed", as_name="lastAccessed", sortable=True),
        TagField("$.user.firstname", as_name="first"),
        TagField("$.user.lastname", as_name="last"),
        TextField("$.visited", as_name="visited"),
        TagField("$.cart[*].itemId", as_name="itemid"),
        GeoField("$.location", as_name="location"),
    ),
    definition=IndexDefinition(prefix=["session:"], index_type=IndexType.JSON))
# >>> END CODING CHALLENGE <<<