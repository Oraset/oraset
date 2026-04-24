# 函数和类

本教程将详细介绍 Oraset 编程语言的函数和类，帮助你掌握模块化编程和面向对象编程的基本概念。

## 函数

### 函数定义

使用 `def` 关键字定义函数：

```oraset
!! 函数定义
def greet(name) {
    show(`Hello, `, name, `!`);
}
```

### 函数调用

通过函数名和参数列表调用函数：

```oraset
!! 函数调用
greet(`Oraset`);  !! 输出: Hello, Oraset!
```

### 参数

函数可以接受多个参数：

```oraset
!! 多参数函数
def add(a, b) {
    return a + b;
}

result = add(10, 5);
show(`10 + 5 = `, result);  !! 输出: 15
```

### 返回值

使用 `return` 语句返回函数结果：

```oraset
!! 带返回值的函数
def multiply(a, b) {
    return a * b;
}

result = multiply(10, 5);
show(`10 * 5 = `, result);  !! 输出: 50
```

### 无参数函数

函数可以不接受任何参数：

```oraset
!! 无参数函数
def say_hello() {
    show(`Hello, World!`);
}

say_hello();  !! 输出: Hello, World!
```

### 默认参数

函数可以有默认参数值：

```oraset
!! 默认参数
def greet(name = `World`) {
    show(`Hello, `, name, `!`);
}

greet();          !! 输出: Hello, World!
greet(`Oraset`);  !! 输出: Hello, Oraset!
```

### 可变参数

函数可以接受可变数量的参数：

```oraset
!! 可变参数
def sum(...args) {
    total = 0;
    i = 0;
    while (i < args.length) {
        total = total + args[i];
        i = i + 1;
    }
    return total;
}

result = sum(1, 2, 3, 4, 5);
show(`Sum: `, result);  !! 输出: 15
```

### 递归函数

函数可以递归调用自身：

```oraset
!! 递归函数
def factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

result = factorial(5);
show(`5! = `, result);  !! 输出: 120
```

### 匿名函数

Oraset 支持匿名函数（也称为 lambda 函数）：

```oraset
!! 匿名函数
double = lambda x: x * 2;
show(`Double of 5: `, double(5));  !! 输出: 10

add = lambda a, b: a + b;
show(`10 + 5 = `, add(10, 5));  !! 输出: 15
```

## 类

### 类定义

使用 `class` 关键字定义类：

```oraset
!! 类定义
class Person {
    name = `Unknown`;
    age = 0;
    
    def __init__(self, name, age) {
        self.name = name;
        self.age = age;
    }
    
    def greet(self) {
        show(`Hello, my name is `, self.name, ` and I am `, self.age, ` years old.`);
    }
    
    def celebrate_birthday(self) {
        self.age = self.age + 1;
        show(`Happy birthday! I am now `, self.age, ` years old.`);
    }
}
```

### 类的实例化

创建类的实例：

```oraset
!! 类的实例化
person = Person(`John`, 30);
person.greet();  !! 输出: Hello, my name is John and I am 30 years old.
```

### 类的方法

调用类的方法：

```oraset
!! 调用类的方法
person = Person(`John`, 30);
person.greet();
person.celebrate_birthday();  !! 输出: Happy birthday! I am now 31 years old.
person.greet();  !! 输出: Hello, my name is John and I am 31 years old.
```

### 类的属性

访问和修改类的属性：

```oraset
!! 访问和修改类的属性
person = Person(`John`, 30);
show(`Name: `, person.name);  !! 输出: John
show(`Age: `, person.age);    !! 输出: 30

person.name = `Jane`;
person.age = 25;
show(`Name: `, person.name);  !! 输出: Jane
show(`Age: `, person.age);    !! 输出: 25
```

### 继承

类可以继承其他类的属性和方法：

```oraset
!! 继承
class Student(Person) {
    student_id = ``;
    
    def __init__(self, name, age, student_id) {
        super().__init__(name, age);
        self.student_id = student_id;
    }
    
    def study(self) {
        show(`I am studying. My student ID is `, self.student_id);
    }
}

student = Student(`Alice`, 18, `S12345`);
student.greet();  !! 输出: Hello, my name is Alice and I am 18 years old.
student.study();  !! 输出: I am studying. My student ID is S12345
```

### 静态方法

类可以有静态方法，不需要实例化就可以调用：

