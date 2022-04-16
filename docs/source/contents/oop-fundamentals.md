# Object Oriented Programming (OOP) Fundamentals

## Procedural Programming

We normally code as a sequence of steps:

1. Download the data 
2. Process the data 
3. Visualize it

The more data we have, the more functionality we might create, and the harder it is to think about as just a 
sequence of steps.

## Object-oriented Programming

An object is a data structure, which contains information about state and behavior.

For example,  an object representing a `person` can have a certain `name`, `phone number`, and`email`  associated 
with them, and behaviors like `callPerson` and `emailPerson`. 

Instead of thinking of `person` data separately from `person` actions, we think of them as one unit representing a 
`person`. This is called encapsulation.

  
### Classes 

Classes describe the possible states and behaviors that every object of a certain `type` could have.

For example. We can say that *"every `person` will have a `name`, `phone number` and `email`, and will be able to 
receive `calls` and `emails`"*. Bingo! you just defined a `class`.

See a `Person Class` summary built in cards for better visualization. 


::::{grid} 2
:::{grid-item-card}
Person 1 
^^^
name:

phone-number:

email:
+++
callPerson

emailPerson
:::
:::{grid-item-card} 
Person 2
^^^
name:

phone-number:

email:
+++
callPerson

emailPerson

:::
::::

```{note}
Now we can talk about any `person` in a unified way. 
```

### Objects

+ Everything in Python is an `object`
+ Every object has a `class`

| Object         | Class       |
|----------------|-------------|
| 5              | int         |
| "Hello"        | str         |
| pd.DateFrame() | DataFrame   |
| ...            | ...         |

+ You can use `type()` to find the class

**Example 1**:

```python
import numpy as np

a = np.array([1,2,3])
print(type(a))
```
```python
numpy.ndarray
```

**Example 2**:

+ Let's create a simple `class` called `Car` and lets display it:

    ```python
    >>> class Car: pass
    >>> Car
    <class '__main__.Car'>        # This says that Car is in the module __main__
    ```

    ```{note}
    The word `Car` is a variable that references the `class` `object` from the memory runtime. 
    ```

+ If we want to Instantiate, or represent, a `class`, we have to add the parenthesis.

    ```python
    >>> Car()
    <__main__.Car object at 0x10a319250>
    ```

    ```{important}
    The Object has the ID 0x10a24d5e0, which is an instantiation/reference of the class Car from the module __main__.
    ```
+ Let's check the `type` of an **instantiation** by doing the following:

    ```python
    >>> type(Car())
    <class '__main__.Car'>
    ```
    ```{note}
    When we call the instantiation `Car()` inside `type()`, the `object` we are creating while calling `type()` is 
    the type = Car.  
    ```

+ Let's now check the `type` of this **class**: 

    ```python
    >>> type(Car)
    <class 'type'>
    ```
    ```{note}
    Here, the `class` Car, is a type type
    ```
+ On Python3, every `class` is a subclass of an `object`.

    ```python
    >>> issubclass(Car, object)
    True
    ```
    `class Car(object): pass` is the same as `class Car: pass`. In other words, we are saying that `Car` is a `class`
    that inherits from `object`. 
