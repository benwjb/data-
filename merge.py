import pandas as pd

 
df1 = pd.DataFrame(pd.read_excel('姓名.xlsx'))
df2 = pd.DataFrame(pd.read_excel('工资.xlsx'))
df3 = pd.DataFrame(pd.read_excel('奖金.xlsx'))

df1.set_index("姓名")
df2.set_index("姓名")
df3.set_index("姓名")

print(df1)
print(df2)
print(df3)

#res = pd.concat([df1,df2,df3],axis=1,join_axes=[df1.index])
df4=pd.merge(df1,df2,how='left')
res =pd.merge(df4,df3,how='left')

res.eval('小计 = 工资 + 奖金' , inplace=True)

res.fillna(0,inplace=True)

print(res)

res.to_excel('汇总.xlsx',na_rep=0)