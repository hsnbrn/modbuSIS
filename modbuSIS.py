import threading
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ipaddress
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import sys
import os

class ModbusScannerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ModbuSIS by OtomaSIS")

        # Pencere boyutunu ayarlama
        self.master.geometry("1000x600")
        self.master.resizable(False, False)

        # Grid yapılandırması
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(6, weight=0)

        # Subnet Label
        self.subnet_label = tk.Label(master, text="Subnet:")
        self.subnet_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        # Subnet Entry
        self.subnet_entry = tk.Entry(master, width=20)
        self.subnet_entry.insert(0, "192.168.1.0/24")
        self.subnet_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Local IP Label
        self.local_ip_label = tk.Label(master, text="Local IP:")
        self.local_ip_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        # Local IP Entry
        self.local_ip_entry = tk.Entry(master, width=20)
        self.local_ip_entry.insert(0, "192.168.1.10")
        self.local_ip_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Tara Button
        self.scan_button = tk.Button(master, text="Tara", command=self.start_scan, width=10)
        self.scan_button.grid(row=0, column=4, padx=2, pady=2, sticky="w")

        # Hakkında Butonu
        self.about_button = tk.Button(master, text="Hakkında", command=self.on_about, width=10)
        self.about_button.grid(row=0, column=5, padx=5, pady=5, sticky="e")

        # Sonuçlar alanı
        self.result_text = tk.Text(master, wrap="none", width=120, height=25)
        self.result_text.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # Scrollbars
        self.scrollbar_y = tk.Scrollbar(master, command=self.result_text.yview)
        self.scrollbar_y.grid(row=1, column=6, sticky='ns', pady=5)
        self.result_text['yscrollcommand'] = self.scrollbar_y.set

        self.scrollbar_x = tk.Scrollbar(master, orient='horizontal', command=self.result_text.xview)
        self.scrollbar_x.grid(row=2, column=0, columnspan=6, sticky='we', padx=5)
        self.result_text['xscrollcommand'] = self.scrollbar_x.set

        # Durum Çubuğu
        self.status_label = tk.Label(master, text="Hazır", fg="blue")
        self.status_label.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="w")

    def start_scan(self):
        threading.Thread(target=self.on_scan).start()

    def on_scan(self):
        subnet = self.subnet_entry.get().strip()
        local_ip = self.local_ip_entry.get().strip()
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, "Tarama başlıyor...\n")
        self.status_label.config(text="Taranıyor...")

        found_devices = []
        network = ipaddress.ip_network(subnet, strict=False)
        for ip in network.hosts():
            ip_str = str(ip)
            thread = threading.Thread(target=self.scan_ip, args=(ip_str, local_ip, found_devices))
            thread.start()
            thread.join(0.1)

        self.status_label.config(text=f"Tarama tamamlandı. {len(found_devices)} cihaz bulundu.")

    def scan_ip(self, ip_str, local_ip, found_devices):
        modbus_info = self.read_device_id(ip_str, local_ip)
        if modbus_info:
            self.result_text.insert(tk.END, f"Modbus Cihazı - IP: {ip_str}, Info: {modbus_info}\n")
            found_devices.append({"ip": ip_str, "info": modbus_info})

    def read_device_id(self, ip_str, local_ip, read_timeout=0.3, slave_id=1):
        client = ModbusTcpClient(
            host=ip_str,
            port=502,
            source_address=(local_ip, 0),
            timeout=read_timeout
        )
        device_info = None
        try:
            if client.connect():
                response = client.read_device_information(slave=slave_id)
                if not response.isError():
                    raw_info = response.information
                    decoded = {}
                    for obj_id, raw_data in raw_info.items():
                        try:
                            decoded[obj_id] = raw_data.decode(errors='ignore')
                        except:
                            decoded[obj_id] = str(raw_data)
                    device_info = decoded
        except Exception as e:
            print(f"{ip_str} için Modbus kontrol hatası: {e}")
        finally:
            client.close()
        return device_info

    def on_about(self):
        about_text = (
            "ModbuSIS by OtomaSIS v1.0\n\n"
            "Bu program, OtomaSIS Ltd. Şti. tarafından geliştirilmiştir.\n"
            "Lisans: GPL (Genel Kamu Lisansı) \n"
            "Yazılımı özgürce dağıtabilirsiniz.\n"
            "Yazılımın kodlarına GitHub üzerinden erişebilirsiniz. \n "
            "https://github.com/hsnbrn/modbuSIS"
        )
        messagebox.showinfo("Hakkında", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModbusScannerApp(root)
    root.mainloop()
