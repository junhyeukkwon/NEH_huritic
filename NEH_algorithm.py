import copy as cp #리스트의 복제를 위해서 쓰는 모듈


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

# job 클래스 만들기

class Job:
    def __init__(self, job_name, processing_time):
        self.job_name = job_name
        self.processing_time = processing_time
        self.total_processing_time = sum(self.processing_time)
    
    #클래스내 내장함수를 활용하기 위한 데코레이션 함수
    @classmethod
    def Sorting(cls, job_fam):
        sorting_jobs = sorted(job_fam, key=lambda x: x.total_processing_time, reverse=True)
        return sorting_jobs


jobs = []

for i in range(1, jobn+1):
    job = Job(i,list(map(int,lines[i-1].split())))
    jobs.append(job)

jobs = Job.Sorting(jobs)


# 알고리즘 시작
'''
소팅한 job에서 processing time을 기준으로 2개의 makespan을 구함 (먼저 )
만약 1,3이뽑아지면 13, 31로 부분 makespan을 구해서 가장 최소의 makespan의 부분 sequence를 만들고, 그 시퀀스는 고정 ,이거는 이제 삭제[1,3]
그리고 나머지 잡에 대해서 추가 될때마다 고정되어있는 시퀀스의 사이사이 마다 추가가 되서 또 부분 makespan을 구함. 여기서 나온 부분 best 시퀀스는 고정되면서
계속 남은 job을 추가
'''

def calc_makespan(jobs):
    '''
    Flow shop에서 모든 job이 진행되었을 때의 시간 즉, makespan을 구하는 함수
    Args: 
        jobs: 각 job의 객체가 담겨져 있는 리스트 형태
    '''
    #n은 job의 수 , m의 기계의 수
    n, m = len(jobs), len(jobs[0].processing_time)
    #n행 m열을 만든다.2차원 배열을 생성
    times = [[0] * m for _ in range(n)]
    # 작업순서 대로 for문 시작
    for i in range(n):
        #현재 순회하는 작업의 번호를 찾습니다.
        job = jobs[i]
        #기계순서대로 순회
        for j in range(m):
            #현재 시점에서 이전 머신에서 job이 끝나는 시간과 지금 머신에서 진행된 job의 끝나는 시간을 비교
            #그 시간에서의 시작을 해야하므로 max값 + pt 
            prev_time = times[i-1][j] if i > 0 else 0
            next_time = times[i][j-1] if j > 0 else 0
            times[i][j] = max(prev_time, next_time) + job.processing_time[j]
    return times[-1][-1]

def NEH_algorithm(jobs):
    n, m = len(jobs), len(jobs[0].processing_time)
    partial_seq = [jobs[0]]
    best_makespan = float('inf')
    for i in range(1, len(jobs)):
        #1,3 , 3,1을 하는 코드 구현
        partial_seq.insert(i, jobs[i])
        for j in range(len(partial_seq)):
            tmp_seq = cp.copy(partial_seq)
            tmp_Cmax = calc_makespan(tmp_seq)
            tmp_seq_swp = cp.copy(tmp_seq)
            tmp_seq_swp[i], tmp_seq_swp[j] = tmp_seq_swp[j], tmp_seq_swp[i]
            tmp_Cmax_swp = calc_makespan(tmp_seq_swp)
            if tmp_Cmax < tmp_Cmax_swp:
                partial_seq = tmp_seq
                best_makespan = tmp_Cmax
            else:
                partial_seq = tmp_seq_swp
                best_makespan = tmp_Cmax_swp
        best_seq = partial_seq

    return best_seq , best_makespan


p, bms = NEH_algorithm(jobs)
print(p)

for i in p:
    print(i.job_name)
print(bms)