# Try-Except-Finally: Use Cases

## Valid Combinations

### Case 1: `try` + `except`
The simplest form. Catches errors and prevents the program from crashing.
Use when you just need to handle an error and move on.

### Case 2: `try` + multiple `except`
Catches different exception types separately so each gets a specific response.
Use when different errors need different recovery logic (e.g., retry DB vs reject bad input).

### Case 3: `try` + `except` + `else`
The `else` block runs only if no exception was raised in `try`.
Use when you have success-only logic (e.g., send confirmation email) that should NOT run on failure.

### Case 4: `try` + `except` + `finally`
The `finally` block runs no matter what — success or failure.
Use when you must release resources (e.g., close DB connection, release file lock).

### Case 5: `try` + `except` + `else` + `finally` (Full Form)
The most complete pattern. Handles errors, runs success logic, and guarantees cleanup.
Use in production services where you need all three: error handling + success path + cleanup.

### Case 6: `try` + `finally` (no `except`)
Guarantees cleanup but does NOT catch the exception — it propagates to the caller.
Use when the current function should clean up but let the caller decide how to handle the error.

