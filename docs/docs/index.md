# Oraset 编程语言

## 什么是 Oraset？

Oraset 是一种简单、强大、跨平台的编程语言，设计目标是提供一种易于学习和使用的编程工具。它具有以下特点：

- **简单易学**：语法简洁明了，适合初学者
- **跨平台**：支持 Windows 和 Linux 操作系统
- **强大功能**：支持变量、表达式、条件语句、循环、函数、类等核心功能
- **内置库**：提供数学、字符串、数组、工具等实用库
- **文件打包**：支持将代码打包为加密的 .osp 二进制文件

## 快速开始

### 安装 Oraset

1. 克隆或下载 Oraset 源码到本地
2. 确保你的系统已安装 Python 3.6 或更高版本
3. 进入 Oraset 目录，直接运行 `oraset.py` 文件

### 运行你的第一个程序

创建一个名为 `hello.oraset` 的文件，内容如下：

```oraset
show(`Hello, Oraset!`);
```

然后运行：

```bash
python oraset.py hello.oraset
```

你将看到输出：

```
Hello, Oraset!
```

## 核心特性

### 语法特点
- 使用反引号 `` ` `` 表示字符串
- 使用 `show` 代替 `print` 进行输出
- 使用 `@` 导入库
- 支持分号作为语句结束符

### 基本数据类型
- 数字（整数和浮点数）
- 字符串
- 数组
- 布尔值

### 控制结构
- 条件语句：`if`、`else`、`else if`
- 循环语句：`while`

### 函数和类
- 函数定义：`def function_name(params) { ... }`
- 类定义：`class ClassName { ... }`

### 内置库
- `@math` - 数学库
- `@string` - 字符串库
- `@array` - 数组库
- `@util` - 工具库

## 学习资源

- **快速开始**：[快速开始教程](tutorial/quickstart.md)
- **基本语法**：[基本语法教程](tutorial/basic-syntax.md)
- **控制结构**：[控制结构教程](tutorial/control-structures.md)
- **函数和类**：[函数和类教程](tutorial/functions-and-classes.md)
- **库参考**：[库参考文档](libraries/math.md)

## 社区

- [GitHub 仓库](https://github.com/Oraset/oraset) - 源代码和贡献
- [论坛](https://bbs.ecuil.com) - 讨论和帮助
- [Issue 追踪](https://github.com/Oraset/oraset/issues) - 报告问题

## 许可证

Oraset 使用 GNU 通用公共许可证 v3.0。