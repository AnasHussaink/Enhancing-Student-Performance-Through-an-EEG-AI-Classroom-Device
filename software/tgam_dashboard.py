# Historical prototype: read docs/KNOWN_ISSUES.md before use.
import serial
import numpy as np
import pandas as pd
from datetime import datetime
from collections import defaultdict
import threading
import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageTk
import os

# Initialize global variables to store data
time_data = []
attention_data = []
high_alpha_data = []
high_beta_data = []
mid_gamma_data = []

# DataFrame to store attention data with time
attention_df = pd.DataFrame(columns=['Time', 'Attention'])

# Dictionary to store daily data
daily_data = defaultdict(list)

# Define the path where the CSV file will be saved
csv_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'local')
csv_file_path = os.path.join(csv_directory, 'attention_session.csv')

# Ensure the directory exists
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)


def read_tgam_data(serial_port):
    ser = serial.Serial(serial_port, 57600)  # Open serial port
    while True:
        if ser.read() == b'\xaa' and ser.read() == b'\xaa':  # Sync bytes
            packet_length = ser.read(1)[0]
            payload = ser.read(packet_length)
            checksum = ser.read(1)[0]
            if checksum == (0xFF - (sum(payload) & 0xFF)):
                attention, high_alpha, high_beta, mid_gamma = parse_payload(payload)
                if attention is not None and high_alpha is not None:
                    update_data(attention, high_alpha, high_beta, mid_gamma)
                    save_attention_data(attention)
                    update_gui(attention, high_alpha, high_beta, mid_gamma)


def parse_payload(payload):
    index = 0
    attention = None
    high_alpha = high_beta = mid_gamma = None

    while index < len(payload):
        code = payload[index]
        index += 1
        try:
            if code == 0x04 and index < len(payload):
                attention = payload[index]
                index += 1
            elif code == 0x83 and index + 23 < len(payload):
                index += 6  # Skip delta and theta
                high_alpha = (payload[index + 3] << 16) | (payload[index + 4] << 8) | payload[index + 5]
                high_beta = (payload[index + 9] << 16) | (payload[index + 10] << 8) | payload[index + 11]
                mid_gamma = (payload[index + 15] << 16) | (payload[index + 16] << 8) | payload[index + 17]
                index += 18
        except IndexError as e:
            print(f'IndexError: {e}, code: {code}, index: {index}, payload length: {len(payload)}')
            break

    return attention, high_alpha, high_beta, mid_gamma


def update_data(attention, high_alpha, high_beta, mid_gamma):
    global time_data, attention_data, high_alpha_data, high_beta_data, mid_gamma_data

    # Append new data to the lists
    current_time = datetime.now()
    time_data.append(current_time)
    attention_data.append(attention)
    high_alpha_data.append(high_alpha)
    high_beta_data.append(high_beta)
    mid_gamma_data.append(mid_gamma)

    # Keep the data lists to a maximum length
    max_length = 100
    if len(time_data) > max_length:
        time_data.pop(0)
        attention_data.pop(0)
        high_alpha_data.pop(0)
        high_beta_data.pop(0)
        mid_gamma_data.pop(0)


def save_attention_data(attention):
    global attention_df, daily_data
    # Get current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Create a new DataFrame row
    new_row = pd.DataFrame({'Time': [current_time], 'Attention': [attention]})
    # Append new row to the DataFrame
    attention_df = pd.concat([attention_df, new_row], ignore_index=True)

    # Append data to daily report
    daily_data[date_str].append(attention)

    # Save the DataFrame to a CSV file every 10 entries
    if len(attention_df) % 10 == 0:
        print(f"Saving to CSV: {len(attention_df)} entries at {csv_file_path}")  # Debug statement
        try:
            attention_df.to_csv(csv_file_path, index=False)
            print(f"Successfully saved to {csv_file_path}")
        except Exception as e:
            print(f"Error saving CSV file: {e}")


def update_gui(attention, high_alpha, high_beta, mid_gamma):
    root.after(0, update_attention_gauge, attention)
    root.after(0, plot_data)
    root.after(0, update_raw_values, attention, high_alpha, high_beta, mid_gamma)


