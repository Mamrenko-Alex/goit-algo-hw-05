# Substring Search Algorithms Performance Analysis

## Overview

This project compares the performance of three substring search algorithms:

- **Knuth-Morris-Pratt (KMP)**
- **Rabin-Karp**
- **Boyer-Moore**

The execution time of each algorithm was measured using two text articles with different encodings (Windows-1251 and UTF-8), testing both existing and non-existing substrings. The results were visualized using graphs.

## Results

### Observations:

- **Knuth-Morris-Pratt (KMP)** performs consistently well for both existing and non-existing substrings. Its time complexity of O(n + m) makes it efficient for long texts and patterns.
- **Rabin-Karp** works well for detecting existing substrings, but can be slower for non-existing substrings due to potential hash collisions, leading to a time complexity of O(n \* m) in the worst case.
- **Boyer-Moore** demonstrates strong performance, especially for longer patterns. Its average case is highly efficient, and the algorithm performs particularly well when the pattern does not appear in the text.

### Performance Comparison:

| Algorithm   | Article 1 - Existing Substring (s) | Article 1 - Non-Existing Substring (s) | Article 2 - Existing Substring (s) | Article 2 - Non-Existing Substring (s) |
| ----------- | ---------------------------------- | -------------------------------------- | ---------------------------------- | -------------------------------------- |
| KMP         | Fast                               | Fast                                   | Fast                               | Fast                                   |
| Rabin-Karp  | Moderate                           | Slower                                 | Moderate                           | Slower                                 |
| Boyer-Moore | Very Fast                          | Moderate                               | Very Fast                          | Moderate                               |

## Visualization

### Article 1 (Windows-1251 Encoding)

Below is a graphical representation of the performance of each substring search algorithm for **Article 1** (Windows-1251 encoded):

![Article 1 Substring Search Performance](/data_1.jpg)

### Article 2 (UTF-8 Encoding)

Below is a graphical representation of the performance of each substring search algorithm for **Article 2** (UTF-8 encoded):

![Article 2 Substring Search Performance](/data_2.jpg)

## Instructions to Run the Experiment

To reproduce the experiment on your computer, follow these steps:

### Prerequisites

Ensure you have Python installed. You also need the following libraries:

```sh
pip install matplotlib
```

### Running the Experiment

1. Clone this repository or download the script.
2. Navigate to the script directory.
3. Run the script using:

```sh
python substring_search_algorithms_test.py
```

This will generate the performance comparison graph and output execution times in the console.

## Conclusion

Knuth-Morris-Pratt (KMP) is the most balanced algorithm, performing efficiently on both existing and non-existing substrings. It is a reliable choice for general substring search tasks.

Rabin-Karp can be useful when dealing with multiple pattern searches, but it is slower for non-existing substrings due to hash collisions.

Boyer-Moore is the fastest algorithm for larger patterns and longer texts, making it an optimal choice for scenarios where the pattern is expected to be absent.

## Future Improvements

- Test the algorithms with larger datasets to assess their scalability.
- Implement an optimized version of Rabin-Karp to handle hash collisions more efficiently.
- Analyze the memory usage of each algorithm alongside execution time for a more comprehensive performance evaluation.
