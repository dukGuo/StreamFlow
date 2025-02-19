import os

# 指定目标文件夹路径
directory = "/Users/dkguo/Downloads/is2025/raw/samples/sr"  # 替换为你的文件夹路径

lst = [
    "00015050","001559" ,"002048" ,"011057" , "101503" , "105431"
]
# 遍历文件夹中的所有文件和子目录
for filename in os.listdir(directory):
    # 构造原始文件完整路径
    old_path = os.path.join(directory, filename)
    
    # 仅处理文件，忽略子目录
    if os.path.isfile(old_path):
        # 自定义新的文件名，比如在文件名前加上 "new_"
        
        new_filename = str(lst.index(filename.split('.')[0])) + '.wav'
        new_path = os.path.join(directory, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"已将文件 {filename} 重命名为 {new_filename}")
        except Exception as e:
            print(f"重命名 {filename} 失败：{e}")
