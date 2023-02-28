
#파일 불러들기
f = open('data.txt', 'r')
lines = f.readlines()
lines = list(map(lambda s : s.strip('\n'), lines))
jobn = int(lines[0])
machines = int(lines[1])

# 위에 있는 3, 3, '', 이값을 지울 수있게 해야함.
del lines[0]
del lines[0]
lines.remove('')
# print(lines)


# job 클래스 만들기
# 1. job number def
# 2. 각 job들에 들어가있는 processing time 
# 3. total processing time 을 계산하는 def

class Job:
    def __init__(self, job_name, processing_time,total_processing_time):
        self.job_name = job_name
        self.processing_time = processing_time
        #total_processing time 
        self.total_processing_time = sum(self.processing_time)


jobs = []

for i in range(1, jobn+1):
    job = Job(i,list(map(int,lines[i-1].split())),list(map(int,lines[i-1].split())))
    jobs.append(job)

for i in jobs:
    print('first:',i.job_name)

# 알고리즘 시작
# jobs의 각각의 객체에서 total_processing_time 에서 내림차순으로 sorting해 다시 저장
# sorting
def Sorting(job_fam):
    # sorting_jobs = []
    sorting_jobs = sorted(job_fam, key=lambda x: x.total_processing_time, reverse=True)
    return sorting_jobs


jobs = Sorting(jobs)

for i in jobs:
    print('sorted:',i.job_name)



def NEH(job_fam,num_machines):
    # desending sorting
    jobs = sorted(job_fam, key=lambda x: x.total_processing_time, reverse=True)
    # NEH 알고리즘
    seq = [] 
    #for문에서는 내림차순 정렬한 리스트를 차례로 순회하면서, 해당 작업을 각 위치에 삽입해본 후 makespan을 계산
    for job in jobs:
        best_index, best_makespan = -1, float('inf') # 값과 인덱스 초기화
        #시간이 가장 적게 걸리는 기계를 찾아 그 기계에서 작업을 수행 기계별로 걸리는 시간을 machine_times 리스트에 저장
        for i in range(len(seq)+1):
            seq.insert(i, job)
            machine_times = [0]*num_machines
            for j in seq:
                for k in range(num_machines):
                    machine_times[k] += j.processing_time[k]
            # makespan은 가장 오래 걸리는 기계에서 걸리는 시간으로 정의
            # machine_times 리스트에서 가장 큰 값을 찾아서 makespan 변수에 저장
            makespan = max(machine_times)
            # 삽입 위치를 결정하기 위해 best_index와 best_makespan을 업데이트
            if makespan < best_makespan:
                best_index, best_makespan = i, makespan
            seq.remove(job)
        seq.insert(best_index, job)
    return seq    

neh = NEH(jobs, machines)
for i in neh:
    print('best_sequence:',i.job_name)


#makespan 예시

job_seq = [1,3,2]
pt = [[82,77,55], [28,48,76], [60,87,34]]

def calculate_makespan(job_sequence, processing_times):
    """
    job_sequence: list of job numbers in the given sequence
    processing_times: 2-D list of processing times for each job on each machine
    """
    num_jobs = len(job_sequence)
    num_machines = len(processing_times[0])
    # 각 기계별로 누적된 작업 시간을 저장하는 리스트 초기화
    machine_times = [0] * num_machines
    # 각 작업별로 시작 시간을 저장하는 리스트 초기화
    start_times = [[0] * num_machines for _ in range(num_jobs)]

    # 각 작업을 해당하는 기계에 할당하면서 누적된 작업 시간과 시작 시간 계산
    for job_num in job_sequence:
        for machine_num in range(num_machines):
            # 해당 기계의 시작 시간 계산
            if job_num == 1:
                start_times[job_num-1][machine_num] = 0
            else:
                start_times[job_num-1][machine_num] = max(machine_times[machine_num], start_times[job_num-2][machine_num])
            # 해당 기계의 누적 작업 시간 계산
            machine_times[machine_num] = start_times[job_num-1][machine_num] + processing_times[job_num-1][machine_num]

    # 전체 작업 중에서 가장 마지막에 끝나는 작업의 누적 작업 시간을 반환
    return max(machine_times)

print(calculate_makespan(job_seq, pt))