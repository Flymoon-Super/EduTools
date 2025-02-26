import tkinter as tk
from tkinter import ttk, filedialog
from edutools.core.config import Config

class SettingsDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("设置")
        self.dialog.geometry("500x400")
        self.dialog.transient(parent)  # 设置为父窗口的临时窗口
        self.dialog.grab_set()  # 模态对话框
        
        self.config = Config()
        
        # 创建主框架
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # OpenAI 设置
        openai_frame = ttk.LabelFrame(main_frame, text="OpenAI 设置", padding="10")
        openai_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # API Key
        ttk.Label(openai_frame, text="API Key:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.api_key_var = tk.StringVar(value=self.config.get_config('openai')['api_key'])
        self.api_key_entry = ttk.Entry(openai_frame, textvariable=self.api_key_var, width=40, show="*")
        self.api_key_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # API Base URL
        ttk.Label(openai_frame, text="API Base URL:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.api_base_var = tk.StringVar(value=self.config.get_config('openai')['api_base'])
        self.api_base_entry = ttk.Entry(openai_frame, textvariable=self.api_base_var, width=40)
        self.api_base_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # 输出路径设置
        output_frame = ttk.LabelFrame(main_frame, text="输出路径设置", padding="10")
        output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        ttk.Label(output_frame, text="输出根目录:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.output_path_var = tk.StringVar(value=self.config.get_config('output_path'))
        self.output_path_entry = ttk.Entry(output_frame, textvariable=self.output_path_var, width=40)
        self.output_path_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        
        browse_btn = ttk.Button(output_frame, text="浏览", command=self.browse_output_path)
        browse_btn.grid(row=0, column=2, padx=5)
        
        # 按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, sticky=(tk.E), pady=20)
        
        # 保存按钮
        save_btn = ttk.Button(button_frame, text="保存", command=self.save_settings)
        save_btn.grid(row=0, column=0, padx=5)
        
        # 取消按钮
        cancel_btn = ttk.Button(button_frame, text="取消", command=self.dialog.destroy)
        cancel_btn.grid(row=0, column=1, padx=5)
        
        # 配置网格权重
        self.dialog.columnconfigure(0, weight=1)
        self.dialog.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        openai_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(1, weight=1)
    
    def browse_output_path(self):
        path = filedialog.askdirectory(initialdir=self.output_path_var.get())
        if path:
            self.output_path_var.set(path)
        
    def save_settings(self):
        # 保存OpenAI设置
        openai_config = {
            'api_key': self.api_key_var.get(),
            'api_base': self.api_base_var.get()
        }
        self.config.update_config('openai', openai_config)
        
        # 保存输出路径
        self.config.update_config('output_path', self.output_path_var.get())
        
        self.dialog.destroy() 