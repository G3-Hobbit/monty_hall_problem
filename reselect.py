# Monty Hall problem : モンティ・ホール問題
import random
ans = 0 # 正答数
MAX = 10**5 # 質問数
N = 3 # 初期選択肢の数, N>=3
S = range(N) # 初期選択肢

for _ in range(MAX):
    q = random.choice(S) # 質問の正解
    a = random.choice(S) # 初期回答

    # 初期回答以外の選択肢から一つだけ残して全てを開く
    # 選択肢に正解を含むとき正解は開かない -> 残った 1 個が正解

    a2 = q # 初期回答で不正解していた場合 -> 正解の扉しか残らない
    # 初期回答で正解していた場合 -> 不正解の扉しか残らない
    if q == a: a2 = random.choice([s for s in S if s!=q]) # 不正解の扉の中から選択

    if q == a2: ans += 1 # 変更後の回答が正解である数

print(f'MAX,ans {MAX,ans} ans/MAX {ans/MAX:.3f}')
