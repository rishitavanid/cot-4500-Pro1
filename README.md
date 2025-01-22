# cot-4500-Pro1

## **Project Description**
This project implements four numerical algorithms discussed in Chapter 2 of the course:
1. **Approximation Algorithm**
2. **The Bisection Method**
3. **Fixed-Point Iteration**
4. **Newton-Raphson Method**

The goal is to demonstrate the use of these algorithms for root-finding and other numerical applications, while following industry-standard project structures.

---

## **Project Structure**
cot-4500-Pro1/
|-- src/
|   |-- main/
|   |   |-- __init__.py
|   |   |-- assignment_1.py
|   |-- test/
|       |-- __init__.py
|       |-- test_assignment_1.py
|-- requirements.txt
|-- README.md

---

### **File Descriptions**
1. `src/main/assignment_1.py`:
   - Contains implementations of all four algorithms.

2. `src/test/test_assignment_1.py`:
   - Unit tests for verifying the correctness of the algorithms.

3. `requirements.txt`:
   - Lists any required Python libraries for running the program.

4. `README.md`:
   - Documentation for the project.

5. `__init__.py`:
   - Allows the `src` and `test` directories to be recognized as Python packages.

---

## **Setup and Installation**

### **Step 1: Clone the Repository**
Clone the repository using Git:
git clone <repository_url>
cd cot-4500-Pro1

### **Step 2: Install Dependencies**
Install the required Python libraries:
pip install -r requirements.txt

---

## **Running the Code**

### **Run the Main Program**
Run the main file to execute the algorithms:
python src/main/assignment_1.py

### **Run Unit Tests**
Run unit tests to verify algorithm implementations:
python -m unittest discover src/test

---

## **Algorithms Implemented**

### 1. **Approximation Algorithm**
- Performs approximations with a given level of precision.

### 2. **The Bisection Method**
- A root-finding algorithm that iteratively divides an interval to locate the root of a function.

### 3. **Fixed-Point Iteration**
- Uses iterative methods to find the fixed point of a function.

### 4. **Newton-Raphson Method**
- A root-finding algorithm that uses function derivatives for faster convergence.

---

## **Example Usage**

### **Bisection Method**
Finding the root of f(x) = x^2 - 4:
from assignment_1 import bisection_method

def example_func(x):
    return x**2 - 4

result = bisection_method(example_func, 0, 3, 0.001)
print(f"Root: {result}")

### **Fixed-Point Iteration**
Finding the fixed point of g(x) = sqrt(x+4):
from assignment_1 import fixed_point_iteration

def example_func(x):
    return (x + 4)**0.5

result = fixed_point_iteration(example_func, 2, 0.001, 100)
print(f"Fixed Point: {result}")

---

## **Dependencies**
This project uses the following libraries:
- `numpy`
- `pytest` (for testing)

Ensure these are installed via:
pip install -r requirements.txt

---

## **Contact**
If you encounter any issues, please reach out to the course instructor or teaching assistant for clarification.

---

## **Key Notes**
- Replace `<repository_url>` with the actual GitHub repository URL when you create it.
- Ensure you include all required libraries in `requirements.txt`.
- Keep your structure consistent with the provided instructions.

