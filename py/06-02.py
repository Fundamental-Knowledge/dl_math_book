from scipy import signal

# 입력
x = [[0, 1, 2, 1, 0, 0], [0, 0, 1, 2, 1, 0], [0, 0, 0, 1, 2, 1], [0, 0, 0, 1, 3, 2], [1, 1, 1, 3, 2, 0], [2, 2, 3, 2, 1, 0]]

# 필터
f = [[0, 1, 1], [0, 1, 1], [0, 1, 1]]

print(signal.correlate(x, f, 'valid'))