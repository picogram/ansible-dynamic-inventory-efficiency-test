## ダイナミックインベントリのホスト変数解決の効率について

ダイナミックインベントリは通常 --listと--hostオプションに対応する必要がある。

スクリプトで外部ソースからデータを取得するような処理を行う場合、ホスト数分、--hostパラメータを指定して呼び出されるため、ホスト数が多い場合に非効率となる（リモートのAPIコール×ホスト数）。
これを避けるため、インベントリオブジェクトの_metaトップレベル要素を追加することで、すべてのホスト変数を一度のスクリプト実行にて返すことができるため、効率的となる。


https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#tuning-the-external-inventory-script


### 検証スクリプト

長めのAPI呼び出しの待ち時間をシミュレート（５秒）に設定した、４ホスト分のダイナミックインベントリスクリプトを２つ用意する。
ひとつは_metaを追加（fast.py),もうひとつは_metaなし（slow.py）

それぞれのダイナミックインベントリを使用してansibleアドホックコマンドを--list-hostsオプション付きで実行する。
3回ずつ実行し、実行時間を計測


テスト実行
```
$./test.sh
--- fast version #1 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m5.594s
user    0m0.511s
sys     0m0.058s
--- fast version #2 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m5.529s
user    0m0.462s
sys     0m0.053s
--- fast version #3 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m5.650s
user    0m0.561s
sys     0m0.071s
-- slow version #1 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m25.900s
user    0m0.732s
sys     0m0.130s
-- slow version #2 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m25.993s
user    0m0.801s
sys     0m0.143s
-- slow version #3 ---
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.1.3
    192.168.1.4

real    0m25.937s
user    0m0.748s
sys     0m0.125s
```


fastバージョンは1回のスクリプト呼び出しで完了しているのに対し、
slowバージョンはスクリプトホスト数＋１回のスクリプト呼び出しが行われているため、
約5倍の実行時間となっている。

### 結論
* --list, --hostオプションは原則必要
* _metaトップレベル要素にてホスト変数を定義することで１回のスクリプト呼び出しで済む
* ホスト変数の定義が不要の場合、_metaオブジェクトのhostvarsは空でもOK