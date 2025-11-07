def analyze_text(input_str):
    """统计字符串中字母字符（含中英文）的出现频率，返回按频率降序排列的元组列表"""
    char_counts = {}
    for char in input_str:
        # 过滤非字母字符（保留中英文，排除数字、符号、空格）
        if not char.isalpha():
            continue
        # 统一转为小写，解决大小写不匹配问题
        lower_char = char.lower()
        # 统计频率
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    
    # 按频率降序排序（频率相同则按字符ASCII码顺序排列，保证一致性）
    sorted_chars = sorted(
        char_counts.items(),
        key=lambda x: (-x[1], x[0])  # 先按频率降序（-x[1]），再按字符升序（x[0]）
    )
    return sorted_chars  # 返回排序后的列表，匹配测试的排序要求


if __name__ == "__main__":
    # 严格按照测试要求的输出文案
    print("文本字符频率分析器")
    print("提示: 尝试输入中英文文章片段")
    user_input = input("请输入一段文本：")
    
    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        result = analyze_text(user_input)
        print("字符频率降序排列：")
        # 直接遍历排序后的结果打印，确保输出顺序正确
        for char, count in result:
            print(f"'{char}': {count}次")
