"""Meta-data regarding the database-manager package."""

from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="Configuration Manager",
    version="0.0.1",
    description="Manage your configuation and environment variables with one singleton class",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Data-Analytics-Center/Configuration_Manager",
    author="Data Analytics Center",
    author_email="daclab@utsa.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["wheel", "python-dotenv", "pytest"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
