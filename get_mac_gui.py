import tkinter as tk
import uuid

def get_mac():
    # 获取本机MAC地址（格式化为常见的00-11-22-33-44-55）
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac_dash = "-".join([mac[i:i+2] for i in range(0, 12, 2)]).upper()
    mac_nodash = mac.upper()
    return mac_dash, mac_nodash

def copy_mac_nodash():
    mac = mac_nodash_var.get()
    root.clipboard_clear()
    root.clipboard_append(mac)
    status_var.set("已复制注册用格式到剪贴板！")

def copy_mac_dash():
    mac = mac_dash_var.get()
    root.clipboard_clear()
    root.clipboard_append(mac)
    status_var.set("已复制常规格式到剪贴板！")

root = tk.Tk()
root.title("本机MAC地址获取工具")
root.geometry("400x180")

mac_dash, mac_nodash = get_mac()
mac_dash_var = tk.StringVar(value=mac_dash)
mac_nodash_var = tk.StringVar(value=mac_nodash)
status_var = tk.StringVar(value="")

tk.Label(root, text="常规MAC地址（带横杠）：").pack(pady=(10,0))
mac_entry_dash = tk.Entry(root, textvariable=mac_dash_var, font=("Consolas", 14), width=25, justify="center")
mac_entry_dash.pack()
tk.Button(root, text="复制常规格式", command=copy_mac_dash).pack(pady=(2,8))

tk.Label(root, text="注册用MAC地址（无分隔符，大写）：").pack()
mac_entry_nodash = tk.Entry(root, textvariable=mac_nodash_var, font=("Consolas", 14), width=25, justify="center")
mac_entry_nodash.pack()
tk.Button(root, text="复制注册用格式", command=copy_mac_nodash).pack(pady=(2,8))

status_label = tk.Label(root, textvariable=status_var, fg="green")
status_label.pack()

root.mainloop()