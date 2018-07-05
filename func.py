# 使用 while 循环打印 1 3 5 7 9
while Ture:
   n = 1
   print(n)
   n = n+2
   if n > 9:
      break

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”
def test(l):
  for i in l:
    if i == 6:
       return 'found'
  return 'not found'
l = [1,5,7,8,9]

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序
import re

s = "aAsnr3id2d4b6gs7DZsf9e1AF" 
s_math = re.findall(r'\d', s)
s_str = re.findall(r'\D', s)
s_math.sort()
s_str = ''.join(s_str)
s_str.lower()
list_str = s_str.split('')
list_str.sort()
