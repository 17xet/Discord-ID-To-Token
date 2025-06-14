Discord ID To Token

> ⚠️ **Disclaimer**: This project is intended strictly for educational purposes only. Do **not** use this tool against any real user or service. Doing so may result in violation of terms of service and legal action. You are fully responsible for how you use this code.

A Python-based tool that simulates brute-forcing part of a Discord token structure to demonstrate how the token format works and how APIs respond to malformed or guessed tokens.

![Screenshot 2025-06-15 013825](https://github.com/user-attachments/assets/8371f21a-a8f7-46e0-8652-ecb6afcbc5de)

---

## 🎨 Features

- ASCII art styled terminal UI
- Base64 encoding of Discord user IDs to simulate the first part of a token
- Random generation of token parts to simulate brute force attempts
- Webhook integration for logging valid token formats (simulated)
- Multi-threaded execution for speed

---

## 🛠️ Requirements

- Python 3.7+
- pip packages:
  - `pystyle`
  - `requests`

Install dependencies with:

```bash
pip install pystyle requests
````

---

## 🚀 Usage

```bash
python token_brute.py
```

You will be prompted for:

* Victim ID (used to generate the base64-encoded first part)
* Whether to simulate brute forcing the second part
* Whether to use a webhook for logging results
* Number of threads to use for the simulation

---

## ⚙️ Example Output

```
[INFO] 15:43:21 [END] [INFO] Victim ID -> 123456789
[INFO] 15:43:22 [END] [INFO] Part One Token: MTIzNDU2Nzg5
[INFO] 15:43:23 [END] [INFO] Token: MTIzNDU2Nzg5.GHjkLx.asdfg1234567...
[VALID] Status: Valid   Token: <simulated>
```

---

## ❗ Legal & Ethical Notice

This repository does **not** encourage hacking or brute-forcing accounts. Discord token brute-forcing is illegal and unethical. This tool is only meant to show how insecure token usage can be, and how attackers might abuse exposed user IDs or tokens. **Always get consent when running any form of penetration test.**

---

## 📜 License

This project is provided under the MIT License for educational purposes only. Misuse of this code is strictly forbidden.

---

## 📞 Contact

For educational or research inquiries, reach out via GitHub or my Discord.

````

---
