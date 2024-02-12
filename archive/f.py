dic = {
    "a": 3,
    "c": 1,
    "ASD": 9
}


r = [key for key, val in dic.items() for _ in range(val)]
print(r)