# Youssef Auth - Official Python SDK & Example

<p align="center">
  <img src="https://youssefauth.wuaze.com/Youssef%20Auth.ico" width="80" alt="Youssef Auth Logo" />
  <br>
  <b>Next-Gen Software Licensing, HWID Locking & Authentication</b>
  <br>
  <a href="https://youssefauth.wuaze.com">Website</a> â€¢
  <a href="https://github.com/x97xff">GitHub Profile</a>
</p>

---

## âš¡ Features
- ðŸ›¡ï¸ **HWID Locking**: Prevents sharing licenses across unauthorized machines.
- ðŸ”‘ **License Management**: Days-based, lifetime, and tiered subscriptions.
- ðŸ“¦ **Zero-Config Cloud Auth**: Connected directly to `https://youssefauth.wuaze.com/api/1.2/`.
- ðŸ“Š **Remote Logging**: Log unauthorized attempts or actions to your dashboard.

## ðŸš€ Quick Start

1. **Clone this repository**:
```bash
git clone https://github.com/x97xff/YoussefAuth-PY-Example.git
cd YoussefAuth-PY-Example
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure your credentials in `main.py`**:
```python
auth = api(
    name="YourAppName",
    ownerid="YourOwnerId",
    secret="YourAppSecret",
    version="1.0"
)
```

4. **Run the example**:
```bash
python main.py
```

---
*Created by [x97xff](https://github.com/x97xff) with Youssef Auth.*