# 字符串库

## 简介

字符串库（`@string`）提供了一系列字符串操作函数，包括字符串分割、大小写转换、查找替换等功能。

## 导入方式

```oraset
@string;
```

## 函数参考

### 字符串分割与连接

#### string.split(s, sep)

分割字符串。

**参数：**
- `s` - 字符串
- `sep` - 分隔符

**返回值：**
- 分割后的数组

**示例：**

```oraset
@string;

text = `Hello,World,Oraset`;
result = string.split(text, `,`);
show(`Split result: `, result);  !! 输出: ["Hello", "World", "Oraset"]
```

#### string.join(arr, sep)

连接数组元素为字符串。

**参数：**
- `arr` - 数组
- `sep` - 分隔符

**返回值：**
- 连接后的字符串

**示例：**

```oraset
@string;

arr = arr(`Hello`, `World`, `Oraset`);
result = string.join(arr, ` `);
show(`Joined result: `, result);  !! 输出: Hello World Oraset
```

### 大小写转换

#### string.upper(s)

转换为大写。

**参数：**
- `s` - 字符串

**返回值：**
- 大写字符串

**示例：**

```oraset
@string;

text = `hello world`;
result = string.upper(text);
show(`Upper case: `, result);  !! 输出: HELLO WORLD
```

#### string.lower(s)

转换为小写。

**参数：**
- `s` - 字符串

**返回值：**
- 小写字符串

**示例：**

```oraset
@string;

text = `HELLO WORLD`;
result = string.lower(text);
show(`Lower case: `, result);  !! 输出: hello world
```

#### string.capitalize(s)

首字母大写。

**参数：**
- `s` - 字符串

**返回值：**
- 首字母大写的字符串

**示例：**

```oraset
@string;

text = `hello world`;
result = string.capitalize(text);
show(`Capitalized: `, result);  !! 输出: Hello world
```

### 字符串长度与提取

#### string.length(s)

获取字符串长度。

**参数：**
- `s` - 字符串

**返回值：**
- 字符串长度

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result = string.length(text);
show(`Length: `, result);  !! 输出: 13
```

#### string.substring(s, start, end)

提取子字符串。

**参数：**
- `s` - 字符串
- `start` - 起始索引
- `end` - 结束索引（可选）

**返回值：**
- 提取的子字符串

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result1 = string.substring(text, 7);
result2 = string.substring(text, 0, 5);
show(`Substring from 7: `, result1);  !! 输出: Oraset!
show(`Substring from 0 to 5: `, result2);  !! 输出: Hello
```

#### string.charAt(s, index)

获取指定位置的字符。

**参数：**
- `s` - 字符串
- `index` - 索引

**返回值：**
- 指定位置的字符

**示例：**

```oraset
@string;

text = `Hello`;
result = string.charAt(text, 0);
show(`First character: `, result);  !! 输出: H
```

### 字符串查找

#### string.indexOf(s, substr)

查找子字符串的位置。

**参数：**
- `s` - 字符串
- `substr` - 子字符串

**返回值：**
- 子字符串的起始位置，未找到返回 -1

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result1 = string.indexOf(text, `Oraset`);
result2 = string.indexOf(text, `World`);
show(`Index of 'Oraset': `, result1);  !! 输出: 7
show(`Index of 'World': `, result2);  !! 输出: -1
```

#### string.lastIndexOf(s, substr)

从末尾开始查找子字符串的位置。

**参数：**
- `s` - 字符串
- `substr` - 子字符串

**返回值：**
- 子字符串的起始位置，未找到返回 -1

**示例：**

```oraset
@string;

text = `Hello, Oraset, Oraset!`;
result = string.lastIndexOf(text, `Oraset`);
show(`Last index of 'Oraset': `, result);  !! 输出: 14
```

#### string.includes(s, substr)

检查字符串是否包含子字符串。

**参数：**
- `s` - 字符串
- `substr` - 子字符串

**返回值：**
- 布尔值，表示是否包含子字符串

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result1 = string.includes(text, `Oraset`);
result2 = string.includes(text, `World`);
show(`Includes 'Oraset': `, result1);  !! 输出: true
show(`Includes 'World': `, result2);  !! 输出: false
```

### 字符串替换

#### string.replace(s, old, new)

替换子字符串。

**参数：**
- `s` - 字符串
- `old` - 要替换的子字符串
- `new` - 替换后的子字符串

**返回值：**
- 替换后的字符串

**示例：**

```oraset
@string;

text = `Hello, World!`;
result = string.replace(text, `World`, `Oraset`);
show(`Replaced: `, result);  !! 输出: Hello, Oraset!
```

#### string.replaceAll(s, old, new)

替换所有匹配的子字符串。

**参数：**
- `s` - 字符串
- `old` - 要替换的子字符串
- `new` - 替换后的子字符串

**返回值：**
- 替换后的字符串

**示例：**

```oraset
@string;

text = `Hello, World! Hello, World!`;
result = string.replaceAll(text, `World`, `Oraset`);
show(`Replaced all: `, result);  !! 输出: Hello, Oraset! Hello, Oraset!
```

