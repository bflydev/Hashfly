<p align="center">
  <img src="hashfly/icon.ico" alt="Hashfly logo" width="160">
</p>

<h1 align="center">Hashfly</h1>

<p align="center"><strong>A lightweight, easy-to-use hash checker for large datasets with a clean mirrored file structure.</strong></p>

---

Hashfly is a portable desktop utility. You drop the `.exe` anywhere in your OS folders, and it automatically creates a `hashes` folder right beside itself. It then recursively routes through all other folders, mirroring every directory and file it comes across, and generates a SHA-256 hash text file for every single file it finds.

> **Portable & Lightweight.** No installation or Python required—just drop and run.

## Features

| | |
|---|---|
| **Mirrored file structure** | Automatically replicates your exact directory tree for intuitive navigation |
| **SHA-256 generation** | Converts every file name into a `.txt` file containing its unique cryptographic SHA-256 hash |
| **Zero installation** | Standalone executable (`.exe`) that runs instantly anywhere on your system |
| **Background execution** | Runs silently without unnecessary console windows cluttering your workspace |
| **Self-excluding logic** | Intelligently ignores its own destination directory and execution path during traversal |

## Requirements

- **Windows 11** (or compatible Windows environment)
- No Python runtime required for end users (bundled via PyInstaller)

## Usage

1. **Download** `hashfly.exe` from the [latest release](https://github.com/YOUR_USERNAME/Hashfly/releases/latest).
2. **Place** the `.exe` inside any base directory or folder you want to scan and audit.
3. **Run** `hashfly.exe`. It will instantly generate a `hashes/` directory mirroring your subfolders and text files containing the SHA-256 hashes.

> **A foreword on security queries.** If your antivirus or Windows SmartScreen flags the executable, it is a known false positive common to PyInstaller-bundled scripts. You can inspect the source code yourself or compile it from source using the instructions below if you prefer complete security.

## LICENSE 
**GPL-3.0** — see [`LICENSE`](LICENSE). Free to use, change and share, but any copy or modified version must also stay free and open source under the same licence.

## Build from source

Needs **Python 3.10+** and **PyInstaller**.

```bash
git clone [https://github.com/YOUR_USERNAME/Hashfly.git](https://github.com/YOUR_USERNAME/Hashfly.git)
pip install pyinstaller
pyinstaller --onefile --noconsole --icon="PATHTOYOURicon.ico" "PATHTOYOURhashfly.py"
