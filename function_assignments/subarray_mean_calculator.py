class SubarrayMeanCalculator:

    def read_input(self):
        """ Reads input values and queries. """
        number_of_elements, number_of_queries = map(int, input().split())
        array_values = list(map(int, input().split()))

        queries = []
        for _ in range(number_of_queries):
            left_index, right_index = map(int, input().split())
            queries.append((left_index, right_index))

        return array_values, queries

    def build_prefix_sum(self, array_values):
        """ Builds prefix sum array. """
        prefix_sum = [0]
        for value in array_values:
            prefix_sum.append(prefix_sum[-1] + value)

        return prefix_sum

    def calculate_subarray_mean(self, prefix_sum, left_index, right_index):
        """ Returns the floor of the mean for a given subarray. """
        subarray_sum = prefix_sum[right_index] - prefix_sum[left_index - 1]
        subarray_length = right_index - left_index + 1

        return subarray_sum // subarray_length

    def process_queries(self, prefix_sum, queries):
        """ Processes each query and prints the result. """
        for left_index, right_index in queries:
            mean_value = self.calculate_subarray_mean(
                prefix_sum, left_index, right_index
            )
            print(mean_value)

    def run(self):
        """ Controls the program flow. """
        array_values, queries = self.read_input()
        prefix_sum = self.build_prefix_sum(array_values)
        self.process_queries(prefix_sum, queries)

SubarrayMeanCalculator().run()
