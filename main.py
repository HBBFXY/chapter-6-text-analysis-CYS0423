def analyze_text(input_str):
    """统计字符串中字母字符（含中英文）的出现频率，返回按原逻辑处理的频率字典"""
    char_counts = {}
    for char in input_str:
        # 1. 过滤非字母字符（保留中英文等字母，排除数字、符号、空格）
        if not char.isalpha():
            continue
        # 2. 统一转为小写（解决大小写不匹配问题）
        lower_char = char.lower()
        # 3. 统计频率
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    return char_counts  # 4. 返回字典（匹配预期返回类型）


if __name__ == "__main__":
    # 补充主程序缺失的提示文本
    print("文本字符频率分析器")
    print("提示: 尝试输入中英文文章片段")
    user_input = input("请输入一段文本：")
    
    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        result = analyze_text(user_input)
        # 按频率降序打印结果（保持原输出格式）
        print("字符频率降序排列：")
        sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
        for char, count in sorted_result:
            print(f"'{char}': {count}次")
