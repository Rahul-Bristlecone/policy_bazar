# compare without indexes
import json


class CompareJson():
    def __init__(self):
        self.file_extraction()

    def file_extraction(self):
        with open("../resources/data_file1.json", 'r') as datafile1:
            self.file1 = json.load(datafile1)
            # print(self.file1)

        with open("../resources/data_file2.json", 'r') as datafile2:
            self.file2 = json.load(datafile2)
            # print(self.file2)

    def compare(self):
        for data1 in self.file1["company"]["employees"]:
            for project in data1['projects']:
                print(project['projectName'])

        # save1 = [project['projectName'] for project in data1['projects'] in self.file1["company"]["employees"]]

        for data2 in self.file2["company"]["employees"]:
            for project in data2['projects']:
                print(project['projectName'])


if __name__ == '__main__':
    conf = CompareJson()
    print(conf.file_extraction())
    print(conf.compare())
