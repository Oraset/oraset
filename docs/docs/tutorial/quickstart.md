# 快速开始

## 安装 Oraset

### 从源码安装

1. 克隆或下载 Oraset 源码到本地
2. 确保你的系统已安装 Python 3.6 或更高版本
3. 进入 Oraset 目录，直接运行 `oraset.py` 文件

### 从二进制安装

1. 下载对应平台的二进制文件（Windows 为 .exe 文件，Linux 为可执行文件）
2. 解压到任意目录
3. 将可执行文件所在目录添加到系统环境变量（可选）

## 运行你的第一个程序

### 创建程序文件

创建一个名为 `hello.oraset` 的文件，内容如下：

```oraset
!! 这是一个注释
show(`Hello, Oraset!`);
```

### 运行程序

#### 使用 Python 运行

```bash
python oraset.py hello.oraset
```

#### 使用二进制文件运行

```bash
# Windows
oraset.exe hello.oraset

# Linux
./oraset hello.oraset
```

### 运行结果

程序运行后，你应该会看到如下输出：

```
Hello, Oraset!
```

## 基本语法示例

### 变量赋值

```oraset
name = `John`;
age = 25;
price = 9.99;
```

### 输出

```oraset
show(`Name: `, name);
show(`Age: `, age);
show(`Price: `, price);
```

### 简单计算

```oraset
num1 = 10;
num2 = 20;
sum = num1 + num2;
show(`Sum: `, sum);
```

## 下一步

- 学习 [基本语法](basic-syntax.md) 了解更多语法规则
- 了解 [数据类型](data-types.md) 的使用
- 学习 [控制结构](control-structures.md) 如条件语句和循环
- 探索 [函数](functions.md) 的定义和使用

## 常见问题

### 程序运行时没有输出

- 检查是否使用了 `show` 函数
- 确保文件路径正确
- 检查是否有语法错误

### 语法错误

- 检查括号是否匹配
- 确保字符串使用反引号包围
- 检查变量名是否正确

### 找不到命令

- 确保 Oraset 所在目录已添加到环境变量
- 或使用绝对路径运行

## 示例代码

### 计算阶乘

```oraset
def factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

show(`5! = `, factorial(5));
```

### 数组操作

```oraset
fruits = arr(`apple`, `banana`, `cherry`);
show(`Fruits: `, fruits);
show(`First fruit: `, fruits[0]);
```