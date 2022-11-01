[![Build Status](
https://travis-ci.com/nickrusso42518/slt-py-example.svg?branch=master)](
https://travis-ci.com/nickrusso42518/slt-py-example)

# Safari Live Training - Python By Example
Source code for the training course. Please contact me with any questions.
Before beginning, be sure you know how to use `git` at a basic level on
your computer (Windows, Mac OS, or Linux).


> Contact information:\
> Email:    njrusmc@gmail.com\
> Twitter:  @nickrusso42518

  * [Download Instructions](#download-instructions)
  * [Usage](#usage)
  * [Testing](#testing)

## Download Instructions
The easiest way to consume this code is to clone it using SSH or HTTPS.

SSH: `git clone git@github.com:nickrusso42518/slt-py-example.git`

or

HTTPS: `git clone https://github.com/nickrusso42518/slt-py-example.git`

After cloning, you should see the following file system structure:

```
$ tree
.
├── Makefile
├── README.md
├── complete.py
├── fundamental.py
├── inputs
│   ├── circle.yml
│   └── rectangle.json
├── requirements.txt
├── shape_pytest.py
├── shape_unittest.py
├── shapes
│   ├── __init__.py
│   ├── circle.py
│   ├── rectangle.py
│   └── shape.py
├── small
│   ├── (many files ...)
└── unittests
    ├── __init__.py
    ├── circle_test.py
    └── rectangle_test.py
```

Ensure you have Python 3.6 or newer installed along with pip.
Ideally, you should have 3.10 to be on par with the instructor.
Note that some minor features require 3.7 or 3.8, but the main
programs can run on 3.6 at a minimum.

```
$ python --version
Python 3.10.5
```

> Visit https://www.python.org/downloads/ to download Python.

`sudo python -m ensurepip`

or

`sudo easy_install pip`

No need to install any packages via pip; this is done during the course.

To get setup, first run `make setup` which will install the required
Python packages and create the `outputs/` directory. Failing to take
this step could result in errors later in the course.

Optionally, run `make` to run a full suite of testing on the code
to ensure everything works. After a fresh `git clone` there should
be no errors.

## Usage
There are two main programs to run, `fundamentals.py` and `complete.py`.
Each program performs some computations on basic shapes, such as area
and perimeter. The input data is included in the `inputs/` folder and uses
YAML for circle radii and JSON for rectangle lengths/widths. Outputs are
written to `outputs/` as JSON files.

The `fundamentals.py` code is a halfway point through the course used to
illustrate the fundamental concepts introduced earlier in the course. It
takes zero or one arguments. When no arguments are supplied, the script
is interactive and asks the user whether the units are inches (in) or
centimeters (cm).

```
$ python fundamental.py
Choose unit of measure (cm or in): in
radius 5 -> area 78.54 in sq
radius 8 -> area 201.06 in sq
radius 11 -> area 380.13 in sq
radius 5 -> perim 31.42 in
radius 8 -> perim 50.27 in
radius 11 -> perim 69.12 in
rectangle1
 8x2 -> area 16 in sq
 (8+2)x2 -> perim 20 in
rectangle2
 3x3 -> area 9 in sq
 (3+3)x2 -> perim 12 in
rectangle3
 1x6 -> area 6 in sq
 (1+6)x2 -> perim 14 in
```

When one argument is supplied, the script is non-interactive, as `in` or `cm`
has been specified.

```
$ python fundamental.py cm
radius 5 -> area 78.54 cm sq
radius 8 -> area 201.06 cm sq
radius 11 -> area 380.13 cm sq
radius 5 -> perim 31.42 cm
radius 8 -> perim 50.27 cm
radius 11 -> perim 69.12 cm
rectangle1
 8x2 -> area 16 cm sq
 (8+2)x2 -> perim 20 cm
rectangle2
 3x3 -> area 9 cm sq
 (3+3)x2 -> perim 12 cm
rectangle3
 1x6 -> area 6 cm sq
 (1+6)x2 -> perim 14 cm
```

If the interactive or command line argument is bogus, the program keeps
asking for the current input (case insensitive):

```
$ python fundamental.py dog
Choose unit of measure (cm or in): cat
Choose unit of measure (cm or in): monkey
Choose unit of measure (cm or in): CM
radius 5 -> area 78.54 cm sq
radius 8 -> area 201.06 cm sq
radius 11 -> area 380.13 cm sq
radius 5 -> perim 31.42 cm
radius 8 -> perim 50.27 cm
radius 11 -> perim 69.12 cm
rectangle1
 8x2 -> area 16 cm sq
 (8+2)x2 -> perim 20 cm
rectangle2
 3x3 -> area 9 cm sq
 (3+3)x2 -> perim 12 cm
rectangle3
 1x6 -> area 6 cm sq
 (1+6)x2 -> perim 14 cm
```

The `complete.py` code wraps up almost everything in this class within
a simple small program. It relies on the `shapes` package and its
component modules. The user input is similar to `fundamental.py` in
that either `in` or `cm` must be specified with some formatting
exceptions described previously. The code uses object-oriented
programming, abstract classes, polymorphism, and YAML/JSON interaction
for execution.

```
$ python complete.py cm
Type:  Rectangle
 Area:  21 cm sq
 Perim: 20 cm

Type:  Rectangle
 Area:  25 cm sq
 Perim: 20 cm

Type:  Rectangle
 Area:  6 cm sq
 Perim: 14 cm

Type:  Circle
 Area:  201.06 cm sq
 Perim: 50.27 cm

Type:  Circle
 Area:  78.54 cm sq
 Perim: 31.42 cm
```

## Testing
A GNU Makefile with phony targets is used for testing this codebase.
There are currently three steps:
  * `setup`: Installs required Python packages in the `requirements.txt`
    file using `pip`. Creates `outputs/` directory.
  * `lint`: Runs YAML and Python linters. This captures any syntax or
    styling errors with the code.
  * `unit`: Runs `unittest` and `pytest` unit tests for the rectangle and
    circle classes. This ensures the methods in each classes are operating
    correctly.
  * `run`: Runs the two programs with both `in` and `cm` as inputs.
    The default input files should have no failures.

You can run `make` or `make all` to run all the testing in series when doing
manual regression testing from the shell. As mentioned earlier in the README,
this is a good idea after first cloning the repository.
