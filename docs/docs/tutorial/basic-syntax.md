# 基本语法

本教程将详细介绍 Oraset 编程语言的基本语法，包括变量、数据类型、运算符、表达式等内容。

## 注释

Oraset 使用两种注释方式：

- **单行注释**：使用 `!!` 开始
- **多行注释**：使用 `!*` 开始，`*!` 结束

```oraset
!! 这是一个单行注释

!* 这是一个
多行注释 *!
```

## 变量

### 变量声明与赋值

Oraset 使用 `=` 进行变量赋值，不需要显式声明变量类型：

```oraset
!! 变量赋值
name = `World`;  !! 字符串
age = 20;        !! 整数
pi = 3.14159;    !! 浮点数
is_valid = true; !! 布尔值
```

### 变量命名规则

- 变量名只能包含字母、数字和下划线
- 变量名不能以数字开头
- 变量名区分大小写
- 变量名不能使用关键字（如 `if`、`else`、`while`、`def`、`class` 等）

### 变量作用域

- **全局变量**：在函数外部定义的变量
- **局部变量**：在函数内部定义的变量

```oraset
!! 全局变量
global_var = `Global`;

def test() {
    !! 局部变量
    local_var = `Local`;
    show(global_var);  !! 可以访问全局变量
    show(local_var);   !! 可以访问局部变量
}

test();
show(global_var);  !! 可以访问全局变量
!! show(local_var);  !! 错误：无法访问局部变量
```

## 数据类型

### 数字

Oraset 支持整数和浮点数：

```oraset
!! 整数
integer = 123;
negative = -456;

!! 浮点数
float = 3.14;
scientific = 1.23e4;  !! 12300
```

### 字符串

Oraset 使用反引号 `` ` `` 表示字符串：

```oraset
!! 字符串
str1 = `Hello`;
str2 = `World`;

!! 字符串拼接
combined = str1 + ` ` + str2;
show(combined);  !! 输出: Hello World
```

### 数组

Oraset 使用 `arr()` 函数创建数组：

```oraset
!! 数组
empty = arr();
numbers = arr(1, 2, 3, 4, 5);
fruits = arr(`apple`, `banana`, `cherry`);
mixed = arr(1, `hello`, 3.14);

!! 访问数组元素
show(numbers[0]);  !! 输出: 1
show(fruits[1]);   !! 输出: banana
```

### 布尔值

Oraset 支持布尔值 `true` 和 `false`：

```oraset
!! 布尔值
true_value = true;
false_value = false;

!! 布尔表达式
is_greater = 5 > 3;  !! true
is_equal = 5 == 3;   !! false
```

## 运算符

### 算术运算符

| 运算符 | 描述 | 示例 |
|-------|------|------|
| `+` | 加法 | `a + b` |
| `-` | 减法 | `a - b` |
| `*` | 乘法 | `a * b` |
| `/` | 除法 | `a / b` |
| `%` | 取模 | `a % b` |
| `**` | 幂运算 | `a ** b` |

```oraset
!! 算术运算符
a = 10;
b = 3;

show(`a + b = `, a + b);  !! 13
show(`a - b = `, a - b);  !! 7
show(`a * b = `, a * b);  !! 30
show(`a / b = `, a / b);  !! 3.3333333333333335
show(`a % b = `, a % b);  !! 1
show(`a ** b = `, a ** b); !! 1000
```

### 比较运算符

| 运算符 | 描述 | 示例 |
|-------|------|------|
| `==` | 等于 | `a == b` |
| `!=` | 不等于 | `a != b` |
| `<` | 小于 | `a < b` |
| `>` | 大于 | `a > b` |
| `<=` | 小于等于 | `a <= b` |
| `>=` | 大于等于 | `a >= b` |

```oraset
!! 比较运算符
a = 5;
b = 10;

