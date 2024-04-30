import os
import locale
import platform

# 로거 이름
LOGGER_NAME = 'rltrader'

# 경로 설정
BASE_DIR = os.environ.get('RLTRADER_BASE', 
    os.path.abspath(os.path.join(__file__, os.path.pardir, os.path.pardir, os.path.pardir, os.path.pardir)))

# 로케일 설정
if 'COLAB_GPU' in os.environ:  # Check if running on Google Colab
    print("Running in Google Colab; Locale setting is skipped.")
elif 'Linux' in platform.system() or 'Darwin' in platform.system():
    try:
        locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
    except locale.Error:
        print("Locale 'ko_KR.UTF-8' is not supported. Falling back to default.")
elif 'Windows' in platform.system():
    locale.setlocale(locale.LC_ALL, '')
