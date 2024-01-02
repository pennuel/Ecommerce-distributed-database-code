# Import the ConfigParser class from the configparser module
from configparser import ConfigParser

# Function to retrieve database configuration details from the config.ini file
def dbconfig(section):
    """
    The function collects the database connection details
    :param section: This is the section in the database config file containing connection details
    :return: Dictionary containing database config file details
    """
    # Set the path to the config.ini file
    config_path = "db/dbconnect/config.ini"

    # Create an instance of the ConfigParser class
    parser = ConfigParser()

    # Read the content of the config.ini file
    parser.read(config_path)

    # Initialize an empty dictionary to store database connection details
    db = {}

    # Check if the specified section exists in the config file
    if parser.has_section(section):
        # Retrieve all parameters (key-value pairs) in the specified section
        params = parser.items(section)

        # Populate the dictionary with the parameters
        for each_param in params:
            db[each_param[0]] = each_param[1]

    else:
        # Raise an exception if the specified section is not found in the config file
        raise Exception("Section is not found")

    # Return the dictionary containing database connection details
    return db
