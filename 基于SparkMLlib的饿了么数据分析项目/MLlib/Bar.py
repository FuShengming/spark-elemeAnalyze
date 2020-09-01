import matplotlib.pyplot as plt

x_x=["口味","卫生","份量","配餐","配送"]
y_y=[346,289,301,237,259]
plt.figure(figsize=(10,5))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('差评预测统计',fontsize=20)
plt.barh(x_x[-20:],y_y[-20:])
plt.show()