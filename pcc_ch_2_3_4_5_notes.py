#Changing Case in a String with Methods 
import itertools
import random
from random import choice, sample
character = "swamp thing"
print(character.title()) # or .upper / .lower

first_name = "kim" # begin using pyton preferred naming. Variables are lowercase w/ underscore, same for py filenames 
last_name = "gordon"
full_name = f"{first_name} {last_name}" # one option: combine variables into NEW variable
print(f"What's up, {full_name}?")
# print(f"{first_name} {last_name}") # or include straight into fnx 

# \t tab \n 
print(f"Cool Band Members:\n\t{full_name}\n\tThurston Moore")

favLang = 'autohotkey   '
newFavLang = favLang.rstrip() # the method only acts temporary, must be assigned to new variable / also .lstrip and .strip

# Removing Prefixes
ASLP_Url = 'https://automatedslp.com'
simplifiedUrl = ASLP_Url.removeprefix('https://').removesuffix('.com') # like above, method adjusted str must be saved to new var to use
print(simplifiedUrl)

# Numbers 
bezosWorth = 146_000_000_000 #underscores can serve as commas
print(bezosWorth + bezosWorth) 
# Multiple Assignments
a, b, c = "Python", "C", "Autohotkey"
print(a, b, c)

# Constants
MAX_POWER_LEVEL = 25_000 # constants are in all caps

import this # The Zen of Python. Use Shift + Enter to run in cmi 
print("\n\n")
      

##################################################################
# CHAPTER 3: INTRODUCING LISTS

cities = ["belvidere", "bangor", "richmond", "mount bethel", "strousburg"]
print(cities[-1].title())  # add case method immediately after index, don't forget method ()
cities_thought = f"Our first dream city was {cities[-1].title()}, our newest is {cities[0].title()}."
cities_thought2 = f"But the best food was in {cities[2].upper()}"
print(cities_thought, cities_thought2)

# Modifying Lists
cities[0] = 'east hampton'
cities.append('clifton')
print(f" appended clifton {cities}")
cities.insert(-1, 'flemington') #inserts before index -1
del cities[-3] # deletes strousburg. Use del when you know the index, this updates reference list
too_grungy = 'mount bethel'
cities.remove(too_grungy) # putting in a variable allows removed item to be used in the future 
print(f'{too_grungy.title()} was too grungy for me and was removed by value.')
print(cities)

degrees = [] # append to empty list, dynamically updated, won't always know what to include, let's user update
degrees.append('AA')
degrees.append('Sociology')
degrees.append('Slpa')

#pop() Method # removes item, but saves for future use
print(f'degrees = {degrees}')
popped_degrees = degrees.pop() # what is 'popped' is what is saved into new variable
print(f' degrees post pop = {degrees}') # degrees
print(f' popped degree = {popped_degrees}') # pop() mutates actual list

#pop() from any index
goal_domains = ['articulation', 'language', 'fluency', 'syntax', 'semantics', 'pragmatics', 'voice']
print(f'\ngoal domains = {goal_domains}')
first_domain = goal_domains.pop(0)
print(f' goal_domains = {goal_domains} popped first domain = {first_domain}')





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROJECT _ CHANGING GUEST LIST 3.5 
guest_list = ['pee wee herman', 'klaus nomi', 'brian eno', 'norm mcdonald', 'dino from dystopia']

cancelled_guest = guest_list.pop(-1) # Cancellation occurs. Pop() removes guest and saves to var
print(f'\nSorry to inform you, but {cancelled_guest} is unable to make it.\n')

guest_list.append('dr. lee')
guest_list.insert(0, 'keanu reeves') # invite new guests
guest_list.insert(3, 'carl sagan') 
guest_list.append('alex g')

for guest in guest_list: 
    print(f'Hello, {guest.title()}! You have been invited to the Allen-Contessa Family Dinner Celebration on December 12th 2023!') # invitation

print('\n') # cancellations to all but two guests due to small table 
while len(guest_list) > 2:
    print(f'Sorry to inform you, {guest_list[-1]}, but our accomodations have changed and we will have to cancel the Allen-Contessa Celebration Dinner. Thank you for understanding')# Shrinking guest list 
    guest_list.pop() 
 
print('\n') # notify remaining guests
print(f'Hello again, {guest_list[0].title()}! We have changed our venue size, however, you are still invited to the reduced capacity venue. Hope to see you there!')
print(f'Hello again, {guest_list[1].title()}! We have changed our venue size, however, you are still invited to the reduced capacity venue. Hope to see you there!')
print(f'Number or guests: {len(guest_list)}') 
while len(guest_list) > 0: # clear list
    del guest_list[0]
print(guest_list)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Sort() method
skateboards = ['world industries', 'element', 'blind', 'deathwish']
skateboards.sort() # this is a permanent method, updates original list. Can use reverse=True key
print(f'\n{skateboards}')
skateboards.reverse() # simply flips the list in place, permanently. Not alphabethical, simply flip again to reset
print(skateboards)

# sortED() FUNCTION - Does not affect actual listexercises = ['bench', 'row', 'squat', 'kb swing', 'curl'
exercises = ['bench', 'row', 'squat', 'curl', ' kb swing', 'ohp']
print(f'Here is sorted exercises: {sorted(exercises)}') # diff from sort method, does not modify
print(f'Here is original exercises: {exercises}') # main list is unchanged



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# PROJECT 3.8 SEEING THE WORLD 
places_to_go = ['london', 'boston', 'burlington', 'chicago', 'florida']
print(f'Places to visit original: {places_to_go}')
print(f'Places to visit sorted: {sorted(places_to_go)}')
print(f'Current state of places to visit list: {places_to_go}') # show list is unchanged
places_to_go.reverse() # modifies in places, SO MUST BE PROCESSED FIRST BEFORE PRINTING  
print(f'Here it is reversed: {places_to_go}') # flipped

print(f'Here it is reversed again: {places_to_go}') # flipped again 
places_to_go.sort() # modifies in place
print(f'Sorted places to visit: {places_to_go}')
places_to_go.sort(reverse=True)
print(f'Places to go reverse sorted: {places_to_go}')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# CHAPTER 4 Working with List      
print('\n') # a print function is also called a print 'call'  
for place in places_to_go: 
    print(f'{place.title()} would be a great place to go.')     
print('Any of these would be great places to go!\n') # After a loop, you may want to SUMMARIZE

# 4.1 Pizzas Loop
pizza = ['plain slice', 'margarita', 'mushroom']
for style in pizza: 
    print(f'{style} is a good pizza option.')
print('All are good pizza option.\n') # Summary of loop 

bugs = ['spider', 'cockroach', 'ladybug', 'rollie pollie']
for bug in bugs: 
    print(f'A {bug} would make a good pet')
print('These are all bugs that could be pets.\n')


# range() function
for value in range(5):  
    print(value)
    
even_numbers = list(range(2,12,2)) # 3rd key is step size/skip
print(even_numbers) # pep standards are underscores

squares = []
for value in range(1,11): # 1st 10 cubed numbers
    squares.append(value**3) # note subtle diff / list is plural
print(squares)

# simple statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min(digits)
max(digits)
sum(digits)

# LIST COMPREHENSION
squares = [value**2 for value in range(1, 11)] # ['define expression for values to store in list' followed by 'for loop']  
print(f'List comprehension squares: {squares}\n') # the for loop section 'feeds into' the value section

# PROJECT _ Count to 20
# for num in range(1, 21): # 1st num inclusive, 2nd exclusive
#     print(num)

# for num in range(20): # alternate version w/ + 1  
#     print(num + 1)
# print('\n')

# One Million
# million = [print(num) for num in range(100_000_000)] #  list comprhensions seem to run faster
# Summing a Million
# million = list(range(1, 100_000_001))
# print(min(million)) # check min and max for accuracy
# print(max(million))
# print(sum(million))

# odd num 
odd_num = list(range(1, 20, 2)) # going from 1 to 3 is an inc of 2, but maintains odd interval
for num in odd_num: 
    print(num)
