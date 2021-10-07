import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='probdists',
    version='1.3',
    author='Ayush Modi',
    author_email='hot9cups@yahoo.in',
    description='Python Package for modelling Gaussian and Binomial distributions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hot9cups/probdists",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'matplotlib',
        'seaborn'
    ],
    zip_safe=False
)
