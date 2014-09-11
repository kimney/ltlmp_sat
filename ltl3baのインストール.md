

インストール方法を確かめるまでの残滓
=============================


1. Buddy の インストール
---------------------
Buddy をダウンロードする．
Makefileに以下を実行しろと書いてある．

> ./configure
> make
> make install

#### configure
以下を実行した

> ./configure // --includedir=/usr/local/include --libdir=/usr/local/lib
> make

Macでもターミナルからやるのは大体 /usr/local/* にインストールするらしい．

インストールされるものは，環境による？
例えば，同じMacでもデフォルトと，homebrewとかでツールを揃えているのとでは環境が違うので，ビルドされるものも違う．
configureはそんな感じ．



2.Makefileの書き換え
------------------


[](http://railsapps.github.io/xcode-command-line-tools.html)
error: reference to 'is_empty' is ambiguous と出て，コンパイルが通らなかった．
名前のかぶり先をみたら，Xcodeやらが表示されていたので，Marvericksにアップグレードした影響かなと思い，
最新のXcode Command Line Tools をインストールした．
-> どう？

xcode-select -switch /Library/Developer/CommandLineTools
で /Applications/Xcode.app/Contents/Developer から /Lib... に切り替えた．

-> 解決しない
http://stackoverflow.com/questions/19644816/linking-c-from-c-in-os-x-mavericks
name Mangling の犠牲者という言葉があったので，


10時間の格闘の後，gccの古いバージョンをインストールすることにした．

> http://toggtc.hatenablog.com/entry/2012/01/28/224006
> http://www.absolute-keitarou.net/blog/?p=984

...?


2014年8月現在の最新の解決法は以下らしい

http://blog.cyclogy.com/2014/02/08/homebrew-versions/


```
sudo brew install homebrew/versions/gcc43
```

頼む，動いてくれー！

\が入っていると動かない情報を得たので，\ の記述を消すべくリネーム．
ld: library not found for -lcrt0.o のエラーは出なくなるか？
変わらなかった．

g++-4.3 -O3 -DNXT -I/Users/taka/Downloads/buddy-2.4/src/ -o ltl3ba parse.o lex.o main.o trans.o buchi.o cset.o set.o mem.o rewrt.o cache.o alternating.o generalized.o optim.o queue.o -L/Users/taka/Downloads/buddy-2.4/src/.libs/ -lbdd -static
ld: library not found for -lcrt0.o
collect2: ld returned 1 exit status
make: *** [ltl3ba] Error 1

ここで躓く．

http://stackoverflow.com/questions/3801011/ld-library-not-found-for-lcrt0-o-on-osx-10-6-with-gcc-clang-static-flag

-static オプションが無い？
ltl3baのMakefile から-staticを取ってみる． コンパイルは通る．

> http://d.hatena.ne.jp/kanonji/20121018/1350538932
> https://github.com/peteg/hBDD/tree/master/hBDD-CMUBDD

dylibを作るとか試したが，特に動かないし問題がややこしくなっていく．

dylibとか出てくるから，パスにインストールしないとだめなのかなと思い，buddyのMakefileのLib,Configureをもとに戻す．書き換える．
おっ動いた．
おｋ，最初からまとめると，

gcc のバージョンを 4.3 (gcc-4.3) にして，
Buddy, ltl3ba のMakefile中のgccとg++をgcc-4.3とg++4.3に書き換える．

in Buddy
/usr/local/* にインストール

```
./configure
make
make install
```

in ltl3ba
Makefile中の -static オプションを外す

```
make
```

-staticオプションは，Macでは設計思想から動かないらしいので，NGらしい．
http://stackoverflow.com/questions/5259249/creating-static-mac-os-x-c-build




