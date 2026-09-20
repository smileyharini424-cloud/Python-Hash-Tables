# Python Hash Tables

## Explanation

A Hash Table is a data structure that stores data as **key-value pairs**.

Python dictionaries are implemented using hash table concepts and provide efficient operations for storing and retrieving data using keys.

This program demonstrates basic hash table operations using a Python dictionary.

## Problem Statement

Write a Python program to implement a hash table using a dictionary.

The program should support:

* Insert
* Search
* Update
* Delete
* Display

## Features

* Stores data as key-value pairs
* Supports insertion
* Supports searching
* Supports updating values
* Supports deletion
* Displays all key-value pairs

## How It Works

1. An empty dictionary is created as the hash table.
2. A key and value are inserted into the table.
3. A key can be searched to retrieve its value.
4. Existing values can be updated.
5. A key-value pair can be deleted.
6. The complete hash table can be displayed.

## Technologies Used

* Python 3

## Data Structure Used

* Hash Table
* Dictionary

## Methods Used

* `input()`
* `get()`
* `update()`
* `pop()`
* `items()`

## Program Flow

1. Create an empty hash table.
2. Display the menu.
3. Select an operation.
4. Perform insertion, searching, updating, or deletion.
5. Display the result.
6. Continue until Exit is selected.

## Sample Input

```text id="e7lq31"
1. Insert
2. Search
3. Update
4. Delete
5. Display
6. Exit

Enter your choice: 1
Enter key: 101
Enter value: Harini

Enter your choice: 2
Enter key to search: 101
```

## Sample Output

```text id="h9f3qk"
Value found: Harini
```

## Time Complexity

Average case:

* Insert: O(1)
* Search: O(1)
* Update: O(1)
* Delete: O(1)

## Space Complexity

* O(n)

## Key Learning

* Understanding hash tables
* Understanding key-value pairs
* Using Python dictionaries
* Performing hash table operations
* Understanding average-case complexity

## File Location

```text id="5e0g8p"
Python-Hash-Tables/hash_table.py
```

## Repository Structure

```text id="d6w2xa"
Python-Hash-Tables/
│
├── hash_table.py
└── README.md
```

## Author

V.Harini
