import os
matrix_link_str = ""

matrix_dict = {}
#"include":[{"repos":{"name":"foo","a":1,"b":2}},{"repos":{"name":"bar","a":3,"b":4}}]
matrix_name = ""
with open("beamline_info.yml") as file:
    for line in file:
        lsplit = line.split(' ')
        # print(lsplit)
        if len(lsplit) <= 1:
            matrix_name = line[:-2]
            first_arr = []
            matrix_dict[matrix_name] = first_arr
        elif lsplit[2] == "-":
            key = lsplit[3][:-1]
            value = lsplit[4][1:-2]
            element_arr = {key:value}
            matrix_dict.get(matrix_name).append(element_arr)
        elif len(lsplit) > 1:
            key = lsplit[4][:-1]
            value = lsplit[5].split("\"")[1]
            matrix_dict.get(matrix_name)[-1][key] = value
# matrix_link_str += "\\\"include\\\":[" + f"\\\"{matrix_name}\\\":"
# for element in matrix_dict.get(matrix_name):
#     matrix_link_str += "{"
#     print(element)
#     for kv_pair in element:
#         k, v = kv_pair, element.get(kv_pair)
#         matrix_link_str += f"\\\"{k}\\\":\\\"{v}\\\","
#     matrix_link_str = matrix_link_str[:-1]
#     matrix_link_str += "},"
# matrix_link_str = matrix_link_str[:-1]
# matrix_link_str += "}]"

matrix_link_str += "{\\\"include\\\":["
for element in matrix_dict.get(matrix_name):
    matrix_link_str += "{\\\"" + matrix_name + "\\\":{"
    for kv_pair in element:
        k, v = kv_pair, element.get(kv_pair)
        matrix_link_str += f"\\\"{k}\\\":\\\"{v}\\\","
    matrix_link_str = matrix_link_str[:-1]
    matrix_link_str += "}},"
matrix_link_str = matrix_link_str[:-1]
matrix_link_str += "]}"

def get_matrix_link():
    test_string = """
      "repos": [
        {
          "org": "NSLS-II-CSX",
          "repo": "profile_collection"
        },
        {
          "org": "NSLS-II-SRX",
          "repo": "profile_collection"
        }
      ]
    """
    return test_string

if __name__ == "__main__":
    print(get_matrix_link())
# os.system("echo LINK_STR=" + matrix_link_str + " >> $GITHUB_ENV")