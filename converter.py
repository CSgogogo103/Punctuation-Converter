import re
def convert_punctuation(text):
    # 替换中文标点为英文标点
    text = re.sub(r'[，]', ',', text)
    text = re.sub(r'[。]', '.', text)
    text = re.sub(r'[“”]', '"', text)
    return text
if __name__ == "__main__":
    input_text = "你好，世界。“今天天气真好”。"
    print(convert_punctuation(input_text))  # 输出：你好, 世界."今天天气真好".
