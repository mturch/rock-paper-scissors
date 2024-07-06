import os

def get_absolute_import_path(relative_path:str) -> str:
    """
    Converts a relative import path to an absolute path.

    Args:
        relative_path (str): The relative path to a module or package.

    Returns:
        str: The absolute path to the module or package.
    """

    # Get the directory of the current module
    working_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the current directory with the relative path
    absolute_path = os.path.join(working_dir, relative_path)

    # Normalize the path to remove any '..' or '.' segments
    absolute_path = os.path.normpath(absolute_path)

    return absolute_path

# Example usage:
relative_path = "../my_package/my_module.py"
absolute_path = get_absolute_import_path(relative_path)

print(absolute_path)