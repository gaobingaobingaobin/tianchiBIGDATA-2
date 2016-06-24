# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:40:36 2016
# data example > 21902688,207800780,1,0,0,0,0
@author: wlei
"""
import numpy
class bayes(object):
    def __init__(self):
        pass
    def fit(self,filename="Pre_processed_data.csv"):
        count=0
        y0=0
        y1=0
        buyed2y0=0
        add2y0=0
        store2y0=0
        frequent2y0=0
        sum2y0=0
        buyed2y1=0
        add2y1=0
        store2y1=0
        frequent2y1=0
        sum2y1=0
        with open(filename,'r') as f:
            for eachline in f:
                count+=1
                elements=eachline.split(',')
                #print(str(elements))
                if elements[-1]=='0\n':
                    y0+=1
                    if elements[-2]=='1':
                        buyed2y0+=1
                    if elements[-3]=='1':
                        add2y0+=1
                    if elements[-4]=='1':
                        store2y0+=1
                    sum2y0+=int(elements[-5])**2
                    frequent2y0+=int(elements[-5])
                else:
                    y1+=1
                    if elements[-2]=='1':
                        buyed2y1+=1
                    if elements[-3]=='1':
                        add2y1+=1
                    if elements[-4]=='1':
                        store2y1+=1
                    sum2y1+=int(elements[-5])**2#用于计算方差 GDA
                    frequent2y1+=int(elements[-5])#用于计算均值
                pass
            pass
        self.py0=y0/count
        self.py1=y1/count
        self.pbuyed2y0=buyed2y0/y0
        self.pbuyed2y1=buyed2y1/y1
        self.padd2y0=add2y0/y0
        self.padd2y1=add2y1/y1
        self.pstore2y0=store2y0/y0
        self.pstore2y1=store2y1/y1
        self.u0=frequent2y0/y0
        self.u1=frequent2y1/y1
        self.val0=sum2y0/y0-self.u0**2
        self.val1=sum2y1/y1-self.u1**2
        pass
    def predict(self,element):
        pf0=numpy.exp(-(int(element[-5])-self.u0)**2/2/self.val0**2)\
        /numpy.sqrt(2*numpy.pi*self.val0)
        
        pf1=numpy.exp(-(int(element[-5])-self.u1)**2/2/self.val1**2)\
        /numpy.sqrt(2*numpy.pi*self.val1)
        
        p0=\
        numpy.log(self.py0)+numpy.log(pf0)\
        
        +numpy.log(self.pbuyed2y0*int(element[-2])+(1-self.pbuyed2y0)\
        *(1-int(element[-2])))\
        
        +5*numpy.log(self.padd2y0*int(element[-3])+(1-self.padd2y0)\
        *(1-int(element[-3])))\
        
        +numpy.log(self.pstore2y0*int(element[-4])+(1-self.pstore2y0)\
        *(1-int(element[-4])))\
        
        p1=\
        numpy.log(self.py1)+numpy.log(pf1)\
        
        +numpy.log(self.pbuyed2y1*int(element[-2])+(1-self.pbuyed2y1)\
        *(1-int(element[-2])))\
        
        +5*numpy.log(self.padd2y1*int(element[-3])+(1-self.padd2y1)\
        *(1-int(element[-3])))\
        #给不同的属性赋予不同的权重,并没有什么效果
        +numpy.log(self.pstore2y1*int(element[-4])+(1-self.pstore2y1)\
        *(1-int(element[-4])))\
        
        if p1>p0:
            #print(p1,p0)
            #print(str(element)+'\n')
            return 1
        else:
            return 0
            pass
        pass
    pass
if __name__ =='__main__':
    #element=('21902688','207800780','15','1','1','1','1')
    task=bayes()
    task.fit()
    count=0
    correct=0
    pcount=0
    pcorrect=0
    with open("Pre_processed_data.csv") as f:
        for line in f:
            elements=line.split(',')
            y=task.predict(elements)
            if y==1 :
                pcount+=1
                if elements[-1]=='1\n':
                    pcorrect+=1
                pass
            pass
            if elements[-1]=='1\n' :
                count+=1
                if y==1:
                    correct+=1
                pass
            pass
        pass
    precision=pcorrect/pcount
    recall=correct/count
    f1=2*precision*recall/(precision+recall)
    print("the recall is %f" %(recall*100))
    print("the precision is %f" %(precision*100))
    print("the f1 value is %f" %(f1*100))
                
    
            
        