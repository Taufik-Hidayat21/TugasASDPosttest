#Nama : Taufik Hidayat
#NIM : 2209116097
#Kelas : Sistem Informasi B '22
import random #Berfungsi untuk memasukan modul random pada code

def quickSort(arr): #function def untuk quick sort
    if len(arr) <= 1: #Jika panjang list atau jumlah elemen yang ada pada list kurang dari atau sama dengan satu
        return arr #maka akan mengembalikan function
    else:
        pivot = arr[0] #pivot yang digunakan adalah elemen list arr pada index ke-0

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot] #jika nilai x kurang dari atau sama dengan pivot yang digunakan maka akan dimasukan pada list variabel "less"

        greater = [x for x in arr[1:] if x > pivot]#jika nilai x lebih dari pivot yang digunakan maka akan dimasukan pada list variabel "greater"
    
        return quickSort(less) + [pivot] + quickSort(greater) #mengembalikan nilai dari quicksort list arr ditambah dengan nilai pivot dan ditambah quicksort list greater

def shellSort(data): #function def shellsort untuk menjalankan algoritma shell sort
    gap = (len(data)//2) #variabel "gap" menyimpan nilai panjang list arr atau data dibagi dengan dua
    a=0 #variabel "a" menyimpan nilai 0

    while gap > 0 : #selama nilai variabel "gap" lebih dari 0 maka akan menjalankan function didalamnya atau dibawahnya 
        for i in range(gap,len(data)):#melakukan perulangan dengan jarak antara nilai variabel "gap" sampai dengan nilai panjang list "data"
            value = data[i] #variabel value digunakan untuk menyimpan elemen list "data" index ke-i
            j = i #nilai variabel "j" sama dengan "i" 

            while j >= gap and data[j-gap] > value: #selama nilai  variabel "j" lebih dari atau sama dengan nilai variabel "gap" dan elemen list data index ke-"j" dikurangi "gap"
                data[j] = data[j-gap] #elemen list "data" index ke-"j" sama dengan elemen "data" index ke-"j" dikurangi "gap"
                j-=gap #nilai variabel "j" dikurangi nilai variabel "gap"

            data[j] = value #elemen "data" index ke-"j" sama dengan nilai variabel "value"
            print(data)
        print("Iterasi ke",a,": ",data,"dengan gap ",gap )
        a+=1 #nilai variabel "a" ditambah dengan satu

        gap //= 2 #setelah setiap iterasi maka nilai variabel "gap" akan dibagi dua

    return data #mengembalikan nilai dari variabel "data" setelah function shell sort selesai

list1 = [1,2,3,4,5,6,7,8,9,10] #menyimpan list yang berisi angka
random.shuffle(list1) #mengacak isi dari "list1" menggunakan function shuffle

print('''
1. Untuk Quicksort
2. Untuk Shellsort
''')
while True: #digunakan untuk melakukan perulangan
    a = input("Masukan Sorting Yang Ingin Digunakan: ") #digunakan untuk menyimpan inputan sorting yang akan digunakan
    if a == "1": #jika user memilih "1" maka akan menjalankan function quick sort
        print(f'list sebelum disort: {list1}')
        print()
        print(f'list setelah disort: {quickSort(list1)}')
        break #setelah function dijalankan maka akan mem break perulangan
    elif a == "2": #jika memilih "2" maka akan menjalankan fucntion shell sort
        print(f'list sebelum disort: {list1}')
        print(f'list setelah disort: {shellSort(list1)}')
        break
    else:
        print("Input salah atau tidak ada") #jika input yang dimasukan tidak ada maka akan mengulangi inputan