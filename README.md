1,000,000の数値をランダムにシャッフルし、それをマージソートで実行した。

・通常時
sorted_list = merge_sort(src)
実行時間は130s程度。

・並列実行時
with futures.ThreadPoolExecutor() as executor :
    sort = executor.map(merge_sort, src)
実行時間は25s程度。