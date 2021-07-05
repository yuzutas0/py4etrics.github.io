#!/usr/bin/env python
# coding: utf-8

# # NumPy

# If you come here without expecting Japanese, please click [Google translated version](https://translate.google.com/translate?hl=&sl=ja&tl=en&u=https%3A%2F%2Fpy4etrics.github.io%2F2_NumPy.html) in English or the language of your choice.
# 
# ---

# ## array

# このパッケージは，数値計算をする上で重要な役割を果たし，特に，行列計算に威力を発揮する。`NumPy`は「ナンパイ」と読む。
# 
# 慣例として`np`として読み込む。

# In[1]:


import numpy as np


# 基本となる関数が`np.array()`であり，次のコードでは１次元配列を作る。

# In[2]:


arr = np.array([10, 20, 30, 40, 50])
arr


# In[3]:


type(arr)


# 次に２次元配列、即ち、行列を作る。

# In[4]:


mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
mat


# In[5]:


print(type(arr))
print(type(mat))


# `arr`と`mat`は`NumPy`の`ndarray`（`n`次元`array`）というデータ型（クラス）である。`[]`に囲まれた数字が並んでいるがリストとではない。従って，要素を抽出して直接リストとして扱うことはできない。そのためにはリストへの変換が必要になるが，その方法については後述する。

# ## １次元配列：要素の抽出

# `arr`の要素を抽出するには要素のインデックスを使う。

# In[6]:


arr[1]


# 複数の要素を抽出するにはインデックスをリストとして使う。

# In[7]:


arr[[0,1,3]]


# 要素を連続で抽出するスライシング（slicing）も使うことができる。

# In[8]:


arr[1:4]


# ## ２次元配列：要素の抽出

# 第$i$行目の第$j$列目要素にアクセスするためには`mat[i,j]`と書く。`[,]`の`,`を挟んで左が行を表し，右が列を示す。
# ```
# [行のインデックス,列のインデックス]
# ```
# 
# コードはキーストロークが少なく，簡単なものが良いと考えられている。一方で，`Python`は初心者に易しい言語だと言われるが，それでも関数・メソッドの数は膨大で，そのオプションとの組み合わせを考えるとまさしく「無数」にあると言っても過言ではない。そのため初心者にとって関数の使い方やオプションの書き方を間違う可能性は小さくない。さらに，自分が書いたコードを数週間・数ヶ月後に読み直すと，何をしようとしているのか分からないという状況が生じることもある。従って，初心者にとっては以下の点が非常に重要になる。
# 
# * 間違いにくいコードの書き方を覚える。
# * 高い可読性を意識したコードの書き方を覚える。
# 
# このスタンスに基づいて以下のルールに従って説明する。
# 
# 1. `[,]`内の`,`を省略可能な場合であっても省略しない。
# 2. `[,]`内の`,`の左または右を省略できる場合であっても省略しない。
# 
# 行または列を連続選択する（slicing）場合を考えよう。以下で説明するように`:`を使うが
# ```
# start:end
# ```
# となる。ここで`start`とは選択する要素の最初インデックスであり，`end`は選択する最後の要素の次のインデックスである（リストの場合と同じ）。上のルールに従うと，
# 
# * `,`の左または右が`:`のみの場合，「全て」という意味になる。
# * `:`の左を省略すると「最初から」という意味になる。
# * `:`の右を省略すると「最後まで」という意味になる。
# 
# これを読むだけでは分かりにくいと思うので，以下の例に目を通してもう一度この箇所の説明を読んむことを推奨する。

# In[9]:


mat[0,1]


# 第$i$行の抽出は`mat[i,:]`で可能である。`:`は「列の全て」という意味になる。

# In[10]:


r0 = mat[0,:]
r0


# 抽出した行は上で説明した１次元配列なのでインデックスやスライシングを使って要素にアクセスすることができる。

# 複数の行の抽出は次の方法で可能である。

# In[11]:


mat[1:3,:]


# 第３行目は含まれないことに注意しよう。リストの要素の取り出し方と同じように`:`の右のインデックスの行は含まれない。
# 
# **（注意）**
# 
# `,:`を省略して`mat[1:3]`と書いてもエラーは発生せず同じ結果が返されるが，`,:`があることにより，行を抽出しており列は全て選択されていることが明示的になる。
# 
# 
# 第$i$ 列目を抽出したい場合は次のコードになる。

# In[12]:


mat[:, 1]


# 複数列の抽出は以下のようにする。

# In[13]:


mat[:, 1:3]


# `:`の役割を考えると以下は`mat`自体である。

# In[14]:


mat[:,:]


# ## 行列計算

# まず２つの行列（２次元配列`array`）を作成する。

# In[15]:


m1 = np.array([[1, 1], [1, 1]])
m1


# In[16]:


m2 = np.array([[2, 2], [2, 2]])
m2


# **行列の和**
# 
# 要素ごとの和となる。

