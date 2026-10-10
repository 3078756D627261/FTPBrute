# 🔐 FTPBrute - Simple FTP/FTPS Password Testing Tool

[![GitHub](https://img.shields.io/badge/github-repo-3776AB?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)
[![Protocol](https://img.shields.io/badge/Protocol-FTP%20%7C%20FTPS-00A98F?style=for-the-badge)](https://img.shields.io/)
[![OS](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black")](https://img.shields.io/)
[![LAB](https://img.shields.io/badge/Security-Lab-8A2BE2?style=for-the-badge)]("https://github.com/3078756D627261/FTPBrute/")

---

## ⚠️ Disclaimer
> [!WARNING]
> Designed for **educational purposes**, **cybersecurity labs**, and **authorized security testing** in controlled lab environments.

---

## 📌 Overview

`FTPBRUTE` is a simple Python-based tool designed to test `FTP` and `FTPS` authentication using a password wordlist. It takes a `single username` and a list of candidate passwords, attempts to authenticate against a specified server, and stops when a password is accepted. Built with Python's standard library, `FTPBRUTE` provides a straightforward introduction to `network authentication`, `FTP protocols`, and `basic security testing`.

---

## ✨ Features

| Feature | Description |
|:---|:---|
| 🔌 FTP Support | Test authentication against standard FTP servers |
| 🔐 FTPS Support | Test authentication against FTP over TLS |
| 📄 Wordlist-Based Testing | Load candidate passwords from a text file | 
| 👤 Single-Username Testing | Test multiple candidate passwords against one specified username |
| ⚙️ Command-Line Interface | Configure the `target`, `port`, `username`, `protocol`, and `wordlist` |
| 🎨 Colored Output | Display results and errors with ANSI terminal colors |
| ✅ Input Validation | Check whether the wordlist exists, is readable, and contains usable entries |
| ⏱️ Connection Timeout | Use a five-second connection timeout |
| 🛑 Stop on Success | Stop testing when a candidate password successfully authenticates |

---

## 📂 Project Structure

A suggested repository structure is:

```text
FTPBRUTE/
|
├── FTPBrute.py       # Main Python script
├── ftp_wordlist.txt  # Example password wordlist
└── README.md         # Project documentation
```

---

## ⚙️ How It Works

`FTPBRUTE` follows a straightforward process:

```text
┌──────────────────────┐
│    Parse Arguments   │
└──────────┬───────────┘
           │ 
           ▼ 
┌──────────────────────┐
│   Validate Wordlist  │
└──────────┬───────────┘ 
           │ 
           ▼
┌──────────────────────┐ 
│  Connect to FTP/FTPS │ 
└──────────┬───────────┘ 
           │ 
           ▼ 
┌──────────────────────┐ 
│     Try Candidate    │
│       Password       │
└──────────┬───────────┘ 
           │ 
           ▼
   ┌─────────────────┐ 
   │  Authentication │
   │   Successful?   │ 
   └────┬────────┬───┘ 
        │        │
       YES       NO
        │        │ 
        ▼        ▼ 
  ┌───────────┐ ┌────────────────┐ 
  │  Report   │ │    Try Next    │
  │  Success  │ │    Candidate   │ 
  └───────────┘ └───────┬────────┘ 
                        │
                        └── Repeat
```

### Process breakdown

1. Parse the command-line arguments.
2. Validate the specified port.
3. Check whether the wordlist exists, is readable, and contains usable entries.
4. Load the candidate passwords into memory.
5. Connect to the target FTP/FTPS server.
6. Attempt authentication using the specified username and each candidate password.
7. Display the authentication result or report an error.
8. Stop when authentication succeeds.

---

## 🖥️ Example Output

The following output is `illustrative`. Actual results depend on the target server and the supplied wordlist.

```text
╭──────────────────────────────────────────╮
│              FTPBRUTE v1.0               │
╰──────────────────────────────────────────╯

  Target : 192.168.1.100:21 
  Username : labuser 
  Wordlist : ftp_wordlist.txt 
  Entries : 4

[•] Starting FTP password brute-forcing for a single username...

[X] NOT FOUND: password123 
[X] NOT FOUND: admin123

[+] FOUND: labpassword
[+] Test completed successfully.
```

### Output indicators

| Indicator | Meaning |
|:---|:---|
| 🟢 `FOUND` | Authentication succeeded for a candidate password |
| 🔴 `NOT FOUND` | The server rejected a candidate with a `530` response |
| 🟡 `FTP permission/protocol error` | An FTP error occurred that was not classified as a standard login rejection |
| 🔴 `ERROR` | A connection or operating-system error occurred |

---

## 🔍 Technical Details

### FTP

FTP is a network protocol used to transfer files between a client and a server. Standard FTP does not encrypt authentication credentials or file transfers by default.

### FTPS

FTPS extends FTP with Transport Layer Security (TLS).

`FTPBRUTE` uses Python's `FTP_TLS` class and calls `prot_p()` to enable TLS protection for the data connection after authentication.

> [!IMPORTANT]
> FTPS is not the same as SFTP. SFTP uses `SSH` and is not supported by this project.

### Password wordlist

The wordlist is a plain-text file containing candidate passwords, one per line. The script removes line-ending characters and ignores blank entries before testing.

### Connection handling

The script uses a `five-second connection timeout` and attempts to close the FTP connection after each authentication attempt.

### Error Handling

`FTPBRUTE` includes basic checks and error handling for common situations:

| Indicator | Meaning |
|:---|:---|
| Missing wordlist | Reports an error if the specified file does not exist |
| Empty wordlist | Rejects an empty file or a file containing only blank lines |
| Invalid port | Rejects port numbers outside the valid range |
| Connection errors | Reports network and connection errors |
| Authentication failures | Reports rejected login attempts |
| FTP permission or protocol errors | Reports certain server responses that are not ordinary authentication failures |

---

## 🛠️ Requirements

- Python 3.6 or newer
- An FTP/FTPS server in an authorized testing environment
- A text file containing candidate passwords

> [!NOTE]
> Dependencies: No third-party Python packages are required.

`FTPBRUTE` uses built-in Python modules, including `ftplib`, `argparse`, `sys`, and `os`.

---

## 📥 Installation

### 1. Clone the repository

```text
git clone https://github.com/3078756D627261/FTPBrute.git
```

### 2. Navigate to the project directory

```text
cd FTPBRUTE
```

### 3. Verify Python is installed

```text
python3 --version
```

### 4. Prepare a password wordlist

Create a file named `ftp_wordlist.txt` in the project directory.

Example:

```text
password123
admin123
labpassword
test123
```

Each line should contain one candidate password.

You can also specify an existing wordlist using the `-w` or `--wordlist` option.

---

## 🚀 Usage

### Basic usage

```text
python3 ftpbrute.py
```

By default, `FTPBRUTE` uses the following configuration:

| Parameter | Default |
|:---|:---|
| Protocol | `FTP` |
| Target | `192.168.1.1` |
| Port | `21` |
| Username | `root` |
| Wordlist | `ftp_wordlist.txt` |

Make sure the target and wordlist match your authorized lab environment.

### Command-line arguments

| Argument | Description | Default |
|:---|:---|:---|
| `-m`, `--mode` | Protocol: `FTP` or `FTPS` | `FTP` |
| `-t`, `--target` | Target hostname or IP address | `192.168.1.1` |
| `-p`, `--port` | Target server port | `21` |
| `-u`, `--username` | Username to test | `root` |
| `-w`, `--wordlist` | Path to the password wordlist | `ftp_wordlist.txt` |
| `-h`, `--help` | Display the help menu | — |

### Example: FTP

```text
python3 ftpbrute.py --mode FTP --target 192.168.1.100 --port 21 --username labuser --wordlist ftp_wordlist.txt
```

### Example: FTPS

```text
python3 ftpbrute.py --mode FTPS --target 192.168.1.100 --port 21 --username labuser --wordlist ftp_wordlist.txt
```

### Example: Custom wordlist

```text
python3 ftpbrute.py --target 192.168.1.100 --username labuser --wordlist /path/to/passwords.txt
```

 > [!NOTE]
> The script defaults to FTP if you do not specify `--mode`.

---

## ⚠️ Limitations

`FTPBRUTE` is a basic educational implementation and has several limitations:

- Supports only one username per execution.
- Loads the entire wordlist into memory.
- Does not implement parallel authentication attempts.
- Does not provide configurable `retry limits` or `rate limiting`.
- May encounter server-side restrictions, `account lockouts`, or `connection throttling`.
- Does not distinguish every possible login failure from other server restrictions.
- Does not explicitly configure FTPS certificate verification.
- Does not provide detailed logging or export results to a file.
- May return an inconclusive result if the wordlist is exhausted without a successful login.

---

## 🔒 Security Considerations

- Use this tool only against `FTP/FTPS` servers that you `own` or have `explicit permission` to test.
- Repeated authentication attempts can trigger `account lockouts`, `intrusion detection alerts`, `rate limits`, or other defensive mechanisms.
- For defensive testing, consider using a dedicated lab account and a test server configured specifically for this purpose.
- When administering a real FTP service, prefer `secure authentication practices`,` strong unique passwords`, `account lockout` or `rate-limiting` controls, and `encrypted protocols`.
