from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    desc = f.read()

setup(
    name="geglu_triton",
    version="0.0.1",
    description="",
    author="Kitsunetic",
    author_email="jh.shim.gg@gmail.com",
    url="https://github.com/Kitsunetic/GEGLU-triton",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    long_description=desc,
    long_description_content_type="text/markdown",
)
