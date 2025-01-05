from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """This function returns the list of requirements, ignoring -e ."""
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Process each line
            requirements_lst = [
                line.strip() for line in file.readlines() if line.strip() and not line.startswith("-e")
            ]
    except FileNotFoundError:
        print("Hey, the requirements file was not found!")
        # Optionally raise an error here to stop the setup from continuing if the file is critical
        raise FileNotFoundError("requirements.txt file is missing!")
    
    return requirements_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="manohar-mata",
    author_email="matamanohar612@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()  # Dynamically loads valid requirements
)
