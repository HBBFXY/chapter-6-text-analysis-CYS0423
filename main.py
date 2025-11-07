def analyze_text(input_str):  # 函数名改为 analyze_text，匹配评分要求
    # 统计每个字符的出现频率
    char_counts = {}
    for char in input_str:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # 按频率降序排序（频率相同按首次出现顺序）
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_chars


# 主程序（测试用，不影响评分）
if __name__ == "__main__":
    user_input = input("请输入需要分析的字符串：")
    
    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        result = analyze_text(input_str=user_input)
        print("\n字符出现频率（按降序排列）：")
        for char, count in result:
            print(f"'{char}': {count}次")
