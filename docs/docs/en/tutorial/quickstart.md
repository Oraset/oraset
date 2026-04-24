# Quick Start

## Installing Oraset

### From Source

1. Clone or download the Oraset source code to your local machine
2. Ensure your system has Python 3.6 or higher installed
3. Navigate to the Oraset directory and run the `oraset.py` file directly

### From Binary

1. Download the binary file for your platform (`.exe` for Windows, executable for Linux)
2. Extract it to any directory
3. Add the executable directory to your system environment variables (optional)

## Running Your First Program

### Create a Program File

Create a file named `hello.oraset` with the following content:

```oraset
!! This is a comment
show(`Hello, Oraset!`);
```

### Run the Program

#### Using Python

```bash
python oraset.py hello.oraset
```

#### Using Binary

```bash
# Windows
oraset.exe hello.oraset

# Linux
./oraset hello.oraset
```

### Expected Output

After running the program, you should see the following output:

```
Hello, Oraset!
```

## Basic Syntax Examples

### Variable Assignment

```oraset
name = `John`;
age = 25;
price = 9.99;
```

### Output

```oraset
show(`Name: `, name);
show(`Age: `, age);
show(`Price: `, price);
```

### Simple Calculation

```oraset
num1 = 10;
num2 = 20;
sum = num1 + num2;
show(`Sum: `, sum);
```

## Next Steps

- Learn about [Basic Syntax](basic-syntax.md) for more syntax rules
- Understand how to use [Data Types](data-types.md)
- Learn about [Control Structures](control-structures.md) like conditionals and loops
- Explore [Functions](functions.md) for defining and using functions

## Common Issues

### No Output When Running Program

- Check if you're using the `show` function
- Ensure the file path is correct
- Check for syntax errors

### Syntax Errors

- Check that parentheses are matched
- Ensure strings are enclosed in backticks
- Verify variable names are correct

### Command Not Found

- Ensure the Oraset directory is added to your environment variables
- Or use the absolute path to run

## Example Code

### Calculating Factorial

```oraset
def factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

show(`5! = `, factorial(5));
```

### Array Operations

```oraset
fruits = arr(`apple`, `banana`, `cherry`);
show(`Fruits: `, fruits);
show(`First fruit: `, fruits[0]);
```