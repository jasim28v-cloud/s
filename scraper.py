import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random

def run_news():
    # مصدر أخبار الفن والمنوعات (RT Arabic - فن)
    rss_url = "https://arabic.rt.com/rss/news/lifestyle/culture/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # رابطك الربحي الذكي من Adsterra
        my_direct_link = "https://www.effectivegatecpm.com/t3rvmzpu?key=26330eef1cb397212db567d1385dc0b9"
        
        response = requests.get(rss_url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_text = " • ".join([item.title.text for item in items[:12]])

        news_html = ""
        for i, item in enumerate(items[:21]):
            title = item.title.text
            news_url = item.link.text
            img_url = item.find('enclosure').get('url') if item.find('enclosure') else "https://via.placeholder.com/600x400/1a1a1a/ffffff?text=Drama+Cafe"
            
            # كرت الدراما (تصميم بوستر سينمائي)
            news_html += f'''
            <div class="drama-card">
                <a href="{my_direct_link}" target="_blank" class="main-link">
                    <div class="poster-box">
                        <img src="{img_url}" loading="lazy">
                        <div class="trending-tag">ترند 🔥</div>
                        <div class="play-icon">▶</div>
                    </div>
                    <div class="drama-info">
                        <h2 class="title">{title}</h2>
                    </div>
                </a>
                <div class="drama-footer">
                    <a href="{news_url}" target="_blank" class="watch-link">شاهد التفاصيل كاملة 🎬</a>
                </div>
            </div>'''
            
            # إعلان "الحلقة المسربة" أو "المشاهدة" بعد كل 3 أخبار
            if (i + 1) % 3 == 0:
                ad_imgs = [
                    "https://images.pexels.com/photos/275977/pexels-photo-275977.jpeg?auto=compress&cs=tinysrgb&w=600",
                    "https://images.pexels.com/photos/33129/pexels-photo-33129.jpg?auto=compress&cs=tinysrgb&w=600"
                ]
                news_html += f'''
                <div class="drama-card ad-card">
                    <a href="{my_direct_link}" target="_blank" class="main-link">
                        <div class="poster-box">
                            <img src="{random.choice(ad_imgs)}" style="filter: brightness(0.4) sepia(0.5);">
                            <div class="ad-content">
                                <div class="premium-tag">حصرياً 🌟</div>
                                <h3>مشاهدة الحلقة المسربة بجودة 4K</h3>
                                <p>بدون إعلانات مزعجة - سيرفر سريع</p>
                                <div class="ad-btn">إضغط للمشاهدة الآن</div>
                            </div>
                        </div>
                    </a>
                </div>'''

        now = datetime.now().strftime("%Y-%m-%d | %I:%M %p")
        
        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>دراما كافيه - Drama Cafe</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {{ --main-red: #e50914; --dark-bg: #141414; --card-bg: #1f1f1f; }}
        body {{ background: var(--dark-bg); color: white; font-family: 'Cairo', sans-serif; margin: 0; padding-top: 70px; }}
        
        header {{ background: rgba(0,0,0,0.9); padding: 15px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; display: flex; justify-content: space-between; align-items: center; box-sizing: border-box; border-bottom: 2px solid var(--main-red); }}
        .logo {{ font-size: 26px; font-weight: 900; color: var(--main-red); text-decoration: none; text-shadow: 0 0 10px rgba(229, 9, 20, 0.5); }}
        .logo span {{ color: white; }}
        
        .ticker {{ background: var(--main-red); color: white; height: 35px; display: flex; align-items: center; overflow: hidden; }}
        .ticker-label {{ background: #000; padding: 0 15px; height: 100%; display: flex; align-items: center; font-weight: 900; font-size: 13px; }}
        .ticker-text {{ white-space: nowrap; animation: scroll 45s linear infinite; font-size: 14px; font-weight: 700; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}

        .container {{ max-width: 1300px; margin: 20px auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px; padding: 0 15px; }}
        
        .drama-card {{ background: var(--card-bg); border-radius: 8px; overflow: hidden; transition: 0.4s; position: relative; border-bottom: 3px solid transparent; }}
        .drama-card:hover {{ transform: scale(1.05); border-bottom-color: var(--main-red); z-index: 10; }}
        
        .poster-box {{ position: relative; height: 380px; overflow: hidden; }}
        .poster-box img {{ width: 100%; height: 100%; object-fit: cover; }}
        
        .play-icon {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 50px; color: rgba(255,255,255,0.8); opacity: 0; transition: 0.3s; }}
        .drama-card:hover .play-icon {{ opacity: 1; }}

        .trending-tag {{ position: absolute; top: 10px; right: 10px; background: var(--main-red); color: white; padding: 4px 10px; font-size: 11px; font-weight: 900; border-radius: 4px; }}
        
        .drama-info {{ padding: 15px; background: linear-gradient(transparent, rgba(0,0,0,0.9)); position: absolute; bottom: 0; width: 100%; box-sizing: border-box; }}
        .title {{ font-size: 16px; font-weight: 700; margin: 0; line-height: 1.4; text-shadow: 2px 2px 4px #000; }}
        
        .drama-footer {{ padding: 10px; text-align: center; background: #111; }}
        .watch-link {{ color: #aaa; text-decoration: none; font-size: 12px; }}

        /* الإعلانات */
        .ad-card {{ border: 1px solid #444; }}
        .ad-content {{ position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 20px; }}
        .premium-tag {{ background: #f1c40f; color: #000; padding: 3px 12px; border-radius: 20px; font-size: 11px; font-weight: 900; margin-bottom: 10px; }}
        .ad-btn {{ background: var(--main-red); color: white; padding: 8px 25px; border-radius: 4px; font-weight: 900; margin-top: 15px; font-size: 14px; box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4); }}
        
        .main-link {{ text-decoration: none; color: inherit; }}

        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} .poster-box {{ height: 450px; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">دراما <span>كافيه</span> 🎬</a>
        <div style="font-size: 11px; color: #888;">{now}</div>
    </header>

    <div class="ticker">
        <div class="ticker-label">ترند الفن</div>
        <div class="ticker-text">{ticker_text}</div>
    </div>

    <div class="container">{news_html}</div>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(html)
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_news()
