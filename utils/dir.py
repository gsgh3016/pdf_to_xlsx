import os


def check_dir(dir_path: str) -> None:
    print(f"{dir_path} 디렉토리 확인 중")
    try:
        if not os.path.exists(dir_path):
            print(f"{dir_path}가 존재하지 않습니다. 디렉토리를 생성합니다.")
            os.makedirs(dir_path)
    except:
        raise FileExistsError(f"{dir_path} 디렉토리를 확인하는데 문제가 생겼습니다.")
        
        
def scan_files(dir_path: str, file_type: str) -> list[str]:
    print(f"{dir_path} 경로에 있는 {file_type} 파일을 스캔합니다.")
    scanned_files = []
    try:
        files = os.listdir(dir_path)
        for file in files:
            if os.path.splitext(file)[1] == "." + file_type:
                scanned_files.append(os.path.join(dir_path, file))
        return scanned_files
    except:
        raise InterruptedError(f"{dir_path} 디렉토리 내부를 스캔하는데 실패했습니다.")