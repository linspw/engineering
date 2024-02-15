# Arrays

## 1. Introduction

Arrays are fundamental data structures that consist of an ordered collections of elements or values.
They provide a way to store multiple items of the same data type or multiple data types in memory locations.

Arrays are widely used due to their simplicity and efficiency for acessing elements or values by their index.

## Examples:

### Python
```python
arr = [1, 2, 3, 4, 20, 30, 40, 50]
```

### Javascript
```javascript
const arr = [0, 1, 3];
```

### Typescript
```ts
const arr: number[] = [0, 1, 3];
```

### C
```c
int arr[3] = {0, 1, 3};
```

## 2. One-dimensional and multi-dimensional arrays


### One-dimensional arrays

One-dimensional arrays are represented simply as ordered lists of values. They are characterized by a single level of indexing, where each element is accessed using a single index value.

#### Definition:
One-dimensional arrays, also known as vectors or lists, are collections of elements of the same data type arranged sequentially in memory.

#### Example in Python:

```python
arr = [1, 99, 200]
```

### Multi-dimensional Arrays:
Multi-dimensional arrays extend the concept of one-dimensional arrays to store data in multiple dimensions, such as rows and columns.

#### Definition: 
Multi-dimensional arrays consist of arrays within arrays, forming a matrix-like structure where elements are accessed using multiple indices.

#### Example in Python:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

## 3. Accessing, inserting, and deleting elements in arrays

### Accessing

Accessing an element in an array requires using its index, which indicates the position of the element within the array. It's important to note that array indices typically start from zero.

#### Example in Python:

```python

vector = [1, 2, 3]
# Indices respectively are 0, 1, 2, corresponding to the order of the elements

# To Access:
vector[2]
# The value is 3

vector[0]
# The value is 1
```

### Inserting

Inserting a new element into an array involves either using a language-specific function or directly replacing a specified element by its index.


#### Example in Pyhton:

```python
vector = [1, 2, 3]

vector.append(10)
# Result: [1, 2, 3, 10]

vector[3] = 20
# Result: [1, 2, 3, 20]
```

### Deleting

Deleting an element from an array requires using specific methods provided by the language.


#### Example in Python:

```python
vector = [1, 2, 3]

vector.pop()
# Removes the last element; alternatively, specify the index of the element to remove
# Result: [1, 2]

# --------------

vector = [1, 2, 3]

vector[1:]
# Result: [2, 3]

vector[:2]
# Result: [1, 2]
```
