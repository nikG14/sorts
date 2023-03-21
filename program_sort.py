from tkinter import *
from tkinter import messagebox as mb
from datetime import datetime
import time

def create_data():
    arr = entry.get()
    trying = arr.replace(" ", "")
    trying = trying.replace("-", "")
    if not trying.isdigit():
        mb.showerror("Ошибка", "Должно быть введено число")
    else: 
        arr = arr.split(" ")
        result = list(map(int, arr))
    return result

def create_output(arr, end):
    lab1['text'] = ' '.join(str(end))
    lab['text'] = ' '.join(str(arr))

def bubble_sort():
    arr = create_data()
    start = datetime.now()
    N = len(arr)
            
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                buff = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = buff
    time.sleep(0.1)
    end = datetime.now() - start
    create_output(arr, end)

def selection_sort():     
    arr = create_data()
    start = datetime.now()

    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j
        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]

    time.sleep(0.1)
    end = datetime.now() - start
    create_output(arr, end)

def insertion_sort():
    arr = create_data()
    start = datetime.now()

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    time.sleep(0.1)
    end = datetime.now() - start
    create_output(arr, end)

def partition(nums, low, high, start):
    
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]
    
def quick_sort():
    nums = create_data()
    start = datetime.now()
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high, start)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    time.sleep(0.1)
    end = datetime.now() - start
    create_output(nums, end)

def info_abt_sys():
    mb.showinfo("Руководство пользователя", 
                "Программа предназначена для сортировки данных, которые ввел пользователь. Данные должны представлять из себя набор чисел, введённых строго через пробел, никаких букв и прочих символов, кроме знака минус, означающего, что число отрицательное.В поле для ввода данных вводятся числа, после нажатием на ту или иную кнопку выбирается вид сортировки.В полях для вывода данных отобразится результат сортировки и время её проведения.")

root = Tk()

f_right = Frame(root)

entry = Entry(root, width=50)

lab = Label(f_right, width=50, bg='black', fg='white')
lab1 = Label(f_right, width=50, bg='black', fg='white')

r_var = IntVar()
r_var.set(0)

f = Frame(root)

info_button = Button(root, width=25, text="Руководство пользователя", command=info_abt_sys)

bubble_box = Radiobutton(f, text='Сортировка пузырьком', variable=r_var, value=0, indicatoron=0, command=bubble_sort)
selection_box = Radiobutton(f, text='Сортировка выбором', variable=r_var, value=1, indicatoron=0, command=selection_sort)
insertion_box = Radiobutton(f, text='Сортировка вставками', variable=r_var, value=2, indicatoron=0, command=insertion_sort)
quick_sort_box = Radiobutton(f, text='Быстрая сортировка', variable=r_var, value=3, indicatoron=0, command=quick_sort)

entry.pack(expand=1,ipady=5,pady=5)
info_button.pack()

f.pack(side=LEFT, padx=10, pady=10)
f_right.pack(side=RIGHT, padx=10, pady=10)

bubble_box.pack(ipady=5, pady=5)
selection_box.pack(ipady=5, pady=5)
quick_sort_box.pack(ipady=5, pady=5)
insertion_box.pack(ipady=5, pady=5)

lab.pack(ipady=5, pady=5)
lab1.pack(ipady=5, pady=5)

root.mainloop()