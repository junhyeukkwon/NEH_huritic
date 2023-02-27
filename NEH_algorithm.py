
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





jd = {1: [82,77,55], 2:[28,48,76] , 3: [60,87,34]}

def NEH(job_dict, num_machines):
    # 작업들의 시간 총합을 구한다.
    job_total_times = {job: sum(job_dict[job]) for job in job_dict}
    # 시간 총합이 큰 순서대로 작업들을 정렬한다.
    jobs = sorted(job_total_times.keys(), key=lambda x: job_total_times[x], reverse=True)

    # NEH 알고리즘
    seq = []
    for job in jobs:
        best_index, best_makespan = -1, float('inf')
        for i in range(len(seq)+1):
            seq.insert(i, job)
            # 시간이 가장 적게 걸리는 기계 찾기
            machine_times = [0] * num_machines
            for j in seq:
                for k in range(num_machines):
                    machine_times[k] += job_dict[j][k]
            makespan = max(machine_times)
            if makespan < best_makespan:
                best_index, best_makespan = i, makespan
            seq.remove(job)
        seq.insert(best_index, job)
    return seq


print(NEH(jd, 3))
# 위 코드에서 job_dict는 딕셔너리 자료형으로, 작업번호를 키(key)로, 각 작업의 처리시간을 나타내는 리스트를 값(value)으로 가지는 딕셔너리입니다.
#  num_machines는 사용할 기계 수를 나타내는 정수입니다.

# 함수는 seq라는 리스트를 반환합니다. 이 리스트는 NEH 알고리즘을 수행한 결과로, 작업번호가 작업 순서대로 저장되어 있습니다.

