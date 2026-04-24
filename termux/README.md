# Oraset 编程语言

Oraset是一种简单的跨平台编程语言，使用Python实现，支持Windows和Linux系统。

## 特性

- 跨平台运行（Windows和Linux）
- 简洁易懂的语法
- 支持变量定义和赋值
- 支持表达式计算（算术、比较、逻辑）
- 支持条件语句（if、else if、else）
- 支持循环语句（while）
- 支持函数定义和调用
- 支持类定义
- 支持输出功能
- 支持注释

## 快速开始

### 运行环境

- Python 3.6+

### 运行方式

```bash
# 运行.oas或.oraset文件
python oraset.py <filename.oas|.oraset>

# 将.oas或.oraset文件打包成.osp文件
python oraset.py pack <filename.oas|.oraset>

# 运行.osp文件
python oraset.py -osp <filename.osp>
```

### 示例

创建一个名为`hello.oas`的文件，内容如下：

```oraset
!! 输出Hello, Oraset!
show(`Hello, Oraset!`);

!! 变量定义和计算
x = 10;
y = 20;
sum = x + y;
show(`10 + 20 = `, sum);

!! 条件语句
if (sum > 25) {
    show(`Sum is greater than 25`);
} else {
    show(`Sum is less than or equal to 25`);
}

!! 循环语句
i = 0;
while (i < 5) {
    show(`i = `, i);
    i = i + 1;
}

!! 函数定义
def add(a, b) {
    return a + b;
}

!! 函数调用
result = add(5, 6);
show(`5 + 6 = `, result);

!! 类定义
class Calculator {
    def multiply(a, b) {
        return a * b;
    }
}
```

运行：

```bash
python oraset.py hello.oas
```

## 语法指南

### 注释

使用`!!`开始单行注释：

```oraset
!! 这是一个注释
```

使用`!*`和`*!`包围多行注释：

```oraset
!* 这是一个
多行注释 *!
```

### 内置库函数

Oraset提供了以下内置库函数：

#### 数学函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `abs(x)` | 返回x的绝对值 | `abs(-10)` → `10` |
| `max(x, y)` | 返回x和y中的最大值 | `max(10, 20)` → `20` |
| `min(x, y)` | 返回x和y中的最小值 | `min(10, 20)` → `10` |
| `pow(x, y)` | 返回x的y次方 | `pow(2, 3)` → `8` |
| `sqrt(x)` | 返回x的平方根（取整数部分） | `sqrt(16)` → `4` |

#### 字符串函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `len(s)` | 返回字符串s的长度 | `len("Hello")` → `5` |
| `upper(s)` | 将字符串s转换为大写 | `upper("Hello")` → `HELLO` |
| `lower(s)` | 将字符串s转换为小写 | `lower("HELLO")` → `hello` |
| `substring(s, start, end)` | 返回字符串s从start到end的子串 | `substring("Hello", 0, 3)` → `Hel` |
| `startsWith(s, prefix)` | 检查字符串s是否以prefix开头 | `startsWith("Hello", "He")` → `1` |
| `endsWith(s, suffix)` | 检查字符串s是否以suffix结尾 | `endsWith("Hello", "lo")` → `1` |
| `replace(s, old, new)` | 替换字符串s中的old为new | `replace("Hello", "He", "Hi")` → `Hiello` |
| `split(s, sep)` | 以sep为分隔符分割字符串s | `split("a,b,c", ",")` → `["a", "b", "c"]` |
| `trim(s)` | 去除字符串s首尾的空白 | `trim("  Hello  ")` → `Hello` |

#### 数组函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `array(...items)` | 创建一个包含指定元素的数组 | `array("a", "b", "c")` → `["a", "b", "c"]` |
| `push(arr, item)` | 向数组arr添加一个元素 | `push(["a", "b"], "c")` → `["a", "b", "c"]` |
| `pop(arr)` | 从数组arr中移除最后一个元素 | `pop(["a", "b", "c"])` → `["a", "b"]` |
| `indexOf(arr, item)` | 返回元素item在数组arr中的索引，若不存在则返回-1 | `indexOf(["a", "b", "c"], "b")` → `1` |

