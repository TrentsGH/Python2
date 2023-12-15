from tkinter import *
from datetime import datetime as dt

class calendar:
    Week ={0:'Mon',
           1:'Tue',
           2:'Wed',
           3:'Thu',
           4:'Fri',
           5:'Sat',
           6:'Sun'}
    Month = {1:'Jan',
             2:'Feb',
             3:'Mar',
             4:'Apr',
             5:'May',
             6:'Jun',
             7:'Jul',
             8:'Aug',
             9:'Sep',
             10:'Oct',
             11:'Nov',
             12:'Dec'}
    def __init__(self):
        self.today = self.get_today()
    
    def get_today(self):
        today = str(dt.today().weekday()) +'-'+str(dt.today().strftime('%Y-%m-%d'))
        return today
    
    def format_date_from_str(self,x):
        day = x.split('-')
        dof = self.Week[int(day[0])]
        year = int(day[1])
        month = self.Month[int(day[2])]
        Day = int(day[3])
        print((dof,month,Day,year))

    def gen_days(self,n):
        
        ndays = [self.today]
        for i in range(n):
            ndays.append(self.next_day(ndays[i]))
        return ndays
    
    def next_day(self,D):
        d = D.split('-')
        for i in range(len(d)):
            d[i] = int(d[i])
        day = d[3]
        month = d[2]
        year = d[1]
        dow = d[0]
        dow = (dow+1)%7
        if d[2] in (1,3,5,7,8,10):
            day = day%31 + 1
            if day == 1:
                month+=1
        elif d[2] in (4,6,9,11):
            day = day%30 + 1
            if day == 1:
                month+=1
        elif d[2] in ([2]):
            if year%4 ==0:
                day = day%29 + 1
                if day == 1:
                    month+=1
            if year%4 !=0:
                day = day%28 + 1
                if day == 1:
                    month+=1
        elif d[2] in ([12]):
            day = day%31 + 1
            if day == 1:
                month=1
                year+=1
        return '{0}-{1}-{2}-{3}'.format(dow,year,month,day)



        


    



class day_cell(Canvas):
    def __init__(self,day,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.day = day
        self.dayl = None
        self.content = []
        self.add_day()
        
    def get_size(self):
        return[self.winfo_height(), self.winfo_width()]
    
    def add_content(self,x):
        self.content.append(str(x))
    def add_day(self):
        x = self.get_size()
        x[1] = 0
        self.dayl = self.create_text(x[0],x[1],text=self.day,anchor='ne')
        self.after(100,self.resize)
    def resize(self):
        x = self.get_size()
        x[1] = 0
        self.
        self.dayl = self.create_text(x[0],x[1],text=self.day,anchor='ne')
        self.after(100,self.add_day)
        

main = Tk()
j = day_cell('11/10/23',main,width=40,height=50,bg='green')
j.pack(fill=BOTH,expand=True)
mainloop()

