# 字符串库

## 简介

字符串库（`@string`）提供了一系列字符串操作函数，包括字符串分割、大小写转换、查找替换等功能。

## 导入方式

```oraset
@string;
```

## 函数参考

### 基本字符串操作

#### string.split(s, sep)

将字符串按照指定分隔符分割成数组。

**参数：**
- `s` - 要分割的字符串
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

#### string.upper(s)

将字符串转换为大写。

**参数：**
- `s` - 要转换的字符串

**返回值：**
- 转换后的大写字符串

**示例：**

```oraset
@string;

text = `hello world`;
result = string.upper(text);
show(`Upper case: `, result);  !! 输出: HELLO WORLD
```

#### string.lower(s)

将字符串转换为小写。

**参数：**
- `s` - 要转换的字符串

**返回值：**
- 转换后的小写字符串

**示例：**

```oraset
@string;

text = `HELLO WORLD`;
result = string.lower(text);
show(`Lower case: `, result);  !! 输出: hello world
```

#### string.length(s)

获取字符串长度。

**参数：**
- `s` - 要获取长度的字符串

**返回值：**
- 字符串的长度

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result = string.length(text);
show(`Length: `, result);  !! 输出: 11
```

#### string.substring(s, start, end)

提取字符串的子串。

**参数：**
- `s` - 原始字符串
- `start` - 起始索引（从0开始）
- `end` - 结束索引（可选，默认为字符串长度）

**返回值：**
- 提取的子串

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.substring(text, 0, 5);
result2 = string.substring(text, 6);
show(`Substring (0-5): `, result1);  !! 输出: Hello
show(`Substring (6+): `, result2);  !! 输出: Oraset
```

#### string.indexOf(s, substr)

查找子串在字符串中的位置。

**参数：**
- `s` - 原始字符串
- `substr` - 要查找的子串

**返回值：**
- 子串的起始位置，未找到返回 -1

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.indexOf(text, `Oraset`);
result2 = string.indexOf(text, `World`);
show(`Index of 'Oraset': `, result1);  !! 输出: 6
show(`Index of 'World': `, result2);  !! 输出: -1
```

#### string.replace(s, old, new)

替换字符串中的子串。

**参数：**
- `s` - 原始字符串
- `old` - 要替换的子串
- `new` - 替换后的子串

**返回值：**
- 替换后的字符串

**示例：**

```oraset
@string;

text = `Hello World`;
result = string.replace(text, `World`, `Oraset`);
show(`Replaced: `, result);  !! 输出: Hello Oraset
```

#### string.trim(s)

去除字符串首尾的空白字符。

**参数：**
- `s` - 要处理的字符串

**返回值：**
- 去除空白后的字符串

**示例：**

```oraset
@string;

text = `   Hello Oraset   `;
result = string.trim(text);
show(`Trimmed: `, result);  !! 输出: Hello Oraset
```

#### string.startsWith(s, prefix)

检查字符串是否以指定前缀开始。

**参数：**
- `s` - 原始字符串
- `prefix` - 要检查的前缀

**返回值：**
- 布尔值，表示是否以指定前缀开始

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.startsWith(text, `Hello`);
result2 = string.startsWith(text, `World`);
show(`Starts with 'Hello': `, result1);  !! 输出: true
show(`Starts with 'World': `, result2);  !! 输出: false
```

#### string.endsWith(s, suffix)

检查字符串是否以指定后缀结束。

**参数：**
- `s` - 原始字符串
- `suffix` - 要检查的后缀

**返回值：**
- 布尔值，表示是否以指定后缀结束

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.endsWith(text, `Oraset`);
result2 = string.endsWith(text, `World`);
show(`Ends with 'Oraset': `, result1);  !! 输出: true
show(`Ends with 'World': `, result2);  !! 输出: false
```

#### string.includes(s, substr)

检查字符串是否包含指定子串。

**参数：**
- `s` - 原始字符串
- `substr` - 要检查的子串

**返回值：**
- 布尔值，表示是否包含指定子串

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result1 = string.includes(text, `Oraset`);
result2 = string.includes(text, `World`);
show(`Includes 'Oraset': `, result1);  !! 输出: true
show(`Includes 'World': `, result2);  !! 输出: false
```

#### string.repeat(s, count)

重复字符串指定次数。

**参数：**
- `s` - 要重复的字符串
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

#### string.reverse(s)

反转字符串。

**参数：**
- `s` - 要反转的字符串

**返回值：**
- 反转后的字符串

**示例：**

```oraset
@string;

text = `Hello Oraset`;
result = string.reverse(text);
show(`Reversed: `, result);  !! 输出: tesarO olleH
```

#### string.capitalize(s)

将字符串首字母大写。

**参数：**
- `s` - 要处理的字符串

**返回值：**
- 首字母大写的字符串

**示例：**

```oraset
@string;

text = `hello oraset`;
result = string.capitalize(text);
show(`Capitalized: `, result);  !! 输出: Hello oraset
```

#### string.title(s)

将字符串每个单词的首字母大写。

**参数：**
- `s` - 要处理的字符串

**返回值：**
- 每个单词首字母大写的字符串

**示例：**

```oraset
@string;

text = `hello oraset world`;
result = string.title(text);
show(`Title case: `, result);  !! 输出: Hello Oraset World
```

## 示例代码

```oraset
@string;

!! 基本操作
text = `Hello Oraset`;
show(`Original: `, text);
show(`Length: `, string.length(text));
show(`Upper case: `, string.upper(text));
show(`Lower case: `, string.lower(text));

!! 字符串分割
csv = `apple,banana,cherry`;
show(`CSV: `, csv);
show(`Split: `, string.split(csv, `,`));

!! 子串操作
show(`Substring: `, string.substring(text, 6));
show(`Index of 'Oraset': `, string.indexOf(text, `Oraset`));

!! 替换和修改
show(`Replace: `, string.replace(text, `Oraset`, `World`));
show(`Trim: `, string.trim(`   Hello   `));
show(`Repeat: `, string.repeat(`Hi `, 3));
show(`Reverse: `, string.reverse(text));

!! 检查操作
show(`Starts with 'Hello': `, string.startsWith(text, `Hello`));
show(`Ends with 'Oraset': `, string.endsWith(text, `Oraset`));
show(`Includes 'Oraset': `, string.includes(text, `Oraset`));

!! 格式化
show(`Capitalize: `, string.capitalize(`hello world`));
show(`Title case: `, string.title(`hello oraset world`));
```

## 注意事项

- 所有字符串操作函数都不会修改原始字符串，而是返回一个新的字符串
- 字符串索引从0开始
- 分隔符为空字符串时，会将字符串分割为单个字符的数组