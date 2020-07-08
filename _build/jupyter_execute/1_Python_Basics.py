# Pythonの基礎

## `=`の意味と「オブジェクト」

変数$x$に値`10`を「代入」するには等号`=`を使う。

x = 10

また$x$の値を表示すには、次のように$x$を書いたセルを評価するだけである。

x

ここで「代入」に使った`=`について少し説明する。実は、`=`は「代入」ではない。更には、`x`と`10`は別物なのである。これを理解するために、多くの品物が保管されている大きな倉庫を考えてみよう。倉庫の管理者はどの品物がどこに保管されているかを記録する在庫リスト（記録帳やコンピューター・ファイル）を作成し、そこに品物が保管されている棚を示す記号を記入しているとしよう。この例を使うと、
* `10`　→　倉庫の棚に保管されている品物
* `x`　→　在庫リストに記載されている棚の記号

となる。品物と棚の記号は別物なのである。`Python`では、品物である`10`がコンピューター内のメモリーの所定の場所に保存され、その場所を示すのが変数`x`となる。即ち、`x`は品物`10`の実態とは異なる単なる「参照記号」なのである。
* `10`　→　PCのメモリーに保存されている情報
* `x`　→　参照記号

この点を明確にするために、上の式は「`x`に`10`を代入する」と考えるのではなく、「`10`を記号`x`に**割り当てる**」と考える。ここで、式を**右から左に**読んでいることに注意しよう。左から右に読んで「記号`x`を`10`に割り当てる」と考えないことを推奨する。意味は同じだが、`=`を右から左に読む（考える）ことを習慣づけることが、今後`Python`を勉強する上で重要となるからである。この点を示すために次のコードを考えてみよう。

x = x + 1

「？」と思うかもしれない。暗に方程式として考えるためであろう（私がそうだった）。これを右から左に読むとスッキリする。
1. 一番上のコードで`10`を`x`に割り当てたが、問題のコードの右辺の`x`がその`10`である。`10`に`1`を加えたものが`11`であり、それが右辺である。
1. `=`を使い右辺の`11`を左辺の`x`に割り当てている。この時点で、`10`の参照記号であった`x`は`11`の参照記号に変更される。

実際に`x`を表示してみよう。

x

この例では、記号`x`は`10`を指していたが`11`に変更されている。これは、同じ記号を複数の「品物」の参照記号に使えないためである。一方で、同じ「品物」を複数の参照記号に割り当てる事は可能である（例えば、`y=x`）。いずれにしろ「品物と参照記号の関係」は今の段階ではそれ程重要ではないが，先に進むにつれて重要性が増してくるので，今のうちにこのようなイメージを持つと良いだろう。

---
更にもう一点付け加える。`Python`を習うと「オブジェクト」という単語が必ず出てくる。今の内にイメージをつかむために自転車をオブジェクトの例として考えてみよう。通常の自転車には車輪が２つあり、サドルが１つあり、左右にペダルが２つある。これらの数字が自転車に関する**データ**である。またペダルを踏むことにより前に動き、ハンドルを右にきると右方向に進むことになる。即ち、あることを実行すると、ある結果が返されるのである。これは数学の**関数**と同じように理解できる。$y=x^2$の場合、$x$が`2`であれば$y$の値として`4`が返される。このように自転車はデータと関数が備わっているオブジェクトとして考えることができる。また、車輪の数やペダルを踏むことは自転車特有のデータと関数であり、他のオブジェクト（例えば、冷蔵庫）にはない。即ち、世の中の「オブジェクト」にはそれぞれ異なるデータと関数が存在していると考えることができる。

`Python`の世界でも「すべて」をこれと同じように考える。上のコードの`10`にもデータと関数が備わっており、それらを**属性**（attributes）と呼ぶ。`10`は単なる数字に見えるが、実は様々な属性から構成されるオブジェクトなのである。上の例の自転車のように、`Python`の「属性」は次の２つに分類される。`10`を例にとると、
1. `10`が持つ様々な**データ（属性）**（data attributes）（例えば、`10`という値や整数という情報）
1. `10`特有の関数である**メソッド（属性）**（method attributes）（例えば、加算、除算のように`10`というデータに働きかける関数）

