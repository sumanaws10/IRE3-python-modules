cats = {
    'weasley' : { 
        'fur': 'white and ginger',
        'eyes': 'yellow',
        'toes': 'pink'
        },
    'noche' : { 
        'fur': 'black',
        'eyes': 'green',
        'toes': 'pink'
        },
    'bigglesworth' : { 
        'fur': 'none',
        'eyes': 'red',
        'toes': 'cloven hoofs'
        }
}

for cat_name, cat_info in cats.items():
    print(cat_name)
    print(cat_info)