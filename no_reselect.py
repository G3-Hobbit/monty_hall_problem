# Monty Hall problem : モンティ・ホール問題
import random
ans = 0 # 正答数
MAX = 10**5 # 質問数
N = 3 # 初期選択肢の数, N>=3
S = range(N) # 初期選択肢

for _ in range(MAX):
    q = random.choice(S) # 質問の正解
    a = random.choice(S) # 初期回答
    if q == a: ans += 1 # 回答が正解である数

print(f'MAX,ans {MAX,ans} ans/MAX {ans/MAX:.3f}')