print('Odd num\n')

threes = list(range(3, 31, 3)) 
for three in threes:
    print(three)
print('Every 3rd num from 3 to 30\n')

cubes = list(range(1, 11)) # create a list of 1-10
for cube in cubes:
    print(cube**3)
print('These were cubes\n')   

# list comprhension cube
# cubes = [cube**3 for cube in range(1, 11)]
# for x in cubes:
#     print(x)  

# Working with part of a list
print(places_to_go)
print(places_to_go[-3:]) # prints the last 3, no matter size of list - could be used for a games Top 3 Scores (if sorted)

print('\nHere are the first 3 places I might like to visit:')
for place in places_to_go[:3]: # Loops only a PORTION of the list
    print(place.title())

# COPYING A LIST 
# Note: Lists are MUTABLE. Assigning a list to a new var does NOT copy
fav_foods = ['tacos', 'indian', 'sushi', 'pot roast']
friend_foods = fav_foods[:] # if friend liked all the same foods, : 'full slice' is one way to copy list

fav_foods.append('lemon chicken') 
friend_foods.append('honey baked ham')

print('\nMy favorite foods are:') 
print(fav_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods) 

# 4.10 SLICES _ TRY IT YOURSELF
print(f'The first three items in exercises are: {exercises[:3]}')
print(f'3 from the middle are: {exercises[2:5]}')
print(f'The last 3 are: {exercises[-3:]}')

# 4.11 My Pizzas, Your Pizzas
print(f'\nMy Pizza List:')
for x in pizza:
    print(x.title())

friends_pizza = pizza[:] # make a copy of pizza
friends_pizza.append('sausage and peppers')
friends_pizza.append('chicken and spinach')
print(f"\nFRIEND'S PIZZA LIST:")
for pizza in friends_pizza:
    print(pizza.title())      
print("These were your friend's favorite pizza's.\j")
for food in fav_foods:
    print(food)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# TUPLES
# TUPLES cannot be modified, aka are immutable
dimensions = (200, 50)
print(f'\n Original Dimensions:\n{dimensions[0]}')
print(dimensions[1])

dimensions = (400, 100)
print(f'\nModified Dimensions:\n{dimensions[0]}')
print('dimensions[1]\n')

buffet_foods = ('prime rib', 'omelette', 'mashed potatoes', 'salad bar', 
                'mac and cheese') # tuples work same as lists
for food in buffet_foods: 
    print(food)
print('\n') # needs to be completely updated if tuple needs to be changed
buffet_foods = ('baked ham', 'green beans', 'baked potatoes', 'fruit', 
                'mac and cheese') 
for fod in buffet_foods:
    print(food)
print('These were buffet foods\n')

# Pep8 Style Guidelines

# Snake_case for variables, DIMENSIONS (all caps for constants), 
# Programs: lowercase, one-word preferably, or _ sep (my_program, or program)
# Lean towards writing readable code vs. code that's easy to write
# Tab must be 4 spaces (check editor) 
# Lines should be 79 char or fewer, comments 72 due to formatting             
# Use blank lines to seperate code, but not excessively
# Operators like = should have a space after unless to show precedence
    # Example of acceptable use of precedence: (a*b) + (b-c)
# Operators, another exception: (key=True) or (rev=True)
# Space after # comment is appropriate
# Don't use "if x == None", use "if x is None"
# Use "if foo.startswith("bar") instead of "if foo[:3] == "bar":
    # startswith fnx is more performative

# CHATR 5: IF STATEMENTS

# bands.py (adapted from cars.py)
bands = ['dead kennedys', 'the descendents', 'electro hippies', 'nofx', 'mxpx']
for band in bands:
    if band == 'mxpx' or band ==  'nofx':
        print(band.upper())
    else:
        print(band.title())
print('These are good bands\n')        

band = 'MXPX' 
band.lower() == 'mxpx' # use .lower to account for various capitalization, does not update variable in place

requested_songs = 'slowly going the way of the buffalo'

if requested_songs != 'freebird': # if True, loop executes 
    print('Hold the Freebird!\n')

answer = 123
if answer != 42:
    print('That is incorrect. Please try again') 
print('\n')

age = 21
age == 21

age < 21 # false if age is 21, < is exclusive
age <= 21 # True if 21, <= is inclusive
age > 21 
age >= 21 

# CHECKING MULTIPLE CONDITIONS
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # false

age_1 = 22 # if this age increases
(age_0 >= 21) and (age_1 >= 21) # both sides become true, parentheses optional

age_0 = 2
age_1 = 18
age_0 >= 21 or age_1 >= 21

# Checking for a Value in a List
requested_features = ['fast pace', 'melodic', 'major key', 'female vocals']
'melodic' in requested_features
'minor key' in requested_features

banned_users = ['groggyOtter', 'ExpiredDebitCard', 'pythonisbetter']
user = 'Weekend Nanchos'
if user not in banned_users:
   print(f'{user.title()}, you can post a response if you wish.') 

# BOOLEAN EXPRESSIONS - A way to track states
user_active = True 
able_to_comment = True 
banned_account = False 

game_active = True 
can_edit = False 
# Practice Equivalency Tests
occupation = 'slpa'
print('Is occupation programmer? I predict True.')
print(occupation == 'programmer\n')
print('Is occupation slpa? I predict True.')
print(occupation == 'slpa')
car = 'camry'
print('Is car a camry? I predict True')
print(car == 'camry')
print('Is car a Jaguar? I predict False')
print(car == 'Jaguar')
skateboard = 'Inactive'
print('Skateboards active? I predict False')
print(skateboard == 'active')
sleep = 'inadequate'
print('Sleep is adequate? I predict False')
print(sleep == 'adequate')
wife = 'amazing'
print('Your wife is amazing? I predict True')
print(wife == 'amazing')
family = 'great'
print('Your family is great? I predict True')
print(family == 'great')
coffee = 'lifesaver'
print('Is coffee a lifesaver? I predict True')
print(coffee == 'lifesaver')
fourpm_coffee = 'not a good idea'
print('A 4pm coffee is a good idea? I predict False')
print(fourpm_coffee == 'good idea')
exercise = 'good idea'
print('Exercise is a good idea? I predict True')
print(exercise == 'good idea')

print(1 == 1) # False
print(1 == 2 ) # True
print(1 > 2) # True
print(1 >= 1) # True
print('joe' == 'joe') # True
print('a' < 'b') # True, ASCII
print('a' > 'c') # False
print('Joe'.lower() == 'joe') # 
print('HeLlO, mY NaMe iS MuD'.lower() == 'Hello, my NAME IS Mud'.lower()) # True
print('JOE'.lower() != 'joe') # False
print((2 * 2) + 1 == (2 * 2) + 1 and 1 < 2 and (3 * 5 == 15)) # True
print((2 * 2) + 1 == (2 * 2) + 1 and 1 < 2 and (3 * 5 == 17)) # False 
print('joe' == 'john' or 'emily' == 'emily') # True
'deadlift' in exercises # False
'deadlift' not in exercises # True 
'curl' in exercises # True 

# If Statements 

# voting.py 
age = 18
if age > 18: # if condition passes
    print('You are old enough to vote') # anything indendeted passes
    print('Have you registered to vote yet?\n')
else: 
    print('Sorry, you are too young to vote')
    print('Please register to vote as soon as you turn 18\n')
# in a simple if/else statement, one of two conditions will always execute
# It is more effcient to have the more likely condition first


# THE IF-ELIF-ELSE CHAIN
age = 19
if age < 4: 
    print('Children Under 4: Free\n')
elif age < 19: 
    print('Child Admisssion: $25\n')
else: 
    print('Regular Admission: $40\n')

# More concise version w/ single print AFTER chain
# IF-ELIF-ELSE chain has narrower purpose and is easier to modify
# If you need to modify the print statement, it now only requires ONE change0.
age = 65
if age < 4:
    price = 0