を指す。自転車と冷蔵庫は異なるデータと関数を持つように、整数`10`と文字列`神戸大学`は異なるデータと関数を備えるオブジェクトなのである。この考え方は`Python`のすべてに当てはまる。即ち、Everything is an object in Python.

## ４つの基本データ型（Data Types）

Pythonでは全てがオブジェクトと話したが，オブジェクトの種類は無数にある。まず，その中心であるデータ型（data types）を紹介する。基本となる次の４つを考える。

* 整数型（int）
* 浮動小数点型（float）
* 文字列型（str）
* ブール型（bool）

整数型とは上の例で使ったもので，

157

も整数型である。Pythonには様々な関数が用意されており，その１つが`type()`である。それを使うとデータ型を確認できる。

type(157)

`int`はintegerの略で整数型を表す。

浮動小数点型は

10.24

のように小数点がついた数字である。`1`は整数型ですが，`1.0`は浮動小数点型となる。

文字列型はシングルクォート`'`かダブルクォート`"`の間に文字を入力します。

"apple"

'pear'

どちらを使っても同じだが，クォートの中でクォートを使う必要がある場合は，それぞれ違ったものを使う。例えば，

'He said "Good luck!" to me.'

また数字をクォートで囲むと文字列型になる。

'100'

type('100')

ブール型には`True`（真）, `False`（偽）がある。名前が示すように「真偽」を確認できる。例えば，

1==10

後ほど説明するが，`==`は「等しい」ということを意味する。また，`True`は`1`, `False`は`0`として計算される。

True==1 # Trueは１なのでTrueを返す

False==0 # Falseは0なのでTrueを返す

True + True

（注意）

`Python`には「クラス（class）」という概念がある。オブジェクトを生成するための設計図となるもので，この授業で説明はおこなわないが「型（types）」と同義と考えて良い。ちなみにクラス自体もオブジェクトである。

上では関数`type()`を使ってデータ型を確認したが，引数を画面上に表示する関数である`print()`を使うと「クラス名$\approx$データ型」が確認できる。

type(10)

print(type(10))

type(10.0)

print(type(10.0))

type('10')

print(type('10'))

type(True)

print(type(True))

コードのかなで想定されたデータ型と異なるデータ型を使うとがエラーが出たり，間違った結果につながる場合があるので，自信がない時は`type()`を使って確認すること。

この他類似する型に`complex type`（複素数型）と`NoneTyep`も存在する。以下の`None`とは「無」という意味である。

type(None)

print(type(None))

## コレクション系データ型

コレクション系とは上で説明した基本データ型の集まりとなるデータ型で，ここでは以下を簡単に説明する。

* リスト（list）
* タプル（tuple）
* 辞書（dict）
* 集合（set）

リストは`[]`を使う。

list0 = [10, 3 , 2]
list0

以下もリストの一例である。

list1 = ['A', True, 100]
type(list1)

print(type(list1))

上で説明したように、`print()`は定義したリストを画面上に表示する関数であり，`print()`を使うと`list`というクラス（class）であることも確認できる。

---
タプルは`()`を使って作成する。

tuple0 = ('A', True, 100)
print(tuple0)

リストと変わりないように見えるが，大きな違いは要素を変更できるかできないかという点である。

* リストの要素は変更可能
* タプルの要素は変更不可能

リストの要素の変更方法は以下で説明する。

**＜コメント１＞**

上で通常タプルは`(`と`)`を使って作成できると説明したが、実は、コンマ`,`によってタプルは定義されるため`(`と`)`は必須ではない。例えば、次のコードでもタプルとなる。従って、`(`と`)`はタプルを明確にするためと考えて良い。

tuple1 = 'B', False, -100

print(tuple1)
print(type(tuple1))

**＜コメント２＞**

１つの要素からなるタプルを作成する場合、コンマ`,`が必ず必要となる。

tuple2 = (10,)

print(tuple2)
print(type(tuple2))

コンマ`,`がないとタプルとはならない。

tuple3 = (10)

print(tuple3)
print(type(tuple3))

---
辞書はキー（key）と値（value）のペアとなって定義され，`:`を挟んで１つのペアとなる。全てを`{}`で囲み辞書を定義する。

dict0 = {'a':10, 'b':'Kobe'}

