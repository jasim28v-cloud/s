import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random

def run_news():
    # المصدر الجديد: العربية - فن ومنوعات (أسرع وأفضل للترند العربي)
    rss_url = "https://www.alarabiya.net/ar/feed/rss/variety"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    try:
        # رابطك الربحي من Adsterra
        my_direct_link = "https://www.effectivegatecpm.com/t3rvmzpu?key=26330eef1cb397212db567d1385dc0b9"
        
        response = requests.get(rss_url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        ticker_text = " 🔥 ".join([item.title.text for item in items[:15]])

        news_html = ""
        for i, item in enumerate(items[:24]):
            title = item.title.text
            news_url = item.link.text
            
            # محاولة جلب الصورة من الوسوم المختلفة (العربية تستخدم وسوم معينة للصورة)
            img_url = ""
            media_content = item.find('media:content') or item.find('enclosure')
            if media_content:
                img_url = media_content.get('url')
            
            # إذا لم يجد صورة، نضع صورة "دراما" احترافية بديلة
            if not img_url:
                img_url = "https://images.pexels.com/photos/33129/pexels-photo-33129.jpg?auto=compress&cs=tinysrgb&w=800"

            news_html += f'''
            <div class="drama-card">
                <a href="{my_direct_link}" target="_blank" class="main-link">
                    <div class="poster-box">
                        <img src="{img_url}" loading="lazy">
                        <div class="trending-tag">ترند الآن 🔥</div>
                        <div class="play-btn-ui">▶</div>
                    </div>
                    <div class="drama-info">
                        <h2 class="title">{title}</h2>
                    </div>
                </a>
                <div class="drama-footer">
                    <a href="{news_url}" target="_blank" class="watch-link">التفاصيل الكاملة للمسلسل 🎬</a>
                </div>
            </div>'''
            
            # إعلان ذكي "مشاهدة" بعد كل 3 أخبار
            if (i + 1) % 3 == 0:
                news_html += f'''
                <div class="drama-card ad-card">
                    <a href="{my_direct_link}" target="_blank" class="main-link">
                        <div class="poster-box ad-grad">
                            <div class="ad-content">
                                <div class="exclusive">حصرياً 🌟</div>
                                <h3>لمشاهدة الحلقة الكاملة وبدون إعلانات</h3>
                                <div class="click-now">إضغط هنا للمشاهدة 📲</div>
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
        :root {{ --red: #e50914; --dark: #141414; }}
        body {{ background: var(--dark); color: white; font-family: 'Cairo', sans-serif; margin: 0; padding-top: 70px; }}
        header {{ background: rgba(0,0,0,0.95); padding: 12px 5%; position: fixed; top: 0; width: 100%; z-index: 1000; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--red); box-sizing: border-box; }}
        .logo {{ font-size: 24px; font-weight: 900; color: var(--red); text-decoration: none; }}
        .logo span {{ color: #fff; }}
        .ticker {{ background: var(--red); color: #fff; height: 35px; display: flex; align-items: center; overflow: hidden; font-weight: bold; font-size: 13px; }}
        .ticker-move {{ white-space: nowrap; animation: scroll 50s linear infinite; }}
        @keyframes scroll {{ 0% {{ transform: translateX(100%); }} 100% {{ transform: translateX(-100%); }} }}
        .container {{ max-width: 1200px; margin: 20px auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; padding: 0 15px; }}
        .drama-card {{ background: #1f1f1f; border-radius: 10px; overflow: hidden; transition: 0.3s; position: relative; border: 1px solid #333; }}
        .drama-card:hover {{ transform: translateY(-5px); border-color: var(--red); }}
        .poster-box {{ height: 380px; position: relative; overflow: hidden; }}
        .poster-box img {{ width: 100%; height: 100%; object-fit: cover; }}
        .play-btn-ui {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); background: rgba(229, 9, 20, 0.8); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 25px; opacity: 0; transition: 0.3s; }}
        .drama-card:hover .play-btn-ui {{ opacity: 1; }}
        .drama-info {{ position: absolute; bottom: 0; width: 100%; padding: 20px 15px; background: linear-gradient(transparent, #000); box-sizing: border-box; }}
        .title {{ font-size: 15px; font-weight: 700; margin: 0; line-height: 1.4; }}
        .drama-footer {{ padding: 10px; background: #111; text-align: center; border-top: 1px solid #222; }}
        .watch-link {{ color: #888; text-decoration: none; font-size: 11px; }}
        .trending-tag {{ position: absolute; top: 10px; right: 10px; background: var(--red); padding: 3px 10px; border-radius: 4px; font-size: 10px; font-weight: bold; }}
        .ad-grad {{ background: linear-gradient(45deg, #2c3e50, #000); display: flex; align-items: center; justify-content: center; }}
        .ad-content {{ padding: 20px; text-align: center; }}
        .exclusive {{ background: #f1c40f; color: #000; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: 900; margin-bottom: 10px; display: inline-block; }}
        .click-now {{ background: var(--red); color: #fff; padding: 10px 20px; border-radius: 5px; font-weight: bold; margin-top: 15px; font-size: 14px; }}
        .main-link {{ text-decoration: none; color: inherit; }}
        @media (max-width: 600px) {{ .container {{ grid-template-columns: 1fr; }} .poster-box {{ height: 450px; }} }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">دراما <span>كافيه</span> 🎬</a>
        <div style="font-size: 11px;">{now}</div>
    </header>
    <div class="ticker"><div class="ticker-move">{ticker_text}</div></div>
    <div class="container">{news_html}</div>
</body>
</html>'''

        with open("index.html", "w", encoding="utf-8") as f: f.write(html)
        print("Done: Drama Cafe is updated with Al Arabiya source!")
            
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run_news()
