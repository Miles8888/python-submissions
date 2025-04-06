class User:
    """A simple class representing a user profile."""

    def __init__(self, first_name, last_name, age, email, location):
        """Initialize user attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print("\nUser Information:")
        print("  Name: {} {}".format(self.first_name, self.last_name))
        print("  Age: {}".format(self.age))
        print("  Email: {}".format(self.email))
        print("  Location: {}".format(self.location))

    def greet_user(self):
        """Prints a greeting message to the user."""
        print("\nHello, {}! Welcome to our platform.".format(self.first_name))

    def increment_login_attempts(self):
        """Increases the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attempts to 0."""
        self.login_attempts = 0

user2 = User("mike", "garcia", 25, "mike.garcia@icloud.com", "asheville")

user2.describe_user()
user2.greet_user()

print("\nMaking multiple login attempts...")
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print("  Login attempts: {}".format(user2.login_attempts))

print("Login failed... Resetting login attempts...")
user2.reset_login_attempts()
print("  Login attempts: {}".format(user2.login_attempts))