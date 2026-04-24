# String Library

## Introduction

The string library (`@string`) provides a range of string manipulation functions, including string splitting, case conversion, search and replace, and more.

## Import

```oraset
@string;
```

## Function Reference

### Basic String Operations

#### string.split(s, sep)

Split a string into an array based on a specified separator.

**Parameters:**
- `s` - String to split
- `sep` - Separator

**Returns:**
- Array of split elements

**Example:**

```oraset
@string;

text = `Hello,World,Oraset`;
result = string.split(text, `,`);
show(`Split result: `, result);  !! Output: ["Hello", "World", "Oraset"]
```

#### string.upper(s)

Convert a string to uppercase.

**Parameters:**
- `s` - String to convert

**Returns:**
- Uppercase string

**Example:**

```oraset
@string;

text = `hello world`;
result = string.upper(text);
show(`Upper case: `, result);  !! Output: HELLO WORLD
```

#### string.lower(s)

Convert a string to lowercase.

**Parameters:**
- `s` - String to convert

**Returns:**
- Lowercase string

**Example:**

```oraset
@string;

text = `HELLO WORLD`;
result = string.lower(text);
show(`Lower case: `, result);  !! Output: hello world
```

#### string.length(s)

Get the length of a string.

**Parameters:**
- `s` - String to get length of

**Returns:**
- Length of the string

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result = string.length(text);
show(`Length: `, result);  !! Output: 11
```

#### string.substring(s, start, end)

Extract a substring from a string.

**Parameters:**
- `s` - Original string
- `start` - Start index (0-based)
- `end` - End index (optional, defaults to string length)

**Returns:**
- Extracted substring

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.substring(text, 0, 5);
result2 = string.substring(text, 6);
show(`Substring (0-5): `, result1);  !! Output: Hello
show(`Substring (6+): `, result2);  !! Output: Oraset
```

#### string.indexOf(s, substr)

Find the position of a substring in a string.

**Parameters:**
- `s` - Original string
- `substr` - Substring to find

**Returns:**
- Starting position of the substring, or -1 if not found

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.indexOf(text, `Oraset`);
result2 = string.indexOf(text, `World`);
show(`Index of 'Oraset': `, result1);  !! Output: 6
show(`Index of 'World': `, result2);  !! Output: -1
```

#### string.replace(s, old, new)

Replace a substring in a string.

**Parameters:**
- `s` - Original string
- `old` - Substring to replace
- `new` - Replacement substring

**Returns:**
- String with replacements

**Example:**

```oraset
@string;

text = `Hello World`;
result = string.replace(text, `World`, `Oraset`);
show(`Replaced: `, result);  !! Output: Hello Oraset
```

#### string.trim(s)

Remove whitespace from the beginning and end of a string.

**Parameters:**
- `s` - String to process

**Returns:**
- String with whitespace removed

**Example:**

```oraset
@string;

text = `   Hello Oraset   `;
result = string.trim(text);
show(`Trimmed: `, result);  !! Output: Hello Oraset
```

#### string.startsWith(s, prefix)

Check if a string starts with a specified prefix.

**Parameters:**
- `s` - Original string
- `prefix` - Prefix to check

**Returns:**
- Boolean indicating if the string starts with the prefix

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.startsWith(text, `Hello`);
result2 = string.startsWith(text, `World`);
show(`Starts with 'Hello': `, result1);  !! Output: true
show(`Starts with 'World': `, result2);  !! Output: false
```

#### string.endsWith(s, suffix)

Check if a string ends with a specified suffix.

**Parameters:**
- `s` - Original string
- `suffix` - Suffix to check

**Returns:**
- Boolean indicating if the string ends with the suffix

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.endsWith(text, `Oraset`);
result2 = string.endsWith(text, `World`);
show(`Ends with 'Oraset': `, result1);  !! Output: true
show(`Ends with 'World': `, result2);  !! Output: false
```

#### string.includes(s, substr)

Check if a string contains a specified substring.

**Parameters:**
- `s` - Original string
- `substr` - Substring to check

**Returns:**
- Boolean indicating if the string contains the substring

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.includes(text, `Oraset`);
result2 = string.includes(text, `World`);
show(`Includes 'Oraset': `, result1);  !! Output: true
show(`Includes 'World': `, result2);  !! Output: false
```

#### string.repeat(s, count)

Repeat a string a specified number of times.

**Parameters:**
- `s` - String to repeat
- `count` - Number of repetitions

**Returns:**
- Repeated string

**Example:**

```oraset
@string;

text = `Hello `;
result = string.repeat(text, 3);
show(`Repeated: `, result);  !! Output: Hello Hello Hello 
```

#### string.reverse(s)

Reverse a string.

**Parameters:**
- `s` - String to reverse

**Returns:**
- Reversed string

**Example:**

```oraset
@string;

text = `Hello Oraset`;
result = string.reverse(text);
show(`Reversed: `, result);  !! Output: tesarO olleH
```

#### string.capitalize(s)

Capitalize the first letter of a string.

**Parameters:**
- `s` - String to process

**Returns:**
- String with first letter capitalized

**Example:**

```oraset
@string;

text = `hello oraset`;
result = string.capitalize(text);
show(`Capitalized: `, result);  !! Output: Hello oraset
```

#### string.title(s)

Capitalize the first letter of each word in a string.

**Parameters:**
- `s` - String to process

**Returns:**
- String with each word capitalized

**Example:**

```oraset
@string;

text = `hello oraset world`;
result = string.title(text);
show(`Title case: `, result);  !! Output: Hello Oraset World
```

## Example Code

```oraset
@string;

!! Basic operations
text = `Hello Oraset`;
show(`Original: `, text);
show(`Length: `, string.length(text));
show(`Upper case: `, string.upper(text));
show(`Lower case: `, string.lower(text));

!! String splitting
csv = `apple,banana,cherry`;
show(`CSV: `, csv);
show(`Split: `, string.split(csv, `,`));

!! Substring operations
show(`Substring: `, string.substring(text, 6));
show(`Index of 'Oraset': `, string.indexOf(text, `Oraset`));

!! Replacement and modification
show(`Replace: `, string.replace(text, `Oraset`, `World`));
show(`Trim: `, string.trim(`   Hello   `));
show(`Repeat: `, string.repeat(`Hi `, 3));
show(`Reverse: `, string.reverse(text));

!! Check operations
show(`Starts with 'Hello': `, string.startsWith(text, `Hello`));
show(`Ends with 'Oraset': `, string.endsWith(text, `Oraset`));
show(`Includes 'Oraset': `, string.includes(text, `Oraset`));

!! Formatting
show(`Capitalize: `, string.capitalize(`hello world`));
show(`Title case: `, string.title(`hello oraset world`));
```

## Notes

- All string operations return a new string instead of modifying the original
- String indices start from 0
- When the separator is an empty string, the string is split into an array of individual characters