from pathlib import Path
from setuptools import setup, find_packages

REQUIREMENTS_FILE = Path(__name__).parent.absolute() / "requirements.txt"

def read_requirements():
    """
    read requirements
    """
    requirements = []
    with open(REQUIREMENTS_FILE, mode="r") as req_file:
        lines = req_file.readlines()
        for line in lines:
            if "#" not in set(line):
                requirements.append(line.replace("\n", ""))
    return requirements 
     
setup(
    name="flask-website",
    install_requires=read_requirements(),
    version="0.0.0",
    packages=find_packages("flask_src"),
    package_dir={"": "flask_src"}
)