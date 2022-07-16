#!/home/st_yudi/programs/anaconda3/bin/python3

# menerima input angka dari user
n = int(input("Masukan input angka yang diinginkan  disini: "))

# loop dari 1 - n mencetak fizzbuzz
for i in range(1,n+1):
    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(str(i))
