import json
with open(
        "E:\main-project\web-recon\webSight\webSight\output\directory\Directory_2023-04-17-12-54.json", "r"
    ) as read_directory_file:
        # for line in read_directory_file:
        #     directory_list.append(line)
        data = read_directory_file.read()[2:]

status = []
size = []
directory_link = []
f=open("E:\main-project\web-recon\webSight\webSight\output\directory\Directory_2023-04-17-12-54.json")
file=json.load(f)
    # print(data)
for line in file['results']:
        # print(line)
        # row = re.split(",", line)
    print(line['content-length'])