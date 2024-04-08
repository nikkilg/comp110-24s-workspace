"""EX07: Evaluating Runtimes and Memory Usage."""

__author__ = "730394747"

from runtime_analysis_functions import evaluate_runtime
from runtime_analysis_functions import evaluate_memory_usage
import matplotlib.pyplot as plt
# had to download extension "matplotlib" in order for computer to recognize "plt"

START_SIZE: int = 0
END_SIZE: int = 1000


# evaluating runtime of selection sort function
times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - nikkilg")
plt.show()

# evaluating runtime of insertion_sort function
times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - nikkilg")
plt.show()

# evaluating memory usage of selection sort function
usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - nikkilg")
plt.show()

# evaluating memory usage of insertion sort function
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - nikkilg")
plt.show()