def update_attention_gauge(attention):
    # Update the gauge plot
    ax_gauge.clear()
    draw_semi_circular_gauge(ax_gauge, attention)
    canvas_gauge.draw()


def plot_data():
    # Clear the plots
    axs[0].clear()
    axs[1].clear()

    # Plot High Alpha, High Beta, and Mid Gamma Waves on a single plot
    axs[0].plot(time_data, high_alpha_data, label='High Alpha', color='cyan')
    axs[0].plot(time_data, high_beta_data, label='High Beta', color='lime')
    axs[0].plot(time_data, mid_gamma_data, label='Mid Gamma', color='orange')
    axs[0].set_ylabel('Wave Amplitude')
    axs[0].legend(loc='upper right')
    axs[0].set_title('High Alpha, Beta, and Gamma Waves Over Time')

    # Plot daily average attention as a bar chart
    if daily_data:
        dates = list(daily_data.keys())
        averages = [np.mean(daily_data[date]) for date in dates]
        axs[1].bar(dates, averages, color='blue')
        axs[1].set_ylabel('Average Attention')
        axs[1].set_title('Daily Average Attention')

        for i, avg in enumerate(averages):
            label = categorize_average(avg)
            axs[1].text(i, avg, label, ha='center', va='bottom')

    # Adjust layout to fit the content
    fig_data.tight_layout()

    # Refresh the canvas
    canvas.draw()


def categorize_average(avg):
    # Categorize the average based on the score
    if avg >= 80:
        return "Best"
    elif avg >= 60:
        return "Good"
    elif avg >= 40:
        return "Bad"
    else:
        return "Worse"


def draw_semi_circular_gauge(ax, value):
    radius = 0.3  # Adjusted the gauge size
    theta = np.linspace(0, np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)

    # Draw the background semi-circle
    ax.fill(x * radius, y * radius, color='lightgray', alpha=0.7)

    # Draw the filled arc
    arc_value = (value / 100.0) * np.pi
    theta_fill = np.linspace(0, arc_value, 100)
    x_fill = np.cos(theta_fill)
    y_fill = np.sin(theta_fill)
    x_fill = np.append(x_fill, [0])
    y_fill = np.append(y_fill, [0])
    ax.fill(x_fill * radius, y_fill * radius, color='blue', alpha=0.8)

    # Add a circle in the center
    ax.add_patch(patches.Circle((0, 0), radius * 0.4, color='white'))

    # Add the attention value text
    ax.text(0, 0, f'{int(value)}', ha='center', va='center', fontsize=16, color='black', fontweight='bold')

    ax.set_xlim(-radius, radius)
    ax.set_ylim(0, radius)
    ax.set_aspect('equal')
    ax.axis('off')


def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        try:
            # Open and resize the image
            image = Image.open(file_path)
            image.thumbnail((150, 150))  # Resize to fit the image preview
            image = ImageTk.PhotoImage(image)

            # Update the image label
            label_image.config(image=image)
            label_image.image = image  # Keep a reference to avoid garbage collection

            # Update name and roll number from entry fields
            student_name = name_entry.get()
            student_roll_no = roll_no_entry.get()
            label_name.config(text=f"Name: {student_name}")
            label_roll_no.config(text=f"Roll No: {student_roll_no}")
        except Exception as e:
            print(f"Error loading image: {e}")


def update_raw_values(attention, high_alpha, high_beta, mid_gamma):
    # Update raw EEG value labels
    label_attention_value.config(text=f"Attention: {attention}")
    label_high_alpha_value.config(text=f"High Alpha: {high_alpha}")
    label_high_beta_value.config(text=f"High Beta: {high_beta}")
    label_mid_gamma_value.config(text=f"Mid Gamma: {mid_gamma}")

    # Add raw EEG frequency data labels
    label_raw_data.config(
        text=f"Raw Frequency Data:\nAttention: {attention}\nHigh Alpha: {high_alpha}\nHigh Beta: {high_beta}\nMid Gamma: {mid_gamma}")


