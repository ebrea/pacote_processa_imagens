
from setuptools import setup, find_packages
with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="pacote_processa_imagens",
    version="0.0.1",
    author="Eber",
    author_email="eberbrea@gmail.com",
    description="Teste de como desenvolver um Pacote em Python para disponibilizar no pypi.org",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebrea/pacote_processa_imagens",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
