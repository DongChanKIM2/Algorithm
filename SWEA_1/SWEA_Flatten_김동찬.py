for i in range(1, 11):
    dump_count = int(input())
    dump_list = list(map(int, input().split()))
    for count in range(dump_count):
        minimum = dump_list[0]
        maximum = dump_list[0]
        minimum_idx = 0
        maximum_idx = 0
        for dump_idx in range(len(dump_list)):
            if maximum < dump_list[dump_idx]:
                maximum = dump_list[dump_idx]
                maximum_idx = dump_idx
            if minimum > dump_list[dump_idx]:
                minimum = dump_list[dump_idx]
                minimum_idx = dump_idx
        dump_list[maximum_idx] -= 1
        dump_list[minimum_idx] += 1

    ans_max = dump_list[0]
    ans_min = dump_list[0]
    for dump in dump_list:
        if dump > ans_max:
            ans_max = dump
        if dump < ans_min:
            ans_min = dump

    print(dump_list)
    print('#{} {}'.format(i, ans_max - ans_min))