#### 类型检查函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `is_number(x)` | 检查x是否为数字 | `is_number("123")` → `1` |
| `is_string(x)` | 检查x是否为字符串 | `is_string("Hello")` → `1` |

#### 其他函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `input(prompt)` | 从用户输入获取值 | `input("请输入: ")` |
| `int(s)` | 将字符串s转换为整数 | `int("123")` → `123` |
| `str(x)` | 将x转换为字符串 | `str(123)` → `"123"` |

#### 文件操作函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `file_read(filename)` | 读取文件内容 | `file_read("test.txt")` |
| `file_write(filename, content)` | 写入内容到文件 | `file_write("test.txt", "Hello")` |
| `file_exists(filename)` | 检查文件是否存在 | `file_exists("test.txt")` → `1` (存在) 或 `0` (不存在) |

#### 时间函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `time_now()` | 获取当前时间戳 | `time_now()` |
| `time_sleep(seconds)` | 暂停指定秒数 | `time_sleep(2)` |

#### 随机数函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `random_int(min, max)` | 生成指定范围内的随机整数 | `random_int(1, 100)` |
| `random_float()` | 生成0-1之间的随机浮点数 | `random_float()` |

#### 系统函数

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `system(command)` | 执行系统命令 | `system("dir")` |
| `get_env(var_name)` | 获取环境变量 | `get_env("PATH")` |



### 数学模块

**注意：使用数学函数需要先导入math模块**

```oraset
import math
```

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `abs(x)` | 返回x的绝对值 | `abs(-10)` → `10.0` |
| `max(x, y)` | 返回x和y中的最大值 | `max(10, 20)` → `20.0` |
| `min(x, y)` | 返回x和y中的最小值 | `min(10, 20)` → `10.0` |
| `pow(x, y)` | 返回x的y次方 | `pow(2, 3)` → `8.0` |
| `sqrt(x)` | 返回x的平方根 | `sqrt(16)` → `4.0` |
| `sin(x)` | 返回x（度）的正弦值 | `sin(90)` → `1.0` |
| `cos(x)` | 返回x（度）的余弦值 | `cos(0)` → `1.0` |
| `tan(x)` | 返回x（度）的正切值 | `tan(45)` → `1.0` |
| `asin(x)` | 返回x的反正弦值（度） | `asin(1)` → `90.0` |
| `acos(x)` | 返回x的反余弦值（度） | `acos(1)` → `0.0` |
| `atan(x)` | 返回x的反正切值（度） | `atan(1)` → `45.0` |
| `pi()` | 返回圆周率π的值 | `pi()` → `3.141592653589793` |
| `e()` | 返回自然常数e的值 | `e()` → `2.718281828459045` |

#### 网络请求函数

**注意：使用网络请求函数需要先导入http模块**

```oraset
import http
```

| 函数名 | 描述 | 示例 |
|-------|------|------|
| `http_get(url)` | 发送HTTP GET请求并返回响应内容 | `http_get("http://example.com")` |
| `http_post(url, data)` | 发送HTTP POST请求并返回响应内容 | `http_post("http://httpbin.org/post", "{\"name\": \"Oraset\", \"version\": \"1.0\"}")` |

### 插件系统

Oraset支持用户自定义插件，您可以将自己的扩展功能放在`includes`文件夹中。

#### 创建插件

1. 在`includes`文件夹中创建一个以`.oraset`为后缀的文件
2. 在文件中定义函数、类等
3. 使用`import 插件名`指令加载插件

#### 示例

创建`includes/math_utils.oraset`文件：

```oraset
!! 数学工具插件

def add(a, b) {
    return a + b;
}

def subtract(a, b) {
    return a - b;
}
```

在您的代码中使用：

```oraset
import math_utils

result = add(10, 20);
show(`10 + 20 = `, result);
```

### 变量

变量定义和赋值：

```oraset
x = 10;  // 整数
message = `Hello`;  // 字符串
```

### 数据类型

- 整数：`10`, `20`, `30`
- 字符串：`` `Hello` ``, `` `World` ``

字符串支持以下转义符：

| 转义符 | 描述 |
|-------|------|
| `\n` | 换行符 |
| `\t` | 制表符 |
| `\r` | 回车符 |
| `\\` | 反斜杠 |
| `` \` `` | 反引号 |

示例：

```oraset
// 输出多行文本
show(`Line 1\nLine 2`);

