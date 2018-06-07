
Setup autopep8 in pycharm:

1. Run `pip3 install autopep8`
2. Open `Pycharm`, go to menu -> preferences -> external tools -> click '+' to add a new tool.
3. filling:
    Name: autopep8
    Program: autopep8
    Arguments: --in-place --aggressive --aggressive $FilePath$
    Working directory: $ProjectFileDir$
    Advanced Options -> Output filters: $FILE_PATH$\:$LINE$\:$COLUMN$\:.*
4. Click OK / Apply


Use autopep8 in pycharm:

Right click in file, select external tools -> autopep8
