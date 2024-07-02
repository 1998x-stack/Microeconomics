structure = {
    "1_经济学原理": [
        "1.1_经济学的定义",
        "1.2_稀缺性与选择",
        "1.3_经济学的研究对象"
    ],
    "2_像经济学家一样思考": [
        "2.1_经济学家的工作方法",
        "2.2_经济模型",
        "2.3_实证分析与规范分析"
    ],
    "3_相互依存性与贸易的好处": [
        "3.1_比较优势",
        "3.2_贸易的互利性",
        "3.3_贸易的影响"
    ],
    "4_供给与需求的市场力量": [
        "4.1_需求理论",
        "4.2_供给理论",
        "4.3_市场均衡",
        "4.4_弹性及其应用"
    ],
    "5_弹性及其应用": [
        "5.1_价格弹性",
        "5.2_收入弹性与交叉弹性",
        "5.3_弹性的影响因素",
        "5.4_弹性的应用"
    ],
    "6_供给_需求与政府政策": [
        "6.1_政府干预的必要性",
        "6.2_价格控制",
        "6.3_税收的影响"
    ],
    "7_消费者_生产者与市场效率": [
        "7.1_消费者剩余",
        "7.2_生产者剩余",
        "7.3_市场效率"
    ],
    "8_应用_税收的代价": [
        "8.1_税收的经济效应",
        "8.2_税收的负担分配",
        "8.3_税收对市场效率的影响"
    ],
    "9_应用_国际贸易": [
        "9.1_国际贸易的好处",
        "9.2_贸易壁垒",
        "9.3_贸易政策"
    ],
    "10_外部性": [
        "10.1_外部性的定义",
        "10.2_外部性的影响",
        "10.3_解决外部性的方法"
    ],
    "11_公共物品和共有资源": [
        "11.1_公共物品的特征",
        "11.2_公共物品的供给",
        "11.3_共有资源的管理"
    ],
    "12_税制的设计": [
        "12.1_税收原则",
        "12.2_税收的种类",
        "12.3_税收的影响"
    ],
    "13_生产成本": [
        "13.1_成本的分类",
        "13.2_成本函数",
        "13.3_规模经济与不经济"
    ],
    "14_竞争市场上的企业": [
        "14.1_完全竞争市场的特征",
        "14.2_企业的利润最大化",
        "14.3_短期与长期的市场供给"
    ],
    "15_垄断": [
        "15.1_垄断的定义",
        "15.2_垄断的形成原因",
        "15.3_垄断的经济效应"
    ],
    "16_寡头": [
        "16.1_寡头市场的特征",
        "16.2_寡头的价格与产量决策",
        "16.3_博弈论在寡头市场中的应用"
    ],
    "17_垄断竞争": [
        "17.1_垄断竞争市场的特征",
        "17.2_短期与长期均衡",
        "17.3_垄断竞争的经济效应"
    ],
    "18_生产要素市场": [
        "18.1_劳动力市场",
        "18.2_资本市场",
        "18.3_土地市场"
    ],
    "19_收入与歧视": [
        "19.1_收入的决定因素",
        "19.2_收入差距与不平等",
        "19.3_歧视的经济分析"
    ],
    "20_收入分配": [
        "20.1_收入分配的理论",
        "20.2_收入分配的政策",
        "20.3_反贫困措施"
    ],
    "21_消费者选择理论": [
        "21.1_消费者偏好",
        "21.2_预算约束",
        "21.3_最优选择与效用最大化"
    ]
}




import os
from typing import Dict, Any

def create_directories_and_files(
        base_path: str, 
        structure: Dict[str, Any], 
        readme_file, 
        parent_path: str = "", 
        level: int = 1
    ):
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    # file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    # file_path = os.path.join(current_path, file_name)
                    # with open(file_path, 'w', encoding='utf-8') as file:
                    #     file.write(f"# {item}\n\n")
                    #     file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {item}\n\n"""\n\n')

                    # # 在README中添加文件链接
                    # item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    # parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    # key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    # readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {item}\n\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.md)\n")
        else:
            # # 创建文件并写入初始内容
            # file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            # file_path = os.path.join(current_path, file_name)
            # with open(file_path, 'w', encoding='utf-8') as file:
            #     file.write(f"# {key}\n\n")
            #     file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {key}\n\n"""\n\n')

            # # 在README中添加文件链接
            # parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            # key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            # readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\n\nLecture: {parent_path}/{key}\nContent: {key}\n\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# 微观经济学\n\n")
        readme_file.write("这是一个关于微观经济学的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()