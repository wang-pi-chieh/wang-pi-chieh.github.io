// 在這裡新增或修改作品與筆記。示範項目均有清楚標示，請換成你的真實經歷。
const portfolio = {
  projects: [
    {title:'個人作品集網站',category:'web',label:'WEB DEVELOPMENT',number:'01',style:'portfolio',description:'用一個網站，串起專案、學習與成長。以輕量靜態網頁打造自己的數位名片。',tags:['HTML','CSS','JavaScript'],body:'<p>這是你正在瀏覽的個人作品集，使用原生 HTML、CSS 與 JavaScript 製作，可直接部署至 GitHub Pages。</p><h3>實作重點</h3><ul><li>支援手機與桌面的響應式版面</li><li>專案分類篩選與筆記閱讀視窗</li><li>集中在 content.js 維護作品與筆記</li><li>不需要安裝套件或後端服務</li></ul><p>之後可在這裡補上開發動機、遇到的問題與改進紀錄。</p>'},
    {title:'下一個實作，正在醞釀',category:'learning',label:'LEARNING EXPERIMENT',number:'02',style:'experiment',description:'保留一個位置，給下一個值得動手解決的問題。完成後，這裡會留下它的故事。',tags:['示範位置','待更新'],body:'<p>這是作品內容的示範位置，並非已完成的專案。</p><h3>你可以這樣整理專案</h3><ul><li>想解決什麼問題？</li><li>你負責了哪些部分？</li><li>使用哪些技術？為什麼？</li><li>有什麼成果、限制與心得？</li></ul><p>編輯 content.js 即可換成你的真實作品，也能新增更多項目。</p>'}
  ],
  notes: [
    {title:'讓第一個個人網站上線：GitHub Pages',topic:'網站架設',date:'入門筆記 · 範例',body:'<p>這是一篇可修改的入門筆記範例。</p><h3>1. 準備網站檔案</h3><p>將 index.html、styles.css、content.js 與 script.js 放在 repository 最外層。</p><h3>2. 設定發布來源</h3><p>前往 Settings → Pages，選擇 Deploy from a branch，再選 main 與 / (root)，按 Save。</p><h3>3. 檢查發布結果</h3><p>從 Actions 查看部署狀態，完成後回到 Pages 開啟網站連結。個人首頁的 repository 名稱要與帳號對應，例如 wang-pi-chieh.github.io。</p>'},
    {title:'我會怎麼整理一份技術學習筆記？',topic:'學習方法',date:'筆記模板 · 範例',body:'<p>這是筆記結構範例，你可以替換成自己的學習內容。</p><h3>今天想弄懂什麼</h3><p>先寫下一個具體問題，縮小這次學習的範圍。</p><h3>用自己的話解釋</h3><p>寫下核心概念，再補一個能實際執行的小例子。</p><h3>遇到的問題</h3><p>保留錯誤訊息、嘗試過的解法和最後的原因，讓未來的自己少走彎路。</p><h3>下一步</h3><p>記錄還不確定的地方，以及下一次想做的練習。</p>'}
  ]
};
