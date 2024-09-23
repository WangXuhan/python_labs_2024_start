# 创建一个包含水果及其颜色的字典
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}

# 访问字典中的值
apple_color = fruit_colors["apple"]
print(apple_color)  # 输出: red

# 修改字典中的值
fruit_colors["banana"] = "green"
print(fruit_colors)  # 输出: {'apple': 'red', 'banana': 'green', 'cherry': 'red'}

# 添加新的键值对到字典
fruit_colors["orange"] = "orange"
print(fruit_colors)  # 输出: {'apple': 'red', 'banana': 'green', 'cherry': 'red', 'orange': 'orange'}

# 删除字典中的键值对
del fruit_colors["cherry"]
print(fruit_colors)  # 输出: {'apple': 'red', 'banana': 'green', 'orange': 'orange'}

# 获取字典的长度
length = len(fruit_colors)
print(length)  # 输出: 3

# 遍历字典中的键值对
for fruit, color in fruit_colors.items():
    print(f"The color of {fruit} is {color}")