import sys
import tkinter as tk
from tkinter import filedialog

debug = False
in_pos = 0
if debug:
    grid = [[0 for _ in range(10)] for _ in range(10)]
else:
    grid = [[0 for _ in range(1024)] for _ in range(1024)]
position = (0, 0)
rotation = 1
result = ""


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CAR# Scripts", "*.car#"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            code = file.read()
            input_text_widget.delete("1.0", tk.END)
            input_text_widget.insert(tk.END, code)


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".car#", filetypes=[("CAR# Scripts", "*.car#"), ("All "
                                                                                                               "files",
                                                                                                               "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            code = input_text_widget.get("1.0", tk.END)
            file.write(code)


def reset():
    global in_pos
    global grid
    global position
    global rotation
    global result
    output_text_widget.config(state=tk.NORMAL)
    output_text_widget.delete("1.0", tk.END)
    output_text_widget.config(state=tk.DISABLED)
    in_pos = 0
    if debug:
        grid = [[0 for _ in range(10)] for _ in range(10)]
    else:
        grid = [[0 for _ in range(1024)] for _ in range(1024)]
    position = (0, 0)
    rotation = 1
    result = ""


def run_command(command):
    usr_in = input_text_widget2.get("1.0", tk.END)
    global result
    global rotation
    global position
    global in_pos
    match command:
        case "/":
            if rotation > 1:
                rotation -= 1
            else:
                rotation = 4
        case "\\":
            if rotation < 4:
                rotation += 1
            else:
                rotation = 1
        case "<":
            x, y = position
            grid[y][x] = ord(usr_in[in_pos])
            in_pos += 1
        case ">":
            x, y = position
            result += chr(grid[y][x])
        case "+":
            x, y = position
            grid[y][x] += 1
        case "=":
            x, y = position
            result += str(grid[y][x])
        case "^":
            match rotation:
                case 1:
                    position = (position[0], position[1] + 1)
                case 2:
                    position = (position[0] + 1, position[1])
                case 3:
                    position = (position[0], position[1] - 1)
                case 4:
                    position = (position[0] - 1, position[1])
        case "-":
            x, y = position
            grid[y][x] -= 1


def main():
    global result
    skip = -1
    code = input_text_widget.get("1.0", tk.END)
    i = -1
    # noinspection PyBroadException
    try:
        while i != len(code):
            i += 1
            if i > skip:
                match code[i]:
                    case "[":
                        x, y = position
                        if grid[y][x] == 0:
                            stack = []
                            for num, char in enumerate(code):
                                if char == '[':
                                    stack.append(num)
                                elif char == ']':
                                    opening_bracket_index = stack.pop()
                                    if opening_bracket_index == i:
                                        skip = num
                    case "]":
                        x, y = position
                        if grid[y][x] != 0:
                            stack = []
                            for num, char in enumerate(code):
                                if char == '[':
                                    stack.append(num)
                                elif char == ']':
                                    opening_bracket_index = stack.pop()
                                    if i == i:
                                        i = opening_bracket_index - 1
                    case _:
                        run_command(code[i])
    except:
        if debug:
            for line in grid:
                print(line)
        output_text_widget.config(state=tk.NORMAL)
        output_text_widget.delete("1.0", tk.END)
        output_text_widget.insert(tk.END, result)
        output_text_widget.config(state=tk.DISABLED)
        return 0


def on_closing():
    root.destroy()
    sys.exit()


def open_gui():
    global debug_gui
    global gui_visible
    global position
    if gui_visible:
        debug_gui.withdraw()
        gui_visible = False
    elif debug_gui is None:
        debug_gui = tk.Toplevel(root)
        debug_gui.title("Debug GUI")

        # Add widgets and functionality for the debug GUI as needed
        x, y = position
        grid_frame = tk.Frame(debug_gui)
        grid_frame.pack(padx=10, pady=10)

        # Display a grid of 11x11 cells with their values
        for i in range(y - 5, y + 6):
            for j in range(x - 5, x + 6):
                cell_value = grid[i][j] if 0 <= i < len(grid) and 0 <= j < len(grid[0]) else 0

                # Highlight the cell at the current position
                bg_color = "yellow" if (i, j) == (y, x) else "white"

                cell_label = tk.Label(grid_frame, text=str(cell_value), width=5, height=2, borderwidth=1,
                                      relief="solid",
                                      bg=bg_color)
                cell_label.grid(row=i - (y - 5), column=j - (x - 5))
        # Handle closing the debug GUI properly
        debug_gui.protocol("WM_DELETE_WINDOW", lambda: close_debug_gui())
        gui_visible = True
    else:
        debug_gui.deiconify()
        gui_visible = True


def close_debug_gui():
    global debug_gui
    global gui_visible
    debug_gui.destroy()
    debug_gui = None
    gui_visible = False


debug_gui = None
gui_visible = False

root = tk.Tk()
root.title("CAR# interpreter by Niko Strauch")
root.configure(bg="#ddd")
root.iconbitmap("")

tk.Label(root, text="Code", bg="#ddd").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Input", bg="#ddd").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Label(root, text="Output", bg="#ddd").grid(row=5, column=0, padx=10, pady=5, sticky="w")

input_text_widget = tk.Text(root, wrap=tk.WORD, width=100, height=10, bd=1, relief=tk.SOLID)
input_text_widget.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

input_text_widget2 = tk.Text(root, wrap=tk.WORD, width=100, height=1, bd=1, relief=tk.SOLID)
input_text_widget2.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

process_button = tk.Button(root, text="Process", command=main, bd=1, relief=tk.SOLID)
process_button.grid(row=4, column=0, padx=10, pady=5)

reset_button = tk.Button(root, text="Reset", command=reset, bd=1, relief=tk.SOLID)
reset_button.grid(row=4, column=1, padx=10, pady=5)

output_text_widget = tk.Text(root, wrap=tk.WORD, width=100, height=10, state=tk.DISABLED, bd=1, relief=tk.SOLID)
output_text_widget.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

browse_button = tk.Button(root, text="Open", command=browse_file, bd=1, relief=tk.SOLID)
browse_button.grid(row=0, column=0, padx=10, pady=5)

save_button = tk.Button(root, text="Save as", command=save_file, bd=1, relief=tk.SOLID)
save_button.grid(row=0, column=1, padx=10, pady=5)

GUI_button = tk.Button(root, text="Open debug GUI", command=open_gui, bd=1, relief=tk.SOLID)
GUI_button.grid(row=7, column=1, padx=10, pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)


if len(sys.argv) > 1:
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        code = file.read()
        input_text_widget.delete("1.0", tk.END)
        input_text_widget.insert(tk.END, code)


root.mainloop()
