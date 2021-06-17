import tkinter as tk
from tkinter.filedialog import askdirectory
from functions import *
from plotter import *
import os

def choose_folder():
    folder = askdirectory()
    chosen_folder_label.config(text = folder)

window = tk.Tk()
window.title("Openpose Plot Creator")
window.minsize(800, 600)

chosen_joint = tk.StringVar()
chosen_joint.set("Select an Option")

choose_folder_frame = tk.Frame(borderwidth=2, relief="solid")
choose_folder_label = tk.Label(master=choose_folder_frame, text="Select the folder containing the JSON files", height = 3, padx=10)
choose_folder_button = tk.Button(master=choose_folder_frame, text="Choose", command=choose_folder)
chosen_folder_label = tk.Label(master=choose_folder_frame)
choose_folder_frame.pack(pady=10)
choose_folder_label.pack()
choose_folder_button.pack()
chosen_folder_label.pack()

choose_joint_frame = tk.Frame(borderwidth=2, relief="solid")
choose_joint_label = tk.Label(master=choose_joint_frame, text="Select the Joint to Graph")
choose_joint_menu = tk.OptionMenu(choose_joint_frame, chosen_joint, *JOINTS.values())
choose_joint_frame.pack(pady=10)
choose_joint_label.pack(padx=5, pady=5)
choose_joint_menu.pack(padx=5, pady=5)

plot_frame = tk.Frame(borderwidth=2, relief="solid")
plot_label = tk.Label(master=plot_frame, text="Plot options")
generate_plot_button = tk.Button(
    master=plot_frame,
    text="Generate graph",
    command=lambda: plot_joint_over_time(
        list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint.get())],
        load_openpose(chosen_folder_label.cget("text"))))
save_plot_button = tk.Button(
    master=plot_frame,
    text="Save graph",
    command=lambda: plot_joint_over_time(
        list(JOINTS.keys())[list(JOINTS.values()).index(chosen_joint.get())],
        load_openpose(chosen_folder_label.cget("text")),
        show=False,
        save=True,
        save_dir=os.path.join(os.path.split(chosen_folder_label.cget("text"))[0],
                              os.path.split(os.path.split(chosen_folder_label.cget("text"))[0])[1] + "_plot.png")))
plot_frame.pack(pady=10)
plot_label.pack()
generate_plot_button.pack(padx=5, pady=5)
save_plot_button.pack(padx=5, pady=5)

window.mainloop()