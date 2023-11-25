import json
import os
import time

from tkinter import Tk, ttk, NW, SOLID
from tkinter.messagebox import askyesno, showinfo

from config import *


def close(main_window, mistake_int, speed_time):
    my_statistics = {'mistake': mistake_int.all_mst, 'all chr': mistake_int.all_chr,
                     'time': speed_time.all_time}

    file_path = os.path.join('src', 'statistic.json')
    with open(file_path, 'w') as f:
        json.dump(my_statistics, f)

    main_window.destroy()


def create_window():
    main_window = Tk()
    main_window.title("Keyboard trainer")

    main_window.geometry(f"{WINDOW_LENGTH}x{WINDOW_HIGHT}+{WINDOW_X_SHIFT}+{WINDOW_Y_SHIFT}")
    main_window.minsize(WINDOW_X_MIN_SIZE, WINDOW_Y_MIN_SIZE)
    main_window.maxsize(WINDOW_X_MAX_SIZE, WINDOW_Y_MAX_SIZE)
    return main_window


def create_label(main_window, cur_task, font1):
    example_label_x = 60
    example_label_y = 30

    example_label = ttk.Label(main_window, text=cur_task, font=font1)
    example_label.place(x=example_label_x, y=example_label_y)
    return example_label


def open_info(main_window, results, mistake_int, speed_time):
    result = askyesno(title="Congratulations", message="You have compiled all tasks! Do you want to do it again?")
    if result:
        results.key = 1
        showinfo("Congratulations", "Restart")
    else:
        showinfo("Congratulations", "Goodbye!")
        close(main_window, mistake_int, speed_time)


def clear_btn(mistake_int, speed_time):
    def clear():
        mistake_int.all_mst = 0
        mistake_int.all_chr = 0
        speed_time.all_time = 0

    restart_btn = ttk.Button(text="Clear all statistics", command=clear)
    restart_btn.pack()


def open_file(file_name):
    with open(file_name) as file:
        return json.load(file)


def create_frame(main_window, my_results, font1):
    total_progress = ttk.Frame(main_window, borderwidth=1, relief=SOLID, padding=[10])

    total_speed = ttk.Label(total_progress, font=font1)
    total_speed.pack(anchor=NW)

    total_mst = ttk.Label(total_progress, font=font1)
    total_mst.pack(anchor=NW)

    total_acc = ttk.Label(total_progress, font=font1)
    total_acc.pack(anchor=NW)

    total_speed["text"] = "Total Speed: " + str(my_results.speed) + " chr in min"
    total_mst["text"] = "Total Count of Mistakes: " + str(my_results.mistake)
    total_acc["text"] = "Total Accuracy: " + str(my_results.acc) + "%"

    total_progress.pack(anchor=NW, padx=5, pady=5)

    return total_progress


def clear_entry(main_window, entry_line, total_progress, cur_task):
    def on_key(event):
        total_progress.destroy()

    main_window.bind("<KeyPress>", on_key)

    entry_line.delete(0, len(cur_task))


def fix_stat(speed_time, mistake_int, cur_task, my_results):
    speed_time.end = time.time()

    speed_time.all_time += round(speed_time.end - speed_time.start, 2)

    mistake_int.all_chr += len(cur_task) + mistake_int.count
    mistake_int.all_mst += mistake_int.count

    mistake_int.count = 0
    my_results.mistake = mistake_int.all_mst

    my_results.speed = round(mistake_int.all_chr / speed_time.all_time * 60, 2)
    my_results.acc = round(((mistake_int.all_chr - mistake_int.all_mst) / mistake_int.all_chr * 100), 2)
