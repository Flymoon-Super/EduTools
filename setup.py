from setuptools import setup, find_packages

setup(
    name="edutools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tkinter>=8.6",
        "openai>=1.0.0",
        "requests>=2.31.0",
    ],
    author="逍遥荷包蛋",
    author_email="bihongfei0222@qq.com",
    description="教育工具集合，包含数学题生成器和作文批改工具",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Flymoon-Super/EduTools.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "math-quiz=edutools.gui.math_quiz_app:main",
            "essay-analyzer=edutools.gui.essay_analyzer_app:main",
        ],
    },
) 