elif age <9:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: # Final Else not required.               
             # Use additional elif if more descriptive. Final elif can even be more reliable/secure
    price = 20
print(f'Your adimssion price is ${price}\n')

# jersey_mikes.py 
requested_sandwich = ['bread', 'turkey', 'mikes way']
if 'bread' in requested_sandwich: 
    print('Adding bread.')
if 'turkey' in requested_sandwich:
    print('Adding turkey')
if 'mikes way' in requested_sandwich: 
    print('Adding Mikes Way')
print('\nFinished your sandwich!\n')
 
# 5-3. Alien Colors  
alien_color = 'green'
if alien_color == 'green': 
    print('+5 Points!')
elif alien_color == 'yellow': 
    print('+10 Points!')
else: 
    print('+15 Points!')

alien_color = 'yellow'
if alien_color == 'green':
    print('+5 Points!')
elif alien_color == 'yellow':
    print('+10 Points!')
else:
    print('+15 Points!')

alien_color = 'red'
if alien_color == 'green':
    print('+5 Points!')
elif alien_color == 'yellow':
    print('+1 Points!')
else:
    print('+15 Points!')

# 5-6 STAGE OF LIFE
age = 35
if age < 2: 
    print('\nYou are a baby\n')
elif age < 4: 
    print('\nYou are a toddler\n')
elif age < 13: 
    print('\nYou are a kid\n')
elif age < 20: 
    print('\nYou are a teenager\n"]')  
elif age < 65:  
    print('\nYou are an adult\n')
else: 
    print('\nYou are an elder\n')

fav_fruits = ['prunes', 'banana', 'prunes again', 'blueberries', 'cooked apples']
if 'prunes' in fav_fruits: 
    print('You really like prunes')
if 'apples' not in fav_fruits:
    print("You don' like apples much")
if 'blueberries' in fav_fruits:
    print('You like blueberries')    
if 'cooked apples' in fav_fruits:        
    print('I agree cooked apples are better')
if 'banana' in fav_fruits:    
    print('You like bananas\n') 

pot_roast_inventory = ['chuck roast', 'potatoes', 'carrots', 'garlic', 'onion']
pot_roast_requested = ['chuck roast', 'potatoes', 'garlic', 'shitakes', 'leeks', 'carrots', 'onion']
pot_roast_missing = ['garlic', 'carrots']
if pot_roast_requested:                                                         # if list is not empty
    for requested in pot_roast_requested:                                       # loop through list of requested ingredients 
        if requested in pot_roast_missing:                                      # if ingredient missing 
            print(f'Sorry. we are out of {requested}')                          # print missing
        elif requested in pot_roast_inventory:                                  # elif requested is in possible ingredients
            print(f'Adding {requested}.')                                       # add ingredient
        else:                                                                   # else
            print(f'Sorry. We do not carry {requested}')                        # print 'do not carry'
else:             
    print('Are you sure you would want plain broth?')
print('Your pot roast is done.\n')


# HELLO ADMIN
usernames = ['admin', 'PrinceTon5', 'NOTyourfriendfriend', 'aurabora98', '15SLOths', 'ruralrusty']
usernames_lower = [user.lower() for user in usernames] # list comprehension to .lower() copy list
new_users = ['johnny5times', 'admiN', 'hi', '15SLOTHS']
new_users_lower = [user.lower() for user in new_users]

# Checking Usernames
for user in new_users_lower:
    if user in usernames_lower:             # if lowered new in lowered original
        print(f'{user} has been used. Please enter a new name.')
        for user1 in usernames[:]:          # loops through a copy [:] original list
            if user1.lower() ==  user:      # if origninal lower.user = deleted_user
                usernames.remove(user1)     # remove from original list 
    else:
        print(f'{user} is available.')
        usernames.append(user)

if usernames: # if list is not empty
    for username in usernames:
        if username == 'admin':
            print(f'Hello, {username}. Would you like to see a status report?')
        else:
            print(f'Hello, {username}. Thank you for logging in.') 
else:
    print('There are no users in the list')
usernames.clear() # could also assing list to []. Can loop .pop(), but pop() is for seeing removed items, not clearing.
print(usernames)    

# ORDINAL NUMBERSr
one_through_nine = []                 # loop with append
for num in range(1, 10):
    one_through_nine.append(num)
print(one_through_nine)

one_through_nine1 = list(range(1,10)) # same, but list and range "pythonic" approach
print(f'{one_through_nine1}\n')

for num in one_through_nine1: # print w/ appropriate suffix  
    if num == 1:
        print(f'{num}st')   
    if num == 2:
        print(f'{num}nd')
    if num == 3: 
        print(f'{num}rd')
    else: 
        print(f'{num}th') 
        


# DICTIONARIES _ CH 6
alien_0 = {'color': 'green', 'points': 5} # braces for dict

new_points = alien_0['points']
print(f"You just earned {new_points} points!")        # save to new var
# print(f"You just earned {alien_0['points']} points!") # can also put straight in

# ADDING NEW KEY-VALUE PAIRS
alien_0['x_position'] = 0 # assing new values to dict dynamically 
alien_0['y_position'] = 25
print(alien_0)

# Staring with Empty Dict
# Use this method for user entere data or with code that automatically generates key-value pairs
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 15

# Modifying Dict
alien_0 = {'color': 'green'} # set to grn
alien_0 = {'color': 'yellow'} # change to yellow 
print(f"The alien is now {alien_0['color']}.\n")


alien_0 =  {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 5}
print(f"Original position: {alien_0['x_position']}") # use double quote since dict (and lists) often use str with ''

# Move the alien to the right
# Determine how far to move based on current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] ==  'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}") # MUST use "" on outside  

# Remove Key-Value Pair
del alien_0['points']
print(alien_0)

# Dict of similiar items
favorite_speech_activities = { 
    'nick': 'flashcards',      # must be indented (use shortcut ctrl+[] if needed)
    'john': 'zelda',
  'marcus': 'mario pronouns', 
    'julio': 'flashcards', 
    }

activity = favorite_speech_activities['john'].title()
print(f"John's favorite activity is {activity}.\n")

# Using get() to Access Values
point_value = alien_0.get('points', 'No point value assigned.') # use if value may not exist.
# If no exception added as 2nd argument, returns None- a special value meaning no value
print(point_value) # variables do not need '', they are not str 


# 6.1 Person: Try it yourself
ryan = {'first name': 'ryan', 'last name': 'heck', 'age': 35, 'location': 'palmdale', 'career': 'construction', }
print(ryan['first name'])
print(ryan['last name'])
print(ryan['location'])
print(ryan['career'])

# 6.2 Favorite Numbers 
favorite_numbers = {'ryan': 45, 'nick': 42, 'kelly': 86, 'frank': 31, 'rita': 31}
print(f"Nicks's favorite number: {favorite_numbers['nick']}")
print(f"Kelly's favorite number: {favorite_numbers['kelly']}")
print(f"Frank's favorite number: {favorite_numbers['frank']}")
print(f"Rita's favorite number: {favorite_numbers['rita']}")
print(f"Ryan's favorite number: {favorite_numbers['ryan']}\n")

6.3 # Glossary (aka 'traditional dictionary')
programming_terms = {}
# practice adding to empty dict
programming_terms['list'] = 'Cycles through items sequentially. References using indexes'
programming_terms['dict'] = 'Select info based on key vaule pairs. Referencing not sequential. Like a list of variables'
programming_terms['function'] = 'A reusable block of code that can be called'
programming_terms['parameter'] = 'The value entered into an argument to be passed to a function call'
programming_terms['method'] = 'A function (associated w/ a class) that acts on the data of an object (chatgpt)'      

for term, definition in programming_terms.items():  
    print(f"{term.title()}: {definition}")

# # # # # # # # # # # # # # # # # # # # # # # # # 
# Looping through a dictionary
user_0 = {
    'username': 'weekend_nanchos', 
    'first name': 'great hardcore band',  
    'last name': 'of all time'
    }
