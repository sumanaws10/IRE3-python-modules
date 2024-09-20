# access value from dict.
weasley = {'fur': 'white and ginger', 'eyes': 'yellow', 'toes': 'pink'}
# key and value is string , key is always name
print(weasley['fur'])
print(weasley['eyes'])  # access key value pair
print(weasley['toes'])

################
weasley = { 
    'fur': 'white and ginger',  # 3 key value pair
    'eyes': 'yellow',
    'toes': 'pink'}
noche = {}      # declare new dict, create empty dict.

weasley['age'] = 1  #add new key value pair , now weasley have 4 key value pair
weasley['toes'] = 'blue'     # modifies an exciting key value pair

noche['fur'] = 'black'  # start adding key value pair in empty list
noche['eyes'] = 'green'
noche['toes'] = 'black'
noche['age'] = 2

print(weasley, noche)