show(`a == b: `, a == b);  !! false
show(`a != b: `, a != b);  !! true
show(`a < b: `, a < b);    !! true
show(`a > b: `, a > b);    !! false
show(`a <= b: `, a <= b);  !! true
show(`a >= b: `, a >= b);  !! false
```

### 逻辑运算符

| 运算符 | 描述 | 示例 |
|-------|------|------|
| `&&` | 逻辑与 | `a && b` |
| `||` | 逻辑或 | `a || b` |
| `!` | 逻辑非 | `!a` |

```oraset
!! 逻辑运算符
t = true;
f = false;

show(`t && f: `, t && f);  !! false
show(`t || f: `, t || f);  !! true
show(`!t: `, !t);          !! false
show(`!f: `, !f);          !! true
```

### 赋值运算符

| 运算符 | 描述 | 示例 |
|-------|------|------|
| `=` | 简单赋值 | `a = b` |
| `+=` | 加赋值 | `a += b` |
| `-=` | 减赋值 | `a -= b` |
| `*=` | 乘赋值 | `a *= b` |
| `/=` | 除赋值 | `a /= b` |
| `%=` | 取模赋值 | `a %= b` |

```oraset
!! 赋值运算符
a = 10;
show(`Initial a: `, a);  !! 10

a += 5;
show(`a += 5: `, a);     !! 15

a -= 3;
show(`a -= 3: `, a);     !! 12

a *= 2;
show(`a *= 2: `, a);     !! 24

a /= 4;
show(`a /= 4: `, a);     !! 6

a %= 5;
show(`a %= 5: `, a);     !! 1
```

## 表达式

表达式是由变量、常量、运算符和函数调用组成的组合，用于计算值：

```oraset
!! 表达式
result = (10 + 5) * 2 / 3;
show(`Result: `, result);  !! 10.0

!! 复杂表达式
a = 10;
b = 5;
c = 3;
result = (a + b) * c - (a / b);
show(`Result: `, result);  !! 45.0
```

## 输入输出

### 输出

使用 `show` 函数输出内容：

```oraset
!! 输出
show(`Hello, World!`);
show(`The answer is: `, 42);
show(`Pi is approximately: `, 3.14159);
```

### 输入

使用 `input` 函数获取用户输入：

```oraset
!! 输入
name = input(`What's your name? `);
age = input(`How old are you? `);
show(`Hello, `, name, `! You are `, age, ` years old.`);
```

## 转义字符

Oraset 支持以下转义字符：

| 转义字符 | 描述 |
|---------|------|
| `\n` | 换行 |
| `\t` | 制表符 |
| `\r` | 回车 |
| `\` | 反斜杠 |
| `` \` `` | 反引号 |

```oraset
!! 转义字符
show(`Line 1\nLine 2`);
show(`Name:\tJohn`);
show(`Path: C:\\folder\\file.txt`);
show(`He said: \`Hello!\``);
```

## 示例代码

```oraset
!! 基本语法示例

!! 变量赋值
name = `Oraset`;
age = 20;
pi = 3.14159;

!! 算术运算
radius = 5;
area = pi * radius ** 2;
show(`Area of circle: `, area);

!! 字符串操作
greeting = `Hello, ` + name + `!`;
show(greeting);

!! 数组操作
numbers = arr(1, 2, 3, 4, 5);
sum = 0;
i = 0;

while (i < 5) {
    sum = sum + numbers[i];
    i = i + 1;
}

show(`Sum of numbers: `, sum);

!! 输入输出
user_name = input(`What's your name? `);
show(`Nice to meet you, `, user_name, `!`);
```

## 小结

本教程介绍了 Oraset 编程语言的基本语法，包括：

- 注释的使用
- 变量的声明和赋值
- 数据类型（数字、字符串、数组、布尔值）
- 各种运算符（算术、比较、逻辑、赋值）
- 表达式的使用
- 输入输出操作
- 转义字符

这些是 Oraset 编程的基础，掌握这些内容后，你可以开始编写更复杂的程序。