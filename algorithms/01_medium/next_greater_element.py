def next_greater_element(A: list[int]) -> list[int]:
    """
    各要素の Next Greater Element を見つける (O(n))

    Args:
        A: 整数の配列

    Returns:
        各要素の Next Greater Element を格納した配列。存在しない場合は -1。
    """
    n = len(A)
    if n == 0:
        return []

    result = [-1] * n
    stack = []  # インデックスを格納するスタック

    for i in range(n):
        # スタックが空でなく、現在の要素がスタックのトップの要素より大きい場合
        while stack and A[i] > A[stack[-1]]:
            # スタックのトップのインデックスに対応する要素のNGEが現在の要素
            top_index = stack.pop()
            result[top_index] = A[i]
        
        # 現在のインデックスをスタックに追加
        stack.append(i)

    return result

# --- テスト ---
def main():
    # 例1
    A1 = [2, 1, 5, 6, 2, 3]
    print(f"A = {A1}")
    print(f"Next Greater Element: {next_greater_element(A1)}") # 期待値: [5, 5, 6, -1, 3, -1]
    print("---")

    # 例2
    A2 = [1, 3, 2, 4]
    print(f"A = {A2}")
    print(f"Next Greater Element: {next_greater_element(A2)}") # 期待値: [3, 4, 4, -1]
    print("---")

    # 例3
    A3 = [11, 13, 21, 3]
    print(f"A = {A3}")
    print(f"Next Greater Element: {next_greater_element(A3)}") # 期待値: [13, 21, -1, -1]
    print("---")

    # すべて降順
    A4 = [5, 4, 3, 2, 1]
    print(f"A = {A4}")
    print(f"Next Greater Element: {next_greater_element(A4)}") # 期待値: [-1, -1, -1, -1, -1]
    print("---")

    # 空の配列
    A5 = []
    print(f"A = {A5}")
    print(f"Next Greater Element: {next_greater_element(A5)}") # 期待値: []
    print("---")

if __name__ == "__main__":
    main()
