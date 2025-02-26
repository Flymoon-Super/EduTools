import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = os.path.join(str(Path.home()), '.edutools')
        self.config_file = os.path.join(self.config_dir, 'config.json')
        self.default_config = {
            'openai': {
                'api_key': '',
                'api_base': 'https://api.openai.com/v1'
            },
            'output_path': os.path.join(str(Path.home()), 'Documents', 'EduTools'),
            'users': [],
            'current_user': ''
        }
        self.current_config = self.load_config()
        
        # 确保输出目录存在
        output_path = self.current_config.get('output_path', self.default_config['output_path'])
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def load_config(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        
        if not os.path.exists(self.config_file):
            self.save_config(self.default_config)
            return self.default_config
        
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # 确保所有必要的键都存在
                for key, value in self.default_config.items():
                    if key not in config:
                        config[key] = value
                    elif isinstance(value, dict):
                        # 对于嵌套的字典，也确保所有键都存在
                        for sub_key, sub_value in value.items():
                            if sub_key not in config[key]:
                                config[key][sub_key] = sub_value
                return config
        except:
            return self.default_config

    def save_config(self, config):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        self.current_config = config

    def get_config(self, key=None):
        if key is None:
            return self.current_config
        return self.current_config.get(key, self.default_config.get(key))

    def update_config(self, key, value):
        if isinstance(value, dict):
            if key not in self.current_config:
                self.current_config[key] = {}
            self.current_config[key].update(value)
        else:
            self.current_config[key] = value
        self.save_config(self.current_config)
    
    def add_user(self, username):
        if username and username not in self.current_config['users']:
            self.current_config['users'].append(username)
            self.current_config['users'].sort()  # 保持用户列表有序
            self.save_config(self.current_config)
    
    def get_tool_output_path(self, tool_id, username=None):
        """获取工具的输出路径"""
        if username is None:
            username = self.current_config.get('current_user', '')
        base_path = self.current_config.get('output_path', self.default_config['output_path'])
        return os.path.join(base_path, tool_id, username) 