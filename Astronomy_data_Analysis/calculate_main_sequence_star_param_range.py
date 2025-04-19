import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x와 y 값 범위 설정
x = np.linspace(-7, 16, 300)

y = np.linspace(0.1, 2000, 300)  # 0은 log10 계산할 수 없으므로 0.1부터 시작

# meshgrid 생성
X, Y = np.meshgrid(x, y)

# z 계산
Z = X - 5 * np.log10(Y / 10)

# 조건에 맞지 않는 부분은 NaN으로 만들어서 그래프에서 제외
Z_masked = np.where((Z > 5) & (Z <= 10), Z, np.nan)

# 3D 그래프 그리기
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 그래프 플로팅 (NaN은 자동으로 무시됨)
ax.plot_surface(X, Y, Z_masked, cmap='viridis', edgecolor='none')

# 라벨 추가
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot (Only 5 < z <= 10)')

plt.show()