# frist practice

names = ["Ziad", "Ahmed", "Mohamed"]
for i in names:
    print(i, len(i), sep='-')

print("==============================")

# ---------------------------- Ziad Amin --------------------------- #

# second practice

print("Enter two lists:")

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

res = []

if len(arr1) >= len(arr2):
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            res.append(arr1[i])
else:
    for i in range(len(arr2)):
        if arr2[i] not in arr1:
            res.append(arr2[i])
    
print(res)
print("==============================")

# ---------------------------- Ziad Amin --------------------------- #

# third practice

std = {"name": "Ziad", "Age": 20}
std.update({"Hoppy": "Football"})

print(std.get("name"), std.get("Age"))
print(std)

for key, val in std.items():
    print(f"the {key} is {val}")

print("==============================")

# ---------------------------- Ziad Amin --------------------------- #

# forth practice

print("Enter two strings:")

def ok(s1, s2):
    mnlen = min(len(s1), len(s2))
    ok = True

    if len(s1) >= len(s2):
        for i in range(mnlen):
            if s2[i] not in s1:
                ok = False
                break
    else:
        for i in range(mnlen):
            if s1[i] not in s2:
                ok = False
                break
    return ok

a = input().strip()
b = input().strip()

print("YES" if ok(a, b) else "NO")
print("==============================")

# ---------------------------- Ziad Amin --------------------------- #

# fifth practice

n = 9
while True:
    num = int(input("Guess a number from 1 to 10: "))
    if num == n:
        print("Bravoo 3leeeek")
        break
print("==============================")

# ---------------------------- Ziad Amin --------------------------- #

# sixth practice

s = input("Enter a string: ").strip()
rev = s[::-1]

if(s == rev):
    print("isPalindrome")
else:
    print("notPalindrome")


# ---------------------------- Finished --------------------------- #

