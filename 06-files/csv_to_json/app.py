import json


class Converter:
    def __init__(self, csv_file, json_file):
        self.csv_content = self.get_csv(csv_file)
        self.json_file = json_file
        self.json_content = self.build_json()

    def get_csv(self, filename):
        file = open(filename, "r")
        return [line.strip() for line in file.readlines()]

    def build_json(self):
        json_arr = []
        json_content = {}

        for team in self.csv_content:
            info = [field.strip() for field in team.split(",")]
            json_content["club"] = info[0]
            json_content["city"] = info[1]
            json_content["country"] = info[2]
            json_arr.append(json_content)
            json_content = {}

        return json_arr

    def write_json_file(self):
        file = open(self.json_file, "w")
        file.write(json.dumps(self.json_content, indent=4))
        file.close()


converter = Converter("csv_file.txt", "json_file.txt")
converter.write_json_file()
