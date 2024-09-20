# how many parameters have dont know
def build_profile(first, last, **user_info):
    user_info['first_name'] = first #create two key-value pair and create user_info create dictonary
    user_info['last_name'] = last
    return user_info

new_user = build_profile('Antony', 'Foy', Age=41, Height="6'", Location='Manchester', Subject='Cloud')
print(new_user)

######################
# each value is key and argument is value in this exAMPLE
def build_profile(first, last, **user_info):
    return user_info

new_user = build_profile(first='Antony', last= 'Foy', Age=41, Height="6'", Location='Manchester', Subject='Cloud')
print(new_user)