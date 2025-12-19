# Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. Subclasses must honor the contracts established by their parent classes, ensuring that derived types can be used interchangeably with their base types.

---

## Files in This Folder

### api_client.py

This file demonstrates LSP through the `APIClientError` class, which extends Python's built-in `Exception` class. The custom exception can be used anywhere a standard exception is expected—it can be raised, caught, and handled just like any other exception. The class adds additional properties (`error_type`, `message`, `status_code`) and methods (`to_dict()`) while fully honoring the `Exception` contract, making it a valid substitute for its parent class.

---

### calendly_status_repository.py

This file follows LSP by extending `BaseRepository`. The `CalendlyStatusRepository` class can be used anywhere a `BaseRepository` is expected. It properly utilizes inherited methods like `_execute_query` and `_execute_count` without violating the parent class's behavioral contract. Any code expecting a base repository will work correctly with this Calendly-specific implementation.

---

### lead_tracking_repository.py

This file demonstrates LSP through composition with `BaseRepository`. The `LeadTrackingRepository` accepts a `BaseRepository` instance in its constructor and delegates database operations to it. This design allows any implementation of `BaseRepository` to be substituted without affecting the lead tracking functionality. The repository methods honor expected behavior patterns, ensuring predictable substitutability.

---

### transcript_extractor.py

This file adheres to LSP through the `TranscriptSchema` class, which extends Pydantic's `BaseModel`. The schema can be used anywhere a `BaseModel` is expected—for validation, serialization, and structured output. It adds domain-specific fields while fully honoring the `BaseModel` contract, ensuring it can be substituted in any context expecting a Pydantic model.
