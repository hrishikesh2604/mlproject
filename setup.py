from setuptools import find_packages, setup
from typing import List

# Define the '-e .' string as a constant
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Function to return all the requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters and clean the requirements list
        requirements = [req.replace("\n", "") for req in requirements]

        # Check if '-e .' is present and remove it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Hrishikesh',
    author_email='hrishikeshdongre26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
