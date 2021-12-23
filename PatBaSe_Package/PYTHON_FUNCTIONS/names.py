# Define function names()
def names():
    # Set up name variable with input
    name = str(input('Enter your name: '))
    # Check whether name has a vowel
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')

    # Iterate over name
    for letter in name:
        print(letter)

# Call the function
names()
######################################
def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)

add_numbers(1, 2, 3)

###########################################
def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

# Call function with parameters assigned as above
profile_info("sammyshark", 945)

# Call function with keyword arguments
profile_info(username="AlexAnglerfish", followers=342)

############################################
# Change order of parameters
profile_info(followers=820, username="cameron-catfish"

############################################

def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: " + str(followers))

profile_info(username="JOctopus")
profile_info(username="sammyshark", followers=945))
