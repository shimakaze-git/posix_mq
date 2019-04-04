## PythonでPOSIXのMessageQueue を使う

- 送信側はドンドン送信できる。
- 受信側は逐次読み込んで取り出せる。
- データが空なら、受信側はブロックされる。


## POSIX message queue を確認

````
$ ls /dev/mqueue/

````

## 参考資料

http://takuya-1st.hatenablog.jp/category/python?page=1490714821