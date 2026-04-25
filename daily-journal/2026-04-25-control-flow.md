# 📅 Daily Journal - April 25, 2026

## 🎯 Day 5 of 30: Control Flow & Conditional Logic

---

### 🌅 Today's Focus

**Primary Topic:** Python Control Flow Structures  
**Dicoding Module:** Conditional Statements and Loops  
**Goal:** Master if/elif/else logic and iteration patterns

**Why This Matters:**  
Control flow is fundamental to ALL programming. Without conditionals and loops, we can't make decisions or process collections of data—both critical for data analysis.

---

### 📚 What I Learned Today

#### ✅ **Conditional Statements (if/elif/else)**

**Core Concepts:**
- Boolean expressions and truthiness
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Nested conditionals
- Ternary operator (one-line if/else)

**Code Practice:**
```python
# Basic conditional
temperature = 25
if temperature > 30:
    print("It's hot! 🔥")
elif temperature > 20:
    print("Nice weather! ☀️")
else:
    print("It's cold! ❄️")

# Multiple conditions with logical operators
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive! 🚗")
elif age >= 18 and not has_license:
    print("You're old enough, but need a license!")
else:
    print("You're too young to drive.")

# Ternary operator (compact if/else)
status = "Adult" if age >= 18 else "Minor"
print(status)
```

**Real-World Application:**
```python
# Data validation function
def validate_email(email):
    if "@" not in email:
        return False, "Missing @ symbol"
    elif "." not in email.split("@")[1]:
        return False, "Missing domain extension"
    elif len(email) < 5:
        return False, "Email too short"
    else:
        return True, "Valid email"

# Grade calculator for students
def calculate_grade(score):
    if not 0 <= score <= 100:
        return "Invalid score"
    elif score >= 90:
        return "A - Excellent!"
    elif score >= 80:
        return "B - Good job!"
    elif score >= 70:
        return "C - Satisfactory"
    elif score >= 60:
        return "D - Needs improvement"
    else:
        return "F - Must retake"
```

---

#### ✅ **Loops (for and while)**

**For Loops:**
```python
# Iterating over range
for i in range(5):
    print(f"Number: {i}")

# Iterating over list
colors = ["red", "green", "blue"]
for color in colors:
    print(f"I like {color}")

# Enumerate for index + value
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")

# List comprehension (advanced for loop)
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**While Loops:**
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# User input validation
while True:
    password = input("Enter password (min 8 chars): ")
    if len(password) >= 8:
        print("Password accepted!")
        break
    else:
        print("Too short! Try again.")

# Countdown timer
seconds = 10
while seconds > 0:
    print(f"{seconds} seconds remaining...")
    seconds -= 1
print("Time's up!")
```

**Loop Control:**
```python
# break - exit loop immediately
for num in range(100):
    if num > 10:
        break
    print(num)

# continue - skip to next iteration
for num in range(10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Only prints odd numbers

# pass - placeholder (do nothing)
for item in collection:
    pass  # TODO: implement later
```

---

#### ✅ **Classic Programming Challenges**

**FizzBuzz (Interview Classic):**
```python
# Print numbers 1-100, but:
# - "Fizz" for multiples of 3
# - "Buzz" for multiples of 5
# - "FizzBuzz" for multiples of both

for num in range(1, 101):
    if num % 15 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

**Factorial Calculator:**
```python
def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))  # 120
```

**Prime Number Checker:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find first 10 primes
primes = []
num = 2
while len(primes) < 10:
    if is_prime(num):
        primes.append(num)
    num += 1
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

### 🧠 Key Insights

#### **About Control Flow:**
> "Every complex program is just a series of simple decisions and repetitions combined in clever ways."

**Realization:** The same if/else and loop patterns appear EVERYWHERE in data analysis:
- Data validation (if checks)
- Processing datasets (for loops)
- Filtering data (if inside for)
- Aggregating results (accumulator pattern)

#### **About Problem-Solving:**
Breaking down problems into:
1. **What decision needs to be made?** → if/elif/else
2. **What needs to be repeated?** → for/while loop
3. **What's the exit condition?** → break/return

This mental framework applies to every coding challenge!

---

### 💡 Practical Applications for Data Science

**Data Cleaning Example:**
```python
# Clean a list of temperatures (remove invalid data)
temperatures = [25, -999, 30, 28, -999, 32, 27]
cleaned = []

for temp in temperatures:
    if temp != -999:  # -999 is "missing data" code
        cleaned.append(temp)

print(f"Valid temperatures: {cleaned}")
# Output: [25, 30, 28, 32, 27]
```

**Data Categorization:**
```python
# Categorize customers by spending
purchases = [45, 120, 300, 75, 250, 30, 180]
categories = {"low": 0, "medium": 0, "high": 0}

for amount in purchases:
    if amount < 50:
        categories["low"] += 1
    elif amount < 200:
        categories["medium"] += 1
    else:
        categories["high"] += 1

print(categories)
# Output: {'low': 2, 'medium': 3, 'high': 2}
```

**Finding Patterns:**
```python
# Find consecutive increases in stock prices
prices = [100, 102, 105, 103, 107, 110, 108]
increases = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
        increases += 1

print(f"Stock increased {increases} times")
```

---

### 🚧 Challenges & Solutions

#### **Challenge 1: Infinite Loop**
**Problem:** Forgot to increment counter in while loop → program froze

**Bad Code:**
```python
count = 0
while count < 5:
    print(count)
    # Forgot: count += 1
    # Loop runs forever! 🔄