`dict0`には２つのペアがある。`a`のキーには値`10`が対応しており，`b`には`'kobe'`が設定されている。今の段階では辞書を使う目的が不明確でしっくりこないと思うが，勉強を進めるととてもパワフルなツールだと気づくだろう。

type(dict0)

print(type(dict0))

集合は使う機会がないので説明は割愛する。

## 要素のアクセス方法

まずリストの要素の数え方を説明する。次の図のように左から`0`，`1`，`2`...，右からは`-1`，`-2`，`-3`と数える。

```
   0   1   2   3   4   5  （左から数える） 
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
  -6  -5  -4  -3  -2  -1　（右から数える）
```

例えば

my_list = ['A', 'B', 'C', 'D', 'E', 'F']

の場合，`'A'`は０番目，`'B'`１番目，`'C'`は２番目と数える。例えば，`A`を抽出したい場合，

my_list[0]

最後の要素にアクセスするには次のようにする。

my_list[-1]

連続する複数の要素を選択する場合（スライシング）は`:`を使う。`:`の左側が選択する最初の要素で，`:`の右側が選択する最後の次の番号である（即ち，`:`の右側の番号の要素は含まれない。

my_list[1:4]

この例では１番目から3番目を選択している。`:`の左側の番号を省略すると`0`と解釈され，`:`右側を省略すると`-1`と解釈される。

my_list[:4]

my_list[1:]

タプルも同じように選択でる。

my_tuple = ('A', 'B', 'C', 'D', 'E', 'F')

my_tuple[2]

my_tuple[:3]

my_tuple[2:]

辞書も同じ方法でアクセスできる。

my_text = 'University'

my_text[1:4]

辞書の場合はキーで指定する。複数指定する場合は，`for loop`などの複雑な手法が必要となる。

my_dict = {'a':10, 'b':'apple', 'c':[1,2,5]}

my_dict['a']

my_dict['c']

## 変数名に使う記号について

上の例では`my_list`など好きなアルファベットの組み合わせを使いわかりやすい変数名にしている。しかし，変数の名前を作る上で守らなくてはならないルールがある。

* `(a-z, A-Z)`もしくは`_`（アンダースコア）で始める
* 最初の文字以外であれば`(a-z, A-Z)`と`_`に加え数字も可
* 長さに制限はない
* 小文字と大文字は異なる記号としてあつかう
* 次の単語は特定の目的のために事前に定義されているため，変数名としては使えない。

<pre>
and       exec     not
as 	   finally  or
assert    for      pass
break     from     print
class     global   raise
continue  if       return
def       import   try
del       in       while
elif      is       with
else      lambda   yield
except
</pre>

これらに加え，

* 変数の頭文字は小文字とする

というのが慣例（エラーにはならない）であり，大文字で始まる変数は`class`と呼ばれるオブジェクトに使う。

また`#`は実行されないコメントを書くときに使われる。以下の例では，`1+2`は実行されるが`#`で始まる行は無視される。

# この行はコメント
1+2

## 算術演算子

* `+`（加算）
* `-`（減算）
* `*`（乗算）
* `/`（除算）
* `//`（切り捨て除算; 実数の整数部分）
* `%`（剰余演算; 余りを取得する演算）
* `**`（累乗）

加算

type(1+1)

type(1+1.0)

'I' + 'like' + 'Kobe'

'I' + ' like' + ' Kobe'

[1, 2] + ['apple']

減算

1-0.5

乗算

type(2*2)

type(2*2.0)

[1,2,3]*3

除算

type(10/5)

切り捨て除算

5//2 # 5/2=2.5

剰余演算

5%2 # 5÷2＝2 余り 1

累乗

type(2**2)

type(2**2.0)

## 関係演算子

* `==`（等号）
* `!=`（等号不成立）
* `<`（小なり）
* `>`（大なり）
* `<=`（小なりイコール）
* `>=`（大なりイコール）

10 == 10

10 != 10

10 > 5

10>=10

10<=10

## 理論演算子

* a & b &nbsp;（aとbの両方） 
* a | b &nbsp;&nbsp;（a又はb又は両方）
* ~a &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;（aではない）

## if 文

`if`文を使うと，あるブール型（真偽）の条件のもとでコードを実行することが可能となる。例えば，`X`の値が正の場合，