# In[17]:


m2 + m1


# **行列の差**
# 
# 要素ごとの差となる。

# In[18]:


m2 - m1


# **行列のスカラー積**
# 
# 与えられた定数とそれぞれの要素の積となる。

# In[19]:


10 * m1


# In[20]:


m1/2  # 1/2をかけるのと同じ


# **行列の積：バージョン１**
# 
# `*`を使うと要素どうしの積となる。数学で学んだ行列の式とは異なるので注意すること。

# In[21]:


m1*m2


# **行列の積:バージョン２**
# 
# `@`を使うと数学で学ぶ行列の積となる。

# In[22]:


m1@m2


# `numpy`の関数`dot()`は`@`と同じとなる。

# In[23]:


np.dot(m1,m2)


# **転置行列**
# 
# 数学で学ぶ転置行列と同じ。`m3`を使って説明する。

# In[24]:


m3 = np.array([[1,2,3],[4,5,6]])
m3


# `m3`のメソッド`transpose()`を使う。

# In[25]:


m3.transpose()


# `.transpose()`の省略形として`.T`を使うこともできる。

# In[26]:


m3.T


# **逆行列**
# 
# 数学で学ぶ逆行列である。`m4`を使い説明する。逆行列を計算するために`numpy`の`linalg`（linear algebra, 線形代数）というサブパッケージの中にある`inv`という関数を読み込む。

# In[27]:


from numpy.linalg import inv

m4 = np.array([[1,2],[3,4]])


# In[28]:


inv(m4)


# ## NumPy使用時によく使う属性とメソッド

# 以前も説明したが、メソッドとはオブジェクト特有の関数であり、オブジェクトの属性の１つである。もう１つの属性の種類にデータ属性（例えば，行数）がある。あるオブジェクトにどのような属性があるかは関数`dir()`を使うことにより確認できる。

# In[29]:


dir(m3)


# このリストの中に`transpose()`や`T`があるのが確認できる。この中でよく使うのが`shape`であり，行と列の数を確認する場合に有用なデータ属性である。

# In[30]:


m3.shape


# データ属性には`()`がない。一方，メソッド属性は`()`が必要となる。言い換えると，メソッドの`()`は「実行する」ということを意味する。
# 
# 次に，抽出した行または列をリストに変換するメソッドについて説明する。

# In[31]:


r0 = mat[0,:]


# In[32]:


type(r0)


# `r0`のデータ型は`NumPy`の`ndarray`である。これをリストに変換するために`tolist()`というメソッドを使う。

# In[33]:


r0_list = r0.tolist()

r0_list


# In[34]:


type(r0_list)


# ## よく使うNumPy関数

# **ルート $\left(\sqrt x\right)$**

# In[35]:


np.sqrt(4)


# `sqrt`は square root の略。

# **底が$e$の指数関数（$e^x$）**

# In[36]:


np.exp(10)


# `exp`は exponentiation の略

# **自然対数（$\log_ex$または$\ln x$）**

# In[37]:


np.log(10)


# **`0`が$N$個の`array`を作る。**
# ```
# np.zeros(N)
# ```

# In[38]:


np.zeros(10)


# **`1`（float）が$N$個の`array`を作る。**
# ```
# np.ones(N)
# ```

# In[39]:


np.ones(10)


# **$a$から$b$までの区間を等間隔に割った$N$個の数字を返す。**
# ```
# np.linspace(a,b,N)
# ```

# In[40]:


np.linspace(0,1,5)


# **$a$から$b$までの区間で$m$ステップずつ増加し等間隔に割った数字を返す（$b$は含まない）。**
# 
# ```
# np.arange(a,b,m)
# ```
# `m = 1`の場合，組み込み関数の`range(a,b)`と同じ数字を生成するが，返り値が`array`であることが異なる。

# In[41]:


np.arange(5,10,0.5)


# **標本平均**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.mean(x)`$=\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$

# In[42]:


xx = [1,2,3,4,5,6]
np.mean(xx)


# **標本中央値**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.median(x)`

# In[43]:


np.median(xx)


# **標本分散**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.var(x, ddof=0)`$=s_x^2=\dfrac{1}{n-\text{ddof}}\sum_{i=1}^n\left(x_i-\bar{x}\right)^2$（`ddof=0`がデフォルト）
# 
# （注意）計量経済学で習う分散の不偏推定量は`ddof=1`が必要！

# In[44]:


np.var(xx,ddof=1)


# **標本標準偏差**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.std(x, ddof=0)`$=s_x=\sqrt{s_x^2}$  （`ddof=0`がデフォルト）
# 
# （注意）標本標準偏差の場合，必ずしも`ddof=1`により不偏推定量とはならないが，通常`ddof=1`を用いる。

# In[45]:


np.std(xx,ddof=1)


