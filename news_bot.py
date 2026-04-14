import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import json

# ====================================================
# [GSF-Factory] 무인 팩토리 봇 (일본 부동산 & 금융 시황)
# ====================================================

# 모니터링할 타겟 공용 RSS 피드 (야후 재팬 경제 등 API 대체품)
TARGET_RSS_URL = "https://news.yahoo.co.jp/rss/topics/business.xml"

# 실제 환경에서는 OPENAI_API_KEY 등을 사용하여 번역 API를 태워야 합니다.
AI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

def fetch_latest_news():
    print(f"📡 타겟 RSS 접속 시도: {TARGET_RSS_URL}")
    try:
        req = urllib.request.Request(TARGET_RSS_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        # 가져올 뉴스 아이템 리스트 (상위 2개)
        items = root.findall('.//item')[:2]
        
        extracted = []
        for item in items:
            title = item.find('title').text
            link = item.find('link').text
            pub_date = item.find('pubDate').text
            extracted.append({"title": title, "link": link, "date": pub_date})
            
        return extracted
    except Exception as e:
        print(f"❌ 크롤링 에러 발생: {e}")
        return []

def translate_and_summarize(news_item, lang="ko"):
    """
    * AI 환각 및 번역을 모의하는 함수입니다.
    # TODO: AI 라이브러리를 통해 news_item['title'] 및 원문 scraping 요약 반영
    """
    if lang == "ko":
        mapped = f"[요약] {news_item['title']} - 최신 금융 파이프라인 분석입니다.\n\n> **💡 GSF 전문가 논평 (Expert Insight):**\n> 이 뉴스는 최근 글로벌 시장의 유동성 흐름과 밀접하게 닿아 있습니다. 특히 일본 금융당국의 금리 정책과 J-REITs 등 부동산 간접 투자 상품으로 자금이 몰릴 가능성을 시사합니다. 보수적인 투자자라면 이번 변동성을 매수 기회로 삼는 것이 유리합니다."
    elif lang == "en":
        mapped = f"[Summary] {news_item['title']} - Latest financial pipeline analysis.\n\n> **💡 GSF Expert Insight:**\n> This news is closely aligned with the recent liquidity flows in the global market. In particular, it hints at the Bank of Japan's interest rate policies and the potential influx of capital into indirect real estate assets like J-REITs. For conservative investors, interpreting this volatility as a buying opportunity could be highly advantageous."
    else:
        mapped = f"[まとめ] {news_item['title']} - 金融パイプラインの最新分析です。\n\n> **💡 GSF 専門家インサイト (Expert Insight):**\n> このニュースは最近のグローバル市場の流動性と密接に関連しています。特に日銀の金利政策やJ-REITsなど、不動産間接投資商品への資金流入の可能性を示唆しています。保守的な投資家の方は、このボラティリティを買い場として捉えることが有利かもしれません。"
    return mapped

def generate_markdown_file(news_data):
    today_str = datetime.now().strftime("%Y-%m-%d")
    output_dir = "src/data/blog"
    os.makedirs(output_dir, exist_ok=True)
    
    # 3개 국어별 저장 포맷 (Astro 다국어 템플릿 호환)
    for lang in ["ko", "en", "ja"]:
        lang_dir = os.path.join(output_dir, lang)
        os.makedirs(lang_dir, exist_ok=True)
        
        # 파일 작성
        filename = f"{today_str}-market-news.md"
        filepath = os.path.join(lang_dir, filename)
        
        # 뉴스 내용 본문 조합
        body_content = ""
        for news in news_data:
            summary = translate_and_summarize(news, lang)
            body_content += f"### [{news['title']}]({news['link']})\n> {news['date']}\n\n{summary}\n\n---\n"
            
        # Frontmatter
        frontmatter = f"""---
title: "Global Financial Market Updates - {today_str}"
pubDatetime: {datetime.now().isoformat()}
modDatetime: {datetime.now().isoformat()}
author: GSF-Bot
featured: false
draft: false
tags: ["news", "market", "japan"]
description: "AI 무인 팩토리가 수집한 실시간 시황 뉴스입니다."
---

{body_content}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter)
        print(f"✅ [{lang}] 마크다운 파일 렌더링 완료: {filepath}")

if __name__ == "__main__":
    print(f"🤖 [Автопилот] 무인 팩토리 뉴스 로봇 구동을 시작합니다.")
    news = fetch_latest_news()
    if news:
        generate_markdown_file(news)
        print(f"✅ GSF-Factory 구동이 완벽하게 끝났습니다. (자동 배포 대기)")
    else:
        print(f"⚠️ 오늘 수집된 뉴스가 없거나 에러가 발생했습니다.")
