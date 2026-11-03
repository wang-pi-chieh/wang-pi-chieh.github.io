# 王碧婕的數位花園

原生 HTML / CSS / JavaScript，多頁靜態網站，可直接部署至 GitHub Pages。

## 頁面

- `index.html`：Home，個人簡介、社群連結、近期筆記與作品。
- `blog.html`：Blog，生活隨筆、競賽心得與成長紀錄。目前沒有真實文章，因此顯示待更新狀態。
- `note.html`：Note，可搜尋的自學筆記與主題快速搜尋。
- `project.html`：Project，可分類的作品列表。
- `about.html`：About，個人介紹、競賽與經歷、聯絡資訊。
- `article.html?type=notes&id=0`：文章閱讀頁，支援 `notes`、`blogs`、`projects`。

## 編輯內容

- `site.config.js`：GitHub、LinkedIn、Gmail、Instagram。Gmail 只填信箱；其他填完整 HTTPS 網址。
- `content.js`：`blogs`、`notes`、`projects` 三個陣列。新增項目放在陣列尾端，避免原有文章索引網址變動。文章的 `body` 是自行撰寫的可信任 HTML，不要載入外部未驗證內容。
- `build_pages.py`：五頁與文章頁的共用結構及固定介紹。修改後執行 `python build_pages.py` 重新產生 HTML，並一併上傳生成檔案。訪客與 GitHub Pages 都不需要執行 Python。
- `styles.css`：響應式樣式與亮／深色配色。
- `theme.js`：首次依作業系統配色，手動切換後以 localStorage 記住選擇。無法存取儲存空間時，仍能在當頁切換。

目前第二個作品及兩篇筆記為明確標示的示範內容。姓名為王碧婕，未虛構學歷、競賽名次或實習單位。

## 預覽與發布

在這個資料夾執行 `python -m http.server 8768 --bind 127.0.0.1`，開啟 http://127.0.0.1:8768 。

將 HTML、CSS、JS、favicon.svg 與 .nojekyll 上傳到 repository 最外層；Pages 使用 main / (root)。不需要 npm 或 build。Google Fonts 無法載入時會使用系統備用字型。
