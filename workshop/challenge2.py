# Answer for Challenge 2. 

# Now let's put that into practice.
# Find the sessions that have either a superwidget or an okwidget in the shopping cart
# AND is has been active since 1:15 pm today (1723576500).
# the special numeric value +inf (without any quotes) means unbounded on the upper end.

index_name = 'session:index' 

# >>> START CODING CHALLENGE <<<
# BTW, here's the CLI syntax for this search:
# FT.SEARCH session:index '@itemid:{superwidget | okwidget} @lastAccessed:[1723576500 +inf]'
# If you ever have problems with FT.SEARCH or any other coding, use the
# CLI to get a reality check. Maybe you're barking up the wrong tree.

query = '@itemid:{superwidget|okwidget} @lastAccessed:[1723576500 +inf]'

result = redis.ft(index_name).search(query)
# >>> END CODING CHALLENGE <<<

print(result)