// 输出带制表符的文本
show(`Column 1\tColumn 2`);

// 输出包含反斜杠的文本
show(`Path: C:\\Users\\Name`);
```

### 运算符

#### 算术运算符

- `+`：加法
- `-`：减法
- `*`：乘法
- `/`：除法（整数除法）

#### 比较运算符

- `==`：等于
- `!=`：不等于
- `<`：小于
- `<=`：小于等于
- `>`：大于
- `>=`：大于等于

#### 逻辑运算符

- `&&`：逻辑与
- `||`：逻辑或

#### 赋值运算符

- `=`：赋值
- `+=`：加赋值
- `-=`：减赋值
- `*=`：乘赋值
- `/=`：除赋值

### 条件语句

```oraset
if (condition) {
    // 代码块
} else if (condition) {
    // 代码块
} else {
    // 代码块
}
```

### 循环语句

```oraset
while (condition) {
    // 代码块
}
```

### 函数定义

```oraset
def function_name(parameter1, parameter2, ...) {
    // 代码块
    return value;
}
```

### 函数调用

```oraset
result = function_name(arg1, arg2, ...);
```

### 类定义

```oraset
class ClassName {
    def method_name(parameter1, parameter2, ...) {
        // 代码块
        return value;
    }
}
```

### 输出

使用`show`函数输出内容：

```oraset
show(`Hello`);
show(`The value is `, x);
```

## 示例代码

### 基础示例

```oraset
// 变量和表达式
x = 10;
y = 20;
sum = x + y;
show(`Sum: `, sum);

// 条件语句
if (sum > 25) {
    show(`Sum is greater than 25`);
} else if (sum == 25) {
    show(`Sum is exactly 25`);
} else {
    show(`Sum is less than 25`);
}

// 循环语句
i = 0;
while (i < 5) {
    show(`i = `, i);
    i += 1;
}
```

### 函数示例

```oraset
// 函数定义
def add(a, b) {
    return a + b;
}

def multiply(a, b) {
    return a * b;
}

// 函数调用
result1 = add(10, 20);
result2 = multiply(5, 6);
show(`10 + 20 = `, result1);
show(`5 * 6 = `, result2);

// 递归函数
def factorial(n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

result = factorial(5);
show(`Factorial of 5 is `, result);
```

### 类示例

```oraset
// 类定义
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

// 注意：类方法的调用需要通过函数实现
// 目前版本中，类定义会被存储但不会直接实例化
```

## 项目结构

```
Oraset/
├── oraset.py          # 核心解释器
├── examples/          # 示例代码
│   ├── hello.oas      # 基础示例
│   ├── hello.osp      # 打包后的基础示例
│   ├── functions.oas  # 函数示例
│   └── classes.oas    # 类示例
├── README.md          # 本教程（中文）
└── README.en_us.md    # 本教程（英文）
```

## .osp文件说明

.osp文件是Oraset的打包文件格式，它是通过对.oas文件进行压缩和编码生成的，具有以下特点：

- **加密性**：.osp文件使用base64编码和zlib压缩，使得源代码不易被直接查看
- **跨平台**：.osp文件可以在Windows和Linux系统上直接运行
- **便捷性**：.osp文件是一个独立的文件，可以方便地分发和使用

### 打包.oas文件

使用`pack`命令将.oas文件打包成.osp文件：

```bash
python oraset.py pack <filename.oas>
```

这将生成一个与.oas文件同名但扩展名为.osp的文件。

### 运行.osp文件

使用`-osp`参数运行.osp文件：

```bash
python oraset.py -osp <filename.osp>
```

这将自动解压和执行.osp文件中的代码。

## 开发说明

Oraset使用Python实现，主要包含以下组件：

- **Lexer**：词法分析器，负责将源代码转换为词法单元
- **Parser**：语法分析器，负责构建抽象语法树（AST）
- **Interpreter**：解释器，负责执行AST并生成结果

## 未来计划

- 支持更多数据类型（浮点数、布尔值等）
- 完善类的实例化和方法调用
- 支持模块导入
- 添加标准库
- 优化性能

## 许可证

GNU General Public License v3.0
