class Food_Search_Engine:
    # original data from crawled json file
    original_data = []
    # the result after filter/ranking
    query_result = []

    def __init__(self, json_file_name):
        self.load_data(json_file_name)
        self.reset()

    def load_data(self, json_file_name):
        with open(json_file_name) as json_data:
            self.original_data = json.load(json_data)

    def reset(self):
        self.query_result = list(self.original_data)

    def filter(self, filter_cond):
        # your code here

    def rank(self, ranking_weight):
        # your code here

    def find_similar(self, restaurant, similiarity_weight, k):
        # your code here

    def print_query_result(self):
        print('Overall number of query_result: %d' % len(self.query_result))
        for restaurant in self.query_result:
            print(restaurant)
