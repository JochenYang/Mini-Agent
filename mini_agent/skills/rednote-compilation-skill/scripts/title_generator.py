#!/usr/bin/env python3
"""
小红书标题生成器
根据产品信息生成多种类型的爆款标题
"""

import random
from typing import List, Dict, Tuple

class TitleGenerator:
    def __init__(self):
        # 情感词汇库
        self.emotion_words = {
            '极致感受': ['绝了', '炸了', '太神了', '爱了', '惊艳', '震撼', '绝了', '超绝'],
            '推荐词汇': ['必囤', '必买', '必试', '必入', '必推', '必安', '必种草'],
            '宝藏词汇': ['宝藏', '神级', '黑马', '隐藏好物', '低调奢华', '小众精品'],
            '效果词汇': ['逆袭', '蜕变', '升级', '重塑', '变身', '逆龄', '回春']
        }
        
        # 数字词汇
        self.number_words = {
            '小数量': ['1个', '3个', '5个', '7个', '9个'],
            '大数量': ['10个', '20个', '30个', '50个', '100个'],
            '倍数': ['10倍', '20倍', '50倍', '100倍'],
            '百分比': ['99%', '95%', '90%', '80%']
        }
        
        # 疑问词汇
        self.question_words = {
            '原因类': ['为什么', '怎么', '如何', '凭什么', '什么'],
            '比较类': ['哪个好', '怎么选', '有什么区别', '为什么选择'],
            '效果类': ['有没有效果', '真的有用吗', '值不值得', '会不会踩雷']
        }
        
        # 对比词汇
        self.comparison_words = {
            '前后对比': ['用了VS没用', 'before VS after', '用了变这样', '差距太大了'],
            '价格对比': ['贵妇VS平价', '100元VS1000元', '性价比之王'],
            '产品对比': ['网红VS小众', '爆款VS冷门', '大牌VS平价']
        }
        
        # 权威背书词汇
        self.authority_words = {
            '专业类': ['皮肤科医生', '美妆博主', '造型师', '专业测评'],
            '明星类': ['明星同款', '网红推荐', '达人都在用'],
            '机构类': ['权威认证', '专业机构', '专家推荐']
        }
        
        # 时间词汇
        self.time_words = {
            '短期': ['1天', '3天', '1周', '半个月'],
            '中期': ['1个月', '2个月', '3个月', '半年'],
            '长期': ['1年', '2年', '3年', '多年']
        }

    def generate_titles(self, product_info: Dict, num_titles: int = 10) -> List[str]:
        """生成指定数量的标题"""
        titles = []
        
        # 生成各类型标题
        titles.extend(self._generate_emotion_titles(product_info, num_titles // 4))
        titles.extend(self._generate_number_titles(product_info, num_titles // 4))
        titles.extend(self._generate_question_titles(product_info, num_titles // 4))
        titles.extend(self._generate_comparison_titles(product_info, num_titles - len(titles)))
        
        # 去重并随机排序
        titles = list(set(titles))
        random.shuffle(titles)
        
        return titles[:num_titles]

    def _generate_emotion_titles(self, product_info: Dict, count: int) -> List[str]:
        """生成情感驱动型标题"""
        titles = []
        product_name = product_info.get('name', '这个产品')
        effect = product_info.get('effect', '超好用')
        
        templates = [
            f"{random.choice(self.emotion_words['极致感受'])}！{product_name}真的{random.choice(self.emotion_words['效果词汇'])}",
            f"姐妹们！{product_name}太{random.choice(self.emotion_words['极致感受'])}！",
            f"{random.choice(self.emotion_words['宝藏词汇'])}发现！{product_name}{effect}",
            f"用了{product_name}，我{random.choice(self.emotion_words['效果词汇'])}了",
            f"绝了！{product_name}{random.choice(self.emotion_words['效果词汇'])}",
            f"不允许你们不知道的{product_name}！{random.choice(self.emotion_words['宝藏词汇'])}",
            f"{product_name}让我{random.choice(self.emotion_words['效果词汇'])}了{random.choice(self.emotion_words['极致感受'])}",
            f"这个{product_name}真的是{random.choice(self.emotion_words['宝藏词汇'])}"
        ]
        
        titles = random.sample(templates, min(count, len(templates)))
        return [title.format(**product_info) for title in titles]

    def _generate_number_titles(self, product_info: Dict, count: int) -> List[str]:
        """生成数字型标题"""
        titles = []
        product_name = product_info.get('name', '这个产品')
        effect = product_info.get('effect', '超好用')
        
        templates = [
            f"用了{random.choice(self.number_words['小数量'])}的{product_name}，{effect}",
            f"{random.choice(self.number_words['大数量'])}用户认证的{product_name}！",
            f"花{random.choice(self.number_words['大数量'])}买{product_name}，{effect}！",
            f"{product_name}{effect}，效果提升{random.choice(self.number_words['倍数'])}",
            f"测试了{random.choice(self.number_words['小数量'])}的{product_name}，只有这个{random.choice(self.number_words['百分比'])}",
            f"坚持用{product_name}{random.choice(self.time_words['短期'])}，{effect}！",
            f"花费{random.choice(self.number_words['小数量'])}元买的{product_name}，{effect}！",
            f"{product_name}让我在{random.choice(self.time_words['短期'])}内{random.choice(self.number_words['百分比'])}"
        ]
        
        titles = random.sample(templates, min(count, len(templates)))
        return [title.format(**product_info) for title in titles]

    def _generate_question_titles(self, product_info: Dict, count: int) -> List[str]:
        """生成疑问引导型标题"""
        titles = []
        product_name = product_info.get('name', '这个产品')
        category = product_info.get('category', '')
        
        templates = [
            f"{random.choice(self.question_words['原因类'])}{product_name}{random.choice(self.question_words['效果类'])}？",
            f"怎么选{product_name}？{random.choice(self.question_words['比较类'])}",
            f"{product_name}{random.choice(self.question_words['效果类'])}？实测告诉你！",
            f"为什么{product_name}{random.choice(self.question_words['效果类'])}？",
            f"{random.choice(self.question_words['原因类'])}明星都爱用{product_name}？",
            f"关于{product_name}，{random.choice(self.question_words['原因类'])}说法？",
            f"{product_name}真的{random.choice(self.question_words['效果类'])}吗？",
            f"用了{product_name}{random.choice(self.time_words['短期'])}，{random.choice(self.question_words['效果类'])}？"
        ]
        
        titles = random.sample(templates, min(count, len(templates)))
        return [title.format(**product_info) for title in titles]

    def _generate_comparison_titles(self, product_info: Dict, count: int) -> List[str]:
        """生成对比冲突型标题"""
        titles = []
        product_name = product_info.get('name', '这个产品')
        competitor = product_info.get('competitor', '网红爆款')
        
        templates = [
            f"{product_name}VS{competitor}，{random.choice(self.comparison_words['前后对比'])}",
            f"用了{product_name}，{random.choice(self.comparison_words['前后对比'])}！",
            f"{random.choice(self.comparison_words['价格对比'])}的{product_name}，结果惊了",
            f"{product_name}和{competitor}哪个好？用了就知道",
            f"告别{competitor}，{product_name}让我{random.choice(self.emotion_words['效果词汇'])}了",
            f"从{competitor}到{product_name}，{random.choice(self.emotion_words['效果词汇'])}",
            f"{random.choice(self.comparison_words['产品对比'])}，{product_name}赢了",
            f"同样的{product_name}，为什么{competitor}不如这个？"
        ]
        
        titles = random.sample(templates, min(count, len(templates)))
        return [title.format(**product_info) for title in titles]

    def generate_with_keywords(self, keywords: List[str], num_titles: int = 10) -> List[str]:
        """基于关键词生成标题"""
        titles = []
        
        for i in range(num_titles):
            keyword = random.choice(keywords)
            title_types = [
                f"{keyword}真的有用吗？实测来了！",
                f"用了{keyword}，效果让我震惊了！",
                f"{keyword}避雷指南，再也不踩坑！",
                f"关于{keyword}，我想说些真话...",
                f"{keyword}测评：这个真的绝了！",
                f"为什么大家都爱{keyword}？",
                f"{keyword}vs竞品，哪个更值得买？",
                f"用了{keyword}{random.choice(self.time_words['短期'])}，变化太大了！",
                f"{keyword}购买攻略，看完再买不后悔！",
                f"这个{keyword}真的是{random.choice(self.emotion_words['宝藏词汇'])}！"
            ]
            
            titles.extend(random.sample(title_types, 2))
        
        # 去重并随机排序
        titles = list(set(titles))
        random.shuffle(titles)
        
        return titles[:num_titles]

    def optimize_title(self, original_title: str) -> List[str]:
        """优化现有标题"""
        suggestions = []
        
        # 添加情感词汇
        emotion_prefixes = [
            f"绝了！{original_title}",
            f"姐妹们！{original_title}",
            f"宝藏发现！{original_title}",
            f"必须安利！{original_title}"
        ]
        suggestions.extend(emotion_prefixes)
        
        # 添加数字
        number_patterns = [
            f"用{random.choice(self.number_words['小数量'])}发现：{original_title}",
            f"测试了{random.choice(self.number_words['小数量'])}，{original_title}最棒",
            f"{random.choice(self.number_words['百分比'])}的人都推荐：{original_title}"
        ]
        suggestions.extend(number_patterns)
        
        # 改为疑问句
        question_patterns = [
            f"{original_title}真的有用吗？",
            f"为什么{original_title}这么火？",
            f"关于{original_title}，你想知道什么？"
        ]
        suggestions.extend(question_patterns)
        
        return suggestions

def main():
    """主函数 - 命令行工具"""
    generator = TitleGenerator()
    
    print("=== 小红书标题生成器 ===")
    print()
    
    mode = input("选择模式：\n1. 基于产品信息生成\n2. 基于关键词生成\n3. 优化现有标题\n请输入选择(1/2/3): ").strip()
    
    if mode == '1':
        print("\n请输入产品信息：")
        product_info = {
            'name': input("产品名称: ").strip(),
            'effect': input("产品效果: ").strip() or "超好用",
            'category': input("产品类别: ").strip() or "未知",
            'competitor': input("竞品(可选): ").strip() or "网红爆款"
        }
        
        if not product_info['name']:
            print("产品名称不能为空！")
            return
            
        num_titles = int(input("生成标题数量(默认10): ").strip() or "10")
        
        titles = generator.generate_titles(product_info, num_titles)
        
        print(f"\n🎯 为'{product_info['name']}'生成的标题：")
        print("=" * 50)
        for i, title in enumerate(titles, 1):
            print(f"{i:2d}. {title}")
    
    elif mode == '2':
        keywords_input = input("请输入关键词(用逗号分隔): ").strip()
        if not keywords_input:
            print("关键词不能为空！")
            return
            
        keywords = [kw.strip() for kw in keywords_input.split(',')]
        num_titles = int(input("生成标题数量(默认10): ").strip() or "10")
        
        titles = generator.generate_with_keywords(keywords, num_titles)
        
        print(f"\n🎯 基于关键词生成的标题：")
        print("=" * 50)
        for i, title in enumerate(titles, 1):
            print(f"{i:2d}. {title}")
    
    elif mode == '3':
        original_title = input("请输入要优化的标题: ").strip()
        if not original_title:
            print("标题不能为空！")
            return
            
        suggestions = generator.optimize_title(original_title)
        
        print(f"\n🔧 '{original_title}'的优化建议：")
        print("=" * 50)
        for i, title in enumerate(suggestions, 1):
            print(f"{i:2d}. {title}")
    
    else:
        print("无效的选择！")
        return
    
    print("\n💡 使用建议：")
    print("1. 选择最符合品牌调性的标题")
    print("2. 可以结合多个标题的优点")
    print("3. 注意标题与内容的匹配度")
    print("4. 定期测试不同标题的效果")

if __name__ == "__main__":
    main()