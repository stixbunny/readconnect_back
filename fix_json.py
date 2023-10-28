import json


def main():
    max_objects = 300
    json_bad_file = "amazon.books.json"
    json_good_file = "books.json"
    json_list = []
    with open(json_bad_file, encoding="utf-8") as file:
        lines = file.readlines()
        current_object = ""
        count = 0
        for line in lines:
            line = line.strip()
            if(line == "}" or line == "} {"):
                count += 1
                current_object += "}"
                json_object = json.loads(current_object)
                json_list.append(json_object)
                if(count == max_objects):
                    break
                current_object = "{"
            else:
                current_object += line
    print(f'read {count} json objects')
    with open(json_good_file, 'w', encoding="utf-8") as file:
        json.dump(json_list, file, indent=4, sort_keys=False, ensure_ascii=False)

if __name__ == "__main__":
    main()
