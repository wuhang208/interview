# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出
 s = s.replace(' ', '')
 list_s = s.split('')
 list_s.sort()
 for i in list_s:
    print(i)

# 问题二：数值比较

n = [9,15,23,89,33,26,2,76]

# 请编写代码，找出数组中的最大数与最小数
def max_min(n)
  for i in range(len(n)):
      for j in range(i, len(n))
          if n[i] > n[j]
            n[i], n[j] = n[j], n[i]
  return n[0], n[len(n)-1]

min, max = max_min(n)
print(min, max)
# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
def print_case(man, city):
   a = "i,am,a,'%s',in,'%s'" %(man, city)
   print(a)
print_case('student', 'chengdu')
# 通过参数输入打印出完整的句子
