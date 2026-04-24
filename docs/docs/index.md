# Oraset 编程语言

## 什么是 Oraset？

Oraset 是一种简单、强大、跨平台的编程语言，设计初衷是提供一种易于学习和使用的编程工具。

### 主要特性

- **简单直观的语法**：清晰的语法设计，易于学习和使用
- **跨平台支持**：可在 Windows 和 Linux 等多个平台运行
- **丰富的库函数**：内置数学、字符串、数组等多种实用库
- **文件打包功能**：支持将代码打包为加密的 .osp 文件
- **网络请求能力**：内置 HTTP 请求功能，轻松与网络服务交互
- **扩展性**：支持通过 includes 目录添加自定义扩展

## 快速开始

### 安装

1. 下载 Oraset 解释器
2. 解压到任意目录
3. 将 Oraset 所在目录添加到系统环境变量（可选）

### 第一个程序

创建一个名为 `hello.oraset` 的文件，内容如下：

```oraset
!! 第一个 Oraset 程序
show(`Hello, Oraset!`);
```

运行程序：

```bash
python oraset.py hello.oraset
```

## 文档导航

- [入门教程](tutorial/quickstart.md) - 学习 Oraset 的基本语法和使用方法
- [语法参考](reference/syntax.md) - 详细的语法规则
- [库函数参考](libraries/math.md) - 内置库函数的使用方法
- [高级特性](advanced/packaging.md) - 高级功能和最佳实践
- [关于项目](about/introduction.md) - 项目介绍和贡献指南

## 社区

- [GitHub 仓库](https://github.com/oraset/oraset) - 源码和贡献
- [论坛](https://bbs.ecuil.com) - 讨论和帮助
- [问题追踪](https://github.com/oraset/oraset/issues) - 报告问题

## 许可证

Oraset 使用 GNU 通用公共许可证 v3.0。