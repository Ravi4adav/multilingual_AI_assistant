from setuptools import setup, find_packages
from typing import List

HYPON_E_DOT='-e .'
def get_requirements(path: str)-> List:
    requirements=[]
    with open(path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    if HYPON_E_DOT in  requirements:
        requirements.remove(HYPON_E_DOT)
    return requirements
        

setup(
    name="Multilingual AI Assistant",
    version=0.1,
    author='Ravi Yadav',
    author_email='ry794396@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirements.txt')
)