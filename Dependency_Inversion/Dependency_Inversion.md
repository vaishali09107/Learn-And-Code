# Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions.

---

## Files in This Folder

### connection.py

This file follows DIP by providing a database connection abstraction that other parts of the application depend upon. The `DatabaseConnection` class encapsulates connection pool management behind a simple interface (`get_connection()`), so consuming code never needs to know the specifics of how connections are created, pooled, or recycled. Higher-level modules depend on this abstraction rather than directly on psycopg2 implementation details.

---

### metadata_transformer.py

This file demonstrates DIP by depending on abstract types rather than concrete implementations. The `MetadataTransformer` class accepts `Dict[str, Optional[Any]]` as input—an abstraction that allows any dictionary implementation to be passed. The class does not depend on specific data sources, databases, or external services. It operates purely on abstract data structures, making it decoupled from low-level implementation details.

---

### validators.py

This file adheres to DIP by providing reusable validation functions that can be injected or imported wherever input validation is needed. The validators depend on configuration abstractions (via `get_config()`) for pagination settings rather than hardcoded values. Higher-level modules that need validation can rely on these abstractions (`validate_email`, `validate_uuid`, `validate_pagination`) without coupling themselves to specific validation implementations or configuration sources.
