import pandas as pd

 
df1 = pd.DataFrame(pd.read_excel('C:\\Users\\shixun03\\Desktop\\汇总\\邬桥姓名.xlsx'))
df2 = pd.DataFrame(pd.read_excel('K:\\工资文件\\集团工资系统数据\\2019年度\\2019年集团工资系统数据\\10月\\职工薪资录入项.xls'))
df3 = pd.DataFrame(pd.read_excel('K:\\工资文件\\集团工资系统数据\\2019年度\\2019年集团工资系统数据\\10月\\绩效奖金.xls'))
df11 = pd.DataFrame(pd.read_excel('C:\\Users\\shixun03\\Desktop\\汇总\\浦江姓名.xlsx'))
df22 = pd.DataFrame(pd.read_excel('K:\\工资文件\\集团工资系统数据\\2019年度\\2019年集团工资系统数据\\10月\\职工薪资录入项PJ.xls'))
df33 = pd.DataFrame(pd.read_excel('K:\\工资文件\\集团工资系统数据\\2019年度\\2019年集团工资系统数据\\10月\\绩效奖金pj.xls'))
#df1.set_index("姓名")
#df2.set_index("姓名")
#df3.set_index("姓名")

print(df1)
print(df2)
print(df3)

print(df11)
print(df22)
print(df33)
#res = pd.concat([df1,df2,df3],axis=1,join_axes=[df1.index])
df4=pd.merge(df1,df2,how='left')
df44=pd.merge(df11,df22,how='left')
#df5=pd.merge(df4,df3,how='left',on='人员姓名')
#df5.to_excel('C:\\Users\\shixun03\\Desktop\\汇总\\汇总1.xlsx',na_rep=0)
wq =pd.merge(df4,df3,how='left',on='人员姓名')
pj =pd.merge(df44,df33,how='left',on='人员姓名')

wq.drop(['部门名称', '人员编码_x', '岗位_x','人员编码_y', '岗位_y', '独生子女奖励' ,'值班费_x' ,'工号', '薪点值', '补差工资', '计量提成工资', '绩效奖励', '技能补贴', '关键岗位津贴', '养老保险', 
	'医疗保险', '失业保险', '公积金', '补缴养老', '补缴医疗', '补缴失业', '补缴公积金', '补缴公积金', '补缴公积金', '补缴公积金', '工会费', 
	'病事假扣款', '各类赔款', '其他扣款', '个人所得税', '行号', '实发奖金'], axis=1, inplace=True)
pj.drop(['部门名称', '人员编码_x', '岗位_x','人员编码_y','人员类别', '岗位_y', '独生子女奖励' ,'值班费_x','中夜班费_x' ,'工号', '薪点值',  '计量提成工资', '绩效奖励', '技能补贴', '关键岗位津贴', '养老保险', 
	'医疗保险', '失业保险', '公积金', '补缴养老', '补缴医疗', '补缴失业', '补缴公积金', '补缴公积金', '补缴公积金', '补缴公积金', '工会费', 
	'病事假扣款', '各类赔款', '其他扣款', '个人所得税', '行号', '上月应发工资', '职务', '应税奖金'], axis=1, inplace=True)
#res.eval('小计 = 工资 + 奖金' , inplace=True)
#res.eval('小计 = 工资 + 奖金' , inplace=True)

#res.fillna(0,inplace=True)

#print(res)

#res.fillna(0,inplace=True)

#print(res)

wq.to_excel('C:\\Users\\shixun03\\Desktop\\汇总\\汇总wq.xlsx',na_rep=0)
pj.to_excel('C:\\Users\\shixun03\\Desktop\\汇总\\汇总pj.xlsx',na_rep=0)