`print(X, 'は正です')`

を実行したいとしよう。

X = 10

if X > 0:
    print(X, 'は正です')
else:
    pass

注意点
* `if`と`else` で始まる条件を示す行の最後は`:`となる。入れ忘れるとエラーとなる。
* `print()`の行は４つの半角スペースのインデントが入る。入れ忘れるとエラーとなる。
* `else`とは「`X>0`以外の場合」という意味。
* `pass`は「何もしない」という意味。

ここで`else`以下を省略してもエラーにはならない（結果も変わらない）。即ち，`else`以下がない場合は，それが省略されていると考えれば良い。

X = -1

if X > 0:
    print(X, 'は正です')
else:
    pass

if X > 0:
    print(X, 'は正です')

両方とも何も表示されない。

---

次に，複数の条件を導入するために次の関数を考える。

1. `print(X, 'は正です')`
1. `print(X, 'はゼロです')`
1. `print(X, 'は負です')`

`X`の値が正の場合は`1`を，ゼロの場合は`2`を，負の場合は`3`を表示したいとしよう。

X = -1

if X == 0:
    print(X, 'はゼロです。')
elif X > 0:
    print(X, 'は正です。')
else:
    print(X, 'は負です。')

注意点
* `if`, `elif`, `else` で始まる条件を示す行の最後は`:`となる。入れ忘れるとエラーとなる。
* `print()`の行は４つの半角スペースのインデントが入る。入れ忘れるとエラーとなる。
* `else`の行に`X<0`は不要（残りの可能性は`X<0`しかないため）
* `elif`は`else if`の省略形であり，２つ目の条件を定義する。
* `elif`は`if`と`else`の間に複数入れることが可能

## for ループ

`for`ループは同じコードを複数回リピートして実行したい場合に有効な方法である。例えば，次のリストにある名前を表示したいとしよう。

name_list = ['太郎', '次郎', '三郎', '四郎', '五郎']

for i in name_list:
    print(i)

説明と注意点
* `for`がある一行目は`:`で終わる。
* `i`は`name_list`にあるそれぞれの要素を示すダミー記号。
* `name_list`にある要素を最初から一つずつ実行する。
* 2行目は4つの半角スペースがインデントして入る。

`for`ループのよく使う例として以下を挙げる。この例では，リストに要素を追加する関数である`.append()`を使うが，この関数については以下でより詳しく説明する。

まず次のリストを定義する。

var_list = [1,2,3,4,5]

それぞれの要素の2倍からなるリストを作成するとしよう。

my_list = []  # 1

for i in var_list:  # 2
    my_list.append(2*i)  # 3

このループの考え方：

1. 空のリストの作成（ここに2倍の要素を格納する）
1. ここから`for`ループの始まり。`i`はリスト`[1,2,3,4,5]`の要素の代理変数であり，`var_list`の左から一つずつ次の行の`i`に該当する要素を代入して評価する。
1. `.append()`は`2*i`を`my_list`に追加するメソッド（関数と同義であり，後ほど違いを説明する）

`my_list`を表示しよう。

print(my_list)

