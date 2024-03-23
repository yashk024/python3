# Python Virtual Environment and Python Package Installer

## Python Package Installer

* [PyPI](https://pypi.org/ "pypi.org")
* `pip` &rarr; an acronym for _`pip` installs packages_

### Some useful commands

* `pip --version` or `pip3 --version`
* `pip help`
* `pip help [operation]`
    * example, `pip help install`
* `pip list` &rarr; to see the list of installed packages
* `pip show package_name` &rarr; to see details of an installed package
    * example, `pip show pip`
* `pip install package_name` or `py -m pip install package_name` &rarr; to install a package
* `pip install requests==2.30.0` &rarr; to install a specific version of a package
* `pip install -U package_name` &rarr; to update a package
* `pip uninstall package_name` &rarr; to uninstall a package

## Python Virtual Environment

* `py -m venv .venv` &rarr; to create a virtual environment
* `.\.venv\Scripts\activate` &rarr; to activate the virtual environment
* `deactivate` &rarr; to deactivate the virtual environment
* `pip freeze > requirements.txt` &rarr; to create a list of dependencies

## Reference

* [Dave Gray](https://youtu.be/eDe-z2Qy9x4?si=4W4dS3eDgnc6iYuW)

---
---
