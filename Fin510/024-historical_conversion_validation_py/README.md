# History Currency Conversion - Validation

This assignment builds on the previous Historical Currency Conversion
assignment, but with a focus on validation, whether the data comes from 
command-line arguments, user input, or a file.

When a program exits in a Linux environment, a status code is returned to the
calling program. This value serves as an indication of how the process ended -
whether it was successful or encountered an error. As multiple error conditions
may arise, 0 indicates success and any non-zero value indicates a failure.
(Notice the difference from a programming perspective where 0 typically indicates
`False`.)

In the Linux shell, we can see the exit code of the previous program through a 
special variable: `$?`


```text
% echo "hello world"
hello world
% echo $?
0
% ls fileNotExists.txt
ls: fileNotExists.txt: No such file or directory
% echo $?
1
```

In Python, we can use the function `exit()` from the `sys` module to immediately 
terminate the program/script and return a specific value to the calling program 
(shell).

```python
import sys

sys.exit(0)  # success
sys.exit(1)  # failure

exit(10)  # usually works, but can also be disabled 
```

If your program crashes due to an unhandled exception, Python - 
* prints the traceback to `stderr`
* exits with a status code of `1`

Due to this behavior, you'll need to specify specific error codes as 
defined in the assignment details when you either detect a data problem
through validation or when a specific exception occurs.


## Learning Objectives
- Data validation
- Command-line argument processing
- Error handling
- Handling user input and formatting output

## Assignment Details
Using `conversion.py` from the prior currency conversion assignment, perform
the following steps:

1. Copy the `conversion.py` and the data file from the previous assignment
   into this assignment's directory. Look at the [`cp`](https://fintechpython.pages.oit.duke.edu/jupyternotebooks/9-The%20Tools/1-Bash-Basics.html#copying-files-and-directories) command.  [tldr version](https://tldr.inbrowser.app/pages/common/cp)

   `..` specifies the parent directory.

2. Modify the program to get the name of the currency data program from
   a command-line argument:
   `python3 conversion.py nameOfHistoricalCurrencyData.json`

3. For the following situations, exit the program with the corresponding
   error/status code:

   | Situation                                          | Code |
   |----------------------------------------------------|-----:|
   | Invalid number of command-line arguments           | 2    |
   | Data file does not exist                           | 3    |
   | Data file contains invalid JSON                    | 4    |
   | Invalid currency code                              | 5    |
   | Invalid date / date not in file                    | 6    |
   | Date rate for a particular current code is not > 0 | 7    |
   | Invalid amount to convert                          | 8    |

4. While the grader will not check output text (other than checking that
   the program functions correctly), you must print an appropriate
   message to stderr.  This will also help you validate your program.
   
5. As necessary, create your own test data files.