# Control Structures

## Conditional Statements

### if Statement

The `if` statement is used to execute different code blocks based on conditions:

```oraset
if (condition) {
    !! Code to execute if condition is true
}
```

Example:

```oraset
age = 18;
if (age >= 18) {
    show(`You are an adult.`);
}
```

### if-else Statement

The `if-else` statement executes one code block if a condition is true and another if it's false:

```oraset
if (condition) {
    !! Code to execute if condition is true
} else {
    !! Code to execute if condition is false
}
```

Example:

```oraset
age = 15;
if (age >= 18) {
    show(`You are an adult.`);
} else {
    show(`You are a minor.`);
}
```

### if-else if-else Statement

The `if-else if-else` statement is used to handle multiple conditions:

```oraset
if (condition1) {
    !! Code to execute if condition1 is true
} else if (condition2) {
    !! Code to execute if condition2 is true
} else {
    !! Code to execute if all conditions are false
}
```

Example:

```oraset
score = 85;
if (score >= 90) {
    show(`Grade: A`);
} else if (score >= 80) {
    show(`Grade: B`);
} else if (score >= 70) {
    show(`Grade: C`);
} else if (score >= 60) {
    show(`Grade: D`);
} else {
    show(`Grade: F`);
}
```

## Loop Statements

### while Loop

The `while` loop repeats a code block as long as a condition is true:

```oraset
while (condition) {
    !! Loop body code
    !! Must have a statement that makes the condition false, otherwise it will loop infinitely
}
```

Example:

```oraset
count = 1;
while (count <= 5) {
    show(`Count: `, count);
    count = count + 1;
}
```

### for Loop

The `for` loop is used to iterate over sequences or execute a loop a fixed number of times:

```oraset
for (variable in sequence) {
    !! Loop body code
}
```

Example:

```oraset
fruits = arr(`apple`, `banana`, `cherry`);
for (fruit in fruits) {
    show(`Fruit: `, fruit);
}
```

### Loop Control

#### break Statement

The `break` statement is used to exit the current loop:

```oraset
count = 1;
while (count <= 10) {
    if (count == 5) {
        break; !! Exit the loop
    }
    show(`Count: `, count);
    count = count + 1;
}
```

#### continue Statement

The `continue` statement skips the remaining part of the current loop iteration and starts the next iteration:

```oraset
count = 1;
while (count <= 5) {
    if (count == 3) {
        count = count + 1;
        continue; !! Skip the rest of the loop body
    }
    show(`Count: `, count);
    count = count + 1;
}
```

## Nested Control Structures

Control structures can be nested:

```oraset
for (i in arr(1, 2, 3)) {
    if (i % 2 == 0) {
        show(`Even number: `, i);
    } else {
        show(`Odd number: `, i);
    }
}
```

## Ternary Operator

Oraset supports the ternary operator for concise conditional expressions:

```oraset
variable = condition ? value1 : value2;
```

Example:

```oraset
age = 18;
status = age >= 18 ? `adult` : `minor`;
show(`Status: `, status);
```

## Example: Number Guessing Game

```oraset
@math;

number = math.randint(1, 100);
guess = 0;
tries = 0;

show(`Guess a number between 1 and 100:`);

while (guess != number) {
    guess = input(`Enter your guess: `);
    guess = int(guess);
    tries = tries + 1;
    
    if (guess < number) {
        show(`Too low!`);
    } else if (guess > number) {
        show(`Too high!`);
    } else {
        show(`Congratulations! You guessed the number in `, tries, ` tries.`);
    }
}
```

## Notes

- Condition expressions must be enclosed in parentheses
- Code blocks must be enclosed in curly braces `{}`
- Ensure loops have termination conditions to avoid infinite loops
- Don't nest control structures too deeply, keep code readable