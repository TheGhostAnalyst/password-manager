# 🔐 Password Manager (CLI)  
A simple, local password manager built using Python — created by **The Ghost Analyst** 👻

This tool allows users to securely store, view, and search for passwords associated with websites and applications via the command line.

---

## 🚀 Features

- ✅ Save passwords with timestamps
- 🔍 Search entries by website or app name
- 📋 View all stored credentials in a clean, organized format
- 🧠 Built with input validation and regex search
- 🗃️ Stores data locally in `password_manager.txt`

---

## 📦 Tech Stack

- Python 3
- [`pyinputplus`](https://pypi.org/project/PyInputPlus/) for validated CLI input
- `re` for regex-based searching
- `datetime` and `pathlib` for timestamping and file management

---

## 🛠️ Setup & Installation

1. **Clone this repo**  
   ```bash
   git clone https://github.com/TheGhostAnalyst/password-manager.git
   cd password-manager
   pip install -r requirements.txt


2. **Run the script**

   ```bash
   python3 password_manager.py
   ```

---

## 🧪 How It Works

1. Choose from:

   * `1` → Save a new password
   * `2` → View all saved passwords
   * `3` → Search for a password by app/website
   * `4` → Exit

2. All passwords are saved in a local file: `password_manager.txt`.

---

## 📌 Example Entry

```
2025-08-22 13:40
Website/App: Facebook
Username/Num/Email: ghost@example.com
Password: MyStrongPass123!
##############################
```

---

## 🛡️ Security Notice

⚠️ **Passwords are stored in plain text**. This tool is meant for educational/personal/local use only.
Future versions will include encryption and optional password masking.

---

## 🧠 Future Plans

* [ ] Encrypt stored data (using Fernet or similar)
* [ ] Add a master password lock
* [ ] Auto-generate strong passwords
* [ ] GUI version with Tkinter or PyQt
* [ ] Export/import to/from CSV or JSON

---

## 👤 Author

**The Ghost Analyst**
🛠 Python Developer • 🧠 Automation Enthusiast • 🕵️ Security Learner
Feel free to connect or contribute!

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

