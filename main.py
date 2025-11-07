def analyze_chars(input_str):
    # 统计每个字符的出现频率
    char_counts = {}
    for char in input_str:
        # 若字符已在字典中，次数加1；否则初始化为1
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # 按频率降序排序（频率相同则按字符首次出现顺序排列）
    # 利用Python 3.7+字典的插入顺序特性，sorted会保留相同频率元素的原始顺序
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_chars


# 主程序
if __name__ == "__main__":
    # 获取用户输入
    user_input = input("请输入需要分析的字符串：")
    
    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        # 分析字符频率并排序
        result = analyze_chars(user_input)
        
        # 打印结果
        print("\n字符出现频率（按降序排列）：")
        for char, count in result:
            print(f"'{char}': {count}次")
