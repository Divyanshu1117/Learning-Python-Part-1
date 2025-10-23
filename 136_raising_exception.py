def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Divyanshu")

a = increment(364)
print(a)