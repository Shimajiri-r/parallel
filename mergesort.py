# coding: UTF-8
import time
import random
from concurrent import futures

def merge_sort(list):
    # リストの要素数が1より大きくなければソートの必要なし
    if len(list) <= 1:
        return list

    # リストを2つのサブリストに分割
    povit = int(round(len(list)/2))
    left_sub_list = list[:povit]
    right_sub_list = list[povit:]

    # 分割したサブリストを、merge_sort()関数を再帰的に呼び出してソート
    left = merge_sort(left_sub_list)
    right = merge_sort(right_sub_list)

    # 2つのサブリストをマージして1つのソート済みリストを作成
    return merge_lists(left, right)


def merge_lists(left_list, right_list):
    sorted_list = []

    while (len(left_list) > 0) and (len(right_list) > 0):
        if left_list[0] < right_list[0]:
            sorted_list.append(left_list[0])
            del left_list[0]
        else:
            sorted_list.append(right_list[0])
            del right_list[0]

    if len(left_list) > 0:
        sorted_list.extend(left_list)
    else:
        sorted_list.extend(right_list)

    return sorted_list


if __name__ == "__main__":
    list = list(range(1000000))
    src = random.sample(list, len(list))
    sorted = []

    start_time = time.time()

    with futures.ThreadPoolExecutor() as executor :
        sort = executor.map(merge_sort, src)

    #sorted_list = merge_sort(src)

    elapsed_time = time.time() - start_time

    print("elapsed_time: {0}[sec]".format(elapsed_time))