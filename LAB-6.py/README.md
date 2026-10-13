# Python OOP Lab Tasks

A collection of beginner-friendly lab tasks covering core Object-Oriented Programming (OOP) concepts in Python: classes and objects, inheritance, and polymorphism.

## Folder Structure

```
python-oop-lab-tasks/
├── TASK-1.py
├── TASK-2.py
├── TASK-3.py
└── README.md
```

## Files Description

| File | Concept | Description |
|------|---------|-------------|
| `TASK-1.py` | Inheritance, `super()` | `Student` is the parent class (name, age, course). `Graduate` inherits from it and adds `research_topic`, reusing the parent's `display()` through `super()`. |
| `TASK-2.py` | Classes & Objects | A basic `student` class with a constructor (`__init__`) and a `display()` method. An object is created and its details are printed. |
| `TASK-3.py` | Polymorphism, Method Overriding | `card_payment` inherits from `cash_payment` and overrides `pay()`. A loop calls `pay()` on each class, showing different behavior for the same method name. |

## Concepts Covered

- Defining classes and creating objects
- Constructors (`__init__`)
- Instance attributes and methods
- Inheritance (single level)
- Calling parent methods with `super()`
- Method overriding and polymorphism

## How to Run

Requires Python 3.x. Clone the repository, then run any task:

```bash
git clone https://github.com/<your-username>/LAB-6.py
cd Lab-6

python TASK-1.py
python TASK-1.py
python TASK-3.py
```

## Expected Output

**Task 1**
```
Junaid
20
AI
Muneeb
20
AI
Artificial Intelligence
```

**Task 2**
```
Haseeb
20
CS
```

**Task 3**
```
cash payment
Card payment
```

## Author

**JUNAID** — BS Artificial Intelligence student
