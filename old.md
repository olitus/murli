# mur - python tool manager

## Useful commands
`pip install —editable .`


## Abstractions
- Interpreter
- Compiler
- Static Checker
- Linter
- Publisher
- Environment manager

```
pyto init /path-to-dir/

# options
--script (deafault)
--package
--bin

--python (Python version to use)

--control <git> (also init git there)

--help
```

```
pyto package
```

```
pyto run

# Options
-- unsafe (do not perform any static checks)
```

```
# add more commands to murli
pyto plugin <name>
```

- Automate this shit:
```
pip install --editable .
```

- [How to set Python’s default version to 3.x on OS X? - Stack Overflow](https://stackoverflow.com/a/38806058)
```
pyto set python default python3

unlink /usr/local/bin/python
ln -s /usr/local/bin/python3.3 /usr/local/bin/python
```

Whole Python ecosystem in one command line

Even for simple projects we recommend using naga as it structures all the code and makes sure all your project are consistent

Naga works the same on all OS and has same commands.

Look at rustfmt and cargo
Adds dependencies

`naga new hello_naga`
Generates a new dir:
hello_naga
    hello_naga
        main.py
    pyenv_hello_naga
    Pipfile
    .git
    .gitignore

Git will not be generated of run inside other git repo
Option `—-vcs` let’s you override default behavior 
Also find author info from the environment 
Also main.py contains a basic python app

If you have a project that does not use naga, conversion is easy, simply use:

`naga init pkg-name`

To compile python code:
`naga build`

To run the script
`naga run`

To run the compiled script
`naga run -c`

To check code for errors:
`naga check`

Add extensibility like this:
`rustup component add clippy`

# naga
Naga is a human beneficial tool that collects best of the python world

Inspired by cargo

naga is a wrapper for python + main tools
naga is NOT a seperate language
naga is a collection of PEP that I liked (PEP8, PEP484) and other standarts such as Sphinx markup
naga is a tool that uses other tools (python, pip, mypy, sphinx, venv)
naga is written in Python3
naga only uses Python3.7+

### Where is structure from?
- [GitHub - navdeep-G/samplemod](https://github.com/navdeep-G/samplemod)

### How to install?
```
...
```

### Usage example:
```Bash
cd new-py-project
naga init                                           # creates a new virtual envirnment if there is none, otherwise uses the existing venv
naga activate                                       # activate the environment
(new-py-project-env) naga install                   # looks at imports and installs all the requirements
(new-py-project-env) run my-script.py               # run default static checks and then the script
```

```Bash
cd new-web-project
naga init --copy ~/my-global-web-venv                         # copies the given venv
naga activate
(new-web-project) naga check --imports                        # make sure all the imports are valid
(new-web-project) run --time --no-check my-web-script.py      # run the script skipping all checks and with tracking time
(new-web-project) default run my-web-script.py                # make the default run to given script
(new-web-project) naga run                                    # now eq to naga run my-web-script.py
```


### Commands
```
$ naga init <optional: dir-path>
  Initialize the environment, creates the initial dir structure.
  Options:
    --enter : enter the environment after initializing
    --name : give name of the package, default: uses dir name
    --version : Specify the Python version, deafault: the most recent one
    --requirments : Will also generate requrimnets file based .py files in the dir
    
$ naga enter
  Enters the envirnment, uses the closes env, if none found, uses the default
  Options:
    --requirments : Will also generate requrimnets file based .py files in the dir

$ naga exit
  Exit the envirnment
  Options:
    --requirments : Will also generate requrimnets file based .py files in the dir
    
$ naga install <pkg-name>
  Install a pkg using pip or easy_install
  
$ naga install --all
  Install all pkg using pip or easy_install
  
$ naga uninstall <pkg-name>
  Uninstalls pkg
  
$ naga clean
  Cleans the env from all unused
  
$ naga doc <python-file>
  Generates doc using sphix

$ naga run <python-file>
  Options:
    --skip-check : skips all checks
    
$ naga check <pythyn-file>
  Runs all the checks
  
$ naga typing on

$ naga typing off
```

```
use io from std
use RandNumGen from rand

setup proc setup():
    do nothing

main proc game():
    print("Guess the number!");

    val secret: Int = 
         rand.gen_range([1..100])

    print(f"The secret number is
          {secret}");

    print("Please input your
          guess.");

    var guess: Maybe(String) =
        io.read_line()

    match guess:
        case Ok: 
             guess = guess.val
        case Error:
             print(guess.err)
          

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    print(f"You guessed: {guess}")
```


# Naga: Python Developmet Workflow for Monsters
### Naga
### is a tool that brings the best of the Python world together to create
### a great developmet envirnment for your projects.
### Naga
### manipulates:
* ### pipenv: packages and virtual envirnments
* ### mypy: typing checks
* ### flake8: syntax
### Naga
### enforces:
* ### PEP 8
### Naga
### is very opinionated, but open for contribution.

### Naga is a human beneficial tool that collects best of the python world
### Inspired by cargo
### pyto is a wrapper for python + main tools
### pyto is NOT a seperate language
### pyto is a collection of PEP that I liked (PEP8, PEP484) and other standarts such as Sphinx markup
### pyto is a tool that uses other tools (python, pip, mypy, sphinx, venv)
### pyto is written in Python3
### pyto only uses Python3.7+
# How to install?
…

# Usage example:
cd new-py-project
pyto init                                           # creates a new virtual envirnment if there is none, otherwise uses the existing venv
naga activate                                       # activate the environment
(new-py-project-env) naga install                   # looks at imports and installs all the requirements
(new-py-project-env) run my-script.py               # run default static checks and then the script

cd new-web-project
pyto init —copy ~/my-global-web-venv                         # copies the given venv
pyto activate
(new-web-project) pyto check —imports                        # make sure all the imports are valid
(new-web-project) run —time —no-check my-web-script.py      # run the script skipping all checks and with tracking time
(new-web-project) default run my-web-script.py                # make the default run to given script
(new-web-project) pyto run                                    # now eq to naga run my-web-script.py

# Commands
$ pyto init <optional: dir-path>
Initialize the environment, creates the initial dir structure.
Options:
  —enter : enter the environment after initializing
  —name : give name of the package, default: uses dir name
  —version : Specify the Python version, default: the most recent one
  —requirements : Will also generate requirements file based .py files in the dir
   
$ pyto enter
Enters the environment, uses the closes env, if none found, uses the default
Options:
  —requirements : Will also generate requirements file based .py files in the dir

$ pyto exit
Exit the environment
Options:
  —requirements : Will also generate requirements file based .py files in the dir
   
$ pyto install <pkg-name>
Install a pkg using pip or easy_install
 
$ pyto install —all
Install all pkg using pip or easy_install
 
$ pyto uninstall <pkg-name>
Uninstalls pkg
 
$ pyto clean
Cleans the env from all unused
 
$ pyto doc <python-file>
Generates doc using sphix

$ pyto run <python-file>
Options:
  —skip-check : skips all checks
   
$ pyto check <pythyn-file>
Runs all the checks
 
$ pyto typing on

$ pyto typing off



### Cool things
- https://github.com/typeddjango/awesome-python-typing



#dev/cli
