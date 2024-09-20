
# List is nested inside the dict
bigglesworth = { 
    'fur': 'none',
    'eyes': 'souls of the damned',
    'toes': 'cloven hoofs',
    'favourite foods': ['joy', 'happiness', 'souls', 'tuna - occasionally']
    }
# Favourite foods is list
for food in bigglesworth['favourite foods']:
    print(f"Bigglesworth just loves eating {food}")