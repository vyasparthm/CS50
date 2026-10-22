# Python Object-Oriented Programming (OOP) Study Sheet & Cheat Sheet

A comprehensive revision guide structured around the core topics from CS50P (Week 8) and extended with essential real-world additions (`__repr__`, inheritance mechanics with `super()`, encapsulation nuances, and typing annotations).

To maintain focus and avoid context switching, every single concept is demonstrated using one unified domain: the **`Flight`** class and its derived **`CharterFlight`** class.

---

## 1. Quick Concept Reference Table

| Concept | Python Syntax / Keyword | Core Purpose |
| :--- | :--- | :--- |
| **Class** | `class Name:` | Blueprint defining attributes and behavior. |
| **Object / Instance** | `obj = Name(...)` | Concrete realization of a class in memory. |
| **Constructor** | `def __init__(self, ...):` | Initializes state and enforces data invariants. |
| **Instance Method** | `def method(self, ...):` | Operates on and mutates state of a single instance. |
| **Properties** | `@property`, `@name.setter` | Encapsulates access; adds validation without breaking dot syntax. |
| **Class Method** | `@classmethod` (`cls`) | Factory constructors and class-level operations. |
| **Static Method** | `@staticmethod` | Utility functions namespace-bound to the class without instance/class access. |
| **Inheritance** | `class Sub(Base):` | Reuses and extends state/behavior from a base class. |
| **`super()`** | `super().method(...)` | Delegates work up the inheritance chain to the parent class. |
| **Dunders** | `__str__`, `__repr__`, `__add__` | Hooks into Python protocols (printing, operators, iteration). |

---

## 2. Classes, Objects, and the `__init__` Constructor

A **class** defines structure; an **instance** is the actual object created from that blueprint.

* `self`: Explicitly points to the current instance.
* `__init__`: Runs automatically during instantiation to establish initial state and invariants.

```python
class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        # Validate inputs early to maintain class invariants
        if not flight_number or not isinstance(flight_number, str):
            raise ValueError("Invalid flight number.")
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.flight_number = flight_number.strip().upper()
        self.capacity = capacity
        self.passengers: list[str] = []

    def add_passenger(self, name: str) -> bool:
        """Instance method: Reads and updates the specific instance's list."""
        if len(self.passengers) >= self.capacity:
            return False
        self.passengers.append(name.strip().title())
        return True
```

---

## 3. String Representations: `__str__` vs `__repr__`

* `__str__`: Called by `print()` and `str()`. Created for end-user readability.
* `__repr__`: Called in the REPL, debugger, and inside collections (`[flight1, flight2]`). Created for developers; should ideally look like the code needed to recreate the object.

```python
class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number.upper()
        self.capacity = capacity
        self.passengers: list[str] = []

    def __str__(self) -> str:
        # Friendly representation for display
        return f"Flight {self.flight_number} ({len(self.passengers)}/{self.capacity} seats filled)"

    def __repr__(self) -> str:
        # Unambiguous representation for debugging/logging
        return f"Flight(flight_number={self.flight_number!r}, capacity={self.capacity!r})"
```

---

## 4. Encapsulation & Properties (`@property`)

Python does not use strict keywords like `private` or `protected`. Instead:
* `_variable`: Convention meaning "protected / internal implementation detail; do not mutate directly."
* `__variable`: Name mangling (renames to `_ClassName__variable`) to avoid collisions in subclasses.
* `@property`: Creates a "getter".
* `@<attribute>.setter`: Creates a "setter" where validation can be enforced without breaking dot-notation access (`flight.capacity = 150`).

```python
class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number
        # Setter called during __init__ to route through validation
        self.capacity = capacity
        self._passengers: list[str] = []

    # --- Property: capacity ---
    @property
    def capacity(self) -> int:
        """Getter for capacity."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """Setter with validation."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if hasattr(self, "_passengers") and len(self._passengers) > value:
            raise ValueError("Cannot set capacity below currently booked passengers.")
        self._capacity = value

    # --- Read-Only Property: seats_available ---
    @property
    def seats_available(self) -> int:
        """Read-only property computed on the fly."""
        return self._capacity - len(self._passengers)
```

---

## 5. Method Types: Instance vs Class vs Static

```python
class Flight:
    airline_name: str = "AeroPython"  # Class attribute shared across all instances

    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers: list[str] = []

    # 1. Instance Method: Receives `self`
    def board(self, passenger: str) -> bool:
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    # 2. Class Method: Receives `cls` (commonly used as alternative constructors)
    @classmethod
    def from_csv_line(cls, csv_line: str) -> "Flight":
        """Factory: parse 'AA100,180' and instantiate Flight."""
        parts = csv_line.strip().split(",")
        if len(parts) != 2:
            raise ValueError("CSV line must be in 'FLIGHT_NUM,CAPACITY' format.")
        flight_num, capacity = parts[0].strip(), int(parts[1].strip())
        return cls(flight_num, capacity)

    # 3. Static Method: Receives neither `self` nor `cls`
    @staticmethod
    def is_valid_flight_code(code: str) -> bool:
        """Pure utility function logically placed inside Flight."""
        return len(code) >= 4 and code[:2].isalpha() and code[2:].isdigit()
```

---

## 6. Inheritance and `super()`

Inheritance allows specialized classes to inherit attributes and methods from a base class. Use `super()` to delegate shared initialization and method calls back up to the parent.

