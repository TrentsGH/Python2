import os
def xtag(funct):
        def inner(self,v,**att):
            if att:
                tagg=funct(self,v,**att)+' '+self.attributes(**att)
            else:
                tagg=funct(self,v)
            return self.xline(tagg,v)
        return inner

def tag(funct):
        def inner(self,v,**att):
            if att:
                tagg=funct(self,v,**att)+' '+self.attributes(**att)
            else:
                tagg=funct(self,v)
            self.line(tagg,v)
        return inner

class formater:
    def __init__(self,paterns):
        self.patterns = paterns
        self.all = ''
    
    def write(self,tag,*x):
        self.all+= self.patterns[tag].format(*x)
    
    def xwrite(self,tag, *x):
        return self.patterns[tag].format(*x)
    
    def show(self):
        print(self.all)

class xformat(formater):
    tag_type = {'open':'<{0}>\n',
            'close':'</{0}>',
            'line':'<{0}>{1}</{2}>\n',
            'single':'<{0}/>'}
    def __init__(self):
        super().__init__(self.tag_type)
        self.last = []
        
    
    def line(self, tag, data):
        end = tag.split(' ')[0]
        self.write('line',tag,data,end)

    def xline(self, tag, data):
        end = tag.split(' ')[0]
        return self.xwrite('line',tag,data,end)
    
    def single(self, tag, data):
        end = tag.split(' ')[0]
        self.write('single',tag,data,end)

    def xsingle(self, tag, data):
        end = tag.split(' ')[0]
        return self.xwrite('single',tag,data,end)

    def open(self,tag):
        self.write('open',tag)
        self.last.append(tag)

    def xopen(self,tag):
        self.last.append(tag)
        return self.xwrite('open',tag)
    
    def close(self):
        self.write('close',self.last[-1])
        self.last.pop(-1)

    def xclose(self):
        last = self.last[-1]
        self.last.pop(-1)
        return self.xwrite('close',last)
    
    def doc(self, file):
        File = open(file,'w')
        File.write(self.all)
        File.close()

class html(xformat):
    blank_doc = '''<!Document html>
<body>
{0}
</body>
</html>'''
    def __init__(self):
        super().__init__()
        self.fname='untitled.html'

    def attributes(self,**x):
        att=''
        for i in x:
            att+=' {0}=\"{1}\"'.format(i,x[i])
        return att
    @tag
    def h1(self,title,**att):
        return 'h1'
    @xtag
    def xh1(self,title,**att):
        return 'h1'
    @tag
    def h2(self,title,**att):
        return 'h2'
    @xtag
    def xh2(self,title,**att):
        return 'h2'
    @tag
    def h3(self,title,**att):
        return 'h3'
    @xtag
    def xh3(self,title,**att):
        return 'h3'
    @tag
    def h4(self,title,**att):
        return 'h4'
    @xtag
    def xh4(self,title,**att):
        return 'h4'
    @tag
    def h5(self,title,**att):
        return 'h5'
    @xtag
    def xh5(self,title,**att):
        return 'h5'
    @tag
    def h6(self,title,**att):
        return 'h6'
    @xtag
    def xh6(self,title,**att):
        return 'h6'
    @tag
    def para(self,p,**att):
       return 'p'
    @xtag
    def xpara(self,p,**att):
        return 'p'
    @tag
    def ref(self,l,**att):
        return 'a'
    @xtag
    def xref(self,l,**att):
        return 'a'
    @tag
    def tab(self,t,**att):
        return 'table'
    @xtag
    def xcap(self,c,**att):
        return 'caption'
    def link(self,dir,lname='Link',**att):
        att.update({'href':dir})
        self.ref(lname,**att)

    def xlink(self,dir,lname='Link',**att):
        att.update({'href':dir})
        return self.xref(lname,**att)

    def table(self,mat,caption='Table', style='',**att):
        r = len(mat)
        tab = ''
        for row in range(r):
            tab += self.xopen('tr')
            for col in range(len(mat[row])):
                if ((row ==0 and style=='-') or (row ==0 and style=='+') ) or ((col ==0 and style=='|') or (col ==0 and style=='+')):
                    tab+=self.xline('th',mat[row][col])
                else:
                    tab+=self.xline('td',mat[row][col])
            tab+=self.xclose()
        tab+= self.xcap(caption)
        self.tab(tab,**att)

    def save(self,fname='untitled.html'):
        self.all = self.blank_doc.format(self.all)
        self.fname=fname
        self.doc(fname)
    
    def show(self):
        self.all = self.blank_doc.format(self.all)
        print(self.all)
    
    def open(self):
        os.system(self.fname)
    
    
    
    



def mktab(n,m):
    mat = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(i*j+i+j)
        mat.append(temp)
    return mat

test_table = mktab(1,5)

doc = html()

test_table[0][0] = doc.xlink('www.google.com','Suck Me')
doc.h1('Hello World',**{'style':'color:red;'})
doc.para('Hey world this is my first paragraph for this',**{'title':'Paragraph 1'})
doc.link('C:/Users/trent/OneDrive/Pictures/Screenshots','First Link',**{'style':'font-size:20xp;'})
doc.para('Testing '+doc.xlink('C:/Users/trent','xlink')+'ok lets see the results')
doc.table(test_table,style='-',**{'border':'1px solid black'})
doc.save()
doc.show()
doc.open()

