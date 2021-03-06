import setuptools

setuptools.setup(
    name="pyMetallex", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="Mettalex sdk package for conducting trade",
    long_description_content_type="text/markdown",
    url="https://github.com/MehulG/pyMettalex/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['pathlib', 'argparse','requests', 'web3'],
    python_requires='>=3.0',
)
