from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Vyctor",
    description="image Processing Package using Skimage",
    long_descrption=page_description,
    long_descripion_content_type="text/markdown",
    url="https://github.com/waves-vy/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)