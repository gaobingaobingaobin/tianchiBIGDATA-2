import matplotlib.pyplot as plt
import numpy as np
import time

start = time.clock()

daydict={}
behavior_file=open('behavior_type_4.csv','w')
with open('fresh_comp_offline/tianchi_fresh_comp_train_user.csv') as file:
    for line in file:
        if line.split(',')[2]=='4':
            #4代表发生购买行为的用户
            #对时间进行统计
            date=line.split(',')[5].split(' ')[0].split('-')[2]
            #
            if date in daydict:
                daydict[date]=daydict[date]+1
            else:
                daydict[date]=1
            #print(line)
            behavior_file.write(line)
        pass
behavior_file.close()
#print(daydict)
temp=np.array(sorted(daydict.items(),key=lambda d:d[0]))
#对字典进行排序,并转化为np数组
x=temp[:,0]
#取时间作为x轴，购买行为数量作为y轴
y=temp[:,1]
plt.plot(x,y,'ro--')
plt.show()

end = time.clock()
print("read : %f s" %(end-start))
#read : 28.754975 s 读完970M数据
#read : 12.383269 s
#read : 11.206042 s
#read : 9.718309 s