```oraset
!! 静态方法
class MathUtils {
    @staticmethod
    def add(a, b) {
        return a + b;
    }
    
    @staticmethod
    def multiply(a, b) {
        return a * b;
    }
}

result1 = MathUtils.add(10, 5);
result2 = MathUtils.multiply(10, 5);
show(`10 + 5 = `, result1);  !! 输出: 15
show(`10 * 5 = `, result2);  !! 输出: 50
```

## 综合示例

### 计算器类

```oraset
!! 计算器类
class Calculator {
    def add(self, a, b) {
        return a + b;
    }
    
    def subtract(self, a, b) {
        return a - b;
    }
    
    def multiply(self, a, b) {
        return a * b;
    }
    
    def divide(self, a, b) {
        if (b == 0) {
            show(`Error: Division by zero`);
            return null;
        }
        return a / b;
    }
    
    def power(self, a, b) {
        result = 1;
        i = 0;
        while (i < b) {
            result = result * a;
            i = i + 1;
        }
        return result;
    }
}

!! 使用计算器
calc = Calculator();
show(`2 + 3 = `, calc.add(2, 3));
show(`5 - 2 = `, calc.subtract(5, 2));
show(`4 * 6 = `, calc.multiply(4, 6));
show(`10 / 2 = `, calc.divide(10, 2));
show(`2 ^ 3 = `, calc.power(2, 3));
```

### 图书管理系统

```oraset
!! 图书管理系统
class Book {
    title = ``;
    author = ``;
    isbn = ``;
    available = true;
    
    def __init__(self, title, author, isbn) {
        self.title = title;
        self.author = author;
        self.isbn = isbn;
    }
    
    def borrow(self) {
        if (self.available) {
            self.available = false;
            return true;
        }
        return false;
    }
    
    def return_book(self) {
        self.available = true;
    }
    
    def get_info(self) {
        status = self.available ? `Available` : `Borrowed`;
        return `Title: ` + self.title + `, Author: ` + self.author + `, ISBN: ` + self.isbn + `, Status: ` + status;
    }
}

class Library {
    books = arr();
    
    def add_book(self, book) {
        self.books = array.push(self.books, book);
    }
    
    def find_book_by_title(self, title) {
        i = 0;
        while (i < array.length(self.books)) {
            book = self.books[i];
            if (book.title == title) {
                return book;
            }
            i = i + 1;
        }
        return null;
    }
    
    def list_books(self) {
        i = 0;
        while (i < array.length(self.books)) {
            book = self.books[i];
            show(book.get_info());
            i = i + 1;
        }
    }
}

!! 使用图书管理系统
library = Library();

!! 添加图书
library.add_book(Book(`The Great Gatsby`, `F. Scott Fitzgerald`, `978-0743273565`));
library.add_book(Book(`To Kill a Mockingbird`, `Harper Lee`, `978-0061120084`));
library.add_book(Book(`1984`, `George Orwell`, `978-0451524935`));

!! 列出所有图书
show(`All books:`);
library.list_books();

!! 借阅图书
book = library.find_book_by_title(`1984`);
if (book) {
    if (book.borrow()) {
        show(`Successfully borrowed: `, book.title);
    } else {
        show(`Book not available: `, book.title);
    }
}

!! 再次列出图书
show(`\nBooks after borrowing:`);
library.list_books();
```

## 注意事项

1. **函数命名**：函数名应该使用小写字母，多个单词之间使用下划线
2. **类命名**：类名应该使用驼峰命名法（首字母大写）
3. **方法命名**：方法名应该使用小写字母，多个单词之间使用下划线
4. **参数传递**：参数按值传递，对于数组等复杂类型，传递的是引用
5. **self 参数**：类的方法第一个参数必须是 `self`，表示实例本身
6. **super()**：在继承中，使用 `super()` 调用父类的方法

## 练习

1. 编写一个函数，计算两个数的最大公约数
2. 编写一个函数，判断一个字符串是否为回文
3. 编写一个类，表示一个银行账户，包含存款、取款和查询余额的方法
4. 编写一个类，表示一个矩形，包含计算面积和周长的方法

## 小结

本教程介绍了 Oraset 编程语言的函数和类，包括：

- 函数定义和调用
- 函数参数和返回值
- 递归函数和匿名函数
- 类的定义和实例化
- 类的方法和属性
- 继承和静态方法
- 综合示例：计算器类和图书管理系统

掌握这些概念后，你可以编写更模块化、更可维护的 Oraset 程序。