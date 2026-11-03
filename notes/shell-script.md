# Shell Script
- ``(反引號): 先執行裡面的指令，再把輸出的結果放到這個位置
- ps -ef: 查看目前 Linux 系統正在執行的所有程式（Processes）
    - ps: 查看目前有哪些 Process。只會顯示目前 Terminal、自己開的 Process
    - -e: 顯示 Every Process（所有 Process），而不是只有自己的
    - -f: Full Format（完整格式），會多顯示很多資訊
- | : 把前一個程式的stdout，接到下一個程式的stdin；用於將多個工具串在一起
- ```> /dev/null```: 丟到垃圾桶

- -d: 用於檢查給定的路徑是否為一個存在的目錄
- -ls: 列出找到的文件的詳細信息，包括文件的權限、擁有者、大小、修改時間等。
- exit:
    - exit 0: 成功
    - exit 1: 一般錯誤
    - exit <其他數值>: 不同程式定義的其他錯誤
    - 可以透過echo $? 來知道剛剛的結果是成功、一般錯誤，或是其他錯誤

- stty -echo: 當在輸入時，畫面不會顯示
- stty echo: 當在輸入時，畫面會正常顯示
- echo -n "123"
    - -n: 當印出內容後，不要換行
- IFS=read -p "$prompt" -r -s -n 1 char
    - IFS=: 這是將內部字段分隔符設置為空，這樣可以確保讀取的輸入不會被分隔
        - 確保空格不會被吃掉
    - -p: 會先顯示內容，再開始進行讀取
    - -n 1: 一次只讀一個字元。一般的read是要等到enter才會結束讀取
    - -r: 不要把反斜線 (\) 當成特殊字元
    - -s: Silent（不要顯示輸入）
    - char: 把剛剛讀到的那一個字元存進char
- tr -d '\r': 
    - tr: 把輸入的文字中的字元，一個一個地進行轉換或刪除
    - -d: delete
- Program=`echo $PrgDir | awk -F/ '{ print $NF}'`:
    - -F/: 以/為分割符號

- ```printf '%*s\n' 80 '' | tr ' ' '*'```
    -  %*s: 字串長度由後面的參數決定
        -   tr ' ' '*': 把所有空格 (' ') 換成星號 ('*')。


- mktemp 是一個命令，用於創建一個唯一的臨時文件或臨時目錄。它會返回創建的臨時文件的路徑
- head -n "$N": 取出前 N 行資料
- sort -r "$checklist": 把 $checklist 的內容做排序，而且是「反向（由大到小）」排序
- mv
    - 移動檔案
    - 改檔名

- [ -n "${SPINNER_PID:-}" ] 
    - -n: 字串長度大於 0（不是空字串）

- wc
    - -l: 用來計算行數(line)
    - -w: 用來計算單字數(word)
    - -c: 用來計算位元組數（byte）
    - -m: 用來計算字元數（character）
- chmod -R 755 ${PrgDir}
    - -R: 不只處理目前這個資料夾，還會一路處理裡面的所有子資料夾和檔案

---

### awk
- 用途: 處理「可以切成欄位的文字」的工具。
- 會藉由空格來切開
- awk -F/ '{ print $NF }'
    - -F: 用 / 當作切割符號。
- awk -F\; '{print $2}'
    - -F\;是表示用用 ; 當分隔符號
### grep
- grep: 找符合條件的文字
    - 第一個參數是 grep 要搜尋的文字，即到每個檔案裡面找有沒有與第一個參數相同的內容
    - 第二個參數是 要搜尋哪些檔案
- grep -v grep: 找不符合條件的文字
    - -v: Invert Match（反向匹配）
- grep -z -m 1 -q '[^ -~]'
    - -q: 不要印出找到的內容，只告訴我有沒有找到
    - -m 1: 找到第一個就停止
    - -z: 讓檔名裡就算有空格或特殊字元，也能正確處理
- grep -l: 只印出符合條件的檔名
- grep "^-": 找開頭是 - 的那一行

### sed
- 目的: 對文字做修改
- 用途: 取代文字、刪除某一行、新增一行、修改檔案內容、清理格式等
- 語法: 
    - sed '/條件/動作'
    - 取代: sed 's/舊資料/新資料'
