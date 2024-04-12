"""Practice writing a class."""

class Profile:

    # creating attributes for the class
    username: str
    private: bool

    def __init__(self, username_input: str):  # self is a reference to the object when it's called
        """Create a new Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """Method that prints msg if self.private is False."""
        if self.private:
            return None
        else: 
            print(msg)

# creating new variable that's referencing profile object with a username
user1: Profile = Profile("110_rulez")
# updating value of private to False
user1.private = False
# using the tweet method call to tweet message
user1.tweet("OOP is cool!")