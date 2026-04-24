# Oraset Programming Language

Oraset is a simple cross-platform programming language implemented in Python, supporting both Windows and Linux systems.

## Features

- Cross-platform operation (Windows and Linux)
- Simple and easy-to-understand syntax
- Support for variable definition and assignment
- Support for expression evaluation (arithmetic, comparison, logical)
- Support for conditional statements (if, else if, else)
- Support for loop statements (while)
- Support for function definition and call
- Support for class definition
- Support for output functionality
- Support for comments

## Quick Start

### Runtime Environment

- Python 3.6+

### How to Run

```bash
# Run .oas or .oraset file
python oraset.py <filename.oas|.oraset>

# Pack .oas or .oraset file into .osp file
python oraset.py pack <filename.oas|.oraset>

# Run .osp file
python oraset.py -osp <filename.osp>
```

### Example

Create a file named `hello.oas` with the following content:

```oraset
!! Output Hello, Oraset!
show(`Hello, Oraset!`);

!! Variable definition and calculation
x = 10;
y = 20;
sum = x + y;
show(`10 + 20 = `, sum);

!! Conditional statement
if (sum > 25) {
    show(`Sum is greater than 25`);
} else {
    show(`Sum is less than or equal to 25`);
}

!! Loop statement
i = 0;
while (i < 5) {
    show(`i = `, i);
    i = i + 1;
}

!! Function definition
def add(a, b) {
    return a + b;
}

!! Function call
result = add(5, 6);
show(`5 + 6 = `, result);

!! Class definition
class Calculator {
    def multiply(a, b) {
        return a * b;
    }
}
```

Run:

```bash
python oraset.py hello.oas
```

## Syntax Guide

### Comments

Use `!!` to start a single-line comment:

```oraset
!! This is a comment
```

Use `!*` and `*!` to enclose multi-line comments:

```oraset
!* This is a
multi-line comment *!
```

### Built-in Library Functions

Oraset provides the following built-in library functions:

#### Math Functions

| Function | Description | Example |
|---------|-------------|--------|
| `abs(x)` | Returns the absolute value of x | `abs(-10)` → `10` |
| `max(x, y)` | Returns the maximum of x and y | `max(10, 20)` → `20` |
| `min(x, y)` | Returns the minimum of x and y | `min(10, 20)` → `10` |
| `pow(x, y)` | Returns x raised to the power of y | `pow(2, 3)` → `8` |
| `sqrt(x)` | Returns the square root of x (integer part) | `sqrt(16)` → `4` |

#### String Functions

| Function | Description | Example |
|---------|-------------|--------|
| `len(s)` | Returns the length of string s | `len("Hello")` → `5` |
| `upper(s)` | Converts string s to uppercase | `upper("Hello")` → `HELLO` |
| `lower(s)` | Converts string s to lowercase | `lower("HELLO")` → `hello` |
| `substring(s, start, end)` | Returns the substring of s from start to end | `substring("Hello", 0, 3)` → `Hel` |
| `startsWith(s, prefix)` | Checks if string s starts with prefix | `startsWith("Hello", "He")` → `1` |
| `endsWith(s, suffix)` | Checks if string s ends with suffix | `endsWith("Hello", "lo")` → `1` |
| `replace(s, old, new)` | Replaces old with new in string s | `replace("Hello", "He", "Hi")` → `Hiello` |
| `split(s, sep)` | Splits string s by separator sep | `split("a,b,c", ",")` → `["a", "b", "c"]` |
| `trim(s)` | Removes whitespace from both ends of string s | `trim("  Hello  ")` → `Hello` |

#### Array Functions

| Function | Description | Example |
|---------|-------------|--------|
| `array(...items)` | Creates an array with the specified elements | `array("a", "b", "c")` → `["a", "b", "c"]` |
| `push(arr, item)` | Adds an element to the array | `push(["a", "b"], "c")` → `["a", "b", "c"]` |
| `pop(arr)` | Removes the last element from the array | `pop(["a", "b", "c"])` → `["a", "b"]` |
| `indexOf(arr, item)` | Returns the index of item in array arr, or -1 if not found | `indexOf(["a", "b", "c"], "b")` → `1` |

#### Type Check Functions

| Function | Description | Example |
|---------|-------------|--------|
| `is_number(x)` | Checks if x is a number | `is_number("123")` → `1` |
| `is_string(x)` | Checks if x is a string | `is_string("Hello")` → `1` |

