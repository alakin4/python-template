from src.main import main


def test_hello_world():
    """
    Test the main function to ensure it returns the expected string.
    """
    assert main() == "Hello, World! this is a template for a Python projects."
