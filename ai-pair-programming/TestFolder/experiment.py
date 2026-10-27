class LargestSumSubarray:
    """
    A class to find the largest sum of a contiguous subarray using Kadane's Algorithm.
    """
    def __init__(self, array):
        """
        Initialize with the input array.

        Args:
            array (list of int): The input array.
        """
        self.array = array

    def find_max_sum(self):
        """
        Finds the largest sum of a contiguous subarray.

        Returns:
            tuple: (maximum_sum, start_index, end_index)
        """
        max_so_far = self.array[0]
        max_ending_here = self.array[0]
        start = end = s = 0

        for i in range(1, len(self.array)):
            if self.array[i] > max_ending_here + self.array[i]:
                max_ending_here = self.array[i]
                s = i
            else:
                max_ending_here += self.array[i]

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = s
                end = i

        return max_so_far, start, end

    def display_result(self):
        """
        Displays the result of the largest sum subarray.
        """
        max_sum, start, end = self.find_max_sum()
        print(f"Largest sum subarray: {self.array[start:end+1]}")
        print(f"Maximum sum: {max_sum}")
        print(f"Start index: {start}, End index: {end}")

# Example usage:
def main():
    arr = [2, -8, 3, -2, 4, -10]  # You can change this array
    subarray_finder = LargestSumSubarray(arr)
    subarray_finder.display_result()

if __name__ == "__main__":
    main()