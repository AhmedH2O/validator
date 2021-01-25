import requests
def valid(x):
    req = requests.get(x)
    val = req.status_code
    if val == 200:
        print("Great!, this site can be scrapped ")
    else:
        print("Oh No,this site maybe can't be scrapped error = {val}")
valid(input("please input your url to check : "))