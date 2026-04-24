# 函数和类

## 函数

### 函数定义

使用 `def` 关键字定义函数：

```oraset
def function_name(parameters) {
    !! 函数体
    return value; !! 可选
}
```

示例：

```oraset
def greet(name) {
    return `Hello, ` + name + `!`;
}

message = greet(`John`);
show(message); !! 输出: Hello, John!
```

### 函数参数

函数可以接受多个参数：

```oraset
def add(a, b) {
    return a + b;
}

result = add(5, 3);
show(result); !! 输出: 8
```

### 默认参数

函数可以设置默认参数值：

```oraset
def greet(name, greeting = `Hello`) {
    return greeting + `, ` + name + `!`;
}

show(greet(`John`)); !! 输出: Hello, John!
show(greet(`John`, `Hi`)); !! 输出: Hi, John!
```

### 可变参数

函数可以接受可变数量的参数：

```oraset
def sum(...numbers) {
    total = 0;
    for (number in numbers) {
        total = total + number;
    }
    return total;
}

show(sum(1, 2, 3, 4, 5)); !! 输出: 15
```

### 函数返回值

函数可以使用 `return` 语句返回值：

```oraset
def multiply(a, b) {
    return a * b;
}

result = multiply(4, 5);
show(result); !! 输出: 20
```

如果函数没有 `return` 语句，或者 `return` 语句没有值，函数会返回 `undefined`。

### 匿名函数

Oraset 支持匿名函数（也称为 lambda 函数）：

```oraset
add = (a, b) => a + b;
show(add(3, 4)); !! 输出: 7
```

### 递归函数

函数可以递归调用自身：

```oraset
def factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

show(factorial(5)); !! 输出: 120
```

## 类

### 类定义

使用 `class` 关键字定义类：

```oraset
class ClassName {
    constructor(parameters) {
        !! 构造函数
        this.property = value;
    }
    
    method(parameters) {
        !! 方法
    }
}
```

示例：

```oraset
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hello, my name is ` + this.name + ` and I am ` + this.age + ` years old.`;
    }
    
    celebrateBirthday() {
        this.age = this.age + 1;
        return `Happy birthday! I am now ` + this.age + ` years old.`;
    }
}

person = new Person(`John`, 30);
show(person.greet()); !! 输出: Hello, my name is John and I am 30 years old.
show(person.celebrateBirthday()); !! 输出: Happy birthday! I am now 31 years old.
```

### 类属性

类可以有属性，通过 `this` 关键字访问：

```oraset
class Circle {
    constructor(radius) {
        this.radius = radius;
    }
    
    getArea() {
        return 3.14 * this.radius * this.radius;
    }
    
    getCircumference() {
        return 2 * 3.14 * this.radius;
    }
}

circle = new Circle(5);
show(`Area: `, circle.getArea()); !! 输出: Area: 78.5
show(`Circumference: `, circle.getCircumference()); !! 输出: Circumference: 31.4
```

### 类方法

类可以定义方法：

```oraset
class Calculator {
    add(a, b) {
        return a + b;
    }
    
    subtract(a, b) {
        return a - b;
    }
    
    multiply(a, b) {
        return a * b;
    }
    
    divide(a, b) {
        if (b == 0) {
            return `Error: Division by zero`;
        }
        return a / b;
    }
}

calc = new Calculator();
show(`Add: `, calc.add(5, 3)); !! 输出: Add: 8
show(`Subtract: `, calc.subtract(5, 3)); !! 输出: Subtract: 2
show(`Multiply: `, calc.multiply(5, 3)); !! 输出: Multiply: 15
show(`Divide: `, calc.divide(6, 2)); !! 输出: Divide: 3
```

### 继承

Oraset 支持类的继承：

```oraset
class Animal {
    constructor(name) {
        this.name = name;
    }
    
    speak() {
        return `The ` + this.name + ` makes a sound.`;
    }
}

class Dog extends Animal {
    speak() {
        return `The ` + this.name + ` barks.`;
    }
    
    fetch() {
        return `The ` + this.name + ` fetches the ball.`;
    }
}

class Cat extends Animal {
    speak() {
        return `The ` + this.name + ` meows.`;
    }
    
    purr() {
        return `The ` + this.name + ` purrs.`;
    }
}

dog = new Dog(`Rex`);
show(dog.speak()); !! 输出: The Rex barks.
show(dog.fetch()); !! 输出: The Rex fetches the ball.

cat = new Cat(`Whiskers`);
show(cat.speak()); !! 输出: The Whiskers meows.
show(cat.purr()); !! 输出: The Whiskers purrs.
```

### 静态方法

类可以定义静态方法，不需要实例化就可以调用：

```oraset
class MathUtils {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}

show(MathUtils.add(5, 3)); !! 输出: 8
show(MathUtils.multiply(5, 3)); !! 输出: 15
```

## 示例：购物车

```oraset
class ShoppingCart {
    constructor() {
        this.items = arr();
    }
    
    addItem(name, price, quantity = 1) {
        item = obj();
        item.name = name;
        item.price = price;
        item.quantity = quantity;
        this.items.push(item);
        return `Added ` + quantity + ` ` + name + `(s) to cart.`;
    }
    
    removeItem(name) {
        for (i in 0..this.items.length - 1) {
            if (this.items[i].name == name) {
                this.items.splice(i, 1);
                return `Removed ` + name + ` from cart.`;
            }
        }
        return `Item not found in cart.`;
    }
    
    getTotal() {
        total = 0;
        for (item in this.items) {
            total = total + (item.price * item.quantity);
        }
        return total;
    }
    
    getItems() {
        return this.items;
    }
}

cart = new ShoppingCart();
show(cart.addItem(`Apple`, 1.99, 3)); !! 输出: Added 3 Apple(s) to cart.
show(cart.addItem(`Banana`, 0.99, 2)); !! 输出: Added 2 Banana(s) to cart.
show(cart.getItems()); !! 输出: [object Object, object Object]
show(`Total: $`, cart.getTotal()); !! 输出: Total: $7.95
show(cart.removeItem(`Apple`)); !! 输出: Removed Apple from cart.
show(`Total: $`, cart.getTotal()); !! 输出: Total: $1.98
```

## 注意事项

- 函数名和类名应该使用驼峰命名法
- 方法名应该使用驼峰命名法
- 类名应该使用首字母大写的驼峰命名法
- 函数和方法应该有清晰的文档说明
- 避免函数过长，保持函数的单一职责原则