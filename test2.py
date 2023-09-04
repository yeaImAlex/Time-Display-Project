import tkinter as tk
import datetime
import pytz

root = tk.Tk()
current_time = ''
display_active = False  

def update_time():
    global current_time, display_active
    if display_active:  
        now = datetime.datetime.now(tz=pytz.timezone('Asia/Kuala_Lumpur'))
        current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")
        print(f"Current time: {current_time}")
        time_label.config(text=current_time)
        root.after(1000, update_time)

def start_time():
    global display_active
    start_button.config(state='disabled')
    stop_button.config(state='normal')
    if not display_active:  
        display_active = True
        update_time()

def stop_time():
    start_button.config(state='normal')
    stop_button.config(state='disabled')
    global display_active
    display_active = False
    print('time has stopped displaying')

time_label = tk.Label(root, text=current_time)
time_label.pack()

start_button = tk.Button(root, text='Start Time', command=start_time)
start_button.pack()

stop_button = tk.Button(root, text='Stop Time', command=stop_time)
stop_button.config(state='disabled')
stop_button.pack()

root.mainloop()

