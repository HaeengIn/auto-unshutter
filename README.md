# auto-unshutter
Python Script to Automatically Disable Shutter Sound for Samsung Galaxy

## Test Environment
- `<Android Version> / <One UI Version>`
- Android 16 / One UI 8.0

## Installation
Visit [Latest Release Page](https://github.com/HaeengIn/auto-unshutter/releases/latest) and download `.exe` file.

## Contribute
1. Clone repository
    ```bash
    git clone https://github.com/HaeengIn/auto-unshutter && cd auto-unshutter
    ```
2. Install pyinstaller
    ```bash
    uv sync
    ```

## Pyinstaller Command
```bash
pyinstaller --onefile --icon=icon.ico --version-file=version.txt --name auto-unshutter --add-data "platform-tools/adb.exe:platform-tools" --add-data "platform-tools/AdbWinApi.dll:platform-tools" --add-data "platform-tools/AdbWinUsbApi.dll:platform-tools" --add-data "licenses:licenses" app.py
```

## How to use
1. Enable Developer Setting on your phone.
2. Enable USB Debugging.
3. Connect your PC and phone.
4. Allow USB Debugging.
5. Run the `.exe` file.