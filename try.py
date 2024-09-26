import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # 讀取 CSV 檔案
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # 寫入 JSON 檔案
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def main():
    csv_file_path = 'username.csv'
    json_file_path = 'username.json'
    csv_to_json(csv_file_path, json_file_path)
    print(f"已將 {csv_file_path} 轉換為 {json_file_path}")

if __name__ == "__main__":
    main()