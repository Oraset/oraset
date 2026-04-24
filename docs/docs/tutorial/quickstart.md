# 快速开始

本教程将帮助你快速上手 Oraset 编程语言，包括安装、编写第一个程序以及基本的使用方法。

## 安装 Oraset

### 从源码安装

1. **克隆或下载源码**
   - 访问 [GitHub 仓库](https://github.com/Oraset/oraset) 克隆或下载源码到本地
   - 解压到任意目录

2. **系统要求**
   - Python 3.6 或更高版本
   - 支持 Windows 和 Linux 操作系统

3. **运行 Oraset**
   - 进入 Oraset 目录
   - 直接运行 `oraset.py` 文件：
     ```bash
     python oraset.py
     ```

### 从二进制安装

1. **下载二进制文件**
   - 访问 [Oraset 官网](https://oraset.org) 下载对应平台的二进制文件
   - Windows 为 `.exe` 文件，Linux 为可执行文件

2. **安装**
   - 解压到任意目录
   - 将可执行文件所在目录添加到系统环境变量（可选）

3. **运行 Oraset**
   - 直接运行可执行文件：
     ```bash
     oraset
     ```

## 运行你的第一个程序

### 创建程序文件

创建一个名为 `hello.oraset` 的文件，内容如下：

```oraset
!! 这是一个注释
show(`Hello, Oraset!`);
```

### 运行程序

**使用源码运行**：

```bash
python oraset.py hello.oraset
```

**使用二进制文件运行**：

```bash
oraset hello.oraset
```

### 查看输出

你将看到输出：

```
Hello, Oraset!
```

## 基本语法示例

### 变量赋值

```oraset
!! 变量赋值
name = `World`;
age = 20;
pi = 3.14159;

show(`Name: `, name);
show(`Age: `, age);
show(`PI: `, pi);
```

### 数学表达式

```oraset
!! 数学表达式
a = 10;
b = 5;

show(`a + b = `, a + b);
show(`a - b = `, a - b);
show(`a * b = `, a * b);
show(`a / b = `, a / b);
show(`a % b = `, a % b);
```

### 条件语句

```oraset
!! 条件语句
age = 18;

if (age >= 18) {
    show(`Adult`);
} else {
    show(`Minor`);
}
```

### 循环语句

```oraset
!! 循环语句
count = 0;

while (count < 5) {
    show(`Count: `, count);
    count = count + 1;
}
```

### 函数定义

```oraset
!! 函数定义
def greet(name) {
    show(`Hello, `, name, `!`);
}

greet(`Oraset`);
```

### 数组操作

```oraset
!! 数组操作
fruits = arr(`apple`, `banana`, `cherry`);
show(`Fruits: `, fruits);
show(`First fruit: `, fruits[0]);
```

## 库的使用

### 导入库

```oraset
!! 导入数学库
@math;

!! 使用数学函数
show(`PI: `, math.pi());
show(`sin(90): `, math.sin(90));
```

## 打包程序

你可以将 Oraset 代码打包为加密的 `.osp` 文件：

```bash
python oraset.py pack hello.oraset
```

这将生成 `hello.osp` 文件，你可以直接运行它：

```bash
python oraset.py -osp hello.osp
```

## 常见问题

### 为什么我的程序没有输出？
- 确保你使用了 `show` 函数来输出内容
- 检查是否有语法错误

### 如何处理输入？
- Oraset 支持 `input` 函数来获取用户输入：
  ```oraset
  name = input(`What's your name? `);
  show(`Hello, `, name, `!`);
  ```

### 如何调试程序？
- 使用 `show` 函数打印变量值
- 检查错误信息，Oraset 会显示详细的错误位置和原因

## 下一步

- [基本语法教程](basic-syntax.md) - 学习 Oraset 的基本语法
- [控制结构教程](control-structures.md) - 学习条件语句和循环
- [函数和类教程](functions-and-classes.md) - 学习函数和类的使用
- [库参考](libraries/math.md) - 了解 Oraset 的内置库