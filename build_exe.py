import PyInstaller.__main__
import os
import sys
from pathlib import Path

def build_exe():
    # 获取当前目录
    current_dir = Path(__file__).parent.absolute()
    
    # 设置图标路径（如果有的话）
    # icon_path = os.path.join(current_dir, "assets", "icon.ico")
    
    # PyInstaller参数
    params = [
        "edutools/gui/main_app.py",  # 主程序入口
        "--name=EduTools",  # 生成的exe名称
        "--noconsole",  # 不显示控制台窗口
        # "--icon=" + icon_path,  # 程序图标
        "--noconfirm",  # 覆盖已存在的文件
        "--clean",  # 清理临时文件
        "--add-data=edutools/core/essay;edutools/core/essay",  # 添加额外的数据文件
        "--hidden-import=openai",
        "--hidden-import=tkinter",
        "--hidden-import=json",
        "--hidden-import=queue",
        "--hidden-import=threading",
        "--paths=" + str(current_dir),  # 添加搜索路径
    ]
    
    # 运行PyInstaller
    PyInstaller.__main__.run(params)
    
    print("打包完成！")
    print(f"可执行文件位置: {os.path.join(current_dir, 'dist', 'EduTools', 'EduTools.exe')}")

if __name__ == "__main__":
    build_exe() 