for key, value in user_0.items(): # SURE TO ADD .ITEMS() METHOD
    print(f"\nKey: {key}") # printing on 2 sep lines follows user/pw format  
    print(f"Value: {value}")

for name, activity in favorite_speech_activities.items(): # MUST INCLUDE .ITEMS() to have TWO ITEMS  
    print(f"\n{name.title()}'s favorite speech activity is {activity}.")

family = {'kelly', 'frank', 'rita'}
for name in favorite_numbers.keys(): # Use keys method for just keys 
    print(name)
    if name in family:               # special message for family members
        print(f"{name}, you are family")
    elif name not in family and name != 'nick': 
        print(f"Sorry {name}, you are not family")
    elif name == 'nick':
        print("Nick, you are yourself.")    
    
if 'jen' not in favorite_numbers.keys(): # able to make conditions for dict just like lists
                                         # not just for looping, keys() actually returns sequence of keys                                     
    print(f"Jen, please report your favorite number\n")

# SORTED DICTIONARY - o/w, they are unsorted. Use sorted()
for name in sorted(favorite_numbers.keys()):
    print(f"{name.title()}, thank you for reporting your favorite number")

# Looping through VALUES in a DICT
print("\nThe following numbers have been mentioned:")
for fav_number in favorite_numbers.values():
    print(fav_number)
    if fav_number == 42:
        print(f"Btw, {fav_number} is the best number") 
print("")  

# Set() - collection in which each item must be unique
# Sets exist but can also call set func on dict
for fav_number in set(favorite_numbers.values()): 
    print(fav_number)
    
# Try it Yourself - 6.4 Glossary 2  
# Glossary (aka 'traditional dictionary')
programming_terms = {}
# practice adding to empty dict
programming_terms['list'] = 'Cycles through items sequentially. References using indexes'
programming_terms['dict'] = 'Select info based on key vaule pairs. Referencing not sequential. Like a list of variables'
programming_terms['function'] = 'A reusable block of code that can be called'
programming_terms['parameter'] = 'The value entered into an argument to be passed to a function call'
programming_terms['method'] = 'A function (associated w/ a class) that acts on the data of an object (chatgpt)'
programming_terms['list comprehension'] = "A one line for loop. 'print(hi) for x in range (10)'. The format is Expression for Item in Iterable (optional If)"
programming_terms['slice'] = "Takes the a RANGE or selection of elements from a list"
programming_terms['nesting'] = "Putting elements inside other elements. If's, Lists and Dicts can all be nested"
programming_terms['conditional test'] = 'Any statement that evaluates to True/False'
programming_terms['boolean expression'] = 'Another name for a conditional TEST that results in a Boolean Value, i.e. True/False, 1/0'
for term, definition in programming_terms.items():
    print(f"{term.title()}: {definition}")
print('These were programming terms.\n')

# 6.5 Rivers
rivers = {'the u.s': 'mississippi', 'china': 'yangtze', 'south america': 'amazon'} 
for river in rivers.values():
    print(f'Value: {river}')
for country in rivers.keys():
    print(f'Key: {country}')
for country, river in rivers.items():
   print(f"The {river} river runs through {country}.")  
print('These were rivers\n')

# 6.6 Polling: 
# List of people to take favorite speech activities poll
have_not_taken_poll = ['john', 'jose', 'julio', 'diana', 'abe', 'jacob']
for name in have_not_taken_poll: 
    if name not in favorite_speech_activities.keys():
        print('You have not taken the favorite speech activity poll. Please, complete.')
    else:
         print('Thank you for taking the speech poll.')
print('This was data for a speech poll.\n')


# NESTING
# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15} 

aliens = [alien_0, alien_1, alien_2]
for alien in aliens: 
    print(alien) 
print('This was dictionary of a dictionary.\n')     

# make 30 aliens
aliens = [] #  make empty list for storing aliens

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the 1st 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")    

# Show how many aliens have been created 
print(f"Total number of aliens: {len(aliens)}\n")


# Lists within a Dictionary 
# info for sandwich
sandwich_options = {
    'bread': ['white', 'wheat', 'rye'],
    'protein': ['turkey', 'ham', 'soy'], 
    'veggies': ['lettuce', 'tomato', 'onion']
    }
sandwich_order = {
    'bread': 'white', 
    'protein': 'ham', 
    'veggies': ['lettuce', 'tomato', 'onion'] # nest a list as a dict value anytime you need more than one value
}
# summarize order
print(f"You ordered a {sandwich_order['protein']} sandwich on "
      f"{sandwich_order['bread']} bread with:")
for veggie in sandwich_order['veggies']: 
    print(f"\t{veggie}") 
 
