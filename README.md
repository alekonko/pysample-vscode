# pysample-vscode: simple helloworl for use VSCODE + Python + virtualenv + git


Create your repo on github 

```
echo "# pysample-vscode" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/alekonko/pysample-vscode.git
git push -u origin main
```

Create right .gitignore files, can you use online generator, [this](https://docs.gitignore.io/install/command-line#git)   offer easy api scripts

- for VSCODE native extension
Press Cmd+P for MacOS and Ctrl+P for Linux/Windows to launch VS Code Quick Open, paste the following command, and press enter.

```
ext install gi
```

- for PSH
```psh
#creo funzione, For PowerShell v3
Function gig {
  param(
    [Parameter(Mandatory=$true)]
    [string[]]$list
  )
  $params = ($list | ForEach-Object { [uri]::EscapeDataString($_) }) -join ","
  Invoke-WebRequest -Uri "https://www.toptal.com/developers/gitignore/api/$params" | select -ExpandProperty content | Out-File -FilePath $(Join-Path -path $pwd -ChildPath ".gitignore") -Encoding ascii
}

# creo .gitignore
gig "vscode","python","windows"

```

- for bash
```
# add to your .bashrc file
gig(){
  curl -sL https://www.toptal.com/developers/gitignore/api/$@
  }
  
gig vscode python
```

Create virtual env for your project

- Windows 10 (python 3.9)

```
# create venv
py -3 -m venv .venv
# activate venv
.venv\scripts\activate
# update pip (if needed)
C:\dev\python\.venv\scripts\python.exe -m pip install --upgrade pip
```

- Linux (Fedora 33 - python 3.9)

```
# create venv
python -m venv .venv
# activate venv
source .venv/bin/activate
# update pip (if needed)
.venv/bin/python -m pip install --upgrade pip
```

From officials documentation [python/environments](https://code.visualstudio.com/docs/python/environments)

To select a specific environment, use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P).

 ![Command Palette](docs/select-interpreters-command.png)

You can switch environments at any time; switching environments helps you test different parts of your project with different interpreters or library versions as needed.

The Python: Select Interpreter command displays a list of available global environments, conda environments, and virtual environments. (See the Where the extension looks for environments section for details, including the distinctions between these types of environments.) The following image, for example, shows several Anaconda and CPython installations along with a conda environment and a virtual environment (env) that's located within the workspace folder:

 ![Command Palette](docs/interpreters-list.png)


Use pip for install your favourite module and start coding

Create requirements at the end of project with pip freeze and put it in requirements.txt

```
pip freeze > requirements.txt
```

- install requirements

```
pip install -r requirements.txt
```

or with new resolve feature (better align dependency)

```
pip install -r requirements.txt --use-feature=2020-resolver
```


Push on you repo


bye
Ale
