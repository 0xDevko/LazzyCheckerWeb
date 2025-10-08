# 🚀 LazzyCheckerWeb

**LazzyCheckerWeb** is a lightweight Python script designed to brute-force and check the availability of endpoints on a website. Just provide a base URL and a dictionary file — it does the rest.

---

## 🔍 What It Does

This tool helps you discover active endpoints on a web server by:

- Taking a **base URL** (e.g., `https://example.com/`)
- Reading a **wordlist file** with potential endpoint paths
- Sending HTTP requests to each constructed URL
- Reporting which endpoints are live based on HTTP status codes


## 📦 Requirements

Only one external library is needed:

```bash
pip install requests
```


## 🛠️ Usage

python lazzy_checker.py -u https://example.com/ -w wordlist.txt

Arguments:
- -u or --url: Base URL of the target website
- -w or --wordlist: Path to the wordlist file containing endpoint candidates

Example wordlist.txt:

```
admin
login
dashboard
api/v1/users
```


## 🧪 Ideal For

- 🔐 Penetration testers and security researchers
- 🧑‍💻 Developers validating API routes
- 🛠️ Automating endpoint discovery during audits


## 🤝 Contributing
Feel free to fork the project, submit pull requests, or suggest improvements. All contributions are welcome!


## ✨ Author
Created with 💻 by [0xDevko]
