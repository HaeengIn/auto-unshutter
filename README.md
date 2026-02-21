# auto-unshutter
Python Script to Automatically Disable Shutter Sound for Samsung Galaxy

## Test Environment
- `<Android Version> / <One UI Version>`
- Android 16 / One UI 8.0

## Installation (For General Users)
Visit [Latest Release Page](https://github.com/HaeengIn/auto-unshutter/releases/latest) and download `.exe` file.

## Installation (For Developers)
- Bash

    ```bash
    git clone https://github.com/HaeengIn/auto-noshutter \
    cd auto-noshutter \
    pip install -r requirements.txt
    ```

## Pyinstaller Command
```bash
pyinstaller --onefile \
--icon=icon.ico \
--version-file=version.txt \
--hidden-import=ppadb.client \
--hidden-import=ppadb.device \
--add-binary "platform-tools/adb.exe:platform-tools" \
--add-binary "platform-tools/AdbWinApi.dll:platform-tools" \
--add-binary "platform-tools/AdbWinUsbApi.dll:platform-tools" \
main.py
```

## How to use
1. Enable Developer Setting on your phone.
2. Enable USE Debugging.
3. Connect your PC and phone.
4. Run the `.exe` file.