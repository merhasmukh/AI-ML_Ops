from setuptools import setup,find_packages


with open("README.md","r",encoding="UTF-8") as f:
    long_description=f.read()


setup(
    name="src",
    version="0.0.1",
    author="hasmukh",
    description="A small package for DVC ML pipeline demo"
    long_description=long_description,
    url="https://github.com/mhgn/AI-ML_Ops/tree/master/simple_dvc_project",
    author_email="mhgn0001@gmail.com",
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'dvc',
        'dvc[gdrive]',
        'pandas',
        'scikit-learn'
    ]
)