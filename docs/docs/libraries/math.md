# 数学库

## 简介

数学库（`@math`）提供了一系列数学运算函数，包括基本运算、三角函数、随机数生成等。

## 导入方式

```oraset
@math;
```

## 函数参考

### 基本数学函数

#### math.abs(x)

计算绝对值。

**参数：**
- `x` - 数字

**返回值：**
- 数字的绝对值

**示例：**

```oraset
@math;

show(`abs(-123) = `, math.abs(-123));  !! 输出: 123
```

#### math.sqrt(x)

计算平方根。

**参数：**
- `x` - 非负数

**返回值：**
- 平方根值

**示例：**

```oraset
@math;

show(`sqrt(16) = `, math.sqrt(16));  !! 输出: 4
```

#### math.pow(x, y)

计算 x 的 y 次方。

**参数：**
- `x` - 底数
- `y` - 指数

**返回值：**
- x 的 y 次方

**示例：**

```oraset
@math;

show(`pow(2, 3) = `, math.pow(2, 3));  !! 输出: 8
```

#### math.exp(x)

计算 e 的 x 次方。

**参数：**
- `x` - 指数

**返回值：**
- e 的 x 次方

**示例：**

```oraset
@math;

show(`exp(1) = `, math.exp(1));  !! 输出: 2.718281828459045
```

#### math.log(x)

计算自然对数。

**参数：**
- `x` - 正数

**返回值：**
- 自然对数值

**示例：**

```oraset
@math;

show(`log(e) = `, math.log(math.exp(1)));  !! 输出: 1
```

#### math.log10(x)

计算以 10 为底的对数。

**参数：**
- `x` - 正数

**返回值：**
- 以 10 为底的对数值

**示例：**

```oraset
@math;

show(`log10(100) = `, math.log10(100));  !! 输出: 2
```

### 三角函数

#### math.sin(x)

计算正弦值（角度）。

**参数：**
- `x` - 角度

**返回值：**
- 正弦值

**示例：**

```oraset
@math;

show(`sin(90) = `, math.sin(90));  !! 输出: 1
```

#### math.cos(x)

计算余弦值（角度）。

**参数：**
- `x` - 角度

**返回值：**
- 余弦值

**示例：**

```oraset
@math;

show(`cos(0) = `, math.cos(0));  !! 输出: 1
```

#### math.tan(x)

计算正切值（角度）。

**参数：**
- `x` - 角度

**返回值：**
- 正切值

**示例：**

```oraset
@math;

show(`tan(45) = `, math.tan(45));  !! 输出: 1
```

#### math.asin(x)

计算反正弦值（返回角度）。

**参数：**
- `x` - 值（-1 到 1 之间）

**返回值：**
- 反正弦角度

**示例：**

```oraset
@math;

show(`asin(1) = `, math.asin(1));  !! 输出: 90
```

#### math.acos(x)

计算反余弦值（返回角度）。

**参数：**
- `x` - 值（-1 到 1 之间）

**返回值：**
- 反余弦角度

**示例：**

```oraset
@math;

show(`acos(1) = `, math.acos(1));  !! 输出: 0
```

#### math.atan(x)

计算反正切值（返回角度）。

**参数：**
- `x` - 值

**返回值：**
- 反正切角度

**示例：**

```oraset
@math;

show(`atan(1) = `, math.atan(1));  !! 输出: 45
```

### 数学常数

#### math.pi()

返回圆周率 π。

**参数：**
- 无

**返回值：**
- 圆周率 π 值

**示例：**

```oraset
@math;

show(`π = `, math.pi());  !! 输出: 3.141592653589793
```

#### math.e()

返回自然对数的底 e。

**参数：**
- 无

**返回值：**
- 自然对数的底 e 值

**示例：**

```oraset
@math;

show(`e = `, math.e());  !! 输出: 2.718281828459045
```

### 取整函数

#### math.floor(x)

向下取整。

**参数：**
- `x` - 数字

**返回值：**
- 向下取整后的整数

**示例：**

```oraset
@math;

show(`floor(3.9) = `, math.floor(3.9));  !! 输出: 3
show(`floor(-3.1) = `, math.floor(-3.1));  !! 输出: -4
```

#### math.ceil(x)

向上取整。

**参数：**
- `x` - 数字

**返回值：**
- 向上取整后的整数

**示例：**

```oraset
@math;

show(`ceil(3.1) = `, math.ceil(3.1));  !! 输出: 4
show(`ceil(-3.9) = `, math.ceil(-3.9));  !! 输出: -3
```

#### math.round(x)

四舍五入。

**参数：**
- `x` - 数字

**返回值：**
- 四舍五入后的整数

**示例：**

```oraset
@math;

show(`round(3.1) = `, math.round(3.1));  !! 输出: 3
show(`round(3.6) = `, math.round(3.6));  !! 输出: 4
```

### 最值函数

#### math.max(...args)

返回多个数字中的最大值。

**参数：**
- `...args` - 多个数字

**返回值：**
- 最大值

**示例：**

```oraset
@math;

show(`max(10, 5, 20) = `, math.max(10, 5, 20));  !! 输出: 20
```

#### math.min(...args)

返回多个数字中的最小值。

**参数：**
- `...args` - 多个数字

**返回值：**
- 最小值

**示例：**

```oraset
@math;

show(`min(10, 5, 20) = `, math.min(10, 5, 20));  !! 输出: 5
```

### 随机数

#### math.random()

生成 0 到 1 之间的随机小数。

**参数：**
- 无

**返回值：**
- 0 到 1 之间的随机小数

**示例：**

```oraset
@math;

show(`random() = `, math.random());  !! 输出: 0.123456789
```

#### math.randint(a, b)

生成指定范围内的随机整数。

**参数：**
- `a` - 最小值
- `b` - 最大值

**返回值：**
- 范围内的随机整数

**示例：**

```oraset
@math;

show(`randint(1, 100) = `, math.randint(1, 100));  !! 输出: 42
```

## 示例代码

```oraset
@math;

!! 基本运算
show(`abs(-123) = `, math.abs(-123));
show(`sqrt(16) = `, math.sqrt(16));
show(`pow(2, 3) = `, math.pow(2, 3));
show(`exp(1) = `, math.exp(1));
show(`log(e) = `, math.log(math.exp(1)));
show(`log10(100) = `, math.log10(100));

!! 三角函数
show(`sin(90) = `, math.sin(90));
show(`cos(0) = `, math.cos(0));
show(`tan(45) = `, math.tan(45));
show(`asin(1) = `, math.asin(1));
show(`acos(1) = `, math.acos(1));
show(`atan(1) = `, math.atan(1));

!! 数学常数
show(`π = `, math.pi());
show(`e = `, math.e());

!! 取整函数
show(`floor(3.9) = `, math.floor(3.9));
show(`ceil(3.1) = `, math.ceil(3.1));
show(`round(3.6) = `, math.round(3.6));

!! 最值
show(`max(10, 5, 20) = `, math.max(10, 5, 20));
show(`min(10, 5, 20) = `, math.min(10, 5, 20));

!! 随机数
show(`random() = `, math.random());
show(`randint(1, 100) = `, math.randint(1, 100));
```

## 注意事项

- 三角函数使用角度作为参数，而非弧度
- 对于 `sqrt` 和 `log` 等函数，参数必须满足数学要求
- 随机数生成函数使用系统的随机数生成器
- 所有函数都返回数字类型的值