### 字符串修剪

#### string.trim(s)

移除字符串两端的空白字符。

**参数：**
- `s` - 字符串

**返回值：**
- 修剪后的字符串

**示例：**

```oraset
@string;

text = `   Hello, Oraset!   `;
result = string.trim(text);
show(`Trimmed: `, result);  !! 输出: Hello, Oraset!
```

#### string.trimStart(s)

移除字符串开头的空白字符。

**参数：**
- `s` - 字符串

**返回值：**
- 修剪后的字符串

**示例：**

```oraset
@string;

text = `   Hello, Oraset!`;
result = string.trimStart(text);
show(`Trimmed start: `, result);  !! 输出: Hello, Oraset!
```

#### string.trimEnd(s)

移除字符串末尾的空白字符。

**参数：**
- `s` - 字符串

**返回值：**
- 修剪后的字符串

**示例：**

```oraset
@string;

text = `Hello, Oraset!   `;
result = string.trimEnd(text);
show(`Trimmed end: `, result);  !! 输出: Hello, Oraset!
```

### 字符串检查

#### string.startsWith(s, prefix)

检查字符串是否以指定前缀开头。

**参数：**
- `s` - 字符串
- `prefix` - 前缀

**返回值：**
- 布尔值，表示是否以指定前缀开头

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result1 = string.startsWith(text, `Hello`);
result2 = string.startsWith(text, `World`);
show(`Starts with 'Hello': `, result1);  !! 输出: true
show(`Starts with 'World': `, result2);  !! 输出: false
```

#### string.endsWith(s, suffix)

检查字符串是否以指定后缀结尾。

**参数：**
- `s` - 字符串
- `suffix` - 后缀

**返回值：**
- 布尔值，表示是否以指定后缀结尾

**示例：**

```oraset
@string;

text = `Hello, Oraset!`;
result1 = string.endsWith(text, `!`);
result2 = string.endsWith(text, `.`);
show(`Ends with '!': `, result1);  !! 输出: true
show(`Ends with '.': `, result2);  !! 输出: false
```

### 字符串重复

#### string.repeat(s, count)

重复字符串指定次数。

**参数：**
- `s` - 字符串
- `count` - 重复次数

**返回值：**
- 重复后的字符串

**示例：**

```oraset
@string;

text = `Hello `;
result = string.repeat(text, 3);
show(`Repeated: `, result);  !! 输出: Hello Hello Hello 
```

### 字符串反转

#### string.reverse(s)

反转字符串。

**参数：**
- `s` - 字符串

**返回值：**
- 反转后的字符串

**示例：**

```oraset
@string;

text = `Hello`;
result = string.reverse(text);
show(`Reversed: `, result);  !! 输出: olleH
```

## 示例代码

```oraset
@string;

!! 字符串分割与连接
text = `Hello,World,Oraset`;
show(`Original: `, text);
show(`Split: `, string.split(text, `,`));

arr = arr(`Hello`, `World`, `Oraset`);
show(`Joined: `, string.join(arr, ` `));

!! 大小写转换
text = `Hello, Oraset!`;
show(`Original: `, text);
show(`Upper: `, string.upper(text));
show(`Lower: `, string.lower(text));
show(`Capitalized: `, string.capitalize(text));

!! 字符串长度与提取
text = `Hello, Oraset!`;
show(`Length: `, string.length(text));
show(`Substring from 7: `, string.substring(text, 7));
show(`Substring 0-5: `, string.substring(text, 0, 5));
show(`Character at 0: `, string.charAt(text, 0));

!! 字符串查找
text = `Hello, Oraset!`;
show(`Index of 'Oraset': `, string.indexOf(text, `Oraset`));
show(`Includes 'Oraset': `, string.includes(text, `Oraset`));

!! 字符串替换
text = `Hello, World!`;
show(`Original: `, text);
show(`Replaced: `, string.replace(text, `World`, `Oraset`));

!! 字符串修剪
text = `   Hello, Oraset!   `;
show(`Original: '`, text, `'`);
show(`Trimmed: '`, string.trim(text), `'`);
show(`Trimmed start: '`, string.trimStart(text), `'`);
show(`Trimmed end: '`, string.trimEnd(text), `'`);

!! 字符串检查
text = `Hello, Oraset!`;
show(`Starts with 'Hello': `, string.startsWith(text, `Hello`));
show(`Ends with '!': `, string.endsWith(text, `!`));

!! 字符串重复和反转
text = `Hello`;
show(`Original: `, text);
show(`Repeated: `, string.repeat(text, 3));
show(`Reversed: `, string.reverse(text));
```

## 注意事项

- 字符串索引从 0 开始
- 所有字符串操作函数都返回新的字符串，不会修改原始字符串
- 对于 `substring` 函数，如果不指定 `end` 参数，将提取到字符串末尾
- 对于 `split` 函数，如果分隔符为空字符串，将分割每个字符