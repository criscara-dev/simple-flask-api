# In real life projects, this would be a database table.
from user import User

users = [ User(1,'John','mypassword123'),
          User(2,'Jane','mysecretpass')]

# Creating a dict that map user to username, using a dictionary comprehension: {u.username: u for u in users}
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# as from the documentation example code
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
