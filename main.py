from tkinter import font

from classes import *
from window_functions import *


def close():
    my_statistics = {'mistake': mistake_int.all_mst, 'all chr': mistake_int.all_chr,
                     'time': speed_time.all_time}

    with open('statistic.json', 'w') as f:
        json.dump(my_statistics, f)

    main_window.destroy()


main_window = create_window()

font1 = font.Font(family="Book Antiqua", size=20, weight="normal", slant="italic")
mistake_int = Mistake()
speed_time = TimeSpeed()
my_results = Results()

my_results.task = open_file('example_task.json')
my_old_stat = open_file('statistic.json')

speed_time.all_time = my_old_stat['time']
mistake_int.all_mst = my_old_stat['mistake']
mistake_int.all_chr = my_old_stat['all chr']


def typing_field():
    example_label = create_label(main_window, my_results.task[str(my_results.key)], font1)

    def is_valid(new_val, smb):
        cur_task = my_results.task[str(my_results.key)]

        if int(smb) == 0:
            speed_time.start = time.time()

        if len(cur_task) - 1 == int(smb) and cur_task[int(smb)] == new_val[int(smb)]:
            fix_stat(speed_time, mistake_int, cur_task, my_results)
            total_progress = create_frame(main_window, my_results, font1)

            clear_entry(main_window, entry_line, total_progress, cur_task)
            my_results.key += 1

            if my_results.key <= len(my_results.task):
                example_label.config(text=my_results.task[str(my_results.key)])
            else:
                example_label.config(text=my_results.task['1'])
                my_results.key = 1
                open_info(main_window, my_results, mistake_int, speed_time)
        else:
            if cur_task[int(smb)] != new_val[int(smb)]:
                mistake_int.count += 1

        if int(smb) >= len(cur_task):
            return False

        return cur_task[int(smb)] == new_val[int(smb)]

    entry_check = (main_window.register(is_valid), "%P", "%i")
    entry_line = ttk.Entry(validate="key", validatecommand=entry_check, width=200, font=font1)
    entry_line.pack(anchor=NW, padx=60, pady=70)


typing_field()

clear_btn(mistake_int, speed_time)

main_window.protocol("WM_DELETE_WINDOW", close)
main_window.bind('<Escape>', close)

main_window.mainloop()
