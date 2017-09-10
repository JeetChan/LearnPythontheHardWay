e:
cd E:\Learn\Python\virtualenv
mkdir py3_t
cd py3_t
# 指定 Python 版本，不依赖系统环境库，创建虚拟环境
virtualenv -p D:\Program\WinPython-64bit-3.6.1.0Qt5\python-3.6.1.amd64\python.exe --no-site-packages ENV
cd E:\Learn\Python\virtualenv\py3_t\ENV\Scripts
激活虚拟环境
activate
pip install -r requirements.txt
cd E:\Program\sqlite-tools-win32-x86-3200100
# 进入 sqlite3 命令行工具
sqlite3
# 创建数据库文件
.open E:\\Learn\\Python\\flask-sqlite\\app\\test.db
# 关闭虚拟环境
deactivate