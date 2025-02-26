import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import json
import time
import sys

# 添加父目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from edutools.core.essay.analyzer import EssayAnalyzer

class EssayAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("智能作文分析工具")
        self.root.geometry("1000x900")
        
        # 配置参数
        self.api_key = "your-api-key-here"  # 需要用户配置
        self.base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # 可选，用于配置不同的API端点
        self.analyzer = EssayAnalyzer(self.api_key, self.base_url)
        self.base_dir = "作文记录"
        
        # 创建界面组件
        self.create_widgets()
        self.setup_layout()
        
        # 创建存储目录
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_widgets(self):
        # 输入面板
        self.input_frame = ttk.LabelFrame(self.root, text="作文输入")
        self.author_label = ttk.Label(self.input_frame, text="作者姓名:")
        self.author_entry = ttk.Entry(self.input_frame, width=20)
        self.title_label = ttk.Label(self.input_frame, text="文章标题:")
        self.title_entry = ttk.Entry(self.input_frame, width=30)
        self.standard_label = ttk.Label(self.input_frame, text="评判标准:")
        self.standard_combo = ttk.Combobox(self.input_frame, values=list(self.analyzer.get_preset_standards().keys()))
        self.custom_standard_entry = ttk.Entry(self.input_frame, width=40)
        self.content_label = ttk.Label(self.input_frame, text="作文内容:")
        self.content_text = tk.Text(self.input_frame, height=12, width=85)
        self.content_text.configure(font=("微软雅黑", 11))
        self.open_file_btn = ttk.Button(self.input_frame, text="打开文件", command=self.load_file)
        
        # 实时分析输出面板
        self.stream_frame = ttk.LabelFrame(self.root, text="AI思考过程")
        self.toggle_stream_btn = ttk.Button(self.root, text="折叠/展开思考过程", command=self.toggle_stream)
        self.stream_text = tk.Text(self.stream_frame, height=8, width=85)
        self.stream_text.config(state=tk.DISABLED)
        self.stream_text.configure(font=("微软雅黑", 11))
        self.is_stream_collapsed = False
        
        # 分析面板
        self.analysis_frame = ttk.LabelFrame(self.root, text="最终分析结果")
        self.score_label = ttk.Label(self.analysis_frame, text="当前得分: ", font=("微软雅黑", 12, "bold"))
        self.analysis_text = tk.Text(self.analysis_frame, height=12, width=85, state=tk.DISABLED)
        self.analysis_text.configure(font=("微软雅黑", 11))
        
        # 添加分析按钮
        self.analyze_btn = ttk.Button(self.input_frame, text="开始分析", command=self.analyze_essay)
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)

    def setup_layout(self):
        # 输入面板布局
        self.input_frame.pack(pady=10, fill=tk.X)
        self.author_label.grid(row=0, column=0, padx=5, pady=2)
        self.author_entry.grid(row=0, column=1, padx=5, pady=2)
        self.title_label.grid(row=0, column=2, padx=5, pady=2)
        self.title_entry.grid(row=0, column=3, padx=5, pady=2)
        self.standard_label.grid(row=1, column=0, padx=5, pady=2)
        self.standard_combo.grid(row=1, column=1, padx=5, pady=2)
        self.custom_standard_entry.grid(row=1, column=3, padx=5, pady=2)
        self.content_label.grid(row=2, column=0, padx=5, pady=2)
        self.content_text.grid(row=3, column=0, columnspan=4, padx=5, pady=2)
        self.open_file_btn.grid(row=4, column=0, padx=5, pady=5)
        self.analyze_btn.grid(row=4, column=3, padx=5, pady=5)
        
        # 实时输出面板布局
        self.toggle_stream_btn.pack(pady=2)
        self.stream_frame.pack(pady=5, fill=tk.BOTH)
        self.stream_text.pack(pady=5, fill=tk.BOTH)
        
        # 分析面板布局
        self.analysis_frame.pack(pady=5, fill=tk.BOTH, expand=True)
        self.score_label.pack(pady=5)
        self.analysis_text.pack(pady=5, fill=tk.BOTH, expand=True)
        
        # 状态栏
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.content_text.delete(1.0, tk.END)
                self.content_text.insert(tk.END, f.read())

    def get_standard(self):
        selected = self.standard_combo.get()
        if selected:
            return self.analyzer.get_preset_standards()[selected]
        return self.custom_standard_entry.get()

    def update_stream_text(self, text):
        self.stream_text.config(state=tk.NORMAL)
        self.stream_text.insert(tk.END, text)
        self.stream_text.see(tk.END)
        self.stream_text.config(state=tk.DISABLED)
        self.root.update()

    def clear_stream_text(self):
        self.stream_text.config(state=tk.NORMAL)
        self.stream_text.delete(1.0, tk.END)
        self.stream_text.config(state=tk.DISABLED)

    def analyze_essay(self):
        # 获取输入内容
        author = self.author_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get(1.0, tk.END).strip()
        standard = self.get_standard()
        
        # 输入验证
        if not author or not content:
            messagebox.showerror("错误", "作者姓名和作文内容不能为空")
            return
        
        # 清空实时输出
        self.clear_stream_text()
        self.status_var.set("正在分析中...")
        self.root.update()

        try:
            result = self.analyzer.analyze_essay(content, title, standard)
            self.show_analysis(result)
            self.save_record(author, title, content, result)
            # 分析完成后自动折叠思考过程面板
            self.root.after(1000, self.toggle_stream)
            
        except Exception as e:
            messagebox.showerror("API错误", f"分析失败: {str(e)}")
        finally:
            self.status_var.set("就绪")

    def toggle_stream(self):
        if self.is_stream_collapsed:
            self.stream_frame.pack(pady=5, fill=tk.BOTH)
            self.is_stream_collapsed = False
        else:
            self.stream_frame.pack_forget()
            self.is_stream_collapsed = True

    def show_analysis(self, result):
        self.score_label.config(text=f"当前得分: {result['score']}/100")
        
        analysis_str = "【分析结果】\n\n"
        analysis_str += "【优点】\n"
        analysis_str += "\n".join(f"✓ {s}" for s in result["strengths"])
        analysis_str += "\n\n【不足】\n"
        analysis_str += "\n".join(f"✗ {w}" for w in result["weaknesses"])
        analysis_str += "\n\n【建议】\n"
        analysis_str += "\n".join(f"▶ {sg}" for sg in result["suggestions"])
        
        self.analysis_text.config(state=tk.NORMAL)
        self.analysis_text.delete(1.0, tk.END)
        self.analysis_text.insert(tk.END, analysis_str)
        self.analysis_text.config(state=tk.DISABLED)

    def save_record(self, author, title, content, result):
        # 创建作者目录
        author_dir = os.path.join(self.base_dir, author)
        if not os.path.exists(author_dir):
            os.makedirs(author_dir)
        
        # 生成文件名
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        safe_title = "".join([c if c.isalnum() else "_" for c in title])
        filename = f"{timestamp}_{safe_title}.json"
        
        # 保存记录
        record = {
            "meta": {
                "author": author,
                "title": title,
                "timestamp": timestamp,
                "score": result["score"]
            },
            "content": content,
            "analysis": result
        }
        
        with open(os.path.join(author_dir, filename), 'w', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=False, indent=2)

def main():
    root = tk.Tk()
    app = EssayAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 