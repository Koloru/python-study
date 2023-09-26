# changeable, unordered, unique key value pars
# objects in javascript

capitals = {
    'usa': 'washington',
    'philippines': 'manila',

}

# can return an error
# capitals['usa']

# more recommended becasue it returns none and doesnt error
capitals.get('manila')

# get all the keys
capitals.keys()

# get all the values
capitals.values()

# get the whole dict
capitals.items()

# for key, value in capitals.items():
#   print(key, value)

# add a new item
# can also update an existing one
capitals.update({
    'germany': 'berlin'
})

# remove
capitals.pop('germany')
# remove all
capitals.clear()
