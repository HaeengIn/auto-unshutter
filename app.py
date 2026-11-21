import os
import subprocess
import sys

BASE_DIR: str = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
ADB_PATH: str = os.path.join(BASE_DIR, "platform-tools", "adb.exe")


def RunAdb(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [ADB_PATH, *args],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(ADB_PATH),
        check=False,
    )


def WaitAnyKey() -> None:
    import msvcrt

    print("아무 키나 눌러 종료하세요...")
    msvcrt.getch()


def main() -> None:
    try:
        RunAdb("start-server")
        devices: list[str] = RunAdb("devices").stdout.splitlines()[1:]
        connected: list[str] = [
            line for line in devices if line.strip().endswith("device")
        ]
        if not connected:
            print("연결된 기기가 없습니다. USB 디버깅과 케이블을 확인하세요.")
            return
        result: subprocess.CompletedProcess[str] = RunAdb(
            "shell",
            "settings",
            "put",
            "system",
            "csc_pref_camera_forced_shuttersound_key",
            "0",
        )
        print(result.stderr.strip() or "카메라 셔터음 강제 설정이 해제되었습니다.")
    finally:
        RunAdb("kill-server")
        WaitAnyKey()


if __name__ == "__main__":
    main()
