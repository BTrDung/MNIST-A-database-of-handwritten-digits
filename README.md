# MNIST

MNIST is a database of handwritten digits available on http://yann.lecun.com/exdb/mnist/.

Read more about MNIST on Wikipedia: https://en.wikipedia.org/wiki/MNIST_database.

## Requirements

Use Python 3. 

Version used in this project is Python 3.8.2.

Use Visual Studio Code to run. 

You can download Python and Visual Studio Code by following link: 

Python: https://www.python.org/downloads/. (Remember your location where you installed)

VS Code: https://code.visualstudio.com/.

## Installation

```bash
git clone : https://github.com/BTrDung/MNIST
```
Open folder ```.vscode -> tasks.json ```. Copy your Python.exe location (where you installed Python) and paste to Line 12.

Example: My Python locaion is ```C:\Users\ABC\AppData\Local\Programs\Python\Python38\python.exe```. Copy link location and paste into
tasks.json with a little changes like this:
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "RUN Python File",
            "type": "shell",
            "command": [
                "C:\\Users\\ABC\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
                ,"-u",
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        }
    ]
}
```

Do the same things with ```settings.json```: 
```
{
    "python.pythonPath": "C:\\Users\\ABC\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
}
```

Use Visual Studio Code to open project. Use terminal and get package: 
```
pip install python-mnist
```

```
pip install scikit-learn
```

Press F5 and choose Python to look what it can do. 
