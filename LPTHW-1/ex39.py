states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
#a dict with keys on the left and values on the right

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
#a dict with keys on the left and values on the right


cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#adding two entries to the cities dict, by giving the key and the value


print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])
#printing the value that is associated with a specific key of the cities dict


print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
#printing the value that is associated with a specific key of the states dict

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
#first the innder dict gets evaluated, then the outer


print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated by {abbrev}")
#we loop thorugh the states dict, creating two vars states and abbrev
# states and abbrev stand for the key and the value in the dict
#the order is imprtant. The first argument stands for the key
#The second arguemnt represents the value

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
#Second print statement: we take the value stored in abbrev
#and look for that abbrev as a key in the cities dict

print('-' * 10)
state = states.get('Texas')
if state:
    print(state)
if not state:
    print("Sorry, no Texas.")
#we check if 'Texas' is in the states dict
#If it is, we print the state
#If it isn't, we print Sorry


city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
#This is a more concise version of the block above
#Here we check whether 'TX' is in the cities dict and also
#specify what to print if it isn't 