```python
class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers: list[str] = []

    def board(self, passenger: str) -> bool:
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False

    def get_summary(self) -> str:
        return f"{self.flight_number} (Capacity: {self.capacity})"


class CharterFlight(Flight):
    def __init__(self, flight_number: str, capacity: int, client_name: str) -> None:
        # Delegate base initialization to parent Flight class
        super().__init__(flight_number, capacity)
        self.client_name = client_name

    def get_summary(self) -> str:
        # Extend parent method via super()
        base_summary = super().get_summary()
        return f"{base_summary} [Charter for {self.client_name}]"

    def board(self, passenger: str) -> bool:
        # Add custom validation, then call parent boarding logic
        print(f"Checking private charter clearance for {passenger}...")
        return super().board(passenger)
```

---

## 7. Operator Overloading (Special / Dunder Methods)

Operator overloading lets your custom classes respond to Python's built-in operators:

| Operator | Syntax | Dunder Method |
| :--- | :--- | :--- |
| Addition | `a + b` | `__add__(self, other)` |
| Equality | `a == b` | `__eq__(self, other)` |
| Length | `len(a)` | `__len__(self)` |
| Membership | `x in a` | `__contains__(self, item)` |
| Comparison | `a < b` | `__lt__(self, other)` |

```python
class Flight:
    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers: list[str] = []

    def __len__(self) -> int:
        """Enables len(flight)."""
        return len(self.passengers)

    def __contains__(self, passenger_name: str) -> bool:
        """Enables 'Alice' in flight."""
        return passenger_name in self.passengers

    def __eq__(self, other: object) -> bool:
        """Enables flight1 == flight2 comparison based on flight number."""
        if not isinstance(other, Flight):
            return NotImplemented
        return self.flight_number == other.flight_number

    def __add__(self, other: "Flight") -> "Flight":
        """Enables flight1 + flight2 to merge flights into a combined route."""
        if not isinstance(other, Flight):
            return NotImplemented
        combined_number = f"{self.flight_number}+{other.flight_number}"
        merged = Flight(combined_number, self.capacity + other.capacity)
        merged.passengers = self.passengers + other.passengers
        return merged
```

---

## 8. Complete Consolidated Implementation

A single, cohesive script demonstrating all concepts working together:

```python
class Flight:
    airline: str = "SkyRoute Airways"

    def __init__(self, flight_number: str, capacity: int) -> None:
        self.flight_number = flight_number.strip().upper()
        self.capacity = capacity  # Invokes property setter
        self._passengers: list[str] = []

    # Properties
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Capacity must be a positive integer.")
        if hasattr(self, "_passengers") and len(self._passengers) > value:
            raise ValueError("Capacity cannot be reduced below current passenger count.")
        self._capacity = value

    @property
    def seats_available(self) -> int:
        return self._capacity - len(self._passengers)

    # Instance Methods
    def board(self, passenger: str) -> None:
        if self.seats_available <= 0:
            raise ValueError(f"Cannot board {passenger}: Flight {self.flight_number} is full.")
        self._passengers.append(passenger.strip().title())

    # Class & Static Methods
    @classmethod
    def from_manifest(cls, manifest_str: str) -> "Flight":
        code, cap = manifest_str.strip().split(":")
        return cls(code.strip(), int(cap.strip()))

    @staticmethod
    def calculate_flight_time_hours(distance_miles: float, speed_mph: float = 500.0) -> float:
        if distance_miles <= 0 or speed_mph <= 0:
            raise ValueError("Distance and speed must be positive numbers.")
        return round(distance_miles / speed_mph, 2)

    # Dunder Methods
    def __len__(self) -> int:
        return len(self._passengers)

    def __str__(self) -> str:
        return f"{self.flight_number} ({len(self)}/{self.capacity} booked)"

    def __repr__(self) -> str:
        return f"Flight(flight_number={self.flight_number!r}, capacity={self.capacity!r})"

    def __contains__(self, item: str) -> bool:
        return item in self._passengers

    def __add__(self, other: "Flight") -> "Flight":
        if not isinstance(other, Flight):
            return NotImplemented
        merged = Flight(f"{self.flight_number}&{other.flight_number}", self.capacity + other.capacity)
        for p in self._passengers + other._passengers:
            merged.board(p)
        return merged


class CharterFlight(Flight):
    def __init__(self, flight_number: str, capacity: int, primary_guest: str) -> None:
        super().__init__(flight_number, capacity)
        self.primary_guest = primary_guest

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} [VIP Client: {self.primary_guest}]"


# --- Execution and Verification ---
if __name__ == "__main__":
    # 1. Instantiation
    f1 = Flight("BA249", 3)
    f2 = Flight.from_manifest("LH400:2")

    # 2. Boarding and properties
    f1.board("Alice")
    f1.board("Bob")
    print(str(f1))              # BA249 (2/3 booked)
    print(repr(f1))             # Flight(flight_number='BA249', capacity=3)
    print("Alice" in f1)        # True
    print(f1.seats_available)   # 1

    # 3. Validation safeguard
    try:
        f1.capacity = 1         # Raises ValueError (already 2 passengers aboard)
    except ValueError as err:
        print(f"Validation Guard: {err}")

    # 4. Operator Overloading
    f2.board("Charlie")
    merged_flight = f1 + f2
    print(merged_flight)        # BA249&LH400 (3/5 booked)

    # 5. Inheritance
    vip = CharterFlight("EXEC01", 4, "Wayne Enterprises")
    vip.board("Bruce")
    print(vip)                  # EXEC01 (1/4 booked) [VIP Client: Wayne Enterprises]
```