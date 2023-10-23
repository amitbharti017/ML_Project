from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements = file_obj.readlines() #in requirements.txt changing line will cause
        # /n to be added which needs to be removed from the list
        requirements = [req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements       
setup(
    name = 'ml_project',
    version = '0.0.1',
    author = 'Amit',
    author_email = 'amitbharti936@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)