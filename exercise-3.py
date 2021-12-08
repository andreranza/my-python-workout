def run_timing():
    timing = list()

    while True:
        time = input('Enter 10 km run time: ')
        if time == '': # better is if not time: break
            break
        else:
            try:
                time = float(time)
                timing.append(time)
            except ValueError:
                print('Please, enter a valid integer number.')

    n = len(timing)
    timing_sum = 0
    for numb in timing:
        timing_sum = timing_sum + numb
    return f'Average of {timing_sum/n}, over {n} runs'

def run_timing2():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break
        else:
            try:
                total_time = total_time + float(one_run)
                number_of_runs = number_of_runs + 1
            except ValueError:
                print('Please, enter a valid integer number.')
        
    avg_time = total_time/number_of_runs
    return f'Average of {avg_time:.2f}, over {number_of_runs} runs'

if __name__== "__main__":
    print(run_timing2())

