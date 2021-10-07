from funcs import *
import matplotlib.pyplot as plt

def main():
    '''
    a main function to conduct all the requiered tests
    '''
    SIZE = 16
    tests = {
        0 : create_random_array,
        1 : create_sorted_array,
        2 : create_inverted_sorted_array,
        3 : create_random_array_123
    }
    tests_names = {
        0 : 'random_array',
        1 : 'sorted_array',
        2 : 'inverted_sorted_array',
        3 : 'random_array_123'
    }
    algorithms = {
        0 : selection_sort,
        1 : insertion_sort,
        2 : calculate_time_for_merge_sort,
        3 : shell_sort
    }
    names = {
        0 : "selection_sort",
        1 : "insertion_sort",
        2 : "merge_sort",
        3 : "shell_sort"
    }
    for k in range(3, 4):
        fig, ax = plt.subplots(1, 2)
        ax[0].set_xscale("log", base=2)
        ax[0].set_yscale("log", base=10)
        ax[1].set_xscale("log", base=2)
        ax[1].set_yscale("log", base=10)
        counts = [0 for i in range(7, SIZE)]
        lengs = [0 for i in range(7, SIZE)]
        times = [0 for i in range(7, SIZE)]
        j, i, z = 0, 0, 0
        for j in range(4):
            counts2 = [counts for h in range(5)]
            times2 = [times for h in range(5)]
            for i in range(7, SIZE):
                if k == 0:
                    for z in range(5):
                        arr = tests[k](i)
                        print(names[j])
                        a, counts[i-7], times[i-7] = algorithms[j](arr)
                        counts2[z][i-7] = counts[i-7]
                        times2[z][i-7] = times[i-7]
                        lengs[i-7] = len(a)
                        counts = [0 for f in range(len(counts))]
                        times = [0 for f in range(len(times))]
                elif k == 3:
                    for z in range(3):
                        arr = tests[k](i)
                        print(names[j])
                        a, counts[i-7], times[i-7] = algorithms[j](arr)
                        counts2[z][i-7] = counts[i-7]
                        times2[z][i-7] = times[i-7]
                        lengs[i-7] = len(a)
                        counts = [0 for f in range(len(counts))]
                        times = [0 for f in range(len(times))]
                else:
                    arr = tests[k](i)
                    print(names[j])
                    a, counts[i-7], times[i-7] = algorithms[j](arr)
                    lengs[i-7] = len(a)
                
            if k == 0 or k == 3:
                for x in range(5 if k == 0 else 3):
                    for g in range(7, SIZE):
                        counts[g-7] += counts2[x][g-7]
                        times[g-7] += times2[x][g-7]
                for g in range(7, SIZE):
                    counts[g-7] /= (5 if k == 0 else 3)
                    times[g-7] /= (5 if k == 0 else 3)


            ax[0].plot(lengs, counts, label = names[j])
            
            ax[1].plot(lengs, times)
        
        ax[0].legend(loc=2)
        plt.savefig(str(tests_names[k]) + ".png", dpi = 300)


    # fig, ax = plt.subplots(1, 2)    
    # ax[0].plot(count, 2^5)
    # plt.show()


if __name__ == "__main__":
    main()