# Python 中級 演習

## 演習 1. 易しい
次のコードを読んで答えてください。

```python
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator))
```

1. `iterator` は何ですか。
2. `print` される値は何ですか。

## 演習 2. 易しい
次の 2 つの違いを 1 文ずつ説明してください。

- `return`
- `yield`

## 演習 3. 易しい
次のコードは何を表示しますか。

```python
def count_up():
    yield 1
    yield 2

for value in count_up():
    print(value)
```

## 演習 4. 標準
次のコードで、`@log_call` はどんな役割を持っていますか。短く説明してください。

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
```

## 演習 5. 標準
次の 2 つのファイル操作を比べて、`with` を使う利点を説明してください。

```python
file = open("sample.txt", "w", encoding="utf-8")
file.write("hello")
file.close()
```

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("hello")
```

## 演習 6. 標準
次のコードを、`collections.Counter` を使う形に書き換えてください。

```python
counts = {}

for word in ["python", "go", "python", "rust", "python"]:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
```

## 演習 7. 応用
次の要件を満たす関数を考えてください。

- 1 から `n` までの偶数を順番に返す
- 結果は一度に全部返すのではなく、必要なときに 1 つずつ取り出せるようにする

次の 3 点を説明してください。

1. `return` と `yield` のどちらを使うか
2. なぜその方法が向いているか
3. 関数のコード例

## 演習 8. 応用
次の要件を満たすデコレータのアイデアを考えてください。

- 関数を呼び出した時刻を表示する
- そのあとで元の関数を実行する

コードを全部書けなくてもよいので、次の 3 点を説明してください。

1. デコレータ関数は何を受け取るか
2. 内側の関数で何をするか
3. 最後に何を返すか
