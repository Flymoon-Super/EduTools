import tkinter as tk
from tkinter import ttk, messagebox
import time
import sys
import os

# 添加父目录到系统路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from edutools.core.math.question_generator import MathQuestionGenerator

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("数学题练习工具")
        self.root.geometry("500x450")
        
        # 配置变量
        self.total_questions = 10
        self.current_question = 0
        self.score = 0
        self.start_time = 0
        self.quiz_data = []
        self.question_generator = MathQuestionGenerator()
        
        # 创建界面组件
        self.create_widgets()
        self.setup_layout()
    
    def create_widgets(self):
        # 控制面板
        self.control_frame = ttk.LabelFrame(self.root, text="控制")
        self.num_questions_label = ttk.Label(self.control_frame, text="题目数量:")
        self.num_questions = ttk.Spinbox(self.control_frame, from_=5, to=50, width=5)
        self.num_questions.set(10)
        
        # 添加题目类型选择
        self.question_type_label = ttk.Label(self.control_frame, text="题目类型:")
        self.question_type = ttk.Combobox(self.control_frame, width=20)
        self.question_type['values'] = [
            "基础运算(加减乘除)",
            "连加减混合",
            "进位加法",
            "退位减法"
        ]
        self.question_type.set("基础运算(加减乘除)")
        
        self.start_btn = ttk.Button(self.control_frame, text="开始练习", command=self.start_quiz)
        
        # 题目面板
        self.question_frame = ttk.LabelFrame(self.root, text="题目")
        self.question_label = ttk.Label(self.question_frame, text="点击开始按钮开始练习", font=('Arial', 24))
        self.answer_entry = ttk.Entry(self.question_frame, width=20, font=('Arial', 20))
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        self.submit_btn = ttk.Button(self.question_frame, text="提交答案", state=tk.DISABLED, command=self.check_answer)
        
        # 统计面板
        self.stats_frame = ttk.LabelFrame(self.root, text="统计信息")
        self.stats_text = tk.Text(self.stats_frame, height=10, width=50, state=tk.DISABLED)
        self.scrollbar = ttk.Scrollbar(self.stats_frame, orient=tk.VERTICAL, command=self.stats_text.yview)
        self.stats_text.configure(yscrollcommand=self.scrollbar.set)
    
    def setup_layout(self):
        # 控制面板布局
        self.control_frame.pack(pady=10, fill=tk.X)
        self.num_questions_label.grid(row=0, column=0, padx=5)
        self.num_questions.grid(row=0, column=1, padx=5)
        self.question_type_label.grid(row=0, column=2, padx=5)
        self.question_type.grid(row=0, column=3, padx=5)
        self.start_btn.grid(row=0, column=4, padx=5)
        
        # 题目面板布局
        self.question_frame.pack(pady=10, fill=tk.X)
        self.question_label.pack(pady=10)
        self.answer_entry.pack(pady=5)
        self.submit_btn.pack(pady=5)
        
        # 统计面板布局
        self.stats_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        self.stats_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def generate_question(self):
        question_type = self.question_type.get()
        
        if question_type == "基础运算(加减乘除)":
            return self.question_generator.generate_basic_question()
        elif question_type == "连加减混合":
            return self.question_generator.generate_mixed_addition_subtraction()
        elif question_type == "进位加法":
            return self.question_generator.generate_carry_addition()
        elif question_type == "退位减法":
            return self.question_generator.generate_borrow_subtraction()
    
    def start_quiz(self):
        try:
            self.total_questions = int(self.num_questions.get())
            if self.total_questions < 1:
                raise ValueError
        except:
            messagebox.showerror("错误", "请输入有效的题目数量")
            return
        
        self.current_question = 0
        self.score = 0
        self.quiz_data = []
        self.start_time = time.time()
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.DISABLED)
        self.submit_btn.config(state=tk.NORMAL)
        self.answer_entry.config(state=tk.NORMAL)
        self.answer_entry.focus()
        self.next_question()
    
    def next_question(self):
        if self.current_question < self.total_questions:
            question, answer = self.generate_question()
            self.current_question += 1
            self.quiz_data.append({
                "question": question,
                "correct_answer": answer,
                "user_answer": None,
                "is_correct": False
            })
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
            self.root.title(f"数学题练习工具 - 第 {self.current_question}/{self.total_questions} 题")
        else:
            self.end_quiz()
    
    def check_answer(self):
        try:
            user_answer = float(self.answer_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")
            return
        
        current_data = self.quiz_data[-1]
        current_data["user_answer"] = user_answer
        correct = round(current_data["correct_answer"], 2) == round(user_answer, 2)
        
        if correct:
            self.score += 1
        
        current_data["is_correct"] = correct
        self.next_question()
        self.answer_entry.focus()
    
    def end_quiz(self):
        total_time = round(time.time() - self.start_time, 2)
        self.submit_btn.config(state=tk.DISABLED)
        self.answer_entry.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)
        
        # 显示统计信息
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.insert(tk.END, f"练习完成！总得分：{self.score}/{self.total_questions}\n")
        self.stats_text.insert(tk.END, f"总用时：{total_time} 秒\n\n详细结果：\n")
        
        for idx, data in enumerate(self.quiz_data, 1):
            result = "正确" if data["is_correct"] else "错误"
            self.stats_text.insert(tk.END, 
                f"{idx}. {data['question']}\n"
                f"   你的答案：{data['user_answer']} | 正确答案：{data['correct_answer']} ({result})\n\n")
        
        self.stats_text.config(state=tk.DISABLED)
        self.root.title("数学题练习工具")

def main():
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 