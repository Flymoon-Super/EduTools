from openai import OpenAI
import json

class EssayAnalyzer:
    def __init__(self, api_key, base_url=None, model_name="deepseek-r1"):
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
    
    def analyze_essay(self, content, title="", standard=""):
        """
        分析作文并返回评分和建议
        
        Args:
            content (str): 作文内容
            title (str): 作文标题
            standard (str): 评判标准
            
        Returns:
            dict: 包含分数、优点、缺点和建议的字典
        """
        prompt = f"""请根据以下标准分析这篇作文并给出评分（满分100）和详细改进建议：
        评分标准：{standard}
        作文标题：{title}
        作文内容：
        {content}
        
        请用JSON格式返回结果，包含以下字段：
        - score (整数)
        - strengths (数组)
        - weaknesses (数组)
        - suggestions (数组)
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = response.choices[0].message.content
            # 提取JSON部分
            json_start = result.find('{')
            json_end = result.rfind('}') + 1
            if json_start != -1 and json_end != -1:
                json_str = result[json_start:json_end]
                return json.loads(json_str)
            else:
                raise ValueError("无法从AI响应中提取JSON数据")
                
        except Exception as e:
            raise Exception(f"分析作文时发生错误: {str(e)}")
    
    def get_preset_standards(self):
        """
        返回预设的评判标准
        """
        return {
            "小学生二年级": "语言简单通顺，200字左右，主题明确",
            "初中生作文": "结构完整，600字左右，有修辞手法",
            "高中议论文": "论点明确，论据充分，逻辑清晰",
            "散文": "形散神聚，语言优美，意境深远",
            "小说": "人物形象鲜明，情节合理，环境描写恰当"
        } 