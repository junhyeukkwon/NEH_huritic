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
        job = order[i] -1
        for j in range(m):
            prev_time = times[i-1][j] if i > 0 else 0
            next_time = times[i][j-1] if j > 0 else 0
            times[i][j] = max(prev_time, next_time) + jobs[job-1].processing_time[j]
    return times[-1][-1]

def NEH_algorithm(jobs):
    n, m = len(jobs), len(jobs[0].processing_time)
    order = list(range(1,n+1))
    order.sort(key=lambda x: jobs[x-1].total_processing_time, reverse=True)
    partial_seq = [order[0]-1, order[1]-1]
    for i in range(2, n):
        job = order[i] - 1
        best_pos, best_makespan = -1, float('inf')
        for j in range(i+1):
            order_copy = order.copy() # order 리스트의 복사본을 만든다.
            # step1. order에서 
            for k in range(2):
                temp_seq = partial_seq[:j] + [job] + partial_seq[j:]
                if k == 1 and j < i:
                    temp_seq[j], temp_seq[j+1] = temp_seq[j+1], temp_seq[j]
                elif k == 1 and j == i:
                    temp_seq.append(temp_seq[-1])
                    temp_seq[-2], temp_seq[-1] = temp_seq[-1], temp_seq[-2]
                # order_copy 리스트를 수정한다.
                order_copy.remove(job+1)
                order_copy.insert(j, job+1)
                makespan = calc_makespan(jobs, [x-1 for x in order_copy])
                if makespan < best_makespan:
                    best_makespan = makespan
                    best_pos = j
            if j < i and best_makespan < calc_makespan(jobs, partial_seq[:j] + [job] + partial_seq[j:]):
                break
        partial_seq.insert(best_pos, job)
        # order 리스트를 수정한다.
        order.remove(job+1)
        order.insert(best_pos, job+1)
    return [x+1 for x in partial_seq], best_makespan


p, best_makespan = NEH_algorithm(jobs)

print(p, best_makespan)