#### Other Functions

| Function | Description | Example |
|---------|-------------|--------|
| `input(prompt)` | Gets input from the user | `input("Enter a value: ")` |
| `int(s)` | Converts string s to an integer | `int("123")` → `123` |
| `str(x)` | Converts x to a string | `str(123)` → `"123"` |

#### File Operation Functions

| Function | Description | Example |
|---------|-------------|--------|
| `file_read(filename)` | Reads file content | `file_read("test.txt")` |
| `file_write(filename, content)` | Writes content to file | `file_write("test.txt", "Hello")` |
| `file_exists(filename)` | Checks if file exists | `file_exists("test.txt")` → `1` (exists) or `0` (does not exist) |

#### Time Functions

| Function | Description | Example |
|---------|-------------|--------|
| `time_now()` | Gets current timestamp | `time_now()` |
| `time_sleep(seconds)` | Sleeps for specified seconds | `time_sleep(2)` |

#### Random Functions

| Function | Description | Example |
|---------|-------------|--------|
| `random_int(min, max)` | Generates random integer between min and max | `random_int(1, 100)` |
| `random_float()` | Generates random float between 0 and 1 | `random_float()` |

#### System Functions

| Function | Description | Example |
|---------|-------------|--------|
| `system(command)` | Executes system command | `system("dir")` |
| `get_env(var_name)` | Gets environment variable | `get_env("PATH")` |



### Math Module

**Note: Using math functions requires importing the math module first**

```oraset
import math
```

| Function | Description | Example |
|---------|-------------|--------|
| `abs(x)` | Returns the absolute value of x | `abs(-10)` → `10.0` |
| `max(x, y)` | Returns the maximum of x and y | `max(10, 20)` → `20.0` |
| `min(x, y)` | Returns the minimum of x and y | `min(10, 20)` → `10.0` |
| `pow(x, y)` | Returns x raised to the power of y | `pow(2, 3)` → `8.0` |
| `sqrt(x)` | Returns the square root of x | `sqrt(16)` → `4.0` |
| `sin(x)` | Returns the sine of x (in degrees) | `sin(90)` → `1.0` |
| `cos(x)` | Returns the cosine of x (in degrees) | `cos(0)` → `1.0` |
| `tan(x)` | Returns the tangent of x (in degrees) | `tan(45)` → `1.0` |
| `asin(x)` | Returns the arcsine of x (in degrees) | `asin(1)` → `90.0` |
| `acos(x)` | Returns the arccosine of x (in degrees) | `acos(1)` → `0.0` |
| `atan(x)` | Returns the arctangent of x (in degrees) | `atan(1)` → `45.0` |
| `pi()` | Returns the value of pi | `pi()` → `3.141592653589793` |
| `e()` | Returns the value of e | `e()` → `2.718281828459045` |

#### Network Request Functions

**Note: Using network request functions requires importing the http module first**

```oraset
import http
```

| Function | Description | Example |
|---------|-------------|--------|
| `http_get(url)` | Sends an HTTP GET request and returns the response | `http_get("http://example.com")` |
| `http_post(url, data)` | Sends an HTTP POST request and returns the response | `http_post("http://httpbin.org/post", "{\"name\": \"Oraset\", \"version\": \"1.0\"}")` |

### Plugin System

Oraset supports user-defined plugins. You can place your extension functions in the `includes` folder.

#### Creating a Plugin

1. Create a file with `.oraset` extension in the `includes` folder
2. Define functions, classes, etc. in the file
3. Load the plugin using `import plugin_name` directive

#### Example

Create `includes/math_utils.oraset` file:

```oraset
!! Math utilities plugin

def add(a, b) {
    return a + b;
}

def subtract(a, b) {
    return a - b;
}
```

Use it in your code:

```oraset
import math_utils

result = add(10, 20);
show(`10 + 20 = `, result);
```

### Variables

Variable definition and assignment:

```oraset
x = 10;  // Integer
message = `Hello`;  // String
```

### Data Types

- Integers: `10`, `20`, `30`
- Strings: `` `Hello` ``, `` `World` ``

Strings support the following escape sequences:

| Escape Sequence | Description |
|----------------|-------------|
| `\n` | Newline |
| `\t` | Tab |
| `\r` | Carriage return |
| `\\` | Backslash |
| `` \` `` | Backtick |

Examples:

```oraset
// Output multi-line text
show(`Line 1\nLine 2`);