favorite_languages = {
    'jen': ['python', 'rust'], 
    'sarah': ['c', 'c++'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    } 
for name, languages in favorite_languages.items():
    if len(languages) != 1:
        print(f"\n{name.title()}'s favorite languages is:")  # first value = key for names
        for language in languages:                           # iterates through VALUES (mult due to list)
            print(f"\t{language.title()}")                   # tab for formatting
    else: 
        print(f"\n{name.title()}'s favorite languages are:") 
        for language in languages:                           
            print(f"\t{language.title()}")

users = {
    'jcage88': {                                                      
        'first': 'john',                                    # Having identical keys for each user makes looping easier 
        'last': 'cage',
        'location': 'black mountain college',
        },

    'sherholmes1000': {
        'first': 'sherlock', 
        'last': 'holmes', 
        'location': 'london', 
        },                                                  # Be sure to put a comma after each dict w/in the main dict
    }

for username, user_info in users.items():                   # 1st var for keys, 2nd variable (user_info) cycles through user dict (user)
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" # begin accessing inner dictionary (first, last, location)
    location = user_info['location']
        
    print(f"\tFull name: {full_name.title()}")              # tabs for inner dictionary helps distinguish from main keys 
    print(f"\tLocation: {location}")
print(f'\nThis was user information\n')


    
# Try it Yourself 6.7 People 
# 6.1 Person: Try it yourself
people = {
    'ryan': {
        'first name': 'ryan', 'last name': 'heck', 'age': 35,
        'location': 'pdale', 'career': 'construction',
        }, 
    'ryan2': {
        'first name': 'ryan', 'last name': 'gosling', 'age': 42,
        'location': 'hollywood', 'career': 'actor',
        }, 
    'alex': {
        'first name': 'alex', 'last name': 'g', 'age': 27,
        'location': 'philidelphia', 'career': 'musician',
        },
    }

for person, person_info in people.items(): 
    print(person.title())
    for key, value in person_info.items():             # inner dict. Do not forget .items() if needing both k/v values
        if str(value).isdigit():                       # convert to str in order to use .isdigit(), converts left to right
            print(f"\t{key.title()}: {value}"); 
        else:
            print(f"\t{key.title()}: {value.title()}")
print(f'\nThese were people\n')

# 6.8 Pets # # Printing a dict key/values
pets =  {
    'baby': {'animal': 'cat', 'owner': 'kelly'}, 
    'miley': {'animal': 'cat', 'owner': 'rita'},
    'oscar': {'animal': 'lizard', 'owner': 'emily'},
    'ozzy': {'animal': 'dog', 'owner': 'sarah'},
    'jake': {'animal': 'dog', 'owner': 'the allens'},
    } 
for pet, pet_info in pets.items():                     # Use .items() to loop through both k/v
    print(pet)
    print(f"\tAnimal: {pet_info['animal']}")           # choose to reference specific dict key instead of loop due to small list size                  
    print(f"\tOwner: {pet_info['owner']}")             
print(f'\nThese were pets.\n')

#  6.9 Favorite Places # Printing a dict list values
favorite_places =  {
    'andy_warhol': ['cambell soup factory', 'new york city', 'the factory'],  
    'snoop dogg': ['long beach', 'dispensary', 'inglewood'], 
    'zodiac killer': ['bay area', 'lookout points', 'newspaper headquarters'],  
    'hipster': ['thrift store', 'coffee shop', 'gentrified town'], 
    }
for name, places in favorite_places.items():          # use .items to loop through values list   
    print(f"{name.title()}'s Favorite Places:")
    for place in places:
        print(f"\t{place}")
print('\nThese were favorite places.\n')
                            
# 6.10 Favorite Numbers                            
favorite_numbers = {'ryan': [45, 7], 'nick': [42, 7],
                    'kelly': [86, 4, 99], 'frank': 31, 'rita': [31, 1]}
for person, numbers in favorite_numbers.items():   
    if isinstance(numbers, list):                                               # if dict value in {numbers} is a list. # instance(variable, data type)
        numbers_str = ', '.join(map(str, numbers))                              # map() is iterates over list, in this case, turning each numeral value in the list to a str in a list. Join only works on iterables of str,   
    else: 
        numbers_str = str(numbers)                                              # str(numbers) works only for a single digit
    print(f"{person.title()}'s favorite numbers: {numbers_str}")
print('\nThese were favorite numbers.\n')
# 6.11 Cities 
cities = {                      
    'boston': {
    'country': 'usa', 'population': '650,000', 
    'intersting fact': 'named after a town in England.'
        },
    'trenton': {
    'country': 'usa', 'population': '90,000', 
    'intersting fact': 'first us victory in revolutionary war.',
        },
    'princeton':{
    'country': 'usa', 'population': '30,000', 
    'intersting fact': "for a few months in 1783, Princeton served as the nation's capital.",
        },
} 

for city, facts in cities.items(): 
    print(city.title()) 
    for key, value in facts.items():
        print(f"\t{key.title()}: {value.capitalize()}")
print('\nThese were city facts.\n') 
 


# # Try it Yourself 7.2 Restaurant 
# dinner_group = int(input(f"How many people are in your party?"))
# if dinner_group < 9: 
#     print(f"Your table for {dinner_group} guests is ready.")
# else:     
#     print(f"Your table for {dinner_group} is not ready.")

# # 7.3 Multiples of Ten
# number = int(input("Input a number and I'll tell you if it's a multiple of 10:"))
# if number % 10 == 0: 
#     print(f"{number} is a multiple of 10.")
# else:     
#     print(f"{number} i9s not a multiple of 10.")

# Intro to While Loops
# current_number = 5
# while current_number <= 10: 
#     print(current_number)
#     current_number += 1 
    
# prompt = "Tell me someting and I'll repeat it back to you."
# prompt +="\nEnter 'quit' to exit the program."
# message = ""                 # loop cannot be compared if var is not initialized. Will cause error
# while message != 'quit':  
#     message = input(prompt)  # uses 'prompt' as input prompt
#     if message != 'quit': 
#         print(message)       # prints user input

# Using a Flag 
# For when many different conditions could end a program 

# prompt = "Tell me someting and I'll repeat it back to you."
# prompt +="\nEnter 'quit' to exit the program."
# active = True 
# while active:     
#     message = input(prompt)

#     if message == 'quit': 
#         active = False 
#     else:  
#         print(message)

# city = "Enter the name of a city you have visited."
# city += "\nEnter 'quit' when you are finished."
# while True:                                         # While True will loop forever
#     message = input(city)

#     if message == 'quit':
#         break 
#     else:
#         print(f"I'd love to go to {message}!")
              

# using 'continue' in a loop to skip to beginning. 
# COUNTING by ODD NUMBERS
current_number = 0
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Try it yourself -  7.4 Pizza Toppings
# pizza_toppings = ""
# while True: 
#     pizza_toppings = input("Please enter your pizza toppings, then press enter: ")
#     if pizza_toppings == 'quit': 
#         break
#     print(f"Got it! I will add {pizza_toppings}!")

# # Try it yourself 7.5 Movie Tickets  
# # if you wrap entire var in int(), cannout use str to quit
# ticket_age = input("Tell me an age (or type 'x' to quit) and I will tell you their ticket price: ")  
# while ticket_age != 'x':  
#     ticket_age = int(ticket_age)
#     if ticket_age < 3: 
#         price = "Free"
#     elif ticket_age <= 12: 
#         price =  "$10"
#     else: 
#         price = "$15"   
#     print(f"For a {ticket_age} year old, the price is {price}") 
#     ticket_age = input("Tell me an age (or type 'x' to quit) and I will tell you their ticket price: ")  
    
# While loops with dictionaries 
# Do not update lists in for loops, use while to avoid update errors
# MOVING ITEMS FROM ONE LIST TO ANOTHER


unconfirmed_users = ['travis', 'russel', 'patrick']
confirmed_users = []
# verfify each user until there are no unconfirmed users left 
# move each verified user into a list of confirmed users 
while unconfirmed_users:                                        # runs for as long as this list is not empty
    current_user = unconfirmed_users.pop()                      # .pop() removes last user of list, one by one

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users 
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: 
    print(confirmed_user.title())
print(f"Confirmed users: {confirmed_users}")
print(f"Unconfirmed users: {unconfirmed_users}")


# # Remove all instances from a list
# airlines =  ['alaska', 'delta', 'jetblue', 'united', 'jetblue', 'delta', 'soutwest', 'delta', 'delta', 'jetblue']
# print(airlines)
# while 'delta' in airlines: 
#     airlines.remove('delta')
# while 'jetblue' in airlines: 
#     airlines.remove('jetblue')
# print(f"\nairlines")    

# # Filling a dictionary with user input 
# responses = {}

# # Set a flag to indicate polling is active 
# polling_active = True
9
# while polling_active: 
#     name = input("What is your name?")
#     response = input(f"Which state would you like to snowboard one day, {name.title()}?")

#     responses[name] = response 
#     # simply assign name to key value "index" in dict, than assign the response value to that key-index
#     # store the responses in the dictionary

#     repeat =  input("Would you like to let another person respond? (y/n)")
#     if repeat == 'no' or repeat == 'n': 
#         polling_active = False

# # Polling is complete. Show results 
# print('\n- - - - - - Poll Results - - - - - - ')
# for name, response in responses.items(): 
#     print(f"{name.title()} would like to board in {response.title()}.")

# Try it yourself _ Deli 
# sandwich_orders = ['rueben', 'turkey', 'pastrami', 'buffalo chicken', 'pastrami', 'honey-baked ham', 'pastrami', 'grilled cheese']
# finished_orders = []
# print('Sorry, we are out of pastrami.')   
# while 'pastrami' in sandwich_orders:     
#     sandwich_orders.remove('pastrami')

# while sandwich_orders: 
#     current_sandwich = sandwich_orders.pop()
#     print(f"Making {current_sandwich}.")
#     finished_orders.append(current_sandwich)
    
# # Display Finished Sandwiches
# for order in finished_orders:
#     print(f"Finished orders: {order}") 
# print('These were sandwich orders')

# # Try it yourself 7.10 _ Dream Vacation
# poll = {}
# while True:
#     name =  input("\nWhat is your name?")
#     dream = input("What is your dream vacation?")
#     poll[name] = dream
#     continue_poll = input("Would you like to continue the poll? y/n")
#     if continue_poll == 'n': 
#         print("")
#         break 
# for name, vacation in poll.items():
#     print(f"{name.title()} would like to visit {vacation.title()}.")
    
    
# CH 8 _ FUNCTIONS     
def greet_user(username):
    """Display a simple greeting.""" # triple quote is a docstring, python looks for this for doc generation of fnx
    print(f"Hello, {username.title()}!")

# when calling a fnx be sure to inc. () # When you use a fnx, you "call" it
greet_user("nick") # str in argument still needs quotes
                   # an argument is passed from the "function call" to the function itself

# Try it yourself 8.1 Message
def display_message():                   
    print('\nYou are learning about functions.\n')
display_message()

# 8.2 Favorite Book
def fav_book(title):
    print(f'One of your favorite books is {title.title()}.\n')
fav_book('breakfast of champions')

# Positional Arguments in Fnx
# argument in fnx call, parameter in fnx defintion
def describe_pet(animal_type, pet_name): # can use keyword arguments if wanting to be explicit (animal_type="dog", pet_name="miggy")
    """Display info about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet("dog", "elliott") #  Don't forget to put str in quotes
describe_pet("cat", "miley")  

# Default values _ These can clarify fxn calls
def describe_pet(pet_name, animal_type='dog'):  
# pet_name still has to come first. It is a positional argument. Default values must come after. 
    """display info about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# Entering arguments into fnx calls, you can use positional arguements or keyword arg
describe_pet('lenny', animal_type='cat')    
describe_pet('gremlin') # This defaults to 'dog' for animal_type

# 8.3 T-Shirt
def make_shirt(size='Large', text='Python is a great programming language.'): 
    print(f"Make a {size} shirt with '{text}' printed on it.")

print()
make_shirt(size='medium', text='Human = Garbage') # keyword arguments override default values
make_shirt(size="small", text="The Aftermath")
make_shirt() # uses default values

# 8.5 Cities
def describe_cities(city, country='United States'):
    print(f"{city.title()} is in {country.title()}.")  
print()          
describe_cities('long beach', 'california')
describe_cities('new bruswick', 'new jersey')
describe_cities('santa fe')

# Return Values
def get_formatted_name(first_name, last_name, middle_name=''):  
    # Formatted name is useful for large data sets where first and last names are stored seperately.
    # middle_name, if optional, must be at end of parameters to maintain "positional" arguments
    """Return a neatly formatted name"""
    if middle_name: 
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('bill', 'callahan')
musician1 = get_formatted_name('mary', 'holland', middle_name='liza')
print(musician)
print(musician1)

def build_person(first_name, last_name, age=None, address=''): # Add None value so that no error occurs for not enough arg 
    """Return a dictionary about a person"""
    person = {'first': first_name.title(), 'last': last_name.title()}               
    if age:                        # if age value exists
        person['age'] = age        # assign age value to age dict key, similar to append    
    if address: 
        person['address'] = address.title()
    print()                        # empty line 
    return person  
musician = build_person('dino', 'dystopia', age='50') # can combine any combo of posiitonal argument and keyword arg
print(musician)
for info in musician.items():
    print(info)

musician = build_person('phil', 'sea of deprivation', age='Deceased at 29', address='2303 glendale, az') # can combine any combo of posiitonal argument and keyword arg
print(musician)

# # Using a fnx in a while loop 
# print("please tell me your name or press x to exit")
# f_name = input("First name:")
# while f_name != 'x': 
#     l_name = input("Last name:")
#     age = input("Age:")
#     formatted_name = build_person(f_name, l_name, age)
#     print(f"Hello, {formatted_name}")
#     print("please tell me your name or press x to exit")
#     f_name = input("First name:")

# Try it yourself_ City Names 8.6
def get_city_country(city, country): # Fnx is able to take input directly, does not always require user input
    formatted_city = f"{city.title()}, {country.title()}"
    print(formatted_city)
get_city_country('santa fe', 'united states') 
get_city_country('barcelona', 'spain')
get_city_country('london', 'england') 

# 8.7 Album _ fnx dict 
def build_album(artist, album, year=None, num_song=None):
    album = {'artist': artist.title(), "album": album.title()}
    if year: 
        album['year'] = year 
    if num_song: 
        album['num_song'] = num_song
    print(album) 

build_album('dystopia', 'the aftermath', '1999', '12')
build_album('graves at sea', 'unknown', num_song='7')
build_album('amebix', 'arise', '1988')
print()   

# 8.8 album with user input
def build_album(artist, album, year=None, num_song=None):
    album = {'artist': artist.title(), "album": album.title()}
    if year:
        album['year'] = year
    if num_song:
        album['num_song'] = num_song
    print(album)

artist = 'q' # to be able to comment out input loop
# artist = input('Please enter an artist or press "q" to exit: ')
# while artist != 'q': 
#     album = input(f'Please enter an album by {artist}: ')
#     year_input = input(f"Please enter the album year, otherwise enter n/a: ")
#     if year_input != 'n/a': 
#         build_album(artist, album, year_input)
#     else:
#         build_album(artist, album)
#     artist = input('Please enter an artist or press "q" to exit: ')
# print("You have exited album information input.\n")  

# CHAPTER 9 CLASSES 
class Dog: 
    """A simple attempt to model a dog"""

    def __init__(self, name, age):  # __init__ is a special method, needed for when you instantiate
                                    # First parameter of init declarations is always SELF                                   
        """Initialize name and age attributes"""
        self.name = name           # self.var allows it to be used by all methods in the class
        self.age = age             # self.var then become called ATTRIBUTES
        
    def sit(self):                 # this method has no additional parameters, self only  
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self): 
        """Simulate a dog rolling over"""
        print(f"{self.name} rolled over!")

