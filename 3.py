def josephus_problem(n, k):
    # 建立初始的圓圈 (1 到 n)
    circle = list(range(1, n + 1))
    index = 0  # 從第 1 個人開始 (0-indexed)

    # 持續移除，直到只剩下一個人
    while len(circle) > 1:
        # 計算需要移除的人的索引
        index = (index + k - 1) % len(circle)
        circle.pop(index)  # 移除該人

    # 返回最後存活的人的編號
    return circle[0]

# 主程式
if __name__ == "__main__":
    # 輸入 n 和 k
    n = int(input("輸入參加遊戲的人數 n: "))
    k = int(input("輸入計數的步數 k: "))

    # 檢查輸入是否有效
    if n > 0 and k > 0:
        # 計算並輸出結果
        result = josephus_problem(n, k)
        print(f"最後存活的人的編號是: {result}")
    else:
        print("n 和 k 必須是正整數！")
