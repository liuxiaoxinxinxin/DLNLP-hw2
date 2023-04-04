import pandas as pd
import math

# 读入data
df = pd.read_csv('height_data.csv')
dic = df.to_dict()
data = dic['height']
heights = []
for key in data:
    heights.append(data[key])

# alpha 男女比例
# mu    初始height
# o     方差
u1,u2,o1,o2,a1,a2 = 180,150,10,10,0.5,0.5

# 示迭代过程的精度
ep = 0.000001


while True:
    r1 = r2 = val1 = val2 = val3 = val4 = 0
    for j in range(len(heights)):  # E步
        temp1 = a1 * (1 / o1) * math.exp(-(pow((heights[j] - u1), 2)) / (2 * pow(o1, 2)))
        temp2 = a2 * (1 / o2) * math.exp(-(pow((heights[j] - u2), 2)) / (2 * pow(o2, 2)))
        temp3 = temp1 / (temp1 + temp2)
        temp4 = 1 - temp3
        r1 += temp3
        r2 += temp4
        val1 += temp3 * heights[j];
        val2 += temp4 * heights[j];
        val3 += temp3 * pow((heights[j] - u1), 2);
        val4 += temp4 * pow((heights[j] - u2), 2);
    if abs(u1- val1/r1)<ep and abs(u2- val2/r2)<ep and abs(o1- math.sqrt(val3/r1))<ep \
        and abs(o2- math.sqrt(val4/r2))<ep and abs(a1- r1/len(heights))<ep \
            and abs(a2- r2/len(heights))<ep:
        break;
    u1 = val1 / r1;
    u2 = val2 / r2;
    o1 = math.sqrt(val3 / r1);
    o2 = math.sqrt(val4 / r2);
    a1 = r1 / len(heights);
    a2 = r2 / len(heights);
    print(round(u1,6),round(u2,6),round(o1,6),round(o2,6),round(a1,6),round(a2,6))