# Initialize the GUI
root = tk.Tk()
root.title("EEG Data Visualization")
root.geometry("1100x700")  # Adjusted size for better fit

# Create a frame for student info
frame_info = tk.Frame(root, bg='#f0f0f0')
frame_info.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

# Create labels for name, roll number, and image preview
label_name = tk.Label(frame_info, text="Name: ", font=("Helvetica", 14), bg='#f0f0f0')
label_name.grid(row=0, column=0, sticky='w')

label_roll_no = tk.Label(frame_info, text="Roll No: ", font=("Helvetica", 14), bg='#f0f0f0')
label_roll_no.grid(row=1, column=0, sticky='w')

label_image = tk.Label(frame_info, bg='#f0f0f0')
label_image.grid(row=2, column=0, pady=10)

# Create entry fields for name and roll number
name_entry = ttk.Entry(frame_info, font=("Helvetica", 12))
name_entry.grid(row=0, column=1)
name_entry.bind("<KeyRelease>", lambda e: label_name.config(text=f"Name: {name_entry.get()}"))

roll_no_entry = ttk.Entry(frame_info, font=("Helvetica", 12))
roll_no_entry.grid(row=1, column=1)
roll_no_entry.bind("<KeyRelease>", lambda e: label_roll_no.config(text=f"Roll No: {roll_no_entry.get()}"))

# Create a button to upload an image
btn_upload = ttk.Button(frame_info, text="Upload Image", command=upload_image)
btn_upload.grid(row=3, column=0, columnspan=2, pady=10)

# Create a frame for the gauge and data plots
frame_plots = tk.Frame(root, bg='#f0f0f0')
frame_plots.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

# Create a header label for the gauge
header_label = tk.Label(frame_plots, text="Real-time Attention Level", font=("Helvetica", 16, "bold"), bg='#f0f0f0')
header_label.grid(row=0, column=0, pady=(10, 5), columnspan=2)

# Create a figure and axes for the gauge
fig_gauge, ax_gauge = plt.subplots(figsize=(4, 1.5))  # Adjusted size
draw_semi_circular_gauge(ax_gauge, 0)
canvas_gauge = FigureCanvasTkAgg(fig_gauge, frame_plots)
canvas_gauge.get_tk_widget().grid(row=1, column=0, padx=10, pady=5)

# Create a figure and axes for the data plots
fig_data, axs = plt.subplots(2, 1, figsize=(6, 5))  # Adjusted size
canvas = FigureCanvasTkAgg(fig_data, frame_plots)
canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=5, rowspan=2)

# Create labels for raw EEG values
label_attention_value = tk.Label(frame_plots, text="Attention: 0", font=("Helvetica", 12), bg='#f0f0f0')
label_attention_value.grid(row=2, column=0, sticky='w', padx=10, pady=5)

label_high_alpha_value = tk.Label(frame_plots, text="High Alpha: 0", font=("Helvetica", 12), bg='#f0f0f0')
label_high_alpha_value.grid(row=3, column=0, sticky='w', padx=10, pady=5)

label_high_beta_value = tk.Label(frame_plots, text="High Beta: 0", font=("Helvetica", 12), bg='#f0f0f0')
label_high_beta_value.grid(row=4, column=0, sticky='w', padx=10, pady=5)

label_mid_gamma_value = tk.Label(frame_plots, text="Mid Gamma: 0", font=("Helvetica", 12), bg='#f0f0f0')
label_mid_gamma_value.grid(row=5, column=0, sticky='w', padx=10, pady=5)

# Create label for raw EEG frequency data
label_raw_data = tk.Label(frame_plots,
                          text="Raw Frequency Data:\nAttention: 0\nHigh Alpha: 0\nHigh Beta: 0\nMid Gamma: 0",
                          font=("Helvetica", 12), bg='#f0f0f0', justify='left')
label_raw_data.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

# Start the serial thread
serial_thread = threading.Thread(target=read_tgam_data, args=('COM4',), daemon=True)
serial_thread.start()

# Start the GUI loop
root.mainloop()
