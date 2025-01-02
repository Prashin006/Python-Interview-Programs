class DatabaseConnection:
    """Simulate a database connection with a context manager"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """Establish the connection."""
        self.connected = True
        print(f"Connected to the database '{self.db_name}'!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection."""
        self.connected = False
        print(f"Disconnected from the database '{self.db_name}'")
        # Handle any exceptions
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True    # Suppresses exceptions if they occur

with DatabaseConnection("ExampleDB") as db:     # calls the `__enter__` method as soon as we enter the `with` context manager
    print(f"Is connected?: {db.connected}")     # `__exit__` method is called as soon as we exit the `with` context manager whether there is an exception or not
