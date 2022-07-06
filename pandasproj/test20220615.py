import pandas as pd
import numpy as np

# object 类型，可保存python 对象作为值
# pd.DataFrame([[(1,2),33]],columns=['a','b'])

# 数据类型 np.int32 'int32' 值不能是nan, pd.Int32Dtype() 'Int32' 值可以是nan

'''
	索引 index
		loc是按照 行名(索引的值) 列名进行访问，iloc按照位置进行访问。
		# df.loc[s:e] df 索引值包含 s和 e,   df.loc[s,:,] 索引值是s，轴上所有的值（Series 类型）
		# df.iloc[s:e] df 索引值 包含s 不包含e
		# df[s:e]      df 位置索引，包含 s 不包含e
		
		df.at[index,col]   值
		df.iat[index,col]  位置
		
		df.index.
		(labels)  lables 在df.index 中的值
		df.index.difference(labels)  lables 不在df.index 中的值
		df.index.union(labels)        lables 和index 并集      
		df.index.symmetric_difference(labels)  只存在 lable 或者  index中的值
		
		
		df.index.is_monotonic_increasing  df.index 是否升序
		df.index.is_monotonic_decreasing  df.index 是否降序
		
		df.at[index,col] 获取单个值   index 索引值
		df.iat[index,col] 获取单个值  index 索引位置
		
		# dataframe where, df.mask() 是 df.where() 的逆条件
		df.wehre(
		        cond,                   # 条件
		        other=lib.no_default,   # 条件 False，替换值的dataframe(按照索引对齐)
		        inplace=False,
		        axis=None,
		        level=None,
		        errors="raise",
		        try_cast=lib.no_default,
		        )
		
		#numpy.where 大致相当于。df1.where(m, df2) np.where(m, df1, df2)
		
		# numpy.select(condlist,choicelist,default=0)   根据条件返回从选择列表中的元素中提取的数组
		
		# df.query()
			df[(df['a'] < df['b']) & (df['b'] < df['c'])] -> df.query('(a < b) & (b < c)')
			
			# query 在 multiIndex 中的应用
				df.index.names = ['color','food']
				
				df.query('color =="red"') == df.query('ilevel_0 == "red"') 约定是ilevel_0，这意味着 . 的第 0 级的“索引级别 0” index。
				
		# df.duplicated()               df.drop_duplicates() 
			subset:
			keep:标明 是否是重复元素，False 删除重复元素
'''

'''
		复合索引  pd.MultiIndex
		arrays = [
				    np.array(["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"]),
				    np.array(["one", "two", "one", "two", "one", "two", "one", "two"]),
				]
		df = pd.DataFrame(np.random.randn(8,8),index=arrays,columns=arrays)
		df.index.names = ['first','second']
		
		df.index.get_level_values(0) "first"
		
		#在索引方面，pandas 中的元组和列表的处理方式不同。元组被解释为一个多级键，而列表用于指定多个键。或者换句话说，元组是水平的（遍历级别），列表是垂直的（扫描级别）
		s = pd.Series(
			    [1, 2, 3, 4, 5, 6],
			    index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]]),
				)
		# 索引 用列表和元组的区别
		s.loc[[("A", "c"), ("B", "d")]]  # list of tuples
		A  c    1
		B  d    5
		dtype: int64
		
		s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists
		A  c    1
		   d    2
		B  c    4
		   d    5
		dtype: int64
'''

'''
	dataframe 合并 连接 比较
	pd.concat()
		objs: Series 或 DataFrame 对象的序列或映射。如果传递了 dict，则排序后的键将用作keys参数，除非传递，在这种情况下将选择值（见下文）。任何 None 对象都将被静默删除，除非它们都是 None 在这种情况下将引发 ValueError 。
		axis: {0, 1, ...}，默认 0。要连接的轴。	
		join: {'inner', 'outer'}，默认为'outer'。如何处理其他轴上的索引。外部用于联合，内部用于交叉。	
		ignore_index：布尔值，默认为 False。如果为 True，则不要使用连接轴上的索引值。结果轴将标记为 0, ..., n - 1。如果您要连接对象，而连接轴没有有意义的索引信息，这将非常有用。请注意，连接中仍然尊重其他轴上的索引值。
		keys：序列，默认无。使用传递的键作为最外层构建层次索引。如果通过了多个级别，则应包含元组。
		levels：序列列表，默认无。用于构造 MultiIndex 的特定级别（唯一值）。否则，它们将从密钥中推断出来。
		names：列表，默认无。生成的分层索引中的级别名称。
		verify_integrity：布尔值，默认为 False。检查新的连接轴是否包含重复项。相对于实际的数据连接，这可能非常昂贵。
		copy：布尔值，默认为真。如果为 False，则不要不必要地复制数据。
		
		objs: df 与df 合并， df series 合并
		axis：axis=0 等于 df.append(), axis=1, 等于 按照 index 连接
	
	df.merge(other_df)
	df.join()
	df.combine_first()
	
		
'''

'''
	df.sort_values(by, axis=0, ascending=True, inplace=False, kind=‘quicksort’, na_position=‘last,ignore_index=False,key=None)
	
	①axis 如果axis=0，那么by=“列名”； 如果axis=1，那么by=“⾏名”；
	②ascending: True则升序，可以是[True,False]，即第⼀字段升序，第⼆个降序
	③inplace: 是否⽤排序后的数据框替换现有的数据框 ，True,或者False
	④kind: 排序⽅法
	⑤na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后⾯
	6:ignore_index: 重置dataframe 索引
	7:key: 在排序之前将键函数应用于值。这类似于内置函数中的keysorted()参数，显着的区别是这个key函数应该是矢量化的。
		它应该期望 a Series并返回一个与输入具有相同形状的系列。它将独立应用于by中的每一列        
		
	df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
			})
	 df.sort_values(by='col4', key=lambda col: col.str.lower())
'''

'''
	分组
	resample(),	重采样
	expanding(),
	rolling()
'''

df = pd.DataFrame([
	[1, 2],
	[3, 4],
	[5, 6],

	[7, 8],
], columns=['a', 'b'])
df.replace
df.groupby
np.true_divide()
df.rank()
df.sort_values
df.nlargest()
pd.NamedAgg
df.transform
pd.date_range()
import functools
# functools.reduce()



# df.columns.difference()
# df.iloc[0:2]
#    a  b
# 0  1  2
# 1  3  4
# df[0:2]
#    a  b
# 0  1  2
# 1  3  4
# df.loc[0:2]
#    a  b
# 0  1  2
# 1  3  4
# 2  5  6

print(df)
