# Write your always_false function here:
def always_false(num):
    return True if num > 0 and num < 0 else False


print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
