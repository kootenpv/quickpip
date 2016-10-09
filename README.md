## quickpip

[![Build Status](https://travis-ci.org/kootenpv/quickpip.svg?branch=master)](https://travis-ci.org/kootenpv/quickpip)
[![PyPI](https://img.shields.io/pypi/v/quickpip.svg?style=flat-square)](https://pypi.python.org/pypi/quickpip/)
[![PyPI](https://img.shields.io/pypi/pyversions/quickpip.svg?style=flat-square)](https://pypi.python.org/pypi/quickpip/)

### Initial flow

- Clone this repo locally:

```bash
git clone https://github.com/kootenpv/quickpip
cd quickpip
```

- Remove preexisting `.git` and make a new git repo:

```bash
rm -rf .git/
git init
```

- Rename folders and file:

```bash
quickpip                      --> yourtool
quickpip/quickpip             --> yourtool/yourtool
quickpip/quickpip/quickpip.py --> yourtool/yourtool/yourtool.py
```

- Go to the new root folder, `yourtool`, and replace `quickpip` occurences with `yourtool` (can also be done manually):

```bash
# OSX
find . -type f -print0 | xargs -0 sed -i '' 's/quickpip/yourtool/g'

# Linux
find . -type f -print0 | xargs -0 sed -i 's/quickpip/yourtool/g'
```

- Install locally: `python setup.py install`

- Run tests with `py.test` (quick) or `tox` (all python versions)

- Be happy. Commit your changes to your local git:

```bash
git add *
git commit -m "initial commit"
```
- Register/login on [github](https://github.com) and create a new empty repository "yourtool"

- Register on [travis-ci.org](https://travis-ci.org/). Make sure you Sync your github. Activate "yourtool".

- Now run:

```bash
git remote add origin git@github.com:yourusername/yourtool.git
git push -u origin master
```

- Your tests will now be run for free by Travis-CI.

- [Register yourself on pypi](https://pypi.python.org/pypi?%3Aaction=register_form)

- Add a `.pypirc` file in your home (~/.pypirc):

```bash
[distutils]
index-servers =
  pypi

[pypi]
repository: https://pypi.python.org/pypi
username:yourusername
password:yourpassword
```

- Set your [classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers) in `setup.py` to describe your package. A good moment to update README.md and README.rst, and perhaps the setup.py the url and description.

- Register your new package on pypi:

```bash
python setup.py register
```

- Upload package to pypi:

```bash
python deploy.py
```

Congratulations :) Now everyone can download *your tool* (using `pip install yourtool`)!

Install yourtool and try it out on the command line by running `yourtool`

Visit every file and try to cleanup whatever you want. Note that you can always test your changes and if something breaks, go back to a previous version on git.

Feel free to hit that "Star" button on the [quickpip github](https://github.com/kootenpv/quickpip) :)

### The flow going forward

- Add new tests

- Make changes

- Test your changes with `py.test` until your tests pass

- Run `tox` to make sure it works for both python 2 and 3

- `git commit -m "second changes"`; save your changes in git

- `git push` your changes to github

- Nicely see your tests pass on [travis](https://travis-ci.org/kootenpv/yourtool), knowing that others can easily contribute.

- When you've added a big new feature, add 1 to your minor version in `setup.py`

- When you've made breaking changes, add 1 to your major version in `setup.py`

- Run `python deploy.py` to deploy a new version on pypi

### Adding new dependencies

Add them in your `setup.py` under `install_requires`. Also add them in your `tox.ini` file under `deps`.

### Changing your command line executable

Edit your `__main__.py`

### Contributing

Feel free to make suggestions.
