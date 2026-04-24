# Basic Syntax

## Comments

Oraset supports two types of comments:

### Single-line Comments

Use `!!` to start a single-line comment:

```oraset
!! This is a single-line comment
name = `John`; !! This is also a comment
```

### Multi-line Comments

Use `!*` to start and `*!` to end a multi-line comment:

```oraset
!* This is a
multi-line comment
that spans multiple lines *!
age = 25;
```

## Variables

### Variable Declaration and Assignment

In Oraset, variables don't require explicit type declaration, just assign values directly:

```oraset
name = `John`;      !! String
age = 25;           !! Integer
price = 9.99;       !! Float
is_student = true;  !! Boolean
```

### Variable Naming Rules

- Variable names can only contain letters, numbers, and underscores
- Variable names cannot start with a number
- Variable names are case-sensitive
- Variable names cannot use keywords (like `if`, `else`, `def`, etc.)

## Data Types

Oraset supports the following data types:

- **String**: Enclosed in backticks `` ` ``
- **Number**: Integer and float
- **Boolean**: `true` and `false`
- **Array**: Created using `arr()` function
- **Object**: Created using `obj()` function

## Operators

### Arithmetic Operators

| Operator | Description | Example |
|---------|-------------|---------|
| `+`     | Addition    | `1 + 2` |
| `-`     | Subtraction | `5 - 3` |
| `*`     | Multiplication | `2 * 4` |
| `/`     | Division    | `10 / 2` |
| `%`     | Modulus     | `7 % 3` |
| `**`    | Exponentiation | `2 ** 3` |

### Comparison Operators

| Operator | Description | Example |
|---------|-------------|---------|
| `==`    | Equal to    | `x == y` |
| `!=`    | Not equal to | `x != y` |
| `<`     | Less than   | `x < y` |
| `>`     | Greater than | `x > y` |
| `<=`    | Less than or equal to | `x <= y` |
| `>=`    | Greater than or equal to | `x >= y` |

### Logical Operators

| Operator | Description | Example |
|---------|-------------|---------|
| `&&`    | Logical AND | `x && y` |
| `||`    | Logical OR  | `x || y` |
| `!`     | Logical NOT | `!x` |

### Assignment Operators

| Operator | Description | Example |
|---------|-------------|---------|
| `=`     | Assignment  | `x = 5` |
| `+=`    | Add and assign | `x += 2` |
| `-=`    | Subtract and assign | `x -= 2` |
| `*=`    | Multiply and assign | `x *= 2` |
| `/=`    | Divide and assign | `x /= 2` |

## Expressions

Expressions are combinations of operators and operands used to calculate values:

```oraset
result = (10 + 5) * 2; !! Result is 30
area = 3.14 * (radius ** 2); !! Calculate circle area
```

## Statements

Each statement ends with a semicolon `;`:

```oraset
x = 10;
y = 20;
sum = x + y;
show(`Sum: `, sum);
```

## Indentation

Oraset doesn't strictly require indentation, but for code readability, it's recommended to use 4 spaces or 1 tab for indentation:

```oraset
def greet(name) {
    if (name == `John`) {
        show(`Hello, John!`);
    } else {
        show(`Hello, `, name, `!`);
    }
}
```

## Escape Characters

In strings, you can use backslash `\` to represent escape characters:

| Escape Character | Description |
|-----------------|-------------|
| `\n`            | Newline     |
| `\t`            | Tab         |
| `\\`           | Backslash   |
| `` \` ``        | Backtick    |
| `\"`           | Double quote |
| `\'`           | Single quote |

Example:

```oraset
message = `Hello\nWorld!`; !! Contains newline
path = `C:\\Users\\John`; !! Contains backslashes
```

## Code Style Recommendations

- Use meaningful variable names
- Add comments for complex code
- Maintain consistent indentation style
- Break long lines into multiple lines for readability
- Add docstrings for functions and classes