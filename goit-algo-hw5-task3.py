from goit_algo_hw5_task3_helpers import kmp_search, boyer_moore_search, rabin_karp_search
from timeit import timeit

with open("стаття 1.txt", "r", encoding="cp1251") as f:
    source1 = f.read()

with open("стаття 2.txt", "r", encoding="cp1251") as f:
    source2 = f.read()

q1 = "задачу можливо вирішити"
q2 = "або задачу або"
q3 = "можливість зберігати дані"
q4 = "стрруктура дуже"
q5 = "exponentialSearch"
q6 = "zzZZzz"

test_suite = [(source1, q1, "позитивний кейс, текст 1")
    , (source1, q2, "негативний кейс, текст 1")
    , (source2, q3, "позитивний кейс, текст 2")
    , (source2, q4, "негативний кейс, текст 2")
    , (source1, q5, "додатковий позитивний кейс, текст 1")
    , (source1, q6, "додатковий негативний кейс, текст 1")
    , (source2, q5, "додатковий позитивний кейс, текст 2")
    , (source2, q6, "додатковий негативний кейс, текст 2")]


if __name__ == "__main__":
    for t in test_suite:
        #longest prefix suffix
        #print(f"Пошук Кнута-Морріса-Пратта, {t[2]}: {timeit(lambda: kmp_search(t[0], t[1]), number=10)}")
        #right to left
        #print(f"Пошук Боєра-Мура, {t[2]}: {timeit(lambda: boyer_moore_search(t[0], t[1]), number=10)}")
        #hashing
        #print(f"Пошук Рабін-Карпа, {t[2]}: {timeit(lambda: rabin_karp_search(t[0], t[1]), number=10)}")
        print(f"| {t[2]} | {timeit(lambda: kmp_search(t[0], t[1]), number=10):.4f} | {timeit(lambda: boyer_moore_search(t[0], t[1]), number=10):.4f} | {timeit(lambda: rabin_karp_search(t[0], t[1]), number=10):.4f}|")

