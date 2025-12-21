#!/usr/bin/env python3
"""
小红书内容分析工具
用于分析小红书内容的关键词、热度、标签等
"""

import re
import json
from collections import Counter
from typing import List, Dict, Tuple

class RedNoteAnalyzer:
    def __init__(self):
        self.emotion_words = {
            'positive': ['太棒了', '绝了', '爱了', '超赞', '惊艳', '完美', '神器', '宝藏', '推荐', '种草', '好物'],
            'negative': ['踩雷', '失望', '不好', '垃圾', '后悔', '坑', '差评', '不推荐'],
            'neutral': ['一般', '还行', '普通', '中等', '正常', '标准']
        }
        
        self.keywords_pattern = {
            '数字': r'\d+',
            '价格': r'[\d]+[元圆￥]',  
            '品牌': r'[\u4e00-\u9fa5]{2,}(?:品牌|官网|官网|正品)',
            '时间': r'\d+[天周月年](?:前|后|内|来)',
            '对比': r'比.*?好|比.*?差|.*?胜.*?'
        }
    
    def analyze_title(self, title: str) -> Dict:
        """分析标题特征"""
        analysis = {
            '长度': len(title),
            '包含数字': bool(re.search(r'\d+', title)),
            '情感词汇': self._find_emotion_words(title),
            '标题类型': self._classify_title_type(title),
            '关键词': self._extract_keywords(title),
            '热度评分': self._calculate_heat_score(title)
        }
        return analysis
    
    def _find_emotion_words(self, text: str) -> List[str]:
        """查找情感词汇"""
        found_words = []
        for category, words in self.emotion_words.items():
            for word in words:
                if word in text:
                    found_words.append(f"{word}({category})")
        return found_words
    
    def _classify_title_type(self, title: str) -> str:
        """分类标题类型"""
        if re.search(r'\d+', title) and any(word in title for word in ['个', '种', '方法']):
            return '数字型'
        elif any(word in title for word in ['为什么', '怎么', '如何']):
            return '疑问型'
        elif any(word in title for word in ['对比', 'VS', 'vs', '和', '与']):
            return '对比型'
        elif any(word in title for word in ['推荐', '种草', '好物']):
            return '种草型'
        elif any(word in title for word in ['测评', '测试', '体验']):
            return '测评型'
        else:
            return '普通型'
    
    def _extract_keywords(self, text: str) -> List[str]:
        """提取关键词"""
        keywords = []
        for category, pattern in self.keywords_pattern.items():
            matches = re.findall(pattern, text)
            keywords.extend([f"{match}({category})" for match in matches])
        return keywords
    
    def _calculate_heat_score(self, title: str) -> int:
        """计算热度评分 (1-10分)"""
        score = 5  # 基础分
        
        # 长度加分 (8-15字最佳)
        length = len(title)
        if 8 <= length <= 15:
            score += 2
        elif length < 8:
            score -= 1
        elif length > 20:
            score -= 2
            
        # 数字加分
        if re.search(r'\d+', title):
            score += 1
            
        # 情感词汇加分
        emotion_count = len(self._find_emotion_words(title))
        score += min(emotion_count, 2)
        
        # 疑问词汇加分
        if any(word in title for word in ['?', '？', '怎么', '如何', '为什么']):
            score += 1
            
        return min(max(score, 1), 10)
    
    def analyze_content(self, content: str) -> Dict:
        """分析正文内容"""
        analysis = {
            '字数': len(content),
            '段落数': content.count('\n') + 1,
            '情感倾向': self._analyze_sentiment(content),
            '关键信息': self._extract_key_info(content),
            '互动引导': self._check_interaction_elements(content)
        }
        return analysis
    
    def _analyze_sentiment(self, content: str) -> Dict:
        """情感分析"""
        positive_count = sum(1 for word in self.emotion_words['positive'] if word in content)
        negative_count = sum(1 for word in self.emotion_words['negative'] if word in content)
        neutral_count = sum(1 for word in self.emotion_words['neutral'] if word in content)
        
        total_emotions = positive_count + negative_count + neutral_count
        if total_emotions == 0:
            return {'倾向': '中性', '情感词汇数': 0}
        
        if positive_count > negative_count and positive_count > neutral_count:
            return {'倾向': '积极', '情感词汇数': total_emotions}
        elif negative_count > positive_count:
            return {'倾向': '消极', '情感词汇数': total_emotions}
        else:
            return {'倾向': '中性', '情感词汇数': total_emotions}
    
    def _extract_key_info(self, content: str) -> Dict:
        """提取关键信息"""
        info = {}
        
        # 价格信息
        price_matches = re.findall(r'[\d]+[元圆￥]', content)
        if price_matches:
            info['价格'] = price_matches
        
        # 时间信息
        time_matches = re.findall(r'\d+[天周月年](?:前|后|内|来)', content)
        if time_matches:
            info['时间'] = time_matches
            
        # 品牌信息
        brand_pattern = r'[\u4e00-\u9fa5]{2,}(?:品牌|官网|正品)'
        brand_matches = re.findall(brand_pattern, content)
        if brand_matches:
            info['品牌'] = brand_matches
            
        # 对比信息
        comparison_matches = re.findall(r'比.*?好|比.*?差|.*?胜.*?', content)
        if comparison_matches:
            info['对比'] = comparison_matches
            
        return info
    
    def _check_interaction_elements(self, content: str) -> List[str]:
        """检查互动元素"""
        elements = []
        
        # 疑问句
        if '?' in content or '？' in content:
            elements.append('疑问句')
            
        # 感叹句
        if re.search(r'[！!]', content):
            elements.append('感叹句')
            
        # 行动引导词
        action_words = ['点赞', '收藏', '关注', '分享', '评论', '互动', '留言']
        if any(word in content for word in action_words):
            elements.append('行动引导')
            
        # 互动问题
        if re.search(r'你们.*?吗|觉得.*?怎么样|.*?吗.*?', content):
            elements.append('互动问题')
            
        return elements

    def generate_tags(self, content: str, title: str, category: str = '通用') -> List[str]:
        """生成推荐标签"""
        tags = []
        
        # 通用标签
        tags.extend(['#小红书', '#种草', '#分享', '#推荐'])
        
        # 根据内容生成标签
        content_lower = (content + title).lower()
        
        # 美妆相关
        if any(keyword in content_lower for keyword in ['美妆', '护肤', '化妆品', '面膜', '精华', '粉底', '口红']):
            tags.extend(['#美妆博主', '#护肤品推荐', '#化妆教程', '#美妆测评'])
            
        # 美食相关
        elif any(keyword in content_lower for keyword in ['美食', '吃', '菜谱', '做饭', '餐厅', '甜品']):
            tags.extend(['#美食分享', '#探店', '#家常菜', '#美食教程'])
            
        # 穿搭相关
        elif any(keyword in content_lower for keyword in ['穿搭', '衣服', '搭配', '时尚', '包包', '鞋子']):
            tags.extend(['#穿搭分享', '#时尚博主', '#日常穿搭', '#ootd'])
            
        # 生活相关
        elif any(keyword in content_lower for keyword in ['生活', '好物', '家居', '收纳', '幸福感']):
            tags.extend(['#生活好物', '#提升幸福感', '#生活品质', '#家居好物'])
            
        # 学习相关
        elif any(keyword in content_lower for keyword in ['学习', '教育', '技能', '知识', '成长']):
            tags.extend(['#学习方法', '#技能分享', '#自我提升', '#成长笔记'])
            
        # 数字标签
        if re.search(r'\d+', title):
            tags.append('#数字分享')
            
        # 情感标签
        emotion_words = self._find_emotion_words(title)
        if emotion_words:
            tags.append('#真实分享')
            
        return tags[:10]  # 限制标签数量

