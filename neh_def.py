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





class Job:
    def __init__(self, id, times):
        self.id = id
        self.times = times

    def __repr__(self):
        return f'Job({self.id}, {self.times})'

    def __str__(self):
        return f'Job {self.id}'

class NEH:
    def __init__(self, jobs, num_machines):
        self.jobs = jobs
        self.num_machines = num_machines

    def run(self):
        # 작업들의 시간 총합을 구한다.
        job_total_times = {job.id: sum(job.times) for job in self.jobs}
        # 시간 총합이 큰 순서대로 작업들을 정렬한다.
        jobs = sorted(self.jobs, key=lambda x: job_total_times[x.id], reverse=True)

        # NEH 알고리즘
        seq = []
        for job in jobs:
            best_index, best_makespan = -1, float('inf')
            for i in range(len(seq)+1):
                seq.insert(i, job)
                # 시간이 가장 적게 걸리는 기계 찾기
                machine_times = [0] * self.num_machines
                for j in seq:
                    for k in range(self.num_machines):
                        machine_times[k] += j.times[k]
                makespan = max(machine_times)
                if makespan < best_makespan:
                    best_index, best_makespan = i, makespan
                seq.remove(job)
            seq.insert(best_index, job)
        return seq





# 코드 수정 필요
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