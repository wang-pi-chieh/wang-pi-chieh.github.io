# PiChieh 個人網站

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

目前第二個作品為明確標示的示範內容；Note 僅保留 Shell Script 筆記。姓名為王碧婕，未虛構學歷、競賽名次或實習單位。

## 預覽與發布

在這個資料夾執行 `python -m http.server 8768 --bind 127.0.0.1`，開啟 http://127.0.0.1:8768 。

將 HTML、CSS、JS、favicon.svg 與 .nojekyll 上傳到 repository 最外層；Pages 使用 main / (root)。不需要 npm 或 build。Google Fonts 無法載入時會使用系統備用字型。
## Illustration asset

`assets/pichieh-girl.png` was generated with the built-in ImageGen tool, then copied into this project. It is reused on Home and About.

Final prompt:
Use case: illustration-story. Create one polished website mascot asset: a cute little girl with straight dark navy shoulder-length hair and bangs, smiling softly, sitting cross-legged with a small open laptop on her lap. Full body, three-quarter front view, friendly editorial illustration, clean hand-drawn rounded lines, soft flat shaded shapes, tasteful details, not a logo, not an emoji. Oversized light sky blue sweatshirt #C0E0FF, dark navy #000033 shorts or trousers and hair, warm peach skin, white socks. Character should occupy 85% of a square canvas, isolated on a genuinely transparent background, no border, no lettering, no flowers, no plants, no garden motifs, no ground scenery. Clear silhouette legible at 180px, attractive on both white and midnight navy website backgrounds. Laptop screen faces her with back of laptop visible, no text or brand marks. Both hands naturally resting at keyboard. Single character only.

## Footer pages

`privacy.html` describes local theme storage, hosting, fonts and external links. `terms.html` describes content sharing and attribution. Edit them through `build_pages.py` if site behavior changes.
## Shell Script 筆記與目錄

- 筆記原始 Markdown：`notes/shell-script.md`，保留 HackMD 原文連結。
- 原文圖片：`assets/notes/`，固定在本站，避免外部圖片轉址失效。
- 重新匯入：執行 `python import_shell_note.py`，需要作者端 Python 套件 `markdown-it-py`；接著執行 `python build_pages.py`。訪客與 GitHub Pages 不需要 Python 套件。
- 所有 Note 閱讀頁會根據 h2/h3/h4 自動產生左側目錄；手機使用可展開目錄。本文使用固定 ID `article.html?type=notes&id=2`；新增筆記請指定不重複的 `id`，避免刪除或調整順序時變更網址。
- 新筆記以 `featured: true` 排在列表前面。HackMD 後續修改不會自動同步，需要重新匯入。
