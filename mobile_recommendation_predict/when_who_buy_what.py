# -*- coding: utf-8 -*-
class  whenby(object):
    def __init__(self):
        pass
    def getdata(self):
        data=open('month11_day24_type4.csv','w')
        with open('behavior_type_4.csv','r') as f:
            for line in f:
                month=line.split(',')[-1].split('-')[1]
                day  =line.split(',')[-1].split('-')[2].split(' ')[0]
                #print(month,day)
                if month =='11' and day =='24':
                    print(line)   
                    data.write(line)
                pass
            pass
        data.close()
        pass
    


if __name__ == '__main__':
    test=whenby()
    test.getdata()
    pass


                
            
        
      