```{note}
上の例では`for`ループの１行目に**リスト**を使って（`name_list`や`var_list`），`0`番目の要素から順に関数・メソッドを使った。これはリストが要素を１つずつ返すことができる反復可能なオブジェクトであるため可能となる。そのようなオブジェクトは**iterable`と呼ばれ，タプルや文字列，そして後で説明する`Numpy`の`array`も含まれる。
```

my_string = 'Kobe'

for s in my_string:
    print(s)

上で使った例では，3行のコードを書き`for`ループを使いリストを作成した。内包表記（list comprehension）を使うと同じ結果を1行のコード（one linerと呼ばれる）で得ることもできる。

[2*i for i in var_list]

色分けすると，上の`for`ループと内包表記は以下のような対応関係にある。

`for`ループ
<pre>
<font color=blue>my_list</font> = []
for <font color=red>i</font> in <font color=orange>val_list</font>:
    <font color=blue>my_list</font>.append(<font color=green>expression</font>)
</pre>

内包表記
<pre>
<font color=blue>my_list</font> = [<font color=green>expression</font> for <font color=red>i</font> in <font color=orange>val_list</font>]
</pre>

内包表記に`if`文を加えることも可能である。次の例では，偶数の2倍だけをリストに追加している。

[2*i for i in var_list if i % 2 == 0]

次の例では偶数を10倍にし，奇数を1/10にしている。

[10*i if i%2 == 0 else i/10 for i in var_list]

応用例として，次のリストの要素抽出について考えてみよう。

lst = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19] 

新たに`0`，`2`, `7`, `9`番目の要素からなるリストを作成したいとする。この場合,

[lst[0],lst[2],lst[7],lst[9]]

とすることも可能だが，内包表記を使うと次のコードになる。

idx = [0,2,7,9]
[lst[i] for i in idx]

何番目の要素にアクセスしているのかは`idx`で確かめる方が見やすい事がわかる。

## while ループ

`for`ループと同様，`while`ループもコードを複数回実行したい場合に使う。２つは以下の点で違いがある。

* `for`ループは与えられたリストに従いループが実行される。
* `while`ループはある条件が満たされるまでループが実行される。

例として，上で定義した`name_list`を表示するループを考える。

i = 0 #　iの値を0に設定

while i <= 4:
    print(name_list[i])
    i = i + 1

説明と注意点
* `while`がある一行目は`:`で終わる。
* `i`は条件を表すカウンターの役割と`name_list`の要素のインデックスの役割がある
* １行目の意味：$i<=4$の条件が満たされ散る限り，下に続くコードを反復実行する（タイプする文字数を少なくするために$i<5$と書く場合が多い
* ２行目の意味：`name_list`の`i`番目の要素を表示
* ３行目の意味：カウンター`i`の値を`1`増やす
    * 先に右辺を評価した後，それを左辺の`i`に割り当てる考える。（方程式としては考えない!）
* ２行目と３行目は４つの半角スペースがインデントとして入る。
* `while`ループは無限ループになる場合があるので注意しよう。

## 関数

コードを書くうえで関数は非常に重要な役割を果たす。Pythonには組み込み関数（事前に準備された関数; built-in functions）が数多くあり，上で使った`print()`と`type()`
も組み込み関数である。組み込み関数は様々なものが存在するが、ここではプログラマー自信が作成する関数について説明する。

（注意）

関数には引数が設定されるが（省略される場合もある）、複数の種類がある。ここでは基本となる引数のみを考えるが，引数の**位置**と`=`が重要な役割を果たすことになる。

最初の例は数字の2乗を計算する関数である。

def func_0(x):
    return x**2

説明：
* １行目：
    * `def`で始まり（`def`はdefinitionの省略形）`:`で終わる。
    * `func_0`が関数名，`x`が第１引数（ひきすう）であり唯一の引数である。
* ２行目：
    * `return`は評価した値を「返す」という意味。必ず`return`の前には4つのスペースが必要であり，ないとエラーになる。
    * `x**2`という返り値（戻り値）の設定をする

関数を評価するには，引数に数字を入れて実行する。

func_0(2)

（注意）
* 関数を定義する場合の引数（上の例では`x`)は「仮引数」（parameter）と呼ぶ。
* 関数を評価する際に関数に引き渡す引数（上の例では`2`）は「実引数」（argument）と呼ぶ。
* 本書では両方を「引数」と読んでいる。

---
引数が無い関数を定義することを可能である。

def func_kobe():
    print('I love Kobe :)')

func_kobe()

### 引数の位置が重要

上の例では引数が１つしかないが，引数が複数ある場合にその位置が重要になってくる。次の例を考えよう。

def func_1(a, b):
    return a/b

func_1(10, 2)

`a`が第1引数、`b`が第2引数である。引数の順番を間違えると意図しない結果につながる。

func_1(2, 10)

もちろん，3つ以上の位置引数も設定可能である。次の例で使う`sum()`は，数字の合計を計算する関数であり，`()`の中にはタプルやリストが入る。即ち，タプルやリストの要素の合計を返す関数となる。

def func_2(a, b, c, d):
    return sum((a, b, c, d))

func_2(10, 20, 30, 40)

### 実行する際に`=`を使う

**関数を実行する際**に、引数に`=`を使って値を指定することも可能である。

func_1(a=10, b=2)

この場合，引数の順番を変えることが可能となる。それが関数を実行する際に`=`を使う利点である。

func_1(b=2, a=10)

この場合，全ての引数に`=`を使わないとエラーとなる。

func_1(10,a=2)

理由は最初の`10`を`a`の値と解釈されるためである。一方で，引数の位置が揃っていれば，全ての引数に`=`を付ける必要なない。

func_2(10, 20, d=40, c=30)

ここでも引数の位置の重要性がうかがえる。

### 定義する際に`=`を使う

**関数を定義する際**、`=`を使って引数のデフォルトの値を設定することができる。即ち，引数を入力すると入力された数値を使うが，引数を入力しない場合は引数を予め設定した値（デフォルトの値）が使われて評価される。次の例では`c`のデフォルトの値が`10`に設定されている。

def func_3(a, b, c=10):
    return sum([a,b])*c

`c`の値を与えずに評価してみる。

func_3(2, 3)

次に`c`にデフォルトと異なる値を設定してみる。

func_3(2, 3, 100)

（Note）
* 関数を実行する際に`=`無しで関数に渡される引数は，その位置が重要であるため「位置引数」と呼ばれる。
* 関数を実行する際に`=`付きで関数に渡される引数は「キーワード引数」と呼ばれる。

### `*args`

`func_0()`の引数の数は1に，`func_1()`の引数は2に，`func_2()`の引数は4に設定されている。関数を実行する際，引数の数が指定された数と合わないとエラーが発生する。では，位置引数の数が事前に決まっていない場合はどうするのか。例えば，`func_2(1,2)`と書いても`func_2(1,2,3,4,5,6)`と書いても引数の合計を計算したいとしよう。このような場合に`*args`を使う。

def func_4(*args):
    return sum(args)

func_4(1,2)

func_4(1,2,3,4,5,6)

`*args`は何を返しているのだろうか。実は，`args`はタプルを返し，`*args`はタプルから取り出した全ての要素を返している。これを理解するために次の例を考えよう。

print((1,2,3))

ここではタプル`(1,2,3)`を表示している。次に、`*`を加えてみる。

print(*(1,2,3))

これは次のコードの返り値と同じである。

print(1,2,3)

即ち、`*`はタプル`(1,2,3)`の全ての要素を取り出して`1,2,3`に置き換えている。このような置き換えを「展開する」（unpack）と呼ぶ。この`*`の役割を念頭に次の関数を使い`*`と`args`の役割を分けて考えてみる。

def func_5(*args):
    print(args)

func_5(1,2,3)

`args`自体は引数のタプルであることがわかる。次に`print()`の`args`に`*`を加える。

def func_5(*args):
    print(*args)

func_5(1,2,3)

ここから分かることは、`func_5(*args)`の`args`自体は引数のタプルであり，`*args`はタプルを展開したものである。`print(*args)`の`*args`もタプルを展開したものである。このことを念頭にもう一度`func_4(*args)`を考えてみよう。`def func_4(*args)の`の`args`は引数になる数字のタプル（例えば，`(1,2,3)`）であり，`*args`はそれを展開したものである。`return sum(args)`の`args`はもちろんタプルである。この性質を使うことにより、関数に任意の数の引数を指定することが可能となる。

＜コメント＞
* `*args`の`args`はarguments（引数）の省略形である。
* `*args`の代わりに`*aaa`や`*abc`としても同じ結果をえることができる。しかし`*args`と書くのが慣例である。

次の例は`*args`と引数を一緒に使うケースである。

def func_6(a, *args):
    return a*sum(args)

func_6(10,2,2,2)

＜注意＞

必ず`*args`は，位置引数の次に置くこと。これは`*args`が「その他全ての位置引数」という意味であるためであり、全ての位置引数の後に位置してこそ意味があるからである。言い換えると、`*args`は位置引数の終わりを意味する。

### `lambda`関数

上の例では`def`を使う方法を紹介したが，複雑な関数を定義する場合によく使われる。一方で単純な関数の場合，より簡単な方法がある。それが`lambda`関数である。例として，$x^2$を計算する関数を考えよう。

func_7 = lambda a: a**2

func_7(2)

複数の引数の場合

func_8 = lambda a, b: a*b

func_8(2,3)

引数が無い場合

func_9 = lambda : print('I love Kobe ;)')

func_9()

## 関数とメソッド

Pythonには「関数（functions）」と「メソッド（methods）」があり，基本的には同じ働きをする。ではどう異なるのか。これを理解するためには，数字の`1`を含めて「全てがオブジェクト」というPythonの根底にある考え方を思い出そう。簡単に説明すると，オブジェクトにもともと備わっているかどうかで「関数」と「メソッド」に区別されると思って十分である。

例えば、上で定義した`func_0()`や`func_7()`は関数であり，特定のオブジェクトに働きかけるものではない。単に引数から計算した返り値を出力しており，計算できる引数である限りどのようなオブジェクトでも構わない。一方，メソッドは元々オブジェクトに備わっている関数である。例として，文字列`I love 神戸!`を考えよう。`I love 神戸!`というオブジェクトには様々なメソッドが用意されており，そのリストを`dir()`という関数を使うことにより表示できる。

moji = 'I love 神戸!'
dir(moji)

アルファベット順に並んでいることが分かる。例として，`upper`を使ってみる。

moji.upper()

`upper`はアルファベットを大文字に変換するメソッドであり，`moji`にもともと備わっている関数である。

```{note}
* `moji`の後に`.upper()`が来ており`()`に引数がないように見えるが，実は先にある`moji`を引数として`upper()`を実行しているのである。
* `upper`はメソッドの名前であって，実行するには`()`が必要となる。つけ忘れるとオブジェクトの型が表示されることになる。これは関数と同じである。

