# MarkdownLocalWiki
MarkDown記法が使える、ディスクトップ上で動くwiki
個人ブログで管理していたものを今更ながらGitHubに展開したもの
今更ながらGitHubにも挑戦中

ベース：
http://kazu-s-diary-2.cocolog-nifty.com/blog/2016/07/htajquerymark-1.html

・サーバ不要、WindowsOSであれば利用可能

・Markdown記法が使える。

　使っているライブラリ
　・marked.js（一部改造）　https://github.com/markedjs/marked

・github-markdown.css　　https://github.com/sindresorhus/github-markdown-css

・jquery-1.12.0.js　https://code.jquery.com/jquery/
 
・テキストファイルの保存機能

　marked.jsを修正し、リンクのルール「( aaaa  )[ aaaa ]　」の中でURL等以外は、テキストファイル(aaaa.md)保存するように改造している。

テキストファイル(aaaa.md)は、リンクのルール「( aaaa  )[ aaaa ]　」によりファイルリンクされるようにしている。

・テキストファイル以外は、ブラウザ等の外部アプリを利用するように修正。

・いわゆるファイルサーバ（\\コンピュータ名）でもリンクされるように機能追加。

追伸：
まだまだ改良の余地あるツールで、作者も勉強途中ですが。
このツール（手法）に興味を持っていただき、さらに改良にチャレンジされた方がいらっしゃり、とてもうれしい。
こちらにリンクを張っておきます。

https://github.com/ma34s/MarkdownLocalWiki

https://qiita.com/hachimitu22/items/5bba11ab89b556b810b4
