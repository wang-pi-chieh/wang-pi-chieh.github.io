"""Generate the static HTML shells. No build is needed when deploying the generated files."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAV = [('home', 'Home', 'index.html'), ('blog', 'Blog', 'blog.html'), ('note', 'Note', 'note.html'), ('project', 'Project', 'project.html'), ('about', 'About', 'about.html')]

def shell(page, title, body):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if key == page else '')+f'>{label}</a>' for key, label, url in NAV)
    return f'''<!doctype html>
<html lang="zh-Hant"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="王碧婕的個人網站：專案作品、自學筆記、生活隨筆與競賽紀錄。">
<meta name="theme-color" content="#f7f8fc"><title>{title} · 王碧婕</title>
<script src="theme.js"></script><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css">
<script src="site.config.js" defer></script><script src="content.js" defer></script><script src="script.js" defer></script>
</head><body data-page="{page}">
<a class="skip" href="#main">跳至主要內容</a>
<header class="site-header"><div class="header-inner"><a class="wordmark" href="index.html" aria-label="王碧婕，首頁"><span class="logo-mark">w<span>·</span></span><span>碧婕的數位花園<small>WANG PI CHIEH</small></span></a>
<div class="header-controls"><nav id="navigation" aria-label="主要導覽">{nav}</nav><button class="theme-toggle icon-button" aria-label="切換配色模式" title="切換配色模式"><span aria-hidden="true">◐</span></button><button class="menu-toggle icon-button" aria-controls="navigation" aria-expanded="false" aria-label="開啟導覽">☰</button></div></div></header>
<main id="main" class="container">{body}</main>
<footer class="site-footer container"><div><a class="footer-name" href="index.html">王碧婕<span> / Keep growing.</span></a><p>© <span id="year">2026</span> · 用作品記錄探索，用文字整理思考。</p></div><div class="socials footer-socials" data-socials></div></footer>
<noscript><p class="noscript">請啟用 JavaScript，以顯示文章、作品及社群連結。五頁導覽仍可正常使用。</p></noscript>
</body></html>'''

def heading(kicker, title, text):
    return f'<header class="page-heading"><p class="eyebrow">{kicker}</p><h1>{title}<span class="title-dot">.</span></h1><p class="page-description">{text}</p></header>'

pages = {
'index.html': ('home','Home', '''
<section class="home-hero"><div class="hero-text"><p class="eyebrow"><span class="status-dot"></span> A LITTLE CORNER OF THE INTERNET</p><h1>嗨，我是<span class="name">王碧婕<span class="wave">✳</span></span></h1><p class="hero-subtitle">寫程式、做筆記，<br>也把生活慢慢<span class="underline">收集成故事。</span></p><p class="hero-description">歡迎來到我的數位花園。這裡有從想法長出來的作品、<br class="desktop-break">學習途中的發現，以及值得留下的每一步。</p><div class="hero-actions"><a class="button" href="project.html">看看我的作品 <span>↗</span></a><a class="plain-link" href="about.html">更多關於我 <span>→</span></a></div><div class="socials hero-socials" data-socials></div></div>
<div class="garden-art" role="img" aria-label="一本筆記、一株幼苗與程式視窗，象徵持續學習與成長"><div class="art-orbit"></div><span class="art-star star-one">✦</span><span class="art-star star-two">✳</span><div class="floating-label">a little better, every day.</div><div class="terminal"><div class="terminal-bar"><i></i><i></i><i></i><span>my-little-garden.js</span></div><div class="terminal-code"><span class="code-purple">const</span> life = {<br>&nbsp; curiosity: <span class="code-green">'always'</span>,<br>&nbsp; learning: <span class="code-orange">true</span>,<br>&nbsp; next: <span class="code-green">'make it happen'</span><br>};<br><br><span class="code-comment">// one small step at a time.</span></div></div><div class="notebook"><span>NOTES & IDEAS</span><div></div><div></div><div></div><b>↗</b></div><div class="plant"><span class="leaf leaf-left"></span><span class="leaf leaf-right"></span><span class="stem"></span><span class="pot"></span></div><div class="art-ground"></div><div class="art-caption">LEARN. BUILD. BLOOM.</div></div></section>
<div class="home-divider"><span>持續學習，也持續創作</span><span>SCROLL TO EXPLORE ↓</span></div>
<section class="home-content"><div class="main-column"><div class="section-heading"><div><p class="eyebrow">FRESH FROM THE GARDEN</p><h2>最近的筆記<span class="title-dot">.</span></h2></div><a class="plain-link" href="note.html">所有筆記 →</a></div><div data-entries="notes" data-limit="2"></div><div class="section-heading second-heading"><div><p class="eyebrow">MADE WITH CURIOSITY</p><h2>精選作品<span class="title-dot">.</span></h2></div><a class="plain-link" href="project.html">所有作品 →</a></div><div data-projects data-limit="1"></div></div><aside class="home-sidebar"><div class="about-card"><span class="mini-flower">✳</span><p class="eyebrow">BEHIND THE SCREEN</p><h3>關於這座小花園</h3><p>我相信，學到的東西值得記下，做過的嘗試值得分享。</p><p>這裡不只收集成果，也收集那些「原來如此」的瞬間。</p><a class="plain-link" href="about.html">認識我 →</a></div><div class="explore-card"><p class="eyebrow">TAKE A WALK</p><a href="blog.html"><span>Blog<small>生活、競賽與成長隨筆</small></span>↗</a><a href="note.html"><span>Note<small>技術筆記與學習整理</small></span>↗</a><a href="project.html"><span>Project<small>從想法走向實作</small></span>↗</a></div><p class="sidebar-quote">「讓好奇心帶路，<br>讓每一次嘗試留下痕跡。」</p></aside></section>'''),
'blog.html': ('blog','Blog', heading('THOUGHTS, STORIES & LITTLE MOMENTS','Blog','寫下生活、競賽與成長的片段。讓成果之外的過程，也有被看見的地方。')+'''<div class="archive-layout"><section aria-label="Blog 文章"><div class="archive-toolbar"><span>生活與成長隨筆</span><span data-count="blogs"></span></div><div data-entries="blogs"></div></section><aside class="archive-aside"><span class="aside-symbol">✺</span><h2>留一點空間，<br>給生活的靈感。</h2><p>競賽的心得、專案背後的故事，或一個突然想通的瞬間，都可以從這裡開始。</p><a class="plain-link" href="note.html">先看看自學筆記 →</a></aside></div>'''),
'note.html': ('note','Note', heading('LEARNING IN PUBLIC','Note','把零散的理解，整理成自己的知識地圖。今天學會的一點點，都是明天的起點。')+'''<div class="archive-layout"><section aria-label="自學筆記"><label class="search-box"><span aria-hidden="true">⌕</span><input id="note-search" type="search" placeholder="搜尋筆記標題、內容或主題…" aria-label="搜尋筆記"></label><div class="archive-toolbar"><span>自學筆記</span><span data-count="notes" aria-live="polite"></span></div><div data-entries="notes" aria-live="polite"></div></section><aside class="archive-aside"><p class="eyebrow">MY KNOWLEDGE MAP</p><h2>理解，來自<br>一次次整理。</h2><p>記錄概念、實作步驟與踩過的坑，也保留還沒想通的問題。</p><div class="topic-list" id="note-topics"></div></aside></div>'''),
'project.html': ('project','Project', heading('IDEAS INTO SOMETHING REAL','Project','從一個「如果可以」開始，到一個真正能使用的作品。這裡整理我的實作與探索。')+'''<div class="project-toolbar"><div class="filters" role="group" aria-label="篩選專案"><button data-filter="all" aria-pressed="true">全部作品</button><button data-filter="web" aria-pressed="false">網站開發</button><button data-filter="learning" aria-pressed="false">學習實作</button></div><span data-count="projects" aria-live="polite"></span></div><div class="project-grid" data-projects aria-live="polite"></div><div class="bottom-note"><span>↗</span><p>每個作品都是一段練習。<br><small>記錄問題、選擇與收穫，讓下一次做得更好。</small></p></div>'''),
'about.html': ('about','About', heading('THE PERSON BEHIND THE PIXELS','About','你好，我是王碧婕。很高興在這個小小的網路角落，與你相遇。')+'''<div class="about-layout"><aside class="profile-card"><div class="profile-monogram" aria-label="王碧婕的文字頭像">碧<span>✳</span></div><h2>王碧婕</h2><p>Wang Pi Chieh</p><span class="profile-location">↳ Taiwan</span><div class="socials" data-socials></div></aside><div class="about-body"><section><p class="eyebrow">A FEW WORDS ABOUT ME</p><h2>喜歡拆解問題，<br>也喜歡創造可能。</h2><p>我正在累積程式開發與專案實作的經驗。這個網站是我的數位工作桌：整理做過的作品、記下學習中的發現，也保存參與競賽與挑戰的過程。</p><p>比起只留下最後的成果，我也想分享一路上的思考、嘗試與修正。希望這些紀錄，能讓未來的自己看見成長，也讓來到這裡的人找到一點靈感。</p><div class="tags"><span>程式開發</span><span>專案實作</span><span>自主學習</span><span>問題解決</span></div></section><section class="experience-section"><p class="eyebrow">EXPERIENCE & CHALLENGES</p><h2>競賽與經歷</h2><div class="timeline-item"><span class="timeline-dot"></span><span class="entry-meta">持續整理中</span><h3>下一段故事，準備留下。</h3><p>這裡將整理競賽、實習與專題經驗，分享參與的角色、面對的挑戰和學到的事。</p></div></section><section class="connect-section"><p class="eyebrow">LET’S CONNECT</p><h2>從一次交流開始。</h2><p>歡迎交流專案、自學與開發經驗。你可以透過以下連結找到我。</p><div class="socials" data-socials data-expanded></div></section></div></div>'''),
'article.html': ('article','閱讀文章', '''<div id="article-content" class="article-container"><p>正在載入內容…</p></div>''')
}

for filename, (page, title, body) in pages.items():
    (ROOT / filename).write_text(shell(page, title, body), encoding='utf-8')
print('Generated', len(pages), 'HTML pages.')
