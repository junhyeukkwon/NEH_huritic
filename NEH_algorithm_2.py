# 파일 불러들이기
f = open('data.txt', 'r')
lines = f.readlines()
lines = list(map(lambda s : s.strip('\n'), lines))
jobn = int(lines[0])
machines = int(lines[1])

# 위에 있는 3, 3, '', 이값을 지울 수 있게 해야함.
del lines[0]
del lines[0]
lines.remove('')

# job 클래스 만들기
class Job:
    def __init__(self, job_name, processing_time):
        self.job_name = job_name
        self.processing_time = processing_time
        self.total_processing_time = sum(self.processing_time)

    # 클래스내 내장함수를 활용하기 위한 데코레이션 함수
    @classmethod
    def Sorting(cls, job_fam):
        sorting_jobs = sorted(job_fam, key=lambda x: x.total_processing_time, reverse=True)
        return sorting_jobs

jobs = []
for i in range(1, jobn+1):
    job = Job(i,list(map(int,lines[i-1].split())))
    jobs.append(job)
sort_jobs = Job.Sorting(jobs)

# 알고리즘 시작
def calc_makespan(jobs, order):
    n, m = len(jobs), len(jobs[0].processing_time)
    # n행 m열을 만든다.
    times = [[0] * m for _ in range(n)]
    for i in range(n):
        job_index = order[i] - 1
        job = jobs[job_index]
        for j in range(m):
            prev_time = times[i-1][j] if i > 0 else 0
            next_time = times[i][j-1] if j > 0 else 0
            times[i][j] = max(prev_time, next_time) + job.processing_time[j]
    return times[-1][-1]



def NEH_algorithm(jobs):
    n, m = len(jobs), len(jobs[0].processing_time)
    order = list(range(n))
    sort_index = sorted(range(n), key=lambda x: jobs[x].total_processing_time, reverse=True)
    partial_seq = [sort_index[0], sort_index[1]]
    for i in range(2, n):
        job = sort_index[i]
        best_pos, best_makespan = -1, float('inf')
        for j in range(i+1):
            order_copy = order.copy()
            partial_copy = partial_seq.copy()
            for k in range(2):
                temp_seq = partial_copy[:j] + [job] + partial_copy[j:]
                if k == 1 and j < i:
                    # 새로운 작업을 추가할 때뿐만 아니라,
                    # 두 개의 작업을 교환하는 경우에도 계산해야 합니다.
                    # 이를 위해 변경된 작업 위치에서 앞 뒤의 작업들의 순서를 뒤집은 경우도 계산합니다.
                    if j > 0 and calc_makespan(jobs, [partial_copy[j-1], job, partial_copy[j]]) < best_makespan:
                        best_makespan = calc_makespan(jobs, [partial_copy[j-1], job, partial_copy[j]])
                        best_pos = j
                    if j < i and calc_makespan(jobs, [partial_copy[j], job, partial_copy[j+1]]) < best_makespan:
                        best_makespan = calc_makespan(jobs, [partial_copy[j], job, partial_copy[j+1]])
                        best_pos = j + 1
                    temp_seq[j], temp_seq[j+1] = temp_seq[j+1], temp_seq[j]
                elif k == 1 and j == i:
                    temp_seq.append(temp_seq[-1])
                    temp_seq[-2], temp_seq[-1] = temp_seq[-1], temp_seq[-2]
                order_copy.remove(job)
                order_copy.insert(j, job)
                makespan = calc_makespan(jobs, [x for x in temp_seq])
                if makespan < best_makespan:
                    best_makespan = makespan
                    best_pos = j
            if j < i and best_makespan < calc_makespan(jobs, partial_seq[:j] + [job] + partial_seq[j:]):
                break
        partial_seq.insert(best_pos, job)
        order = [partial_seq[x] for x in range(i+1)]
    return [x+1 for x in partial_seq], best_makespan

p, best_makespan = NEH_algorithm(sort_jobs)

print(p, best_makespan)