# **標本共分散**
# 
# 2次元以上の`array`やリストの場合
# 
# `np.cov(xy, ddof=0)`$=c_{xy}=\dfrac{1}{n-\text{ddof}}\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})$（`ddof=0`がデフォルト）
# 
# （注意１）計量経済学で習う分散の不偏推定量は`ddof=1`が必要！
# 
# 下の計算結果
# 
# * $c_{xy}=-0.6$
# * $s_x^2=3.5$  (\[1,2,3,4,5,6\]の分散）
# * $s_y^2=4.4$  (\[1,6,2,5,3,1\]の分散）

# In[46]:


x = [1,2,3,4,5,6]
y = [1,6,2,5,3,1]

cov_xy = np.cov([x,y],ddof=1)
cov_xy


# In[47]:


from myst_nb import glue
varx = cov_xy[0,0]
vary = cov_xy[1,1]
covxy = cov_xy[0,1]
glue('varx', varx, display=False)
glue('vary', vary, display=False)
glue('covxy', covxy, display=False)


# ここでそれぞれの数字は次を表している。
# * {glue:text}`covxy:.1f`：`x`と`y`の共分散であり，次のように値を抽出できる。
#     ```
#     `cov_xy[0,1]` もしくは　`cov_xy[1,0]`
#     ```
# * {glue:text}`varx`：`x`の分散であり，次のように値を抽出できる。
#     ```
#     `cov_xy[0,0]`
#     ```
# * {glue:text}`vary`：`y`の分散であり，次のように値を抽出できる。
#     ```
#     `cov_xy[1,1]`
#     ```

# **標本相関係数**
# 
# 2次元以上の`array`やリストの場合
# 
# `np.corrcoef(xy)`$=r_{xy}=\dfrac{c_{xy}}{s_x\cdot s_y}$
# 
# （注意）`ddof`の影響はない。
# 
# 下の計算結果
# * $r_{xy}=-0.152...$
# * $r_{xx}=r_{yy}=1$

# In[48]:


corr_xy = np.corrcoef([x,y])
corr_xy


# In[49]:


from myst_nb import glue
corrx = corr_xy[0,0]
corry = corr_xy[1,1]
corrxy = corr_xy[0,1]
glue('corrx', corrx, display=False)
glue('corry', corry, display=False)
glue('corrxy', corrxy, display=False)


# ここでそれぞれの数字は次を表している。
# * {glue:text}`corrxy:.8f`：`x`と`y`の相関係数であり，次のように値を抽出できる。
#     ```
#     `corr_xy[0,1]` もしくは　`corr_xy[1,0]`
#     ```
# * {glue:text}`corrx`：`x`と`x`の相関関係であり，次のように値を抽出できる。
#     ```
#     `corr_xy[0,0]`
#     ```
# * {glue:text}`corry`：`y`と`y`の相関係数であり，次のように値を抽出できる。
#     ```
#     `corr_xy[1,1]`
#     ```

# ## array vs list

# ここでは`list`と`NumPy`の`array`の重要な違いについて説明する。
# 次のリストのそれぞれの要素に`10`を足したいとしよう。

# In[50]:


list0 = [1.0, 2.0, 3.0, 4.0, 5.0]


# `for`ループを使うと次のようになる。

# In[51]:


list1 = []
for i in list0:
    list1.append(i + 10)

list1


# もう１つの方法として内包標記（list comprehension）がある。

# In[52]:


list2 = [i + 10 for i in list0]
list2


# どちらの方法を使ったとしても複雑さが残る。また次のコードでは`10`を最後に追加するだけである。

# In[53]:


list0 + [10]


# より簡単なコードで実行できれば良いが，以下のコードではエラーが発生する。

# In[54]:


list0 + 10


# ---
# これを実現するのが`NumPy`の`array`である。
# 
# まず`array`を作成する。

# In[55]:


arr0 = np.array(list0)
arr0


# In[56]:


arr0 + 10


# この機能はベクトル演算（Vectorization）と呼ばれ、ループを使わずに個々の要素に直接働きかけ計算している。上記のコードは次の計算を行っている。

# In[57]:


arr0 + np.array([10]*5)


# 裏で`arr0`の長さに合わせて`10`を「拡張」し計算している。この機能により、より高速な計算が可能となるばかりか、より短いコードでそれを実現できる。`+`, `-`, `*`, `**` や他の関数にも同様に使うことができる。以下で例を挙げる。

# In[58]:


arr0 - 5


# In[59]:


arr0 * 10  


# In[60]:


arr0 ** 2


# In[61]:


np.sqrt(arr0)


# In[62]:


np.log(arr0)


# 次の計算も可能である。

# In[63]:


y = arr0 * 2 + np.sqrt(arr0) + 10
y


# この機能は`NumPy`の行列でも有効である。

# In[64]:


mat0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat0


# In[65]:


mat0 * 10


# In[66]:


np.sqrt(mat0)


# In[67]:


np.log(mat0)

