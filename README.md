# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
   A hash function is any function that can be used to map data. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are used to index a fixed-size table called a hash table. Use of a hash function to index a hash table is called hashing.

Hash functions and their associated hash tables are used in data storage and retrieval applications to access data in a small and nearly constant time per retrieval, and storage space only fractionally greater than the total space required for the data or records themselves.

2. Collision resolution
   When one or more hash values compete with a single hash table slot, collisions occur. To resolve this, the next available empty slot is assigned to the current hash value. The most common methods are chaining, probabilistic hashing, perfect hashing technique.
   Chaining: This technique implements a linked list

3. Performance of basic hash table operations
   In the worst case, search, insertion, and deletion operations take linear time (O(n)) and are not constant. The worst case would be if every hash table entry were placed inside the linked list that was referenced by a single index.
   However, the average case is still constant time (O(1)).

4. Load factor is the number of items stored in the hash table divided by the number of slots. If you use linear probing for collision resolution, then the maximum load factor is 1. If you use chaining for collision resolution, then the load factor can be greater than 1.
   The general rule of thumb is to resize your hash table when your load factor is greater than 0.7.

5. Automatic resizing
   As the load factor of your hash table increases, so does the likelihood of a collision, which reduces the performance of your hash table. Therefore, you need to monitor the load factor and resize your hash table when the load factor gets too large. The general rule of thumb is to resize your hash table when your load factor is greater than 0.7. Also, when you resize, it is common to double the size of the hash table. When you resize the array, you need to re-insert all of the items into this new hash table. You cannot simply copy the old items into the new hash table. Each item has to be rerun through the hashing function because the hashing function takes into account the size of the hash table when determining the index that it returns.

6. Various use cases for hash tables
   By default hash-tables are non-ordered structures - which means the items don’t get accessed in the order they get inserted. So the use cases are :

- Storing anything where you need access based on a non integer
- Storing anything where there is no need to access data in the order the data is inserted.
- Storage where insertion and access both need to be fast.
- Storage where uniqueness is useful.
- Text index into flatter data structures - use a hashtable to index data items in an array/list.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

_Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)_

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
