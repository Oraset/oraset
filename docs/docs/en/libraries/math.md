# Math Library

## Introduction

The math library (`@math`) provides a range of mathematical functions, including basic operations, trigonometric functions, random number generation, and more.

## Import

```oraset
@math;
```

## Function Reference

### Basic Math Functions

#### math.abs(x)

Calculate absolute value.

**Parameters:**
- `x` - Number

**Returns:**
- Absolute value of the number

**Example:**

```oraset
show(`abs(-123) = `, math.abs(-123));  // Output: 123
```

#### math.sqrt(x)

Calculate square root.

**Parameters:**
- `x` - Non-negative number

**Returns:**
- Square root value

**Example:**

```oraset
show(`sqrt(16) = `, math.sqrt(16));  // Output: 4
```

#### math.pow(x, y)

Calculate power operation.

**Parameters:**
- `x` - Base
- `y` - Exponent

**Returns:**
- x raised to the power of y

**Example:**

```oraset
show(`pow(2, 3) = `, math.pow(2, 3));  // Output: 8
```

### Trigonometric Functions

#### math.sin(x)

Calculate sine value (in degrees).

**Parameters:**
- `x` - Angle in degrees

**Returns:**
- Sine value

**Example:**

```oraset
show(`sin(90) = `, math.sin(90));  // Output: 1
```

#### math.cos(x)

Calculate cosine value (in degrees).

**Parameters:**
- `x` - Angle in degrees

**Returns:**
- Cosine value

**Example:**

```oraset
show(`cos(0) = `, math.cos(0));  // Output: 1
```

#### math.tan(x)

Calculate tangent value (in degrees).

**Parameters:**
- `x` - Angle in degrees

**Returns:**
- Tangent value

**Example:**

```oraset
show(`tan(45) = `, math.tan(45));  // Output: 1
```

### Math Constants

#### math.pi()

Return the value of pi (π).

**Parameters:** None

**Returns:**
- Value of π (approximately 3.14159...)

**Example:**

```oraset
show(`π = `, math.pi());  // Output: 3.141592653589793
```

#### math.e()

Return the value of Euler's number (e).

**Parameters:** None

**Returns:**
- Value of e (approximately 2.71828...)

**Example:**

```oraset
show(`e = `, math.e());  // Output: 2.718281828459045
```

### Extremum Functions

#### math.max(...args)

Calculate the maximum of multiple numbers.

**Parameters:**
- `...args` - Multiple numbers

**Returns:**
- Maximum value

**Example:**

```oraset
show(`max(10, 5, 20) = `, math.max(10, 5, 20));  // Output: 20
```

#### math.min(...args)

Calculate the minimum of multiple numbers.

**Parameters:**
- `...args` - Multiple numbers

**Returns:**
- Minimum value

**Example:**

```oraset
show(`min(10, 5, 20) = `, math.min(10, 5, 20));  // Output: 5
```

### Random Number Functions

#### math.random()

Generate a random number between 0 and 1.

**Parameters:** None

**Returns:**
- Random float between 0 and 1

**Example:**

```oraset
show(`random() = `, math.random());  // Output: 0.123456...
```

#### math.randint(a, b)

Generate a random integer within a specified range.

**Parameters:**
- `a` - Minimum value
- `b` - Maximum value

**Returns:**
- Random integer between a and b (inclusive)

**Example:**

```oraset
show(`randint(1, 100) = `, math.randint(1, 100));  // Output: 42
```

## Example Code

```oraset
@math;

!! Basic operations
show(`abs(-123) = `, math.abs(-123));
show(`sqrt(16) = `, math.sqrt(16));
show(`pow(2, 3) = `, math.pow(2, 3));

!! Trigonometric functions
show(`sin(90) = `, math.sin(90));
show(`cos(0) = `, math.cos(0));
show(`tan(45) = `, math.tan(45));

!! Math constants
show(`π = `, math.pi());
show(`e = `, math.e());

!! Extremum
show(`max(10, 5, 20) = `, math.max(10, 5, 20));
show(`min(10, 5, 20) = `, math.min(10, 5, 20));

!! Random numbers
show(`random() = `, math.random());
show(`randint(1, 100) = `, math.randint(1, 100));
```