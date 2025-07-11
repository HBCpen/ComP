import bisect

def longest_increasing_subsequence(A: list[int]) -> int:
    """
    最長増加部分列の長さを求める (O(n log n))

    Args:
        A: 整数の配列

    Returns:
        最長増加部分列の長さ
    """
    if not A:
        return 0

    # dp[i] = 長さが i+1 である増加部分列の末尾要素の最小値
    dp = []

    for x in A:
        # dp の中で x 以上の値を持つ最初の要素の位置を探索
        idx = bisect.bisect_left(dp, x)

        if idx == len(dp):
            # x が dp の全要素より大きい場合、末尾に追加
            dp.append(x)
        else:
            # 既存の要素を x で置き換える
            dp[idx] = x

    return len(dp)

# --- テスト --- 
def main():
    # 例1
    A1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"A = {A1}")
    print(f"LIS の長さ: {longest_increasing_subsequence(A1)}") # 期待値: 4
    print("---")

    # 例2
    A2 = [0, 1, 0, 3, 2, 3]
    print(f"A = {A2}")
    print(f"LIS の長さ: {longest_increasing_subsequence(A2)}") # 期待値: 4
    print("---")

    # 例3
    A3 = [7, 7, 7, 7, 7, 7, 7]
    print(f"A = {A3}")
    print(f"LIS の長さ: {longest_increasing_subsequence(A3)}") # 期待値: 1
    print("---")

    # 空の配列
    A4 = []
    print(f"A = {A4}")
    print(f"LIS の長さ: {longest_increasing_subsequence(A4)}") # 期待値: 0
    print("---")

    # すべて降順
    A5 = [5, 4, 3, 2, 1]
    print(f"A = {A5}")
    print(f"LIS の長さ: {longest_increasing_subsequence(A5)}") # 期待値: 1
    print("---")

if __name__ == "__main__":
    main()
