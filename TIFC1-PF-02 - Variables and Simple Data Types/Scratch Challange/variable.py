weasley = { 
    'fur': 'white and ginger',
    'eyes': 'yellow',
    'toes': 'pink'
    }
noche = {}

#Add to an existing dictionary
weasley['age'] = 1

#Copy an existing dictionary and modify the new one
bigglesworth = dict(weasley)
bigglesworth['fur'] = 'none'
bigglesworth['age'] = 666

#Populate an empty dictionary
noche['fur'] = 'black'
noche['eyes'] = 'green'
noche['toes'] = 'black'
noche['age'] = 2

print("Weasley's attributes are:")
print(weasley)
print("Noche's attributes are:")
print(noche)
print("Bigglesworth's attributes are:")
print(bigglesworth)