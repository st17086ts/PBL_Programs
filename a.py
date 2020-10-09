#MAKURO

#未確定のノードに対しては大きな値を割り当てる
INF = 9999
#配列の中身
SIZE = 10
TRUE = 1
FALSE = 0
#Nはノードの数、Routeは辺の数を想定
N = 0
Route = 0

#配列の定義、重み、使われてるか判定する配列、経由内容、それぞれの辺の重み
COST = [0] * SIZE
USED = [0] * SIZE
VIA = [0] * SIZE
DIST = [[0 for i in range(SIZE)] for j in range(SIZE)]

#それぞれ使う配列を初期化
for i in range(SIZE):
    COST[i] = INF
    USED[i] = FALSE
    VIA[i] = -1
    for j in range(SIZE):
        DIST[i][j] = INF

def dijkstra(s, d):

    COST[s] = 0
    target = -1

    while True:
        #どこから始めるかを決める
        min = INF
        for i in range(0, N):
            if ((not USED[i]) and min > COST[i]):
                min = COST[i]
                target = i
        
        #経路確定
        if(target == d):
            return COST[d]
        
        for Ne in range(0, N):
            if(COST[Ne] > DIST[target][Ne] + COST[target] ):
                COST[Ne] = DIST[target][Ne] + COST[target]
                VIA[Ne] = target
        
        USED[target] = TRUE


#グラフの内容を入力
N = int(input("ノードの数:"))
Route = int(input("道の数："))
for i in range(0,Route):
    A, B = input("どこからどこまで？:").split()
    L = int(input("その重さは？："))
    A, B = int(A), int(B)
    DIST[A][B] = L


s = int(input("どのノードからスタートする？："))
d = int(input("どこをゴール地点にしますか？："))

print("距離は",dijkstra(s,d))

node = d
print(node,end = "")
while True:
    node = VIA[node]
    print(" <- ", node, end = "")
    if(node == s):
        break








