# class Job_fam(object):

#     def __init__(self, j1, j2, j3):
#         self.j1=[]
#         self.j2=[]
#         self.j3=[]

# j1 = [82,77,55]
# j2 = [28,48,76]
# j3 = [60, 87, 34]

# T1 = sum(j1)
# T2 = sum(j2)
# T3 = sum(j3)

# T_array = [T1, T2, T3]

#파일 불러들기
with open('data.txt', 'r') as f:
    lines = f.readlines()

# 각각의 숫자를 담기
numbers = []
for line in lines:
    numbers.append(line.split())
print(numbers)
print(type(numbers[0][0]))

#

#sorting 하는 function
# for i in range(len(T_array)):
#     max_index = i
#     for j in range(i+1 , len(T_array)):
#         if T_array[max_index] < T_array[j]:
#             max_index = j
# T_array[i], T_array[max_index] = T_array[max_index], T_array[i]

# print(T_array)

# 



