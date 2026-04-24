# Functions and Classes

## Functions

### Function Definition

Use the `def` keyword to define a function:

```oraset
def function_name(parameters) {
    !! Function body
    return value; !! Optional
}
```

Example:

```oraset
def greet(name) {
    return `Hello, ` + name + `!`;
}

message = greet(`John`);
show(message); !! Output: Hello, John!
```

### Function Parameters

Functions can accept multiple parameters:

```oraset
def add(a, b) {
    return a + b;
}

result = add(5, 3);
show(result); !! Output: 8
```

### Default Parameters

Functions can have default parameter values:

```oraset
def greet(name, greeting = `Hello`) {
    return greeting + `, ` + name + `!`;
}

show(greet(`John`)); !! Output: Hello, John!
show(greet(`John`, `Hi`)); !! Output: Hi, John!
```

### Variable Arguments

Functions can accept a variable number of arguments:

```oraset
def sum(...numbers) {
    total = 0;
    for (number in numbers) {
        total = total + number;
    }
    return total;
}

show(sum(1, 2, 3, 4, 5)); !! Output: 15
```

### Function Return Values

Functions can return values using the `return` statement:

```oraset
def multiply(a, b) {
    return a * b;
}

result = multiply(4, 5);
show(result); !! Output: 20
```

If a function doesn't have a `return` statement, or the `return` statement has no value, the function returns `undefined`.

### Anonymous Functions

Oraset supports anonymous functions (also called lambda functions):

```oraset
add = (a, b) => a + b;
show(add(3, 4)); !! Output: 7
```

### Recursive Functions

Functions can call themselves recursively:

```oraset
def factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

show(factorial(5)); !! Output: 120
```

## Classes

### Class Definition

Use the `class` keyword to define a class:

```oraset
class ClassName {
    constructor(parameters) {
        !! Constructor
        this.property = value;
    }
    
    method(parameters) {
        !! Method
    }
}
```

Example:

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
show(person.greet()); !! Output: Hello, my name is John and I am 30 years old.
show(person.celebrateBirthday()); !! Output: Happy birthday! I am now 31 years old.
```

### Class Properties

Classes can have properties, accessed through the `this` keyword:

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
show(`Area: `, circle.getArea()); !! Output: Area: 78.5
show(`Circumference: `, circle.getCircumference()); !! Output: Circumference: 31.4
```

### Class Methods

Classes can define methods:

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
show(`Add: `, calc.add(5, 3)); !! Output: Add: 8
show(`Subtract: `, calc.subtract(5, 3)); !! Output: Subtract: 2
show(`Multiply: `, calc.multiply(5, 3)); !! Output: Multiply: 15
show(`Divide: `, calc.divide(6, 2)); !! Output: Divide: 3
```

### Inheritance

Oraset supports class inheritance:

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
show(dog.speak()); !! Output: The Rex barks.
show(dog.fetch()); !! Output: The Rex fetches the ball.

cat = new Cat(`Whiskers`);
show(cat.speak()); !! Output: The Whiskers meows.
show(cat.purr()); !! Output: The Whiskers purrs.
```

### Static Methods

Classes can define static methods, which can be called without instantiating the class:

```oraset
class MathUtils {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}

show(MathUtils.add(5, 3)); !! Output: 8
show(MathUtils.multiply(5, 3)); !! Output: 15
```

## Example: Shopping Cart

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
show(cart.addItem(`Apple`, 1.99, 3)); !! Output: Added 3 Apple(s) to cart.
show(cart.addItem(`Banana`, 0.99, 2)); !! Output: Added 2 Banana(s) to cart.
show(cart.getItems()); !! Output: [object Object, object Object]
show(`Total: $`, cart.getTotal()); !! Output: Total: $7.95
show(cart.removeItem(`Apple`)); !! Output: Removed Apple from cart.
show(`Total: $`, cart.getTotal()); !! Output: Total: $1.98
```

## Notes

- Use camelCase for function and method names
- Use PascalCase for class names
- Functions and methods should have clear documentation
- Avoid long functions, follow the single responsibility principle