# Instantiation of a class . Classes are always instantiated by assigning to a variable
my_first_dog = Dog('natasha', '16')       # lowercasee is an instance, upper is for class
print(f"My first dog's name was {my_first_dog.name}")
print(f"My first dog's age was {my_first_dog.age} years old.")

my_first_dog.sit() # use the method on an instance "my_first_dog"
my_first_dog.roll_over()

my_second_dog = Dog('peanut', '15') # another instance of a class, a particular use 
print()
print(f"My second dog's name was {my_second_dog.name}.")
my_second_dog.sit()
my_second_dog.roll_over()


# Classes Restaurant 9.1 TYS
class Restaurant: 
    """Take a restaurant's name and cuisine and print"""  
    def __init__(self, name, cuisine): 
        """Initialize name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        self.num_served = 0 # used to set inital state, attributes of objects

    def describe_restaurant(self): # no param for name, already in self
        print(f"\nRestaurant: {self.name}")
        print(f"Cuisine type: {self.cuisine}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_num_served(self, num=None): # don't forget "self" in methods
        """Set initial value of number served. This serves as an alternate to __init__ attribute"""
        if num is not None: # allows set to be optional
            self.num_served = num
        print(f"\nNumber of patrons served: {self.num_served}") # don't forget self. when calling
    
    def increment_num_served(self, num):
        """Passes number to add/increment sum of patrons served"""
        self.num_served += num 
        print(f"Number of patrons served: {self.num_served}")

titos = Restaurant('titos and tacos', 'mexican') # intanstiation
titos.describe_restaurant()
titos.open_restaurant() 

rooster = Restaurant('rooster', 'refinded american breakfast')
rooster.describe_restaurant()
rooster.open_restaurant()

whiskey_park = Restaurant('whiskey park', 'bar')
whiskey_park.describe_restaurant()
whiskey_park.open_restaurant()

whiskey_park.set_num_served() # defaults to 0 if no arg
whiskey_park.increment_num_served(158)
whiskey_park.increment_num_served(1_000_234)
whiskey_park.increment_num_served(2_000_000)

whiskey_park.set_num_served(0)
whiskey_park.increment_num_served(1_323)
whiskey_park.set_num_served(2_234)

# 9.3 Users 
class User: 
    """Create and print typical attributes stored in a user profile"""

    def __init__(self, first_name, last_name, email, join_date='Not Provided'): 
        """Initialize user info. Create the initial state of the object"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email 
        self.join_date = join_date  
        self.login_attempts = 0

    def describe_user(self): 
        """Print user info"""
        print(f"\nFirst name: {self.first_name}") # Be sure to include "self." for methods
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Join: {self.join_date}")

    def greet_user(self):  
        """Greet user"""
        print(f"\nHello, {self.first_name} {self.last_name}. Thank you for joining!\n") 
        # include self or else variable can reference others

    def increment_login_attempts(self): 
        """A method to increment login attempts by 1"""
        self.login_attempts += 1
    
    def reset_login_attempts(self): 
        """Reset login attempts to 0"""
        print("Resetting login attempts to 0")
        self.login_attempts = 0

