__author__ = 'Mohammad'
"""
* Given set of jobs with start and end interval and profit, how to maximize profit such that
* jobs in subset do not overlap.

/**
* Sort the jobs by finish time.
* For every job find the first job which does not overlap with this job
* and see if this job profit plus profit till last non overlapping job is greater
* than profit till last job.

https://www.youtube.com/watch?v=cr6Ip0J9izc&index=14&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

"""



def weighted_job_scheduling(jobs):
    # sort jobs based on end time
    jobs.sort(key = lambda x:x[1])

    profit =[i[2] for i in jobs]

    for i in range(1, len(profit)):
        for j in range(i):
            # check if jobs overlap
            # check if starting time of job_i is after or equal to endtime of job_j
            if jobs[i][0] >= jobs[j][1]:
                if profit[j] + jobs[i][2] > profit[i]:
                    profit[i] = profit[j] + jobs[i][2]

    print(profit)

jobs = [(1,3,5), (5, 8, 11), (7, 9, 2), (4,6, 5) , (2, 5, 6), (6, 7, 4)]
weighted_job_scheduling(jobs)