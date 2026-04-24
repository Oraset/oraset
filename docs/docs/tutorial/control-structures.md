# 控制结构

本教程将详细介绍 Oraset 编程语言的控制结构，包括条件语句和循环语句，帮助你掌握程序的流程控制。

## 条件语句

### if 语句

`if` 语句用于根据条件执行不同的代码块：

```oraset
!! if 语句
age = 18;

if (age >= 18) {
    show(`You are an adult.`);
}
```

### if-else 语句

`if-else` 语句用于在条件为真和为假时执行不同的代码块：

```oraset
!! if-else 语句
age = 16;

if (age >= 18) {
    show(`You are an adult.`);
} else {
    show(`You are a minor.`);
}
```

### if-else if-else 语句

`if-else if-else` 语句用于处理多个条件：

```oraset
!! if-else if-else 语句
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

### 嵌套条件语句

条件语句可以嵌套使用：

```oraset
!! 嵌套条件语句
age = 20;
has_license = true;

if (age >= 18) {
    if (has_license) {
        show(`You can drive.`);
    } else {
        show(`You need a driver's license to drive.`);
    }
} else {
    show(`You are too young to drive.`);
}
```

## 循环语句

### while 循环

`while` 循环用于重复执行代码块，直到条件为假：

```oraset
!! while 循环
count = 0;

while (count < 5) {
    show(`Count: `, count);
    count = count + 1;
}
```

### 无限循环

你可以创建无限循环，但需要注意在适当的时候使用 `break` 语句退出循环：

```oraset
!! 无限循环
i = 0;

while (true) {
    show(`Iteration: `, i);
    i = i + 1;
    
    if (i >= 5) {
        break;  !! 退出循环
    }
}
```

### 循环控制

#### break 语句

`break` 语句用于立即退出循环：

```oraset
!! break 语句
count = 0;

while (count < 10) {
    show(`Count: `, count);
    
    if (count == 5) {
        show(`Breaking the loop.`);
        break;
    }
    
    count = count + 1;
}
```

#### continue 语句

`continue` 语句用于跳过当前循环的剩余部分，直接进入下一次循环：

```oraset
!! continue 语句
count = 0;

while (count < 5) {
    count = count + 1;
    
    if (count == 3) {
        show(`Skipping count: `, count);
        continue;
    }
    
    show(`Count: `, count);
}
```

## 综合示例

### 猜数字游戏

```oraset
!! 猜数字游戏
@math;

secret_number = math.randint(1, 100);
guess = 0;
tries = 0;

show(`I'm thinking of a number between 1 and 100.`);
show(`Can you guess what it is?`);

while (guess != secret_number) {
    guess = input(`Enter your guess: `);
    guess = util.toNumber(guess);
    tries = tries + 1;
    
    if (guess < secret_number) {
        show(`Too low!`);
    } else if (guess > secret_number) {
        show(`Too high!`);
    } else {
        show(`Congratulations! You guessed the number in `, tries, ` tries.`);
    }
}
```

### 计算斐波那契数列

```oraset
!! 计算斐波那契数列
n = 10;
a = 0;
b = 1;
i = 0;

show(`Fibonacci sequence up to `, n, ` terms:`);

while (i < n) {
    show(a);
    next = a + b;
    a = b;
    b = next;
    i = i + 1;
}
```

### 素数判断

```oraset
!! 素数判断
number = input(`Enter a number: `);
number = util.toNumber(number);
is_prime = true;

if (number <= 1) {
    is_prime = false;
} else {
    i = 2;
    while (i * i <= number) {
        if (number % i == 0) {
            is_prime = false;
            break;
        }
        i = i + 1;
    }
}

if (is_prime) {
    show(number, ` is a prime number.`);
} else {
    show(number, ` is not a prime number.`);
}
```

## 注意事项

1. **括号使用**：条件语句和循环语句的条件必须用括号 `()` 包围
2. **代码块**：代码块必须用大括号 `{}` 包围
3. **缩进**：虽然缩进不是强制的，但良好的缩进可以提高代码可读性
4. **分号**：语句结束时使用分号 `;`
5. **条件表达式**：条件表达式必须返回布尔值

## 练习

1. 编写一个程序，输入一个年份，判断是否为闰年
2. 编写一个程序，计算 1 到 100 的和
3. 编写一个程序，打印乘法表（1-9）
4. 编写一个程序，输入一个字符串，判断是否为回文

## 小结

本教程介绍了 Oraset 编程语言的控制结构，包括：

- 条件语句：`if`、`else if`、`else`
- 循环语句：`while`
- 循环控制：`break`、`continue`
- 综合示例：猜数字游戏、斐波那契数列、素数判断

这些控制结构是编写复杂程序的基础，掌握它们后，你可以编写更灵活、更强大的 Oraset 程序。