# -*- coding: utf-8 -*-
class target(dict):
   
    def __init__(self,month=11,day=24):
        self.month=month
        self.day  =day
        pass

class featureExtr(object):
    def __init__(self):
        pass
    def getFeature(self):
        count=0#用来过滤掉第一行
        temp=target()
        with open('fresh_comp_offline/tianchi_fresh_comp_train_user.csv') as file:
            for line in file:
                value=[0,0,0,0,0]
                 #frequent,store,addinbox,buyed,willbuy
                if count==0:
                    pass
                else:
                    month=int(line.split(',')[-1].split('-')[1])
                    day  =int(line.split(',')[-1].split('-')[2].split(' ')[0])
                    #根据日期做出选择
                    if temp.month<month or temp.day<day:
                        continue
                    elif temp.month==month and temp.day==day:
                        field=line.split(',')
                        user_id=field[0]
                        item_id=field[1]
                        behavior_type=field[2]
                    
                        key=(user_id,item_id)
                        if key in temp:
                            if behavior_type=='4':
                                temp[key][4]|=1
                        continue
                    else:
                        pass
                    #值考察目标日期之前的数据
                    field=line.split(',')
                    user_id=field[0]
                    item_id=field[1]
                    behavior_type=field[2]
                    
                    key=(user_id,item_id)
                    if key in temp:
                        if behavior_type=='1':
                            temp[key][0]+=1
                        elif behavior_type=='2':
                            temp[key][1]|=1
                        elif behavior_type=='3':
                            temp[key][2]|=1
                        elif behavior_type=='4':
                            temp[key][3]|=1
                        pass
                    else:
                        if behavior_type=='1':
                            value[0]+=1
                        elif behavior_type=='2':
                            value[1]|=1
                        elif behavior_type=='3':
                            value[2]|=1
                        elif behavior_type=='4':
                            value[3]|=1
                        pass
                        temp[key]=value
                        #tuple是不可变的，所以可以作为字典的key
                        #用(uid,item)来唯一确定一个二元组
                        #用[f1,f2,f3]来作为value，可以uptate
                        
                    pass
                count=1
                pass
            pass
        return temp
        
if __name__=='__main__':
    allnum=0
    buyednum=0
    addinboxnum=0
    storenum=0
    task=featureExtr()
    feature=task.getFeature()
    for line in feature.items():
        if line[1][4]!=1:
            continue
        
        allnum+=1
        if line[1][4]==1 and line[1][3]==1:
            buyednum+=1
        if line[1][4]==1 and line[1][2]==1:
            addinboxnum+=1
        if line[1][4]==1 and line[1][1]==1:
            storenum+=1
    rate1=float(buyednum)/float(allnum)
    rate2=float(addinboxnum)/float(allnum)
    rate3=float(storenum)/float(allnum)
    print("重复购买率是%f" %(rate1))
    print("加入购物车后%f" %(rate2))
    print("收藏商品之后%f" %(rate3))
    
    
    
    
    
    
