
# тут уже пришлось реально включаться)
def appearance(intervals: dict[str, list[int]]) -> int:
    def get_merged_intervals(times):   # склеиваем интервалы. Почему-то во втором тесте они накладываются друг на друга
        pairs = [(times[i], times[i+1]) for i in range(0, len(times), 2)]
        pairs.sort()
        merged = []
        for start, end in pairs:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged

    def intersect_intervals(ints1, ints2):  # и, наконец, сравниваем интервалы преподавателя и ученика
        i = j = 0
        total = 0
        while i < len(ints1) and j < len(ints2):
            start1, end1 = ints1[i]
            start2, end2 = ints2[j]
            start = max(start1, start2)
            end = min(end1, end2)
            if start < end:
                total += end - start
            if end1 < end2:
                i += 1
            else:
                j += 1
        return total

    lesson = intervals['lesson']
    pupil_intervals = get_merged_intervals(intervals['pupil'])
    tutor_intervals = get_merged_intervals(intervals['tutor'])
    def clip_to_lesson(ints, lesson):  # обрезаем по границам урока
        return [
            (max(start, lesson[0]), min(end, lesson[1]))
            for start, end in ints
            if min(end, lesson[1]) > max(start, lesson[0])
        ]

    pupil_intervals = clip_to_lesson(pupil_intervals, lesson)
    tutor_intervals = clip_to_lesson(tutor_intervals, lesson)

    return intersect_intervals(pupil_intervals, tutor_intervals)  #возвращаем все это
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'