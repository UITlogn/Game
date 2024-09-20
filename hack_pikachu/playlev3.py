import pyautogui, time

a = [[0 for i in range(11)] for j in range(18)]
# a[1..16][1..9] = 0:trống, 1..36:obj

### test click
# pyautogui.hotkey('alt', 'tab')
# time.sleep(0.5)
# for i in range(10, 16):
#     for j in range(9):
#         pyautogui.click(580+i*52, 310+j*65)
#         time.sleep(0.5)

## crop datanode:
# p = 0
# for i in range(16):
#     for j in range(9):
#         s = 'datanode/button' + str(i) + ',' + str(j) + '.png'
#         pyautogui.screenshot(s, region=(561+i*52 + p, 296+j*65, 35, 40))
#     p += (i%3==0)

def prepare():
    global a
    for i in range(1, 37):
        s = 'datanode/button_' + str(i) + '.png'
        obj = pyautogui.locateAllOnScreen(s)
        for j in obj:
            x = (j[0]-560) // 52
            y = (j[1]-295) // 65
            a[x+1][y+1] = i

##################################################
def findsame(x):
    res = []
    for i in range(1, 17):
        for j in range(1, 10):
            if [i, j] != x and a[i][j] == a[x[0]][x[1]]:
                res.append([i, j])
    return res

def inside(x):
    return 0 <= x[0] and x[0] <= 17 and 0 <= x[1] and x[1] <= 10

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dp = [[0 for i in range(11)] for j in range(18)]
# dp[i][j]: số đoạn gấp khúc ít nhất để đi tới ô (i, j)

findd = 0
def dfs(pos, y, last, cnt):
    dp[pos[0]][pos[1]] = cnt
    for i in range(4):
        v = [pos[0] + dx[i], pos[1] + dy[i]]
        newcnt = cnt + (i != last)
        if v == y and newcnt <= 3:
            global findd
            findd = 1
            return
        if inside(v) and a[v[0]][v[1]] == 0 and newcnt <= 3:
            if dp[v[0]][v[1]] > newcnt:
                dfs(v, y, i, newcnt)
            
def canmove(x, y):
    global dp
    for i in range(18):
        for j in range(11):
            dp[i][j] = 100

    global findd
    findd = 0
    dfs(x, y, -1, 0)
    return findd

def followup(x, y):
    global a
    k = y
    while a[x][k] > 0:
        a[x][k] = a[x][k+1]
        k += 1

def solve():
    flag = 0
    for i in range(1, 17):
        for j in range(1, 10):
            if a[i][j] != 0:
                flag = 1
                for x in findsame([i, j]):
                    if (canmove([i, j], x)):
                        print(i, j, x)
                        pyautogui.click(580+(i-1)*52, 310+(j-1)*65)
                        followup(i, j)
                        time.sleep(0.3)
                        pyautogui.click(580+(x[0]-1)*52, 310+(x[1]-1)*65)
                        followup(x[0], x[1])
                        time.sleep(0.3)
                        break
    return flag

######################################################
# main:

pyautogui.hotkey('alt', 'tab')
time.sleep(0.3)
prepare()

while 1:
    time.sleep(0.3)
    obj = pyautogui.locateCenterOnScreen('datanode/ok.png')
    if obj:
        pyautogui.click(obj[0], obj[1])
        time.sleep(0.3)
        prepare()
    # print(a)
    if solve() == 0:
        pyautogui.hotkey('alt', 'tab')
        exit(0)

'''a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 13, 35, 31, 11, 13, 32, 8, 2, 21, 0],
    [0, 14, 7, 18, 15, 35, 17, 15, 28, 34, 0],
    [0, 3, 23, 17, 29, 21, 33, 21, 9, 28, 0],
    [0, 22, 17, 34, 35, 2, 9, 23, 12, 20, 0],
    [0, 8, 4, 4, 18, 17, 36, 14, 33, 27, 0],
    [0, 14, 25, 31, 28, 1, 22, 5, 16, 20, 0],
    [0, 36, 19, 32, 4, 34, 23, 27, 12, 28, 0],
    [0, 3, 10, 33, 1, 1, 10, 29, 24, 6, 0],
    [0, 9, 30, 3, 25, 22, 11, 30, 3, 34, 0],
    [0, 7, 27, 16, 33, 6, 13, 7, 18, 25, 0],
    [0, 26, 8, 4, 29, 6, 15, 19, 5, 10, 0],
    [0, 9, 27, 5, 26, 31, 2, 16, 10, 18, 0],
    [0, 16, 2, 1, 25, 31, 32, 20, 11, 13, 0],
    [0, 19, 26, 36, 6, 7, 24, 23, 11, 22, 0],
    [0, 29, 12, 8, 20, 19, 35, 24, 15, 36, 0],
    [0, 14, 5, 24, 30, 30, 26, 12, 32, 21, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]'''

'''
9x16
    560       614
295 ########  ########   ^
    ########  ########   |
    ########  ########   | : 40
    ########  ########   v

360 ########  ########
    ########  ########
    ########  ########
    ########  ########

    <------> :35
'''

