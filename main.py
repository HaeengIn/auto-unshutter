import os, sys, time, subprocess
from ppadb.client import Client as AdbClient

COMMAND = "settings put system csc_pref_camera_forced_shuttersound_key 0"

def get_runtime_base_path():
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def get_adb_path():
    base_path = get_runtime_base_path()
    return os.path.join(base_path, "platform-tools", "adb.exe")

def start_adb_server(adb_path):
    try:
        subprocess.run(
            [adb_path, "start-server"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print("ADB 서버 시작 실패:", e)

def wait_for_adb_server(timeout=10):
    client = AdbClient(host="127.0.0.1", port=5037)
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            client.devices()
            return client
        except Exception:
            time.sleep(1)

    raise RuntimeError("ADB 서버 연결 실패")

def main():
    adb_path = get_adb_path()

    if not os.path.exists(adb_path):
        print("내부 adb 실행 파일을 찾을 수 없습니다.")
        return

    print("ADB 서버 시작...")
    start_adb_server(adb_path)

    print("ADB 준비 대기...")
    try:
        client = wait_for_adb_server()
    except RuntimeError as e:
        print(e)
        return

    print("기기 연결 대기 중...")

    executed_devices = set()

    while True:
        try:
            devices = client.devices()
            current_serials = set(d.serial for d in devices)

            for device in devices:
                if device.serial not in executed_devices:
                    print(f"기기 연결 감지: {device.serial}")
                    try:
                        device.shell(COMMAND)
                        print("명령 실행 완료")
                        executed_devices.add(device.serial)
                    except Exception as e:
                        print("명령 실행 실패:", e)

            executed_devices &= current_serials

        except Exception:
            # ADB 통신 오류 시 서버 재시작 시도
            start_adb_server(adb_path)

        time.sleep(2)

if __name__ == "__main__":
    main()