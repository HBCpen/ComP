# 最長増加部分列 (Longest Increasing Subsequence)

## 問題概要

配列 `A` が与えられます。この配列の「部分列」とは、元の配列から0個以上の要素を取り除き、残りの要素の順序を保ったままにしたものです（連続している必要はない）。要素の値が単調に増加する部分列の中で、最も長いものの長さを求めるアルゴリズムを作成してください。

### 例

`A = [10, 9, 2, 5, 3, 7, 101, 18]` の場合、最長増加部分列 (LIS) は `[2, 3, 7, 101]` (または `[2, 5, 7, 101]`, `[2, 5, 7, 18]` など) であり、長さは 4 です。

## 制約

- `1 <= A.length <= 2500`
- `-10^4 <= A[i] <= 10^4`

## 解法

### 動的計画法 (DP) - O(n^2)

この問題は動的計画法を用いて解くことができます。

`dp[i]` を「`A[i]` を末尾とする増加部分列の最大長」と定義します。

`dp[i]` を計算するには、`j < i` となるすべての `j` について、`A[j] < A[i]` を満たすものを探します。そのような `j` の中で、`dp[j]` が最大となるものを見つけ、その値に1を加えたものが `dp[i]` となります。もし、そのような `j` が存在しない場合、`A[i]` 自身からなる長さ1の部分列が考えられるので、`dp[i] = 1` となります。

数式で表すと以下のようになります。

`dp[i] = max({dp[j] | 0 <= j < i, A[j] < A[i]}) + 1`
(もし `{...}` が空集合の場合は `max` の結果を `0` とします)

これをすべての `i` について計算し、`dp` 配列全体の最大値が求める答えとなります。

### 効率的な解法 (二分探索) - O(n log n)

より効率的な O(n log n) の解法も存在します。

`dp` 配列を少し異なる意味で使います。`dp[i]` を「長さが `i+1` であるような増加部分列の末尾の要素の中で、最小の値」と定義します。

配列 `A` の要素を一つずつ見ていきます。
- `A[k]` が `dp` 配列のすべての要素よりも大きい場合、`A[k]` を `dp` 配列の末尾に追加します。これは、既存の最長増加部分列をさらに1つ伸ばせることを意味します。
- `A[k]` が `dp` 配列のいずれかの要素以下の場合、`dp` 配列の中で `A[k]` 以上の値を持つ最初の要素を `A[k]` で置き換えます。これは、同じ長さの増加部分列を、より小さい末尾の要素で実現できることを意味し、将来的に部分列を伸ばせる可能性を高めます。

この操作は、`dp` 配列が常にソートされた状態になるため、二分探索 (`bisect_left` など) を用いて効率的に行うことができます。

最終的に、この `dp` 配列の長さが、最長増加部分列の長さとなります。

**例:** `A = [10, 9, 2, 5, 3, 7, 101, 18]`

1.  `x = 10`: `dp = [10]`
2.  `x = 9`: `dp` の中で `9` 以上の最初の値は `10`。`dp = [9]`
3.  `x = 2`: `dp` の中で `2` 以上の最初の値は `9`。`dp = [2]`
4.  `x = 5`: `dp` の中で `5` 以上の最初の値はない。`dp = [2, 5]`
5.  `x = 3`: `dp` の中で `3` 以上の最初の値は `5`。`dp = [2, 3]`
6.  `x = 7`: `dp` の中で `7` 以上の最初の値はない。`dp = [2, 3, 7]`
7.  `x = 101`: `dp` の中で `101` 以上の最初の値はない。`dp = [2, 3, 7, 101]`
8.  `x = 18`: `dp` の中で `18` 以上の最初の値は `101`。`dp = [2, 3, 7, 18]`

最終的な `dp` 配列は `[2, 3, 7, 18]` となり、その長さ `4` が答えです。
