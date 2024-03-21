from setuptools import find_packages, setup
from typing import List

HYPHENE_DOT = "-e ."
def get_requirements(file_path : str) -> List[str]:
    # Function to return Requirements list
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHENE_DOT in requirements:
           requirements.remove(HYPHENE_DOT) 
    
    return requirements


setup(
    name = "ETOEMLPRO",
    version = "0.0.1",
    author = "Srishti",
    author_email = "srishtimuskan552gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)