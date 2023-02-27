
#파일 불러들기
f = open('data.txt', 'r')
lines = f.readlines()
lines = list(map(lambda s : s.strip('\n'), lines))
jobn = int(lines[0])
opern = int(lines[1])

# 위에 있는 3, 3, '', 이값을 지울 수있게 해야함.
del lines[0]
del lines[0]
lines.remove('')
print(lines)


# job 클래스 만들기
# 1. job number def
# 2. 각 job들에 들어가있는 processing time 
# 3. total processing time 을 계산하는 def

class Job:
    def __init__(self, job_name, pt):
        self.job_name = job_name
        self.pt = pt
        pt = lines[self.job_name].split()
        self.pt = list(map(int, pt))


jobs = []

for i in range(jobn):
        jobs.append([Job(i, j) for j in lines])
print(jobs)

for i in jobs:
    print(i)







