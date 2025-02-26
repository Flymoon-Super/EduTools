import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from edutools.gui.math_quiz_app import MathQuizApp
from edutools.gui.essay_analyzer_app import EssayAnalyzerApp
from edutools.gui.settings_dialog import SettingsDialog
from edutools.core.config import Config

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("教育工具集")
        self.root.geometry("400x400")  # 增加高度以适应用户选择
        
        # 加载配置
        self.config = Config()
        
        # 设置窗口样式
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('微软雅黑', 12))
        
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="欢迎使用教育工具集", font=('微软雅黑', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=20)
        
        # 用户选择框架
        user_frame = ttk.Frame(main_frame)
        user_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(user_frame, text="当前用户:", font=('微软雅黑', 10)).grid(row=0, column=0, padx=5)
        
        # 用户选择下拉框
        self.user_var = tk.StringVar(value=self.config.get_config('current_user'))
        self.user_combo = ttk.Combobox(user_frame, textvariable=self.user_var, width=15)
        self.user_combo['values'] = self.config.get_config('users')
        self.user_combo.grid(row=0, column=1, padx=5)
        
        # 添加用户按钮
        add_user_btn = ttk.Button(user_frame, text="+", width=3, command=self.add_user)
        add_user_btn.grid(row=0, column=2, padx=5)
        
        # 数学练习按钮
        math_btn = ttk.Button(main_frame, text="数学题练习", command=self.open_math_quiz)
        math_btn.grid(row=2, column=0, pady=10, padx=50, sticky=(tk.W, tk.E))
        
        # 作文分析按钮
        essay_btn = ttk.Button(main_frame, text="作文分析工具", command=self.open_essay_analyzer)
        essay_btn.grid(row=3, column=0, pady=10, padx=50, sticky=(tk.W, tk.E))
        
        # 设置按钮
        settings_btn = ttk.Button(main_frame, text="设置", command=self.open_settings)
        settings_btn.grid(row=4, column=0, pady=10, padx=50, sticky=(tk.W, tk.E))
        
        # 配置列权重以实现居中
        main_frame.columnconfigure(0, weight=1)
        user_frame.columnconfigure(1, weight=1)
        
        # 绑定用户选择事件
        self.user_combo.bind('<<ComboboxSelected>>', self.on_user_selected)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # 处理窗口关闭事件
        
    def add_user(self):
        new_user = self.user_var.get().strip()
        if not new_user:
            messagebox.showerror("错误", "请输入用户名")
            return
            
        self.config.add_user(new_user)
        self.config.update_config('current_user', new_user)
        
        # 更新下拉框
        self.user_combo['values'] = self.config.get_config('users')
        self.user_combo.set(new_user)
    
    def on_user_selected(self, event):
        selected_user = self.user_var.get()
        self.config.update_config('current_user', selected_user)
        
    def open_math_quiz(self):
        if not self.check_user():
            return
        math_window = tk.Toplevel(self.root)
        math_window.protocol("WM_DELETE_WINDOW", lambda: self.on_tool_closing(math_window))
        math_app = MathQuizApp(math_window)
        
    def open_essay_analyzer(self):
        if not self.check_user():
            return
        essay_window = tk.Toplevel(self.root)
        essay_window.protocol("WM_DELETE_WINDOW", lambda: self.on_tool_closing(essay_window))
        essay_app = EssayAnalyzerApp(essay_window)
    
    def check_user(self):
        """检查是否选择了用户"""
        if not self.user_var.get().strip():
            messagebox.showerror("错误", "请先选择或添加用户")
            return False
        return True
    
    def open_settings(self):
        SettingsDialog(self.root)
    
    def on_tool_closing(self, window):
        window.destroy()
    
    def on_closing(self):
        self.root.quit()
        self.root.destroy()
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run() 