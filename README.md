# MarkdownLocalWiki

WindowsのHTML Application（HTA）として動作し、MarkdownファイルをローカルPC上で閲覧・編集する個人用Wikiです。Webサーバーやデータベースは不要で、Wikiページはリポジトリ直下の`.md`ファイルとして保存されます。

> [!CAUTION]
> このリポジトリはHTA／`mshta.exe`を使うレガシー版です。HTAは通常のWebページより強い権限でActiveXやローカルファイルを操作できます。組織のセキュリティ設定で実行を禁止されている場合があり、新規利用にはPowerShellローカルサーバー版の[`MarkDownPSLocalServerWiki`](https://github.com/papanda925/MarkDownPSLocalServerWiki)を推奨します。

## 主な機能

- Markdownページの表示と編集
- 新規ページ作成、名前変更、削除
- ページ一覧
- ファイル名と本文の文字列検索
- 表示履歴
- 文字サイズの拡大・縮小
- HTTP／HTTPSリンクを外部ブラウザーで開く機能
- WindowsのファイルパスやUNCパスを関連付けられたアプリで開く機能
- ページを同じフォルダーの`.md`ファイルとして保存

## 動作環境

- Windows
- `mshta.exe`／HTAの実行が許可されている環境
- リポジトリのフォルダーへ書き込めること

Edge、Chrome、Firefoxの拡張機能として動くものではありません。`index.hta`はWindowsのHTML Application Hostで実行されます。

## 起動方法

1. リポジトリをダウンロードまたはクローンします。
2. `index.hta`、`core`フォルダー、`.md`ファイルを同じ構成のまま置きます。
3. `index.hta`をダブルクリックします。
4. 「トップページ」が表示されることを確認します。

実行前に`index.hta`の入手元と内容を確認してください。メールや不明なWebサイトから取得したHTAファイルは実行しないでください。

## ページデータ

| 場所 | 内容 |
| --- | --- |
| `トップページ.md` | 最初に表示するページ |
| `*.md` | 作成したWikiページ |
| `index.hta` | 画面、Markdown処理、ファイル操作 |
| `core\marked.js` | MarkdownからHTMLへの変換 |
| `core\github-markdown.css` | Markdown表示用CSS |
| `core\jquery-1.12.4.js` | 同梱されている旧版jQuery |

バックアップする場合は、リポジトリ直下の`.md`ファイルをすべてコピーしてください。更新、名前変更、削除の前には別フォルダーへバックアップすることを推奨します。

## ページ名の扱い

ページ名はWindowsのファイル名として使われます。現在のコードは次を拒否します。

- 空のページ名
- `.`または`..`
- `\ / : * ? " < > |`など、Windowsのファイル名に使用できない文字
- 制御文字

すべてのページパスは`index.hta`があるフォルダーを基準に組み立てます。これにより、新規作成、保存、名前変更、削除でWikiフォルダー外を直接指定できないようにしています。

## セキュリティ上の注意

- HTAは現在のブラウザーのサンドボックス内では動作しません。
- `Scripting.FileSystemObject`でファイルを作成・変更・削除します。
- `Shell.Application`でローカルファイルやフォルダーを開きます。
- 信頼できないMarkdownには、HTMLや不正なリンクが含まれる可能性があります。
- このWikiフォルダーへ、信頼できない`.hta`、JavaScript、Markdownを追加しないでください。
- 組織で`mshta.exe`が禁止されている場合、設定を回避せずPowerShellローカルサーバー版を使用してください。

`mshta.exe`は正規のWindows機能ですが、任意のスクリプト実行に悪用される例があるため、セキュリティ製品や組織ポリシーで制限されることがあります。参考：[MITRE ATT&CK - Mshta](https://attack.mitre.org/techniques/T1218/005/)

## PowerShellローカルサーバー版への移行

1. [`MarkDownPSLocalServerWiki`](https://github.com/papanda925/MarkDownPSLocalServerWiki)を別フォルダーへ準備します。
2. HTA版を終了します。
3. このリポジトリ直下の`.md`ファイルを、移行先の`doc`フォルダーへコピーします。
4. `トップページ.md`が`doc`フォルダーにあることを確認します。
5. 移行先の`startWiki.bat`または`StartWiki.ps1`を起動します。
6. 表示、編集、検索、リンクを確認してから旧フォルダーを保管します。

最初は移動ではなくコピーにし、元データを残してください。

## 制限事項

- HTA／Internet Explorer系のMSHTML実行環境に依存
- 現在のWeb標準やブラウザー機能を前提にしたコードではない
- 複数利用者、ログイン、権限管理、同時編集に非対応
- 自動バックアップ、世代管理、ごみ箱はなし
- 同梱JavaScriptライブラリは旧版であり、無条件の最新版置換は互換性を壊す可能性あり
- Markdown内の信頼できないHTMLを安全に無害化する機能はなし

## トラブルシューティング

### `index.hta`を開けない

組織ポリシー、EDR、ウイルス対策ソフト、ファイルの関連付けでHTAが禁止されている可能性があります。設定の回避は行わず、PowerShellローカルサーバー版への移行を検討してください。

### トップページが見つからない

`index.hta`と同じフォルダーに`トップページ.md`があるか確認してください。

### 保存できない

Wikiフォルダーへの書き込み権限を確認してください。読み取り専用の場所、ZIPファイル内、保護されたフォルダーでは保存できません。

### 文字化けする

`index.hta`はShift_JISを前提としています。ソースやMarkdownの文字コードを変更する場合は、必ずコピーで試し、既存ページの表示と再保存を確認してください。

## 由来と関連プロジェクト

このリポジトリは、個人ブログで公開していたHTA／jQuery／marked.jsによるMarkdown WikiをGitHubへ移したものです。

- [元になったブログ記事](http://kazu-s-diary-2.cocolog-nifty.com/blog/2016/07/htajquerymark-1.html)
- [ma34s/MarkdownLocalWiki](https://github.com/ma34s/MarkdownLocalWiki)
- [Qiitaでの関連紹介](https://qiita.com/hachimitu22/items/5bba11ab89b556b810b4)
- [後継：MarkDownPSLocalServerWiki](https://github.com/papanda925/MarkDownPSLocalServerWiki)

## English summary

Legacy Windows HTA-based personal Markdown wiki. It can read and write local files with the current user's permissions. New users should prefer the localhost-only PowerShell server successor.
