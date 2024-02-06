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
        print(
            f"\nFirst name: {self.first_name}")  # Be sure to include "self." for methods
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Join Date: {self.join_date}")

    def greet_user(self):
        """Greet user"""
        print(
            f"\nHello, {self.first_name} {self.last_name}. Thank you for joining!\n")
        # include self or else variable can reference others

    def increment_login_attempts(self):
        """A method to increment login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        print("Resetting login attempts to 0")
        self.login_attempts = 0

