from user import User 

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
