import os
import re

def find_files_with_insecure_var_declarations(start_path):
    # 변수 선언 패턴을 찾기 위한 정규 표현식
    var_pattern = re.compile(r'\b(user|password)\b\s*=\s*["\'][^"\']+["\']')
    # os.environ 사용 패턴
    env_pattern = re.compile(r'os\.environ')

    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith('.py'):  # Python 파일만 확인
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        content = f.read()
                        # 변수 선언이 있는지 확인
                        if var_pattern.search(content) and not env_pattern.search(content):
                            print(f"Insecure variable declaration found in: {file_path}")
                    except UnicodeDecodeError:
                        print(f"Error reading file: {file_path}")

# 시작 디렉토리 경로를 설정하세요 (예: '/path/to/your/project')
start_directory = '/home/cdsw'
find_files_with_insecure_var_declarations(start_directory)