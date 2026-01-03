class UserInputReader:
    """Reads and validates user input"""

    def get_blog_name(self):
        """Gets Tumblr blog name from user"""
        return input("enter the Tumblr blog name:\n").strip()

    def get_post_range(self):
        """Gets post range from user"""
        while True:
            try:
                user_input = input("enter the range (e.g., 1-10):\n").strip()
                start, end = user_input.split("-")
                return int(start), int(end)
            except ValueError:
                print("Invalid format. Please enter range like '1-10'.")