class Privileges():
    """A list of strings to be used by Admin"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"Privileges:")
        # don't forget to target instance info using self.
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    """Admin is a special type of user. Admin inherits from User class"""

    def __init__(self, first_name, last_name, email, join_date='Not Provided'):
        """First initialize all parameters, then import parent, then att specific to child (Admin)"""
        super().__init__(first_name, last_name, email,
                         join_date)         # seperated by dot notation, this func is still w/in initial __init__, now don't need to reassign all param. to self.
        self.privileges = Privileges()


andre_the_giant = Admin('Andre', 'The Giant',
                        'agiantWrestler83@gmail.com', '01/24/2024')
# usable since Admin() inherited User() and it's methods
andre_the_giant.describe_user()
andre_the_giant.privileges.show_privileges()

user_1 = User('john', 'cena', 'jdawg44@gmail.com', 'March 23, 2023') # intanstiation
user_1.describe_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(f"User 1 Login Attempts: {user_1.login_attempts}") # accessing attribute directly
user_1.reset_login_attempts() # don't forget () when calling methods
print(f"{user_1.first_name.title()} {user_1.last_name.title()} Login Attempts: {user_1.login_attempts}")

user_1.greet_user()

user_2 = User('jim', 'varney','earnestscaredStudpid1989@hotmail.com', 'Jan 8, 2024')
user_2.describe_user()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
print(f"User 1 Login Attempts: {user_2.login_attempts}")
user_2.greet_user()



# Once you write a class, most time will be spent working with instances from this class

# The Car Class
class Car: 
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """initialize attributes to describe a car"""
        self.make = make
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 # Default attributes can be assigned in __init__ method 
    
    def get_descriptive_name(self): 
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title() # "Dryer than putting .title() in each var above

    def read_odometer(self): 
        """Print car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.\n")
    
    def update_odometer(self, mileage): 
        """Set the odometer to the given value"""
        """Reject the value if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles): 
        """Add the given amount to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles # += same as saying 'reading = reading + miles'
        else:  
            print("You can't roll back an odometer!")

class Battery:
    """A simple attempt to model a battery for an electric car""" # organizing classes is "composition"
    def __init__(self, battery_size=40):          # For if no other value is input, default is available/no errors
       """Initialize the battery's attributes"""
       self.battery_size = battery_size
    
    def describe_battery(self):                        
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.") # use self. in methods

    def get_range(self): 
        """Print a statement about the range this battery provides"""
        battery_range = 0
        if self.battery_size  == 40:               # don't forget self. when assigning parameters in methods
            battery_range = 150
        elif self.battery_size == 65: 
            battery_range  = 225      
        elif self.battery_size >= 65:
            battery_range = 300                   
        print(f"This car can go about {battery_range} miles on a full charge.")

    def upgrade_battery(self): 
        """Check battery size and set capacity to 65"""
        if self.battery_size != 65:
            self.battery_size = 65
            print(f"Battery size has been updated to {self.battery_size}.\n")
        

class ElectricCar(Car):                           # INHERITANCE _ class syntax does not need def
                                                  # Parent class must come before child
    """"Represent aspects of car unique to electric vehicles"""
    def __init__(self, make, model, year):        # don't forget __init__ is a method too
        """Initalize attributes of the parent class. Then initialize attributes specific to EV"""
        super().__init__(make, model, year) 
        """ 
         super() imports __init__ from parent class to child. Name comes from super/sub class 
         Super() is called INSIDE the __init__ method. Super DOES NOT NEED SELF argument
        """      
        self.battery = Battery(80)                 # Now every ElectricCar class has Battery instance installed since it is in ElectricCar's __init__ method's attributes
        """assign another class instance to this att. w/in a class. This is where you can change Battery's default battery_size, 
            which was assigned in Battery() parameters. This addition was part of the section "Instances as Attributes. 
            This may seem like a lot of extra work, but now Battery() class can expand w/o cluttering ElectricCar() class"""                                
    def fill_gas_tank(self):                       # same-name method in parent class would be overidden
        """Electric cars don't have gastanks"""
        print("This car does not have a gas tank!")
 

                                                  
my_new_car = Car('audi', 'a4', 2024)    
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 9_034           # This updates attribute value directly
my_new_car.read_odometer()

my_first_car = Car('ford', 'bronco', '1993')
print(my_first_car.get_descriptive_name())
my_first_car.odometer_reading = 195_023  # Uses "dot notation" to update an instance. 1 of 3 ways
my_first_car.read_odometer()

my_second_car = Car('ford', 'explorer', '1994') # default odometer is 0
print(my_second_car.get_descriptive_name()) # don't forget () when calling method (same as w/ func)
my_second_car.odometer_reading = 300_000
my_second_car.update_odometer(232_140) # alt way to update: Call a specialized method
my_second_car.read_odometer() # if update is lower than initial reading, error is printed
my_second_car.increment_odometer(1000) # negative values print an error, no rollback allowed
my_second_car.read_odometer()

my_second_car.odometer_reading = 304_000 # restrictions can be placed on update method and
                                         # print methods, but users can still update value 'directly' 
                                         # with dot notation
my_second_car.read_odometer()

volt_ev = ElectricCar('chevy', 'volt', 2023)
print(volt_ev.get_descriptive_name())  # print() is built into this method already
                                       # be sure to include () for method calls w/in functions
volt_ev.battery.describe_battery()     # instance.other_class.method_from_inherited_class()
"""This is used bc volt_ev was created with ElectricCar and describe_battery() method was in
    new class, Battery. If follows the 'dot dot notation'"""            
volt_ev.battery.get_range()                        


# an instance of ElectricCar class
lightning_ev = ElectricCar('Neo', 'Lighting', 2025)
print(lightning_ev.get_descriptive_name())
lightning_ev.battery.describe_battery()     # calls ATTRIBUTE which was set to Battery() class inside ElectricCar() class 
lightning_ev.battery.get_range()                        
print()

# TYS 9.9 Battery Upgrade
new_ev = ElectricCar('chevy', 'volt', '2023')
new_ev.battery.get_range()
print()

new_ev.battery.upgrade_battery()
new_ev.battery.get_range()

#  TIY Ice Cream Stand 
class IceCreamStand(Restaurant):
    """An attempt to represent an ice cream stand"""

    def __init__(self, name, flavors, cuisine='ice cream'): # initialize all parameters, including names to be inherited  
        super().__init__(name, cuisine)
        self.flavors = flavors   
        
    def show_flavors(self):
        """Print the flavors that were given"""
        print(f"{self.name.title()} carries the following flavors: ")  
        for flavor in self.flavors: 
            print(f"-- {flavor.title()}")  # without 'self.', prefix var is out of scope 

the_banana_stand = IceCreamStand(  
    'The Banana Stand', [
        'Ice Cream', 'vanilla', 'strawberry', 'chocolate', 'pistachio'
        ], 'Ice Cream'
    ) 
the_banana_stand.show_flavors()
print() 

salt_and_straw = IceCreamStand(  # Pep8 Format
    'salt and straw', [
        'jalapeno corn', 'raspberry pear', 'balsamic', 'olive oil and pear'
        ]
)
salt_and_straw.describe_restaurant() # pulled from parent class Restaurant
salt_and_straw.increment_num_served(50)
salt_and_straw.show_flavors()

# If you import the entire module, import car (instead of 'from car import ElectricCar), you have to use .notation, such as: my_mustang = car.Car('ford', 'mustang', 2022)

# you can import any user-created func or methods
from random import randint
randint(1, 6)

from random import choice
techniques = ['slow rate', 'light contact', 'stretchy speech', 'pausing', 'easy onset']
technique = choice(techniques)
print(f"\nRandomized Fluency Strategy: {technique.title()}\n")

# TIY 9.13 DICE
class Die:

    """A class to represent a single Die"""
    def __init__(self, sides=6, rolls=10):
        self.sides = sides
        self.rolls = rolls
    
    def roll_die(self):
        roll_sum = 0
        rounded_average = 0
       
        for i in range(self.rolls):
            rolled_num = randint(1, self.sides)
            roll_statement = f"This die has {self.sides} sides. You rolled a {rolled_num}" # print not needed
            print(f"Loop {i + 1}: {roll_statement}")
            roll_sum += rolled_num
        
        rounded_average = round(roll_sum /self.rolls, 2)
        print(f"\nThe average roll is: {rounded_average}\n")
        return 
    
