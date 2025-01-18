from setuptools import setup, find_packages

setup(
    name="ciclistes_analysis_PAC4",
    version="1.0.0",
    description="Projecte per analitzar i processar dades de ciclistes participants a Orbea Monegros.",
    author="Clara Ferrer",
    author_email="cferrer4@uoc.edu",
    url="https://github.com/Claraferrer24/PAC4.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=1.0.0",
        "matplotlib>=3.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "ciclistes-analysis=main:main",
        ],
    },
)
