# RedReaper 🩸

**RedReaper** is an automated Red Team adversary simulation framework designed to simulate real-world attack techniques in a lab or controlled environment.

> ⚠️ For educational and ethical hacking purposes only.

## 🔥 Features

- 🎯 Simulates real-world Red Team kill chain phases
- 🔍 Recon module (mocked subdomain enumeration)
- 🐚 Reverse shell payload generator
- 🛠️ Configurable via JSON
- 📦 Modular structure – easy to expand with new attack modules

## 🧠 Simulated Stages

1. Reconnaissance (subdomain scan)
2. Payload generation (Python reverse shell)
3. Ready for extension: C2, privilege escalation, lateral movement, exfiltration

## 📂 Project Structure

```
RedReaper/
├── config/
│   └── settings.json         # Simulation config
├── payloads/
│   └── reverse_shell.py      # Generated payload
├── RedReaper.py              # Main framework file
├── README.md
└── requirements.txt
```

## ▶️ Usage

```bash
python3 RedReaper.py
```

Modify `settings.json` to set:
- Target domain for recon
- IP and port for C2 callback

## 💻 Requirements

- Python 3.7+
- Works on Linux, Windows, macOS

## 🧪 Author

Created by ZeroTrace as part of an offensive security portfolio.
