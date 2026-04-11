# Python 中級 レッスン

## 1. イテレータとは何か
イテレータとは、値を 1 つずつ順番に取り出せる仕組みです。

まずは普段よく見る `for` 文から考えます。

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

このコードは、リストから値を 1 つずつ取り出して表示しています。

実は `for` 文の裏側では、「次の値を順番に取り出す仕組み」が動いています。これがイテレータです。

次のコードで、その考え方を少しだけ見てみます。

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

このコードは、リストから値を 1 つずつ手動で取り出しています。

- `iter(numbers)` でイテレータを作る
- `next(iterator)` で次の値を取り出す

という流れです。

### 要点
- イテレータは、値を順番に 1 つずつ取り出す仕組みです。
- `for` 文はこの仕組みを自動で使っています。

## 2. ジェネレータとは何か
ジェネレータとは、`yield` を使って値を少しずつ返す仕組みです。

まずは普通の関数です。

```python
def get_numbers():
    return [1, 2, 3]

print(get_numbers())
```

この関数は、リスト全体をまとめて返します。

次はジェネレータです。

```python
def get_numbers():
    yield 1
    yield 2
    yield 3

for number in get_numbers():
    print(number)
```

このコードでは、値を 1 つずつ順番に取り出せます。

`return` は「ここで関数を終えて結果を返す」動きです。  
`yield` は「いったん値を返すが、続きから再開できる」動きです。

### 要点
- `yield` を使う関数はジェネレータになります。
- ジェネレータは、値をまとめて持たずに少しずつ扱いたいときに便利です。

## 3. ジェネレータが役立つ場面
たくさんのデータを扱うとき、全部を先にリストへ入れる必要がない場合があります。

まずは少し回りくどい例です。

```python
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

for value in squares_list(5):
    print(value)
```

次はジェネレータで書き換えた例です。

```python
def squares_gen(n):
    for i in range(n):
        yield i * i

for value in squares_gen(5):
    print(value)
```

後者は、必要になったときに 1 つずつ値を作ります。

特に件数が多いときは、ジェネレータの方が無駄なメモリを使いにくくなります。

### 要点
- すべての結果を先に作らなくてよいとき、ジェネレータが向いています。
- 「順番に処理する」場面でよく使われます。

## 4. デコレータとは何か
デコレータとは、関数に機能を追加する仕組みです。

まずはデコレータを使わない例です。

```python
def greet(name):
    print("start")
    print(f"Hello, {name}")
    print("end")
```

このままだと、別の関数にも同じ「start/end の表示」を入れたいとき、同じコードが増えやすくなります。

次のように関数を包む形にすると、共通処理をまとめられます。

```python
def log_call(func):
    def wrapper(name):
        print("start")
        func(name)
        print("end")
    return wrapper

def greet(name):
    print(f"Hello, {name}")

greet = log_call(greet)
greet("Aki")
```

このコードでは、`greet` にログ表示の機能を追加しています。

### 要点
- デコレータは、元の関数を包んで機能を足す考え方です。
- 共通処理をまとめたいときに役立ちます。

## 5. `@` を使ったデコレータ
Python では、さきほどの書き方を `@` でもっと読みやすく書けます。

```python
def log_call(func):
    def wrapper(name):
        print("start")
        func(name)
        print("end")
    return wrapper

@log_call
def greet(name):
    print(f"Hello, {name}")

greet("Aki")
```

`@log_call` は、「この関数を `log_call` で包む」という意味です。

つまり次の 2 つは、ほぼ同じ考え方です。

```python
greet = log_call(greet)
```

```python
@log_call
def greet(name):
    print(f"Hello, {name}")
```

### 要点
- `@decorator_name` は、関数をデコレータで包む記法です。
- 読み方がわかると、見慣れないコードも追いやすくなります。

## 6. デコレータの実用例
時間計測のような共通処理は、デコレータと相性がよいです。

