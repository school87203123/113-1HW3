def knight_tour(N, startX, startY):
    # 定義騎士的8個移動方向
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    
    # 初始化棋盤，所有格子標記為未訪問
    board = [[False for _ in range(N)] for _ in range(N)]
    
    # 初始化堆疊
    stack = [(startX, startY)]
    board[startX][startY] = True  # 標記起始位置已訪問
    visited_count = 1  # 計算訪問過的格子數
    
    while stack:
        x, y = stack.pop()
        
        # 嘗試8個方向
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            # 確保新位置在棋盤內，且未被訪問
            if 0 <= nx < N and 0 <= ny < N and not board[nx][ny]:
                board[nx][ny] = True  # 標記為已訪問
                stack.append((nx, ny))
                visited_count += 1
                break  # 進入下一個位置後，重新開始搜尋
                
    # 若訪問格子的數量等於棋盤大小，表示成功遍歷
    return visited_count == N * N

# 主程式
if __name__ == "__main__":
    # 輸入
    N = int(input("輸入棋盤大小 N (4 <= N <= 10): "))
    if 4 <= N <= 10:
        startX = int(input("輸入起始位置 startX (0 <= startX < N): "))
        startY = int(input("輸入起始位置 startY (0 <= startY < N): "))
        
        # 檢查起始位置是否合法
        if 0 <= startX < N and 0 <= startY < N:
            result = knight_tour(N, startX, startY)
            print("True" if result else "False")
        else:
            print("起始位置無效，請確保 0 <= startX, startY < N")
    else:
        print("N 必須在範圍 4 <= N <= 10")
