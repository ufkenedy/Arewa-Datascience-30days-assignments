
### Exercises: Level 1

We'll create a `Statistics` class to handle various statistical calculations.

```python
from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        data_count = Counter(self.data)
        mode_data = data_count.most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}

    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return variance

    def std(self):
        return math.sqrt(self.var())

    def freq_dist(self):
        data_count = Counter(self.data)
        total_count = self.count()
        return [(count / total_count * 100, value) for value, count in data_count.items()]

    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Variance': self.var(),
            'Standard Deviation': self.std(),
            'Frequency Distribution': self.freq_dist()
        }

# Example usage:
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())
print(data.describe())
```

### Exercises: Level 2

We'll create a `PersonAccount` class to manage financial information.

```python
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, description, amount):
        self.incomes.append({'description': description, 'amount': amount})

    def add_expense(self, description, amount):
        self.expenses.append({'description': description, 'amount': amount})

    def total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            'Firstname': self.firstname,
            'Lastname': self.lastname,
            'Total Income': self.total_income(),
            'Total Expense': self.total_expense(),
            'Account Balance': self.account_balance(),
            'Incomes': self.incomes,
            'Expenses': self.expenses
        }

# Example usage:
person = PersonAccount("John", "Doe")
person.add_income("Salary", 5000)
person.add_income("Freelancing", 1500)
person.add_expense("Rent", 1000)
person.add_expense("Groceries", 300)

print(person.account_info())
```
