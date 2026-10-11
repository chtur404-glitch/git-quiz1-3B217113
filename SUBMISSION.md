# 作答資料

- 學號：3B217113
- 姓名：邱祺鈞

## 第 2 題：Git 的三個版本

請填寫完成第二步後，`version.txt` 在三個位置中的內容。

- 已提交版本：V1
- 暫存區版本：V2
- 工作區版本：V3

### 使用的 Git 指令

請填寫你用來確認三種差異的 Git 指令。

1. 工作區 vs 暫存區：

   ```bash
      git diff
   ```

   紀錄:
   ```diff --git a/version.txt b/version.txt
      index 8c1384d..29ef827 100644
      --- a/version.txt
      +++ b/version.txt
      @@ -1 +1 @@
      -v2
      +v3
   ```
2. 暫存區 vs 上一次 commit：

   ```bash
      git diff --staged
   ```

   紀錄:
   ```
      忘記複製紀錄了
   ```
3. 工作區 vs 上一次 commit：

   ```bash
      git diff HEAD
   ```

   紀錄:
   ```
      忘記複製紀錄了
   ```
## 完成前自我檢查

- [O] 我保留了題目專案原本的 Git commit 歷史。
- [O] `.vscode` 已從目前版本開始停止追蹤，但本機檔案仍保留。
- [O] `version.txt` 的 Git 歷史依序為 `v1 → v2 → v3`。
- [O] 程式修正與文件修改分成不同的 commit。
- [O] `python app.py` 執行後平均為 `72.6`。
- [O] 我已確認 `git status` 沒有尚未處理的變更。
- [O] 我已把完成結果推送到自己的 GitHub Repository。
