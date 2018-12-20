current_users = ["amy", 'maria', 'wendy', 'john', 'cat', 'admin']
new_users = ["CAT", "coca", "corin", "jan", "robin", "amy"]
"""
if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}. How are you?")
else:
    print("We need users!")
"""

for user in new_users:
    if user.lower() in current_users:
        print(f"Username '{user}' already taken.")
    else:
        print(f"Username '{user}' availbe")
