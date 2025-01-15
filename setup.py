import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
VERSION = '0.0.0'
AUTHOR_USER_NAME = "JotiRoy01"
REPO_NAME = "Number_Plate_Recognition"
PROJECT_NAME = 'ANPR'
AUTHOR_NAME = 'JOTI ROY'
DESCRIPTION = 'This is a automatic number plate recognition project'


setuptools.setup(
    version=VERSION,
    name = PROJECT_NAME,
    author=AUTHOR_NAME,
    description=DESCRIPTION,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="jotiroygit.com",
    license="MIT",
    python_requires =">=3.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)