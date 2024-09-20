weasley = { 
    'fur': 'white and ginger',
    'eyes': 'yellow',
    'toes': 'pink'
    }

for key, value in weasley.items():
    print(f"The key is {key} and the value is {value}")


#################
weasley = { 
    'fur': 'white and ginger',
    'eyes': 'yellow',
    'toes': 'pink'
    }

for key in sorted(weasley.keys()):
    print(f"The keys are: {key}")   # extract keys in alphabatical order