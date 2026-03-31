# Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change. In other words, each class should be responsible for a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class.

---

## Files in This Folder

### api_client.py

This file demonstrates SRP by defining the `APIClientError` class with a single, focused responsibility: representing and handling API client errors. The class encapsulates error type, message, and status code, and provides a `to_dict()` method for consistent error serialization. It does not concern itself with making API calls, logging, or any other functionality—its sole purpose is error representation.

---

### calendly_integration.py

This file follows SRP by containing the `CalendlyStatusRepository` class, which has one responsibility: managing database operations for Calendly status records. All methods (`get_all_calendly_status`, `get_calendly_status_paginated`) are focused solely on retrieving Calendly-related data from the database. The class does not handle API calls, email sending, or any unrelated functionality.

---

### call_monitor.py

This file adheres to SRP by defining the `CallMonitor` class with a single responsibility: monitoring call status by polling the database. The class tracks call state transitions, handles timeouts, and invokes status callbacks. It does not manage database connections, make API calls, or handle transcripts—its only concern is monitoring and reporting call status changes.

---

### exceptions.py

This file exemplifies SRP through a hierarchy of exception classes, each with a single, distinct responsibility:
- `RepositoryException`: Base exception for repository operations
- `ValidationError`: Handles input validation failures
- `DatabaseConnectionError`: Handles database connection issues
- `RecordNotFoundError`: Handles missing record scenarios
- `QueryExecutionError`: Handles query execution failures
- `TransactionError`: Handles transaction failures

Each exception class is responsible for representing one specific type of error, making error handling clear and maintainable.
