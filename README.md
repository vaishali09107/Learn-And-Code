# Python Coding Guidelines (Based on Internal Standards)

These guidelines define best practices for writing clean, maintainable, and scalable Python code. They help ensure consistency, readability, and high-quality development across the team.

## 1. Naming Standards
- Use `CapitalizedWords` (PascalCase) for classes.
- Use `lowercase_with_underscores` (snake_case) for modules, functions, methods, and instance variables.
- Use `UPPER_CASE_WITH_UNDERSCORES` for constants.
- Prefix private attributes with a single leading underscore (e.g., `_my_var`).
- Use meaningful and descriptive names.
- Avoid abbreviations unless commonly accepted.
- Keep package names short and `lowercase`.

## 2. Code Styling and Formatting (PEP 8)
- Follow **PEP 8** style guidelines.
- Function length should be kept reasonable and focused on a single task.
- Limit method parameters to avoid long argument lists.
- Maintain proper indentation (**4 spaces**) and spacing (no tabs).
- Code should be kept within **79 characters** per line (or 99 depending on team agreement); comments/docstrings to **72 characters**.
- Keep code clean, easy to read, and explicitly use 2 blank lines before top-level definitions.
- Consistently use **double quotes** (`"..."`) for strings.

## 3. Object-Oriented Design Rules
- Utilize `__init__` for constructors to initialize instances.
- Group related methods and properties together.
- Use `@property` decorators to provide read-only access to private attributes instead of writing explicit getter/setter functions.
- Follow the single responsibility principle (SRP); a class should do exactly one thing.
- Implement Dunder (magic) methods like `__repr__`, `__str__`, and `__len__` appropriately.

## 4. Managing Dependencies & Coupling
- Prefer constructor injection for dependencies to ensure testability.
- Avoid tightly coupling classes by instantiating complex objects directly within other classes (e.g., assemble all components in an entry point like `main.py`).
- Keep configuration objects decoupled from business logic.

## 5. Exception Management and Logging
- Handle errors properly using context managers (`with open(...) as f:`) to ensure resources are always cleaned up.
- Use built-in exception types or create descriptive custom exception classes.
- Handle specific exceptions rather than catching all errors broadly with bare `except:` statements.
- Log errors properly using a structured logger for easier debugging.
- Do not expose sensitive information (PII) in error messages.

## 6. Input Validation and Sanitization
- Validate inputs early and immediately before processing (e.g., checking for empty or `None` values using `is None`).
- Utilize libraries like Pydantic or Marshmallow for external data shapes and external API validation boundaries.
- Handle validation errors immediately with early returns.

## 7. Application Monitoring Flow
- Log important events to track data flow across services (e.g. tracking requests via an ID).
- Follow a consistent pipeline execution order for easier trace debugging (e.g. Read -> Parse -> Validate -> Transform -> Statistics -> Export).
- Use structured logging (key-value format) where applicable.

## 8. Python Language Integrity & Best Practices
- Utilize **list comprehensions** (`[x for x in lst]`) for concise filtering and mapping, provided they remain readable.
- Embrace Python's dynamic typing, but combine it heavily with explicit **type hinting**.
- Utilize context managers (`with`) instead of explicit try-finally blocks for safe resource management.
- Always include `if __name__ == "__main__":` to guard executable scripts.
- Prefer `is None` and `is not None` over `== None`.
- Take advantage of python's truthy/falsy evaluation (e.g. `if not record_id:` instead of checking length).
- Utilize f-strings (`f"text {var}"`) for readable string interpolation.
- Leverage Object-Oriented patterns like the **Strategy Pattern** across classes when varying behavior is needed.

## 9. Codebase Documentation
- Document project directories and file responsibilities using a standard layout (`config/`, `models/`, `api/`, `utils/`, etc.).
- Clearly delineate between Models (internal representation/database) and Schemas (external shape validation/API responses).
- Use descriptive, standard docstrings (Google or Sphinx) for modules, classes, and complex functions.
- Centralize all configurations and constants to prevent magic numbers scattered in the code.

## 10. Testing Strategies
- Write unit tests for all business logic using `pytest` or Python's built-in `unittest`.
- Cover edge cases and negative scenarios (e.g., handling missing fields, division by zero).
- Keep tests independent and avoid testing multiple units of behavior within one function.
- Group tests logically, mirroring the source folder structure in the `tests/` directory.

## 11. Code Review Expectations
- Keep PRs small and focused on single responsibilities.
- Ensure the code handles edge cases gracefully.
- Ensure tests still pass and the code is reviewed against these styling and architecture standards before merging.

## 12. Core Pythonic Principles
- Follow clean code principles (remember the Zen of Python: "Flat is better than nested").
- Keep logic simple and avoid over-engineering.
- Write code that is easy to read and maintain for the whole team.
- Ensure consistency across the entire codebase.
- Focus on readability over complexity.

---

## 13. Understanding `__init__.py` Files

- Every Python package (a directory that should be importable) must contain an `__init__.py` file.
- The `__init__.py` file tells Python that the directory is a **package**, not just a regular folder.
- It can be **empty** (just marks the directory as a package) or can contain **re-exports** to simplify imports for external consumers.
- Example: Instead of writing `from vehicle_management_system.vehicles.car import Car`, a well-structured `__init__.py` lets you write `from vehicle_management_system.vehicles import Car`.
- Common uses:
  - **Re-exporting classes/functions** using `from .module import ClassName` for cleaner public API.
  - **Defining `__all__`** to control what gets exported when someone does `from package import *`.

## 14. How to Run Python Files

### Running a Script Directly
```bash
python3 filename.py
```

### Running the Vehicle Management System
Navigate into the project directory and run `main.py`:
```bash
cd vehicle_management_system
python3 main.py
```

### Running as a Module (from the parent directory)
```bash
cd Learn-And-Code
python3 -m vehicle_management_system.main
```

### Key Points
- Always use `if __name__ == "__main__":` guard in scripts to prevent code from running on import.
- Use `python3` (not `python`) to ensure you are using Python 3.
- If you get `ModuleNotFoundError`, make sure you are running from the correct directory and all `__init__.py` files exist.
