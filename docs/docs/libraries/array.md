# 数组库

## 简介

数组库（`@array`）提供了一系列数组操作函数，包括数组长度获取、元素添加、删除、查找、排序等功能。

## 导入方式

```oraset
@array;
```

## 函数参考

### 基本数组操作

#### array.length(arr)

获取数组长度。

**参数：**
- `arr` - 数组

**返回值：**
- 数组的长度

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result = array.length(fruits);
show(`Array length: `, result);  !! 输出: 3
```

#### array.push(arr, item)

向数组末尾添加一个元素。

**参数：**
- `arr` - 数组
- `item` - 要添加的元素

**返回值：**
- 添加元素后的新数组

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`);
result = array.push(fruits, `cherry`);
show(`After push: `, result);  !! 输出: ["apple", "banana", "cherry"]
```

#### array.pop(arr)

移除数组末尾的元素。

**参数：**
- `arr` - 数组

**返回值：**
- 移除元素后的新数组

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result = array.pop(fruits);
show(`After pop: `, result);  !! 输出: ["apple", "banana"]
```

#### array.shift(arr)

移除数组开头的元素。

**参数：**
- `arr` - 数组

**返回值：**
- 移除元素后的新数组

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result = array.shift(fruits);
show(`After shift: `, result);  !! 输出: ["banana", "cherry"]
```

#### array.unshift(arr, item)

向数组开头添加一个元素。

**参数：**
- `arr` - 数组
- `item` - 要添加的元素

**返回值：**
- 添加元素后的新数组

**示例：**

```oraset
@array;

fruits = arr(`banana`, `cherry`);
result = array.unshift(fruits, `apple`);
show(`After unshift: `, result);  !! 输出: ["apple", "banana", "cherry"]
```

### 数组查找

#### array.indexOf(arr, item)

查找元素在数组中的位置。

**参数：**
- `arr` - 数组
- `item` - 要查找的元素

**返回值：**
- 元素的索引，未找到返回 -1

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result1 = array.indexOf(fruits, `banana`);
result2 = array.indexOf(fruits, `orange`);
show(`Index of 'banana': `, result1);  !! 输出: 1
show(`Index of 'orange': `, result2);  !! 输出: -1
```

#### array.lastIndexOf(arr, item)

从数组末尾开始查找元素的位置。

**参数：**
- `arr` - 数组
- `item` - 要查找的元素

**返回值：**
- 元素的索引，未找到返回 -1

**示例：**

```oraset
@array;

numbers = arr(1, 2, 3, 2, 1);
result = array.lastIndexOf(numbers, 2);
show(`Last index of 2: `, result);  !! 输出: 3
```

#### array.includes(arr, item)

检查数组是否包含指定元素。

**参数：**
- `arr` - 数组
- `item` - 要检查的元素

**返回值：**
- 布尔值，表示数组是否包含指定元素

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result1 = array.includes(fruits, `banana`);
result2 = array.includes(fruits, `orange`);
show(`Includes 'banana': `, result1);  !! 输出: true
show(`Includes 'orange': `, result2);  !! 输出: false
```

### 数组转换

#### array.join(arr, sep)

将数组元素连接成一个字符串。

**参数：**
- `arr` - 数组
- `sep` - 分隔符

**返回值：**
- 连接后的字符串

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result = array.join(fruits, `, `);
show(`Joined: `, result);  !! 输出: apple, banana, cherry
```

#### array.reverse(arr)

反转数组元素的顺序。

**参数：**
- `arr` - 数组

**返回值：**
- 反转后的新数组

**示例：**

```oraset
@array;

fruits = arr(`apple`, `banana`, `cherry`);
result = array.reverse(fruits);
show(`Reversed: `, result);  !! 输出: ["cherry", "banana", "apple"]
```

#### array.sort(arr)

对数组元素进行排序。

**参数：**
- `arr` - 数组

**返回值：**
- 排序后的新数组

**示例：**

```oraset
@array;

numbers = arr(3, 1, 4, 1, 5, 9, 2, 6);
result = array.sort(numbers);
show(`Sorted: `, result);  !! 输出: [1, 1, 2, 3, 4, 5, 6, 9]

fruits = arr(`cherry`, `apple`, `banana`);
result = array.sort(fruits);
show(`Sorted fruits: `, result);  !! 输出: ["apple", "banana", "cherry"]
```

#### array.slice(arr, start, end)

提取数组的一部分。

**参数：**
- `arr` - 数组
- `start` - 起始索引（从0开始）
- `end` - 结束索引（不包含）

**返回值：**
- 提取的子数组

**示例：**

```oraset
@array;

numbers = arr(0, 1, 2, 3, 4, 5);
result1 = array.slice(numbers, 2, 4);
result2 = array.slice(numbers, 1);
show(`Slice (2-4): `, result1);  !! 输出: [2, 3]
show(`Slice (1+): `, result2);  !! 输出: [1, 2, 3, 4, 5]
```

## 示例代码

```oraset
@array;

!! 创建数组
fruits = arr(`apple`, `banana`, `cherry`);
show(`Original array: `, fruits);

!! 基本操作
show(`Length: `, array.length(fruits));
show(`After push: `, array.push(fruits, `orange`));
show(`After pop: `, array.pop(fruits));
show(`After unshift: `, array.unshift(fruits, `grape`));
show(`After shift: `, array.shift(fruits));

!! 查找操作
show(`Index of 'banana': `, array.indexOf(fruits, `banana`));
show(`Last index of 'banana': `, array.lastIndexOf(fruits, `banana`));
show(`Includes 'cherry': `, array.includes(fruits, `cherry`));

!! 转换操作
show(`Joined: `, array.join(fruits, ` | `));
show(`Reversed: `, array.reverse(fruits));

!! 排序操作
numbers = arr(5, 2, 8, 1, 9);
show(`Original numbers: `, numbers);
show(`Sorted numbers: `, array.sort(numbers));

!! 切片操作
show(`Slice (1-3): `, array.slice(numbers, 1, 3));
```

## 注意事项

- 所有数组操作函数都返回一个新的数组，不会修改原始数组
- 数组索引从0开始
- 数组元素可以是不同类型的值
- 对于大型数组，某些操作（如排序）可能会影响性能