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



#flow shop의 코드 구현
def flow_shop_makespan(process_times):
    """
    Calculate the makespan of a flow shop problem given a list of processing times.

    Args:
        process_times (list): A 2D list where the rows represent the jobs and the columns represent the machines.

    Returns:
        int: The makespan of the flow shop problem.
    """
    n_jobs = len(process_times)
    n_machines = len(process_times[0])

    # Initialize the starting times of the first job on each machine
    start_times = [process_times[0][0]]
    for j in range(1, n_machines):
        start_times.append(start_times[j-1] + process_times[0][j])

    # Calculate the starting times of each job on each machine
    for i in range(1, n_jobs):
        for j in range(n_machines):
            if j == 0:
                start_times[j] += process_times[i][j]
            else:
                start_times[j] = max(start_times[j], start_times[j-1]) + process_times[i][j]

    # Return the makespan, which is the completion time of the last job on the last machine
    return start_times[-1]

# Define the processing times for each job and machine
process_times = [
    [2, 3, 1],
    [1, 2, 2],
    [3, 1, 2]
]

# Calculate the makespan
makespan = flow_shop_makespan(process_times)
print("Makespan:", makespan)




'''
저는 m개의 기계와 n개의 작업이 있는 flow-shop sequencing problem의 휴리스틱 알고리즘 중 하나인 Johnson's rule에 대한 파이썬 코드를 구현해드렸습니다.

이 알고리즘은 두 단계로 이루어져 있습니다.

1단계에서는 첫 번째 기계와 마지막 기계에 대해 최적의 작업 순서를 찾습니다. 이를 위해서 각 작업에 대해 첫 번째 기계와 마지막 기계에서의 처리 시간의 합을 계산하고, 이 중 가장 작은 값을 가지는 작업을 선택합니다. 이 작업의 첫 번째 기계에서의 처리 시간이 마지막 기계에서의 처리 시간보다 작으면 이 작업을 첫 번째 작업으로 스케줄링하고, 그렇지 않으면 이 작업을 마지막 작업으로 스케줄링합니다. 이 작업을 스케줄링한 후에는 이 작업을 아직 스케줄링하지 않은 작업의 집합에서 제거하고, 모든 작업이 스케줄링될 때까지 이를 반복합니다.

2단계에서는 남은 작업들을 남은 기계들에 대해 스케줄링합니다. 각 단계에서는 현재 기계에서 처리 시간이 가장 짧은 작업을 선택하고, 이 작업을 다음 작업으로 스케줄링합니다. 이 때, 처리 시간이 같은 작업이 여러 개인 경우에는 임의로 선택합니다. 모든 작업이 스케줄링될 때까지 이를 반복합니다.

이 알고리즘은 파이썬 함수로 구현되어 있으며, 처리 시간을 나타내는 2차원 리스트를 입력으로 받습니다. 이 함수는 작업을 스케줄링한 결과물로, 각 작업의 번호를 나타내는 정수의 리스트를 반환합니다.
'''


def johnson_rule(process_times):
    """
    Implement Johnson's rule for the flow-shop problem.

    Args:
        process_times (list): A 2D list where the rows represent the jobs and the columns represent the machines.

    Returns:
        list: A list of integers representing the sequence in which the jobs should be scheduled.
    """
    n_jobs = len(process_times)
    n_machines = len(process_times[0])

    # Initialize the set of unscheduled jobs
    unscheduled_jobs = set(range(n_jobs))

    # Initialize the scheduled jobs and the sequence
    scheduled_jobs = []
    sequence = []

    # Stage 1: Find the optimal sequence for the first and last machines
    while unscheduled_jobs:
        # Compute the sums of the processing times on the first and last machines
        sums = [(i, sum(process_times[i][:2]), sum(process_times[i][-2:])) for i in unscheduled_jobs]

        # Select the job with the smallest sum
        i, _, _ = min(sums, key=lambda x: min(x[1], x[2]))

        # Schedule the job as the first or last job
        if process_times[i][0] < process_times[i][-1]:
            scheduled_jobs.append((i, 0))
            sequence.append(i)
        else:
            scheduled_jobs.append((i, n_machines-1))
            sequence.insert(0, i)

        # Remove the job from the set of unscheduled jobs
        unscheduled_jobs.remove(i)

    # Stage 2: Schedule the remaining jobs on the remaining machines
    for j in range(1, n_machines-1):
        # Initialize the set of candidate jobs
        candidate_jobs = set(range(n_jobs))

        # Remove the jobs that have already been scheduled
        for i, _ in scheduled_jobs:
            candidate_jobs.discard(i)

        # Select the job with the smallest processing time on the current machine
        i = min(candidate_jobs, key=lambda i: process_times[i][j])

        # Schedule the job on the current machine
        scheduled_jobs.append((i, j))
        sequence.append(i)

    return sequence



# Define the processing times for each job and machine
process_times = [
    [2, 3, 1],
    [1, 2, 2],
    [3, 1, 2]
]

# Find the optimal sequence using Johnson's rule
sequence = johnson_rule(process_times)