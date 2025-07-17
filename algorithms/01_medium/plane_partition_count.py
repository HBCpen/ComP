"""
問題概要
自然数 'r', 'c' が与えられます。'r' x 'c'の二次元配列の要素に以下の条件を満たすように0, 1, 2のいずれかの整数を書き込む方法の総数を求めるプログラムを作成してください。
- 左右に隣り合う二つの要素について、左の要素の持つ値は右の要素の値以上である。
- 上下に隣り合う二つの要素について、上の要素の持つ値は下の要素の値以上である。

この問題は、平面分割の数え上げ問題の一種です。
r x c の格子状の領域に、0, 1, 2 の3つの値を、単調非増加の条件で配置する場合の数に相当します。
解法にはMacMahonの公式を用いることができます。
n+1個の値 (0, 1, ..., n) を使う場合、その総数は以下の式で与えられます。
Π_{i=1 to r} Π_{j=1 to c} (n + i + j - 1) / (i + j - 1)
この問題では n=2 なので、総数は以下のようになります。
Π_{i=1 to r} Π_{j=1 to c} (i + j + 1) / (i + j - 1)
"""

import math

def calculate_plane_partitions(r: int, c: int) -> int:
    """
    MacMahonの公式を用いて、r x c の2次元配列に3つの値(0, 1, 2)を
    単調非増加で配置する場合の数を計算します。

    Args:
        r: 配列の行数
        c: 配列の列数

    Returns:
        書き込み方法の総数
    """
    # 浮動小数点数で計算を進めるが、最終的な結果は整数になることが保証されている
    result = 1.0
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            numerator = i + j + 1
            denominator = i + j - 1
            result *= numerator / denominator
    
    # 浮動小数点数の誤差を考慮して、最も近い整数に丸める
    return round(result)

if __name__ == '__main__':
    # 問題で与えられた例
    r_val = 10
    c_val = 10
    total_combinations = calculate_plane_partitions(r_val, c_val)
    print(f'r={r_val}, c={c_val} の場合の総数は {total_combinations} 通りです。')

    # 小さなケースでのテスト
    r_test = 2
    c_test = 2
    total_test = calculate_plane_partitions(r_test, c_test)
    print(f'r={r_test}, c={c_test} の場合の総数は {total_test} 通りです。 (期待値: 20)')
    # assert total_test == 20