```

`_`はアンダースコア（underscore）と呼ぶが，２つ連続した場合`__`となりダブル・アンダースコア（double underscore）と呼ぶ。長いのでダンダー（dunder）と省略する場合が多々ある。上のリストにはこのダンダーに挟まれたメソッドが含まれている（ダンダー・メソッドと呼ばれる）。これらは対応するコードを実行するとPythonが裏で使うメソッドであるため，直接コードに書く必要はない。例えば，次のコードを考えてみよう。

moji + ' (^o^)/'

`+`を使い文字列を結合しているが，この裏でPythonが使っているメソッドが`__add__`である。

moji.__add__(' (^o^)/')

`+`は`__add__`の便利な省略形を考えれば良いだろう。「全てがオブジェクト」なのでリストもそうである。

list_0 = [4,3,9,0,1]

dir(list_0)

この中に`append`とあるが，`for`ループの説明で使ったメソッドである。

list_0.append(100)

list_0

他に`sort`とあるがこれは要素を昇順に並び替えるメソッドである。

list_0.sort()

list_0

是非他のメソッドも試して欲しい。またオブジェクトのメソッドを調べる場合，`dir()`の出力は見にくいので[`see`モジュール](https://pypi.org/project/see/)を使うのがおすすめである（モジュールについては次のセクションを参照）。もちろん，Pythonやモジュールの説明書（docs）をチェックするのも必要である。

## パッケージとモジュール

Pythonには組み込み関数が多く用意されている。例えば，[このリンク](https://docs.python.org/ja/3/library/functions.html)を参照。しかし組み込み関数には計量経済学用の便利な関数は用意されていない。そこで活躍するのがモジュール（modules）やパッケージ（package）と呼ばれるもである。もちろん計量経済学以外のモジュールやパッケージが無数にあり，使う用途（例えば，グラフを描く）に沿って読み込むことになる。２つの違いを簡単にいうと

* モジュールは１つのファイル（.py）にまとめられた関数群であり，
* パッケージは複数つのファイル（.py）で構成されている（フォルダーにまとめられている）

となる。従って，モジュール全体を読み込んだり，あるパッケージの１つのモジュールだけを読み込むということも可能である。

まず例として`math`モジュールを考える。名前が示すように数学用のモジュールである。使うためには`import`を使って読み込む必要がある。

モジュールの全てを読み込むとモジュール内の全ての関数が使用可能となる。

import math

math.sqrt(4)    # sqrt（）とはルート

この場合モジュール名が必要とり，「`math`モジュールの`sqrt`」を指定しているという意味である。これは他のモジュールとバッティングしないようにするためである。

モジュール名が長い場合は，短い名前で読み込むことも可能である

import math as m

m.sqrt(9)

モジュール内の特定の関数だけを読み込むことも可能である。

from math import sqrt, log   # logは自然対数で, sqrtの両方を読み込む

「`math`モジュールから`sqrt`と`log`を読み込む」と理解すれば良いだろう。

sqrt(10)

この読み込み方法の利点はモジュール名を省略できることである。しかし他のパッケージやモジュールと同じ関数がある場合は，後で`import`したものが優先されるので注意が必要だ。

`import`文はファイルの最初に書き，どのモジュールが導入されるかを明示的に示すとわかりやすいだろう。

前のセクションで`dir()`を使いオブジェクトの属性を調べたが，その際`see`を使うとリストが見やすくなると説明した。それを使ってみよう。

from see import see  # seeモジュールから関数seeを導入

see(moji)

ダンダー・メソッドは省略され，メソッドには`()`が追加され見やすくなっている。

````{note}
`see`モジュールはAnacondaに含まれていないので，TerminalもしくはGit Bashで以下を実行して事前にインストールする必要がある。
```
$ pip install see
```
````

## よく使う組み込み関数

# 表示
print('私は神戸大学の学生です。')

# 様々なものからリストを返す関数
list()  # 空のリスト

# 0から9までの整数を用意する関数 
range(10)

list(range(0,10))

## エラー

エラー（Errors）は以下の２つに分けられる。
1. 構文エラー（Syntax Errors）
    * 構文自体が間違っている場合に発生するエラー（例えば，スペル間違い）。
1. 例外（Exceptoins）
    * 構文は間違っていなくてもコードの実行中に発生するエラー（例えば，数字を`0`で割る）

---
＜＜コメント＞＞
* エラーが発生するとエラー・メッセージが表示されるが，多くの場合，エラー・メッセージにエラーの理由のヒントがあるので確認することを強く推奨する。はじめは意味が分からないかも知れないが，パターンがあるので慣れると直ぐに理解できるケースも多くあるだろう。
* 例外の場合，最初にエラーが発生するとそれに付随して他の場所でもエラーが誘発される場合がある。`Python`はエラーを追跡し，最後に確認したエラーをメッセージの一番最後に示すことになる。

### 構文エラー

#### 例１

（正）`print`<br>
（誤）`primt`

primt('hello')

* 矢印（---->）でエラー箇所が示されている。
* `NameError`として最終行にスペル間違いである`primt`が示されている。

#### 例２

次のセルの３行目の終わりに`:`が抜けている。

a = 3

for i in range(0,3)
    print(i)

* `line 3`はセル内の３行目を示している。
* `SyntaxError`として最後の行で`:`が足りない箇所を`^`で指し示している。

#### 例３

括弧を閉じていない。

(2.1 + 1.5)/(10.0 + 1.0 + 3.2 

この場合，`Python`はプログラマーがどこに`)`を入れようとしたかは分からない。従って，最後に`)`が入ると想定して`^`を文末に置いている。

---
＜＜コメント１＞＞<br>
`()`の場合，改行しても構わない。一行が長くなる場合，`(`と`)`の間で改行することができる。

(10, 20, 30,
 40, 50, 50)

＜＜コメント２＞＞<br>
文字列を改行する場合は次の例のように`\`を使う。

'神戸大学\
経済学部'

### 例外

#### 例１

`0`が分母にある。

2.0 + 1/0

#### 例２

定義されていない変数`xx`が使われている。

10 + xx * 2

#### 例３

文字列とfloatを足している。

'3' + 10

## ヘルプ

組み込み関数`help()`を使うと関数やモジュールなどの`Docstring`と呼ばれる説明を表示させることができる。例えば，`print()`を例として挙げる。

help(print)

引数は関数名であり`()`は付いていないことに留意しよう。`()`を付けると`print()`を評価した結果に対しての説明が表示されることになる。英語での説明だがパターンを理解すればこれだけでも有用に感じることだろう。 

`help()`の代わりに`?`を使うこともできる。

print?

## Pythonの基本のまとめ（日英対訳）

[日本語](https://learnxinyminutes.com/docs/ja-jp/python3-jp/)

[英語](https://learnxinyminutes.com/docs/python3/)