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

noche = {}
#Populate an empty dictionary
noche['fur'] = 'black'
noche['eyes'] = 'green'
noche['toes'] = 'black'
noche['age'] = 2

bigglesworth = dict(noche)
print(bigglesworth)

#delete a value from a dict
del bigglesworth['fur'] # #because he doesnt have any
print


print("Weasley's attributes are:")
print(weasley)
print("Noche's attributes are:")
print(noche)
print("Bigglesworth's attributes are:")
print(bigglesworth)