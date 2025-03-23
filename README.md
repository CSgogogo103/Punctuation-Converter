# Punctuation-Converter 
**中英文标点自动转换工具**

## 目标
解决中英文混排文本的标点混乱问题，提升机器翻译和数据清洗效率。

## 功能
- 将中文全角标点（，。“”）转换为英文半角标点（, . "）
- 支持自定义扩展标点替换规则

## 使用示例
```python
input_text = "你好，世界。“今天天气真好”。"
output_text = convert_punctuation(input_text)
print(output_text)  # 输出：你好, 世界."今天天气真好".
