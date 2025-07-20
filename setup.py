from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."



def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        return requirements

        if HYPEN_E_DOT in requirment:
            requirment.remove("HYPEN_E_DOT")


setup(
    name="ml projects",
    version="0.0.1",
    author="Netra Shivhare",
    author_email="netrashivhare03@gmail.com",
    install_requires=get_requirements("requirment.txt"),
    packages=find_packages(),
    
    
    
    
)