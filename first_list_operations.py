l1 = [
    2,5,7,8,11,18,23,31
]

## Initializing lists
list_odds = []
list_evens = []
list_sqr = []

## Getting all odd nos. in this list
for i in l1:
    if i%2!=0:                  # Checking whether the number is odd
        list_odds.append(i)     # Adding to the odd nos list

print(list_odds)

## Getting all even nos. in this list
for i in l1:
    if i%2==0:                  # Checking whether the number is even
        list_evens.append(i)     # Adding to the even nos list

print(list_evens)

list_reverse = l1[::-1]
print(list_reverse)

## Calculating square of each list number
list_sqr = []
for i in l1:
    list_sqr.append(i*i)
print(list_sqr)
