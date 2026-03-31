# Open/Closed Principle (OCP)

The Open/Closed Principle states that software entities (classes, modules, functions) should be open for extension but closed for modification. This means you should be able to add new functionality without changing existing code, typically achieved through inheritance, interfaces, or composition.

---

## Files in This Folder

### base_repository.py

This file is the cornerstone of OCP in this folder. The `BaseRepository` abstract class provides common database operations (`_execute_query`, `_execute_single`, `_execute_write`, `_execute_count`) that are closed for modification. New repository classes can extend this base class to add specific functionality without altering the base implementation. The use of abstract methods and protected helper methods ensures extensibility while maintaining stability.

---

### calendly_integration.py

This file demonstrates OCP by extending `BaseRepository` to add Calendly-specific database operations. The `CalendlyStatusRepository` class inherits all the base functionality and adds its own methods (`get_all_calendly_status`, `get_calendly_status_paginated`) without modifying the parent class. New Calendly-related operations can be added to this class without changing the base repository.

---

### calendly_status_repository.py

This file follows OCP by extending `BaseRepository` with Calendly status management capabilities. It leverages the inherited `_execute_query` and `_execute_count` methods while adding domain-specific logic for Calendly status retrieval. The base class remains untouched, demonstrating how new features are added through extension rather than modification.

---

### email_sequence_tracking_repositories.py

This file adheres to OCP by extending `BaseRepository` for email sequence tracking operations. The `EmailSequenceTrackingRepository` class adds pagination and tracking-specific methods while relying on the base class for core database operations. The file even includes a comment showing how additional methods can be added following OCP principles—extending behavior without modifying existing code.