// Output text with tabs
show(`Column 1\tColumn 2`);

// Output text with backslashes
show(`Path: C:\\Users\\Name`);
```

### Operators

#### Arithmetic Operators

- `+`：Addition
- `-`：Subtraction
- `*`：Multiplication
- `/`：Division (integer division)

#### Comparison Operators

- `==`：Equal to
- `!=`：Not equal to
- `<`：Less than
- `<=`：Less than or equal to
- `>`：Greater than
- `>=`：Greater than or equal to

#### Logical Operators

- `&&`：Logical AND
- `||`：Logical OR

#### Assignment Operators

- `=`：Assignment
- `+=`：Add assignment
- `-=`：Subtract assignment
- `*=`：Multiply assignment
- `/=`：Divide assignment

### Conditional Statements

```oraset
if (condition) {
    // Code block
} else if (condition) {
    // Code block
} else {
    // Code block
}
```

### Loop Statements

```oraset
while (condition) {
    // Code block
}
```

### Function Definition

```oraset
def function_name(parameter1, parameter2, ...) {
    // Code block
    return value;
}
```

### Function Call

```oraset
result = function_name(arg1, arg2, ...);
```

### Class Definition

```oraset
class ClassName {
    def method_name(parameter1, parameter2, ...) {
        // Code block
        return value;
    }
}
```

### Output

Use the `show` function to output content:

```oraset
show(`Hello`);
show(`The value is `, x);
```

## Example Code

### Basic Example

```oraset
// Variables and expressions
x = 10;
y = 20;
sum = x + y;
show(`Sum: `, sum);

// Conditional statements
if (sum > 25) {
    show(`Sum is greater than 25`);
} else if (sum == 25) {
    show(`Sum is exactly 25`);
} else {
    show(`Sum is less than 25`);
}

// Loop statements
i = 0;
while (i < 5) {
    show(`i = `, i);
    i += 1;
}
```

### Function Example

```oraset
// Function definition
def add(a, b) {
    return a + b;
}

def multiply(a, b) {
    return a * b;
}

// Function call
result1 = add(10, 20);
result2 = multiply(5, 6);
show(`10 + 20 = `, result1);
show(`5 * 6 = `, result2);

// Recursive function
def factorial(n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

result = factorial(5);
show(`Factorial of 5 is `, result);
```

### Class Example

```oraset
// Class definition
class Calculator {
    def add(a, b) {
        return a + b;
    }
    
    def subtract(a, b) {
        return a - b;
    }
    
    def multiply(a, b) {
        return a * b;
    }
    
    def divide(a, b) {
        return a / b;
    }
}

// Note: Class method calls need to be implemented through functions
// In the current version, class definitions are stored but not directly instantiated
```

## Project Structure

```
Oraset/
├── oraset.py          # Core interpreter
├── examples/          # Example code
│   ├── hello.oas      # Basic example
│   ├── hello.osp      # Packed basic example
│   ├── functions.oas  # Function example
│   └── classes.oas    # Class example
├── README.md          # This tutorial (Chinese)
└── README.en_us.md    # This tutorial (English)
```

## .osp File Description

.osp files are the packed file format for Oraset, generated by compressing and encoding .oas files. They have the following features:

- **Encryption**: .osp files use base64 encoding and zlib compression, making the source code not easily viewable directly
- **Cross-platform**: .osp files can be run directly on both Windows and Linux systems
- **Convenience**: .osp files are standalone files that can be easily distributed and used

### Packing .oas Files

Use the `pack` command to pack .oas files into .osp files:

```bash
python oraset.py pack <filename.oas>
```

This will generate a file with the same name as the .oas file but with the .osp extension.

### Running .osp Files

Use the `-osp` parameter to run .osp files:

```bash
python oraset.py -osp <filename.osp>
```

This will automatically decompress and execute the code in the .osp file.

## Development Notes

Oraset is implemented in Python and mainly consists of the following components:

- **Lexer**: Lexical analyzer, responsible for converting source code into tokens
- **Parser**: Syntax analyzer, responsible for building abstract syntax tree (AST)
- **Interpreter**: Interpreter, responsible for executing AST and generating results

## Future Plans

- Support more data types (floating-point numbers, booleans, etc.)
- Improve class instantiation and method calls
- Support module import
- Add standard library
- Optimize performance

## License

GNU General Public License v3.0
