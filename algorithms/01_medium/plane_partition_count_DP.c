#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_R 100
#define MAX_C 100
#define MAX_VALUE 2
#define MAX_PATTERNS 2000

// 1つの行パターンを表す構造体
typedef struct {
    int values[MAX_C];
} Pattern;

// パターンリスト
Pattern patterns[MAX_PATTERNS];
int pattern_count = 0;

// 行パターンを生成するための再帰関数 (DPの前処理)
void generate_patterns_recursive(int c, int col, int prev_val, int current_pattern[]) {
    if (col == c) {
        for (int i = 0; i < c; i++) {
            patterns[pattern_count].values[i] = current_pattern[i];
        }
        pattern_count++;
        return;
    }

    for (int val = 0; val <= prev_val; val++) {
        current_pattern[col] = val;
        generate_patterns_recursive(c, col + 1, val, current_pattern);
    }
}

// c列の有効な行パターンを全て生成する
void generate_all_patterns(int c) {
    pattern_count = 0;
    int current_pattern[MAX_C];
    // 最初のマス(col=0)には0,1,2のいずれでも置ける
    generate_patterns_recursive(c, 0, MAX_VALUE, current_pattern);
}

// パターンBの上にパターンAを置けるかチェック
bool can_place_on_top(int c, const Pattern* pattern_A, const Pattern* pattern_B) {
    for (int i = 0; i < c; i++) {
        if (pattern_A->values[i] < pattern_B->values[i]) {
            return false;
        }
    }
    return true;
}

long long solve_dp(int r, int c) {
    // 1. 有効な行パターンをすべて列挙する
    generate_all_patterns(c);

    // 2. DPテーブルを確保
    // dp[i][j]: i行目がj番目のパターンである場合の数
    long long dp[MAX_R][MAX_PATTERNS];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < pattern_count; j++) {
            dp[i][j] = 0;
        }
    }

    // 3. DPテーブルの初期化 (0行目)
    for (int j = 0; j < pattern_count; j++) {
        dp[0][j] = 1;
    }

    // 4. DPテーブルを埋める (1行目からr-1行目まで)
    for (int i = 1; i < r; i++) { // 現在の行
        for (int j = 0; j < pattern_count; j++) { // 現在の行のパターン (pattern_j)
            for (int k = 0; k < pattern_count; k++) { // 1つ前の行のパターン (pattern_k)
                // pattern_k の上に pattern_j を置ける場合
                if (can_place_on_top(c, &patterns[k], &patterns[j])) {
                    dp[i][j] += dp[i-1][k];
                }
            }
        }
    }

    // 最後の行(r-1行目)の全パターンの場合の数を合計する
    long long total_count = 0;
    for (int j = 0; j < pattern_count; j++) {
        total_count += dp[r-1][j];
    }

    return total_count;
}

int main(void) {
    int r, c;

    while (true) {
        printf("r, c を入力してください (終了する場合は 0 0): ");
        if (scanf("%d %d", &r, &c) != 2) {
            printf("不正な入力です。\n");
            while(getchar() != '\n');
            continue;
        }

        if (r == 0 && c == 0) {
            printf("プログラムを終了します。\n");
            break;
        }

        if (r <= 0 || r > MAX_R || c <= 0 || c > MAX_C) {
            printf("rとcは 1 から %d の範囲で入力してください。\n", MAX_R);
            continue;
        }
        
        long long count = solve_dp(r, c);
        printf("r=%d, c=%d の場合の数: %lld\n", r, c, count);
    }

    return 0;
}