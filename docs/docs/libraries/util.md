# 工具库

## 简介

工具库（`@util`）提供了一系列实用的工具函数，包括随机数生成、数学计算、类型检查等功能。

## 导入方式

```oraset
@util;
```

## 函数参考

### 随机数生成

#### util.random()

生成一个0到1之间的随机小数。

**参数：**
- 无

**返回值：**
- 0到1之间的随机小数

**示例：**

```oraset
@util;

result = util.random();
show(`Random number: `, result);  !! 输出: 0.123456789
```

#### util.randint(a, b)

生成一个指定范围内的随机整数。

**参数：**
- `a` - 最小值
- `b` - 最大值

**返回值：**
- 范围内的随机整数

**示例：**

```oraset
@util;

result = util.randint(1, 100);
show(`Random integer: `, result);  !! 输出: 42
```

### 数学计算

#### util.round(x, n)

对数字进行四舍五入。

**参数：**
- `x` - 要四舍五入的数字
- `n` - 小数位数（默认为0）

**返回值：**
- 四舍五入后的数字

**示例：**

```oraset
@util;

result1 = util.round(3.14159);
result2 = util.round(3.14159, 2);
show(`Rounded: `, result1);  !! 输出: 3
show(`Rounded to 2 decimals: `, result2);  !! 输出: 3.14
```

#### util.abs(x)

计算数字的绝对值。

**参数：**
- `x` - 数字

**返回值：**
- 数字的绝对值

**示例：**

```oraset
@util;

result = util.abs(-123);
show(`Absolute value: `, result);  !! 输出: 123
```

#### util.min(...args)

返回多个数字中的最小值。

**参数：**
- `...args` - 多个数字

**返回值：**
- 最小值

**示例：**

```oraset
@util;

result = util.min(10, 5, 20, 3);
show(`Minimum: `, result);  !! 输出: 3
```

#### util.max(...args)

返回多个数字中的最大值。

**参数：**
- `...args` - 多个数字

**返回值：**
- 最大值

**示例：**

```oraset
@util;

result = util.max(10, 5, 20, 3);
show(`Maximum: `, result);  !! 输出: 20
```

#### util.sum(...args)

计算多个数字的和。

**参数：**
- `...args` - 多个数字

**返回值：**
- 数字的和

**示例：**

```oraset
@util;

result = util.sum(1, 2, 3, 4, 5);
show(`Sum: `, result);  !! 输出: 15
```

#### util.average(...args)

计算多个数字的平均值。

**参数：**
- `...args` - 多个数字

**返回值：**
- 数字的平均值

**示例：**

```oraset
@util;

result = util.average(1, 2, 3, 4, 5);
show(`Average: `, result);  !! 输出: 3
```

### 类型检查

#### util.isNumber(x)

检查值是否为数字。

**参数：**
- `x` - 要检查的值

**返回值：**
- 布尔值，表示是否为数字

**示例：**

```oraset
@util;

result1 = util.isNumber(123);
result2 = util.isNumber(`123`);
result3 = util.isNumber(`abc`);
show(`Is 123 a number: `, result1);  !! 输出: true
show(`Is '123' a number: `, result2);  !! 输出: true
show(`Is 'abc' a number: `, result3);  !! 输出: false
```

#### util.isString(x)

检查值是否为字符串。

**参数：**
- `x` - 要检查的值

**返回值：**
- 布尔值，表示是否为字符串

**示例：**

```oraset
@util;

result1 = util.isString(`Hello`);
result2 = util.isString(123);
show(`Is 'Hello' a string: `, result1);  !! 输出: true
show(`Is 123 a string: `, result2);  !! 输出: false
```

#### util.isArray(x)

检查值是否为数组。

**参数：**
- `x` - 要检查的值

**返回值：**
- 布尔值，表示是否为数组

**示例：**

```oraset
@util;

result1 = util.isArray(arr(1, 2, 3));
result2 = util.isArray(`[1, 2, 3]`);
result3 = util.isArray(123);
show(`Is arr(1, 2, 3) an array: `, result1);  !! 输出: true
show(`Is '[1, 2, 3]' an array: `, result2);  !! 输出: true
show(`Is 123 an array: `, result3);  !! 输出: false
```

### 类型转换

#### util.toNumber(x)

将值转换为数字。

**参数：**
- `x` - 要转换的值

**返回值：**
- 转换后的数字

**示例：**

```oraset
@util;

result = util.toNumber(`123`);
show(`Converted to number: `, result);  !! 输出: 123
```

#### util.toString(x)

将值转换为字符串。

**参数：**
- `x` - 要转换的值

**返回值：**
- 转换后的字符串

**示例：**

```oraset
@util;

result = util.toString(123);
show(`Converted to string: `, result);  !! 输出: 123
```

#### util.typeof(x)

获取值的类型。

**参数：**
- `x` - 要检查的值

**返回值：**
- 值的类型（'array'、'number'、'string' 或 'unknown'）

**示例：**

```oraset
@util;

result1 = util.typeof(123);
result2 = util.typeof(`Hello`);
result3 = util.typeof(arr(1, 2, 3));
show(`Type of 123: `, result1);  !! 输出: number
show(`Type of 'Hello': `, result2);  !! 输出: string
show(`Type of arr(1, 2, 3): `, result3);  !! 输出: array
```

## 示例代码

```oraset
@util;

!! 随机数生成
show(`Random number: `, util.random());
show(`Random integer (1-100): `, util.randint(1, 100));

!! 数学计算
show(`Absolute value of -123: `, util.abs(-123));
show(`Round 3.14159: `, util.round(3.14159));
show(`Round 3.14159 to 2 decimals: `, util.round(3.14159, 2));
show(`Minimum of 10, 5, 20, 3: `, util.min(10, 5, 20, 3));
show(`Maximum of 10, 5, 20, 3: `, util.max(10, 5, 20, 3));
show(`Sum of 1, 2, 3, 4, 5: `, util.sum(1, 2, 3, 4, 5));
show(`Average of 1, 2, 3, 4, 5: `, util.average(1, 2, 3, 4, 5));

!! 类型检查
show(`Is 123 a number: `, util.isNumber(123));
show(`Is '123' a number: `, util.isNumber(`123`));
show(`Is 'abc' a number: `, util.isNumber(`abc`));
show(`Is 'Hello' a string: `, util.isString(`Hello`));
show(`Is 123 a string: `, util.isString(123));
show(`Is arr(1, 2, 3) an array: `, util.isArray(arr(1, 2, 3)));

!! 类型转换
show(`Convert '123' to number: `, util.toNumber(`123`));
show(`Convert 123 to string: `, util.toString(123));

!! 类型判断
show(`Type of 123: `, util.typeof(123));
show(`Type of 'Hello': `, util.typeof(`Hello`));
show(`Type of arr(1, 2, 3): `, util.typeof(arr(1, 2, 3)));
```

## 注意事项

- 所有工具函数都不会修改原始值，而是返回新的值
- 类型检查函数会尝试进行合理的类型判断
- 对于 `isNumber` 函数，字符串形式的数字也会被认为是数字
- 对于 `isArray` 函数，字符串形式的数组表示也会被认为是数组