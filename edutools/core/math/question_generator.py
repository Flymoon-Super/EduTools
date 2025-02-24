import random

class MathQuestionGenerator:
    @staticmethod
    def generate_basic_question():
        operators = ['+', '-', '×', '÷']
        operator = random.choice(operators)
        
        if operator == '+':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            answer = num1 + num2
        elif operator == '-':
            num1 = random.randint(1, 20)
            num2 = random.randint(1, num1)  # 确保结果非负
            answer = num1 - num2
        elif operator == '×':
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)  # 乘法口诀表范围
            answer = num1 * num2
        else:  # 除法
            num2 = random.randint(1, 9)
            num1 = num2 * random.randint(1, 9)  # 确保能整除
            answer = num1 // num2
            
        return f"{num1} {operator} {num2} = ?", answer
    
    @staticmethod
    def generate_mixed_addition_subtraction():
        operators = ['+', '-']
        op1 = random.choice(operators)
        op2 = random.choice(operators)
        
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 20)
        
        if op1 == '+':
            temp = num1 + num2
        else:
            if num1 < num2:  # 确保中间结果非负
                num1, num2 = num2, num1
            temp = num1 - num2
            
        if op2 == '+':
            answer = temp + num3
        else:
            if temp < num3:  # 如果最终结果可能为负，调整num3
                num3 = random.randint(1, temp)
            answer = temp - num3
            
        return f"{num1} {op1} {num2} {op2} {num3} = ?", answer
    
    @staticmethod
    def generate_carry_addition():
        num1 = random.randint(1, 99)
        ones1 = num1 % 10
        ones2 = random.randint(10 - ones1, 9)
        num2 = random.randint(1, 9) * 10 + ones2
        
        answer = num1 + num2
        return f"{num1} + {num2} = ?", answer
    
    @staticmethod
    def generate_borrow_subtraction():
        num1 = random.randint(11, 99)
        ones1 = num1 % 10
        ones2 = random.randint(ones1 + 1, 9)
        num2 = (random.randint(0, num1 // 10 - 1) * 10) + ones2
        
        answer = num1 - num2
        return f"{num1} - {num2} = ?", answer 