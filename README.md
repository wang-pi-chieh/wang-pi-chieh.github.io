# 個人履歷／作品集網站

輕量靜態網站，可直接使用 GitHub Pages，無須安裝套件。

## 發布

1. 個人首頁的 repo 建議命名為 `wang-pi-chieh.github.io`（需與 GitHub 帳號完全一致）。
2. 上傳 `index.html`、`styles.css`、`content.js`、`script.js` 和 `.nojekyll` 至 repo 最外層。
3. Settings → Pages → Deploy from a branch → main → / (root) → Save。
4. 從 Actions 確認部署完成，回 Pages 查看實際網址。

## 修改內容

- `index.html`：姓名、關於我、競賽經歷、GitHub 聯絡連結及網站描述。
- `content.js`：作品與筆記。複製陣列中的項目即可新增；`category` 可填 `web` 或 `learning`。`body` 是你自己撰寫的可信任 HTML，請勿直接放入外部未驗證內容。
- `styles.css`：顏色、字型與響應式排版。
- `script.js`：分類、閱讀視窗與行動版選單。

目前姓名依帳號推定為「王丕傑」，請在發布前確認或替換。網站沒有虛構競賽名次、實習單位或學歷；第二個作品與兩篇筆記皆為清楚標示的示範內容。替換後可自行移除示範標示。

Google Fonts 無法連線時會使用系統備用字型。網站不需後端，不包含聯絡表單或訪客資料蒐集。

## 本機預覽

在此資料夾執行 `python -m http.server 8000`，再開啟 http://localhost:8000 。
