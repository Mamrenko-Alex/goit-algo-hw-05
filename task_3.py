import timeit
import matplotlib.pyplot as plt

# Реалізація алгоритму Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

# Реалізація алгоритму Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256 
    modulus = 101
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

# Реалізація алгоритму Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1

# Завантаження тексту з файлу
with open("article_1.txt", encoding="windows-1251") as f:
    article_1 = f.read()

with open("article_2.txt", encoding="utf-8-sig") as f:
    article_2 = f.read()

# Підрядки для тестування
existing_substring = "рекомендаційна система"
non_existing_substring = "вигаданий підрядок"

# Функція для заміру часу виконання
def measure_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=10)

# Заміри часу
results = {
    "article_1":{
        "KMP": {
            "existing": measure_time(kmp_search, article_1, existing_substring),
            "non_existing": measure_time(kmp_search, article_1, non_existing_substring)
        },
        "Rabin-Karp": {
            "existing": measure_time(rabin_karp_search, article_1, existing_substring),
            "non_existing": measure_time(rabin_karp_search, article_1, non_existing_substring)
        },
        "Boyer-Moore": {
            "existing": measure_time(boyer_moore_search, article_1, existing_substring),
            "non_existing": measure_time(boyer_moore_search, article_1, non_existing_substring)
        }
    },
    "article_2":{
        "KMP": {
            "existing": measure_time(kmp_search, article_2, existing_substring),
            "non_existing": measure_time(kmp_search, article_2, non_existing_substring)
        },
        "Rabin-Karp": {
            "existing": measure_time(rabin_karp_search, article_2, existing_substring),
            "non_existing": measure_time(rabin_karp_search, article_2, non_existing_substring)
        },
        "Boyer-Moore": {
            "existing": measure_time(boyer_moore_search, article_2, existing_substring),
            "non_existing": measure_time(boyer_moore_search, article_2, non_existing_substring)
        }
    }
}

# Виведення результатів для кожної статті
for article, algorithms in results.items():
    print(f"{article}:")
    for algo, times in algorithms.items():
        print(f"  {algo}:")
        print(f"    Existing substring: {times['existing']:.5f} seconds")
        print(f"    Non-existing substring: {times['non_existing']:.5f} seconds")

# Побудова графіку
# Побудова графіку
articles = ["article_1", "article_2"]
algorithms = ["KMP", "Rabin-Karp", "Boyer-Moore"]

for article in results:
    existing_times = [results[article][algo]["existing"] for algo in algorithms]
    non_existing_times = [results[article][algo]["non_existing"] for algo in algorithms]

    x = range(len(algorithms))
    plt.bar(x, existing_times, width=0.4, label="Existing Substring", align='center')
    plt.bar([i + 0.4 for i in x], non_existing_times, width=0.4, label="Non-Existing Substring", align='center')

    plt.xticks([i + 0.2 for i in x], algorithms)
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Comparison of Substring Search Algorithms for {article}")
    plt.legend()
    plt.show()