```

**Solution:** Always ensure loop variable changes
```python
count = 0
while count < 5:
    print(count)
    count += 1  # ✅ Exit condition will eventually be met
```

**Lesson:** In while loops, ALWAYS have a clear path to the exit condition.

---

#### **Challenge 2: Off-by-One Errors**
**Problem:** range(10) gives 0-9, not 1-10 as I initially thought

**Confusion:**
```python
# I wanted numbers 1-10, but got 0-9
for i in range(10):
    print(i)  # Prints: 0, 1, 2, ... 9
```

**Solution:** Use range(1, 11) for 1-10
```python
for i in range(1, 11):
    print(i)  # Prints: 1, 2, 3, ... 10
```

**Lesson:** Python ranges are [start, stop) → includes start, excludes stop

---

#### **Challenge 3: Nested Loop Confusion**
**Problem:** Lost track of which loop variable was which in nested loops

**Confusing Code:**
```python
for i in range(3):
    for i in range(3):  # ❌ Reusing variable name!
        print(i, i)
```

**Solution:** Use descriptive variable names
```python
for row in range(3):
    for col in range(3):  # ✅ Clear what each represents
        print(f"Position ({row}, {col})")
```

**Lesson:** In nested loops, use meaningful names like row/col, outer/inner, i/j

---

### 📊 Practice Statistics

**Exercises Completed:** 12  
**Time Spent:**
- Theory & examples: 45 min
- Coding practice: 60 min
- Challenge problems: 30 min
- **Total:** 2 hours 15 minutes

**Problems Solved:**
- ✅ FizzBuzz (classic interview problem)
- ✅ Factorial calculator
- ✅ Prime number checker
- ✅ Grade calculator
- ✅ Email validator
- ✅ Temperature converter with validation
- ✅ Password strength checker
- ✅ Number guessing game (while loop)
- ✅ Multiplication table generator (nested loops)
- ✅ Pattern printing (loops + conditionals)
- ✅ Sum of even numbers in range
- ✅ Countdown timer with break condition

**Success Rate:** 10/12 on first try (83%)  
**Debugging Sessions:** 4 (all resolved)

---

### 🎯 Tomorrow's Plan (Day 6)

**Topic:** Functions and Parameters  
**Dicoding Module:** Function Definition, Arguments, Return Values

**Learning Goals:**
- [ ] Understand function syntax and structure
- [ ] Practice parameters (positional, keyword, default)
- [ ] Learn return statements and multiple returns
- [ ] Write reusable, modular code
- [ ] Understand scope (local vs global variables)

**Practice Plan:**
- Define 10+ functions from scratch
- Refactor today's code into functions
- Build mini calculator with functions
- Create data cleaning utilities

**Time Allocation:**
- 📚 Dicoding module: 60 minutes
- 💻 Coding practice: 60 minutes
- 📝 Documentation: 15 minutes

---

### 🌟 Wins Today

✨ **Completed 12 coding exercises** (most in one day so far!)  
✨ **Solved FizzBuzz** without looking at solution first  
✨ **Zero infinite loops** in final code (debugged all mistakes!)  
✨ **Applied concepts to data scenarios** (not just abstract examples)  
✨ **Day 5/30 streak maintained** 🔥  

---

### 🔄 Continuous Improvement

**What Went Well:**
- More hands-on coding than previous days
- Tackled classic interview problems
- Connected concepts to data science applications
- Debugged mistakes independently

**What Could Be Better:**
- Spend less time on perfect notes, more on coding
- Practice more complex nested loop problems
- Time-box exercises (don't overthink simple problems)

**Adjustment:**
- Tomorrow: 80% coding, 20% documentation
- Set 10-minute timer per exercise
- Focus on writing code, not perfect code

---

### 💭 Reflection

**Before Today:** Control flow seemed abstract—just syntax to memorize.

**After Today:** Control flow is the LOGIC of programming. Every data pipeline, every analysis, every ML model uses these same patterns:
- Filter data → if statements
- Process records → for loops
- Validate input → while loops with conditions
- Transform values → conditionals inside loops

**The "Aha!" Moment:**  
When I wrote the data categorization function and realized it's the same pattern as the SQL GROUP BY I'll learn later. Programming concepts transfer across languages and domains!

---

### 📈 Progress Metrics

**Week 1 Status:**
- Days completed: 5/7 (71%)
- On track for weekly goal ✅
- 2 more days to complete Week 1

**Overall Progress:**
- Total days: 5/30 (16.7%)
- Total hours: ~15 hours
- GitHub streak: 5 days 🔥
- Confidence level: ⬆️ Growing daily

**Job Hunt Update:**
- Portfolio: ✅ Ready
- Applications sent this week: 0 (focused on learning)
- Next week goal: 15 applications

---

**Energy Level:** ⚡⚡⚡⚡⚡ (5/5) - High! Best learning day yet  
**Confidence Level:** 📈📈📈📈 (4/5) - Control flow feels natural now  
**Tomorrow's Excitement:** 🔥🔥🔥🔥🔥 - Can't wait to learn functions!  

---

**Quote of the Day:**
> "Logic will get you from A to B. Imagination will take you everywhere." — Albert Einstein

Today was all about logic (control flow). Tomorrow, I'll add imagination (functions that combine these patterns in creative ways). 🚀

---

**Signed off:** 21:00 WIB  
**Status:** Day 5 complete ✅  
**Next:** Day 6 - Functions & Modularity 💪
