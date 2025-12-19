# Interface Segregation Principle (ISP)

The Interface Segregation Principle states that clients should not be forced to depend on interfaces they do not use. Instead of one large, monolithic interface, it is better to have many smaller, specific interfaces so that clients only need to know about the methods that are relevant to them.

---

## Files in This Folder

### calendly_status_repository.py

This file demonstrates ISP by providing a focused, cohesive interface for Calendly status operations only. The `CalendlyStatusRepository` class exposes methods specifically for Calendly-related functionality (`create_table`, `create_calendly_invite`, `get_status_by_lead_id`, `get_status_by_email`). Clients that need Calendly status management depend only on this specific interface, not on a bloated repository with unrelated methods.

---

### email_service.py

This file follows ISP by providing a dedicated interface for email operations. The `EmailService` class exposes only email-related methods (`send_email`, `send_email_sequence`, `_load_email_template`). Clients needing email functionality depend on this specific service without being coupled to unrelated features like database operations or API calls. The singleton pattern (`get_email_service()`) ensures clients get a focused email interface.

---

### usage_tracker.py

This file exemplifies ISP with a minimal, focused interface. The `UsageTracker` class provides exactly three methods that clients need: `add_usage()` to record token usage, `get_metrics()` to retrieve aggregated statistics, and `reset()` to clear the tracker. Clients tracking API usage depend only on these specific methods, without any unnecessary dependencies on logging, persistence, or other unrelated functionality.
