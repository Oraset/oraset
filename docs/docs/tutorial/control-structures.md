# 控制结构

## 条件语句

### if 语句

`if` 语句用于根据条件执行不同的代码块：

```oraset
if (condition) {
    !! 条件为真时执行的代码
}
```

示例：

```oraset
age = 18;
if (age >= 18) {
    show(`You are an adult.`);
}
```

### if-else 语句

`if-else` 语句用于在条件为真时执行一个代码块，在条件为假时执行另一个代码块：

```oraset
if (condition) {
    !! 条件为真时执行的代码
} else {
    !! 条件为假时执行的代码
}
```

示例：

```oraset
age = 15;
if (age >= 18) {
    show(`You are an adult.`);
} else {
    show(`You are a minor.`);
}
```

### if-else if-else 语句

`if-else if-else` 语句用于处理多个条件：

```oraset
if (condition1) {
    !! 条件1为真时执行的代码
} else if (condition2) {
    !! 条件2为真时执行的代码
} else {
    !! 所有条件都为假时执行的代码
}
```

示例：

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

## 循环语句

### while 循环

`while` 循环在条件为真时重复执行代码块：

```oraset
while (condition) {
    !! 循环体代码
    !! 必须有使条件变为假的语句，否则会无限循环
}
```

示例：

```oraset
count = 1;
while (count <= 5) {
    show(`Count: `, count);
    count = count + 1;
}
```

### for 循环

`for` 循环用于遍历序列或执行固定次数的循环：

```oraset
for (variable in sequence) {
    !! 循环体代码
}
```

示例：

```oraset
fruits = arr(`apple`, `banana`, `cherry`);
for (fruit in fruits) {
    show(`Fruit: `, fruit);
}
```

### 循环控制

#### break 语句

`break` 语句用于跳出当前循环：

```oraset
count = 1;
while (count <= 10) {
    if (count == 5) {
        break; !! 跳出循环
    }
    show(`Count: `, count);
    count = count + 1;
}
```

#### continue 语句

`continue` 语句用于跳过当前循环的剩余部分，直接开始下一次循环：

```oraset
count = 1;
while (count <= 5) {
    if (count == 3) {
        count = count + 1;
        continue; !! 跳过当前循环的剩余部分
    }
    show(`Count: `, count);
    count = count + 1;
}
```

## 嵌套控制结构

控制结构可以嵌套使用：

```oraset
for (i in arr(1, 2, 3)) {
    if (i % 2 == 0) {
        show(`Even number: `, i);
    } else {
        show(`Odd number: `, i);
    }
}
```

## 三元运算符

Oraset 支持三元运算符，用于简洁地表达条件表达式：

```oraset
variable = condition ? value1 : value2;
```

示例：

```oraset
age = 18;
status = age >= 18 ? `adult` : `minor`;
show(`Status: `, status);
```

## 示例：猜数字游戏

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

## 注意事项

- 条件表达式必须用括号包围
- 代码块必须用大括号 `{}` 包围
- 确保循环有终止条件，避免无限循环
- 嵌套控制结构不要过深，保持代码可读性