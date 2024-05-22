import json

json_file = open("DNS.json", "r")
dns_arr = json.load(json_file)
json_file.close()


def check_DNS(url):
    if url in dns_arr:
        return dns_arr[url]
    else:
        return "URL NOT FOUND, PLEASE TRY A DIFFERENT URL"
