# statesxt


<br/>

## How to install?

- Manually cloning the project in Github repository: [statesxt](https://github.com/jsonnnnn/statesxt)
- Using `pip`, that the package is hosted in [here](https://test.pypi.org/project/statesxt/) <b>(recommended)</b>. 
  Currently, due to the Pypi repository being down and is blocking any account registers and project uploads, the package is now hosted on TestPypi for the time being.
  ```
  pip install -i https://test.pypi.org/simple/ statesxt
  ```

## How to uninstall?
There are two approaches or options to uninstall the package.
- Uninstalling only the package
  ```
  pip uninstall statesxt
  ```
- Uninstalling the package and its dependencies <b>(vulnerable)</b>.
  To do this, the user must install a package called `pip-autoremove` (if not already installed).
  ```
  pip install pip-autoremove
  ```
  Once the package is installed, user can now uninstall the package with the following command.
  ```
  pip-autoremove statesxt -y
  ```
  Note: If there is an error saying that `ModuleNotFoundError: No module named 'pip_autoremove'`, you could try to move the `pip_autoremove.py` file from `./Scripts` into `./Lib` instead. For further information: [here](https://stackoverflow.com/questions/74523001/modulenotfounderror-when-trying-to-use-pip-autoremove).

## How to update?

Currently, the package can't be updated through usual command `pip install --upgrade statesxt`. Probably because is hosted in TestPypi.
So, for the time being, user have to reinstall the package.

## How to use?

- Generating the framework
  ```bash
  statesxt gen
  ```
- Remove the framework
  ```
  statesxt rem
  ```