```python
import time

def measure_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"took {end - start:.3f} sec")
    return wrapper

@measure_time
def run_task():
    time.sleep(0.2)
    print("task finished")

run_task()
```

このコードは、関数の前後で計測を行っています。

最初は「関数を受け取って、別の関数を返す」と理解できれば十分です。

### 要点
- デコレータはログ、計測、認可などの共通処理と相性がよいです。
- まずは「包んで追加する」イメージを持てば十分です。

## 7. コンテキストマネージャとは何か
コンテキストマネージャとは、処理の開始と後片付けを安全にまとめる仕組みです。

まずはファイル操作でよくある例です。

```python
file = open("sample.txt", "w", encoding="utf-8")
file.write("hello")
file.close()
```

この書き方でも動きますが、途中で例外が起きると `close()` を忘れやすくなります。

次のように `with` を使う方が安全です。

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("hello")
```

`with` ブロックを抜けるときに、必要な後片付けが自動で行われます。

### 要点
- コンテキストマネージャは、後片付け漏れを防ぐための仕組みです。
- `with` は「安全に使って、最後に片付ける」という書き方です。

## 8. 自分でコンテキストマネージャを作る考え方
自分で作る場合も、考え方は同じです。

次の例は、開始と終了のメッセージをまとめています。

```python
from contextlib import contextmanager

@contextmanager
def log_context(name):
    print(f"start: {name}")
    try:
        yield
    finally:
        print(f"end: {name}")

with log_context("job"):
    print("working...")
```

このコードでは、`with` に入ると開始メッセージを出し、抜けると終了メッセージを出します。

最初は「前処理」と「後処理」を 1 つにまとめる道具として理解するとわかりやすいです。

### 要点
- `contextlib.contextmanager` を使うと、簡単なコンテキストマネージャを作れます。
- 「使う前」と「使い終わった後」をまとめる道具と考えると理解しやすいです。

## 9. 中級者がよく使う標準ライブラリ
Python では、自分で全部書かなくても便利な標準ライブラリが多くあります。

### 9-1. `pathlib`
ファイルパスを文字列ではなく、扱いやすいオブジェクトとして扱えます。

```python
from pathlib import Path

path = Path("data") / "input.txt"
print(path.exists())
print(path.suffix)
```

文字列連結より読みやすく、OS ごとの差も吸収しやすいです。

### 9-2. `collections.Counter`
出現回数を数えたいときに便利です。

```python
from collections import Counter

words = ["python", "java", "python", "go", "python", "go"]
counter = Counter(words)

print(counter["python"])
print(counter.most_common(2))
```

辞書で数える処理を毎回手書きするより短く書けます。

### 9-3. `itertools`
繰り返し処理を組み立てたいときに便利です。

```python
from itertools import islice

numbers = range(100)
first_five = list(islice(numbers, 5))
print(first_five)
```

大きなデータを一部だけ使いたいときにも役立ちます。

### 要点
- 標準ライブラリは、よくある問題を安全に短く解くための道具です。
- `pathlib`、`Counter`、`itertools` は中級の入口で特に役立ちます。

## 10. 書き換え前後で見る Python らしさ
中級では、「動く」だけでなく「読みやすい」ことも大切になります。

まずは少し手作業が多い例です。

```python
counts = {}

for word in ["a", "b", "a", "c", "b", "a"]:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
```

`Counter` を使うと次のように書けます。

```python
from collections import Counter

counts = Counter(["a", "b", "a", "c", "b", "a"])
```

短いだけでなく、「何をしたいコードか」が伝わりやすくなります。

### 要点
- 中級では、標準ライブラリを使って意図が伝わる書き方を選ぶことが大切です。

## まとめ
- イテレータは値を順番に取り出す仕組みです。
- ジェネレータは `yield` で値を少しずつ返します。
- デコレータは関数に共通処理を追加する仕組みです。
- コンテキストマネージャは開始と後片付けを安全にまとめます。
- 標準ライブラリを使うと、より短く読みやすいコードになりやすいです。
