from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt", "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

setup(
    name="SnapEditor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "SnapEditor=src.main:main",
        ],
    }
)