dice_player_1 = Die(6, 100)
dice_player_1.roll_die()

# Alternative ChatGpt version: Utilizes single-responsibility principle, seperates calculations from
# printing for future flexibility. Utilizes enumerate() 

from random import randint

class Die: 
    """A class to represent a single Die, it's rolls and averages."""
    
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self, rolls=10):
        """Creates List using List Comprehension to store data for all random rolls""" 
        # The underscore _ is a conventional way to indicate that the loop variable is a placeholder and won't be used.
        return [randint(1, self.sides) for _ in range(rolls)] # [expresssion for item in iterable]
    
# Using the class / instantiating 
dice_player_1 = Die(10)
print(f'The die has {dice_player_1.sides} sides. ')

roll_results = dice_player_1.roll_die(20)
# Handling the results outside the class
for i, result in enumerate(roll_results, start=1):
    print(f"Roll {i}: You rolled a {result}")

average_roll = round(sum(roll_results) / len(roll_results), 2)
print(f"\nThe average roll is: {average_roll}\n")


# TIY 9.14 Lottery
lottery_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']
winning_ticket = []
my_ticket = []
loop_count = 0

# Randomly select 4 items from lottery_choices to create winning ticket
for i in range(4):
    winning_ticket += choice(lottery_choices)
print(f"The winning ticket is {winning_ticket}")

while my_ticket != winning_ticket: 
    # create my_ticket
    my_ticket = []   # must reset ticket each non-winning loop
    for i in range(4): 
        my_ticket += choice(lottery_choices)
    loop_count += 1

print(f"Winner. My ticket: {my_ticket}")
print(f"Lottery won in {loop_count} tries!\n")


# Using sample sets that do NOT need to be in identical order
from random import choice, sample, uniform
lottery_choices = ['1', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']

# Randomly select 4 unique items from lottery_choices to create winning ticket
winning_ticket = sample(lottery_choices, 4) # sample() samples w/o replacement (objects choosen once)
print(f"The winning ticket is {winning_ticket}")

# Initialize my_ticket outside the while loop for clarity
my_ticket = []

loop_count = 0  # Track how many attempts are needed
while sorted(my_ticket) != sorted(winning_ticket):# sorted() makes order selection irrelevant 
    # Reset my_ticket each iteration to simulate a new draw
    my_ticket = sample(lottery_choices, 4)
    loop_count += 1

print(f"Winner after {loop_count} tries. My ticket: {my_ticket}")

# TIY 9-16 Python Module of the Week
# random module examples. Generates values b/w 0 and 1.0
# import random
for i in range(5):
    print(f'{random.random():04.3f}', end=' ')
print()

# Use uniform for numbers in a specific range
min_value = 1
max_value = 1000 

for i in range(5):
    print(f"{uniform(min_value, max_value):04.2f}", end=' ') # imported function, so syntax of 
                                                             # module.function is optional
print()    

# Pymotw Heads or Tails Average
outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])


# Ch 10 _ Files and Exceptions
from pathlib import Path # Path is newer and often preferrable to os.path

path = Path('pi_digits.txt') # Create object with instantiation of class 
contents = path.read_text()  # read file
print(f"\n{contents}\nThis was the read files content read and printed\n")       # output to console
                 

# Relative path means it looks in current folder FIRST, folders can also be w/in current folder
# For instance, path = Path('text_files/filename.txt')

# Absolute can be anywhere but requires more information in your code
# path = Path('/home/eric/data_files/text_files/filename.text')
# Use forward slash (/). Even though windows uses back slash (\), path will convert to standard

# Accessing File Lines
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text() 

pi_string = ''
lines = contents.splitlines() # separate the read txt file, return a list
for line in lines:            # loops over lines and prints in original format
    print(line)
print(f'This was the read files content printed line by line\n')

# Printing in a single line
for line in lines:            
    print(line.lstrip(), end='') # To remove formatting and print on one line
print(f'This was the read files lines appeneded to one line')  

# Alt printing in single line
pi_string = ''
for line in lines: 
    pi_string += line.lstrip() # Appending to list is more versatile if more complex conditions

print(f'This was the read files lines appeneded to one line using an accumulated List\n')
print(pi_string)               # Print the appended List
print(f"The length of the accumulated List is: {len(pi_string)}\n")

# Is your birthday contained in Pi?
# path1 = Path('pi_digits_1_million.txt')
# contents = path1.read_text()
# pi_digits = ''

# lines = contents.splitlines() # to create line w/o whitespace found in human readable txt file
                              # needed to find sequences spanning across multiple lines
# for line in lines: 
#     pi_digits += line 

# birthday = input("Enter your birthday, in the form of mmddyy: ")
# if birthday in pi_digits:
#     print("Your birthday appears in the first million digits of pi!")
# else: 
#     print("Your birthday does not appear in the first million digits of pi")

# 10.1 TIY 
from pathlib import Path 

path = Path('learning_python.txt') # convert format
contents = path.read_text()        # save read text file
lines = contents.splitlines()

for _ in range(2):                 
    for i in range(3, len(lines)): # skip title lines 
        print(lines[i])            # prints the correct lines at their respective indexes

# Find and Replace
str = 'My name is Isaac'
replaced_str = str.replace('Isaac', 'Ezekial')
print(replaced_str)

# Find and Replace from read file
path1 = Path('learning_python.txt')  # Path oject not enough to work with, use read_text()
learn_file = path1.read_text()
for line in learn_file.splitlines(): # Can skip assigning this item/method to separate var 
    print(line.replace('function', 'method').replace('dictionaries', 'methods').replace('libraries', 'methods'))
    # You can chain mult. .replace()

# Alternate version of Find and Replace path/read file
learn_file = Path('learning_python.txt').read_text()


from pathlib import Path

path = Path('programming.txt')              # create and save new file (if file doesn't exist)
path.write_text("I love programming.")      # save txt w/in file 

contents = "I love programming.\n"          # Append a list
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)
print(f"Saved to {path}:\n{contents}")

# TIY 10.4 Guest Book
# guest_file = Path('guest.txt')              # create file 
# guest_list = ''

# name = input('What is your name?')
# while name != '' and name != 'quit':
   # guest_list += f"{name}\n"               # create list, then write. O/w it overwrites each loop
   # name = input('What is your name?')

# guest_file.write_text(guest_list) 

# Exceptions
try:
    print(5/0)                           # Can't divide by zero
except ZeroDivisionError:
    print(f"You can't divide by zero!\n")   # If error is found, py looks for except block 


# division_calculator.py / Using exceptions to prevent crashes
# print("Give me two numbers and I'll divide them.")
# print("Enter 'q' to quit")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:                           # try can appear earlier, but here is closer to the potential error
#         answer = int(first_number)  / int(second_number)
#     except ZeroDivisionError:      # letting users see traceback errors can compromise security
#         print("You cannot divide by zero")        
#     else:                          # Any code that depends on try block goes in else block
#         print(answer)

# Handling the FileNotFoundError Exception and Analyzing Text
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file"""
    path = Path(path)                               
    try:                                            # contents holds alice.txt below as one long stri
        contents = path.read_text(encoding='utf-8') # use utf-8 when decoding files w/ special characters 
    except FileNotFoundError:     
        print(f'Sorry, the file {path} does not exist.') # You can use Pass to do nothing w/ errors
    else:
                                                   # if no exceptions, code executes here
        words = contents.split()                   # separates by whitespace as default, returns a List
        num_words = len(words)    
        print(f"The file {path} has about {num_words} words.")

count_words('alice.txt')
count_words('little_women.txt')
count_words('siddhartha.txt')
count_words('moby_dick.txt')

# Report errors if User expects/understands them, o/w may hinder user experience. Don't give info
# they are not looking for, e.g. "siddhartha" missing if they hadn't uploaded it