- 舉例
    - sed 's/\/$//g'
    ![image](https://hackmd.io/_uploads/rJFGmXDHzl.png)
    ![image](https://hackmd.io/_uploads/ByZ4QmwrGl.png)
    - sed '/total /d'
    - sed -n: 只印出符合條件的內容
#### 取代文字
- sed 's/ /_/g'
    ![image](https://hackmd.io/_uploads/HJfaT1vBfl.png)
#### 刪除某一行
- sed 's/abc//g': 把abc刪掉

### tee
- ```echo "****************************************"|tee ${logfile}```
    - 一邊顯示在螢幕，一邊寫到檔案。
- tee -a logfile: 追加寫入檔案中

### cut
- 方式: 切出你想要的一部分資料
    - -c: 依照字元位置來做切割
- 舉例
    - cut -c 1-3: 取前三個字元
    - cut -c 5-: 從第五個字元開始
### trap
- 用途: 攔截某個事件，發生時自動執行指定的指令。
- 種類
    - trap '觸發時會做哪些事寫在這邊' INT: 當使用者按下Ctrl+C會被觸發
    - trap '觸發時會做哪些事寫在這邊' EXIT: 終止信號，通常用於請求程序正常終止
    - trap '觸發時會做哪些事寫在這邊' HUP: 掛起信號，通常在終端關閉或連接斷開時發送
- 舉例
    - trap - RETURN: 取消（清除）之前設定的 RETURN trap。


### 測試條件[]
#### 檔案判斷
- -f: 是否為file
- -s: 是否檔案存在且大小 > 0
- -e: 是否路徑存在（檔案或目錄）
- -r: 是否可讀
- -w: 是否可寫
- -x: 是否可執行


#### 字串判斷
- -n: 是否字串不為空
- -z: 是否字串為空
- =: 相等
- !=: 不相等


#### 比較
- -gt: greater than
- -ge: greater than or equal
- -lt: less than
- -le: less than or equal
- -eq: equal
- -ne: not equal
- 舉例
    - ```[ "$a" -eq "$b" ]```


#### 邏輯運算子
- OR: -o
- AND: - a
- NOT: !

#### 其他
- -t: 這個檔案描述符（File Descriptor）是不是連接到終端機（Terminal）
    - [ -t 1 ]: stdout 是不是接到終端機？
    - ![image](https://hackmd.io/_uploads/S1Z8xfDHGl.png)


### 特殊變數
- $?: 上一個執行完成的指令的 Exit Status（結束狀態碼）
- $$: 目前 Shell 的 PID
- $*: 代表所有傳入的參數






### 計算
- 舊的寫法前面需要加上expr
- 加法: +
- 減法: -
- 乘法: \*
    - 因為*是萬用字元
- 除法: /
- 取餘: %

### if
- ```if  [ -f ${PrgDir}/${Program}.tar ]```
    - -f: 判斷是不是一個普通檔案（regular file）
- ```if [ -e "$newpath" ]; then```
    - -e: 檢查這個路徑存不存在
        - exist
- ```if  [ -s /tmp/Check_bzip2_code.$$ ]```
    - -s: 會判斷檔案是否存在及檔案是否不為空
        - size

### find
- ```find . -type f \( -name "core.[0-9]*" \) ! -name "core.[0-9]*.bz2"```
    - core.[0-9]*: 檔名一定要以core.開頭，接著會接一個數字，最後可以接任意個字元（包含 0 個）

- ```find ${i} -type f \( -name "*.edl"  -o -name "*.edf"  -o -name "*.stdf" \) -print -exec /usr/bin/bzip2 {} \;```
    - ```-print -exec /usr/bin/bzip2 {} \;```
        - 先做印出，再對找到的檔案，都執行一次 bzip2
        - {}: 目前找到的那個檔案

- ```find ${PrgDir} -maxdepth 1 -name tpmConf.txt\*    -exec /bin/rm {} \;  > /dev/null```
    - -maxdepth 1: 最多只搜尋一層
- ```find . -type f -mtime +18000 -ls```
    - -mtime +18000: 找出「最後修改時間超過 18000 天」的檔案。
        - mtime = Modification Time
        - +18000: 超過 7 天沒修改的檔案
        - -18000: 7 天內修改過的檔案
        - 18000: 剛好約 7 天前修改的檔案



### 其他
#### MD5
- 方法: 根據檔案內容，計算出一組固定長度的 MD5 值（128 bits，通常顯示為 32 個十六進位字元）
- 目的: 確認檔案沒有被修改


#### touch
- 用途: 建立新檔案、更新時間戳


#### du
- 目的: 用來查看檔案或資料夾占用了多少磁碟空間
- 舉例
    - du -sk .
        - -s: 不要列出每個子目錄，只顯示總計。
            - summary
        - -k: 以 KB（Kilobytes）為單位顯示