def main():
    """主函数 - 命令行工具"""
    analyzer = RedNoteAnalyzer()
    
    print("=== 小红书内容分析工具 ===")
    print("请输入要分析的内容：")
    print()
    
    title = input("标题: ").strip()
    content = input("正文: ").strip()
    category = input("分类 (可选): ").strip() or "通用"
    
    if not title or not content:
        print("标题和正文不能为空！")
        return
    
    print("\n" + "="*50)
    print("分析结果：")
    print("="*50)
    
    # 分析标题
    title_analysis = analyzer.analyze_title(title)
    print(f"\n📝 标题分析：")
    for key, value in title_analysis.items():
        print(f"  {key}: {value}")
    
    # 分析正文
    content_analysis = analyzer.analyze_content(content)
    print(f"\n📄 正文分析：")
    for key, value in content_analysis.items():
        print(f"  {key}: {value}")
    
    # 生成标签
    tags = analyzer.generate_tags(content, title, category)
    print(f"\n🏷️ 推荐标签：")
    print(" ".join(tags))
    
    # 整体建议
    print(f"\n💡 优化建议：")
    suggestions = []
    
    if title_analysis['长度'] > 20:
        suggestions.append("标题过长，建议控制在15字以内")
    if title_analysis['热度评分'] < 6:
        suggestions.append("标题热度较低，建议添加数字或情感词汇")
    if content_analysis['情感倾向']['倾向'] == '中性':
        suggestions.append("正文情感色彩较弱，建议增加更多情感表达")
    if '行动引导' not in content_analysis['互动引导']:
        suggestions.append("建议添加互动引导，提高用户参与度")
        
    if suggestions:
        for i, suggestion in enumerate(suggestions, 1):
            print(f"  {i}. {suggestion}")
    else:
        print("  内容质量良好，暂无明显优化建议！")

if __name__ == "__main__":
    main()