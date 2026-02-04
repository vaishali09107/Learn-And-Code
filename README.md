## Learn and Code – Chapter 6 (Clean Code)

This repository contains exercises and examples based on **Chapter 6 – Objects and Data Structures** from *Clean Code*.

The primary focus is on:
- **Law of Demeter** (avoiding "train wrecks")
- **Tell, Don't Ask**
- **Objects vs Data Structures** (behavior vs data exposure)
- Applying **meaningful names**, **small functions**, and **clear formatting**

### Week 6 Example

In `Week_6/main.py` you will find a small payment example involving:
- **Customer** – an object that owns its internal data and exposes behavior (e.g., `pay`).
- **Wallet** – a data holder for balance.
- **Paperboy** (or equivalent orchestrator) – a service that collects payment by *asking the customer to pay*, instead of directly manipulating internal structures.

This design demonstrates:
- The **Paperboy** does not navigate into nested objects (no `customer.wallet.balance` train wrecks).
- The **Customer** encapsulates its internals and decides how to fulfil a payment request.
- Clear, intention-revealing names and small, focused functions.

### How to Run

From the project root:

```bash
python Week_6/main.py
```

This will execute the Week 6 example and print the result of the payment collection to the console.


